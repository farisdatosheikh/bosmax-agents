# BOSMAX RUNTIME STATE MACHINE v1
# Architecture Authority: BOSMAX Production Kernel
# Authors: Codex + Claude Cowork (shake-hand consensus)
# Status: CANONICAL — all skills and CLAUDE.md defer to this document
# Version: v1.0 | Date: 2026-06-03

---

## 1. PURPOSE

This document replaces prose-based orchestration with a deterministic state machine.

BOSMAX is no longer a "document collection that an AI reads".
BOSMAX is a **runtime system with enforced execution order**.

Every request passes through mandatory states.
Every state produces a validated packet.
No state can be skipped.
No worker can route itself.
No output reaches the user without passing the final gate.

---

## 2. KERNEL AUTHORITY

The **BOSMAX Kernel** is the single runtime authority.

Only the Kernel may:
- open a new request session
- create the session state object
- authorize state transitions
- assign which worker runs next
- surface questions to the user (on behalf of workers)
- receive user answers and inject into state
- release final output to the user
- mark a session ABORTED

**No worker may:**
- route itself to another worker
- modify any upstream packet
- emit output directly to the user
- skip a required state
- start without Kernel authorization

Violation of any Kernel authority rule = immediate `STATE_ABORTED`.

---

## 3. SESSION OBJECT

Every request opens exactly one session. The session carries all state.

```yaml
session:
  session_id:           string          # unique per request
  schema_version:       "v1"
  opened_at:            timestamp
  task_mode:            null            # IMAGE | VIDEO
  current_state:        STATE_INTAKE
  state_history:        []
  user_approval_needed: false
  user_approval_received: false
  packets:
    intake_packet:              null
    visual_truth_packet:        null
    route_decision_packet:      null
    engine_plan_packet:         null    # VIDEO lane only
    storyboard_packet:          null    # VIDEO lane only
    composition_packet:         null    # IMAGE lane only
    prompt_blocks_packet:       null
    compliance_report_packet:   null
    final_output_packet:        null
  abort_reason:         null
  released_to_user:     false
```

---

## 4. STATES

### STATE_INTAKE
**Entry point for every request.**

Kernel actions:
- parse raw user input
- detect uploaded assets (images, video, frames)
- detect modality hint from text (image/video/poster/repair)
- detect platform hint
- detect language hint
- populate `intake_packet`

Gate condition: `intake_packet.status == VALID`

Required intake_packet fields (see HANDOFF_SCHEMA):
- `raw_request`
- `detected_assets[]`
- `detected_modality_hint`
- `platform_hint`
- `language_hint`

Transitions:
- Assets detected → `STATE_ASSET_ANALYSIS`
- No assets, modality clear → `STATE_ROUTE_RESOLVED`
- Modality unclear → Kernel surfaces ONE question, holds state

Fail condition: required fields unresolvable → `STATE_ABORTED`

---

### STATE_ASSET_ANALYSIS
**Asset Intelligence Worker runs here.**

Input: `intake_packet`
Output: `visual_truth_packet`

Worker scope (strictly bounded):
- scan all uploaded images/frames as primary source
- identify avatar(s): extract visual DNA, lock as USER_UPLOAD
- identify product(s): read label/text visible in image
- classify each asset by type
- estimate scale from hand/body reference in image
- cross-check product against `products/*.yaml` registry
- build `sandbox_visual_stub` if product not in registry but label is clear

**HARD RULE: Worker reads uploaded assets directly. Session memory and user text are SECONDARY. Visual evidence is PRIMARY.**

**HARD RULE: Worker does NOT assume product identity from text if image shows different product.**

Gate condition: `visual_truth_packet.status == VALID`

Blocker: if `ambiguous_items` non-empty → Kernel surfaces ONE question to user, holds state until resolved.

Fail condition: assets in `intake_packet` but worker returns null scan → `STATE_ABORTED`

Transitions:
- VALID packet → `STATE_ROUTE_RESOLVED`

---

### STATE_ROUTE_RESOLVED
**Route Resolver Worker runs here.**

Input: `intake_packet` + `visual_truth_packet`
Output: `route_decision_packet`

Worker scope (strictly bounded):
- determine `task_mode`: IMAGE | VIDEO
- determine `content_type`: UGC | PGC | HYBRID
- determine `image_goal` (IMAGE): VIDEO_SUPPORT | SELLING_POSTER
- determine `reference_mode` (VIDEO): NONE | IMAGE_REFERENCE | VIDEO_REFERENCE | BOSMAX_IMAGE_HANDOFF
- determine `route`: A | B | C | D | REG | BULK | REPAIR
- determine `risk_class`: DIRECT | SENSITIVE | HOUSEHOLD | TRADITIONAL | WELLNESS
- confirm `platform` and `language`

Gate condition: `route_decision_packet.status == VALID`

Fail condition: `task_mode` cannot be determined → `STATE_ABORTED`

Transitions:
- VIDEO → `STATE_ENGINE_PLANNED`
- IMAGE → `STATE_COMPOSITION_DIRECTED`

---

### STATE_ENGINE_PLANNED
**Engine Planner Worker runs here. VIDEO lane only.**

Input: `route_decision_packet`
Output: `engine_plan_packet`

Worker scope (strictly bounded):
- confirm or suggest engine (from user declaration or content_type + platform heuristic)
- validate engine exists in `ENGINE_CONSTRAINT_TABLE`
- calculate block math
- determine `content_mode`: T2V | FRAMES | INGREDIENTS | IMAGE
- lock block durations
- declare WPS budget per block (from language WPS table)
- declare `pace_class`

**GROK hard-default block math (non-negotiable unless operator explicitly overrides):**
```
12s  → 6s + 6s          (only valid combination)
16s  → 10s + 6s         (only valid combination)
18s  → 6s + 6s + 6s     (only valid combination)
20s  → 10s + 10s        (default)
30s  → 10s + 10s + 10s  (default — alternate 5×6s only on explicit request)
```

**VEO_3_1_LITE:** fixed 8s per block. Dialog budget uses 7s (actual render).
**KLING_3_0:** max 15s per block.
**SEEDANCE_2_0:** max 15s per block.

Gate condition: `engine_plan_packet.status == VALID`

Blocker: if GROK multi-option and operator hasn't confirmed → Kernel surfaces choice, holds state.

Fail condition: engine not in `ENGINE_CONSTRAINT_TABLE` → `STATE_ABORTED`

Transitions:
- VALID packet → `STATE_STORYBOARD_BUILT`

---

### STATE_STORYBOARD_BUILT
**Storyboard Director Worker runs here. VIDEO lane only.**
**This is the most critical worker in the VIDEO pipeline.**

Input: `visual_truth_packet` + `route_decision_packet` + `engine_plan_packet`
Output: `storyboard_packet`

Worker scope (strictly bounded):
- select `copy_formula`: SELL_THROUGH_HPFRC | STORY_HSARC
- build full copy arc:
  - SELL_THROUGH_HPFRC: Hook → Pain → Friction → Relief → CTA
  - STORY_HSARC: Hook → Setup → Agitate → Relief → CTA
- write full dialogue arc as one continuous narrative (all blocks)
- slice dialogue per block, validate each slice ≤ WPS budget from `engine_plan_packet`
- build shot ladder per block: ECU / CU / MCU / MS / WS / POV / OTS / TOP_DOWN
- assign product moment timing per block
- write `bridge_out` phrase for Block N → Block N+1
- write `bridge_in` phrase for Block N+1 (resumes within 0.5s–1.0s for GROK)
- declare end state visual per block

**HARD RULE: Worker may NOT modify `visual_truth_packet`. Product truth from visual scan is immutable.**

**HARD RULE: BM commercial / UGC / TikTok recommendation MUST have dialogue. `pure visual` / `WPS: 0` FORBIDDEN unless user explicitly requests silent montage.**

**HARD RULE: Hook MUST appear in the first spoken line. Pain/friction MUST precede product payoff.**

Gate condition: `storyboard_packet.status == VALID` AND `user_approval_received == true`

Kernel action at this gate: surface storyboard to user, set `user_approval_needed = true`, hold state. Release only after user approves (or requests revision).

Fail condition: dialogue empty for BM commercial UGC → `STATE_ABORTED`
Fail condition: word_count exceeds WPS → AUTO-HEAL trim → re-validate

Transitions:
- Approved → `STATE_PROMPTS_COMPILED`
- User requests revision → Worker revises, re-surfaces, holds

---

### STATE_COMPOSITION_DIRECTED
**Poster Composition Director Worker runs here. IMAGE lane only.**

Input: `visual_truth_packet` + `route_decision_packet`
Output: `composition_packet`

Worker scope:
- determine selling hierarchy: product position, avatar position, text zones
- determine copy hierarchy: headline → subhead → CTA
- determine background/scene class
- set platform-specific negative locks
- declare scale anchor from `visual_truth_packet`

**HARD RULE: Worker may NOT modify `visual_truth_packet`.**

Gate condition: `composition_packet.status == VALID`

Transitions:
- VALID packet → `STATE_PROMPTS_COMPILED`

---

### STATE_PROMPTS_COMPILED
**Prompt Compiler Worker runs here.**
**THIS WORKER RENDERS ONLY. NO CREATIVE THINKING PERMITTED.**

Input (VIDEO): `storyboard_packet` + `engine_plan_packet` + `visual_truth_packet`
Input (IMAGE): `composition_packet` + `visual_truth_packet`
Output: `prompt_blocks_packet`

Worker scope:
- compile structured packets into engine-specific prompt format
- inject avatar DNA from `visual_truth_packet`
- inject product scale anchor from `visual_truth_packet`
- inject `bridge_in` / `bridge_out` phrases from `storyboard_packet`
- apply engine-specific syntax rules (GROK format ≠ Google Flow format ≠ Kling format)
- set `overlay_flag = NO_OVERLAY` by default
- output one prompt block per storyboard block

**HARD RULE: Compiler cannot change the story. Cannot change dialogue. Cannot change product truth. RENDER ONLY.**

**HARD RULE: No metadata, debug labels, internal control prose in output.**

Gate condition: `prompt_blocks_packet.status == VALID`

Fail condition: `overlay_flag ≠ NO_OVERLAY` without explicit operator request → AUTO-HEAL set NO_OVERLAY

Transitions:
- VALID packet → `STATE_COMPLIANCE_CHECKED`

---

### STATE_COMPLIANCE_CHECKED
**Compliance Auditor Worker runs here.**

Input: all upstream packets + `prompt_blocks_packet`
Output: `compliance_report_packet`

Full audit checklist (every item must PASS):

**Visual truth checks:**
```
☐ visual_truth_packet was produced (not null)
☐ no registry default used when uploaded image was available
☐ product identity derived from visual label (not from text/memory)
☐ avatar source = USER_UPLOAD when image was uploaded
☐ no registry persona name in avatar DNA
```

**Engine checks:**
```
☐ engine is in ENGINE_CONSTRAINT_TABLE
☐ block_count is valid for engine
☐ block_durations are valid for engine
☐ no monolithic prompt when multiple blocks required
☐ GROK: every block duration is 6s or 10s only
☐ GROK: no fake extension math (no 8s, no 12s base+ext invented)
```

**Storyboard checks (VIDEO):**
```
☐ storyboard_packet exists and user_approved = true
☐ WPS per block ≤ declared budget
☐ dialogue present for BM commercial / UGC / TikTok recommendation
☐ copy_formula declared
☐ hook present in first spoken line
☐ pain/friction present before product payoff
☐ reason-to-believe present before CTA
☐ bridge_out declared for all non-final blocks
☐ bridge_in declared for all non-first blocks
☐ end_state_visual declared per block
```

**Output shape checks:**
```
☐ overlay_flag = NO_OVERLAY (or explicit operator request on file)
☐ no metadata / debug scaffolding leaked in prompt text
☐ no internal BOSMAX labels in operator-facing content
☐ final output uses CHATGPT_CLEAN_VIDEO_ROLE_MODEL shape
```

**Product truth checks:**
```
☐ product scale matches visual_truth_packet scale_estimate
☐ product packaging matches visual_truth_packet packaging_summary
☐ no product substitution (e.g., BOSMAX Serum replacing Air Cushion)
```

Verdict:
- ALL PASS → `compliance_report_packet.verdict = PASS` → `STATE_OUTPUT_READY`
- FIXABLE FAIL → AUTO-HEAL → re-audit
- CRITICAL FAIL → `compliance_report_packet.verdict = ABORT` → `STATE_ABORTED`

Auto-healable failures:
- WPS over limit → trim dialogue
- `overlay_flag` wrong → reset NO_OVERLAY
- bridge_in missing → inject from `GROK_EXTENSION_SEAM_TEMPLATES`
- metadata leaked → strip internal labels

Non-healable (force ABORT):
- storyboard missing for VIDEO
- engine not in registry
- BM commercial UGC video with zero dialogue
- visual_truth_packet null despite uploaded image

Transitions:
- PASS → `STATE_OUTPUT_READY`
- ABORT → `STATE_ABORTED`

---

### STATE_OUTPUT_READY
**Final Emitter Worker runs here.**
**THIS WORKER FORMATS ONLY. NO SUBSTANCE CHANGES PERMITTED.**

Input: `compliance_report_packet (PASS)` + `prompt_blocks_packet` + `storyboard_packet`
Output: `final_output_packet`

Worker scope:
- format output using CHATGPT_CLEAN_VIDEO_ROLE_MODEL shape:
  1. `VISUAL SCAN SUMMARY`
  2. `ENGINE CONTRACT` (engine, block math, WPS, pace_class)
  3. `STORYBOARD` (approved version)
  4. `BLOCK 1 PROMPT`
  5. `BLOCK 2+ PROMPTS` (if multi-block)
- strip ALL internal scaffolding, metadata, debug labels
- ensure output is immediately copy-paste usable by operator

Kernel action: receives `final_output_packet`, sets `released_to_user = true`, delivers to user.

→ Session transitions to: `SESSION_COMPLETE`

---

### STATE_ABORTED
**Terminal failure state.**

Kernel surfaces `abort_reason` to user.
Session ends.
No partial output delivered.

---

## 5. PIPELINE SUMMARY

**VIDEO pipeline:**
```
STATE_INTAKE
  → STATE_ASSET_ANALYSIS
  → STATE_ROUTE_RESOLVED
  → STATE_ENGINE_PLANNED
  → STATE_STORYBOARD_BUILT [USER APPROVAL GATE]
  → STATE_PROMPTS_COMPILED
  → STATE_COMPLIANCE_CHECKED
  → STATE_OUTPUT_READY
  → [Kernel releases] → USER
```

**IMAGE pipeline:**
```
STATE_INTAKE
  → STATE_ASSET_ANALYSIS
  → STATE_ROUTE_RESOLVED
  → STATE_COMPOSITION_DIRECTED
  → STATE_PROMPTS_COMPILED
  → STATE_COMPLIANCE_CHECKED
  → STATE_OUTPUT_READY
  → [Kernel releases] → USER
```

**REPAIR pipeline:**
```
STATE_INTAKE
  → [Kernel identifies which packet failed]
  → [Route to responsible worker]
  → STATE_COMPLIANCE_CHECKED
  → STATE_OUTPUT_READY
  → [Kernel releases] → USER
```

---

## 6. WORKER ISOLATION CONTRACT

Every worker must obey:

1. Reads ONLY its declared input packets.
2. Writes ONLY its declared output packet.
3. Does NOT read packets outside its input spec.
4. Does NOT modify any upstream packet.
5. Does NOT communicate with user — Kernel communicates on worker's behalf.
6. Does NOT route itself — Kernel routes.
7. Does NOT emit final answer — Final Emitter emits, Kernel releases.

---

## 7. ABSOLUTE FAIL-CLOSED GATES

These conditions always trigger `STATE_ABORTED`. No exceptions. No auto-heal.

```
☐ Video prompt emitted without storyboard existing
☐ Video prompt emitted without storyboard user approval
☐ Engine not in ENGINE_CONSTRAINT_TABLE
☐ Monolithic prompt produced for multi-block requirement
☐ BM commercial UGC video with zero dialogue
☐ overlay_flag ≠ NO_OVERLAY without explicit operator request
☐ visual_truth_packet null despite uploaded image
☐ Any worker emits final output directly to user
☐ Any worker modifies upstream packet
☐ Kernel bypassed by any worker
```

---

## 8. RELATIONSHIP TO EXISTING BOSMAX FILES

This state machine is the **runtime authority**.

All existing BOSMAX authority files (CLAUDE.md, skill files, law files) are **reference material** that workers consult. They do not replace the state machine. They do not override packet schemas.

Priority order when conflict exists:
1. This state machine (highest)
2. `BOSMAX_AGENT_HANDOFF_SCHEMA_v1.md`
3. `BOSMAX_SOP_GOVERNOR_v1.md`
4. `CLAUDE.md`
5. Individual skill files (lowest)
