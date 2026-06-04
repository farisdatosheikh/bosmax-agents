from __future__ import annotations

"""
BOSMAX G-05 validator — PRODUCT_TRUTH_GATE.

Checks:
  - products/_SCHEMA.yaml exists
  - All product YAML files are structurally complete (required fields)
  - All variants have a non-empty scale_anchor_descriptor starting with "EXACTLY"
  - STEALTH products use SCRIPT_REGISTRY dialogue authority (not freeform copywriting)
  - BOSMAX_SERUM scale anchors match expected physical references (lip balm / chapstick)
  - CAP_BURUNG_MINYAK scale anchor matches expected physical references (30ml glass bottle)
  - No forbidden drift terms appear in scale_anchor_descriptor for guarded products
  - product_status is a valid enumeration value
  - recommended_avatars resolve to existing avatar YAML files
  - named persona avatar files carry bidirectional assigned_products link back to the product
  - recommended_archetypes resolve to existing archetype YAML files (existence only)

Scope note:
  This validator covers the product registry layer (products/*.yaml, avatars/*.yaml).
  Multi-block prompt text drift and visual reference override remain runtime concerns
  and are documented as PARTIAL in kernel contract G-05.
"""

import sys
from pathlib import Path
from typing import Any

import yaml

# Ensure UTF-8 output on Windows regardless of console code page
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS_DIR = ROOT / "products"
AVATARS_DIR = ROOT / "avatars"
SCHEMA_PATH = PRODUCTS_DIR / "_SCHEMA.yaml"

VALID_STATUSES = {"Available", "Discontinued", "Draft"}
VALID_SILOS = {"STEALTH", "DIRECT", "LIFESTYLE", "SAVAGE_HPAS"}

PRODUCT_REQUIRED_FIELDS = ["product_id", "product_name", "brand", "product_status", "variants"]
VARIANT_REQUIRED_FIELDS = ["variant_id", "variant_name", "scale_anchor_descriptor"]

# Product-specific scale anchor guards — prevents AI drift on known flagship products
SCALE_ANCHOR_GUARDS: dict[str, dict[str, Any]] = {
    "BOSMAX_SERUM": {
        "5ML": {
            "must_contain": ["lip balm"],
            "forbidden_terms": ["perfume", "roll-on oil", "enlarged", "large bottle", "spray", "deodorant"],
        },
        "10ML": {
            "must_contain": ["chapstick"],
            "forbidden_terms": ["perfume", "roll-on oil", "enlarged", "large bottle", "spray", "pump", "deodorant"],
        },
    },
    "CAP_BURUNG_MINYAK": {
        "30ML_WG40_BOTTLE": {
            "must_contain_any": ["30ml", "30 ml", "glass", "rectangular", "pocket"],
            "forbidden_terms": ["tall", "wide bottle", "perfume", "serum", "dropper", "spray"],
        },
    },
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def discover_products() -> list[Path]:
    return sorted(
        p for p in PRODUCTS_DIR.glob("*.yaml")
        if p.name != "_SCHEMA.yaml"
    )


def validate_schema_exists() -> None:
    require(SCHEMA_PATH.exists(), f"products/_SCHEMA.yaml missing: {SCHEMA_PATH}")
    products = discover_products()
    require(len(products) > 0, f"No product YAML files found in {PRODUCTS_DIR}")


def validate_product_fields(product_id: str, data: dict[str, Any]) -> list[str]:
    checks: list[str] = []
    for field in PRODUCT_REQUIRED_FIELDS:
        require(field in data and data[field] is not None, f"Product {product_id} missing required field: {field!r}")
    require(
        isinstance(data["variants"], list) and len(data["variants"]) > 0,
        f"Product {product_id} has empty variants list",
    )
    checks.append(f"product_record ok: {product_id} ({len(data['variants'])} variant(s))")
    return checks


def validate_product_status(product_id: str, data: dict[str, Any]) -> list[str]:
    status = data.get("product_status", "")
    require(
        status in VALID_STATUSES,
        f"product_status invalid for {product_id}: {status!r} — must be one of {sorted(VALID_STATUSES)}",
    )
    return [f"product_status ok: {product_id} — {status}"]


def validate_variants(product_id: str, data: dict[str, Any]) -> list[str]:
    checks: list[str] = []
    for variant in data["variants"]:
        variant_id = variant.get("variant_id", "<unknown>")
        for field in VARIANT_REQUIRED_FIELDS:
            require(
                field in variant and variant[field],
                f"Variant {variant_id} in {product_id} missing required field: {field!r}",
            )
        scale = str(variant["scale_anchor_descriptor"]).strip()
        require(
            scale.upper().startswith("EXACTLY"),
            f"scale_anchor_descriptor does not start with 'EXACTLY' for {product_id}/{variant_id}: {scale!r}",
        )
        checks.append(f"scale_anchor ok: {product_id}/{variant_id}")
    return checks


def validate_scale_anchor_guards(product_id: str, data: dict[str, Any]) -> list[str]:
    checks: list[str] = []
    if product_id not in SCALE_ANCHOR_GUARDS:
        return checks
    guards = SCALE_ANCHOR_GUARDS[product_id]
    for variant in data["variants"]:
        variant_id = variant.get("variant_id", "")
        if variant_id not in guards:
            continue
        scale = str(variant.get("scale_anchor_descriptor", "")).lower()
        guard = guards[variant_id]

        if "must_contain" in guard:
            for term in guard["must_contain"]:
                require(
                    term.lower() in scale,
                    f"{product_id} {variant_id} scale drift — expected {term!r} in scale_anchor_descriptor, got: {scale!r}",
                )

        if "must_contain_any" in guard:
            any_match = any(term.lower() in scale for term in guard["must_contain_any"])
            require(
                any_match,
                f"{product_id} {variant_id} scale drift — expected one of {guard['must_contain_any']} in scale_anchor_descriptor, got: {scale!r}",
            )

        for term in guard.get("forbidden_terms", []):
            require(
                term.lower() not in scale,
                f"Drift term {term!r} found in scale_anchor_descriptor for {product_id}/{variant_id}: {scale!r}",
            )

        checks.append(f"scale_drift_guard ok: {product_id}/{variant_id}")
    return checks


def validate_stealth_compliance(product_id: str, data: dict[str, Any]) -> list[str]:
    checks: list[str] = []
    silo = str(data.get("silo", "")).upper()
    compliance_class = str(data.get("compliance_class", "")).upper()
    is_stealth = silo == "STEALTH" or "STEALTH" in compliance_class
    if not is_stealth:
        return checks

    dialogue_auth = data.get("dialogue_authority") or {}
    mode = str(dialogue_auth.get("mode", "")).upper()
    require(
        mode == "SCRIPT_REGISTRY",
        f"STEALTH product {product_id} must use dialogue_authority.mode SCRIPT_REGISTRY, found: {mode!r}",
    )
    for sub_field in ("registry_file", "variant_file", "silo_id"):
        val = str(dialogue_auth.get(sub_field, "")).strip()
        require(
            bool(val),
            f"STEALTH product {product_id} missing dialogue_authority.{sub_field}",
        )
    checks.append(f"stealth_silo ok: {product_id} — SCRIPT_REGISTRY")
    return checks


def validate_avatar_cross_references(product_id: str, data: dict[str, Any]) -> list[str]:
    checks: list[str] = []

    # named persona bidirectional check — only for recommended_avatars field
    recommended_avatars = data.get("recommended_avatars") or []
    for avatar_id in recommended_avatars:
        avatar_path = AVATARS_DIR / f"{avatar_id}.yaml"
        require(
            avatar_path.exists(),
            f"recommended_avatar {avatar_id!r} for {product_id} has no file in avatars/",
        )
        avatar_data = load_yaml(avatar_path)
        assigned = avatar_data.get("assigned_products") or []
        require(
            product_id in assigned,
            f"Avatar {avatar_id}.assigned_products does not include {product_id} "
            f"(broken bidirectional link) — found: {assigned}",
        )
        checks.append(f"bidirectional ok: {product_id} <-> {avatar_id}")

    # archetype existence check only — archetypes have no assigned_products
    # recommended_archetypes may be a flat list of IDs OR a nested dict
    # {primary: [{avatar_id: "..."}, ...], secondary: [...]} — flatten both shapes
    raw_archetypes = data.get("recommended_archetypes") or []
    archetype_ids: list[str] = []
    if isinstance(raw_archetypes, list):
        archetype_ids = [str(item) for item in raw_archetypes]
    elif isinstance(raw_archetypes, dict):
        for group in raw_archetypes.values():
            if isinstance(group, list):
                for entry in group:
                    if isinstance(entry, dict) and "avatar_id" in entry:
                        archetype_ids.append(str(entry["avatar_id"]))
                    elif isinstance(entry, str):
                        archetype_ids.append(entry)
    for archetype_id in archetype_ids:
        archetype_path = AVATARS_DIR / f"{archetype_id}.yaml"
        require(
            archetype_path.exists(),
            f"recommended_archetype {archetype_id!r} for {product_id} has no file in avatars/",
        )
        checks.append(f"archetype_ref ok: {product_id} → {archetype_id}")

    return checks


def _run_synthetic_drift_test() -> None:
    """Inline regression: confirm the scale guard rejects a known bad descriptor."""
    bad_scale = "EXACTLY perfume bottle size, sits in palm like a large spray"
    lower = bad_scale.lower()
    assert "perfume" in lower, "Synthetic drift test setup error"
    for term in SCALE_ANCHOR_GUARDS["BOSMAX_SERUM"]["5ML"]["forbidden_terms"]:
        if term.lower() in lower:
            return  # guard would fire correctly
    raise AssertionError("Scale drift guard did not detect 'perfume' in synthetic bad descriptor")


def main() -> None:
    _run_synthetic_drift_test()

    validate_schema_exists()
    products = discover_products()

    all_checks: list[str] = [
        f"Products registry: {PRODUCTS_DIR} ({len(products)} products)",
        f"Schema: {SCHEMA_PATH}",
    ]

    for product_path in products:
        data = load_yaml(product_path)
        product_id = data.get("product_id") or product_path.stem

        all_checks += validate_product_fields(product_id, data)
        all_checks += validate_product_status(product_id, data)
        all_checks += validate_variants(product_id, data)
        all_checks += validate_scale_anchor_guards(product_id, data)
        all_checks += validate_stealth_compliance(product_id, data)
        all_checks += validate_avatar_cross_references(product_id, data)

    print("VALIDATION PASSED")
    for item in all_checks:
        print(item)


if __name__ == "__main__":
    main()
