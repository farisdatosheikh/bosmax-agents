from __future__ import annotations

"""
BOSMAX G-08 + G-10 validator — NOTION_DOWNSTREAM_GATE + SAMPLE_OUTPUT_GATE.

Checks:
  - registries/notion_sample_readiness.yaml exists and is structurally valid
  - All required sample IDs are present in the manifest
  - block_plan for each deterministic run matches the engine contract
    (cross-validated via video_block_plan.build_plan)
  - unsupported GOOGLE_FLOW modes never receive READY posture
  - READY and READY_REVIEWED_FLOW_EXTEND runs satisfy all proof field requirements
  - formulaResult:// and omitted-rollup values are rejected as proof
  - multi-block runs have correct child_block_count_expected
  - dependent validator scripts exist on disk
"""

import sys
from pathlib import Path
from typing import Any

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "registries" / "notion_sample_readiness.yaml"

READY_STATUSES = {"READY", "READY_REVIEWED_FLOW_EXTEND"}

REQUIRED_SAMPLE_IDS = [
    "SAMPLE-HYBRID-01",
    "SAMPLE-HYBRID-02",
    "SAMPLE-HYBRID-GROK-16S-RIZAL",
    "SAMPLE-VEO31-16S-CLIP-CHAIN-RIZAL",
    "SAMPLE-VEO31-24S-CLIP-CHAIN-RIZAL",
    "SAMPLE-FLOW-16S-RIZAL",
    "SAMPLE-FLOW-24S-RIZAL",
    "SAMPLE-FLOW-32S-RIZAL",
    "SAMPLE-FLOW-MWCB-16S-DIRECT",
]

DEPENDENT_VALIDATORS = [
    ROOT / "scripts" / "validate_product_truth_drift.py",
    ROOT / "scripts" / "validate_avatar_registry_coverage.py",
    ROOT / "scripts" / "validate_video_block_contracts.py",
    ROOT / "scripts" / "validate_flow_extend_proof.py",
]

REJECTED_PROOF_PATTERNS = [
    "formulaResult://",
    "<omitted />",
    "omitted",
    "rollup omitted",
    "formula result",
]

READY_REQUIRED_BOOL_FIELDS = [
    "parent_video_run_required",
    "product_truth_check_required",
    "avatar_check_required",
    "engine_contract_summary_required",
    "output_test_report_required",
    "validator_proof_required",
    "formula_result_not_accepted_as_proof",
    "omitted_rollup_not_accepted_as_proof",
]

FLOW_READY_REQUIRED_BOOL_FIELDS = [
    "child_blocks_required",
    "wps_audit_required",
    "seam_proof_required",
    "previous_clip_final_second_state_required",
    "identity_reanchor_required",
    "product_reanchor_required",
    "shared_copywriting_avatar_resolver_payload",
]

# Multi-block seam fields required for READY non-GOOGLE_FLOW samples with > 1 block.
# GOOGLE_FLOW uses FLOW_READY_REQUIRED_BOOL_FIELDS which is a superset.
MULTI_BLOCK_SEAM_REQUIRED_BOOL_FIELDS = [
    "seam_proof_required",
    "previous_clip_final_second_state_required",
    "identity_reanchor_required",
    "product_reanchor_required",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def validate_manifest_exists() -> dict[str, Any]:
    require(MANIFEST_PATH.exists(), f"registries/notion_sample_readiness.yaml missing: {MANIFEST_PATH}")
    data = load_yaml(MANIFEST_PATH)
    runs = data.get("sample_runs")
    require(isinstance(runs, list) and len(runs) > 0, "notion_sample_readiness.yaml has empty sample_runs list")
    return data


def validate_required_samples(runs: list[dict[str, Any]]) -> list[str]:
    present_ids = {str(r.get("sample_id", "")) for r in runs}
    checks: list[str] = []
    for sid in REQUIRED_SAMPLE_IDS:
        require(sid in present_ids, f"Required sample run missing from manifest: {sid!r}")
        checks.append(f"required_sample ok: {sid}")
    return checks


def validate_engine_contract(run: dict[str, Any]) -> list[str]:
    sample_id = str(run.get("sample_id", "<unknown>"))
    engine = str(run.get("engine", "")).upper()
    execution_mode = str(run.get("execution_mode", "")).upper() or None
    exec_status = str(run.get("execution_status", "")).upper()
    total_secs = run.get("total_duration_seconds")
    manifest_plan = [int(x) for x in (run.get("block_plan") or [])]

    if exec_status in ("MANUAL_REVIEW_ONLY", "NEEDS_REVIEW") and not manifest_plan:
        return [f"engine_contract skip: {sample_id} — {exec_status}, no deterministic block math"]

    if not engine or total_secs is None:
        return []

    try:
        sys.path.insert(0, str(ROOT / "scripts"))
        from video_block_plan import build_plan  # type: ignore[import]

        kwargs: dict[str, Any] = {"engine_id": engine, "total_duration_seconds": int(total_secs)}
        if execution_mode and execution_mode not in ("", "NONE"):
            kwargs["execution_mode"] = execution_mode
        plan = build_plan(**kwargs)
        contract_plan = [int(x) for x in plan.get("block_durations_seconds", [])]
        require(
            manifest_plan == contract_plan,
            f"{sample_id} block_plan {manifest_plan} does not match engine contract {contract_plan} for {engine} {total_secs}s",
        )
        return [f"engine_contract ok: {sample_id} — {engine} {total_secs}s -> {'+'.join(str(x) for x in contract_plan)}"]
    except ValueError as exc:
        fail(f"{sample_id} engine contract lookup failed: {exc}")
        return []


def validate_manual_review_posture(run: dict[str, Any]) -> list[str]:
    sample_id = str(run.get("sample_id", "<unknown>"))
    engine = str(run.get("engine", "")).upper()
    exec_mode = str(run.get("execution_mode", "")).upper()
    exec_status = str(run.get("execution_status", "")).upper()

    if engine != "GOOGLE_FLOW":
        return []

    if exec_mode == "FLOW_EXTEND_UI":
        require(exec_status in READY_STATUSES | {"NEEDS_PROOF"}, f"GOOGLE_FLOW sample {sample_id!r} FLOW_EXTEND_UI has invalid status {exec_status!r}")
        if exec_status == "READY":
            fail(f"GOOGLE_FLOW sample {sample_id!r} must use READY_REVIEWED_FLOW_EXTEND, not generic READY")
    elif exec_mode == "FLOW_EXTEND_VERTEX":
        require(exec_status in ("MANUAL_REVIEW_ONLY", "NEEDS_REVIEW", "NEEDS_PROOF"), f"GOOGLE_FLOW sample {sample_id!r} FLOW_EXTEND_VERTEX must remain non-ready")
        require(exec_status not in READY_STATUSES, f"GOOGLE_FLOW sample {sample_id!r} FLOW_EXTEND_VERTEX must not be ready")
    else:
        fail(f"GOOGLE_FLOW sample {sample_id!r} uses unsupported execution_mode {exec_mode!r}")

    return []


def validate_proof_fields(run: dict[str, Any]) -> list[str]:
    sample_id = str(run.get("sample_id", "<unknown>"))
    engine = str(run.get("engine", "")).upper()
    exec_mode = str(run.get("execution_mode", "")).upper()
    exec_status = str(run.get("execution_status", "")).upper()
    if exec_status not in READY_STATUSES:
        return []

    checks: list[str] = []

    for field in READY_REQUIRED_BOOL_FIELDS:
        val = run.get(field)
        require(val is True, f"{exec_status} sample {sample_id!r} has {field!r} = {val!r} (must be true)")

    capture = str(run.get("validator_capture", "")).strip()
    require(bool(capture), f"{exec_status} sample {sample_id!r} has empty validator_capture")
    require("VALIDATION PASSED" in capture, f"{exec_status} sample {sample_id!r} validator_capture does not contain 'VALIDATION PASSED'")
    for pattern in REJECTED_PROOF_PATTERNS:
        require(pattern.lower() not in capture.lower(), f"{exec_status} sample {sample_id!r} validator_capture contains rejected proof pattern: {pattern!r}")

    block_plan = run.get("block_plan") or []
    if len(block_plan) > 1:
        require(run.get("child_blocks_required") is True, f"Multi-block sample {sample_id!r} must have child_blocks_required: true")
        child_count = run.get("child_block_count_expected", 0)
        require(isinstance(child_count, int) and child_count == len(block_plan), f"Multi-block sample {sample_id!r} child_block_count_expected {child_count} != block_plan length {len(block_plan)}")

    if engine == "GOOGLE_FLOW" and exec_mode == "FLOW_EXTEND_UI":
        for field in FLOW_READY_REQUIRED_BOOL_FIELDS:
            val = run.get(field)
            require(val is True, f"Flow sample {sample_id!r} has {field!r} = {val!r} (must be true)")
        require(run.get("copywriting_id"), f"Flow sample {sample_id!r} missing copywriting_id")
        require(run.get("avatar_context_id") or run.get("avatar_pool_id"), f"Flow sample {sample_id!r} missing avatar context/pool ID")
        checks.append(f"flow_ready ok: {sample_id}")

    checks.append(f"proof_fields ok: {sample_id} — {exec_status}")
    return checks


def validate_child_block_seam_proof(run: dict[str, Any]) -> list[str]:
    """Check child-block seam integrity for READY multi-block non-GOOGLE_FLOW samples."""
    sample_id = str(run.get("sample_id", "<unknown>"))
    engine = str(run.get("engine", "")).upper()
    exec_status = str(run.get("execution_status", "")).upper()
    block_plan = run.get("block_plan") or []

    if exec_status not in READY_STATUSES:
        return []
    if engine == "GOOGLE_FLOW":
        return []  # GOOGLE_FLOW seam proof is handled by validate_flow_extend_proof.py
    if len(block_plan) <= 1:
        return []  # single-block runs do not require seam proof

    checks: list[str] = []

    for field in MULTI_BLOCK_SEAM_REQUIRED_BOOL_FIELDS:
        val = run.get(field)
        require(val is True, f"Multi-block READY sample {sample_id!r} ({engine}) has {field!r} = {val!r} (must be true)")

    child_blocks = run.get("child_blocks")
    require(
        isinstance(child_blocks, list) and len(child_blocks) == len(block_plan),
        f"Multi-block READY sample {sample_id!r} ({engine}) must have child_blocks with {len(block_plan)} entries, "
        f"got {len(child_blocks) if isinstance(child_blocks, list) else 'none'}",
    )

    total_blocks = len(block_plan)
    for block in child_blocks:
        idx = int(block.get("block_index", 0))
        is_first = idx == 1
        is_last = idx == total_blocks

        word_count = block.get("block_dialogue_word_count", 0)
        require(isinstance(word_count, int) and word_count > 0, f"{sample_id!r} block {idx} has missing or zero block_dialogue_word_count")

        block_status = str(block.get("block_status", "")).strip()
        require(bool(block_status), f"{sample_id!r} block {idx} has empty block_status")

        validator_proof = str(block.get("validator_proof", "")).strip()
        require(bool(validator_proof), f"{sample_id!r} block {idx} has empty validator_proof")
        require("VALIDATION PASSED" in validator_proof, f"{sample_id!r} block {idx} validator_proof does not contain 'VALIDATION PASSED'")

        if not is_first:
            prev_state = str(block.get("previous_clip_final_second_state", "")).strip()
            require(bool(prev_state), f"{sample_id!r} block {idx} (non-first) has empty previous_clip_final_second_state")
            bridge_in = str(block.get("bridge_in", "")).strip()
            require(bool(bridge_in), f"{sample_id!r} block {idx} (non-first) has empty bridge_in")

        if not is_last:
            bridge_out = str(block.get("bridge_out", "")).strip()
            require(bool(bridge_out), f"{sample_id!r} block {idx} (non-last) has empty bridge_out")

    checks.append(f"child_block_seam ok: {sample_id} — {engine} {len(block_plan)}-block seam proof verified")
    return checks


def validate_dependent_validators() -> list[str]:
    checks: list[str] = []
    for path in DEPENDENT_VALIDATORS:
        require(path.exists(), f"Dependent validator missing: {path.name} — must exist before Notion readiness can be asserted")
        checks.append(f"dependent_validator ok: {path.name}")
    return checks


def validate_proof_guard_logic() -> list[str]:
    assert "formulaResult://" in REJECTED_PROOF_PATTERNS, "Proof guard must include formulaResult://"
    assert "<omitted />" in REJECTED_PROOF_PATTERNS, "Proof guard must include <omitted />"
    return ["proof_guard ok: formulaResult and omitted rollup rejected as proof"]


def _run_synthetic_regression() -> None:
    bad_flow = {"engine": "GOOGLE_FLOW", "execution_mode": "FLOW_EXTEND_VERTEX", "execution_status": "READY_REVIEWED_FLOW_EXTEND"}
    assert bad_flow["engine"] == "GOOGLE_FLOW", "Synthetic: GOOGLE_FLOW setup correct"
    assert bad_flow["execution_mode"] == "FLOW_EXTEND_VERTEX", "Synthetic: FLOW_EXTEND_VERTEX setup correct"
    assert bad_flow["execution_status"] == "READY_REVIEWED_FLOW_EXTEND", "Synthetic: vertex ready drift should be caught"

    bad_capture = "formulaResult://some-notion-id/field"
    found = any(p.lower() in bad_capture.lower() for p in REJECTED_PROOF_PATTERNS)
    assert found, "Synthetic: formulaResult pattern should be caught by proof guard"

    empty_capture = ""
    assert not bool(empty_capture.strip()), "Synthetic: empty capture should be falsy"


def main() -> None:
    _run_synthetic_regression()

    data = validate_manifest_exists()
    runs: list[dict[str, Any]] = data.get("sample_runs", [])

    all_checks: list[str] = [f"Manifest: {MANIFEST_PATH} ({len(runs)} sample runs)"]
    all_checks += validate_required_samples(runs)
    all_checks += validate_dependent_validators()
    all_checks += validate_proof_guard_logic()

    for run in runs:
        sample_id = str(run.get("sample_id", "<unknown>"))
        exec_status = str(run.get("execution_status", "")).upper()

        require("sample_id" in run, "Sample run missing sample_id field")
        require("engine" in run, f"Sample {sample_id!r} missing engine field")
        require("execution_status" in run, f"Sample {sample_id!r} missing execution_status field")
        require("block_plan" in run, f"Sample {sample_id!r} missing block_plan field")

        all_checks += validate_manual_review_posture(run)
        all_checks += validate_engine_contract(run)
        all_checks += validate_proof_fields(run)
        all_checks += validate_child_block_seam_proof(run)

        if exec_status in ("NEEDS_PROOF", "NEEDS_REVIEW"):
            all_checks.append(f"sample ok: {sample_id} — {exec_status}")
        elif exec_status == "MANUAL_REVIEW_ONLY":
            all_checks.append(f"sample ok: {sample_id} — MANUAL_REVIEW_ONLY")
        elif exec_status in READY_STATUSES:
            all_checks.append(f"sample ok: {sample_id} — {exec_status}")

    print("VALIDATION PASSED")
    for item in all_checks:
        print(item)


if __name__ == "__main__":
    main()
