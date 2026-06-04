from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

from video_block_plan import CONTRACT_PATH, DIALOGUE_BUDGET_PATH, build_plan, load_registry_bundle

ROOT = Path(__file__).resolve().parents[1]
HANDOFF_DOC_PATH = ROOT / "BOSMAX_NOTION_MULTI_BLOCK_VIDEO_HANDOFF_v1.md"
DECISION_DOC_PATH = ROOT / "BOSMAX_VEO31_FLOW_CONTRACT_DECISION_v1.md"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def validate_registry_shape() -> dict[str, Any]:
    require(CONTRACT_PATH.exists(), f"Missing video contract registry: {CONTRACT_PATH}")
    require(DIALOGUE_BUDGET_PATH.exists(), f"Missing dialogue budget registry: {DIALOGUE_BUDGET_PATH}")
    require(HANDOFF_DOC_PATH.exists(), f"Missing multi-block handoff doc: {HANDOFF_DOC_PATH}")
    require(DECISION_DOC_PATH.exists(), f"Missing VEO/Flow decision record: {DECISION_DOC_PATH}")

    registry = load_yaml(CONTRACT_PATH)
    engines = registry.get("engines")
    require(isinstance(engines, dict) and engines, "video_engine_duration_contracts.yaml has no engines map")

    for engine_id in ("GROK", "VEO_3_1", "VEO_3_1_LITE", "GOOGLE_FLOW"):
        require(engine_id in engines, f"Registry missing required engine entry: {engine_id}")

    return engines


def validate_grok_contract(engines: dict[str, Any]) -> list[str]:
    grok = engines["GROK"]
    require(grok.get("authority_status") == "VERIFIED", "GROK must remain VERIFIED")
    require(grok.get("notion_execution_status") == "READY", "GROK notion_execution_status must remain READY")

    valid_blocks = [int(value) for value in grok.get("valid_block_durations_seconds", [])]
    require(valid_blocks == [6, 10], f"GROK valid block durations drifted: {valid_blocks}")

    expected_plans = {
        12: [6, 6],
        16: [10, 6],
        20: [10, 10],
        30: [10, 10, 10],
    }
    checks: list[str] = []
    for duration, expected_blocks in expected_plans.items():
        plan = build_plan("GROK", duration)
        actual_blocks = [int(item) for item in plan["block_durations_seconds"]]
        require(actual_blocks == expected_blocks, f"GROK {duration}s plan mismatch: expected {expected_blocks}, got {actual_blocks}")
        require(plan["block_count"] == len(expected_blocks), f"GROK {duration}s block_count mismatch")
        require(all(block in (6, 10) for block in actual_blocks), f"GROK {duration}s contains invalid block duration")
        for block in plan["blocks"]:
            block_index = int(block["block_index"])
            if block_index < plan["block_count"]:
                require(block["bridge_out_required"] is True, f"GROK {duration}s block {block_index} missing bridge-out requirement")
            if block_index > 1:
                require(block["bridge_in_required"] is True, f"GROK {duration}s block {block_index} missing bridge-in requirement")
                resume = block.get("speech_resume_window_seconds") or {}
                require(resume.get("min") == 0.5 and resume.get("max") == 1.0, f"GROK {duration}s block {block_index} resume window drifted")
            budget = block.get("dialogue_budget")
            require(isinstance(budget, dict), f"GROK {duration}s block {block_index} missing per-block budget")
        checks.append(f"GROK {duration}s -> {'+'.join(str(item) for item in actual_blocks)}")
    return checks


def validate_veo_contract(engines: dict[str, Any]) -> list[str]:
    checks: list[str] = []
    veo = engines["VEO_3_1"]
    require(veo.get("authority_status") == "PARTIAL_VERIFIED", "VEO_3_1 must be PARTIAL_VERIFIED")
    require(veo.get("notion_execution_status") == "READY_CLIP_MODE", "VEO_3_1 notion_execution_status must be READY_CLIP_MODE")
    require(veo.get("decision_record") == DECISION_DOC_PATH.name, "VEO_3_1 decision record link missing")
    clip_chain = (veo.get("execution_modes") or {}).get("CLIP_CHAIN") or {}
    require(str(clip_chain.get("status", "")).upper() == "READY", "VEO_3_1.CLIP_CHAIN must be READY")
    expected_plans = {
        16: [8, 8],
        24: [8, 8, 8],
        32: [8, 8, 8, 8],
        40: [8, 8, 8, 8, 8],
        48: [8, 8, 8, 8, 8, 8],
        56: [8, 8, 8, 8, 8, 8, 8],
    }
    for duration, expected_blocks in expected_plans.items():
        plan = build_plan("VEO_3_1", duration)
        actual_blocks = [int(item) for item in plan["block_durations_seconds"]]
        require(plan["status"] == "READY", f"VEO_3_1 {duration}s must resolve READY")
        require(actual_blocks == expected_blocks, f"VEO_3_1 {duration}s mismatch: expected {expected_blocks}, got {actual_blocks}")
        require(plan["requires_frame_bridge"] is True, f"VEO_3_1 {duration}s missing frame bridge requirement")
        require(plan["requires_identity_reanchor"] is True, f"VEO_3_1 {duration}s missing identity re-anchor requirement")
        require(plan["requires_product_reanchor"] is True, f"VEO_3_1 {duration}s missing product re-anchor requirement")
        for block in plan["blocks"][1:]:
            require(block["requires_frame_bridge"] is True, f"VEO_3_1 {duration}s block {block['block_index']} missing frame bridge flag")
            require(block["bridge_in_required"] is True, f"VEO_3_1 {duration}s block {block['block_index']} missing bridge-in")
        checks.append(f"VEO_3_1 {duration}s -> {'+'.join(str(item) for item in actual_blocks)}")

    try:
        build_plan("VEO_3_1", 14)
        fail("VEO_3_1 14s should fail closed")
    except ValueError:
        checks.append("VEO_3_1 invalid 14s rejected")
    return checks


def validate_veo31_lite_contract(engines: dict[str, Any]) -> list[str]:
    checks: list[str] = []
    lite = engines["VEO_3_1_LITE"]
    require(lite.get("authority_status") == "PARTIAL_VERIFIED", "VEO_3_1_LITE must be PARTIAL_VERIFIED")
    require(lite.get("notion_execution_status") == "READY_CLIP_MODE", "VEO_3_1_LITE notion_execution_status must be READY_CLIP_MODE")
    clip_chain = (lite.get("execution_modes") or {}).get("CLIP_CHAIN") or {}
    require(str(clip_chain.get("status", "")).upper() == "READY", "VEO_3_1_LITE.CLIP_CHAIN must be READY")
    require(int(clip_chain.get("actual_render_duration_seconds", 0)) == 7, "VEO_3_1_LITE must declare actual_render_duration_seconds: 7")
    require(int(clip_chain.get("dialogue_budget_actual_render_seconds", 0)) == 7, "VEO_3_1_LITE must declare dialogue_budget_actual_render_seconds: 7")

    bundle = load_registry_bundle()
    seven_s_budget = bundle.budgets.get(("BM", "BRISK_UGC", 7))
    require(isinstance(seven_s_budget, dict), "Dialogue budget corridor missing BM/BRISK_UGC/7s (required for VEO_3_1_LITE)")

    expected_plans = {
        8: [8],
        16: [8, 8],
        24: [8, 8, 8],
        32: [8, 8, 8, 8],
        40: [8, 8, 8, 8, 8],
        48: [8, 8, 8, 8, 8, 8],
        56: [8, 8, 8, 8, 8, 8, 8],
    }
    for duration, expected_blocks in expected_plans.items():
        plan = build_plan("VEO_3_1_LITE", duration)
        actual_blocks = [int(item) for item in plan["block_durations_seconds"]]
        require(plan["status"] == "READY", f"VEO_3_1_LITE {duration}s must resolve READY")
        require(actual_blocks == expected_blocks, f"VEO_3_1_LITE {duration}s mismatch: expected {expected_blocks}, got {actual_blocks}")
        require(plan["requires_frame_bridge"] is True, f"VEO_3_1_LITE {duration}s missing frame bridge requirement")
        require(plan["requires_identity_reanchor"] is True, f"VEO_3_1_LITE {duration}s missing identity re-anchor requirement")
        require(plan["requires_product_reanchor"] is True, f"VEO_3_1_LITE {duration}s missing product re-anchor requirement")
        for block in plan["blocks"]:
            block_budget = block.get("dialogue_budget") or {}
            require(
                int(block_budget.get("duration_seconds", 0)) == 7,
                f"VEO_3_1_LITE {duration}s block {block['block_index']} dialogue_budget must use 7s actual-render corridor, got {block_budget.get('duration_seconds')}",
            )
        for block in plan["blocks"][1:]:
            require(block["requires_frame_bridge"] is True, f"VEO_3_1_LITE {duration}s block {block['block_index']} missing frame bridge flag")
            require(block["bridge_in_required"] is True, f"VEO_3_1_LITE {duration}s block {block['block_index']} missing bridge-in")
        checks.append(f"VEO_3_1_LITE {duration}s -> {'+'.join(str(item) for item in actual_blocks)}")

    try:
        build_plan("VEO_3_1_LITE", 14)
        fail("VEO_3_1_LITE 14s should fail closed")
    except ValueError:
        checks.append("VEO_3_1_LITE invalid 14s rejected")
    return checks


def validate_flow_contract(engines: dict[str, Any]) -> list[str]:
    flow = engines["GOOGLE_FLOW"]
    require(flow.get("authority_status") == "PARTIAL_VERIFIED", "GOOGLE_FLOW must be PARTIAL_VERIFIED")
    require(flow.get("notion_execution_status") == "MANUAL_REVIEW_ONLY", "GOOGLE_FLOW must remain MANUAL_REVIEW_ONLY")
    require(flow.get("decision_record") == DECISION_DOC_PATH.name, "GOOGLE_FLOW decision record link missing")
    flow_extend = ((flow.get("execution_modes") or {}).get("FLOW_EXTEND")) or {}
    require(str(flow_extend.get("status", "")).upper() == "NEEDS_REVIEW", "FLOW_EXTEND must remain NEEDS_REVIEW")
    plan = build_plan("GOOGLE_FLOW", 16, execution_mode="FLOW_EXTEND")
    require(plan["status"] == "NEEDS_REVIEW", "FLOW_EXTEND 16s must remain NEEDS_REVIEW")
    require(plan["requires_previous_clip_final_second"] is True, "FLOW_EXTEND must require previous clip final second state")
    require("manual-review only" in (plan["reason"] or "").lower(), "FLOW_EXTEND reason must explain manual-review-only state")

    reviewed_plan = build_plan(
        "GOOGLE_FLOW",
        16,
        execution_mode="FLOW_EXTEND",
        previous_clip_final_second_state="Close-up grip locked, serum held near chest, speech continues through final beat.",
    )
    require(reviewed_plan["status"] == "NEEDS_REVIEW", "FLOW_EXTEND must not silently flip READY from a provided previous state")
    checks = ["GOOGLE_FLOW FLOW_EXTEND 16s flagged NEEDS_REVIEW"]
    return checks


def validate_dialogue_budget_coverage() -> list[str]:
    bundle = load_registry_bundle()
    expected = [6, 7, 8, 10, 12, 16, 18, 20, 24, 30, 32, 40, 48, 56]
    checks: list[str] = []
    for duration in expected:
        budget = bundle.budgets.get(("BM", "BRISK_UGC", duration))
        require(isinstance(budget, dict), f"Dialogue budget corridor missing BM/BRISK_UGC/{duration}s")
        chain = [
            int(budget["minimum_words"]),
            int(budget["target_min_words"]),
            int(budget["target_max_words"]),
            int(budget["safe_max_words"]),
            int(budget["hard_ceiling_words"]),
        ]
        require(chain == sorted(chain), f"Dialogue budget monotonicity failed for {duration}s: {chain}")
        checks.append(f"budget {duration}s ok")
    return checks


def main() -> None:
    engines = validate_registry_shape()
    grok_checks = validate_grok_contract(engines)
    veo_checks = validate_veo_contract(engines)
    veo_lite_checks = validate_veo31_lite_contract(engines)
    flow_checks = validate_flow_contract(engines)
    budget_checks = validate_dialogue_budget_coverage()

    print("VALIDATION PASSED")
    print(f"Video Contract Registry: {CONTRACT_PATH}")
    print(f"Dialogue Budget Registry: {DIALOGUE_BUDGET_PATH}")
    print(f"Handoff Doc: {HANDOFF_DOC_PATH}")
    print(f"Decision Record: {DECISION_DOC_PATH}")
    for item in grok_checks + veo_checks + veo_lite_checks + flow_checks + budget_checks:
        print(item)


if __name__ == "__main__":
    main()
