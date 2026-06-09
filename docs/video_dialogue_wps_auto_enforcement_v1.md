# BOSMAX Video Dialogue WPS Auto-Enforcement
# Version: v1
# Authority: BOSMAX Systems Architecture
# Status: ACTIVE — dialogue runtime contract
# Last updated: 2026-06-10

---

## Core Law

WPS is universal for **all video engines** whenever `dialogue_required = YES`.
This enforcement applies to:

- GROK
- GOOGLE_FLOW / FLOW_EXTEND_UI
- VEO clip-chain (`VEO_3_1`, `VEO_3_1_LITE`)
- KLING
- SEEDANCE
- any future BOSMAX video engine that emits spoken dialogue

Per-block budgets are authoritative for multi-block outputs.
Total-duration budget cannot replace per-block budget.

---

## Runtime Sequence

For every dialogue video route, BOSMAX must:

1. Resolve engine and total duration.
2. Resolve block plan from `registries/video_engine_duration_contracts.yaml`.
3. Resolve per-block dialogue budget from `registries/dialogue_budget_corridor.yaml`.
4. Build storyboard beats by block duration.
5. Write exact dialogue line per block before final prompt assembly.
6. Count dialogue words per block.
7. Rewrite any block marked `UNDERFILLED`.
8. Rewrite any block above the `hard ceiling`.
9. Keep rewriting internally until every block passes its corridor.
10. Emit final clean operator-facing prompt only after the per-block WPS audit passes.

Multi-block dialogue must be split by block duration.
The final prompt output is blocked if any dialogue block is under minimum words.
The final prompt output is blocked if any dialogue block exceeds hard ceiling.

---

## Corridor Status Logic

Per-block word count must resolve to one of these states:

- `UNDERFILLED` when final word count is below `minimum_words`
- `TARGET_RANGE` when final word count lands within the target band
- `OVER SAFE` when final word count exceeds `target_max_words` but stays within the soft recovery band
- `HARD FAIL` when final word count exceeds `hard ceiling_words`

`UNDERFILLED` and `HARD FAIL` are blocking states for final prompt emission.

---

## Clean Output Law

Normal operator prompt must stay clean.
The final clean operator-facing prompt must not expose:

- WPS table
- word budget
- validator metadata
- internal audit object
- hidden source-mode labels
- internal seam fields

The output should surface only the approved spoken line naturally, for example:

`Natural Malaysian Malay male voice says exactly: "[dialogue line]"`

---

## Presentation Route Enforcement

For TikTok Shop Malaysia UGC videos where:

- `dialogue_required = YES`
- total duration is greater than 10 seconds

Default route must be `AVATAR_PRODUCT_UGC`.

Hand-only or product-only route is allowed only if at least one of the following is true:

- the user explicitly asks for product-only or no-avatar
- the template is a 6s CTA close
- `dialogue_required = NO`
- the source frame already has no avatar and the route is image-to-video continuation

This route law is universal across BOSMAX video products and engines.
