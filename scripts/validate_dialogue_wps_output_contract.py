from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_STRINGS = {
    "docs/video_dialogue_wps_auto_enforcement_v1.md": [
        "all video engines",
        "per-block",
        "UNDERFILLED",
        "hard ceiling",
        "final clean operator-facing prompt",
    ],
    ".claude/skills/bosmax-dialogue-wps-enforcer.md": [
        "GROK",
        "GOOGLE_FLOW",
        "VEO",
        "KLING",
        "SEEDANCE",
        "REWRITE_REQUIRED",
        "BLOCKED",
        "UNDERFILLED",
    ],
    ".claude/skills/bosmax-script-generator.md": [
        "DIALOGUE WPS AUTO-ENFORCEMENT",
        "AVATAR_PRODUCT_UGC",
        "dialogue_required = YES",
        "Do not expose WPS metadata",
    ],
    "docs/agents/BOSMAX_RAW_SEED_TO_FINAL_PROMPT_FLOW_v1.md": [
        "per-block WPS",
        "exact dialogue draft",
        "word count audited",
    ],
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def main() -> None:
    missing_items: list[str] = []

    for relative_path, required_tokens in REQUIRED_STRINGS.items():
        path = ROOT / relative_path
        if not path.exists():
            missing_items.append(f"{relative_path}: file missing")
            continue

        text = path.read_text(encoding="utf-8")
        for token in required_tokens:
            if token not in text:
                missing_items.append(f"{relative_path}: missing required string {token!r}")

    if missing_items:
        for item in missing_items:
            print(item)
        fail("dialogue WPS output contract validation failed")

    print("VALIDATION PASSED")
    for relative_path, required_tokens in REQUIRED_STRINGS.items():
        print(f"{relative_path}: {len(required_tokens)} required strings present")


if __name__ == "__main__":
    main()
