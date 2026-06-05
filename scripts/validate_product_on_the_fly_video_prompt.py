from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

from product_on_the_fly_video_prompt import (
    CONTRACT_PATH,
    build_manual_request,
    load_contract,
)


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ROUTE_MODES = [
    "REGISTERED_PRODUCT",
    "FAMILY_MATCHED_PRODUCT",
    "ON_THE_FLY_PRODUCT",
    "REVIEW_ONLY_PRODUCT",
]
COMMAND_CENTRE_DOC = ROOT / "docs" / "notion_bosmax_command_centre_template_v1.md"


def fail(message: str) -> None:
    print(f"VALIDATION FAILED: {message}")
    sys.exit(1)


def expect(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def validate_contract_shape(contract: dict[str, Any]) -> None:
    expect(CONTRACT_PATH.exists(), "product_on_the_fly_video_prompt_contract.yaml missing")
    authority = contract.get("authority", {})
    expect(authority.get("repo_truth") is True, "repo_truth must be true")
    expect(authority.get("notion_downstream_only") is True, "notion_downstream_only must be true")
    expect(authority.get("default_notion_flow") == "COMMAND_CENTRE_PLUG_AND_PLAY", "default_notion_flow drift detected")
    expect(authority.get("legacy_manual_flow") == "LEGACY_EXPERT_MODE", "legacy_manual_flow drift detected")
    expect(authority.get("legacy_manual_override_posture") == "MANUAL_OVERRIDE_REVIEW_ONLY", "legacy_manual_override_posture drift detected")
    field_candidates = authority.get("downstream_output_field_candidates", [])
    expect("AI-Ready Request Manual Output" in field_candidates, "AI-Ready Request Manual Output must remain a field candidate")

    templates = contract.get("route_templates", {})
    for mode in REQUIRED_ROUTE_MODES:
        expect(mode in templates, f"route template missing: {mode}")
    on_the_fly_template = templates["ON_THE_FLY_PRODUCT"]
    expect(on_the_fly_template.get("copywriting_mode") == "SESSION_ONLY_GENERATE", "ON_THE_FLY copywriting_mode drift detected")
    expect(on_the_fly_template.get("registry_writeback") == "FORBIDDEN", "ON_THE_FLY registry_writeback drift detected")
    workflows = contract.get("command_centre_product_workflows", {})
    expect(workflows.get("BOSMAX_SERUM_STEALTH_REGISTERED_PRODUCT", {}).get("copywriting_id") == "BOSMAX_SERUM_CP_0001", "STEALTH workflow copywriting_id drift detected")
    expect(workflows.get("MINYAK_WARISAN_CAP_BURUNG_DIRECT_REGISTERED_PRODUCT", {}).get("copywriting_id") == "CAP_BURUNG_MINYAK_CP_0031", "DIRECT workflow copywriting_id drift detected")
    expect(workflows.get("ON_THE_FLY_SESSION_ONLY_TEMPLATE", {}).get("registry_writeback") == "FORBIDDEN", "SESSION_ONLY workflow registry_writeback drift detected")
    expect(COMMAND_CENTRE_DOC.exists(), "notion_bosmax_command_centre_template_v1.md missing")
    print("contract shape ok")


def validate_registered_example(contract: dict[str, Any]) -> None:
    payload = contract["sample_payloads"]["registered_cap_burung"]
    result = build_manual_request(payload)
    route = result["route_result"]
    text = result["manual_output"]
    expect(route["route_mode"] == "REGISTERED_PRODUCT", "registered sample did not resolve to REGISTERED_PRODUCT")
    expect(result["prompt_module_status"] == "READY_REGISTERED_LIBRARY", "registered sample prompt status mismatch")
    expect("copy_pack_row_id: PRODUCT_MW_CAP_BURUNG_R031" in text, "registered output must anchor to PRODUCT_MW_CAP_BURUNG_R031")
    expect("copy_formula: PAS" in text, "registered output missing formula")
    expect("copy_hook: Kepala dah mula rasa berat?" in text, "registered output missing approved hook")
    expect("session_scope: REUSABLE_REGISTERED_LANE" in text, "registered output missing reusable lane scope")
    print("registered route output ok")


def validate_family_example(contract: dict[str, Any]) -> None:
    payload = contract["sample_payloads"]["family_traditional_remedy"]
    result = build_manual_request(payload)
    route = result["route_result"]
    text = result["manual_output"]
    expect(route["route_mode"] == "FAMILY_MATCHED_PRODUCT", "family sample did not resolve to FAMILY_MATCHED_PRODUCT")
    expect("family_sheet: FAMILY_TRAD_REMEDY_OIL" in text, "family output missing family sheet")
    expect("session_scope: FAMILY_LIBRARY_ONLY" in text, "family output missing family scope")
    expect("Do not pretend exact product-specific truth exists." in text, "family output missing fail-closed family rule")
    print("family route output ok")


def validate_registered_resolver_examples(contract: dict[str, Any]) -> None:
    single_payload = contract["sample_payloads"]["registered_bosmax_resolver_single"]
    single_result = build_manual_request(single_payload)
    single_text = single_result["manual_output"]
    expect(single_result["route_result"]["route_mode"] == "REGISTERED_PRODUCT", "resolver single sample did not remain REGISTERED_PRODUCT")
    expect("copywriting_id: BOSMAX_SERUM_CP_0001" in single_text, "resolver single output missing copywriting ID")
    expect("avatar_context_id: BOSMAX_AVP_0001" in single_text, "resolver single output missing avatar context ID")
    expect("resolved_persona_id: RIZAL" in single_text, "resolver single output missing resolved persona")
    expect("resolved_scene_context_id: CTX_HOME_STEALTH_RESET_001" in single_text, "resolver single output missing scene context")

    batch_payload = contract["sample_payloads"]["registered_bosmax_resolver_batch"]
    batch_result = build_manual_request(batch_payload)
    batch_text = batch_result["manual_output"]
    expect(batch_result["route_result"]["route_mode"] == "REGISTERED_PRODUCT", "resolver batch sample did not remain REGISTERED_PRODUCT")
    expect("avatar_pool_id: BOSMAX_MALE_STEALTH_POOL_001" in batch_text, "resolver batch output missing avatar pool ID")
    expect("rotation_rule: ROUND_ROBIN_NO_REPEAT" in batch_text, "resolver batch output missing rotation rule")
    expect("batch_count: 20" in batch_text, "resolver batch output missing batch count")
    expect("rotation_sequence: BOSMAX_AVP_0001, BOSMAX_AVP_0002" in batch_text, "resolver batch output missing deterministic rotation sequence")
    print("stealth registered resolver output ok")


def validate_registered_direct_resolver_example(contract: dict[str, Any]) -> None:
    payload = contract["sample_payloads"]["registered_mwcb_direct_resolver_single"]
    result = build_manual_request(payload)
    text = result["manual_output"]
    expect(result["route_result"]["route_mode"] == "REGISTERED_PRODUCT", "direct resolver sample did not remain REGISTERED_PRODUCT")
    expect("copywriting_id: CAP_BURUNG_MINYAK_CP_0031" in text, "direct resolver output missing MWCB copywriting ID")
    expect("avatar_context_id: MWCB_DIRECT_AVP_0001" in text, "direct resolver output missing MWCB avatar context ID")
    expect("resolved_persona_id: RIZAL" in text, "direct resolver output missing resolved persona")
    expect("resolved_scene_context_id: CTX_HOME_TRAD_REMEDY_001" in text, "direct resolver output missing MWCB scene context")
    print("direct registered resolver output ok")


def validate_command_centre_doc() -> None:
    text = COMMAND_CENTRE_DOC.read_text(encoding="utf-8")
    required_markers = [
        "BOSMAX Command Centre",
        "Plug & Play Video Prompt Template",
        "Copywriting ID Mini Database",
        "Avatar Context ID Mini Database",
        "Avatar Pool ID Mini Database",
        "Batch Production Template",
        "BOSMAX Serum / STEALTH Registered Product",
        "Minyak Warisan Cap Burung / DIRECT Registered Product",
        "ON_THE_FLY Product / SESSION_ONLY",
        "Legacy Expert Mode / Manual Override Notice",
        "Operator Rules",
        "Avatar Context ID: BOSMAX_AVP_0001",
        "Copywriting ID: BOSMAX_SERUM_CP_0001",
        "Avatar Pool ID: BOSMAX_MALE_STEALTH_POOL_001",
        "NOTION_COMMAND_CENTRE_BOSMAX_STEALTH_COPY_ID_VIEW",
        "NOTION_COMMAND_CENTRE_MWCB_DIRECT_COPY_ID_VIEW",
        "MWCB_DIRECT_AVP_0001",
        "MWCB_DIRECT_AVP_0002",
        "MWCB_TRAD_REMEDY_POOL_001",
        "Copywriting Mode: SESSION_ONLY_GENERATE",
        "Registry Writeback: FORBIDDEN",
        "LEGACY_EXPERT_MODE",
        "MANUAL_OVERRIDE_REVIEW_ONLY",
        "Needs Compliance Review",
    ]
    for marker in required_markers:
        expect(marker in text, f"Command Centre doc missing marker: {marker}")
    print("command centre doc ok")


def validate_on_the_fly_example(contract: dict[str, Any]) -> None:
    payload = contract["sample_payloads"]["on_the_fly_portable_blender"]
    result = build_manual_request(payload)
    route = result["route_result"]
    text = result["manual_output"]
    expect(route["route_mode"] == "ON_THE_FLY_PRODUCT", "on-the-fly sample did not resolve to ON_THE_FLY_PRODUCT")
    expect(result["prompt_module_status"] == "READY_SESSION_ONLY", "on-the-fly sample prompt status mismatch")
    expect("router_output_status: AD_HOC_GENERATED" in text, "on-the-fly output missing AD_HOC_GENERATED status")
    expect("session_scope: AD_HOC_GENERATED_THIS_SESSION_ONLY" in text, "on-the-fly output missing session-only scope")
    expect("copywriting_id: none" in text, "on-the-fly output must explicitly omit copywriting ID")
    expect("copywriting_mode: SESSION_ONLY_GENERATE" in text, "on-the-fly output missing session-only copywriting mode")
    expect("registry_writeback: FORBIDDEN" in text, "on-the-fly output missing forbidden registry writeback")
    expect("Do not write the ad-hoc output back into workbook or approved registry." in text, "on-the-fly output missing no-writeback rule")
    print("on-the-fly session-only output ok")


def validate_review_only_example(contract: dict[str, Any]) -> None:
    payload = contract["sample_payloads"]["review_only_baby_supplement"]
    result = build_manual_request(payload)
    route = result["route_result"]
    text = result["manual_output"]
    expect(route["route_mode"] == "REVIEW_ONLY_PRODUCT", "review-only sample did not resolve to REVIEW_ONLY_PRODUCT")
    expect(result["prompt_module_status"] == "BLOCKED_REVIEW_ONLY", "review-only sample prompt status mismatch")
    expect("prompt_module_status: BLOCKED_REVIEW_ONLY" in text, "review-only output missing blocked status")
    expect("STOP. Do not generate a final AI-ready video prompt for this route." in text, "review-only output missing stop instruction")
    print("review-only route output ok")


def main() -> None:
    contract = load_contract()
    validate_contract_shape(contract)
    validate_registered_example(contract)
    validate_registered_resolver_examples(contract)
    validate_registered_direct_resolver_example(contract)
    validate_command_centre_doc()
    validate_family_example(contract)
    validate_on_the_fly_example(contract)
    validate_review_only_example(contract)
    print("VALIDATION PASSED")


if __name__ == "__main__":
    main()
