# BOSMAX VEO 3.1 / Flow Contract Decision v1

Date: 2026-06-05
Status: ACTIVE REPO DECISION RECORD

Authority stack:
- `.claude/CLAUDE.md`
- `BOSMAX_EXECUTION_KERNEL_CONTRACT_v1.md`
- `registries/video_engine_duration_contracts.yaml`
- `docs/google_flow_parity_audit_v1.md`

Official sources checked on 2026-06-05:
- Google Flow Help: `https://support.google.com/flow/answer/16352836`
- Vertex AI Veo Extend docs: `https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/extend-a-veo-video`
- Google blog: `https://blog.google/innovation-and-ai/products/veo-updates-flow/`
- Google AI for Developers video docs: `https://ai.google.dev/gemini-api/docs/video`

---

## 1. Verified Facts

### A. Raw Veo clip generation

- Veo raw generation exposes short clip primitives in the `4s`, `6s`, `8s` family.
- BOSMAX longform planning remains a repo-layer contract built on top of those primitives.

### B. Flow Extend basis

- Google states that Extend continues from the final second of the previous clip.
- Vertex docs state the extend output length is `7 seconds` and the input video can be `1-30 seconds`.
- Flow Help documents an `8s` Extend-supported Flow UI surface on the current reviewed matrix.

### C. Operational consequence

Google Flow is not mysterious at the operator-structure level.

Like GROK and VEO clip-chain, reviewed Flow long duration still needs:
- parent run
- child block rows
- block duration
- per-block WPS
- bridge-in and bridge-out
- continuity control
- identity reanchor
- product reanchor
- shared copywriting/avatar resolver payload
- validator proof

---

## 2. BOSMAX Operating Decision

### A. `VEO_3_1.CLIP_CHAIN`

Status:
- `READY`

Approved BOSMAX clip-chain math:
- `8s -> [8]`
- `16s -> [8, 8]`
- `24s -> [8, 8, 8]`
- `32s -> [8, 8, 8, 8]`
- `40s -> [8, 8, 8, 8, 8]`
- `48s -> [8, 8, 8, 8, 8, 8]`
- `56s -> [8, 8, 8, 8, 8, 8, 8]`

### B. `VEO_3_1_LITE.CLIP_CHAIN`

Status:
- `READY`

Rule:
- API block size stays `8s`
- dialogue budget uses `7s` actual-render corridor per block

### C. `GOOGLE_FLOW.FLOW_EXTEND_UI`

Status:
- `READY_REVIEWED_FLOW_EXTEND`

Reason:
- official Flow UI evidence exists for the current reviewed 8s surface
- repo now ships deterministic block math, per-block WPS, child-block schema, sample proof, and validator coverage

Approved BOSMAX Flow UI block math:
- `8s -> [8]`
- `16s -> [8, 8]`
- `24s -> [8, 8, 8]`
- `32s -> [8, 8, 8, 8]`
- `40s -> [8, 8, 8, 8, 8]`
- `48s -> [8, 8, 8, 8, 8, 8]`
- `56s -> [8, 8, 8, 8, 8, 8, 8]`

This is not generic GROK math.

It is a Flow-specific continuation contract that still requires:
- previous clip final-second state on continuation blocks
- bridge-in on non-first blocks
- bridge-out on non-final blocks
- identity reanchor every block
- product reanchor every block
- shared copywriting/avatar resolver payload

### D. `GOOGLE_FLOW.FLOW_EXTEND_VERTEX`

Status:
- `NEEDS_REVIEW`

Reason:
- Vertex docs verify the `7s` extend output surface
- repo documents the deterministic `7s` ladder
- repo does not yet ship a dedicated reviewed Vertex proof lane

Documented BOSMAX Vertex block math:
- `7s -> [7]`
- `14s -> [7, 7]`
- `21s -> [7, 7, 7]`
- `28s -> [7, 7, 7, 7]`
- `35s -> [7, 7, 7, 7, 7]`
- `42s -> [7, 7, 7, 7, 7, 7]`
- `49s -> [7, 7, 7, 7, 7, 7, 7]`
- `56s -> [7, 7, 7, 7, 7, 7, 7, 7]`

---

## 3. Continuity Rules

For every `VEO_3_1` or `VEO_3_1_LITE` clip after the first:
- frame bridge required
- identity reanchor required
- product reanchor required

For every `FLOW_EXTEND_UI` continuation block:
- previous clip final-second state required
- continuity goal required
- identity reanchor required
- product reanchor required
- scene continuity notes required
- audio continuity notes required
- frame bridge notes required

Shared copywriting/avatar resolver payload:
- unchanged across GROK, VEO, and GOOGLE_FLOW

---

## 4. Notion Posture

- `VEO_3_1.CLIP_CHAIN` -> `READY_CLIP_MODE`
- `VEO_3_1_LITE.CLIP_CHAIN` -> `READY_CLIP_MODE`
- `GOOGLE_FLOW.FLOW_EXTEND_UI` -> `READY_REVIEWED_FLOW_EXTEND`
- `GOOGLE_FLOW.FLOW_EXTEND_VERTEX` -> `NEEDS_REVIEW`

---

## 5. Fail-Closed Rules

- Do not mark `FLOW_EXTEND_VERTEX` as reviewed-ready without a dedicated proof lane.
- Do not allow Google Flow long duration to collapse into a monolithic prompt.
- Do not apply GROK split math to Google Flow.
- Do not allow Flow child rows to omit previous-final-second state on continuation blocks.
- Do not allow Flow reviewed posture without validator proof.

---

## 6. Repo Action Result

This decision record authorizes:
- `VEO_3_1` clip-chain planning in repo + Notion
- `VEO_3_1_LITE` 7s actual-render WPS budgeting
- `GOOGLE_FLOW.FLOW_EXTEND_UI` reviewed-ready block planning with child-block proof
- continued review-only posture for `GOOGLE_FLOW.FLOW_EXTEND_VERTEX`
