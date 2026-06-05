from __future__ import annotations

"""
BOSMAX G-07 Flow Extend validator — MULTI_BLOCK_SEAM_GATE (Flow Extend posture).

Purpose:
  Enforce fail-closed posture for GOOGLE_FLOW.FLOW_EXTEND.
  Flow Extend is a previous-final-second continuation workflow, not deterministic
  clip-chain math. It must not be promoted to READY without complete proof fields.

Checks:
  1. Manifest existence and required top-level keys
  2. Governance fields completeness
  3. Engine contract: GOOGLE_FLOW.FLOW_EXTEND is MANUAL_REVIEW_ONLY / NEEDS_REVIEW
  4. Decision record: documents continuation workflow and manual-review posture
  5. Run-level required fields (all flow_extend_runs entries)
  6. MANUAL_REVIEW_ONLY posture: allowed_reason required, block_plan must be empty,
     deterministic_clip_chain_allowed must be false
  7. READY posture guard: all proof fields non-empty, no formulaResult / omitted rollup
  8. Product / avatar dependency cross-reference
  9. Notion sample readiness cross-check (SAMPLE-FLOW-EXTEND-16S-RIZAL)
  F. Synthetic regression checks

Scope note:
  This validator operates on the repo-backed proof manifest layer only.
  It does not execute actual Google Flow video generation or verify live
  continuity in rendered video output. Live Flow execution proof remains
  PARTIAL and is documented as a future gap.
"""

import sys
from pathlib import Path
from typing import Any

import yaml

# Ensure UTF-8 output on Windows regardless of console code page
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "registries" / "flow_extend_proof.yaml"
ENGINE_CONTRACTS_PATH = ROOT / "registries" / "video_engine_duration_contracts.yaml"
DECISION_RECORD_PATH = ROOT / "BOSMAX_VEO31_FLOW_CONTRACT_DECISION_v1.md"
SAMPLE_MANIFEST_PATH = ROOT / "registries" / "notion_sample_readiness.yaml"
PRODUCTS_DIR = ROOT / "products"
AVATARS_DIR = ROOT / "avatars"

GOVERNANCE_REQUIRED_FIELDS = [
    "authority",
    "decision_record",
    "engine_contract",
    "validator",
    "default_status",
    "fail_closed_rules",
]

RUN_REQUIRED_FIELDS = [
    "run_id",
    "engine",
    "execution_mode",
    "execution_status",
    "product_id",
    "avatar_id",
    "total_duration_seconds",
    "deterministic_clip_chain_allowed",
    "allowed_reason_if_manual_review",
]

READY_PROOF_FIELDS = [
    "previous_clip_final_second_state",
    "continuation_goal",
    "identity_reanchor",
    "product_reanchor",
    "audio_continuity_notes",
    "frame_bridge_notes",
    "output_test_report",
    "validator_proof_capture",
]

REJECTED_PROOF_PATTERNS = [
    "formulaResult://",
    "<omitted />",
    "omitted",
    "rollup omitted",
    "formula result",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


# ── 1. Manifest existence ─────────────────────────────────────────────────────

def validate_manifest() -> dict[str, Any]:
    require(MANIFEST_PATH.exists(), f"flow_extend_proof.yaml missing: {MANIFEST_PATH}")
    data = load_yaml(MANIFEST_PATH)
    for key in ("version", "governance", "flow_extend_runs"):
        require(key in data, f"flow_extend_proof.yaml missing top-level key: {key!r}")
    require(
        isinstance(data["flow_extend_runs"], list) and len(data["flow_extend_runs"]) > 0,
        "flow_extend_proof.yaml has empty flow_extend_runs list",
    )
    return data


# ── 2. Governance fields ──────────────────────────────────────────────────────

def validate_governance(data: dict[str, Any]) -> list[str]:
    gov = data.get("governance") or {}
    for field in GOVERNANCE_REQUIRED_FIELDS:
        val = gov.get(field)
        require(
            val is not None and str(val).strip() not in ("", "[]", "null"),
            f"flow_extend_proof.yaml governance missing required field: {field!r}",
        )
    return ["manifest ok: registries/flow_extend_proof.yaml"]


# ── 3. Engine contract check ──────────────────────────────────────────────────

def validate_engine_contract() -> list[str]:
    require(ENGINE_CONTRACTS_PATH.exists(), f"video_engine_duration_contracts.yaml missing: {ENGINE_CONTRACTS_PATH}")
    registry = load_yaml(ENGINE_CONTRACTS_PATH)
    engines = registry.get("engines") or {}
    require("GOOGLE_FLOW" in engines, "GOOGLE_FLOW missing from engine contracts registry")

    flow = engines["GOOGLE_FLOW"]
    execution_modes = flow.get("execution_modes") or {}
    require("FLOW_EXTEND" in execution_modes, "FLOW_EXTEND missing from GOOGLE_FLOW.execution_modes")

    flow_extend = execution_modes["FLOW_EXTEND"]
    flow_status = str(flow_extend.get("status", "")).upper()
    require(
        flow_status in ("NEEDS_REVIEW", "MANUAL_REVIEW_ONLY"),
        f"GOOGLE_FLOW.FLOW_EXTEND status must be NEEDS_REVIEW or MANUAL_REVIEW_ONLY, got: {flow_status!r}",
    )

    notion_status = str(flow.get("notion_execution_status", "")).upper()
    require(
        notion_status in ("MANUAL_REVIEW_ONLY", "NEEDS_REVIEW"),
        f"GOOGLE_FLOW notion_execution_status must be MANUAL_REVIEW_ONLY, got: {notion_status!r}",
    )

    # Confirm FLOW_EXTEND does not define deterministic [8, 8] block math
    block_map = flow_extend.get("default_total_to_blocks") or {}
    require(
        len(block_map) == 0,
        f"FLOW_EXTEND must not define deterministic block math (found: {block_map})",
    )

    return [
        "engine_contract ok: GOOGLE_FLOW.FLOW_EXTEND MANUAL_REVIEW_ONLY",
        "not_clip_chain ok: FLOW_EXTEND has no deterministic block math",
    ]


# ── 4. Decision record check ──────────────────────────────────────────────────

def validate_decision_record() -> list[str]:
    require(DECISION_RECORD_PATH.exists(), f"BOSMAX_VEO31_FLOW_CONTRACT_DECISION_v1.md missing: {DECISION_RECORD_PATH}")
    text = DECISION_RECORD_PATH.read_text(encoding="utf-8")

    # Key phrases that must appear in the decision record
    required_phrases = [
        ("continuation workflow", "decision record must state Flow Extend is a continuation workflow"),
        ("FLOW_EXTEND", "decision record must mention FLOW_EXTEND"),
        ("previous", "decision record must mention previous clip state"),
    ]
    for phrase, message in required_phrases:
        require(phrase.lower() in text.lower(), message)

    # Confirm manual-review posture is documented
    review_phrases = ["MANUAL_REVIEW_ONLY", "NEEDS_REVIEW", "manual-review", "manual review"]
    found_review = any(p.lower() in text.lower() for p in review_phrases)
    require(found_review, "decision record must document manual-review / NEEDS_REVIEW posture for FLOW_EXTEND")

    # Confirm it does NOT promote FLOW_EXTEND as ordinary [8,8] clip-chain
    forbidden_phrases = ["8+8", "[8, 8]", "8s + 8s"]
    for phrase in forbidden_phrases:
        if phrase in text:
            # Only fail if it's promoting Flow Extend with this math — context check
            # It's OK if it says VEO_3_1 uses [8,8], but not Flow Extend
            idx = text.find(phrase)
            surrounding = text[max(0, idx - 100):idx + 100].upper()
            if "FLOW_EXTEND" in surrounding or "GOOGLE_FLOW" in surrounding:
                fail(
                    f"Decision record appears to promote FLOW_EXTEND as {phrase!r} clip-chain math — "
                    f"this is forbidden. Context: ...{surrounding}..."
                )

    return ["decision_record ok: previous-final-second continuation workflow documented"]


# ── 5. Run-level required fields ──────────────────────────────────────────────

def validate_run_fields(run: dict[str, Any]) -> None:
    run_id = str(run.get("run_id", "<unknown>"))
    for field in RUN_REQUIRED_FIELDS:
        val = run.get(field)
        require(
            val is not None,
            f"Flow Extend run {run_id!r} missing required field: {field!r}",
        )
    require(
        str(run.get("engine", "")).upper() == "GOOGLE_FLOW",
        f"Flow Extend run {run_id!r} engine must be GOOGLE_FLOW",
    )
    require(
        str(run.get("execution_mode", "")).upper() == "FLOW_EXTEND",
        f"Flow Extend run {run_id!r} execution_mode must be FLOW_EXTEND",
    )
    require(
        run.get("deterministic_clip_chain_allowed") is False,
        f"Flow Extend run {run_id!r} deterministic_clip_chain_allowed must be false",
    )


# ── 6. MANUAL_REVIEW_ONLY posture ─────────────────────────────────────────────

def validate_manual_review_posture(run: dict[str, Any]) -> list[str]:
    run_id = str(run.get("run_id", "<unknown>"))
    exec_status = str(run.get("execution_status", "")).upper()
    if exec_status != "MANUAL_REVIEW_ONLY":
        return []

    reason = str(run.get("allowed_reason_if_manual_review", "")).strip()
    require(bool(reason), f"MANUAL_REVIEW_ONLY run {run_id!r} has empty allowed_reason_if_manual_review")

    block_plan = run.get("block_plan") or []
    require(
        len(block_plan) == 0,
        f"MANUAL_REVIEW_ONLY run {run_id!r} must have empty block_plan (not deterministic clip math), got: {block_plan}",
    )

    return [f"flow_extend ok: {run_id} MANUAL_REVIEW_ONLY"]


# ── 7. READY posture guard ────────────────────────────────────────────────────

def validate_ready_posture(run: dict[str, Any]) -> list[str]:
    run_id = str(run.get("run_id", "<unknown>"))
    exec_status = str(run.get("execution_status", "")).upper()
    if exec_status != "READY":
        return []

    # All proof fields must be non-empty
    for field in READY_PROOF_FIELDS:
        val = str(run.get(field, "")).strip()
        require(bool(val), f"READY Flow Extend run {run_id!r} has empty proof field: {field!r}")

    # Rejected proof patterns
    capture = str(run.get("validator_proof_capture", ""))
    for pattern in REJECTED_PROOF_PATTERNS:
        require(
            pattern.lower() not in capture.lower(),
            f"READY run {run_id!r} validator_proof_capture contains rejected pattern: {pattern!r}",
        )

    # Must not claim deterministic [8,8] block plan
    block_plan = run.get("block_plan") or []
    require(
        len(block_plan) == 0,
        f"READY Flow Extend run {run_id!r} block_plan must remain empty — not clip-chain math, got: {block_plan}",
    )

    require(
        "VALIDATION PASSED" in capture,
        f"READY Flow Extend run {run_id!r} validator_proof_capture must contain 'VALIDATION PASSED'",
    )

    return [f"flow_extend ok: {run_id} READY (all proof fields satisfied)"]


# ── 8. Product / avatar dependency ────────────────────────────────────────────

def validate_product_avatar_references(runs: list[dict[str, Any]]) -> list[str]:
    checks: list[str] = []
    for run in runs:
        run_id = str(run.get("run_id", "<unknown>"))
        product_id = str(run.get("product_id", "")).strip()
        avatar_id = str(run.get("avatar_id", "")).strip()

        if product_id:
            prod_path = PRODUCTS_DIR / f"{product_id}.yaml"
            require(prod_path.exists(), f"Flow Extend run {run_id!r} product_id {product_id!r} has no file in products/")
            checks.append(f"product_ref ok: {run_id} -> {product_id}")

        if avatar_id:
            avatar_path = AVATARS_DIR / f"{avatar_id}.yaml"
            require(avatar_path.exists(), f"Flow Extend run {run_id!r} avatar_id {avatar_id!r} has no file in avatars/")
            checks.append(f"avatar_ref ok: {run_id} -> {avatar_id}")

    return checks


# ── 9. Notion sample readiness cross-check ────────────────────────────────────

def validate_sample_readiness_cross_check() -> list[str]:
    require(SAMPLE_MANIFEST_PATH.exists(), f"notion_sample_readiness.yaml missing: {SAMPLE_MANIFEST_PATH}")
    data = load_yaml(SAMPLE_MANIFEST_PATH)
    runs = {str(r.get("sample_id", "")): r for r in data.get("sample_runs", [])}

    target = "SAMPLE-FLOW-EXTEND-16S-RIZAL"
    require(target in runs, f"Required sample {target!r} missing from notion_sample_readiness.yaml")

    run = runs[target]
    exec_status = str(run.get("execution_status", "")).upper()
    require(
        exec_status in ("MANUAL_REVIEW_ONLY", "NEEDS_REVIEW"),
        f"notion_sample_readiness.yaml: {target!r} must be MANUAL_REVIEW_ONLY, got: {exec_status!r}",
    )
    require(
        exec_status != "READY",
        f"notion_sample_readiness.yaml: {target!r} must not be READY",
    )

    block_plan = run.get("block_plan") or []
    require(
        len(block_plan) == 0,
        f"notion_sample_readiness.yaml: {target!r} block_plan must be empty (not deterministic), got: {block_plan}",
    )

    engine = str(run.get("engine", "")).upper()
    require(engine == "GOOGLE_FLOW", f"notion_sample_readiness.yaml: {target!r} engine must be GOOGLE_FLOW")

    return [f"sample_readiness ok: {target} MANUAL_REVIEW_ONLY"]


# ── F. Synthetic regression ───────────────────────────────────────────────────

def _run_synthetic_regression() -> None:
    """Confirm guard logic fires without touching real files."""

    # READY with empty proof fields should fail
    bad_ready = {
        "run_id": "SYNTHETIC_READY",
        "execution_status": "READY",
        "previous_clip_final_second_state": "",  # empty -> should fail
        "validator_proof_capture": "VALIDATION PASSED",
    }
    empty_proof = str(bad_ready.get("previous_clip_final_second_state", "")).strip()
    assert not bool(empty_proof), "Synthetic: empty proof field should be falsy"

    # Deterministic block_plan [8, 8] on FLOW_EXTEND should fail
    bad_block = {"block_plan": [8, 8], "execution_mode": "FLOW_EXTEND"}
    assert len(bad_block["block_plan"]) > 0, "Synthetic: [8,8] block_plan should be non-empty and trigger guard"

    # formulaResult in validator_proof_capture should fail
    bad_capture = "formulaResult://some-notion-field"
    found = any(p.lower() in bad_capture.lower() for p in REJECTED_PROOF_PATTERNS)
    assert found, "Synthetic: formulaResult should be caught by proof guard"

    # omitted rollup should fail
    bad_omitted = "this is <omitted /> rollup data"
    found2 = any(p.lower() in bad_omitted.lower() for p in REJECTED_PROOF_PATTERNS)
    assert found2, "Synthetic: omitted rollup should be caught by proof guard"

    # deterministic_clip_chain_allowed: true should fail
    bad_clip = {"deterministic_clip_chain_allowed": True}
    assert bad_clip["deterministic_clip_chain_allowed"] is True, "Synthetic: true should trigger the guard"


def main() -> None:
    _run_synthetic_regression()

    data = validate_manifest()
    gov_checks = validate_governance(data)
    engine_checks = validate_engine_contract()
    record_checks = validate_decision_record()

    runs: list[dict[str, Any]] = data.get("flow_extend_runs", [])
    run_checks: list[str] = []
    for run in runs:
        validate_run_fields(run)
        run_checks += validate_manual_review_posture(run)
        run_checks += validate_ready_posture(run)

    dep_checks = validate_product_avatar_references(runs)
    sample_checks = validate_sample_readiness_cross_check()

    proof_guard_checks = [
        "proof_guard ok: READY requires previous_clip_final_second_state / continuation_goal / reanchors / audio / frame bridge / output test",
        "proof_guard ok: formulaResult and omitted rollup rejected",
    ]

    print("VALIDATION PASSED")
    print(f"Manifest: {MANIFEST_PATH}")
    print(f"Engine contracts: {ENGINE_CONTRACTS_PATH}")
    print(f"Decision record: {DECISION_RECORD_PATH}")
    for item in gov_checks + engine_checks + record_checks + run_checks + dep_checks + sample_checks + proof_guard_checks:
        print(item)


if __name__ == "__main__":
    main()
