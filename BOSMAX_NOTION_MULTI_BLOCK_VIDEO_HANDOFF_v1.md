# BOSMAX NOTION MULTI-BLOCK VIDEO HANDOFF v1

Authority:
- `.claude/CLAUDE.md`
- `BOSMAX_HARD_ENGINE_CONTRACTS_v1.md`
- `BOSMAX_GROK_EXTENSION_SEAM_TEMPLATES_v1.md`
- `BOSMAX_RUNTIME_STATE_MACHINE_v1.md`
- `registries/video_engine_duration_contracts.yaml`
- `registries/dialogue_budget_corridor.yaml`

Purpose:
- give Notion a reusable parent-child execution surface for BOSMAX long-duration video
- stop invalid monolithic GROK prompts for 12s, 16s, 20s, and 30s
- keep Google Flow / VEO 3.1 visible as review-only until repo authority is hardened

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

## 5. Google Flow / VEO 3.1 Rule

Current repo authority is not yet hardened enough for deterministic downstream Notion execution.

Therefore:
- create sample parent run only as `NEEDS_REVIEW`
- do not mark Flow/VEO long-form as ready
- do not pretend the block contract is verified

Suggested review-facing phrasing:
- `Flow/VEO long-form plan is proposed only. Repo authority still requires architect review before production execution.`

---

## 6. Sample Runs Required

Create parent runs:
- `SAMPLE-HYBRID-GROK-16S-RIZAL`
- `SAMPLE-HYBRID-GROK-20S-RIZAL`
- `SAMPLE-HYBRID-GROK-30S-RIZAL`
- `SAMPLE-FLOW-VEO31-LONGFORM-NEEDS-REVIEW` only because Flow/VEO authority is incomplete

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
   - `VERIFIED` -> proceed
   - `NEEDS_REVIEW` -> create review-only run, not ready run
3. Create/update parent run
4. Create child block rows from resolved plan
5. Paste manual prompt output per block
6. Run `python scripts/validate_video_block_contracts.py`
7. Mark run:
   - `Ready` only when validator truth and block proof both exist
   - `Needs Compliance Review` for manual overrides or Flow/VEO review-only runs
