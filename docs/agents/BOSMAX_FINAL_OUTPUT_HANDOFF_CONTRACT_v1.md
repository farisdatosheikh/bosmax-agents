# BOSMAX Final Output Handoff Contract
# Version: v1.1
# Authority: BOSMAX Systems Architecture
# Status: ACTIVE — wired via prompt-level skill file in PR #30A
# Last updated: 2026-06-08
# Changelog v1.1: Skill file created + orchestrator wired (PR #30A)

---

## 1. CURRENT STATUS

The Final Output Handoff role is **defined by this contract** and **active via a dedicated skill file** as of PR #30A.

- **Skill file:** `.claude/skills/bosmax-final-output-agent.md` — created in PR #30A.
- **Orchestrator wiring:** `.claude/CLAUDE.md` updated in PR #30A — `bosmax-final-output-agent` is now a named step in all 6 route sequences (A, B, C, D, REG image/video paths, BULK) after Compliance Gate returns any terminal state.
- **Current behaviour:** After bosmax-compliance-gate returns any terminal state, `bosmax-final-output-agent` is appointed to format and deliver the clean final output to the operator.

**IMPORTANT — agent nature:** `bosmax-final-output-agent` is a **Claude Code prompt-level skill persona**. It is NOT an autonomous runtime process, NOT a background service, and NOT a self-triggering agent. It executes within a human-initiated Claude Code session only.

---

## 2. ROLE DEFINITION

The Final Output Handoff role sits **between** the compliance gate and the user. It does not audit content — that is the compliance gate's job. It does not generate content — that is the specialist skills' job.

**Its sole responsibility is:** take the compliance-passed output and format it into a clean, operator-ready final delivery.

```
bosmax-compliance-gate → [VERIFICATION PASSED] → Final Output Handoff → USER
```

---

## 3. WHAT THE FINAL USER OUTPUT MUST INCLUDE

Every final delivery to the operator must contain exactly these components:

### Component 1: Final Copy-Paste Prompt Block
- The complete, deployment-ready prompt
- Formatted for the specific engine (9-section, Google Flow block, poster structure, etc.)
- No commentary or explanation embedded inside the prompt text
- Clearly delimited so the operator can copy it without selecting surrounding text

### Component 2: Short QA Status Line
- One line only
- States: VERIFICATION PASSED + the compliance gate audit date/mode
- Example: `QA: VERIFICATION PASSED — Mode A Poster | 2026-06-08`
- Does NOT reproduce the full compliance audit log

### Component 3: Unresolved Gaps (if any)
- Declared only if the compliance gate passed with known limitations
- Each gap stated in one line: what is missing, what the operator must confirm before submitting to generator
- Example: `⚠️ Gap: scale_anchor_descriptor estimated from visual — confirm exact size before submitting`
- If no gaps: this component is omitted entirely

### Component 4: Warnings (if any)
- Declared only if a condition exists that could affect generator output
- Example: `⚠️ Warning: GROK blocks longer than 10s are not supported — prompt split into 2×10s`
- If no warnings: omitted entirely

---

## 4. WHAT MUST BE HIDDEN FROM FINAL USER OUTPUT

The following must NEVER appear in the final delivery to the operator:

```
HIDDEN — INTERNAL ONLY:
  ❌ Internal routing notes (e.g., "BOSMAX routed this to Route B because...")
  ❌ PRE-FLIGHT validation logs (e.g., "CHECK 1 passed, CHECK 2 passed...")
  ❌ Debug JSON blocks (subject_dna, source_image_handoff internal fields)
  ❌ Working metadata (session state variables, null-field declarations)
  ❌ Agent chatter (e.g., "I will now appoint bosmax-compliance-gate...")
  ❌ Contract explanations (e.g., "Per BOSMAX v11.6 CLAUDE.md section 3...")
  ❌ Storyboard working notes (storyboard is an approval step, not a delivery artefact)
  ❌ Master Narrative Brief (internal planning document, not user-facing)
  ❌ WORK ORDER text (internal dispatch instruction, not user-facing)
  ❌ Full compliance audit checklist (summarised to QA status line only)
```

**Operator-facing output must be clean, minimal, and copy-paste ready.**
If the operator wants internal details, they may ask explicitly; they are never surfaced by default.

---

## 5. MULTI-BLOCK OUTPUT FORMAT

For multi-block video requests, each block is delivered separately and clearly labelled:

```
──────────────────────────────────────
BLOCK 1 OF [N] — [engine] [duration]s
──────────────────────────────────────
[Full block 1 prompt — copy-paste ready]

──────────────────────────────────────
BLOCK 2 OF [N] — [engine] [duration]s
──────────────────────────────────────
[Full block 2 prompt — copy-paste ready]

QA: VERIFICATION PASSED — Mode B Multi-block | [date]
⚠️ [Any gaps or warnings]
```

Each block must be independently copy-paste ready. The operator submits each block to the generator as a separate generation request.

---

## 6. NOTION BOUNDARY — ABSOLUTE RULE

The Final Output Handoff role **must never write to Notion** unless the operator has explicitly scoped a Notion-write task in the current session.

Default behaviour:
- Deliver final prompt to operator in the session chat
- Operator manually copies to Notion if desired
- BOSMAX does not initiate, trigger, or automate any Notion write

This rule applies regardless of what Notion templates exist or what previous sessions did. Every Notion write requires explicit operator instruction in the current session.

---

## 7. ABORT HANDLING

If the compliance gate returns ABORT, the Final Output Handoff role must:

1. Surface the exact ABORT reason in clear operator-facing language
2. State what the operator must do to resolve it
3. Suppress the draft prompt entirely — no partial prompt is delivered
4. Wait for operator input before proceeding

```
ABORT FORMAT:
  🚫 ABORT — [exact reason]
  Resolution: [what operator must do]
  [No prompt delivered until resolved]
```

---

## 8. IMPLEMENTATION — COMPLETED PR #30A

The following changes landed in PR #30A:

| Item | Status |
|------|--------|
| `.claude/skills/bosmax-final-output-agent.md` | CREATED — prompt-level skill persona; reads this contract as authority |
| `.claude/CLAUDE.md` | UPDATED — `bosmax-final-output-agent` inserted as named step in all 6 route sequences after Compliance Gate returns any terminal state |
| `docs/agents/BOSMAX_AGENT_ROLE_INVENTORY_v1.md` | UPDATED — Unit 13 added; inventory count updated to 14 units |
| `docs/agents/BOSMAX_COWORK_AGENT_ORCHESTRATION_CONTRACT_v1.md` | UPDATED — placeholder replaced with named skill reference |

**Remaining note:** This is a prompt-level skill persona implementation. It does not constitute full production-scale activation or autonomous agent deployment.
