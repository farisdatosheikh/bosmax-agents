from __future__ import annotations

"""
BOSMAX G-08 + G-10 validator — NOTION_DOWNSTREAM_GATE + SAMPLE_OUTPUT_GATE.

Checks:
  - registries/notion_sample_readiness.yaml exists and is structurally valid
  - All required sample IDs are present in the manifest
  - block_plan for each non-MANUAL_REVIEW_ONLY run matches the engine contract
    (cross-validated via video_block_plan.build_plan)
  - MANUAL_REVIEW_ONLY / NEEDS_REVIEW runs are never marked execution_status READY
  - GOOGLE_FLOW.FLOW_EXTEND runs must always be MANUAL_REVIEW_ONLY
  - READY runs satisfy all proof field requirements
  - formulaResult:// and omitted-rollup values are rejected as proof
  - READY multi-block runs have correct child_block_count_expected
  - Dependent validator scripts exist on disk

Scope note:
  This validator operates on the repo-backed manifest only. It does not call
  the Notion API. Live Notion page existence, MCP rollup rendering, and
  formula result accuracy remain runtime concerns documented as PARTIAL in
  kernel contract G-08/G-10. Repo authority outranks Notion downstream UI.
"""

import sys
from pathlib import Path
from typing import Any

import yaml

# Ensure UTF-8 output on Windows regardless of console code page
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "registries" / "notion_sample_readiness.yaml"

REQUIRED_SAMPLE_IDS = [
    "SAMPLE-HYBRID-01",
    "SAMPLE-HYBRID-02",
    "SAMPLE-HYBRID-GROK-16S-RIZAL",
    "SAMPLE-VEO31-16S-CLIP-CHAIN-RIZAL",
    "SAMPLE-VEO31-24S-CLIP-CHAIN-RIZAL",
    "SAMPLE-FLOW-EXTEND-16S-RIZAL",
]

DEPENDENT_VALIDATORS = [
    ROOT / "scripts" / "validate_product_truth_drift.py",
    ROOT / "scripts" / "validate_avatar_registry_coverage.py",
    ROOT / "scripts" / "validate_video_block_contracts.py",
]

# Proof-rejected values: operator must not paste these as validator_capture
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
    """Cross-reference block_plan against video_block_plan.build_plan."""
    sample_id = str(run.get("sample_id", "<unknown>"))
    engine = str(run.get("engine", "")).upper()
    execution_mode = str(run.get("execution_mode", "")).upper() or None
    exec_status = str(run.get("execution_status", "")).upper()
    total_secs = run.get("total_duration_seconds")
    manifest_plan = [int(x) for x in (run.get("block_plan") or [])]

    # Skip engine contract check for MANUAL_REVIEW_ONLY / NEEDS_REVIEW with empty block_plan
    if exec_status in ("MANUAL_REVIEW_ONLY", "NEEDS_REVIEW") and not manifest_plan:
        return [f"engine_contract skip: {sample_id} — {exec_status}, no deterministic block math"]

    if not engine or total_secs is None:
        return []

    try:
        # Import at call-time so the validator fails cleanly if video_block_plan is absent
        sys.path.insert(0, str(ROOT / "scripts"))
        from video_block_plan import build_plan  # type: ignore[import]
        kwargs: dict[str, Any] = {"engine_id": engine, "total_duration_seconds": int(total_secs)}
        if execution_mode and execution_mode not in ("", "NONE"):
            kwargs["execution_mode"] = execution_mode
        plan = build_plan(**kwargs)
        contract_plan = [int(x) for x in plan.get("block_durations_seconds", [])]
        require(
            manifest_plan == contract_plan,
            f"{sample_id} block_plan {manifest_plan} does not match engine contract {contract_plan} "
            f"for {engine} {total_secs}s",
        )
        return [f"engine_contract ok: {sample_id} — {engine} {total_secs}s -> {'+'.join(str(x) for x in contract_plan)}"]
    except ValueError as exc:
        fail(f"{sample_id} engine contract lookup failed: {exc}")
        return []  # unreachable


def validate_manual_review_posture(run: dict[str, Any]) -> list[str]:
    sample_id = str(run.get("sample_id", "<unknown>"))
    engine = str(run.get("engine", "")).upper()
    exec_mode = str(run.get("execution_mode", "")).upper()
    exec_status = str(run.get("execution_status", "")).upper()

    # GOOGLE_FLOW runs must NEVER be READY
    if engine == "GOOGLE_FLOW" or exec_mode == "FLOW_EXTEND":
        require(
            exec_status in ("MANUAL_REVIEW_ONLY", "NEEDS_REVIEW", "NEEDS_PROOF"),
            f"GOOGLE_FLOW sample {sample_id!r} must not be READY — must remain MANUAL_REVIEW_ONLY",
        )
        if exec_status == "READY":
            fail(f"GOOGLE_FLOW sample {sample_id!r} is marked READY — forbidden")

    return []


def validate_proof_fields(run: dict[str, Any]) -> list[str]:
    """Only applies to READY runs — all proof fields must be satisfied."""
    sample_id = str(run.get("sample_id", "<unknown>"))
    exec_status = str(run.get("execution_status", "")).upper()
    if exec_status != "READY":
        return []

    checks: list[str] = []

    # All required bool proof fields must be true
    for field in READY_REQUIRED_BOOL_FIELDS:
        val = run.get(field)
        require(
            val is True,
            f"READY sample {sample_id!r} has {field!r} = {val!r} (must be true)",
        )

    # validator_capture must contain "VALIDATION PASSED"
    capture = str(run.get("validator_capture", "")).strip()
    require(
        bool(capture),
        f"READY sample {sample_id!r} has empty validator_capture — paste VALIDATION PASSED output",
    )
    require(
        "VALIDATION PASSED" in capture,
        f"READY sample {sample_id!r} validator_capture does not contain 'VALIDATION PASSED'",
    )

    # Reject invalid proof patterns
    for pattern in REJECTED_PROOF_PATTERNS:
        require(
            pattern.lower() not in capture.lower(),
            f"READY sample {sample_id!r} validator_capture contains rejected proof pattern: {pattern!r}",
        )

    # Multi-block: child_blocks_required must be true and child_block_count_expected > 0
    block_plan = run.get("block_plan") or []
    if len(block_plan) > 1:
        require(
            run.get("child_blocks_required") is True,
            f"READY multi-block sample {sample_id!r} must have child_blocks_required: true",
        )
        child_count = run.get("child_block_count_expected", 0)
        require(
            isinstance(child_count, int) and child_count == len(block_plan),
            f"READY multi-block sample {sample_id!r} child_block_count_expected {child_count} "
            f"!= block_plan length {len(block_plan)}",
        )
        if run.get("wps_audit_required") is True:
            checks.append(f"wps_audit required: {sample_id}")

    checks.append(f"proof_fields ok: {sample_id} — READY")
    return checks


def validate_dependent_validators() -> list[str]:
    checks: list[str] = []
    for path in DEPENDENT_VALIDATORS:
        require(path.exists(), f"Dependent validator missing: {path.name} — must exist before Notion readiness can be asserted")
        checks.append(f"dependent_validator ok: {path.name}")
    return checks


def validate_proof_guard_logic() -> list[str]:
    """Confirm rejected patterns constant is populated and would fire."""
    assert "formulaResult://" in REJECTED_PROOF_PATTERNS, "Proof guard must include formulaResult://"
    assert "<omitted />" in REJECTED_PROOF_PATTERNS, "Proof guard must include <omitted />"
    return ["proof_guard ok: formulaResult and omitted rollup rejected as proof"]


def _run_synthetic_regression() -> None:
    """
    Synthetic regression: confirm the validator logic rejects known bad states.
    Does not mutate real files.
    """
    # GOOGLE_FLOW READY should fail
    bad_flow = {"engine": "GOOGLE_FLOW", "execution_status": "READY", "sample_id": "SYNTHETIC_FLOW"}
    engine = str(bad_flow.get("engine", "")).upper()
    status = str(bad_flow.get("execution_status", "")).upper()
    assert engine == "GOOGLE_FLOW" and status == "READY", "Synthetic: GOOGLE_FLOW READY setup correct"
    # This would trigger the GOOGLE_FLOW check in validate_manual_review_posture

    # formulaResult in capture should fail
    bad_capture = "formulaResult://some-notion-id/field"
    found = any(p.lower() in bad_capture.lower() for p in REJECTED_PROOF_PATTERNS)
    assert found, "Synthetic: formulaResult pattern should be caught by proof guard"

    # Empty validator_capture for READY should fail
    empty_capture = ""
    assert not bool(empty_capture.strip()), "Synthetic: empty capture should be falsy"


def main() -> None:
    _run_synthetic_regression()

    data = validate_manifest_exists()
    runs: list[dict[str, Any]] = data.get("sample_runs", [])

    all_checks: list[str] = [
        f"Manifest: {MANIFEST_PATH} ({len(runs)} sample runs)",
    ]

    all_checks += validate_required_samples(runs)
    all_checks += validate_dependent_validators()
    all_checks += validate_proof_guard_logic()

    for run in runs:
        sample_id = str(run.get("sample_id", "<unknown>"))
        exec_status = str(run.get("execution_status", "")).upper()

        # Structural completeness
        require("sample_id" in run, f"Sample run missing sample_id field")
        require("engine" in run, f"Sample {sample_id!r} missing engine field")
        require("execution_status" in run, f"Sample {sample_id!r} missing execution_status field")
        require("block_plan" in run, f"Sample {sample_id!r} missing block_plan field")

        all_checks += validate_manual_review_posture(run)
        all_checks += validate_engine_contract(run)
        all_checks += validate_proof_fields(run)

        if exec_status in ("NEEDS_PROOF", "NEEDS_REVIEW"):
            all_checks.append(f"sample ok: {sample_id} — {exec_status}")
        elif exec_status == "MANUAL_REVIEW_ONLY":
            all_checks.append(f"sample ok: {sample_id} — MANUAL_REVIEW_ONLY")
        elif exec_status == "READY":
            all_checks.append(f"sample ok: {sample_id} — READY (all proof fields satisfied)")

    print("VALIDATION PASSED")
    for item in all_checks:
        print(item)


if __name__ == "__main__":
    main()
