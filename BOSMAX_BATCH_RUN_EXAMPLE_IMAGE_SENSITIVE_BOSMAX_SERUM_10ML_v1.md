# BOSMAX Batch Run Example — Image Sensitive — BOSMAX Serum 10ML v1
# Date: 2026-06-02
# Status: 10ML companion sensitive image benchmark for BOSMAX Serum

## Objective

This is the first `10ML` companion sensitive image benchmark for:
`BOSMAX Serum`.

Use case:
- flagship BOSMAX sensitive male stealth product
- image generation with owner-supplied `10ML` product reference lock
- no explicit anatomy cues
- safe selling-poster benchmark for the taller standard-size companion variant

This example uses:
- `BATCH_IMAGE_SELLING`
- `Content quantity: 10`
- `Platform: TikTok`
- `Language: Malay`
- `Reference requirement: actual BOSMAX 10ML product image must be uploaded`

---

## Product Truth Lock

### Product
- `BOSMAX Serum`
- variant: `10ML`

### Exact scale anchor
- `EXACTLY chapstick size, fit into fingers naturally`

### Reference-bound image authority
- local primary reference: `reference_images/bosmax/bosmax_serum_10ml_primary.png`
- use uploaded reference as absolute truth for:
  - chapstick-sized slim cylindrical bottle geometry
  - glossy black cap
  - matte black body
  - white `BOSMAX HERBS` branding
  - taller natural-wellness front-label hierarchy

### Hard compliance rules
- no explicit body-part visuals
- no explicit sexual-performance claims in overlay
- no feminized cosmetic styling
- no bottle redesign
- no scale drift into deodorant, perfume, serum pump, or dropper packaging
- no label drift away from `BOSMAX HERBS`

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

Produk: BOSMAX Serum
Variant: 10ML
Scale anchor: EXACTLY chapstick size, fit into fingers naturally

Reference upload:
- bosmax_serum_10ml_primary.png

Image mix:
- VIDEO_SUPPORT: 0%
- SELLING_POSTER: 100%

Variation condition: 3

Avatar pool:
- RIZAL
- AZMAN

Scene pool:
- masculine premium black backdrop
- clean wellness in-hand presentation
- private shelf routine setup
- premium stealth product stage

Compliance rule:
- stealth positioning only
- no explicit anatomy or obscene wording
- preserve uploaded BOSMAX 10ML product truth exactly

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
    PRODUCT: BOSMAX SERUM 10ML | REFERENCE-BOUND SENSITIVE IMAGE LANE ═══

SET | TASK MODE | SUBMODE         | PRODUCT        | AVATAR | SCENE BUCKET                 | FUNCTION
----|-----------|-----------------|----------------|--------|------------------------------|------------------------------
1   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | RIZAL  | masculine premium black      | flagship tall-bottle poster
2   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | AZMAN  | clean wellness in-hand       | discreet confidence poster
3   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | RIZAL  | private shelf routine setup  | daily-routine poster
4   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | AZMAN  | premium stealth product stage| premium conversion poster
5   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | RIZAL  | masculine premium black      | hero black-tube poster
6   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | AZMAN  | clean wellness in-hand       | handheld standard-size poster
7   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | RIZAL  | private shelf routine setup  | low-noise stealth poster
8   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | AZMAN  | premium stealth product stage| direct-response poster
9   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | RIZAL  | masculine premium black      | authority poster
10  | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | AZMAN  | clean wellness in-hand       | final companion poster
```

---

## Row Expansion Rule

Every row above must expand into:
- `IMAGE + SELLING_POSTER`

This means every generated prompt must include:
- uploaded BOSMAX 10ML reference-bound product truth
- exact chapstick-sized scale lock
- row-specific avatar lock
- stealth-safe selling hierarchy
- no explicit anatomy cues

No row may drift into:
- `IMAGE + VIDEO_SUPPORT`
- `VIDEO + NONE`
- reference-free product redesign
- skincare-pump or perfume-bottle logic

---

## Operator Notes

Why this is the `10ML` image companion benchmark:
- proves BOSMAX can hold both flagship sizes, not just the smallest one
- `10ML` has a different vertical read and label hierarchy from `5ML`
- stronger companion benchmark reduces the chance that the system only knows one BOSMAX silhouette

Companion benchmark after this:
- `BATCH_VIDEO_FRESH`
- `BOSMAX Serum`
- `10ML`
- `KLING_3_0`
- `10s`

---

## Final Rule

If anything in this example conflicts with:
- `products/BOSMAX_SERUM.yaml`
- `SCRIPT_REGISTRY_UNIFIED.md`
- `SCRIPT_VARIANT_LIBRARY.md`
- `BOSMAX_BATCH_LANE_v1.md`

those authority layers win.
