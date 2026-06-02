# BOSMAX Batch Run Example — Video Fresh — Minyak Warisan Cap Burung v1
# Date: 2026-06-02
# Status: Second real production example

## Objective

This is the second real BOSMAX batch run example for one actual product:
`Minyak Warisan Cap Burung`.

Use case:
- direct product
- stable packaging truth
- fresh video generation from zero
- no reference media dependency
- low ambiguity for first video batch benchmark

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
- `Minyak Warisan Cap Burung`
- variant: `30ML WG40 Bottle`

### Exact scale anchor
- `EXACTLY a small pocket-size 30ml rectangular clear glass medicated oil bottle with a red ribbed cap, shorter than the palm and only two fingers wide`

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

### Dialogue authority lock
- authority source: `products/CAP_BURUNG_MINYAK.yaml`
- copywriting source: `copywriting_angles`
- benchmark angle range for this example: `A01` to `A10`
- named avatar pool aligned to registry recommendation

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

Produk: Minyak Warisan Cap Burung
Variant: 30ML WG40 Bottle
Scale anchor: EXACTLY a small pocket-size 30ml rectangular clear glass medicated oil bottle with a red ribbed cap, shorter than the palm and only two fingers wide
Dialogue authority: products/CAP_BURUNG_MINYAK.yaml → copywriting_angles

Variation condition: 3

Avatar pool:
- SARA
- MAK_TOK
- BELLA
- AZMAN
- JULIA

Scene pool:
- heritage home remedy setup
- bedside relief context
- kitchen / family medicine corner
- travel-ready emergency context
- calm studio explainer setup

Copy angle pool:
- A01 stres & aroma terapi
- A02 resdung & hidung tersumbat
- A03 batuk / selesema / sakit dada
- A04 gigitan serangga / gatal
- A05 luka kecil / bengkak
- A06 sakit gigi / gusi
- A07 bayi kembung
- A08 urutan badan / saraf
- A09 sakit kepala / migrain
- A10 kembung / senggugut

CTA style pool:
- soft trust CTA
- practical household CTA
- urgent relief CTA

Build Variant Plan first.
Every row must resolve to VIDEO + NONE.
Output required:
- batch_plan
- batch_prompt_pack
- batch_summary
```

---

## Approved Variant Plan Example

```text
═══ VARIANT PLAN — 10 SETS | BATCH TYPE: BATCH_VIDEO_FRESH | PLATFORM: TikTok |
    ENGINE: KLING_3_0 | DURATION: 10s | REFERENCE MODE: NONE ═══

SET | TASK MODE | SUBMODE | PRODUCT                   | AVATAR  | SCENE BUCKET                | ANGLE ID | ANGLE
----|-----------|---------|---------------------------|---------|-----------------------------|----------|-------------------------------
1   | VIDEO     | NONE    | Minyak Warisan Cap Burung | SARA    | calm studio explainer       | A01      | stres & aroma terapi
2   | VIDEO     | NONE    | Minyak Warisan Cap Burung | SARA    | bedside relief context      | A02      | resdung / hidung tersumbat
3   | VIDEO     | NONE    | Minyak Warisan Cap Burung | MAK_TOK | family medicine corner      | A03      | batuk / selesema / sakit dada
4   | VIDEO     | NONE    | Minyak Warisan Cap Burung | BELLA   | travel-ready emergency      | A04      | gigitan serangga / gatal
5   | VIDEO     | NONE    | Minyak Warisan Cap Burung | AZMAN   | active home first-aid       | A05      | luka kecil / bengkak
6   | VIDEO     | NONE    | Minyak Warisan Cap Burung | AZMAN   | quiet home relief close-up  | A06      | sakit gigi / gusi
7   | VIDEO     | NONE    | Minyak Warisan Cap Burung | MAK_TOK | baby-care comfort setup     | A07      | bayi kembung
8   | VIDEO     | NONE    | Minyak Warisan Cap Burung | AZMAN   | shoulder / body relief      | A08      | urutan badan / saraf
9   | VIDEO     | NONE    | Minyak Warisan Cap Burung | SARA    | office-to-home stress carry | A09      | sakit kepala / migrain
10  | VIDEO     | NONE    | Minyak Warisan Cap Burung | JULIA   | women comfort room context  | A10      | kembung / senggugut
```

---

## Row Expansion Rule

Every row above must expand into:
- `VIDEO + NONE`

This means every generated prompt must include:
- avatar lock for that row
- exact product truth lock
- `KLING_3_0` engine lock
- `10s` duration lock
- Malay spoken-dialogue lane
- fresh video logic from zero
- no dependency on `source_image_handoff`

No row may drift into:
- `IMAGE_REFERENCE`
- `VIDEO_REFERENCE`
- `BOSMAX_IMAGE_HANDOFF`
- multi-block logic
- generic Mode C continuation logic

---

## Prompt-Pack Target Shape

For this example, the final batch output should contain:

### `batch_plan`
- the exact 10 approved rows

### `batch_prompt_pack`
- 10 final fresh-video prompts
- each one labeled by `job_id` or `set number`
- each one carrying the same product truth and exact scale anchor
- each one carrying `KLING_3_0` and `10s` as locked runtime fields
- each one carrying `dialogue_authority_resolved` from the selected angle ID

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

Why this is the second benchmark:
- same stable product truth as the first image benchmark
- easy comparison between poster lane and fresh-video lane
- single engine and single duration
- no multi-block ambiguity
- no reference-media ambiguity

Companion mixed benchmark now available:
- `BOSMAX_BATCH_RUN_EXAMPLE_MIXED_DETERMINISTIC_MINYAK_WARISAN_CAP_BURUNG_v1.md`
- same product
- `BATCH_MIXED_DETERMINISTIC`
- `10` outputs
- `5 × IMAGE + VIDEO_SUPPORT`
- `5 × VIDEO + NONE`

---

## Final Rule

If anything in this example conflicts with:
- `products/CAP_BURUNG_MINYAK.yaml`
- `BOSMAX_DETERMINISTIC_FLOW_v1.md`
- `BOSMAX_BATCH_LANE_v1.md`

those authority layers win.
