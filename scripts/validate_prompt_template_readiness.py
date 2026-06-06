"""
BOSMAX Prompt Template Readiness Validator v1.

Checks that all required sample files exist and contain the correct coverage
for the readiness closure layer:
  A. Video single-block (BOSMAX, MWCB, ON_THE_FLY)
  B. Video multi-block (VEO_LITE 16/24, GROK 16/20)
  C. Batch single-block (BOSMAX, MWCB, ON_THE_FLY)
  D. Batch multi-block (declares child block output shape)
  E. Field alias map (CopyPack ID -> copywriting_id)
  F. Forbidden fields absent from beginner-facing templates

Exit code 0 = all checks passed.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]

SAMPLES_NOTION = ROOT / "samples" / "notion"
DOCS = ROOT / "docs"

SINGLE_BLOCK_FILE = SAMPLES_NOTION / "video_single_block_templates.yaml"
MULTI_BLOCK_FILE = SAMPLES_NOTION / "video_multi_block_templates.yaml"
BATCH_SINGLE_FILE = SAMPLES_NOTION / "batch_single_block_templates.yaml"
BATCH_MULTI_FILE = SAMPLES_NOTION / "batch_multi_block_templates.yaml"
READINESS_CONTRACT = DOCS / "prompt_template_readiness_contract_v1.md"
MULTIBLOCK_CONTRACT = DOCS / "batch_multiblock_output_contract_v1.md"

FORBIDDEN_FIELDS = {"hook", "usp", "usp_1", "usp_2", "usp_3", "cta"}
FORBIDDEN_LABELS = {"hook", "usp 1", "usp 2", "usp 3", "cta", "usp"}

_failures: list[str] = []


def fail(msg: str) -> None:
    _failures.append(msg)
    print(f"FAIL: {msg}")


def check(condition: bool, msg: str) -> None:
    if condition:
        print(f"PASS: {msg}")
    else:
        fail(msg)


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _has_forbidden_fields(data: Any, context: str = "") -> bool:
    """Recursively check that forbidden fields are absent."""
    if isinstance(data, dict):
        for key in data:
            key_lower = str(key).lower().strip()
            if key_lower in FORBIDDEN_FIELDS or key_lower in FORBIDDEN_LABELS:
                fail(f"Forbidden field '{key}' found in {context}")
                return True
            if _has_forbidden_fields(data[key], context=f"{context}.{key}"):
                return True
    elif isinstance(data, list):
        for i, item in enumerate(data):
            if _has_forbidden_fields(item, context=f"{context}[{i}]"):
                return True
    return False


# ─────────────────────────────────────────────────────────────────────────────
# CHECK 1 — Required sample files exist
# ─────────────────────────────────────────────────────────────────────────────

def check_files_exist() -> None:
    for path in [
        SINGLE_BLOCK_FILE,
        MULTI_BLOCK_FILE,
        BATCH_SINGLE_FILE,
        BATCH_MULTI_FILE,
        READINESS_CONTRACT,
        MULTIBLOCK_CONTRACT,
    ]:
        check(path.exists(), f"Required file exists: {path.relative_to(ROOT)}")


# ─────────────────────────────────────────────────────────────────────────────
# CHECK 2 — Video single-block has BOSMAX, MWCB, ON_THE_FLY
# ─────────────────────────────────────────────────────────────────────────────

def check_single_block_coverage() -> None:
    data = load_yaml(SINGLE_BLOCK_FILE)
    templates = data.get("templates") or []
    workflows = {str(t.get("product_workflow", "")).upper() for t in templates}
    check("BOSMAX_SERUM_STEALTH" in workflows,
          "video_single_block has BOSMAX_SERUM_STEALTH template")
    check("MWCB_DIRECT" in workflows,
          "video_single_block has MWCB_DIRECT template")
    check("ON_THE_FLY_SESSION_ONLY" in workflows,
          "video_single_block has ON_THE_FLY_SESSION_ONLY template")


# ─────────────────────────────────────────────────────────────────────────────
# CHECK 3 — Video multi-block has VEO_LITE 16/24 and GROK 16/20
# ─────────────────────────────────────────────────────────────────────────────

def check_multi_block_coverage() -> None:
    data = load_yaml(MULTI_BLOCK_FILE)
    templates = data.get("templates") or []

    def find(engine: str, total_s: str) -> bool:
        return any(
            str(t.get("engine", "")).upper() == engine.upper()
            and str(t.get("total_duration", "")) == total_s
            for t in templates
        )

    check(find("VEO_3_1_LITE", "16s"),
          "video_multi_block has VEO_3_1_LITE 16s template")
    check(find("VEO_3_1_LITE", "24s"),
          "video_multi_block has VEO_3_1_LITE 24s template")
    check(find("GROK", "16s"),
          "video_multi_block has GROK 16s template")
    check(find("GROK", "20s"),
          "video_multi_block has GROK 20s template")


# ─────────────────────────────────────────────────────────────────────────────
# CHECK 4 — Batch single-block has BOSMAX, MWCB, ON_THE_FLY
# ─────────────────────────────────────────────────────────────────────────────

def check_batch_single_block_coverage() -> None:
    data = load_yaml(BATCH_SINGLE_FILE)
    templates = data.get("batch_templates") or []
    workflows = {str(t.get("product_workflow", "")).upper() for t in templates}
    check("BOSMAX_SERUM_STEALTH" in workflows,
          "batch_single_block has BOSMAX_SERUM_STEALTH template")
    check("MWCB_DIRECT" in workflows,
          "batch_single_block has MWCB_DIRECT template")
    check("ON_THE_FLY_SESSION_ONLY" in workflows,
          "batch_single_block has ON_THE_FLY_SESSION_ONLY template")


# ─────────────────────────────────────────────────────────────────────────────
# CHECK 5 — Batch multi-block declares child block output shape
# ─────────────────────────────────────────────────────────────────────────────

def check_batch_multi_block_shape() -> None:
    data = load_yaml(BATCH_MULTI_FILE)
    status = str(data.get("implementation_status", "")).upper()
    check("CONTRACT_READY" in status,
          "batch_multi_block declares CONTRACT_READY implementation_status")

    templates = data.get("templates") or []
    check(len(templates) > 0,
          "batch_multi_block has at least one template")

    for t in templates:
        tid = t.get("template_id", "?")
        contracts = t.get("block_contracts") or []
        check(len(contracts) >= 2,
              f"batch_multi_block template {tid} has >= 2 block_contracts")

        for bc in contracts:
            bidx = bc.get("block_index", "?")
            prefix = f"batch_multi_block template {tid} block {bidx}"
            check("bridge_in_required" in bc,
                  f"{prefix} declares bridge_in_required")
            check("bridge_out_required" in bc,
                  f"{prefix} declares bridge_out_required")
            check("identity_reanchor_required" in bc,
                  f"{prefix} declares identity_reanchor_required")
            check("product_reanchor_required" in bc,
                  f"{prefix} declares product_reanchor_required")

        # Validate child row math
        batch_count = t.get("batch_count", 0)
        block_count = t.get("block_count", 0)
        exp_parent = t.get("expected_parent_rows", None)
        exp_child = t.get("expected_child_block_rows", None)
        if batch_count and block_count:
            if exp_parent is not None:
                check(int(exp_parent) == int(batch_count),
                      f"batch_multi_block template {tid} expected_parent_rows == batch_count")
            if exp_child is not None:
                check(int(exp_child) == int(batch_count) * int(block_count),
                      f"batch_multi_block template {tid} expected_child_block_rows == batch_count × block_count")


# ─────────────────────────────────────────────────────────────────────────────
# CHECK 6 — Field alias map exists and includes CopyPack ID -> copywriting_id
# ─────────────────────────────────────────────────────────────────────────────

def check_field_alias_map() -> None:
    content = READINESS_CONTRACT.read_text(encoding="utf-8")
    check("CopyPack ID" in content and "copywriting_id" in content,
          "readiness contract contains CopyPack ID -> copywriting_id alias mapping")
    check("avatar_pool_id" in content,
          "readiness contract contains avatar_pool_id alias")
    check("registry_writeback" in content,
          "readiness contract declares registry_writeback field")
    check("FORBIDDEN" in content,
          "readiness contract declares registry_writeback FORBIDDEN rule")


# ─────────────────────────────────────────────────────────────────────────────
# CHECK 7 — Manual Hook / USP / CTA absent from beginner-facing templates
# ─────────────────────────────────────────────────────────────────────────────

def check_no_forbidden_fields() -> None:
    for path in [SINGLE_BLOCK_FILE, BATCH_SINGLE_FILE, BATCH_MULTI_FILE]:
        data = load_yaml(path)
        had = _has_forbidden_fields(data, context=path.name)
        if not had:
            print(f"PASS: No forbidden fields (hook/USP/CTA) in {path.name}")


# ─────────────────────────────────────────────────────────────────────────────
# CHECK 8 — ON_THE_FLY has SESSION_ONLY_GENERATE
# ─────────────────────────────────────────────────────────────────────────────

def check_on_the_fly_session_only_generate() -> None:
    for path, key in [
        (SINGLE_BLOCK_FILE, "templates"),
        (BATCH_SINGLE_FILE, "batch_templates"),
    ]:
        data = load_yaml(path)
        templates = data.get(key) or []
        for t in templates:
            if str(t.get("product_workflow", "")).upper() == "ON_THE_FLY_SESSION_ONLY":
                check(
                    str(t.get("copywriting_mode", "")).upper() == "SESSION_ONLY_GENERATE",
                    f"{path.name}: ON_THE_FLY template has copywriting_mode=SESSION_ONLY_GENERATE",
                )


# ─────────────────────────────────────────────────────────────────────────────
# CHECK 9 — ON_THE_FLY has registry_writeback: FORBIDDEN
# ─────────────────────────────────────────────────────────────────────────────

def check_on_the_fly_registry_writeback_forbidden() -> None:
    for path, key in [
        (SINGLE_BLOCK_FILE, "templates"),
        (BATCH_SINGLE_FILE, "batch_templates"),
    ]:
        data = load_yaml(path)
        templates = data.get(key) or []
        for t in templates:
            if str(t.get("product_workflow", "")).upper() == "ON_THE_FLY_SESSION_ONLY":
                check(
                    str(t.get("registry_writeback", "")).upper() == "FORBIDDEN",
                    f"{path.name}: ON_THE_FLY template has registry_writeback=FORBIDDEN",
                )


# ─────────────────────────────────────────────────────────────────────────────
# CHECK 10 — Registered products use approved workflows only
# ─────────────────────────────────────────────────────────────────────────────

APPROVED_REGISTERED_WORKFLOWS = {"BOSMAX_SERUM_STEALTH", "MWCB_DIRECT"}
APPROVED_OTF_WORKFLOWS = {"ON_THE_FLY_SESSION_ONLY"}


def check_approved_workflows() -> None:
    all_approved = APPROVED_REGISTERED_WORKFLOWS | APPROVED_OTF_WORKFLOWS
    for path, key in [
        (SINGLE_BLOCK_FILE, "templates"),
        (BATCH_SINGLE_FILE, "batch_templates"),
        (BATCH_MULTI_FILE, "templates"),
    ]:
        if not path.exists():
            continue
        data = load_yaml(path)
        templates = data.get(key) or []
        for t in templates:
            wf = str(t.get("product_workflow", "")).upper()
            if wf:
                check(
                    wf in all_approved,
                    f"{path.name}: workflow '{wf}' is in approved workflow list",
                )


# ─────────────────────────────────────────────────────────────────────────────
# CHECK 11 — MWCB uses MWCB_TRAD_REMEDY_POOL_001
# ─────────────────────────────────────────────────────────────────────────────

def check_mwcb_pool() -> None:
    for path, key in [
        (SINGLE_BLOCK_FILE, "templates"),
        (BATCH_SINGLE_FILE, "batch_templates"),
        (BATCH_MULTI_FILE, "templates"),
    ]:
        if not path.exists():
            continue
        data = load_yaml(path)
        templates = data.get(key) or []
        for t in templates:
            if str(t.get("product_workflow", "")).upper() == "MWCB_DIRECT":
                pool = str(t.get("avatar_pool_id", ""))
                check(
                    pool == "MWCB_TRAD_REMEDY_POOL_001",
                    f"{path.name}: MWCB_DIRECT template uses MWCB_TRAD_REMEDY_POOL_001 (got '{pool}')",
                )


# ─────────────────────────────────────────────────────────────────────────────
# CHECK 12 — BOSMAX uses BOSMAX_MALE_STEALTH_POOL_001
# ─────────────────────────────────────────────────────────────────────────────

def check_bosmax_pool() -> None:
    for path, key in [
        (SINGLE_BLOCK_FILE, "templates"),
        (BATCH_SINGLE_FILE, "batch_templates"),
        (BATCH_MULTI_FILE, "templates"),
    ]:
        if not path.exists():
            continue
        data = load_yaml(path)
        templates = data.get(key) or []
        for t in templates:
            if str(t.get("product_workflow", "")).upper() == "BOSMAX_SERUM_STEALTH":
                pool = str(t.get("avatar_pool_id", ""))
                check(
                    pool == "BOSMAX_MALE_STEALTH_POOL_001",
                    f"{path.name}: BOSMAX_SERUM_STEALTH template uses BOSMAX_MALE_STEALTH_POOL_001 (got '{pool}')",
                )


# ─────────────────────────────────────────────────────────────────────────────
# CHECK 13 — Multi-block examples include bridge-in/out fields
# ─────────────────────────────────────────────────────────────────────────────

def check_multi_block_bridge_fields() -> None:
    for path, key in [
        (MULTI_BLOCK_FILE, "templates"),
        (BATCH_MULTI_FILE, "templates"),
    ]:
        if not path.exists():
            continue
        data = load_yaml(path)
        templates = data.get(key) or []
        for t in templates:
            tid = t.get("template_id", "?")
            blocks = t.get("blocks") or t.get("block_contracts") or []
            for b in blocks:
                bidx = b.get("block_index", "?")
                prefix = f"{path.name} template {tid} block {bidx}"
                check("bridge_in_required" in b,
                      f"{prefix} has bridge_in_required")
                check("bridge_out_required" in b,
                      f"{prefix} has bridge_out_required")


# ─────────────────────────────────────────────────────────────────────────────
# CHECK 14 — Multi-block examples include identity/product reanchor fields
# ─────────────────────────────────────────────────────────────────────────────

def check_multi_block_reanchor_fields() -> None:
    for path, key in [
        (MULTI_BLOCK_FILE, "templates"),
        (BATCH_MULTI_FILE, "templates"),
    ]:
        if not path.exists():
            continue
        data = load_yaml(path)
        templates = data.get(key) or []
        for t in templates:
            tid = t.get("template_id", "?")
            blocks = t.get("blocks") or t.get("block_contracts") or []
            for b in blocks:
                bidx = b.get("block_index", "?")
                prefix = f"{path.name} template {tid} block {bidx}"
                check("identity_reanchor_required" in b,
                      f"{prefix} has identity_reanchor_required")
                check("product_reanchor_required" in b,
                      f"{prefix} has product_reanchor_required")


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    print("=" * 70)
    print("BOSMAX Prompt Template Readiness Validator v1")
    print("=" * 70)

    print("\n[CHECK 1] Required sample files exist")
    check_files_exist()

    print("\n[CHECK 2] Video single-block workflow coverage")
    check_single_block_coverage()

    print("\n[CHECK 3] Video multi-block engine/duration coverage")
    check_multi_block_coverage()

    print("\n[CHECK 4] Batch single-block workflow coverage")
    check_batch_single_block_coverage()

    print("\n[CHECK 5] Batch multi-block child block output shape")
    check_batch_multi_block_shape()

    print("\n[CHECK 6] Field alias map (CopyPack ID -> copywriting_id)")
    check_field_alias_map()

    print("\n[CHECK 7] No forbidden fields in beginner-facing templates")
    check_no_forbidden_fields()

    print("\n[CHECK 8] ON_THE_FLY has SESSION_ONLY_GENERATE")
    check_on_the_fly_session_only_generate()

    print("\n[CHECK 9] ON_THE_FLY has registry_writeback: FORBIDDEN")
    check_on_the_fly_registry_writeback_forbidden()

    print("\n[CHECK 10] Registered products use approved workflows only")
    check_approved_workflows()

    print("\n[CHECK 11] MWCB uses MWCB_TRAD_REMEDY_POOL_001")
    check_mwcb_pool()

    print("\n[CHECK 12] BOSMAX uses BOSMAX_MALE_STEALTH_POOL_001")
    check_bosmax_pool()

    print("\n[CHECK 13] Multi-block examples include bridge-in/out fields")
    check_multi_block_bridge_fields()

    print("\n[CHECK 14] Multi-block examples include identity/product reanchor fields")
    check_multi_block_reanchor_fields()

    print("\n" + "=" * 70)
    if _failures:
        print(f"VALIDATION FAILED — {len(_failures)} check(s) failed:")
        for f in _failures:
            print(f"  ✗ {f}")
        sys.exit(1)
    else:
        print("VALIDATION PASSED — all readiness checks passed")
    print("=" * 70)


if __name__ == "__main__":
    main()
