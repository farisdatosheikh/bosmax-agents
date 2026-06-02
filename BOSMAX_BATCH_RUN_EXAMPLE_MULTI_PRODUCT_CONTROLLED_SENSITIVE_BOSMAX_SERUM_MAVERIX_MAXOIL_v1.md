# BOSMAX Batch Run Example — Multi Product Controlled Sensitive — BOSMAX Serum + Maverix Maxoil v1
# Date: 2026-06-02
# Status: First sensitive multi-product production example

## Objective

This is the first sensitive `BATCH_MULTI_PRODUCT_CONTROLLED` benchmark.

Products used:
- `BOSMAX Serum`
- `Maverix Maxoil`

Use case:
- two known sensitive male stealth products
- same silo
- same dialogue family
- controlled fresh-video dispatcher benchmark

This example uses:
- `BATCH_MULTI_PRODUCT_CONTROLLED`
- `Content quantity: 10`
- `Platform: TikTok`
- `Language: Malay`
- `Batch goal: VIDEO_ONLY`
- `Video split: 10 × VIDEO + NONE`
- `Video engine: KLING_3_0`
- `Duration target: 10s`

---

## Product Truth Lock

### Product A
- `BOSMAX Serum`
- variant: `5ML`
- scale anchor: `EXACTLY lip balm size, fit into fingers naturally`

### Product B
- `Maverix Maxoil`
- variant: `SET_5_BOTTLES`
- scale anchor: `EXACTLY lip balm size per bottle, fit into fingers naturally, sold as a 5-bottle set`

### Shared sensitive authority
- dialogue mode: `SCRIPT_REGISTRY`
- silo: `male_health_stealth_01`
- variant family: `EGO_01`
- benchmark law: same stealth rules across both products, but each product keeps its own truth and scale lock

### Hard compliance rules
- no direct anatomy wording
- no explicit sexual-performance claims
- no obscene slang
- no medical-cure language
- no cross-product dialogue confusion
- no direct-product copy logic

---

## Ready-Copy Batch Intake Block

```text
Mode: BULK
Batch type: BATCH_MULTI_PRODUCT_CONTROLLED
Batch goal: VIDEO_ONLY
Product scope: MULTI_PRODUCT
Total output count: 10
Platform: TikTok
Language: Malay

Product list:
- Product: BOSMAX Serum
  Variant: 5ML
  Target count: 5
  Scale anchor: EXACTLY lip balm size, fit into fingers naturally
  Dialogue authority: male_health_stealth_01 / EGO_01
- Product: Maverix Maxoil
  Variant: SET_5_BOTTLES
  Target count: 5
  Scale anchor: EXACTLY lip balm size per bottle, fit into fingers naturally, sold as a 5-bottle set
  Dialogue authority: male_health_stealth_01 / EGO_01

Image count: 0
Video count: 10

Image mix:
- VIDEO_SUPPORT: 0%
- SELLING_POSTER: 0%

Video mix:
- NONE: 100%
- IMAGE_REFERENCE: 0%
- VIDEO_REFERENCE: 0%
- BOSMAX_IMAGE_HANDOFF: 0%

Video engine: KLING_3_0
Duration target: 10s
Variation condition: 3

Avatar pool:
- RIZAL
- AZMAN

Formula pool:
- SAVAGE_HPAS
- PAS
- HSO

Batch requirement:
Build Variant Plan first.
Keep both products inside the same sensitive silo only.
Every row must resolve to VIDEO + NONE.
Every row must resolve dialogue_authority_resolved before script generation.
Output required:
- batch_plan
- batch_prompt_pack
- batch_summary
```

---

## Approved Variant Plan Example

```text
═══ VARIANT PLAN — 10 SETS | BATCH TYPE: BATCH_MULTI_PRODUCT_CONTROLLED | GOAL: VIDEO_ONLY |
    ENGINE: KLING_3_0 | DURATION: 10s | SILO: male_health_stealth_01 ═══

SET | TASK MODE | SUBMODE | PRODUCT         | AVATAR | FORMULA      | DIALOGUE FAMILY | FUNCTION
----|-----------|---------|-----------------|--------|--------------|-----------------|-------------------------------
1   | VIDEO     | NONE    | BOSMAX Serum    | RIZAL  | SAVAGE_HPAS  | EGO_01          | confidence-first fresh video
2   | VIDEO     | NONE    | BOSMAX Serum    | AZMAN  | PAS          | EGO_01          | daily-routine fresh video
3   | VIDEO     | NONE    | BOSMAX Serum    | RIZAL  | HSO          | EGO_01          | compact-use fresh video
4   | VIDEO     | NONE    | BOSMAX Serum    | AZMAN  | SAVAGE_HPAS  | EGO_01          | premium-angle fresh video
5   | VIDEO     | NONE    | BOSMAX Serum    | RIZAL  | PAS          | EGO_01          | soft-authority fresh video
6   | VIDEO     | NONE    | Maverix Maxoil  | AZMAN  | SAVAGE_HPAS  | EGO_01          | confidence-first fresh video
7   | VIDEO     | NONE    | Maverix Maxoil  | RIZAL  | PAS          | EGO_01          | daily-routine fresh video
8   | VIDEO     | NONE    | Maverix Maxoil  | AZMAN  | HSO          | EGO_01          | compact-set fresh video
9   | VIDEO     | NONE    | Maverix Maxoil  | RIZAL  | SAVAGE_HPAS  | EGO_01          | premium-angle fresh video
10  | VIDEO     | NONE    | Maverix Maxoil  | AZMAN  | PAS          | EGO_01          | soft-authority fresh video
```

---

## Row Expansion Rule

Every row above must expand into:
- `VIDEO + NONE`

This means every generated prompt must include:
- row-specific product truth
- row-specific scale anchor
- shared `male_health_stealth_01 / EGO_01` dialogue authority
- `KLING_3_0` engine lock
- `10s` duration lock
- no explicit/direct sensitive wording

No row may drift into:
- `IMAGE + SELLING_POSTER`
- `IMAGE + VIDEO_SUPPORT`
- `VIDEO + IMAGE_REFERENCE`
- `VIDEO + VIDEO_REFERENCE`
- `VIDEO + BOSMAX_IMAGE_HANDOFF`
- cross-silo dialogue logic

---

## Prompt-Pack Target Shape

For this example, the final batch output should contain:

### `batch_plan`
- the exact 10 approved rows

### `batch_prompt_pack`
- 5 fresh-video prompts for `BOSMAX Serum`
- 5 fresh-video prompts for `Maverix Maxoil`
- each one labeled by `job_id` or `set number`
- each one carrying its own product truth and scale anchor
- each one carrying shared stealth dialogue authority resolution

### `batch_summary`
- `total_jobs: 10`
- `image_jobs: 0`
- `video_jobs: 10`
- `products_covered: 2`
- `engines_covered: 1`
- `failed_jobs: 0` unless validation fails
- `blocked_jobs: 0` unless validation fails

---

## Operator Notes

Why this is the first sensitive multi-product benchmark:
- keeps both products inside the same male stealth silo
- avoids mixed-compliance chaos
- proves BOSMAX can handle `ubat kuat` lane with controlled authority, not freestyle prompting

Do not upgrade this benchmark to mixed image/video or mixed-silo until:
- Maverix visual truth is hardened with actual product images
- product-specific stealth variant strategy is mature enough for broader rotation

---

## Final Rule

If anything in this example conflicts with:
- `products/BOSMAX_SERUM.yaml`
- `products/MAVERIX_MAXOIL.yaml`
- `SCRIPT_REGISTRY_UNIFIED.md`
- `SCRIPT_VARIANT_LIBRARY.md`
- `BOSMAX_BATCH_LANE_v1.md`

those authority layers win.
