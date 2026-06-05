# BOSMAX NOTION MULTI-BLOCK VIDEO HANDOFF v1

Authority:
- `BOSMAX_EXECUTION_KERNEL_CONTRACT_v1.md` ← top-level gate (all template READY claims must pass)
- `.claude/CLAUDE.md`
- `BOSMAX_HARD_ENGINE_CONTRACTS_v1.md`
- `BOSMAX_GROK_EXTENSION_SEAM_TEMPLATES_v1.md`
- `BOSMAX_RUNTIME_STATE_MACHINE_v1.md`
- `registries/video_engine_duration_contracts.yaml`
- `registries/dialogue_budget_corridor.yaml`

Note: Notion remains downstream UI only. Multi-block runs require child block records in
`🎞️ BOSMAX Video Run Blocks`. VEO/Flow readiness depends on engine contract registry and
validator proof — see BOSMAX_EXECUTION_KERNEL_CONTRACT_v1.md Section 15 for VEO_3_1_LITE
live gap status.

Purpose:
- give Notion a reusable parent-child execution surface for BOSMAX long-duration video
- stop invalid monolithic GROK prompts for 12s, 16s, 20s, and 30s
- separate raw `VEO_3_1` clip-chain planning from `GOOGLE_FLOW` extend workflow
- keep Google Flow manual-review only until direct operational proof is hardened

---

## 1. Source Of Truth

Repo remains the source of truth.

Notion is downstream execution UI only.

Do not let Notion become the place where engine math is invented.

Use:
- `registries/video_engine_duration_contracts.yaml` for engine duration law
- `scripts/video_block_plan.py` for deterministic block planning
- `scripts/validate_video_block_contracts.py` for fail-closed validation

---

## 2. Required Notion Databases

### A. Existing parent database

`🎬 BOSMAX Video Runs`

This remains the parent run surface.

### B. New child database

`🎞️ BOSMAX Video Run Blocks`

This stores one row per executable block.

Required properties:
- `Block Name` — title
- `Parent Video Run` — relation to `🎬 BOSMAX Video Runs`
- `Engine` — relation to `⚙️ Engine Registry` if supported, otherwise text fallback
- `Total Duration`
- `Block Index`
- `Block Duration Seconds`
- `Block Role`
- `Prompt Count`
- `Requires Seam`
- `Seam Template`
- `Bridge-Out`
- `Bridge-In`
- `Previous Clip End State`
- `Opening Continuation Action`
- `Speech Resume Window`
- `Dialogue Role`
- `Dialogue Budget`
- `Final Block Dialogue`
- `Block Dialogue Word Count`
- `Block Prompt Manual Output`
- `Block Status`
- `QA Notes`

If rollups or formulas are connector-blocked, add manual text/number fields and a visible proof block on the page body.

---

## 3. Parent Database Patches

Add these properties to `🎬 BOSMAX Video Runs`:
- `Block Plan Summary`
- `Block Count`
- `Prompt Count`
- `Requires Multi-Block`
- `Block Plan Status`
- `Multi-Block Execution Mode`
- `Video Run Blocks` relation to `🎞️ BOSMAX Video Run Blocks`
- `Parent Multi-Block Manual Output`

Optional rollups if connector supports them safely:
- child prompt count
- child status summary
- child block duration summary

If rollups are omitted by MCP fetch, keep manual summary fields on the parent page.

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

Do not emit monolithic GROK prompts for:
- `12s`
- `16s`
- `20s`
- `30s`

For all GROK extension runs:
- non-final blocks must end with explicit bridge-out
- non-first blocks must open with bridge-in
- speech must resume inside `0.5s-1.0s`
- operator-facing seam wording must reference `previous clip`, not internal labels like `Block 1`

---

## 5. VEO / Flow Rule

### `VEO_3_1`

Repo authority now promotes `VEO_3_1.CLIP_CHAIN` to downstream-ready planning.

Allowed clip-chain totals:
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

### `GOOGLE_FLOW`

Keep Google Flow separate from raw Veo clip-chain math.

Current downstream posture:
- `FLOW_EXTEND` remains `MANUAL_REVIEW_ONLY`
- do not treat `FLOW_EXTEND` as ordinary `8 + 8` clip math
- require previous clip final-second state
- require continuity notes, frame-bridge notes, and re-anchor notes

Suggested review-facing phrasing:
- `Flow Extend is officially real but remains BOSMAX manual-review only. Do not treat it as production-ready deterministic long-form math.`

---

## 6. Sample Runs Required

Create parent runs:
- `SAMPLE-HYBRID-GROK-16S-RIZAL`
- `SAMPLE-HYBRID-GROK-20S-RIZAL`
- `SAMPLE-HYBRID-GROK-30S-RIZAL`
- `SAMPLE-VEO31-16S-CLIP-CHAIN-RIZAL`
- `SAMPLE-VEO31-24S-CLIP-CHAIN-RIZAL`
- `SAMPLE-FLOW-VEO31-LONGFORM-NEEDS-REVIEW` because Flow extend remains manual-review only

For `SAMPLE-HYBRID-GROK-16S-RIZAL`, create two child rows:
- Block 1: `10s`
- Block 2: `6s`

Required block semantics:
- Block 1: Hook + Pain + Friction + bridge-out
- Block 2: bridge-in + Relief + CTA

---

## 7. Manual Proof Surface

Because MCP can omit rollups and the legacy `AI-Ready Request Block` formula is not the reliable execution surface, keep:
- `AI-Ready Request Manual Output`
- `Parent Multi-Block Manual Output`
- page-body proof sections such as:
  - `ENGINE CONTRACT SUMMARY`
  - `BLOCK PLAN SUMMARY`
  - `OUTPUT TEST REPORT v2 — Multi-Block`

For block pages, keep:
- explicit dialogue budget note
- seam QA
- speech resume note
- bridge-out / bridge-in text

---

## 8. Compliance Notes

For BOSMAX Serum and other STEALTH lanes:
- source-backed STEALTH copy must still pass export sanitizer before final TikTok / GROK execution
- avoid unsanitized endurance or explicit-adjacent phrasing in final spoken dialogue
- keep product truth anchored to approved copy pack and product registry only

---

## 9. Operator Sequence

1. Resolve engine and total duration using `scripts/video_block_plan.py`
2. Confirm authority status:
   - `READY` / `READY_CLIP_MODE` -> proceed
   - `MANUAL_REVIEW_ONLY` / `NEEDS_REVIEW` -> create review-only run, not ready run
3. Create/update parent run
4. Create child block rows from resolved plan
5. Paste manual prompt output per block
6. Run `python scripts/validate_video_block_contracts.py`
7. Mark run:
   - `Ready` only when validator truth and block proof both exist
   - `Needs Compliance Review` for manual overrides or Flow/VEO review-only runs

---

## 12. BOSMAX Flow Extend Proof Validator

Repo authority now includes `scripts/validate_flow_extend_proof.py` and `registries/flow_extend_proof.yaml`.

Rules:
- GOOGLE_FLOW.FLOW_EXTEND is a previous-final-second continuation workflow. It is not ordinary VEO_3_1 8+8 clip-chain math.
- READY requires: previous clip final-second state, continuation goal, identity re-anchor, product re-anchor, audio continuity notes, frame bridge notes, output test report, and validator proof.
- `formulaResult://...` and `<omitted />` rollups are not accepted as proof.
- FLOW_EXTEND remains MANUAL_REVIEW_ONLY until all proof fields are complete.

Validator: `python scripts\validate_flow_extend_proof.py`

---

## 11. BOSMAX Per-Block WPS Validator

Repo authority now includes `scripts/validate_wps_per_block.py`.

Rules:
- Multi-block videos must use per-block dialogue budgets. Total duration WPS alone is not accepted.
- GROK 16s = 10s + 6s, with separate 10s and 6s dialogue corridors.
- VEO_3_1 clip-chain uses 8s block corridors.
- VEO_3_1_LITE uses 8s API blocks but 7s actual-render dialogue budgets.
- GOOGLE_FLOW.FLOW_EXTEND remains MANUAL_REVIEW_ONLY and is not deterministic WPS block math.

READY claims require validator proof: `python scripts\validate_wps_per_block.py`

---

## 10. BOSMAX Sample Readiness Validator

Repo authority now includes `scripts/validate_notion_sample_readiness.py` and
`registries/notion_sample_readiness.yaml`.

READY sample claims must be backed by:
- engine contract proof (block plan matches `scripts/video_block_plan.py`)
- block plan summary present
- product truth check passed
- avatar source check passed
- WPS audit passed per block
- output test report present
- child block records for all multi-block runs

`formulaResult://...` and `<omitted />` rollups are not accepted as proof.
`GOOGLE_FLOW.FLOW_EXTEND` remains `MANUAL_REVIEW_ONLY`.

To promote a sample run to READY:
1. Fill all proof fields in `registries/notion_sample_readiness.yaml`
2. Run `python scripts/validate_notion_sample_readiness.py`
3. Paste `VALIDATION PASSED` output into `validator_capture` field
4. Update `execution_status: READY`
5. Re-run validator to confirm
