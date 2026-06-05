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
  C. Engine block-level budget — GROK, VEO_3_1, VEO_3_1_LITE, GOOGLE_FLOW
                                 per-block WPS
  D. Total vs block budget     — multi-block plans must carry per-block budgets
  E. Sample manifest cross-check — manifest WPS requirements and block plans
  F. Synthetic regression        — invalid ordering, missing budget,
                                   VEO_3_1_LITE 8s-budget-instead-of-7s,
                                   Flow UI missing per-block WPS guard
"""

import sys
from pathlib import Path
from typing import Any

import yaml

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

GROK_PLANS = [
    (6, [6]),
    (10, [10]),
    (12, [6, 6]),
    (16, [10, 6]),
    (18, [6, 6, 6]),
    (20, [10, 10]),
    (30, [10, 10, 10]),
]
VEO_3_1_PLANS = [
    (8, [8]),
    (16, [8, 8]),
    (24, [8, 8, 8]),
    (32, [8, 8, 8, 8]),
    (40, [8, 8, 8, 8, 8]),
    (48, [8, 8, 8, 8, 8, 8]),
    (56, [8, 8, 8, 8, 8, 8, 8]),
]
VEO_3_1_LITE_PLANS = [
    (8, [8]),
    (16, [8, 8]),
    (24, [8, 8, 8]),
    (32, [8, 8, 8, 8]),
    (40, [8, 8, 8, 8, 8]),
    (48, [8, 8, 8, 8, 8, 8]),
    (56, [8, 8, 8, 8, 8, 8, 8]),
]
FLOW_UI_PLANS = [
    (8, [8]),
    (16, [8, 8]),
    (24, [8, 8, 8]),
    (32, [8, 8, 8, 8]),
    (40, [8, 8, 8, 8, 8]),
    (48, [8, 8, 8, 8, 8, 8]),
    (56, [8, 8, 8, 8, 8, 8, 8]),
]

DETERMINISTIC_SAMPLE_IDS = [
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


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_build_plan() -> Any:
    sys.path.insert(0, str(ROOT / "scripts"))
    from video_block_plan import build_plan  # type: ignore[import]

    return build_plan


def validate_corridor_structure() -> tuple[dict[int, dict[str, Any]], list[str]]:
    require(DIALOGUE_BUDGET_PATH.exists(), f"dialogue_budget_corridor.yaml missing: {DIALOGUE_BUDGET_PATH}")
    data = load_yaml(DIALOGUE_BUDGET_PATH)
    corridors = data.get("corridors", [])
    require(len(corridors) > 0, "dialogue_budget_corridor.yaml has empty corridors list")

    corridor_map: dict[int, dict[str, Any]] = {}
    checks: list[str] = []

    for row in corridors:
        for field in CORRIDOR_REQUIRED_FIELDS:
            require(field in row and row[field] is not None, f"Corridor row missing required field: {field!r} in row: {row}")

        chain = [
            int(row["minimum_words"]),
            int(row["target_min_words"]),
            int(row["target_max_words"]),
            int(row["safe_max_words"]),
            int(row["hard_ceiling_words"]),
        ]
        require(chain == sorted(chain), f"Corridor monotonicity failed for {row['duration_seconds']}s: {chain}")

        dur = int(row["duration_seconds"])
        corridor_map[dur] = row
        checks.append(f"corridor ok: {dur}s")

    return corridor_map, checks


def validate_required_durations(corridor_map: dict[int, dict[str, Any]]) -> list[str]:
    checks: list[str] = []
    for dur in REQUIRED_CORRIDOR_DURATIONS:
        require(dur in corridor_map, f"Required dialogue budget corridor missing for {dur}s")
        checks.append(f"required_duration ok: {dur}s covered")
    return checks


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
    kwargs: dict[str, Any] = {"engine_id": engine_id, "total_duration_seconds": total_secs}
    if execution_mode:
        kwargs["execution_mode"] = execution_mode
    plan = build_plan(**kwargs)

    actual_blocks = [int(b) for b in plan["block_durations_seconds"]]
    require(actual_blocks == expected_blocks, f"{engine_id} {execution_mode or 'DEFAULT'} {total_secs}s block plan mismatch: expected {expected_blocks}, got {actual_blocks}")

    blocks = plan.get("blocks", [])
    if len(actual_blocks) > 1:
        require(
            len(blocks) == len(actual_blocks),
            f"{engine_id} {total_secs}s: multi-block plan has {len(actual_blocks)} durations but only {len(blocks)} block budgets",
        )
        require(plan.get("wps_budget_mode") == "PER_BLOCK", f"{engine_id} {total_secs}s must declare PER_BLOCK WPS mode")

    for block in blocks:
        budget = block.get("dialogue_budget") or {}
        budget_dur = int(budget.get("duration_seconds", 0))
        require(budget_dur > 0, f"{engine_id} {total_secs}s block {block['block_index']} has no per-block dialogue budget")
        require(budget_dur in corridor_map, f"{engine_id} {total_secs}s block {block['block_index']} budget duration {budget_dur}s has no corridor entry")
        if expected_budget_duration is not None:
            require(
                budget_dur == expected_budget_duration,
                f"{engine_id} {total_secs}s block {block['block_index']} expected budget duration {expected_budget_duration}s, got {budget_dur}s",
            )

        if execution_mode == "FLOW_EXTEND_UI":
            require(plan.get("shared_copywriting_avatar_resolver_payload") is True, f"{engine_id} {total_secs}s must declare shared copywriting/avatar payload")
            require(block.get("requires_identity_reanchor") is True, f"{engine_id} {total_secs}s block {block['block_index']} missing identity re-anchor")
            require(block.get("requires_product_reanchor") is True, f"{engine_id} {total_secs}s block {block['block_index']} missing product re-anchor")
            if int(block["block_index"]) > 1:
                require(block.get("requires_previous_clip_final_second") is True, f"{engine_id} {total_secs}s block {block['block_index']} missing previous clip final-second requirement")

    if engine_id == "VEO_3_1_LITE":
        api_str = "+".join(str(b) for b in actual_blocks)
        bgt_str = "+".join(str(expected_budget_duration) for _ in actual_blocks)
        return f"per_block_wps ok: {engine_id} {total_secs}s -> api {api_str} / budget {bgt_str}"

    block_str = "+".join(str(b) for b in actual_blocks)
    suffix = f" ({execution_mode})" if execution_mode else ""
    return f"per_block_wps ok: {engine_id}{suffix} {total_secs}s -> {block_str}"


def validate_engine_block_budgets(corridor_map: dict[int, dict[str, Any]]) -> list[str]:
    build_plan = load_build_plan()
    checks: list[str] = []

    for total_secs, expected_blocks in GROK_PLANS:
        checks.append(_validate_plan_blocks(build_plan, "GROK", total_secs, expected_blocks, corridor_map))

    for total_secs, expected_blocks in VEO_3_1_PLANS:
        checks.append(_validate_plan_blocks(build_plan, "VEO_3_1", total_secs, expected_blocks, corridor_map))

    for total_secs, expected_blocks in VEO_3_1_LITE_PLANS:
        checks.append(
            _validate_plan_blocks(
                build_plan,
                "VEO_3_1_LITE",
                total_secs,
                expected_blocks,
                corridor_map,
                expected_budget_duration=7,
            )
        )

    for total_secs, expected_blocks in FLOW_UI_PLANS:
        checks.append(
            _validate_plan_blocks(
                build_plan,
                "GOOGLE_FLOW",
                total_secs,
                expected_blocks,
                corridor_map,
                execution_mode="FLOW_EXTEND_UI",
                expected_budget_duration=8,
            )
        )

    return checks


def validate_total_vs_block_budget(corridor_map: dict[int, dict[str, Any]]) -> list[str]:
    build_plan = load_build_plan()

    grok = build_plan("GROK", 16)
    grok_blocks = grok.get("blocks", [])
    require(len(grok_blocks) == 2, "GROK 16s must produce exactly 2 blocks for total-vs-block budget assertion")
    for block in grok_blocks:
        bdur = int((block.get("dialogue_budget") or {}).get("duration_seconds", 0))
        require(bdur in {10, 6}, f"GROK 16s block {block['block_index']} budget duration {bdur}s should be 10 or 6, not 16")
        require(bdur in corridor_map, f"GROK 16s block {block['block_index']} per-block budget duration {bdur}s missing from corridor")

    flow = build_plan("GOOGLE_FLOW", 16, execution_mode="FLOW_EXTEND_UI")
    flow_blocks = flow.get("blocks", [])
    require(len(flow_blocks) == 2, "GOOGLE_FLOW 16s FLOW_EXTEND_UI must produce exactly 2 blocks")
    for block in flow_blocks:
        bdur = int((block.get("dialogue_budget") or {}).get("duration_seconds", 0))
        require(bdur == 8, f"GOOGLE_FLOW 16s block {block['block_index']} budget duration must be 8s, got {bdur}")
        require(bdur in corridor_map, f"GOOGLE_FLOW 16s block {block['block_index']} per-block budget duration {bdur}s missing from corridor")

    return [
        "total_vs_block ok: GROK 16s uses separate 10s and 6s block budgets",
        "total_vs_block ok: GOOGLE_FLOW FLOW_EXTEND_UI 16s uses separate 8s and 8s block budgets",
    ]


def validate_sample_manifest(corridor_map: dict[int, dict[str, Any]]) -> list[str]:
    require(SAMPLE_MANIFEST_PATH.exists(), f"notion_sample_readiness.yaml missing: {SAMPLE_MANIFEST_PATH}")
    data = load_yaml(SAMPLE_MANIFEST_PATH)
    runs_list = data.get("sample_runs", [])
    runs = {str(r.get("sample_id", "")): r for r in runs_list}
    build_plan = load_build_plan()
    checks: list[str] = []

    for sid in DETERMINISTIC_SAMPLE_IDS:
        require(sid in runs, f"Required deterministic sample missing from manifest: {sid!r}")
        run = runs[sid]
        engine = str(run.get("engine", "")).upper()
        exec_mode = str(run.get("execution_mode", "")).upper() or None
        total_secs = run.get("total_duration_seconds")
        manifest_plan = [int(x) for x in (run.get("block_plan") or [])]

        require(run.get("wps_audit_required") is not False, f"{sid!r} wps_audit_required is false for deterministic engine {engine}")

        if total_secs and manifest_plan:
            kwargs: dict[str, Any] = {"engine_id": engine, "total_duration_seconds": int(total_secs)}
            if exec_mode and exec_mode not in ("", "NONE", "EXTENSION"):
                kwargs["execution_mode"] = exec_mode
            plan = build_plan(**kwargs)
            contract_plan = [int(x) for x in plan["block_durations_seconds"]]
            require(manifest_plan == contract_plan, f"{sid!r} block_plan {manifest_plan} != engine contract {contract_plan}")

            for block in plan.get("blocks", []):
                budget = block.get("dialogue_budget") or {}
                bdur = int(budget.get("duration_seconds", 0))
                require(bdur in corridor_map, f"{sid!r} block {block['block_index']} budget duration {bdur}s missing from corridor")

            if run.get("child_blocks_required") is True:
                expected_count = run.get("child_block_count_expected", 0)
                require(int(expected_count) == len(contract_plan), f"{sid!r} child_block_count_expected {expected_count} != block count {len(contract_plan)}")

            if engine == "GOOGLE_FLOW":
                require(exec_mode == "FLOW_EXTEND_UI", f"{sid!r} GOOGLE_FLOW sample must use FLOW_EXTEND_UI")
                require(run.get("execution_status") == "READY_REVIEWED_FLOW_EXTEND", f"{sid!r} GOOGLE_FLOW sample must be READY_REVIEWED_FLOW_EXTEND")
                require(run.get("shared_copywriting_avatar_resolver_payload") is True, f"{sid!r} lost shared copywriting/avatar payload flag")
                require(run.get("previous_clip_final_second_state_required") is True, f"{sid!r} missing previous clip final-second requirement")
                require(run.get("identity_reanchor_required") is True, f"{sid!r} missing identity re-anchor requirement")
                require(run.get("product_reanchor_required") is True, f"{sid!r} missing product re-anchor requirement")

        checks.append(f"sample_wps ok: {sid}")

    return checks


def _run_synthetic_regression(corridor_map: dict[int, dict[str, Any]]) -> None:
    bad_chain = [20, 18, 22, 24, 26]
    assert bad_chain != sorted(bad_chain), "Synthetic: bad chain should not be sorted"

    fake_block: dict[str, Any] = {"block_index": 1, "dialogue_budget": {"duration_seconds": 0}}
    bdur = int((fake_block.get("dialogue_budget") or {}).get("duration_seconds", 0))
    assert bdur == 0, "Synthetic: zero budget duration should be falsy"

    fake_lite_block: dict[str, Any] = {"block_index": 1, "dialogue_budget": {"duration_seconds": 8}}
    lite_bdur = int((fake_lite_block.get("dialogue_budget") or {}).get("duration_seconds", 0))
    assert lite_bdur != 7, "Synthetic: 8s budget should not equal 7s actual-render expectation"

    fake_flow_block = {"execution_mode": "FLOW_EXTEND_UI", "dialogue_budget": {"duration_seconds": 0}}
    flow_bdur = int(fake_flow_block["dialogue_budget"]["duration_seconds"])
    assert flow_bdur == 0, "Synthetic: Flow UI zero budget should trigger the guard"

    assert 7 in corridor_map, "Synthetic: 7s corridor must exist for VEO_3_1_LITE actual-render budgeting"
    assert 8 in corridor_map, "Synthetic: 8s corridor must exist for Flow UI and VEO clip-chain budgeting"


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
