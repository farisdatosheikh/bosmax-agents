# BOSMAX Batch Run Example — Mixed Deterministic — Minyak Warisan Cap Burung v1
# Date: 2026-06-02
# Status: Third real production example

## Objective

This is the third real BOSMAX batch run example for one actual product:
`Minyak Warisan Cap Burung`.

Use case:
- same product truth across image and video rows
- controlled bridge between support-image lane and fresh-video lane
- deterministic mixed batch with no reference ambiguity
- first production benchmark for mixed daily operation

This example uses:
- `BATCH_MIXED_DETERMINISTIC`
- `Content quantity: 10`
- `Platform: TikTok`
- `Language: Malay`
- `Image split: 5 × IMAGE + VIDEO_SUPPORT`
- `Video split: 5 × VIDEO + NONE`
- `Video engine: KLING_3_0`
- `Duration target: 10s`

---

## Product Truth Lock

### Product
- `Minyak Warisan Cap Burung`
- variant: `30ML WG40 Bottle`

### Exact scale anchor
- `EXACTLY a small pocket-size 30ml rectangular clear glass medicated oil bottle with a red ribbed cap, shorter than the palm and only two fingers wide`

### Packaging truth
- WG40 30ml rectangular clear flint glass bottle
- red ribbed screw cap
- hidden stopper / PE plug
- translucent emerald herbal green oil
- dark forest green label
- cream center panel
- gold border
- perched bird on leafy branch
- exact printed label text: `Sejak 1958, Petua Turun Temurun.`

### Dialogue authority lock
- authority source: `products/CAP_BURUNG_MINYAK.yaml`
- video copywriting source: `copywriting_angles`
- mixed benchmark angle range for video rows: `A01` to `A05`

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
- no accidental shift from `VIDEO_SUPPORT` into `SELLING_POSTER`
- no accidental shift from `VIDEO + NONE` into reference-based video modes

---

## Ready-Copy Batch Intake Block

```text
Mode: BULK
Batch type: BATCH_MIXED_DETERMINISTIC
Batch goal: MIXED
Product scope: SINGLE_PRODUCT
Content quantity: 10
Platform: TikTok
Language: Malay

Produk: Minyak Warisan Cap Burung
Variant: 30ML WG40 Bottle
Scale anchor: EXACTLY a small pocket-size 30ml rectangular clear glass medicated oil bottle with a red ribbed cap, shorter than the palm and only two fingers wide

Image count: 5
Video count: 5

Image mix:
- VIDEO_SUPPORT: 100% of image rows
- SELLING_POSTER: 0% of image rows

Video mix:
- NONE: 100% of video rows
- IMAGE_REFERENCE: 0%
- VIDEO_REFERENCE: 0%
- BOSMAX_IMAGE_HANDOFF: 0%

Video engine: KLING_3_0
Duration target: 10s
Reference mode: NONE
Content mode: MIXED

Variation condition: 3

Avatar pool:
- SARA
- MAK_TOK
- BELLA
- AZMAN

Image scene pool:
- clean ivory support-image studio
- lifestyle in-hand home relief context
- bedside practical product-holding setup
- travel-ready carry scene

Video scene pool:
- calm studio explainer
- family medicine corner
- bedside relief context
- active home first-aid
- travel-ready emergency context

Video copy angle pool:
- A01 stres & aroma terapi
- A02 resdung & hidung tersumbat
- A03 batuk / selesema / sakit dada
- A04 gigitan serangga / gatal
- A05 luka kecil / bengkak

Build Variant Plan first.
Every image row must resolve to IMAGE + VIDEO_SUPPORT.
Every video row must resolve to VIDEO + NONE.
Output required:
- batch_plan
- batch_prompt_pack
- batch_summary
```

---

## Approved Variant Plan Example

```text
═══ VARIANT PLAN — 10 SETS | BATCH TYPE: BATCH_MIXED_DETERMINISTIC | PLATFORM: TikTok |
    IMAGE: 5 × VIDEO_SUPPORT | VIDEO: 5 × NONE | ENGINE: KLING_3_0 | DURATION: 10s ═══

SET | TASK MODE | SUBMODE        | PRODUCT                   | AVATAR  | SCENE BUCKET                   | ANGLE / FUNCTION
----|-----------|----------------|---------------------------|---------|--------------------------------|------------------------------
1   | IMAGE     | VIDEO_SUPPORT  | Minyak Warisan Cap Burung | SARA    | ivory support-image studio     | clean hand-held product prep
2   | IMAGE     | VIDEO_SUPPORT  | Minyak Warisan Cap Burung | MAK_TOK | home relief holding setup      | heritage product prep
3   | IMAGE     | VIDEO_SUPPORT  | Minyak Warisan Cap Burung | BELLA   | travel-ready carry scene       | compact product prep
4   | IMAGE     | VIDEO_SUPPORT  | Minyak Warisan Cap Burung | AZMAN   | bedside practical setup        | relief-context product prep
5   | IMAGE     | VIDEO_SUPPORT  | Minyak Warisan Cap Burung | SARA    | lifestyle in-hand close-up     | clean continuity-ready prep
6   | VIDEO     | NONE           | Minyak Warisan Cap Burung | SARA    | calm studio explainer          | A01 stres & aroma terapi
7   | VIDEO     | NONE           | Minyak Warisan Cap Burung | SARA    | bedside relief context         | A02 resdung / hidung tersumbat
8   | VIDEO     | NONE           | Minyak Warisan Cap Burung | MAK_TOK | family medicine corner         | A03 batuk / selesema / sakit dada
9   | VIDEO     | NONE           | Minyak Warisan Cap Burung | BELLA   | travel-ready emergency         | A04 gigitan serangga / gatal
10  | VIDEO     | NONE           | Minyak Warisan Cap Burung | AZMAN   | active home first-aid          | A05 luka kecil / bengkak
```

---

## Row Expansion Rule

Rows `1` to `5` must expand into:
- `IMAGE + VIDEO_SUPPORT`

This means every image-support prompt must include:
- avatar lock for that row
- exact product truth lock
- clean composition with minimal or zero selling text
- `source_image_handoff`-ready framing
- no selling-poster hierarchy

Rows `6` to `10` must expand into:
- `VIDEO + NONE`

This means every fresh-video prompt must include:
- avatar lock for that row
- exact product truth lock
- `KLING_3_0` engine lock
- `10s` duration lock
- Malay spoken-dialogue lane
- no reference-media dependency

No row may drift into:
- `IMAGE + SELLING_POSTER`
- `VIDEO + IMAGE_REFERENCE`
- `VIDEO + VIDEO_REFERENCE`
- `VIDEO + BOSMAX_IMAGE_HANDOFF`

---

## Prompt-Pack Target Shape

For this example, the final batch output should contain:

### `batch_plan`
- the exact 10 approved rows

### `batch_prompt_pack`
- 5 final support-image prompts
- 5 final fresh-video prompts
- each one labeled by `job_id` or `set number`
- all 10 carrying the same product truth and exact scale anchor
- video rows carrying `KLING_3_0` and `10s` as locked runtime fields

### `batch_summary`
- `total_jobs: 10`
- `image_jobs: 5`
- `video_jobs: 5`
- `failed_jobs: 0` unless validation fails
- `blocked_jobs: 0` unless validation fails
- `products_covered: 1`
- `engines_covered: 1`

---

## Operator Notes

Why this is the third benchmark:
- proves the mixed dispatcher can separate image rows and video rows cleanly
- keeps one product truth across both lanes
- avoids selling-poster noise inside the mixed benchmark
- acts as the first realistic bridge for operators building image prep plus fresh-video in one run

If this batch behaves well, the next recommended benchmark is:
- `BATCH_MULTI_PRODUCT_CONTROLLED`
- two known products only
- no sensitive-product mixing at first

---

## Final Rule

If anything in this example conflicts with:
- `products/CAP_BURUNG_MINYAK.yaml`
- `BOSMAX_DETERMINISTIC_FLOW_v1.md`
- `BOSMAX_BATCH_LANE_v1.md`

those authority layers win.
