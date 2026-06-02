# BOSMAX Batch Run Example — Video Fresh — Maverix Maxoil v1
# Date: 2026-06-02
# Status: First sensitive production example for Maverix

## Objective

This is the first real BOSMAX sensitive batch run example for:
`Maverix Maxoil`.

Use case:
- sensitive male stealth product
- fresh video generation from zero
- no reference media dependency
- dialogue routed through script registry, not freestyle AI copy

This example uses:
- `BATCH_VIDEO_FRESH`
- `Content quantity: 10`
- `Platform: TikTok`
- `Language: Malay`
- `Video engine: KLING_3_0`
- `Duration target: 10s`

---

## Product Truth Lock

### Product
- `Maverix Maxoil`
- variant: `SET_5_BOTTLES`

### Exact scale anchor
- `EXACTLY lip balm size per bottle, fit into fingers naturally, sold as a 5-bottle set`

### Dialogue authority lock
- authority source: `products/MAVERIX_MAXOIL.yaml`
- dialogue mode: `SCRIPT_REGISTRY`
- registry file: `SCRIPT_REGISTRY_UNIFIED.md`
- variant file: `SCRIPT_VARIANT_LIBRARY.md`
- silo: `male_health_stealth_01`
- variant family: `EGO_01`

### Hard compliance rules
- no direct anatomy wording
- no explicit sexual-performance claims
- no obscene slang
- no medical-cure language
- no freestyle hook outside script-registry lane
- no Mode C continuity assumptions
- no reference-image dependency

---

## Ready-Copy Batch Intake Block

```text
Mode: BULK
Batch type: BATCH_VIDEO_FRESH
Batch goal: VIDEO_ONLY
Product scope: SINGLE_PRODUCT
Content quantity: 10
Platform: TikTok
Language: Malay
Video engine: KLING_3_0
Duration target: 10s
Reference mode: NONE
Content mode: T2V

Produk: Maverix Maxoil
Variant: SET_5_BOTTLES
Scale anchor: EXACTLY lip balm size per bottle, fit into fingers naturally, sold as a 5-bottle set

Dialogue authority:
- mode: SCRIPT_REGISTRY
- silo: male_health_stealth_01
- variant family: EGO_01

Variation condition: 3

Avatar pool:
- RIZAL
- AZMAN

Scene pool:
- calm masculine explainer setup
- discreet daily-routine shelf
- confident pocket-carry setup
- premium product confidence stage

Formula pool:
- SAVAGE_HPAS
- PAS
- HSO

Build Variant Plan first.
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
═══ VARIANT PLAN — 10 SETS | BATCH TYPE: BATCH_VIDEO_FRESH | PLATFORM: TikTok |
    ENGINE: KLING_3_0 | DURATION: 10s | SILO: male_health_stealth_01 ═══

SET | TASK MODE | SUBMODE | PRODUCT         | AVATAR | FORMULA      | SCENE BUCKET                  | DIALOGUE FAMILY
----|-----------|---------|-----------------|--------|--------------|-------------------------------|----------------
1   | VIDEO     | NONE    | Maverix Maxoil  | RIZAL  | SAVAGE_HPAS  | calm masculine explainer      | EGO_01
2   | VIDEO     | NONE    | Maverix Maxoil  | AZMAN  | PAS          | discreet daily-routine shelf  | EGO_01
3   | VIDEO     | NONE    | Maverix Maxoil  | RIZAL  | HSO          | confident pocket-carry setup  | EGO_01
4   | VIDEO     | NONE    | Maverix Maxoil  | AZMAN  | SAVAGE_HPAS  | premium confidence stage      | EGO_01
5   | VIDEO     | NONE    | Maverix Maxoil  | RIZAL  | PAS          | calm masculine explainer      | EGO_01
6   | VIDEO     | NONE    | Maverix Maxoil  | AZMAN  | HSO          | discreet daily-routine shelf  | EGO_01
7   | VIDEO     | NONE    | Maverix Maxoil  | RIZAL  | SAVAGE_HPAS  | confident pocket-carry setup  | EGO_01
8   | VIDEO     | NONE    | Maverix Maxoil  | AZMAN  | PAS          | premium confidence stage      | EGO_01
9   | VIDEO     | NONE    | Maverix Maxoil  | RIZAL  | HSO          | calm masculine explainer      | EGO_01
10  | VIDEO     | NONE    | Maverix Maxoil  | AZMAN  | SAVAGE_HPAS  | discreet daily-routine shelf  | EGO_01
```

---

## Row Expansion Rule

Every row above must expand into:
- `VIDEO + NONE`

This means every generated prompt must include:
- row-specific avatar lock
- Maverix product truth lock
- `KLING_3_0` engine lock
- `10s` duration lock
- resolved stealth dialogue payload from `male_health_stealth_01 / EGO_01`
- no explicit/direct sensitive wording

No row may drift into:
- `IMAGE_REFERENCE`
- `VIDEO_REFERENCE`
- `BOSMAX_IMAGE_HANDOFF`
- direct-product dialogue logic
- multi-block logic

---

## Prompt-Pack Target Shape

For this example, the final batch output should contain:

### `batch_plan`
- the exact 10 approved rows

### `batch_prompt_pack`
- 10 final fresh-video prompts
- each one labeled by `job_id` or `set number`
- each one carrying the same Maverix truth and same scale anchor
- each one carrying `KLING_3_0` and `10s` as locked runtime fields
- each one carrying `dialogue_authority_resolved` from `male_health_stealth_01 / EGO_01`

### `batch_summary`
- `total_jobs: 10`
- `image_jobs: 0`
- `video_jobs: 10`
- `failed_jobs: 0` unless validation fails
- `blocked_jobs: 0` unless validation fails
- `products_covered: 1`
- `engines_covered: 1`

---

## Operator Notes

Why this is the first Maverix benchmark:
- fastest way to prove sensitive-lane strength
- video is BOSMAX core advantage here
- same stealth family across all rows reduces risk
- avoids visual-truth overreach while product packaging is still provisional

Companion benchmark after this:
- `BATCH_MULTI_PRODUCT_CONTROLLED`
- `Bosmax Serum + Maverix Maxoil`
- same silo
- same `male_health_stealth_01`

---

## Final Rule

If anything in this example conflicts with:
- `products/MAVERIX_MAXOIL.yaml`
- `SCRIPT_REGISTRY_UNIFIED.md`
- `SCRIPT_VARIANT_LIBRARY.md`
- `BOSMAX_BATCH_LANE_v1.md`

those authority layers win.
