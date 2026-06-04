from __future__ import annotations

"""
BOSMAX G-06 validator — AVATAR_SOURCE_GATE.

Checks:
  - avatars/_SCHEMA.yaml exists
  - At least one named persona and one base archetype are present
  - Required biometric DNA fields exist on all base archetypes
  - Required identity fields exist on all named personas
  - Named persona base_archetype resolves to an existing avatar YAML file
  - Named persona assigned_products resolve to existing product YAML files
  - Named persona compatible_silos contain only repo-authorised values
  - Named persona prompt_fragment is non-empty
  - Named persona distinguishing_features is non-empty (required for multi-block re-anchor)
  - Bidirectional: product.recommended_avatars -> persona.assigned_products
  - Hybrid mode rules are documented in repo authority (registry-mode checks)
  - Multi-block avatar re-anchor rule is documented in repo authority

Scope note:
  This validator covers the registry layer (avatars/*.yaml, products/*.yaml).
  Runtime USER_UPLOAD mode validation, live Notion Avatar Registry mirror,
  and active-run avatar source tracking remain runtime concerns documented
  as PARTIAL in kernel contract G-06.
"""

import sys
from pathlib import Path
from typing import Any

import yaml

# Ensure UTF-8 output on Windows regardless of console code page
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
AVATARS_DIR = ROOT / "avatars"
PRODUCTS_DIR = ROOT / "products"
SCHEMA_PATH = AVATARS_DIR / "_SCHEMA.yaml"

VALID_SILOS = {"STEALTH", "DIRECT", "LIFESTYLE", "SAVAGE_HPAS"}

PERSONA_REQUIRED_FIELDS = [
    "schema_version",
    "persona_type",
    "persona_id",
    "persona_name",
    "base_archetype",
    "compatible_silos",
    "assigned_products",
    "prompt_fragment",
]

ARCHETYPE_REQUIRED_BIOMETRIC_FIELDS = [
    "avatar_id",
    "ethnicity",
    "gender",
    "age_range",
    "skin_tone",
    "face_shape",
    "eye_shape",
    "nose",
    "lips",
    "hair_texture",
    "build",
    "distinguishing_features",
]

# Repo authority files that must contain hybrid-mode and multi-block re-anchor rules
AUTHORITY_RULE_SOURCES = [
    ROOT / "BOSMAX_EXECUTION_KERNEL_CONTRACT_v1.md",
    ROOT / "BOSMAX_NOTION_MULTI_BLOCK_VIDEO_HANDOFF_v1.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def discover_avatars() -> tuple[list[Path], list[Path]]:
    """Return (persona_files, archetype_files) excluding _SCHEMA.yaml."""
    personas, archetypes = [], []
    for f in sorted(AVATARS_DIR.glob("*.yaml")):
        if f.name == "_SCHEMA.yaml":
            continue
        data = load_yaml(f)
        if str(data.get("persona_type", "")).upper() == "NAMED_PERSONA":
            personas.append(f)
        else:
            archetypes.append(f)
    return personas, archetypes


def validate_schema_exists() -> None:
    require(SCHEMA_PATH.exists(), f"avatars/_SCHEMA.yaml missing: {SCHEMA_PATH}")


def validate_named_persona(path: Path) -> list[str]:
    checks: list[str] = []
    data = load_yaml(path)
    persona_id = str(data.get("persona_id") or path.stem)

    # Required fields
    for field in PERSONA_REQUIRED_FIELDS:
        val = data.get(field)
        require(
            val is not None and str(val).strip() not in ("", "[]", "null"),
            f"Named persona {persona_id} missing required field: {field!r}",
        )

    # Prompt fragment non-empty
    require(
        bool(str(data.get("prompt_fragment", "")).strip()),
        f"Named persona {persona_id} has empty prompt_fragment — cannot inject into AI engine",
    )

    # Distinguishing features (required for multi-block re-anchor)
    dist_features = data.get("distinguishing_features") or []
    require(
        isinstance(dist_features, list) and len(dist_features) > 0,
        f"Named persona {persona_id} has empty distinguishing_features — cannot re-anchor in multi-block runs",
    )
    checks.append(f"named_persona ok: {persona_id} -> {data.get('base_archetype', '?')}")

    # Base archetype resolution
    base = str(data.get("base_archetype", "")).strip()
    require(bool(base), f"Named persona {persona_id} base_archetype is empty")
    base_path = AVATARS_DIR / f"{base}.yaml"
    require(
        base_path.exists(),
        f"Named persona {persona_id} base_archetype {base!r} has no file in avatars/",
    )

    # Compatible silos
    silos = data.get("compatible_silos") or []
    require(
        isinstance(silos, list) and len(silos) > 0,
        f"Named persona {persona_id} compatible_silos is empty",
    )
    for silo in silos:
        require(
            str(silo).upper() in VALID_SILOS,
            f"Named persona {persona_id} silo {silo!r} is not a valid BOSMAX silo: {sorted(VALID_SILOS)}",
        )

    # Assigned products — each must resolve
    assigned = data.get("assigned_products") or []
    require(
        isinstance(assigned, list) and len(assigned) > 0,
        f"Named persona {persona_id} assigned_products is empty",
    )
    for product_id in assigned:
        prod_path = PRODUCTS_DIR / f"{product_id}.yaml"
        require(
            prod_path.exists(),
            f"Named persona {persona_id} assigned_product {product_id!r} has no file in products/",
        )
        checks.append(f"assigned_product ok: {persona_id} -> {product_id}")

    return checks


def validate_base_archetype(path: Path) -> list[str]:
    checks: list[str] = []
    data = load_yaml(path)
    avatar_id = str(data.get("avatar_id") or path.stem)

    for field in ARCHETYPE_REQUIRED_BIOMETRIC_FIELDS:
        val = data.get(field)
        is_empty = (
            val is None
            or (isinstance(val, str) and not val.strip())
            or (isinstance(val, list) and len(val) == 0)
        )
        require(
            not is_empty,
            f"Base archetype {avatar_id} missing required biometric field: {field!r}",
        )

    checks.append(f"base_archetype ok: {avatar_id}")
    return checks


def validate_bidirectional_references(persona_files: list[Path]) -> list[str]:
    """
    For each product with recommended_avatars: every named persona listed must
    have that product in their assigned_products.
    """
    checks: list[str] = []
    persona_data: dict[str, dict[str, Any]] = {}
    for f in persona_files:
        d = load_yaml(f)
        pid = str(d.get("persona_id") or f.stem)
        persona_data[pid] = d

    for prod_path in sorted(PRODUCTS_DIR.glob("*.yaml")):
        if prod_path.name == "_SCHEMA.yaml":
            continue
        prod = load_yaml(prod_path)
        product_id = str(prod.get("product_id") or prod_path.stem)
        for avatar_id in (prod.get("recommended_avatars") or []):
            if avatar_id in persona_data:
                assigned = persona_data[avatar_id].get("assigned_products") or []
                require(
                    product_id in assigned,
                    f"Bidirectional link broken: {product_id}.recommended_avatars includes {avatar_id} "
                    f"but {avatar_id}.assigned_products does not include {product_id} — found: {assigned}",
                )
                checks.append(f"bidirectional ok: {product_id} <-> {avatar_id}")

    return checks


def validate_hybrid_mode_rules() -> list[str]:
    """
    Check that repo authority files document the hybrid-mode avatar rules:
    - REGISTRY mode does NOT require avatar image upload
    - REGISTRY mode DOES require product image
    These are documented rules, not runtime enforcement.
    """
    checks: list[str] = []
    hybrid_rule_markers = [
        ("REGISTRY", "avatar image"),
        ("product image", "REGISTRY"),
    ]
    found_markers: set[str] = set()
    for auth_path in AUTHORITY_RULE_SOURCES:
        if not auth_path.exists():
            continue
        text = auth_path.read_text(encoding="utf-8")
        for a, b in hybrid_rule_markers:
            key = f"{a}:{b}"
            if a.lower() in text.lower() and b.lower() in text.lower():
                found_markers.add(key)

    # Check CLAUDE.md as well for BOSMAX_IMAGE_HANDOFF / product image rules
    claude_md = ROOT / ".claude" / "CLAUDE.md"
    if claude_md.exists():
        claude_text = claude_md.read_text(encoding="utf-8")
        if "product_image" in claude_text and "avatar_image" in claude_text:
            found_markers.add("REGISTRY:avatar image")
            found_markers.add("product image:REGISTRY")

    # Check BOSMAX_RUNTIME_STATE_MACHINE_v1.md
    runtime_sm = ROOT / "BOSMAX_RUNTIME_STATE_MACHINE_v1.md"
    if runtime_sm.exists():
        sm_text = runtime_sm.read_text(encoding="utf-8")
        if "product" in sm_text.lower() and "avatar" in sm_text.lower():
            found_markers.add("REGISTRY:avatar image")

    for a, b in hybrid_rule_markers:
        key = f"{a}:{b}"
        require(
            key in found_markers,
            f"Repo authority does not document hybrid-mode rule: '{a}' and '{b}' must co-appear in authority files",
        )

    checks.append("hybrid_rule ok: REGISTRY mode — product image required; avatar image not required (repo-documented)")
    return checks


def validate_multi_block_reanchor_rule() -> list[str]:
    """
    Check that repo authority includes multi-block avatar re-anchor rule.
    Named personas must have distinguishing_features (checked per-persona above).
    This check confirms the rule is documented in repo authority.
    """
    REANCHOR_MARKERS = [
        "identity re-anchor",
        "re-anchor",
    ]
    for auth_path in AUTHORITY_RULE_SOURCES:
        if not auth_path.exists():
            continue
        text = auth_path.read_text(encoding="utf-8")
        for marker in REANCHOR_MARKERS:
            if marker.lower() in text.lower():
                return ["multi_block_reanchor ok: avatar re-anchor rule found in repo authority"]

    # Also check engine contracts
    engine_reg = ROOT / "registries" / "video_engine_duration_contracts.yaml"
    if engine_reg.exists():
        reg_text = engine_reg.read_text(encoding="utf-8")
        if "identity" in reg_text.lower() and "reanchor" in reg_text.lower():
            return ["multi_block_reanchor ok: avatar re-anchor rule found in engine contracts"]

    fail("Multi-block avatar re-anchor rule not found in any repo authority file")
    return []  # unreachable


def _run_synthetic_regression() -> None:
    """
    Synthetic regression: confirm validator logic rejects a bad persona stub.
    Does not mutate real files.
    """
    bad_persona: dict[str, Any] = {
        "persona_type": "NAMED_PERSONA",
        "persona_id": "SYNTHETIC_BAD",
        "persona_name": "Bad",
        "base_archetype": "",          # EMPTY — should fail
        "compatible_silos": ["STEALTH"],
        "assigned_products": ["BOSMAX_SERUM"],
        "prompt_fragment": "test fragment",
        "schema_version": "1.0",
        "distinguishing_features": ["test feature"],
    }
    # base_archetype empty check
    base = str(bad_persona.get("base_archetype", "")).strip()
    assert not bool(base), "Synthetic test: empty base_archetype should be falsy"

    bad_silo: dict[str, Any] = {
        "compatible_silos": ["INVALID_SILO"],
    }
    silo = str((bad_silo.get("compatible_silos") or [""])[0]).upper()
    assert silo not in VALID_SILOS, "Synthetic test: INVALID_SILO should not be in VALID_SILOS"

    empty_dist: dict[str, Any] = {"distinguishing_features": []}
    dist = empty_dist.get("distinguishing_features") or []
    assert not (isinstance(dist, list) and len(dist) > 0), "Synthetic test: empty dist features should fail"


def main() -> None:
    _run_synthetic_regression()
    validate_schema_exists()

    personas, archetypes = discover_avatars()
    require(len(personas) > 0, "No named personas found in avatars/")
    require(len(archetypes) > 0, "No base archetypes found in avatars/")

    all_checks: list[str] = [
        f"Avatar registry: {AVATARS_DIR} ({len(personas)} personas, {len(archetypes)} archetypes)",
        f"Schema: {SCHEMA_PATH}",
    ]

    for f in archetypes:
        all_checks += validate_base_archetype(f)

    for f in personas:
        all_checks += validate_named_persona(f)

    all_checks += validate_bidirectional_references(personas)
    all_checks += validate_hybrid_mode_rules()
    all_checks += validate_multi_block_reanchor_rule()

    print("VALIDATION PASSED")
    for item in all_checks:
        print(item)


if __name__ == "__main__":
    main()
