# BOSMAX Batch Run Example — Image Sensitive — Maverix Maxoil v1
# Date: 2026-06-02
# Status: First sensitive image production example

## Objective

This is the first reference-bound sensitive image benchmark for:
`Maverix Maxoil`.

Use case:
- sensitive male stealth product
- image generation with actual product reference lock
- no explicit anatomy cues
- safe selling-poster benchmark after visual truth hardening

This example uses:
- `BATCH_IMAGE_SELLING`
- `Content quantity: 10`
- `Platform: TikTok`
- `Language: Malay`
- `Reference requirement: actual Maverix product image must be uploaded`

---

## Product Truth Lock

### Product
- `Maverix Maxoil`
- variant: `SET_5_BOTTLES`

### Exact scale anchor
- `EXACTLY lip balm size per bottle, fit into fingers naturally, sold as a 5-bottle set`

### Reference-bound image authority
- local primary reference: `reference_images/maverix/maverix_fastmoss_primary.jpg`
- local secondary reference: `reference_images/maverix/maverix_fastmoss_secondary.webp`
- use uploaded reference as absolute truth for:
  - 5-bottle set structure
  - black masculine carton
  - slim cylindrical bottles
  - black caps
  - horse silhouette branding

### Hard compliance rules
- no explicit body-part visuals
- no explicit sexual-performance claims in overlay
- no feminized pastel styling
- no bottle count drift
- no packaging redesign

---

## Ready-Copy Batch Intake Block

```text
Mode: BULK
Batch type: BATCH_IMAGE_SELLING
Batch goal: IMAGE_ONLY
Product scope: SINGLE_PRODUCT
Content quantity: 10
Platform: TikTok
Language: Malay

Produk: Maverix Maxoil
Variant: SET_5_BOTTLES
Scale anchor: EXACTLY lip balm size per bottle, fit into fingers naturally, sold as a 5-bottle set

Reference upload:
- maverix_fastmoss_primary.jpg
- optional secondary support: maverix_fastmoss_secondary.webp

Image mix:
- VIDEO_SUPPORT: 0%
- SELLING_POSTER: 100%

Variation condition: 2

Avatar pool:
- RIZAL
- AZMAN

Scene pool:
- masculine premium black backdrop
- discreet bedside luxury setup
- in-hand confidence presentation
- premium direct-response product stage

Compliance rule:
- stealth positioning only
- no explicit anatomy or obscene wording

Build Variant Plan first.
Every row must resolve to IMAGE + SELLING_POSTER.
Every row must preserve uploaded reference product truth.
Output required:
- batch_plan
- batch_prompt_pack
- batch_summary
```

---

## Approved Variant Plan Example

```text
═══ VARIANT PLAN — 10 SETS | BATCH TYPE: BATCH_IMAGE_SELLING | PLATFORM: TikTok |
    PRODUCT: MAVERIX MAXOIL | REFERENCE-BOUND SENSITIVE IMAGE LANE ═══

SET | TASK MODE | SUBMODE         | PRODUCT         | AVATAR | SCENE BUCKET                   | FUNCTION
----|-----------|-----------------|-----------------|--------|--------------------------------|-------------------------------
1   | IMAGE     | SELLING_POSTER  | Maverix Maxoil  | RIZAL  | masculine premium black        | hero trust poster
2   | IMAGE     | SELLING_POSTER  | Maverix Maxoil  | AZMAN  | discreet bedside luxury        | private-use value poster
3   | IMAGE     | SELLING_POSTER  | Maverix Maxoil  | RIZAL  | in-hand confidence presentation| compact set poster
4   | IMAGE     | SELLING_POSTER  | Maverix Maxoil  | AZMAN  | premium direct-response stage  | premium kit poster
5   | IMAGE     | SELLING_POSTER  | Maverix Maxoil  | RIZAL  | masculine premium black        | discreet confidence poster
6   | IMAGE     | SELLING_POSTER  | Maverix Maxoil  | AZMAN  | bedside luxury                 | private routine poster
7   | IMAGE     | SELLING_POSTER  | Maverix Maxoil  | RIZAL  | in-hand confidence presentation| small-bottle precision poster
8   | IMAGE     | SELLING_POSTER  | Maverix Maxoil  | AZMAN  | premium direct-response stage  | premium black kit poster
9   | IMAGE     | SELLING_POSTER  | Maverix Maxoil  | RIZAL  | masculine premium black        | direct stealth-sell poster
10  | IMAGE     | SELLING_POSTER  | Maverix Maxoil  | AZMAN  | discreet bedside luxury        | final conversion poster
```

---

## Row Expansion Rule

Every row above must expand into:
- `IMAGE + SELLING_POSTER`

This means every generated prompt must include:
- uploaded reference-bound product truth
- exact set geometry and bottle count
- row-specific avatar lock
- stealth-safe selling hierarchy
- no explicit anatomy cues

No row may drift into:
- `IMAGE + VIDEO_SUPPORT`
- `VIDEO + NONE`
- reference-free product redesign
- direct explicit sensitive wording

---

## Final Rule

If anything in this example conflicts with:
- `products/MAVERIX_MAXOIL.yaml`
- `SCRIPT_REGISTRY_UNIFIED.md`
- `SCRIPT_VARIANT_LIBRARY.md`
- `BOSMAX_BATCH_LANE_v1.md`

those authority layers win.
