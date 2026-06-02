# BOSMAX Batch Run Example — Minyak Warisan Cap Burung v1
# Date: 2026-06-02
# Status: First real production example

## Objective

This is the first real BOSMAX batch run example for one actual product:
`Minyak Warisan Cap Burung`.

Use case:
- direct product
- stable scale anchor
- strong TikTok Shop poster demand
- low ambiguity for first production benchmark

This example uses:
- `BATCH_IMAGE_SELLING`
- `Content quantity: 10`
- `Platform: TikTok`
- `Language: Malay`

---

## Product Truth Lock

### Product
- `Minyak Warisan Cap Burung`
- variant: `30ML WG40 Bottle`

### Exact scale anchor
- `EXACTLY a compact 30ml oblong clear glass medicated oil bottle with a red cap, naturally hand-sized`

### Packaging truth
- WG40 30ml oblong clear flint glass bottle
- red ribbed screw cap
- hidden stopper / PE plug
- translucent emerald herbal green oil
- dark forest green label
- cream center panel
- gold border
- perched bird on leafy branch
- exact printed label text: `Sejak 1958, Petua Turun Temurun.`

### Hard negatives
- no black cap
- no roller ball
- no roll-on applicator
- no square bottle
- no pump top
- no dropper cap
- no spray nozzle
- no label morphing
- no flying bird
- no oversized bottle hallucination

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

Produk: Minyak Warisan Cap Burung
Variant: 30ML WG40 Bottle
Scale anchor: EXACTLY a compact 30ml oblong clear glass medicated oil bottle with a red cap, naturally hand-sized

Image mix:
- VIDEO_SUPPORT: 0%
- SELLING_POSTER: 100%

Variation condition: 3

Avatar pool:
- SARA
- MAK_TOK
- BELLA
- AZMAN

Scene pool:
- clean ivory studio heritage backdrop
- warm household medicine corner
- lifestyle bedside / living room context
- premium traditional remedy product stage

Copy angle pool:
- 14 kegunaan
- warisan sejak 1958
- wajib ada di rumah
- travel / simpan dalam beg
- resdung / pening / kembung / gigitan serangga

CTA style pool:
- soft trust CTA
- practical household CTA

Build Variant Plan first.
Every row must resolve to IMAGE + SELLING_POSTER.
Output required:
- batch_plan
- batch_prompt_pack
- batch_summary
```

---

## Approved Variant Plan Example

```text
═══ VARIANT PLAN — 10 SETS | BATCH TYPE: BATCH_IMAGE_SELLING | PLATFORM: TikTok |
    CONDITION: 3 | DIALOG: VARIES | AVATAR: ROTATES ═══

SET | TASK MODE | SUBMODE         | PRODUCT                       | AVATAR   | SCENE BUCKET                  | COPY ANGLE
----|-----------|-----------------|-------------------------------|----------|-------------------------------|-----------------------------
1   | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | SARA     | ivory studio heritage         | 14 kegunaan / 1 botol
2   | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | MAK_TOK  | warm household medicine corner| warisan sejak 1958
3   | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | BELLA    | lifestyle bedside             | wajib ada di rumah
4   | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | AZMAN    | premium product stage         | travel / dalam beg
5   | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | SARA     | living room practical context | pening kepala
6   | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | MAK_TOK  | warm medicine shelf           | resdung
7   | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | BELLA    | premium ivory spotlight       | kembung
8   | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | AZMAN    | travel / bag context          | gigitan serangga
9   | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | SARA     | heritage remedy display       | tradisi terbukti dipercayai
10  | IMAGE     | SELLING_POSTER  | Minyak Warisan Cap Burung     | MAK_TOK  | family-home remedy corner     | botol kecil banyak guna
```

---

## Row Expansion Rule

Every row above must expand into:
- `IMAGE + SELLING_POSTER`

This means every generated prompt must include:
- avatar lock for that row
- exact product truth lock
- selling hierarchy
- negative lock block
- TikTok-safe composition

No row may drift into:
- `VIDEO_SUPPORT`
- video prompt logic
- generic Mode C logic

---

## Prompt-Pack Target Shape

For this example, the final batch output should contain:

### `batch_plan`
- the exact 10 approved rows

### `batch_prompt_pack`
- 10 final selling-poster prompts
- each one labeled by `job_id` or `set number`
- each one carrying the same product truth and exact scale anchor

### `batch_summary`
- `total_jobs: 10`
- `image_jobs: 10`
- `video_jobs: 0`
- `failed_jobs: 0` unless validation fails
- `blocked_jobs: 0` unless validation fails
- `products_covered: 1`

---

## Operator Notes

Why this is the first benchmark:
- direct product lane
- stable packaging truth
- strong retail use case
- easy to visually audit

Companion benchmark now available:
- `BOSMAX_BATCH_RUN_EXAMPLE_VIDEO_FRESH_MINYAK_WARISAN_CAP_BURUNG_v1.md`
- same product
- `BATCH_VIDEO_FRESH`
- `10` outputs
- `KLING_3_0`
- `10s`

---

## Final Rule

If anything in this example conflicts with:
- `products/CAP_BURUNG_MINYAK.yaml`
- `BOSMAX_DETERMINISTIC_FLOW_v1.md`
- `BOSMAX_BATCH_LANE_v1.md`

those authority layers win.
