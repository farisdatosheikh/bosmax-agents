# BOSMAX Batch Template Set v1
# Date: 2026-06-02
# Status: Production-ready operator templates

## Purpose

This file is the first production-ready BOSMAX batch prompt template set.

Use these templates only after:
- product truth is known
- scale anchors are available
- deterministic single-output flow is already stable

These templates are not freeform prompts.
They are structured batch intake blocks for BOSMAX.

---

## Operator Rule

Always run batch in chunks:
- `10`
- `25`
- `50`

If target is `200/day`, use chunked runs such as:
- `4×50`
- `5×40`

Do not request one raw 200-output blast in a single pass.

---

## Template 1 — `BATCH_IMAGE_SUPPORT`

Use when you want many clean still images for later video continuation.

```text
Mode: BULK
Batch type: BATCH_IMAGE_SUPPORT
Batch goal: IMAGE_ONLY
Product scope: SINGLE_PRODUCT
Content quantity: [10 / 25 / 50]
Platform: [TikTok / Shopee / Lazada / Meta]
Language: [Malay / English]

Produk: [PRODUCT NAME]
Variant: [VARIANT]
Scale anchor: [EXACT SCALE ANCHOR]
Batch variation mode: [COPY_VARIANT_BATCH / ANGLE_ROTATION_BATCH / VISUAL_VARIANT_BATCH / MATRIX_BATCH]
Angle lock: [ANGLE ID or NONE]
Semantic intent: [same commercial meaning to preserve]
Copy variant count: [N]
Visual variation level: [LOW / MEDIUM / HIGH]
Semantic drift guard: ON

Image mix:
- VIDEO_SUPPORT: 100%
- SELLING_POSTER: 0%

Variation condition: [1 / 2 / 3]

Avatar pool:
- [AVATAR 1]
- [AVATAR 2]
- [AVATAR 3]

Scene pool:
- [SCENE 1]
- [SCENE 2]
- [SCENE 3]

Camera/style pool:
- clean product hero
- in-hand lifestyle
- light scene variation

Batch requirement:
Build Variant Plan first, then generate only after approval.
Every row must resolve to IMAGE + VIDEO_SUPPORT.
Output required:
- batch_plan
- batch_prompt_pack
- batch_summary
```

---

## Template 2 — `BATCH_IMAGE_SELLING`

Use when you want many conversion-oriented posters.

```text
Mode: BULK
Batch type: BATCH_IMAGE_SELLING
Batch goal: IMAGE_ONLY
Product scope: SINGLE_PRODUCT
Content quantity: [10 / 25 / 50]
Platform: [TikTok / Shopee / Lazada / Meta]
Language: [Malay / English]

Produk: [PRODUCT NAME]
Variant: [VARIANT]
Scale anchor: [EXACT SCALE ANCHOR]
Batch variation mode: [COPY_VARIANT_BATCH / ANGLE_ROTATION_BATCH / VISUAL_VARIANT_BATCH / MATRIX_BATCH]
Angle lock: [ANGLE ID or NONE]
Semantic intent: [same commercial meaning to preserve]
Copy variant count: [N]
Visual variation level: [LOW / MEDIUM / HIGH]
Semantic drift guard: ON

Image mix:
- VIDEO_SUPPORT: 0%
- SELLING_POSTER: 100%

Variation condition: [1 / 2 / 3]

Avatar pool:
- [AVATAR 1]
- [AVATAR 2]

Scene pool:
- [SCENE 1]
- [SCENE 2]

Copy angle pool:
- benefit-first
- trust-first
- pain-point
- heritage / authority

CTA style pool:
- soft CTA
- direct CTA

Batch requirement:
Build Variant Plan first, then generate only after approval.
Every row must resolve to IMAGE + SELLING_POSTER.
Preserve product truth and exact scale anchor in every row.
Output required:
- batch_plan
- batch_prompt_pack
- batch_summary
```

---

## Template 3 — `BATCH_VIDEO_FRESH`

Use when you want many fresh video prompts from known product authority.

```text
Mode: BULK
Batch type: BATCH_VIDEO_FRESH
Batch goal: VIDEO_ONLY
Product scope: SINGLE_PRODUCT
Content quantity: [10 / 25 / 50]
Platform: [TikTok]
Language: [Malay / English]

Produk: [PRODUCT NAME]
Variant: [VARIANT]
Scale anchor: [EXACT SCALE ANCHOR]
Batch variation mode: [COPY_VARIANT_BATCH / ANGLE_ROTATION_BATCH / VISUAL_VARIANT_BATCH / MATRIX_BATCH]
Angle lock: [ANGLE ID or NONE]
Semantic intent: [same commercial meaning to preserve]
Copy variant count: [N]
Visual variation level: [LOW / MEDIUM / HIGH]
Semantic drift guard: ON

Video engine: [VEO_3_1_LITE / VEO_3_1 / KLING_3_0 / SEEDANCE_2_0 / GROK / GOOGLE_FLOW]
Duration target: [VALID DURATION]

Video mix:
- NONE: 100%
- IMAGE_REFERENCE: 0%
- VIDEO_REFERENCE: 0%
- BOSMAX_IMAGE_HANDOFF: 0%

Variation condition: [1 / 2 / 3]
Formula pool:
- [PAS / HSO / AIDA / FAB / SAVAGE_HPAS]

Avatar pool:
- [AVATAR 1]
- [AVATAR 2]

Scene pool:
- [SCENE 1]
- [SCENE 2]

Copy angle pool:
- testimonial
- problem-agitation
- social proof
- transformation

Batch requirement:
Build Variant Plan first, then generate only after approval.
Every row must resolve to VIDEO + NONE.
For sensitive products, resolve dialogue authority from SCRIPT_REGISTRY + SCRIPT_VARIANT_LIBRARY before script generation.
Output required:
- batch_plan
- batch_prompt_pack
- batch_summary
```

---

## Template 4 — `BATCH_MIXED_DETERMINISTIC`

Use when you need a controlled mix of image and video outputs.

```text
Mode: BULK
Batch type: BATCH_MIXED_DETERMINISTIC
Batch goal: MIXED
Product scope: SINGLE_PRODUCT
Total output count: [10 / 25 / 50]
Image count: [X]
Video count: [Y]
Platform: [TikTok / Shopee / Lazada / Meta]
Language: [Malay / English]

Produk: [PRODUCT NAME]
Variant: [VARIANT]
Scale anchor: [EXACT SCALE ANCHOR]
Batch variation mode: [COPY_VARIANT_BATCH / ANGLE_ROTATION_BATCH / VISUAL_VARIANT_BATCH / MATRIX_BATCH]
Angle lock: [ANGLE ID or NONE]
Semantic intent: [same commercial meaning to preserve]
Copy variant count: [N]
Visual variation level: [LOW / MEDIUM / HIGH]
Semantic drift guard: ON

Image mix:
- VIDEO_SUPPORT: [PERCENT]
- SELLING_POSTER: [PERCENT]

Video mix:
- NONE: [PERCENT]
- IMAGE_REFERENCE: [PERCENT]
- VIDEO_REFERENCE: [PERCENT]
- BOSMAX_IMAGE_HANDOFF: [PERCENT]

Video engine: [ENGINE]
Duration target: [VALID DURATION]
Variation condition: [1 / 2 / 3]

Avatar pool:
- [AVATAR 1]
- [AVATAR 2]
- [AVATAR 3]

Scene pool:
- [SCENE 1]
- [SCENE 2]
- [SCENE 3]

Copy angle pool:
- [ANGLE 1]
- [ANGLE 2]
- [ANGLE 3]

CTA style pool:
- [STYLE 1]
- [STYLE 2]

Batch requirement:
Build Variant Plan first, then generate only after approval.
Each approved row must resolve to one of these paths only:
- IMAGE + VIDEO_SUPPORT
- IMAGE + SELLING_POSTER
- VIDEO + NONE
- VIDEO + IMAGE_REFERENCE
- VIDEO + VIDEO_REFERENCE
- VIDEO + BOSMAX_IMAGE_HANDOFF
Output required:
- batch_plan
- batch_prompt_pack
- batch_summary
```

---

## Template 5 — `BATCH_MULTI_PRODUCT_CONTROLLED`

Use only when you already have multiple products with clear truth and scale anchors.
The safest first multi-product benchmark is usually `IMAGE_ONLY`.

```text
Mode: BULK
Batch type: BATCH_MULTI_PRODUCT_CONTROLLED
Batch goal: [IMAGE_ONLY / VIDEO_ONLY / MIXED]
Product scope: MULTI_PRODUCT
Total output count: [10 / 25 / 50]
Platform: [TikTok / Shopee / Lazada / Meta]
Language: [Malay / English]

Product list:
- Product: [PRODUCT A]
  Variant: [VARIANT]
  Target count: [N]
  Scale anchor: [EXACT SCALE ANCHOR]
- Product: [PRODUCT B]
  Variant: [VARIANT]
  Target count: [N]
  Scale anchor: [EXACT SCALE ANCHOR]

Batch variation mode: [COPY_VARIANT_BATCH / ANGLE_ROTATION_BATCH / VISUAL_VARIANT_BATCH / MATRIX_BATCH]
Angle lock: [ANGLE ID or NONE]
Semantic intent: [same commercial meaning to preserve]
Copy variant count: [N]
Visual variation level: [LOW / MEDIUM / HIGH]
Semantic drift guard: ON

Image count: [X]
Video count: [Y]

Image mix:
- VIDEO_SUPPORT: [PERCENT]
- SELLING_POSTER: [PERCENT]

Video mix:
- NONE: [PERCENT]
- IMAGE_REFERENCE: [PERCENT]
- VIDEO_REFERENCE: [PERCENT]
- BOSMAX_IMAGE_HANDOFF: [PERCENT]

Video engine: [ENGINE]
Duration target: [VALID DURATION]
Variation condition: [1 / 2 / 3]

Batch requirement:
Build Variant Plan first.
Separate rows cleanly by product truth, scale anchor, and compliance class.
Do not mix sensitive-product dialogue rules with direct-product dialogue rules in the same row logic.
For the first low-risk benchmark, prefer:
- `Batch goal: IMAGE_ONLY`
- `Image count = total output count`
- `Video count = 0`
Output required:
- batch_plan
- batch_prompt_pack
- batch_summary
```

---

## Fast Prompts — Ready Copy Blocks

### Fast block — 10 selling posters

```text
Mode: BULK
Batch type: BATCH_IMAGE_SELLING
Batch goal: IMAGE_ONLY
Product scope: SINGLE_PRODUCT
Content quantity: 10
Platform: TikTok
Language: Malay
Produk: [PRODUCT NAME]
Variant: [VARIANT]
Scale anchor: [EXACT SCALE ANCHOR]
Image mix:
- VIDEO_SUPPORT: 0%
- SELLING_POSTER: 100%
Variation condition: 3
Build Variant Plan first. Every row must resolve to IMAGE + SELLING_POSTER.
```

### Fast block — 10 copy variants from one selling angle

```text
Mode: BULK
Batch type: BATCH_IMAGE_SELLING
Batch goal: IMAGE_ONLY
Batch variation mode: COPY_VARIANT_BATCH
Product scope: SINGLE_PRODUCT
Content quantity: 10
Platform: TikTok
Language: Malay
Produk: [PRODUCT NAME]
Product ID: [PRODUCT ID]
Scale anchor: [EXACT SCALE ANCHOR]
Angle lock: [ANGLE ID + angle name]
Semantic intent: [same meaning to preserve]
Copy variant count: 10
Visual variation level: LOW
Image mix:
- SELLING_POSTER: 100%
- VIDEO_SUPPORT: 0%
Build Variant Plan first.
Every row must keep the same angle meaning.
Every row must vary copywriting wording.
Do not rotate to a different angle unless user explicitly changes batch_variation_mode to ANGLE_ROTATION_BATCH.
```

### Fast block — 10 fresh videos

```text
Mode: BULK
Batch type: BATCH_VIDEO_FRESH
Batch goal: VIDEO_ONLY
Product scope: SINGLE_PRODUCT
Content quantity: 10
Platform: TikTok
Language: Malay
Produk: [PRODUCT NAME]
Variant: [VARIANT]
Scale anchor: [EXACT SCALE ANCHOR]
Video engine: [ENGINE]
Duration target: [VALID DURATION]
Video mix:
- NONE: 100%
- IMAGE_REFERENCE: 0%
- VIDEO_REFERENCE: 0%
- BOSMAX_IMAGE_HANDOFF: 0%
Variation condition: 3
Build Variant Plan first. Every row must resolve to VIDEO + NONE.
```

### Sensitive note for fresh-video batches

If product is sensitive:
- set `Dialogue authority: SCRIPT_REGISTRY`
- keep one silo per batch
- keep one variant family per first benchmark
- do not freestyle direct sexual-health wording

### Fast block — 50 clean support images

```text
Mode: BULK
Batch type: BATCH_IMAGE_SUPPORT
Batch goal: IMAGE_ONLY
Product scope: SINGLE_PRODUCT
Content quantity: 50
Platform: TikTok
Language: Malay
Produk: [PRODUCT NAME]
Variant: [VARIANT]
Scale anchor: [EXACT SCALE ANCHOR]
Image mix:
- VIDEO_SUPPORT: 100%
- SELLING_POSTER: 0%
Variation condition: 2
Build Variant Plan first. Every row must resolve to IMAGE + VIDEO_SUPPORT.
```

---

## Final Rule

If a batch request conflicts with:
- `BOSMAX_DETERMINISTIC_FLOW_v1.md`
- `BOSMAX_BATCH_LANE_v1.md`
- product truth from registry

those authority layers win.
