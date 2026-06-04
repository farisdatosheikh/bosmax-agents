from __future__ import annotations

"""
First-pass structural validator for BOSMAX_EXECUTION_KERNEL_CONTRACT_v1.md.

Checks:
  - BOSMAX_EXECUTION_KERNEL_CONTRACT_v1.md exists
  - Required sections exist (by heading)
  - Registry files referenced exist
  - Validator scripts referenced exist
  - VEO_3_1_LITE parity is resolved — PARTIAL_VERIFIED / READY_CLIP_MODE (PR #4)
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CONTRACT_PATH = ROOT / "BOSMAX_EXECUTION_KERNEL_CONTRACT_v1.md"

REQUIRED_SECTIONS = [
    "## 1. Purpose",
    "## 2. Authority Order",
    "## 3. Kernel Readiness Gates",
    "## 4. ENGINE_DURATION_GATE",
    "## 5. EXECUTION_MODE_GATE",
    "## 6. WPS_DIALOGUE_GATE",
    "## 7. COPY_AUTHORITY_GATE",
    "## 8. PRODUCT_TRUTH_GATE",
    "## 9. AVATAR_SOURCE_GATE",
    "## 10. MULTI_BLOCK_SEAM_GATE",
    "## 11. NOTION_DOWNSTREAM_GATE",
    "## 12. VALIDATOR_PROOF_GATE",
    "## 13. SAMPLE_OUTPUT_GATE",
    "## 14. MERGE_PROOF_GATE",
    "## 15.",  # VEO_3_1_LITE LIVE GAP section
    "## 16.",  # Current Enforcement Matrix
    "## 17.",  # Required Next Validators
    "## 18.",  # Operational Law For AI Agents
    "## 19.",  # Fail-Closed Rules
    "## 20.",  # Relationship To Existing Authority Files
]

REFERENCED_REGISTRIES = [
    "registries/video_engine_duration_contracts.yaml",
    "registries/dialogue_budget_corridor.yaml",
    "registries/stealth_copy_authority_map.yaml",
]

REFERENCED_SCRIPTS = [
    "scripts/validate_video_block_contracts.py",
    "scripts/validate_copywriting_ecosystem.py",
    "scripts/video_block_plan.py",
]

VEO31_LITE_PARITY_MARKERS = [
    "VEO_3_1_LITE",
    "PARTIAL_VERIFIED / READY_CLIP_MODE",
    "previously LIVE GAP",
    "8s per request",
    "7s per block",
    "7s actual-render corridor",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def validate_contract_exists() -> str:
    require(CONTRACT_PATH.exists(), f"BOSMAX_EXECUTION_KERNEL_CONTRACT_v1.md missing: {CONTRACT_PATH}")
    return CONTRACT_PATH.read_text(encoding="utf-8")


def validate_sections(text: str) -> list[str]:
    checks: list[str] = []
    for section in REQUIRED_SECTIONS:
        require(section in text, f"Required section missing from contract: {section!r}")
        checks.append(f"section present: {section.strip()[:60]}")
    return checks


def validate_referenced_files(text: str) -> list[str]:
    checks: list[str] = []
    for rel_path in REFERENCED_REGISTRIES:
        abs_path = ROOT / rel_path
        require(abs_path.exists(), f"Referenced registry missing from repo: {rel_path}")
        require(rel_path in text, f"Contract does not mention referenced registry: {rel_path}")
        checks.append(f"registry exists and referenced: {rel_path}")
    for rel_path in REFERENCED_SCRIPTS:
        abs_path = ROOT / rel_path
        require(abs_path.exists(), f"Referenced validator script missing from repo: {rel_path}")
        require(rel_path in text, f"Contract does not mention referenced script: {rel_path}")
        checks.append(f"script exists and referenced: {rel_path}")
    return checks


def validate_veo31_lite_parity_resolved(text: str) -> list[str]:
    for marker in VEO31_LITE_PARITY_MARKERS:
        require(
            marker in text,
            f"Contract must document VEO_3_1_LITE parity as resolved. Missing: {marker!r}",
        )
    return ["VEO_3_1_LITE parity resolved in kernel contract"]


def validate_authority_order(text: str) -> list[str]:
    require("Notion is downstream UI only" in text, "Contract must state: Notion is downstream UI only")
    require("Notion may NOT" in text, "Contract must declare what Notion may NOT do")
    require("AI-generated prose" in text, "Contract must list AI-generated prose as lowest authority")
    return ["authority order section validated"]


def validate_fail_closed_rules(text: str) -> list[str]:
    key_rules = [
        "ABORT",
        "bridge-out",
        "bridge-in",
        "VALIDATION PASSED",
        "NEEDS_REVIEW",
    ]
    checks: list[str] = []
    for rule in key_rules:
        require(rule in text, f"Contract fail-closed rules missing keyword: {rule!r}")
        checks.append(f"fail-closed keyword present: {rule}")
    return checks


def main() -> None:
    text = validate_contract_exists()
    section_checks = validate_sections(text)
    file_checks = validate_referenced_files(text)
    gap_checks = validate_veo31_lite_parity_resolved(text)
    authority_checks = validate_authority_order(text)
    rule_checks = validate_fail_closed_rules(text)

    print("VALIDATION PASSED")
    print(f"Contract: {CONTRACT_PATH}")
    for item in section_checks + file_checks + gap_checks + authority_checks + rule_checks:
        print(item)


if __name__ == "__main__":
    main()
