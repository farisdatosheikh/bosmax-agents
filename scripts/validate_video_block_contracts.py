from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

from video_block_plan import CONTRACT_PATH, DIALOGUE_BUDGET_PATH, build_plan, load_registry_bundle

ROOT = Path(__file__).resolve().parents[1]
HANDOFF_DOC_PATH = ROOT / "BOSMAX_NOTION_MULTI_BLOCK_VIDEO_HANDOFF_v1.md"


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

    registry = load_yaml(CONTRACT_PATH)
    engines = registry.get("engines")
    require(isinstance(engines, dict) and engines, "video_engine_duration_contracts.yaml has no engines map")

    for engine_id in ("GROK", "VEO_3_1", "GOOGLE_FLOW"):
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


def validate_review_only_engines(engines: dict[str, Any]) -> list[str]:
    checks: list[str] = []
    for engine_id in ("VEO_3_1", "GOOGLE_FLOW"):
        engine = engines[engine_id]
        require(engine.get("authority_status") == "NEEDS_REVIEW", f"{engine_id} must remain NEEDS_REVIEW until authority is verified")
        require(engine.get("notion_execution_status") != "READY", f"{engine_id} cannot be marked READY without verified authority")
        constraints = engine.get("proposed_constraints") or {}
        require("proposed_single_block_max_seconds" in constraints, f"{engine_id} missing proposed_single_block_max_seconds")
        require("proposed_temporal_bridge" in constraints, f"{engine_id} missing proposed_temporal_bridge")
        checks.append(f"{engine_id} flagged NEEDS_REVIEW")
    return checks


def validate_dialogue_budget_coverage() -> list[str]:
    bundle = load_registry_bundle()
    expected = [6, 10, 12, 16, 18, 20, 30]
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
    review_checks = validate_review_only_engines(engines)
    budget_checks = validate_dialogue_budget_coverage()

    print("VALIDATION PASSED")
    print(f"Video Contract Registry: {CONTRACT_PATH}")
    print(f"Dialogue Budget Registry: {DIALOGUE_BUDGET_PATH}")
    print(f"Handoff Doc: {HANDOFF_DOC_PATH}")
    for item in grok_checks + review_checks + budget_checks:
        print(item)


if __name__ == "__main__":
    main()
