# BOSMAX VEO 3.1 / Flow Contract Decision v1

Date: 2026-06-04
Status: ACTIVE REPO DECISION RECORD

Authority stack:
- `.claude/CLAUDE.md`
- `BOSMAX_HARD_ENGINE_CONTRACTS_v1.md`
- `BOSMAX_RUNTIME_STATE_MACHINE_v1.md`
- `registries/video_engine_duration_contracts.yaml`

Official sources checked on 2026-06-04:
- Google AI for Developers: `https://ai.google.dev/gemini-api/docs/video`
- Vertex AI Veo 3.1 generate docs: `https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-1-generate`
- Vertex AI Veo extend docs: `https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/extend-a-veo-video`
- Google blog: `https://blog.google/innovation-and-ai/products/veo-updates-flow/`
- Google Flow Help: `https://support.google.com/flow/answer/16352836`

---

## 1. Verified Facts

### A. Raw Veo clip generation

Verified from Google AI / Gemini API docs:
- Veo video generation exposes `durationSeconds` values `4`, `6`, and `8`.
- When using extension, reference images, or certain higher-resolution cases, the duration must be `8`.

Verified from Google Flow Help:
- Veo 3.1 model rows expose short-form clip lengths in the `4s`, `6s`, `8s` family.
- Some Flow model tiers also expose `10s` at the UI layer, but that is not enough to promote a deterministic BOSMAX raw-engine contract for longform math.

### B. Veo extension basis

Verified from Vertex AI extend docs and Google blog:
- Veo extension is a continuation workflow, not the same thing as ordinary fresh clip generation.
- Extension uses the final second / final frames of the previous clip as the continuity basis.
- The extend flow is intended for seamless continuation rather than independent block restarts.

### C. Flow feature surface

Verified from Google blog:
- `Frames to Video` bridges a start image and end image into one seamless clip.
- `Extend` creates longer seamless shots by continuing from the action in the prior clip.

---

## 2. Not Verified Or Not Safe To Promote

These items are not promoted to production-ready BOSMAX truth:

- A universal Google Flow deterministic `16s`, `24s`, `32s`, `40s`, `48s`, `56s` contract.
- A claim that Flow `Extend` should be treated as ordinary `8s + 8s` clip math.
- A claim that all Flow subfeatures are uniformly ready across every Veo 3.1 model tier.
- A claim that Flow longform should be marked repo-ready without manual continuity review.

Reason:
- Google Flow Help still shows feature-matrix nuance and "coming soon" surfaces around certain Frames / Extend combinations.
- Vertex docs verify the primitive capabilities, but they do not give BOSMAX a deterministic operator-safe production contract for all Flow UI longform cases.

---

## 3. BOSMAX Operating Decision

### A. `VEO_3_1` raw clip-chain decision

BOSMAX promotes `VEO_3_1` raw clip-chain planning to `PARTIAL_VERIFIED`:
- verified primitive: raw Veo clip generation supports short clip durations
- BOSMAX operating rule: longform planning is built as chained `8s` clip windows

Approved BOSMAX clip-chain math:
- `8s`   -> `[8]`
- `16s`  -> `[8, 8]`
- `24s`  -> `[8, 8, 8]`
- `32s`  -> `[8, 8, 8, 8]`
- `40s`  -> `[8, 8, 8, 8, 8]`
- `48s`  -> `[8, 8, 8, 8, 8, 8]`
- `56s`  -> `[8, 8, 8, 8, 8, 8, 8]`

This is a BOSMAX planning contract layered on top of verified short-clip primitives.
It is not a claim that Google documents these long totals as one native monolithic clip.

### B. `GOOGLE_FLOW` workflow decision

BOSMAX keeps Google Flow as a separate workflow layer:
- `GOOGLE_FLOW` is not duplicated as fake raw-engine math.
- `FLOW_EXTEND` remains `NEEDS_REVIEW` for production execution.
- `FLOW_EXTEND` may exist as a manual-review template because the official docs prove the workflow exists.
- `FLOW_EXTEND` must require previous-clip final-second state and continuity notes.

### C. Continuity rules promoted by BOSMAX

For every `VEO_3_1` clip-chain block after the first:
- frame bridge required
- identity re-anchor required
- product re-anchor required
- previous clip continuity note required

For every `FLOW_EXTEND` review-only plan:
- previous clip final-second state required
- continuation goal required
- identity re-anchor required
- product re-anchor required
- audio continuity notes required
- frame bridge notes required

---

## 4. Engine Modes

### `VEO_3_1.CLIP_CHAIN`
- Status: `READY`
- Meaning: BOSMAX-approved raw Veo clip-chain planning in `8s` windows
- Notion posture: `READY_CLIP_MODE`

### `GOOGLE_FLOW.FLOW_EXTEND`
- Status: `NEEDS_REVIEW`
- Meaning: official extend primitive exists, but downstream deterministic BOSMAX production contract is not promoted
- Notion posture: `MANUAL_REVIEW_ONLY`

---

## 5. Fail-Closed Rules

- Do not mark `GOOGLE_FLOW` longform as production-ready from blog language alone.
- Do not convert Flow `Extend` into fake `8 + 8` math.
- Do not mark any Flow mode `READY` unless the validator can trace a verified decision surface.
- Do not allow `VEO_3_1` totals outside `[4, 6, 8, 16, 24, 32, 40, 48, 56]`.
- Do not allow `VEO_3_1` clip-chain totals above `8s` without continuity bridge and re-anchor requirements.

---

## 6. Remaining Risks

- Google may change Flow model-feature availability independently of raw Veo API surfaces.
- Flow UI length labels can diverge from raw Veo generation primitives.
- Extend output duration behavior is workflow-specific and not safe to collapse into generic longform math without further direct operational proof.

---

## 7. Repo Action Result

This decision record authorizes:
- `VEO_3_1` clip-chain planning in repo + Notion
- validator enforcement for `16 = 8 + 8`, `24 = 8 + 8 + 8`, and higher approved ladders
- continued review-only posture for `GOOGLE_FLOW.FLOW_EXTEND`
