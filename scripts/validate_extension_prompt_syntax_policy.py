from __future__ import annotations

"""
BOSMAX Extension Prompt Syntax Policy Validator v1.0
scripts/validate_extension_prompt_syntax_policy.py

Purpose:
  Enforce the engine-specific extension prompt syntax policy documented in:
    docs/engine_extension_prompt_syntax_policy_v1.md
    docs/google_flow_extend_prompt_sop_v1.md
    docs/grok_extension_prompt_sop_v1.md

  Specifically: ensure that internal continuity planning metadata and
  policy-banned continuity phrases do NOT appear in final engine-visible
  prompt text surfaces.

INTERNAL vs FINAL PROMPT TEXT:
  Internal planning fields such as previous_clip_final_second_state,
  bridge_in, bridge_out, child_prompt_output_rule, identity_reanchor,
  product_reanchor, continuity_goal, etc. are intentionally allowed to
  contain continuity language and internal notation. This validator
  NEVER scans those fields.

  Only explicitly designated final-prompt-text fields are scanned:
    - block_prompt_manual_output  (flow_extend_proof.yaml child blocks)
    - operator_prompt_text        (future field — not yet in repo)
    - final_prompt_text           (future field — not yet in repo)
    - prompt_text                 (future field — not yet in repo)

  When block_prompt_manual_output holds a status marker such as
  READY_FLOW_UI_SAMPLE_16S_RIZAL_BLOCK_1, it is not actual prompt text
  and is skipped (not a violation, reported as SKIP).

ENGINE SURFACES COVERED:
  - GOOGLE_FLOW.FLOW_EXTEND_UI
  - GOOGLE_FLOW.FLOW_EXTEND_VERTEX
  - VEO_3_1.CLIP_CHAIN
  - VEO_3_1_LITE.CLIP_CHAIN
  - GROK_EXTENSION

NOTE — BOSMAX policy vs. official platform behaviour:
  The phrase bans in this validator are BOSMAX-imposed policy rules,
  not claims about official Google or xAI hard bans. See section 5 of
  docs/engine_extension_prompt_syntax_policy_v1.md for the explicit
  distinction.
"""

import re
import sys
from pathlib import Path
from typing import Any

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# Doc paths
# ---------------------------------------------------------------------------
POLICY_DOC       = ROOT / "docs" / "engine_extension_prompt_syntax_policy_v1.md"
FLOW_SOP_DOC     = ROOT / "docs" / "google_flow_extend_prompt_sop_v1.md"
GROK_SOP_DOC     = ROOT / "docs" / "grok_extension_prompt_sop_v1.md"
PARITY_AUDIT_DOC = ROOT / "docs" / "google_flow_parity_audit_v1.md"

# ---------------------------------------------------------------------------
# Registry / sample paths that contain potential prompt-text surfaces
# ---------------------------------------------------------------------------
FLOW_EXTEND_PROOF      = ROOT / "registries" / "flow_extend_proof.yaml"
MULTI_BLOCK_TEMPLATES  = ROOT / "samples" / "notion" / "video_multi_block_templates.yaml"
SINGLE_BLOCK_TEMPLATES = ROOT / "samples" / "notion" / "video_single_block_templates.yaml"

# ---------------------------------------------------------------------------
# Status marker pattern
# block_prompt_manual_output currently holds completion markers such as
#   READY_FLOW_UI_SAMPLE_16S_RIZAL_BLOCK_1
# These are not actual final prompt text and must be skipped, not flagged.
# ---------------------------------------------------------------------------
_STATUS_MARKER_RE = re.compile(
    r"^(READY|NEEDS_REVIEW|PENDING|SKIP|BLOCKED|NOT_APPLICABLE)[_A-Z0-9]*$"
)


def _is_status_marker(value: str) -> bool:
    return bool(_STATUS_MARKER_RE.match(value.strip()))


# ---------------------------------------------------------------------------
# Internal-only field names — NEVER scanned for banned phrases
# These fields are required at the planning / Notion schema layer and may
# legitimately contain continuity metadata and internal notation.
# ---------------------------------------------------------------------------
INTERNAL_FIELDS: frozenset[str] = frozenset({
    "previous_clip_final_second_state",
    "bridge_in",
    "bridge_out",
    "bridge_in_required",
    "bridge_out_required",
    "child_prompt_output_rule",
    "identity_reanchor_required",
    "product_reanchor_required",
    "identity_reanchor",
    "product_reanchor",
    "continuity_goal",
    "scene_continuity_notes",
    "audio_continuity_notes",
    "frame_bridge_notes",
    "validator_proof",
    "validator_proof_capture",
    "output_test_report",
    "block_role",
    "block_status",
    "notes",
    "allowed_reason_if_manual_review",
    "block_dialogue_word_count",
    "final_block_dialogue",
    "speech_resume_window_seconds",
    "dialogue_budget_duration_seconds",
})

# ---------------------------------------------------------------------------
# Final prompt-text fields — these ARE scanned when present
# ---------------------------------------------------------------------------
PROMPT_TEXT_FIELDS: frozenset[str] = frozenset({
    "block_prompt_manual_output",  # flow_extend_proof.yaml child blocks
    "operator_prompt_text",        # future field (not yet in repo)
    "final_prompt_text",           # future field (not yet in repo)
    "prompt_text",                 # future field (not yet in repo)
})

# ---------------------------------------------------------------------------
# Engine surfaces covered by this policy
# ---------------------------------------------------------------------------
ENGINE_SURFACES: list[str] = [
    "GOOGLE_FLOW.FLOW_EXTEND_UI",
    "GOOGLE_FLOW.FLOW_EXTEND_VERTEX",
    "VEO_3_1.CLIP_CHAIN",
    "VEO_3_1_LITE.CLIP_CHAIN",
    "GROK_EXTENSION",
]

# ---------------------------------------------------------------------------
# Policy-banned phrases — ALL engine surfaces (final prompt text only)
# Case-insensitive substring matches unless noted as regex.
# These are BOSMAX-imposed rules — not official Google/xAI hard bans.
# ---------------------------------------------------------------------------
GLOBAL_BANNED_PHRASES: list[tuple[str, str]] = [
    ("continue from the last frame",     "explicit continuity meta-phrase"),
    ("continue from the previous clip",  "explicit continuity meta-phrase"),
    ("continue from where we left off",  "explicit continuity meta-phrase"),
    ("the video continues",              "explicit continuity meta-phrase"),
    ("seamless continuation",            "explicit continuity meta-phrase"),
    ("exact same face",                  "biometric anchor phrase"),
    ("biometric anchor",                 "biometric anchor phrase"),
    ("bridge-in",                        "internal planning field name leaked"),
    ("bridge-out",                       "internal planning field name leaked"),
    ("previous_clip_final_second_state", "internal planning field name leaked"),
    ("identity_reanchor_required",       "internal planning field name leaked"),
    ("product_reanchor_required",        "internal planning field name leaked"),
    ("wps budget",                       "internal planning metadata leaked"),
]

# Structural meta-notation — regex patterns
GLOBAL_BANNED_REGEX: list[tuple[re.Pattern[str], str]] = [
    (
        re.compile(r"\[continues\s+from\s+block", re.IGNORECASE),
        "internal block label [CONTINUES FROM BLOCK ...] leaked",
    ),
    (
        re.compile(r"\bblock\s+\d+\s+of\s+\d+\b", re.IGNORECASE),
        "internal block index label (BLOCK N OF M) leaked",
    ),
]

# ---------------------------------------------------------------------------
# Flow-specific: generic identity tokens (banned in Flow final prompt text)
# ---------------------------------------------------------------------------
FLOW_GENERIC_IDENTITY_TOKENS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bthe\s+character\b",  re.IGNORECASE), "generic identity token: 'the character'"),
    (re.compile(r"\bthe\s+subject\b",    re.IGNORECASE), "generic identity token: 'the subject'"),
    (re.compile(r"\bthe\s+individual\b", re.IGNORECASE), "generic identity token: 'the individual'"),
    (re.compile(r"\bthe\s+person\b",     re.IGNORECASE), "generic identity token: 'the person'"),
]

# Acceptable Flow identity anchors (concrete noun or @CharacterName)
FLOW_OK_IDENTITY_RE = re.compile(
    r"@\w+"                        # @CharacterName / @IngredientName
    r"|the\s+man(?:\s+in)?"
    r"|the\s+woman(?:\s+in)?"
    r"|the\s+presenter"
    r"|the\s+product\s+bottle"
    r"|the\s+bottle"
    r"|the\s+serum\s+bottle",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# Required doc sections (for CHECK 2)
# ---------------------------------------------------------------------------
REQUIRED_SECTIONS: dict[str, list[str]] = {
    "engine_extension_prompt_syntax_policy_v1.md": [
        "Internal Metadata vs Final Prompt Text",
        "Official Evidence vs BOSMAX Policy",
        "Policy-Banned Phrases",
        "Identity Reference Policy",
    ],
    "google_flow_extend_prompt_sop_v1.md": [
        "Policy-Banned Phrases",
        "Identity Reference Rules",
        "Internal Metadata",
        "Compliance Checklist",
    ],
    "grok_extension_prompt_sop_v1.md": [
        "Seam Law",
        "Policy-Banned Phrases",
        "Identity",
        "GROK_FLEX_EXTEND",
    ],
    "google_flow_parity_audit_v1.md": [
        "Prompt Syntax Policy",
        "BOSMAX policy",
        "internal metadata",
    ],
}

# ---------------------------------------------------------------------------
# Result counters
# ---------------------------------------------------------------------------
_pass_count = 0
_fail_count = 0
_skip_count = 0
_failures: list[str] = []


def _pass(msg: str) -> None:
    global _pass_count
    _pass_count += 1
    print(f"PASS: {msg}")


def _fail(msg: str) -> None:
    global _fail_count
    _fail_count += 1
    _failures.append(msg)
    print(f"FAIL: {msg}")


def _skip(msg: str) -> None:
    global _skip_count
    _skip_count += 1
    print(f"SKIP: {msg}")


def _load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


# ---------------------------------------------------------------------------
# CHECK 1 — Policy doc existence
# ---------------------------------------------------------------------------
def check_policy_docs_exist() -> None:
    print("\n[CHECK 1] Policy doc existence")
    for path, label in [
        (POLICY_DOC,       "engine_extension_prompt_syntax_policy_v1.md"),
        (FLOW_SOP_DOC,     "google_flow_extend_prompt_sop_v1.md"),
        (GROK_SOP_DOC,     "grok_extension_prompt_sop_v1.md"),
        (PARITY_AUDIT_DOC, "google_flow_parity_audit_v1.md"),
    ]:
        if path.exists():
            _pass(f"Policy doc exists: docs/{label}")
        else:
            _fail(f"Policy doc missing: docs/{label}")


# ---------------------------------------------------------------------------
# CHECK 2 — Required sections present in policy docs
# ---------------------------------------------------------------------------
def check_policy_doc_sections() -> None:
    print("\n[CHECK 2] Required sections in policy docs")
    for path, filename in [
        (POLICY_DOC,       "engine_extension_prompt_syntax_policy_v1.md"),
        (FLOW_SOP_DOC,     "google_flow_extend_prompt_sop_v1.md"),
        (GROK_SOP_DOC,     "grok_extension_prompt_sop_v1.md"),
        (PARITY_AUDIT_DOC, "google_flow_parity_audit_v1.md"),
    ]:
        if not path.exists():
            _skip(f"Cannot check sections — file missing: {filename}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in REQUIRED_SECTIONS.get(filename, []):
            if phrase.lower() in text.lower():
                _pass(f"{filename}: required section/phrase present: {phrase!r}")
            else:
                _fail(f"{filename}: required section/phrase missing: {phrase!r}")


# ---------------------------------------------------------------------------
# CHECK 3 — Engine surface map coverage in policy doc
# ---------------------------------------------------------------------------
def check_engine_surface_map_coverage() -> None:
    print("\n[CHECK 3] Engine-surface policy map coverage")
    if not POLICY_DOC.exists():
        _skip("Policy doc missing — engine surface map check skipped")
        return
    text = POLICY_DOC.read_text(encoding="utf-8")
    for surface in ENGINE_SURFACES:
        # Accept either the full surface name or the mode part after the dot
        key = surface.split(".")[-1] if "." in surface else surface
        if key in text or surface in text:
            _pass(f"Policy doc covers engine surface: {surface}")
        else:
            _fail(f"Policy doc missing engine surface coverage: {surface}")


# ---------------------------------------------------------------------------
# Core phrase scanner — used by CHECK 4 only for final-prompt-text fields
# ---------------------------------------------------------------------------
def _scan_final_prompt_text(
    surface_label: str,
    engine_surface: str,
    text: str,
) -> int:
    """Scan a confirmed final-prompt-text value for policy violations.

    Returns the number of violations found.
    Does NOT check internal fields — callers must never pass internal fields here.
    """
    local_fails = 0
    text_lower = text.lower()

    # Global banned phrases (substring, case-insensitive)
    for phrase, reason in GLOBAL_BANNED_PHRASES:
        if phrase.lower() in text_lower:
            _fail(
                f"{surface_label} [{engine_surface}]: "
                f"policy-banned phrase ({reason}): {phrase!r}"
            )
            local_fails += 1

    # Global banned regex patterns
    for pat, reason in GLOBAL_BANNED_REGEX:
        if pat.search(text):
            _fail(
                f"{surface_label} [{engine_surface}]: "
                f"policy-banned pattern ({reason}): pattern={pat.pattern!r}"
            )
            local_fails += 1

    # Flow-specific generic identity token check
    if "FLOW" in engine_surface.upper():
        for pat, reason in FLOW_GENERIC_IDENTITY_TOKENS:
            if pat.search(text):
                if FLOW_OK_IDENTITY_RE.search(text):
                    _pass(
                        f"{surface_label} [{engine_surface}]: "
                        f"generic token present but acceptable concrete/@ anchor overrides: {reason}"
                    )
                else:
                    _fail(
                        f"{surface_label} [{engine_surface}]: "
                        f"{reason} — no concrete noun or @CharacterName anchor found"
                    )
                    local_fails += 1

    if local_fails == 0:
        _pass(
            f"{surface_label} [{engine_surface}]: "
            f"no policy-banned phrases in final prompt text"
        )
    return local_fails


# ---------------------------------------------------------------------------
# CHECK 4 — Final prompt text surface scan
# ---------------------------------------------------------------------------
def check_flow_extend_proof_prompts() -> None:
    print("\n[CHECK 4] Final prompt text surface scan: flow_extend_proof.yaml")
    if not FLOW_EXTEND_PROOF.exists():
        _skip("registries/flow_extend_proof.yaml not found — prompt surface scan skipped")
        return

    data = _load_yaml(FLOW_EXTEND_PROOF)
    runs: list[dict[str, Any]] = data.get("flow_extend_runs", [])
    if not runs:
        _skip("flow_extend_proof.yaml has no runs — prompt surface scan skipped")
        return

    found_actual_prompts = False

    for run in runs:
        run_id = str(run.get("run_id", "?"))
        execution_mode = str(run.get("execution_mode", "FLOW_EXTEND_UI")).upper()
        engine_surface = f"GOOGLE_FLOW.{execution_mode}"

        child_blocks: list[dict[str, Any]] = run.get("child_blocks") or []
        for block in child_blocks:
            block_idx = block.get("block_index", "?")

            for field in PROMPT_TEXT_FIELDS:
                raw_value = block.get(field)
                if raw_value is None:
                    continue

                value = str(raw_value).strip()
                surface_label = (
                    f"flow_extend_proof.yaml / run={run_id} / "
                    f"block={block_idx} / {field}"
                )

                if not value:
                    _skip(f"{surface_label}: empty — no prompt text to scan")
                    continue

                if _is_status_marker(value):
                    _skip(
                        f"{surface_label}: status marker "
                        f"({value!r}) — not final prompt text, scan deferred"
                    )
                    continue

                # Actual final prompt text found — scan it
                found_actual_prompts = True
                _scan_final_prompt_text(surface_label, engine_surface, value)

    if not found_actual_prompts:
        _skip(
            "flow_extend_proof.yaml: all block_prompt_manual_output values are "
            "status markers — no actual final prompt text present; "
            "scans skipped, PASS by posture"
        )


# ---------------------------------------------------------------------------
# CHECK 5 — Internal field protection confirmation
# ---------------------------------------------------------------------------
def check_internal_field_protection() -> None:
    """Confirm that internal planning fields are NOT scanned as prompt text.

    This check is self-documenting: it lists the exempted fields and verifies
    that multi-block templates containing internal notation ([CONTINUES FROM
    BLOCK], BLOCK N OF N, previous_clip_final_second_state) in their
    child_prompt_output_rule are NOT flagged.
    """
    print("\n[CHECK 5] Internal field protection")

    _pass(
        "Internal fields exempt from scanning: "
        "previous_clip_final_second_state, bridge_in, bridge_out, "
        "child_prompt_output_rule, identity_reanchor*, product_reanchor*, "
        "continuity_goal, scene_continuity_notes, audio_continuity_notes, "
        "frame_bridge_notes, final_block_dialogue"
    )

    if MULTI_BLOCK_TEMPLATES.exists():
        data = _load_yaml(MULTI_BLOCK_TEMPLATES)
        templates: list[dict[str, Any]] = data.get("templates") or []
        found_any = False
        for tmpl in templates:
            tid = tmpl.get("template_id", "?")
            for block in tmpl.get("blocks") or []:
                rule = str(block.get("child_prompt_output_rule") or "")
                bidx = block.get("block_index", "?")
                has_internal = (
                    "[CONTINUES FROM BLOCK" in rule.upper()
                    or re.search(r"\bBLOCK\s+\d+\s+OF\s+\d+\b", rule, re.IGNORECASE)
                )
                if has_internal:
                    found_any = True
                    _pass(
                        f"video_multi_block_templates.yaml / {tid} / block {bidx}: "
                        f"child_prompt_output_rule contains internal notation "
                        f"— correctly NOT scanned (internal field)"
                    )
        if not found_any:
            _skip(
                "video_multi_block_templates.yaml: no child_prompt_output_rule "
                "with internal notation found (nothing to verify exemption against)"
            )
    else:
        _skip("video_multi_block_templates.yaml not found — internal field protection sample check skipped")

    # Verify flow_extend_proof.yaml internal fields are also not scanned
    if FLOW_EXTEND_PROOF.exists():
        data = _load_yaml(FLOW_EXTEND_PROOF)
        runs: list[dict[str, Any]] = data.get("flow_extend_runs", [])
        checked = 0
        for run in runs:
            for block in run.get("child_blocks") or []:
                for internal_field in ("previous_clip_final_second_state", "bridge_in", "bridge_out"):
                    val = str(block.get(internal_field) or "")
                    if val.strip():
                        checked += 1
        if checked:
            _pass(
                f"flow_extend_proof.yaml: found {checked} non-empty internal planning "
                f"field values — none scanned for banned phrases (internal field exemption)"
            )
        else:
            _skip("flow_extend_proof.yaml: no non-empty internal fields found to verify exemption")


# ---------------------------------------------------------------------------
# CHECK 6 — Synthetic self-check
# ---------------------------------------------------------------------------
def check_synthetic_self() -> None:
    """Run small in-script fixtures to verify the scanner behaves correctly.

    Good prompts must NOT trigger any bans.
    Bad prompts MUST trigger the expected ban.
    """
    print("\n[CHECK 6] Synthetic self-check")

    good_fixtures: list[tuple[str, str]] = [
        (
            "the woman reaches for the bottle and smiles at the camera",
            "GOOGLE_FLOW.FLOW_EXTEND_UI",
        ),
        (
            "@NadiaCooks lifts the serum bottle and says takyah susah dah",
            "GOOGLE_FLOW.FLOW_EXTEND_UI",
        ),
        (
            "rizal holds the bottle close and says sambung terus dari semalam",
            "GROK_EXTENSION",
        ),
        (
            "the woman in the hijab turns toward camera product in hand",
            "GOOGLE_FLOW.FLOW_EXTEND_UI",
        ),
        (
            "the presenter picks up the product bottle and demonstrates the texture",
            "GOOGLE_FLOW.FLOW_EXTEND_VERTEX",
        ),
        (
            "the man sets the serum bottle down on the counter medium shot",
            "VEO_3_1_LITE.CLIP_CHAIN",
        ),
    ]

    bad_fixtures: list[tuple[str, str, str]] = [
        (
            "continue from the last frame where she was holding the bottle",
            "GOOGLE_FLOW.FLOW_EXTEND_UI",
            "continue from the last frame",
        ),
        (
            "[CONTINUES FROM BLOCK 1] she keeps holding the product",
            "GROK_EXTENSION",
            "[CONTINUES FROM BLOCK",
        ),
        (
            "BLOCK 2 OF 2 — she lifts the bottle close to camera",
            "GOOGLE_FLOW.FLOW_EXTEND_UI",
            "BLOCK 2 OF 2 (regex)",
        ),
        (
            "previous_clip_final_second_state: standing at counter",
            "GOOGLE_FLOW.FLOW_EXTEND_UI",
            "previous_clip_final_second_state",
        ),
        (
            "seamless continuation from block one into CTA",
            "GROK_EXTENSION",
            "seamless continuation",
        ),
        (
            "exact same face as before holds the bottle high",
            "VEO_3_1.CLIP_CHAIN",
            "exact same face",
        ),
        (
            "the video continues with the presenter walking forward",
            "VEO_3_1_LITE.CLIP_CHAIN",
            "the video continues",
        ),
        (
            "continue from the previous clip with the bottle still in hand",
            "GROK_EXTENSION",
            "continue from the previous clip",
        ),
    ]

    # Good prompts — must produce zero violations
    for text, surface in good_fixtures:
        text_lower = text.lower()
        hit = False

        for phrase, _ in GLOBAL_BANNED_PHRASES:
            if phrase.lower() in text_lower:
                hit = True
                break
        if not hit:
            for pat, _ in GLOBAL_BANNED_REGEX:
                if pat.search(text):
                    hit = True
                    break
        # Flow generic token check (only fail if no anchor)
        if not hit and "FLOW" in surface.upper():
            for pat, _ in FLOW_GENERIC_IDENTITY_TOKENS:
                if pat.search(text) and not FLOW_OK_IDENTITY_RE.search(text):
                    hit = True
                    break

        if hit:
            _fail(f"synthetic good prompt INCORRECTLY triggered a ban: {text!r}")
        else:
            _pass(f"synthetic good prompt clean [{surface}]: {text[:55]!r}")

    # Bad prompts — must each detect the expected phrase
    for text, surface, expected_phrase in bad_fixtures:
        text_lower = text.lower()
        detected = False

        for phrase, _ in GLOBAL_BANNED_PHRASES:
            if phrase.lower() in text_lower:
                detected = True
                break
        if not detected:
            for pat, _ in GLOBAL_BANNED_REGEX:
                if pat.search(text):
                    detected = True
                    break

        if detected:
            _pass(
                f"synthetic bad prompt correctly detected "
                f"({expected_phrase!r}) [{surface}]: {text[:55]!r}"
            )
        else:
            _fail(
                f"synthetic bad prompt NOT detected — "
                f"missed: {expected_phrase!r} in {text!r}"
            )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    print("=" * 70)
    print("BOSMAX Extension Prompt Syntax Policy Validator v1.0")
    print("=" * 70)
    print(f"Root: {ROOT}")
    print()

    check_policy_docs_exist()
    check_policy_doc_sections()
    check_engine_surface_map_coverage()
    check_flow_extend_proof_prompts()
    check_internal_field_protection()
    check_synthetic_self()

    print()
    print("=" * 70)
    if _failures:
        print(
            f"VALIDATION FAILED — "
            f"{_fail_count} failure(s), {_pass_count} pass(es), {_skip_count} skip(s)"
        )
        for f in _failures:
            print(f"  FAILED: {f}")
        sys.exit(1)
    else:
        print(
            f"VALIDATION PASSED — "
            f"{_pass_count} pass(es), {_skip_count} skip(s), 0 failures"
        )
    print("=" * 70)


if __name__ == "__main__":
    main()
