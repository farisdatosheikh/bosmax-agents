# BOSMAX Batch Run Example — Image Sensitive — BOSMAX Serum v1
# Date: 2026-06-02
# Status: First reference-bound sensitive image benchmark for BOSMAX Serum

## Objective

This is the first reference-bound sensitive image benchmark for:
`BOSMAX Serum`.

Use case:
- flagship BOSMAX sensitive male stealth product
- image generation with owner-supplied product reference lock
- no explicit anatomy cues
- safe selling-poster benchmark after visual hardening of `BOSMAX_SERUM.yaml`

This example uses:
- `BATCH_IMAGE_SELLING`
- `Content quantity: 10`
- `Platform: TikTok`
- `Language: Malay`
- `Reference requirement: actual BOSMAX 5ML product image must be uploaded`

---

## Product Truth Lock

### Product
- `BOSMAX Serum`
- variant: `5ML`

### Exact scale anchor
- `EXACTLY lip balm size, fit into fingers naturally`

### Reference-bound image authority
- local primary reference: `reference_images/bosmax/bosmax_serum_5ml_primary.jpg`
- use uploaded reference as absolute truth for:
  - tiny lip-balm-sized cylindrical bottle geometry
  - glossy black cap
  - matte black body
  - white `BOSMAX HERBS` branding
  - discreet masculine minimal label system

### Hard compliance rules
- no explicit body-part visuals
- no explicit sexual-performance claims in overlay
- no feminized cosmetic styling
- no bottle redesign
- no scale drift into perfume, deodorant, or skincare pump packaging
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
Variant: 5ML
Scale anchor: EXACTLY lip balm size, fit into fingers naturally

Reference upload:
- bosmax_serum_5ml_primary.jpg

Image mix:
- VIDEO_SUPPORT: 0%
- SELLING_POSTER: 100%

Variation condition: 3

Avatar pool:
- RIZAL
- AZMAN

Scene pool:
- masculine premium black backdrop
- discreet in-hand confidence presentation
- private shelf routine setup
- premium stealth product stage

Compliance rule:
- stealth positioning only
- no explicit anatomy or obscene wording
- preserve uploaded BOSMAX 5ML product truth exactly

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
    PRODUCT: BOSMAX SERUM 5ML | REFERENCE-BOUND SENSITIVE IMAGE LANE ═══

SET | TASK MODE | SUBMODE         | PRODUCT        | AVATAR | SCENE BUCKET                    | FUNCTION
----|-----------|-----------------|----------------|--------|---------------------------------|------------------------------
1   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | RIZAL  | masculine premium black         | flagship trust poster
2   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | AZMAN  | in-hand confidence presentation | discreet carry poster
3   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | RIZAL  | private shelf routine setup     | daily-routine poster
4   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | AZMAN  | premium stealth product stage   | premium conversion poster
5   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | RIZAL  | masculine premium black         | brand-authority poster
6   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | AZMAN  | in-hand confidence presentation | compact-size poster
7   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | RIZAL  | private shelf routine setup     | low-noise stealth poster
8   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | AZMAN  | premium stealth product stage   | hero black-bottle poster
9   | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | RIZAL  | masculine premium black         | direct-response poster
10  | IMAGE     | SELLING_POSTER  | BOSMAX Serum   | AZMAN  | in-hand confidence presentation | final flagship poster
```

---

## Row Expansion Rule

Every row above must expand into:
- `IMAGE + SELLING_POSTER`

This means every generated prompt must include:
- uploaded BOSMAX 5ML reference-bound product truth
- exact lip-balm-sized scale lock
- row-specific avatar lock
- stealth-safe selling hierarchy
- no explicit anatomy cues

No row may drift into:
- `IMAGE + VIDEO_SUPPORT`
- `VIDEO + NONE`
- reference-free product redesign
- feminized cosmetic bottle logic

---

## Operator Notes

Why this is the first BOSMAX Serum image benchmark:
- strongest current owner-supplied reference is the `5ML` handheld image
- smallest variant has the highest risk of scale drift if left unbound
- proving the `5ML` first gives BOSMAX the hardest visual benchmark before expanding to `10ML`

Companion benchmark after this:
- `BATCH_VIDEO_FRESH`
- `BOSMAX Serum`
- `5ML`
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
