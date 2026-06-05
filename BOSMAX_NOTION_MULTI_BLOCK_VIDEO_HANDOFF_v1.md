# BOSMAX NOTION MULTI-BLOCK VIDEO HANDOFF v1

Authority:
- `BOSMAX_EXECUTION_KERNEL_CONTRACT_v1.md`
- `.claude/CLAUDE.md`
- `registries/video_engine_duration_contracts.yaml`
- `registries/dialogue_budget_corridor.yaml`
- `docs/google_flow_parity_audit_v1.md`

Notion remains downstream UI only.

Repo remains source of truth for:
- block math
- WPS per block
- copywriting resolver payload
- avatar resolver payload
- readiness status
- validator proof posture

Purpose:
- give Notion a reusable parent-child execution surface for BOSMAX long-duration video
- stop invalid monolithic multi-block prompts
- keep GROK, VEO, and GOOGLE_FLOW structurally comparable without collapsing engine-specific block math

---

## 1. Source Of Truth

Use:
- `registries/video_engine_duration_contracts.yaml` for engine duration law
- `scripts/video_block_plan.py` for deterministic block planning
- `scripts/validate_video_block_contracts.py` for fail-closed validation
- `scripts/validate_wps_per_block.py` for per-block WPS validation
- `scripts/validate_notion_sample_readiness.py` for Notion sample posture
- `scripts/validate_flow_extend_proof.py` for Flow child-block seam proof

Do not let Notion invent:
- block durations
- WPS budgets
- copywriting rows
- avatar context rows
- seam law

---

## 2. Required Notion Databases

### Parent database

`🎬 BOSMAX Video Runs`

### Child database

`🎞️ BOSMAX Video Run Blocks`

Required child properties:
- `Parent Video Run`
- `Engine`
- `Execution Mode`
- `Block Index`
- `Block Duration Seconds`
- `Block Role`
- `Copywriting ID`
- `Avatar Context ID or Avatar Pool ID`
- `Dialogue Budget`
- `Final Block Dialogue`
- `Block Dialogue Word Count`
- `Previous Clip Final Second State`
- `Continuity Goal`
- `Identity Reanchor`
- `Product Reanchor`
- `Scene Continuity Notes`
- `Audio Continuity Notes`
- `Frame Bridge Notes`
- `Bridge-Out`
- `Bridge-In`
- `Block Prompt Manual Output`
- `Block Status`
- `Validator Proof`

If rollups or formulas are connector-blocked, keep manual text/number mirrors on the page body.

---

## 3. Parent Database Patches

Add these properties to `🎬 BOSMAX Video Runs`:
- `Block Plan Summary`
- `Block Count`
- `Prompt Count`
- `Requires Multi-Block`
- `Block Plan Status`
- `Multi-Block Execution Mode`
- `Video Run Blocks`
- `Parent Multi-Block Manual Output`
- `Validator Proof Summary`

---

## 4. GROK Hard Execution Law

Allowed single blocks:
- `6s`
- `10s`

Required multi-block totals:
- `12s = 6 + 6`
- `16s = 10 + 6`
- `20s = 10 + 10`
- `30s = 10 + 10 + 10`

For all GROK extension runs:
- non-final blocks must end with explicit bridge-out
- non-first blocks must open with bridge-in
- speech must resume inside `0.5s-1.0s`
- operator wording must reference `previous clip`, not internal block labels

---

## 5. VEO / Flow Rule

### `VEO_3_1.CLIP_CHAIN`

Allowed totals:
- `16s = 8 + 8`
- `24s = 8 + 8 + 8`
- `32s = 8 + 8 + 8 + 8`
- `40s = 8 + 8 + 8 + 8 + 8`
- `48s = 8 + 8 + 8 + 8 + 8 + 8`
- `56s = 8 + 8 + 8 + 8 + 8 + 8 + 8`

For every clip after the first:
- frame bridge required
- identity re-anchor required
- product re-anchor required

### `VEO_3_1_LITE.CLIP_CHAIN`

Block split matches raw `8s` API windows.

WPS rule:
- dialogue budget uses `7s` actual-render corridor per block

### `GOOGLE FLOW MULTI-BLOCK — Flow Extend`

Google Flow long duration must create child block rows just like GROK.

It must not be:
- one monolithic prompt
- GROK duration math
- free-typed Notion logic

#### Flow UI surface

Execution mode:
- `FLOW_EXTEND_UI`

Reviewed totals:
- `8s = 8`
- `16s = 8 + 8`
- `24s = 8 + 8 + 8`
- `32s = 8 + 8 + 8 + 8`
- `40s = 8 + 8 + 8 + 8 + 8`
- `48s = 8 + 8 + 8 + 8 + 8 + 8`
- `56s = 8 + 8 + 8 + 8 + 8 + 8 + 8`

Per-block rules:
- WPS corridor uses `8s` per block
- non-first blocks require `Previous Clip Final Second State`
- every block requires `Identity Reanchor`
- every block requires `Product Reanchor`
- non-first blocks require `Bridge-In`
- non-final blocks require `Bridge-Out`
- child rows are mandatory
- status may use `READY_REVIEWED_FLOW_EXTEND` only when validator proof exists

#### Optional Vertex surface

Execution mode:
- `FLOW_EXTEND_VERTEX`

Documented totals:
- `7s = 7`
- `14s = 7 + 7`
- `21s = 7 + 7 + 7`
- `28s = 7 + 7 + 7 + 7`
- `35s = 7 + 7 + 7 + 7 + 7`
- `42s = 7 + 7 + 7 + 7 + 7 + 7`
- `49s = 7 + 7 + 7 + 7 + 7 + 7 + 7`
- `56s = 7 + 7 + 7 + 7 + 7 + 7 + 7 + 7`

Status:
- `NEEDS_REVIEW`

Operator rule:
- document the 7s surface
- do not promote it into reviewed Flow UI readiness until dedicated proof exists

---

## 6. Sample Runs Required

Required parent runs:
- `SAMPLE-HYBRID-GROK-16S-RIZAL`
- `SAMPLE-VEO31-16S-CLIP-CHAIN-RIZAL`
- `SAMPLE-VEO31-24S-CLIP-CHAIN-RIZAL`
- `SAMPLE-FLOW-16S-RIZAL`
- `SAMPLE-FLOW-24S-RIZAL`
- `SAMPLE-FLOW-32S-RIZAL`
- `SAMPLE-FLOW-MWCB-16S-DIRECT`

Required Flow proof:
- parent run exists
- child block rows exist
- block plan matches engine contract
- per-block WPS exists
- copywriting ID resolved
- avatar context ID or pool resolved
- previous-final-second state filled on continuation blocks
- identity reanchor filled
- product reanchor filled
- validator proof captured

---

## 7. Manual Proof Surface

Keep these proof blocks visible on parent pages:
- `ENGINE CONTRACT SUMMARY`
- `BLOCK PLAN SUMMARY`
- `OUTPUT TEST REPORT`
- `VALIDATOR PROOF SUMMARY`

Keep these proof fields visible on child pages:
- `Dialogue Budget`
- `Block Dialogue Word Count`
- `Previous Clip Final Second State`
- `Bridge-Out`
- `Bridge-In`
- `Validator Proof`

---

## 8. Compliance Notes

- Copywriting ID and Avatar Context ID resolution remain shared across GROK, VEO, and GOOGLE_FLOW.
- Engine-specific differences are limited to block math, seam law, and WPS budgeting.
- BOSMAX Serum STEALTH and MWCB DIRECT still inherit their existing copy/avatar approval rules.

---

## 9. Operator Sequence

1. Resolve engine and total duration using `scripts/video_block_plan.py`.
2. Confirm authority status.
   - `READY`, `READY_CLIP_MODE`, `READY_REVIEWED_FLOW_EXTEND` -> proceed.
   - `NEEDS_REVIEW`, `MANUAL_REVIEW_ONLY` -> review-only run, not ready run.
3. Create or update parent run.
4. Create child block rows from resolved plan.
5. Paste manual prompt output per block.
6. Run validators.
7. Promote status only after validator proof is captured.

---

## 10. BOSMAX Sample Readiness Validator

Validator:
- `python scripts/validate_notion_sample_readiness.py`

Ready posture:
- `READY` for standard deterministic runs with proof
- `READY_REVIEWED_FLOW_EXTEND` for reviewed Flow UI runs with proof

Blocked posture:
- `FLOW_EXTEND_VERTEX` may not use `READY_REVIEWED_FLOW_EXTEND`
- formula results and omitted rollups are not accepted as proof

---

## 11. BOSMAX Per-Block WPS Validator

Validator:
- `python scripts/validate_wps_per_block.py`

Rules:
- multi-block videos must use per-block dialogue budgets
- GROK 16s = `10s + 6s`
- VEO clip-chain uses `8s` corridor per block
- VEO_3_1_LITE uses `7s` actual-render corridor per block
- GOOGLE_FLOW FLOW_EXTEND_UI uses `8s` corridor per block

---

## 12. BOSMAX Flow Extend Proof Validator

Validator:
- `python scripts/validate_flow_extend_proof.py`

Rules:
- `FLOW_EXTEND_UI` reviewed runs must have child rows
- continuation blocks must include `Previous Clip Final Second State`
- all Flow blocks must include identity and product reanchors
- `FLOW_EXTEND_VERTEX` remains `NEEDS_REVIEW`
