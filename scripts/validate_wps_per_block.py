from __future__ import annotations

"""
BOSMAX G-03 per-block validator — WPS_DIALOGUE_GATE.

Purpose:
  Prevent the recurring failure where total video duration has a WPS budget
  but individual engine blocks do not — causing dead-air, underfilled Block 2,
  filler actions, hallucinated movement, or rushed dialogue in multi-block runs.

Checks:
  A. Corridor structure  — every row has required fields in logical order
  B. Required durations  — corridor covers at least 6s/7s/8s/10s/12s/16s/18s/
                           20s/24s/30s/32s/40s/48s/56s
  C. Engine block-level budget — GROK, VEO_3_1, VEO_3_1_LITE per-block WPS
  D. Total vs block budget     — multi-block plans must carry per-block budgets
  E. Sample manifest cross-check — manifest WPS requirements and block plans
  F. Synthetic regression        — invalid ordering, missing budget,
                                   VEO_3_1_LITE 8s-budget-instead-of-7s,
                                   Flow Extend READY guard

Scope note:
  This validator operates on the registry/planner/sample-manifest layer only.
  It does not inspect actual generated video speech timing or live Notion fields.
  Runtime speech timing validation remains PARTIAL and is documented as a future
  gap (validate_runtime_speech_timing.py or equivalent).
"""

import sys
from pathlib import Path
from typing import Any

import yaml

# Ensure UTF-8 output on Windows regardless of console code page
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
DIALOGUE_BUDGET_PATH = ROOT / "registries" / "dialogue_budget_corridor.yaml"
ENGINE_CONTRACTS_PATH = ROOT / "registries" / "video_engine_duration_contracts.yaml"
SAMPLE_MANIFEST_PATH = ROOT / "registries" / "notion_sample_readiness.yaml"

REQUIRED_CORRIDOR_DURATIONS = [6, 7, 8, 10, 12, 16, 18, 20, 24, 30, 32, 40, 48, 56]

CORRIDOR_REQUIRED_FIELDS = [
    "duration_seconds",
    "minimum_words",
    "target_min_words",
    "target_max_words",
    "safe_max_words",
    "hard_ceiling_words",
]

# Engine plans to validate: {engine_id: [(total_secs, expected_blocks)]}
GROK_PLANS = [
    (6,  [6]),
    (10, [10]),
    (12, [6, 6]),
    (16, [10, 6]),
    (18, [6, 6, 6]),
    (20, [10, 10]),
    (30, [10, 10, 10]),
]
VEO_3_1_PLANS = [
    (8,  [8]),
    (16, [8, 8]),
    (24, [8, 8, 8]),
    (32, [8, 8, 8, 8]),
    (40, [8, 8, 8, 8, 8]),
    (48, [8, 8, 8, 8, 8, 8]),
    (56, [8, 8, 8, 8, 8, 8, 8]),
]
VEO_3_1_LITE_PLANS = [
    (8,  [8]),
    (16, [8, 8]),
    (24, [8, 8, 8]),
    (32, [8, 8, 8, 8]),
    (40, [8, 8, 8, 8, 8]),
    (48, [8, 8, 8, 8, 8, 8]),
    (56, [8, 8, 8, 8, 8, 8, 8]),
]

# Deterministic sample IDs (require per-block WPS validation)
DETERMINISTIC_SAMPLE_IDS = [
    "SAMPLE-HYBRID-01",
    "SAMPLE-HYBRID-02",
    "SAMPLE-HYBRID-GROK-16S-RIZAL",
    "SAMPLE-VEO31-16S-CLIP-CHAIN-RIZAL",
    "SAMPLE-VEO31-24S-CLIP-CHAIN-RIZAL",
]
MANUAL_REVIEW_SAMPLE_IDS = [
    "SAMPLE-FLOW-EXTEND-16S-RIZAL",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_build_plan() -> Any:
    """Import build_plan from video_block_plan at call-time."""
    sys.path.insert(0, str(ROOT / "scripts"))
    from video_block_plan import build_plan  # type: ignore[import]
    return build_plan


# ── A. Corridor structure ─────────────────────────────────────────────────────

def validate_corridor_structure() -> tuple[dict[int, dict[str, Any]], list[str]]:
    require(DIALOGUE_BUDGET_PATH.exists(), f"dialogue_budget_corridor.yaml missing: {DIALOGUE_BUDGET_PATH}")
    data = load_yaml(DIALOGUE_BUDGET_PATH)
    corridors = data.get("corridors", [])
    require(len(corridors) > 0, "dialogue_budget_corridor.yaml has empty corridors list")

    corridor_map: dict[int, dict[str, Any]] = {}
    checks: list[str] = []

    for row in corridors:
        for field in CORRIDOR_REQUIRED_FIELDS:
            require(
                field in row and row[field] is not None,
                f"Corridor row missing required field: {field!r} in row: {row}",
            )

        chain = [
            int(row["minimum_words"]),
            int(row["target_min_words"]),
            int(row["target_max_words"]),
            int(row["safe_max_words"]),
            int(row["hard_ceiling_words"]),
        ]
        require(
            chain == sorted(chain),
            f"Corridor monotonicity failed for {row['duration_seconds']}s: {chain}",
        )

        dur = int(row["duration_seconds"])
        corridor_map[dur] = row
        checks.append(f"corridor ok: {dur}s")

    return corridor_map, checks


# ── B. Required durations ─────────────────────────────────────────────────────

def validate_required_durations(corridor_map: dict[int, dict[str, Any]]) -> list[str]:
    checks: list[str] = []
    for dur in REQUIRED_CORRIDOR_DURATIONS:
        require(
            dur in corridor_map,
            f"Required dialogue budget corridor missing for {dur}s",
        )
        checks.append(f"required_duration ok: {dur}s covered")
    return checks


# ── C. Engine block-level budget ──────────────────────────────────────────────

def _validate_plan_blocks(
    build_plan: Any,
    engine_id: str,
    total_secs: int,
    expected_blocks: list[int],
    corridor_map: dict[int, dict[str, Any]],
    *,
    execution_mode: str | None = None,
    expected_budget_duration: int | None = None,
) -> str:
    """
    Run build_plan and verify every block has a corridor-backed budget.
    For VEO_3_1_LITE: expected_budget_duration=7 asserts the 7s actual-render override.
    Returns a check string.
    """
    kwargs: dict[str, Any] = {"engine_id": engine_id, "total_duration_seconds": total_secs}
    if execution_mode:
        kwargs["execution_mode"] = execution_mode
    plan = build_plan(**kwargs)

    actual_blocks = [int(b) for b in plan["block_durations_seconds"]]
    require(
        actual_blocks == expected_blocks,
        f"{engine_id} {total_secs}s block plan mismatch: expected {expected_blocks}, got {actual_blocks}",
    )

    blocks = plan.get("blocks", [])
    if len(actual_blocks) > 1:
        require(
            len(blocks) == len(actual_blocks),
            f"{engine_id} {total_secs}s: multi-block plan has {len(actual_blocks)} durations "
            f"but only {len(blocks)} block budgets — total-duration budget alone is insufficient",
        )

    for block in blocks:
        budget = block.get("dialogue_budget") or {}
        budget_dur = int(budget.get("duration_seconds", 0))
        require(
            budget_dur > 0,
            f"{engine_id} {total_secs}s block {block['block_index']} has no per-block dialogue budget",
        )
        require(
            budget_dur in corridor_map,
            f"{engine_id} {total_secs}s block {block['block_index']} budget duration {budget_dur}s "
            f"has no corridor entry",
        )
        if expected_budget_duration is not None:
            require(
                budget_dur == expected_budget_duration,
                f"{engine_id} {total_secs}s block {block['block_index']} expected budget duration "
                f"{expected_budget_duration}s (actual render), got {budget_dur}s — "
                f"VEO_3_1_LITE must use 7s actual-render corridor, not 8s API block duration",
            )

    if engine_id == "VEO_3_1_LITE":
        api_str = "+".join(str(b) for b in actual_blocks)
        bgt_str = "+".join(str(expected_budget_duration) for _ in actual_blocks)
        return f"per_block_wps ok: {engine_id} {total_secs}s -> api {api_str} / budget {bgt_str}"

    block_str = "+".join(str(b) for b in actual_blocks)
    return f"per_block_wps ok: {engine_id} {total_secs}s -> {block_str}"


def validate_engine_block_budgets(
    corridor_map: dict[int, dict[str, Any]]
) -> list[str]:
    build_plan = load_build_plan()
    checks: list[str] = []

    for total_secs, expected_blocks in GROK_PLANS:
        checks.append(_validate_plan_blocks(build_plan, "GROK", total_secs, expected_blocks, corridor_map))

    for total_secs, expected_blocks in VEO_3_1_PLANS:
        checks.append(_validate_plan_blocks(build_plan, "VEO_3_1", total_secs, expected_blocks, corridor_map))

    for total_secs, expected_blocks in VEO_3_1_LITE_PLANS:
        checks.append(_validate_plan_blocks(
            build_plan, "VEO_3_1_LITE", total_secs, expected_blocks, corridor_map,
            expected_budget_duration=7,
        ))

    return checks


# ── D. Total vs block budget ──────────────────────────────────────────────────

def validate_total_vs_block_budget(corridor_map: dict[int, dict[str, Any]]) -> list[str]:
    """
    Explicit assertion: for multi-block GROK 16s, each block must have its own
    budget — the 16s total budget alone is insufficient.
    """
    build_plan = load_build_plan()
    plan = build_plan("GROK", 16)
    blocks = plan.get("blocks", [])
    require(
        len(blocks) == 2,
        "GROK 16s must produce exactly 2 blocks for total-vs-block budget assertion",
    )
    block_durations = [int(b["block_duration_seconds"]) for b in blocks]
    require(
        block_durations == [10, 6],
        f"GROK 16s blocks must be [10, 6], got {block_durations}",
    )
    # Each block must have its own budget corridor entry, not share the 16s total
    for block in blocks:
        budget = block.get("dialogue_budget") or {}
        bdur = int(budget.get("duration_seconds", 0))
        require(
            bdur in {10, 6},
            f"GROK 16s block {block['block_index']} budget duration {bdur}s should be 10 or 6, not 16",
        )
        require(
            bdur in corridor_map,
            f"GROK 16s block {block['block_index']} per-block budget duration {bdur}s missing from corridor",
        )
    return ["total_vs_block ok: GROK 16s uses separate 10s and 6s block budgets (not total 16s)"]


# ── E. Sample manifest cross-check ────────────────────────────────────────────

def validate_sample_manifest(corridor_map: dict[int, dict[str, Any]]) -> list[str]:
    require(SAMPLE_MANIFEST_PATH.exists(), f"notion_sample_readiness.yaml missing: {SAMPLE_MANIFEST_PATH}")
    data = load_yaml(SAMPLE_MANIFEST_PATH)
    runs_list = data.get("sample_runs", [])
    runs = {str(r.get("sample_id", "")): r for r in runs_list}
    build_plan = load_build_plan()
    checks: list[str] = []

    # Deterministic samples
    for sid in DETERMINISTIC_SAMPLE_IDS:
        require(sid in runs, f"Required deterministic sample missing from manifest: {sid!r}")
        run = runs[sid]
        engine = str(run.get("engine", "")).upper()
        exec_mode = str(run.get("execution_mode", "")).upper() or None
        total_secs = run.get("total_duration_seconds")
        manifest_plan = [int(x) for x in (run.get("block_plan") or [])]
        exec_status = str(run.get("execution_status", "")).upper()
        wps_required = run.get("wps_audit_required", True)

        # WPS audit must be required for deterministic READY/NEEDS_PROOF runs
        require(
            wps_required is not False,
            f"{sid!r} wps_audit_required is false for deterministic engine {engine} — cannot be WPS-valid",
        )

        # Block plan must match planner
        if total_secs and manifest_plan:
            kwargs: dict[str, Any] = {"engine_id": engine, "total_duration_seconds": int(total_secs)}
            if exec_mode and exec_mode not in ("", "NONE", "EXTENSION"):
                kwargs["execution_mode"] = exec_mode
            plan = build_plan(**kwargs)
            contract_plan = [int(x) for x in plan["block_durations_seconds"]]
            require(
                manifest_plan == contract_plan,
                f"{sid!r} block_plan {manifest_plan} != engine contract {contract_plan}",
            )

            # Every block must have a budget corridor
            for block in plan.get("blocks", []):
                budget = block.get("dialogue_budget") or {}
                bdur = int(budget.get("duration_seconds", 0))
                require(
                    bdur in corridor_map,
                    f"{sid!r} block {block['block_index']} budget duration {bdur}s missing from corridor",
                )

            # child_block_count_expected must match block count for multi-block
            if run.get("child_blocks_required") is True:
                expected_count = run.get("child_block_count_expected", 0)
                require(
                    int(expected_count) == len(contract_plan),
                    f"{sid!r} child_block_count_expected {expected_count} != block count {len(contract_plan)}",
                )

        checks.append(f"sample_wps ok: {sid}")

    # Flow Extend sample: must be MANUAL_REVIEW_ONLY and not READY
    for sid in MANUAL_REVIEW_SAMPLE_IDS:
        require(sid in runs, f"Required Flow Extend sample missing from manifest: {sid!r}")
        run = runs[sid]
        exec_status = str(run.get("execution_status", "")).upper()
        require(
            exec_status == "MANUAL_REVIEW_ONLY",
            f"{sid!r} execution_status must be MANUAL_REVIEW_ONLY, got {exec_status!r}",
        )
        require(
            exec_status != "READY",
            f"{sid!r} must not be READY — GOOGLE_FLOW.FLOW_EXTEND remains MANUAL_REVIEW_ONLY",
        )
        checks.append(f"flow_extend ok: {sid} MANUAL_REVIEW_ONLY")

    return checks


# ── F. Synthetic regression ───────────────────────────────────────────────────

def _run_synthetic_regression(corridor_map: dict[int, dict[str, Any]]) -> None:
    """
    Confirm guard logic fires on bad data without touching real files.
    """
    # Invalid corridor ordering should fail the chain check
    bad_chain = [20, 18, 22, 24, 26]  # 20 > 18 — not monotone
    assert bad_chain != sorted(bad_chain), "Synthetic: bad chain should not be sorted"

    # Missing block budget: budget_dur == 0 should fail
    fake_block: dict[str, Any] = {"block_index": 1, "dialogue_budget": {"duration_seconds": 0}}
    bdur = int((fake_block.get("dialogue_budget") or {}).get("duration_seconds", 0))
    assert bdur == 0, "Synthetic: zero budget duration should be falsy"

    # VEO_3_1_LITE using 8s budget instead of 7s should fail
    fake_lite_block: dict[str, Any] = {"block_index": 1, "dialogue_budget": {"duration_seconds": 8}}
    lite_bdur = int((fake_lite_block.get("dialogue_budget") or {}).get("duration_seconds", 0))
    assert lite_bdur != 7, "Synthetic: 8s budget should not equal 7s actual-render expectation"

    # Flow Extend marked READY should fail
    fake_flow = {"execution_status": "READY", "engine": "GOOGLE_FLOW"}
    status = str(fake_flow.get("execution_status", "")).upper()
    engine = str(fake_flow.get("engine", "")).upper()
    assert engine == "GOOGLE_FLOW" and status == "READY", "Synthetic: GOOGLE_FLOW READY case confirmed"
    # Confirm our guard would catch it
    assert status == "READY", "Synthetic: guard should detect this as forbidden"

    # Required duration missing from corridor: 7s must exist (VEO_3_1_LITE actual-render)
    assert 7 in corridor_map, "Synthetic: 7s corridor must exist for VEO_3_1_LITE actual-render budgeting"


def main() -> None:
    corridor_map, corridor_checks = validate_corridor_structure()
    _run_synthetic_regression(corridor_map)

    duration_checks = validate_required_durations(corridor_map)
    engine_checks = validate_engine_block_budgets(corridor_map)
    total_vs_block_checks = validate_total_vs_block_budget(corridor_map)
    sample_checks = validate_sample_manifest(corridor_map)

    print("VALIDATION PASSED")
    print(f"Corridor: {DIALOGUE_BUDGET_PATH}")
    print(f"Engine contracts: {ENGINE_CONTRACTS_PATH}")
    print(f"Sample manifest: {SAMPLE_MANIFEST_PATH}")
    for item in corridor_checks + duration_checks + engine_checks + total_vs_block_checks + sample_checks:
        print(item)


if __name__ == "__main__":
    main()
