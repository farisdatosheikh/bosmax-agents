# BOSMAX Batch Run Example — Multi Product Controlled — Minyak Warisan Cap Burung + Minyak Jungle Girl v1
# Date: 2026-06-02
# Status: Fourth real production example

## Objective

This is the fourth real BOSMAX batch run example and the first
`BATCH_MULTI_PRODUCT_CONTROLLED` benchmark.

Products used:
- `Minyak Warisan Cap Burung`
- `Minyak Jungle Girl`

Use case:
- two known direct-product lanes only
- no sensitive-product dialogue lane
- low-risk first multi-product benchmark
- controlled image-only run before any multi-product video expansion

This example uses:
- `BATCH_MULTI_PRODUCT_CONTROLLED`
- `Content quantity: 10`
- `Platform: TikTok`
- `Language: Malay`
- `Batch goal: IMAGE_ONLY`
- `Image split: 10 × IMAGE + SELLING_POSTER`
- `Video split: 0`

---

## Product Truth Lock

### Product A
- `Minyak Warisan Cap Burung`
- variant: `30ML WG40 Bottle`
- scale anchor: `EXACTLY a small pocket-size 30ml rectangular clear glass medicated oil bottle with a red ribbed cap, shorter than the palm and only two fingers wide`

### Product B
- `Minyak Jungle Girl`
- variant: `30ML JG01`
- scale anchor: `EXACTLY a compact 30ml massage oil bottle size, naturally hand-sized`

### Multi-product rule
- each row must preserve its own product truth and scale anchor
- no cross-pollination between product A and product B packaging descriptors
- no sensitive-product script-registry rules in this benchmark

### Hard negatives
- no product A label drifting into product B rows
- no product B title drifting into product A rows
- no scale-anchor swapping between rows
- no mixed compliance logic
- no multi-product row merging

---

## Ready-Copy Batch Intake Block

```text
Mode: BULK
Batch type: BATCH_MULTI_PRODUCT_CONTROLLED
Batch goal: IMAGE_ONLY
Product scope: MULTI_PRODUCT
Total output count: 10
Platform: TikTok
Language: Malay

Product list:
- Product: Minyak Warisan Cap Burung
  Variant: 30ML WG40 Bottle
  Target count: 5
  Scale anchor: EXACTLY a small pocket-size 30ml rectangular clear glass medicated oil bottle with a red ribbed cap, shorter than the palm and only two fingers wide
- Product: Minyak Jungle Girl
  Variant: 30ML JG01
  Target count: 5
  Scale anchor: EXACTLY a compact 30ml massage oil bottle size, naturally hand-sized

Image count: 10
Video count: 0

Image mix:
- VIDEO_SUPPORT: 0%
- SELLING_POSTER: 100%

Video mix:
- NONE: 0%
- IMAGE_REFERENCE: 0%
- VIDEO_REFERENCE: 0%
- BOSMAX_IMAGE_HANDOFF: 0%

Variation condition: 2

Avatar pool:
- SARA
- MAK_TOK
- BELLA
- AZMAN

Scene pool:
- heritage remedy studio backdrop
- practical home medicine corner
- lifestyle in-hand direct product setup
- premium clean poster composition

Batch requirement:
Build Variant Plan first.
Separate rows cleanly by product truth and scale anchor.
Every row in this benchmark must resolve to IMAGE + SELLING_POSTER.
Output required:
- batch_plan
- batch_prompt_pack
- batch_summary
```

---

## Approved Variant Plan Example

```text
═══ VARIANT PLAN — 10 SETS | BATCH TYPE: BATCH_MULTI_PRODUCT_CONTROLLED | PLATFORM: TikTok |
    GOAL: IMAGE_ONLY | SUBMODE: SELLING_POSTER ONLY ═══

SET | TASK MODE | SUBMODE         | PRODUCT                       | AVATAR   | SCENE BUCKET                  | FUNCTION
----|-----------|-----------------|-------------------------------|----------|-------------------------------|----------------------------------
1   | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | SARA     | heritage remedy studio        | hero trust poster
2   | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | MAK_TOK  | home medicine corner          | heritage authority poster
3   | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | BELLA    | lifestyle in-hand             | compact carry poster
4   | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | AZMAN    | premium clean composition     | practical relief poster
5   | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | SARA     | family-home remedy setup      | household essential poster
6   | IMAGE     | SELLING_POSTER  | Minyak Jungle Girl            | BELLA    | lifestyle in-hand             | direct product poster
7   | IMAGE     | SELLING_POSTER  | Minyak Jungle Girl            | MAK_TOK  | practical home corner         | tradition / value poster
8   | IMAGE     | SELLING_POSTER  | Minyak Jungle Girl            | AZMAN    | premium clean composition     | straightforward product poster
9   | IMAGE     | SELLING_POSTER  | Minyak Jungle Girl            | SARA     | warm remedy shelf             | compact utility poster
10  | IMAGE     | SELLING_POSTER  | Minyak Jungle Girl            | BELLA    | simple direct retail setup    | final value poster
```

---

## Row Expansion Rule

Every row above must expand into:
- `IMAGE + SELLING_POSTER`

This means every generated prompt must include:
- row-specific avatar lock
- row-specific product truth lock
- row-specific scale anchor
- selling hierarchy
- negative lock block
- no reference-media dependency

No row may drift into:
- `IMAGE + VIDEO_SUPPORT`
- any video route
- any sensitive-product dialogue authority path

---

## Prompt-Pack Target Shape

For this example, the final batch output should contain:

### `batch_plan`
- the exact 10 approved rows

### `batch_prompt_pack`
- 10 final selling-poster prompts
- 5 prompts for `Minyak Warisan Cap Burung`
- 5 prompts for `Minyak Jungle Girl`
- each one labeled by `job_id` or `set number`
- each one carrying its own exact product truth and exact scale anchor

### `batch_summary`
- `total_jobs: 10`
- `image_jobs: 10`
- `video_jobs: 0`
- `products_covered: 2`
- `failed_jobs: 0` unless validation fails
- `blocked_jobs: 0` unless validation fails

---

## Operator Notes

Why this is the fourth benchmark:
- first multi-product benchmark
- keeps both products in direct-product lanes
- avoids sensitive-product registry complications
- uses image-only selling rows for the safest first multi-product dispatcher test

Current caution:
- `Minyak Jungle Girl` is currently registry-provisional from FASTMOSS tier-2
- harden product B later with direct uploaded product image, exact bottle truth,
  and richer prompt locks before promoting it to heavier production lanes

---

## Final Rule

If anything in this example conflicts with:
- `products/CAP_BURUNG_MINYAK.yaml`
- `products/JUNGLE_GIRL_MINYAK.yaml`
- `BOSMAX_DETERMINISTIC_FLOW_v1.md`
- `BOSMAX_BATCH_LANE_v1.md`

those authority layers win.
