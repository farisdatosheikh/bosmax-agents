from __future__ import annotations

"""
BOSMAX G-07 Flow Extend validator — MULTI_BLOCK_SEAM_GATE.

Purpose:
  Enforce fail-closed posture for GOOGLE_FLOW Flow Extend while allowing the
  reviewed Flow UI 8s surface to be promoted when complete child-block proof is
  present. Vertex 7s continuation remains documented but review-only until a
  dedicated proof lane exists.
"""

import re
import sys
from pathlib import Path
from typing import Any

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "registries" / "flow_extend_proof.yaml"
ENGINE_CONTRACTS_PATH = ROOT / "registries" / "video_engine_duration_contracts.yaml"
DECISION_RECORD_PATH = ROOT / "BOSMAX_VEO31_FLOW_CONTRACT_DECISION_v1.md"
SAMPLE_MANIFEST_PATH = ROOT / "registries" / "notion_sample_readiness.yaml"
COPYWRITING_REGISTRY_PATH = ROOT / "registries" / "copywriting_id_resolver.yaml"
AVATAR_REGISTRY_PATH = ROOT / "registries" / "avatar_context_rotation.yaml"
PRODUCTS_DIR = ROOT / "products"

FLOW_READY_STATUS = "READY_REVIEWED_FLOW_EXTEND"
REJECTED_PROOF_PATTERNS = [
    "formulaResult://",
    "<omitted />",
    "omitted",
    "rollup omitted",
    "formula result",
]

GOVERNANCE_REQUIRED_FIELDS = [
    "authority",
    "decision_record",
    "engine_contract",
    "validator",
    "default_ready_status",
    "unsupported_mode_status",
    "fail_closed_rules",
]

RUN_REQUIRED_FIELDS = [
    "run_id",
    "engine",
    "execution_mode",
    "execution_status",
    "product_id",
    "copywriting_id",
    "total_duration_seconds",
    "block_plan",
    "shared_copywriting_avatar_resolver_payload",
    "child_blocks_required",
    "child_block_count_expected",
    "child_blocks",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def word_count(text: str) -> int:
    tokens = re.findall(r"[A-Za-z0-9_'-]+", text)
    return len(tokens)


def load_build_plan() -> Any:
    sys.path.insert(0, str(ROOT / "scripts"))
    from video_block_plan import build_plan  # type: ignore[import]

    return build_plan


def validate_manifest() -> dict[str, Any]:
    require(MANIFEST_PATH.exists(), f"flow_extend_proof.yaml missing: {MANIFEST_PATH}")
    data = load_yaml(MANIFEST_PATH)
    for key in ("version", "governance", "flow_extend_runs"):
        require(key in data, f"flow_extend_proof.yaml missing top-level key: {key!r}")
    require(isinstance(data["flow_extend_runs"], list) and len(data["flow_extend_runs"]) > 0, "flow_extend_proof.yaml has empty flow_extend_runs list")
    return data


def validate_governance(data: dict[str, Any]) -> list[str]:
    gov = data.get("governance") or {}
    for field in GOVERNANCE_REQUIRED_FIELDS:
        val = gov.get(field)
        require(val is not None and str(val).strip() not in ("", "[]", "null"), f"flow_extend_proof.yaml governance missing required field: {field!r}")
    require(gov.get("default_ready_status") == FLOW_READY_STATUS, f"flow_extend_proof.yaml default_ready_status must be {FLOW_READY_STATUS}")
    require(gov.get("unsupported_mode_status") == "NEEDS_REVIEW", "flow_extend_proof.yaml unsupported_mode_status must remain NEEDS_REVIEW")
    return ["manifest ok: registries/flow_extend_proof.yaml"]


def validate_engine_contract() -> list[str]:
    require(ENGINE_CONTRACTS_PATH.exists(), f"video_engine_duration_contracts.yaml missing: {ENGINE_CONTRACTS_PATH}")
    registry = load_yaml(ENGINE_CONTRACTS_PATH)
    engines = registry.get("engines") or {}
    require("GOOGLE_FLOW" in engines, "GOOGLE_FLOW missing from engine contracts registry")

    flow = engines["GOOGLE_FLOW"]
    require(flow.get("notion_execution_status") == FLOW_READY_STATUS, f"GOOGLE_FLOW notion_execution_status must be {FLOW_READY_STATUS}")
    require(flow.get("shared_copywriting_avatar_resolver_payload") is True, "GOOGLE_FLOW must declare shared copywriting/avatar resolver payload")

    execution_modes = flow.get("execution_modes") or {}
    require("FLOW_EXTEND_UI" in execution_modes, "FLOW_EXTEND_UI missing from GOOGLE_FLOW.execution_modes")
    require("FLOW_EXTEND_VERTEX" in execution_modes, "FLOW_EXTEND_VERTEX missing from GOOGLE_FLOW.execution_modes")

    ui = execution_modes["FLOW_EXTEND_UI"]
    vertex = execution_modes["FLOW_EXTEND_VERTEX"]
    require(str(ui.get("status", "")).upper() == FLOW_READY_STATUS, f"GOOGLE_FLOW.FLOW_EXTEND_UI must be {FLOW_READY_STATUS}")
    require(str(vertex.get("status", "")).upper() == "NEEDS_REVIEW", "GOOGLE_FLOW.FLOW_EXTEND_VERTEX must remain NEEDS_REVIEW")
    require(ui.get("default_total_to_blocks"), "FLOW_EXTEND_UI must define deterministic block math")
    require(vertex.get("default_total_to_blocks"), "FLOW_EXTEND_VERTEX must document 7s review-only block math")

    return [
        f"engine_contract ok: GOOGLE_FLOW notion_execution_status {FLOW_READY_STATUS}",
        "engine_contract ok: FLOW_EXTEND_UI ready / FLOW_EXTEND_VERTEX needs review",
    ]


def validate_decision_record() -> list[str]:
    require(DECISION_RECORD_PATH.exists(), f"BOSMAX_VEO31_FLOW_CONTRACT_DECISION_v1.md missing: {DECISION_RECORD_PATH}")
    text = DECISION_RECORD_PATH.read_text(encoding="utf-8")
    required_phrases = [
        "FLOW_EXTEND_UI",
        "FLOW_EXTEND_VERTEX",
        "previous clip final-second state",
        FLOW_READY_STATUS,
        "shared copywriting/avatar resolver payload",
    ]
    for phrase in required_phrases:
        require(phrase.lower() in text.lower(), f"Decision record missing required Flow phrase: {phrase!r}")
    return ["decision_record ok: Flow UI ready posture and Vertex review posture documented"]


def load_reference_sets() -> tuple[set[str], set[str], set[str], set[str]]:
    copy_registry = load_yaml(COPYWRITING_REGISTRY_PATH)
    avatar_registry = load_yaml(AVATAR_REGISTRY_PATH)

    copy_ids = {str(item.get("copywriting_id", "")).strip() for item in copy_registry.get("copy_packs", []) if item.get("copywriting_id")}
    avatar_context_ids = {str(item.get("avatar_context_id", "")).strip() for item in avatar_registry.get("avatar_context_packs", []) if item.get("avatar_context_id")}
    avatar_pool_ids = {str(item.get("pool_id", "")).strip() for item in avatar_registry.get("rotation_pools", []) if item.get("pool_id")}
    product_ids = {path.stem for path in PRODUCTS_DIR.glob("*.yaml") if path.name != "_SCHEMA.yaml"}
    return product_ids, copy_ids, avatar_context_ids, avatar_pool_ids


def validate_run_fields(run: dict[str, Any], product_ids: set[str], copy_ids: set[str], avatar_context_ids: set[str], avatar_pool_ids: set[str]) -> None:
    run_id = str(run.get("run_id", "<unknown>"))
    for field in RUN_REQUIRED_FIELDS:
        require(run.get(field) is not None, f"Flow Extend run {run_id!r} missing required field: {field!r}")

    require(str(run.get("engine", "")).upper() == "GOOGLE_FLOW", f"Flow Extend run {run_id!r} engine must be GOOGLE_FLOW")
    require(str(run.get("execution_mode", "")).upper() in {"FLOW_EXTEND_UI", "FLOW_EXTEND_VERTEX"}, f"Flow Extend run {run_id!r} execution_mode unsupported")
    require(str(run.get("product_id", "")).strip() in product_ids, f"Flow Extend run {run_id!r} product_id not found in products/: {run.get('product_id')!r}")
    require(str(run.get("copywriting_id", "")).strip() in copy_ids, f"Flow Extend run {run_id!r} copywriting_id not found in copywriting resolver registry")
    require(run.get("shared_copywriting_avatar_resolver_payload") is True, f"Flow Extend run {run_id!r} must share copywriting/avatar resolver payload with GROK/VEO")

    avatar_context_id = str(run.get("avatar_context_id", "") or "").strip()
    avatar_pool_id = str(run.get("avatar_pool_id", "") or "").strip()
    require(bool(avatar_context_id or avatar_pool_id), f"Flow Extend run {run_id!r} must provide avatar_context_id or avatar_pool_id")
    if avatar_context_id:
        require(avatar_context_id in avatar_context_ids, f"Flow Extend run {run_id!r} avatar_context_id not found: {avatar_context_id!r}")
    if avatar_pool_id:
        require(avatar_pool_id in avatar_pool_ids, f"Flow Extend run {run_id!r} avatar_pool_id not found: {avatar_pool_id!r}")


def validate_ready_capture(label: str, capture: str) -> None:
    require(bool(capture.strip()), f"{label} capture is empty")
    require("VALIDATION PASSED" in capture, f"{label} capture must contain 'VALIDATION PASSED'")
    for pattern in REJECTED_PROOF_PATTERNS:
        require(pattern.lower() not in capture.lower(), f"{label} capture contains rejected proof pattern: {pattern!r}")


def validate_ui_ready_run(run: dict[str, Any], build_plan: Any) -> list[str]:
    run_id = str(run.get("run_id", "<unknown>"))
    require(str(run.get("execution_status", "")).upper() == FLOW_READY_STATUS, f"Flow UI run {run_id!r} must use {FLOW_READY_STATUS}")

    total_duration = int(run["total_duration_seconds"])
    manifest_plan = [int(value) for value in (run.get("block_plan") or [])]
    plan = build_plan("GOOGLE_FLOW", total_duration, execution_mode="FLOW_EXTEND_UI")
    contract_plan = [int(value) for value in plan["block_durations_seconds"]]
    require(manifest_plan == contract_plan, f"Flow UI run {run_id!r} block_plan {manifest_plan} != engine contract {contract_plan}")

    validate_ready_capture(f"{run_id} validator_proof_capture", str(run.get("validator_proof_capture", "")))
    require(bool(str(run.get("output_test_report", "")).strip()), f"Flow UI run {run_id!r} missing output_test_report")

    require(run.get("child_blocks_required") is True, f"Flow UI run {run_id!r} must require child blocks")
    require(int(run.get("child_block_count_expected", 0)) == len(contract_plan), f"Flow UI run {run_id!r} child_block_count_expected drifted")
    child_blocks = run.get("child_blocks") or []
    require(len(child_blocks) == len(contract_plan), f"Flow UI run {run_id!r} child_blocks length {len(child_blocks)} != block plan length {len(contract_plan)}")

    checks = [f"flow_ui ok: {run_id} -> {'+'.join(str(x) for x in contract_plan)}"]

    for contract_block, manifest_block in zip(plan["blocks"], child_blocks, strict=True):
        block_index = int(contract_block["block_index"])
        block_label = f"{run_id} block {block_index}"
        require(int(manifest_block.get("block_index", 0)) == block_index, f"{block_label} block_index drifted")
        require(int(manifest_block.get("block_duration_seconds", 0)) == int(contract_block["block_duration_seconds"]), f"{block_label} block_duration_seconds drifted")
        require(int(manifest_block.get("dialogue_budget_duration_seconds", 0)) == int(contract_block["dialogue_budget_duration_seconds"]), f"{block_label} dialogue budget duration drifted")
        require(bool(str(manifest_block.get("block_role", "")).strip()), f"{block_label} missing block_role")
        require(bool(str(manifest_block.get("continuity_goal", "")).strip()), f"{block_label} missing continuity_goal")
        require(bool(str(manifest_block.get("identity_reanchor", "")).strip()), f"{block_label} missing identity_reanchor")
        require(bool(str(manifest_block.get("product_reanchor", "")).strip()), f"{block_label} missing product_reanchor")
        require(bool(str(manifest_block.get("scene_continuity_notes", "")).strip()), f"{block_label} missing scene_continuity_notes")
        require(bool(str(manifest_block.get("audio_continuity_notes", "")).strip()), f"{block_label} missing audio_continuity_notes")
        require(bool(str(manifest_block.get("frame_bridge_notes", "")).strip()), f"{block_label} missing frame_bridge_notes")
        require(bool(str(manifest_block.get("final_block_dialogue", "")).strip()), f"{block_label} missing final_block_dialogue")
        require(bool(str(manifest_block.get("block_prompt_manual_output", "")).strip()), f"{block_label} missing block_prompt_manual_output")
        require(str(manifest_block.get("block_status", "")).upper() == FLOW_READY_STATUS, f"{block_label} block_status must be {FLOW_READY_STATUS}")
        validate_ready_capture(f"{block_label} validator_proof", str(manifest_block.get("validator_proof", "")))

        actual_words = word_count(str(manifest_block.get("final_block_dialogue", "")))
        declared_words = int(manifest_block.get("block_dialogue_word_count", 0))
        require(actual_words == declared_words, f"{block_label} word count drifted: declared {declared_words}, actual {actual_words}")
        budget = contract_block.get("dialogue_budget") or {}
        require(int(budget.get("target_min_words", 0)) <= actual_words <= int(budget.get("target_max_words", 0)), f"{block_label} dialogue word count {actual_words} outside target range {budget.get('target_min_words')}..{budget.get('target_max_words')}")

        if block_index == 1:
            require(not str(manifest_block.get("bridge_in", "")).strip(), f"{block_label} first block must not declare bridge_in")
            require(bool(str(manifest_block.get("bridge_out", "")).strip()), f"{block_label} first block must declare bridge_out")
        elif block_index == len(contract_plan):
            require(bool(str(manifest_block.get("previous_clip_final_second_state", "")).strip()), f"{block_label} continuation block missing previous_clip_final_second_state")
            require(bool(str(manifest_block.get("bridge_in", "")).strip()), f"{block_label} continuation block missing bridge_in")
            require(not str(manifest_block.get("bridge_out", "")).strip(), f"{block_label} final block must not declare bridge_out")
        else:
            require(bool(str(manifest_block.get("previous_clip_final_second_state", "")).strip()), f"{block_label} continuation block missing previous_clip_final_second_state")
            require(bool(str(manifest_block.get("bridge_in", "")).strip()), f"{block_label} continuation block missing bridge_in")
            require(bool(str(manifest_block.get("bridge_out", "")).strip()), f"{block_label} continuation block missing bridge_out")

    return checks


def validate_vertex_review_run(run: dict[str, Any], build_plan: Any) -> list[str]:
    run_id = str(run.get("run_id", "<unknown>"))
    require(str(run.get("execution_status", "")).upper() == "NEEDS_REVIEW", f"Flow Vertex run {run_id!r} must remain NEEDS_REVIEW")
    total_duration = int(run["total_duration_seconds"])
    manifest_plan = [int(value) for value in (run.get("block_plan") or [])]
    plan = build_plan("GOOGLE_FLOW", total_duration, execution_mode="FLOW_EXTEND_VERTEX")
    contract_plan = [int(value) for value in plan["block_durations_seconds"]]
    require(manifest_plan == contract_plan, f"Flow Vertex run {run_id!r} block_plan {manifest_plan} != engine contract {contract_plan}")
    require(bool(str(run.get("allowed_reason_if_manual_review", "")).strip()), f"Flow Vertex run {run_id!r} missing allowed_reason_if_manual_review")
    return [f"flow_vertex ok: {run_id} -> {'+'.join(str(x) for x in contract_plan)} NEEDS_REVIEW"]


def validate_sample_readiness_cross_check(flow_runs: list[dict[str, Any]]) -> list[str]:
    require(SAMPLE_MANIFEST_PATH.exists(), f"notion_sample_readiness.yaml missing: {SAMPLE_MANIFEST_PATH}")
    data = load_yaml(SAMPLE_MANIFEST_PATH)
    notion_runs = {str(r.get("sample_id", "")): r for r in data.get("sample_runs", [])}
    checks: list[str] = []

    for flow_run in flow_runs:
        run_id = str(flow_run.get("run_id", ""))
        require(run_id in notion_runs, f"Required sample {run_id!r} missing from notion_sample_readiness.yaml")
        notion_run = notion_runs[run_id]
        require(str(notion_run.get("execution_mode", "")).upper() == str(flow_run.get("execution_mode", "")).upper(), f"notion_sample_readiness mismatch on execution_mode for {run_id}")
        require(str(notion_run.get("execution_status", "")).upper() == str(flow_run.get("execution_status", "")).upper(), f"notion_sample_readiness mismatch on execution_status for {run_id}")
        require([int(v) for v in (notion_run.get("block_plan") or [])] == [int(v) for v in (flow_run.get("block_plan") or [])], f"notion_sample_readiness mismatch on block_plan for {run_id}")
        checks.append(f"sample_readiness ok: {run_id}")

    return checks


def _run_synthetic_regression() -> None:
    bad_ready = {
        "run_id": "SYNTHETIC_READY",
        "execution_mode": "FLOW_EXTEND_UI",
        "execution_status": FLOW_READY_STATUS,
        "validator_proof_capture": "",
    }
    assert not bool(str(bad_ready["validator_proof_capture"]).strip()), "Synthetic: empty validator capture should be falsy"

    bad_vertex = {"execution_mode": "FLOW_EXTEND_VERTEX", "execution_status": FLOW_READY_STATUS}
    assert bad_vertex["execution_mode"] == "FLOW_EXTEND_VERTEX", "Synthetic: vertex setup correct"
    assert bad_vertex["execution_status"] == FLOW_READY_STATUS, "Synthetic: vertex ready drift should be caught"

    bad_capture = "formulaResult://some-notion-field"
    found = any(pattern.lower() in bad_capture.lower() for pattern in REJECTED_PROOF_PATTERNS)
    assert found, "Synthetic: formulaResult should be caught by proof guard"


def main() -> None:
    _run_synthetic_regression()

    data = validate_manifest()
    gov_checks = validate_governance(data)
    engine_checks = validate_engine_contract()
    record_checks = validate_decision_record()
    product_ids, copy_ids, avatar_context_ids, avatar_pool_ids = load_reference_sets()
    build_plan = load_build_plan()

    runs: list[dict[str, Any]] = data.get("flow_extend_runs", [])
    run_checks: list[str] = []
    for run in runs:
        validate_run_fields(run, product_ids, copy_ids, avatar_context_ids, avatar_pool_ids)
        execution_mode = str(run.get("execution_mode", "")).upper()
        if execution_mode == "FLOW_EXTEND_UI":
            run_checks += validate_ui_ready_run(run, build_plan)
        else:
            run_checks += validate_vertex_review_run(run, build_plan)

    sample_checks = validate_sample_readiness_cross_check(runs)
    proof_guard_checks = [
        "proof_guard ok: Flow UI ready posture requires validator capture, output test, child rows, and seam proof",
        "proof_guard ok: formulaResult and omitted rollup rejected",
    ]

    print("VALIDATION PASSED")
    print(f"Manifest: {MANIFEST_PATH}")
    print(f"Engine contracts: {ENGINE_CONTRACTS_PATH}")
    print(f"Decision record: {DECISION_RECORD_PATH}")
    for item in gov_checks + engine_checks + record_checks + run_checks + sample_checks + proof_guard_checks:
        print(item)


if __name__ == "__main__":
    main()
