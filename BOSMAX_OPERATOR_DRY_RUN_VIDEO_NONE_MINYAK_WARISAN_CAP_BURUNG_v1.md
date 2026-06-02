# BOSMAX Operator Dry Run v1
# Product: Minyak Warisan Cap Burung
# Route: VIDEO + NONE
# Date: 2026-06-02
# Status: Front-door operator walkthrough

## Purpose

This file is the second real operator dry run for the BOSMAX front-door
workflow:
- `Input Helper`
- `Ignition`
- `Repair`
- `Variation`

This time the walkthrough proves the simplest fresh-video lane on a known
direct product.

The goal is not batch generation.
The goal is to prove that one operator can move through the direct-product
video lane without guessing engine, duration, reference mode, or scale anchor.

---

## Dry-Run Choice

### Product
- `Minyak Warisan Cap Burung`

### Why this product
- known direct product
- exact variant already locked
- exact scale anchor already locked
- no stealth-dialogue complication
- suitable for first direct-product video onboarding test

### Branch chosen
- `VIDEO + NONE`

### Why this branch
- cleanest possible fresh-video route
- no reference-media ambiguity
- no Mode C handoff requirement
- no multi-block math

### Engine chosen
- `KLING_3_0`

### Duration chosen
- `10s`

### Why this engine-duration pair
- valid in current BOSMAX engine table
- already used in the existing direct-product batch benchmark
- enough room for one hook, one benefit, and one CTA without forcing block split

---

## Step 1 — Input Helper Fill

The operator should fill the fields by reading `BOSMAX_INPUT_HELPER_v1.md`.

### Chosen values

| Field | Dry-run value |
|---|---|
| `task_mode` | `VIDEO` |
| `reference_mode` | `NONE` |
| `product_name` | `Minyak Warisan Cap Burung` |
| `variant` | `30ml WG40 Glass Bottle` |
| `platform` | `TikTok` |
| `language` | `Malay` |
| `category` | `Health & Wellness / Traditional Remedy` |
| `scale_anchor` | `EXACTLY a compact 30ml oblong clear glass medicated oil bottle with a red cap, naturally hand-sized` |
| `video_engine` | `KLING_3_0` |
| `duration_target` | `10s` |
| `avatar_image` | uploaded female lifestyle avatar |
| `product_image` | uploaded product packshot |
| `product_info_simple` | minyak angin warisan keluarga untuk pening kepala, resdung, dan kegunaan harian |
| `scene_preference` | home shelf to in-hand demonstration |
| `formula_preference` | `PAS` |

### Operator check

This dry run is valid because:
- product is known
- variant is known
- scale anchor is exact
- engine is valid
- duration is valid
- no reference mode ambiguity exists

---

## Step 2 — Ignition Prompt

The operator now uses `BOSMAX_IGNITION_WORKFLOW_v1.md`.

### Final filled ignition prompt

```text
You are operating inside BOSMAX deterministic video flow.

Use BOSMAX product truth first.
Resolve dialogue authority before script generation.

Task mode: VIDEO
Reference mode: NONE
Platform: TikTok
Language: Malay

Product name: Minyak Warisan Cap Burung
Variant: 30ml WG40 Glass Bottle
Category: Health & Wellness / Traditional Remedy
Scale anchor: EXACTLY a compact 30ml oblong clear glass medicated oil bottle with a red cap, naturally hand-sized

Video engine: KLING_3_0
Duration target: 10s

Avatar input:
- uploaded female lifestyle avatar

Product input:
- uploaded Minyak Warisan Cap Burung product image

Product info simple:
- minyak angin warisan keluarga untuk pening kepala, resdung, dan kegunaan harian

Scene preference:
- home shelf to in-hand demonstration

Formula preference:
- PAS

Required output:
1. Resolve the correct BOSMAX deterministic branch.
2. Validate engine and duration against BOSMAX rules.
3. Build one final video prompt only.
4. Return engine id, duration target, block plan, and product truth lock.
5. Preserve direct-product truth and exact scale anchor literally.
```

### Expected BOSMAX path

- `VIDEO + NONE`
- known direct product
- no reference analysis required
- no multi-block required
- video prompt assembly through fresh video lane

---

## Step 3 — Example Repair Trigger

Assume the first output is almost correct but still has these issues:
- product appears too late in the sequence
- dialogue feels slightly too generic
- the product scale reads fine, but the bottle visibility is too brief

### Filled repair prompt

```text
Repair the previous BOSMAX output without changing the task mode or product truth.

Current task mode: VIDEO
Current branch: VIDEO + NONE
Product name: Minyak Warisan Cap Burung
Variant: 30ml WG40 Glass Bottle
Scale anchor: EXACTLY a compact 30ml oblong clear glass medicated oil bottle with a red cap, naturally hand-sized

Preserve these locks:
- avatar identity
- product truth
- exact scale anchor
- current platform and language

Problems to repair:
- product appears too late in the sequence
- dialogue is slightly too generic
- bottle visibility should be clearer without changing the exact geometry

Repair rule:
1. Keep what is already correct.
2. Change only the failing parts.
3. Restate the exact product truth if scale, cap, label, or packaging drift happened.
4. Keep the video within the same engine and duration.
5. Return one repaired final prompt only.
```

### What this repair is proving

The operator does not need to rebuild the whole video request.
The operator only:
- keeps the branch fixed
- keeps the engine fixed
- keeps the duration fixed
- keeps the product fixed
- declares the weak points precisely

---

## Step 4 — Variation Prompt

Assume the repaired video prompt is now approved.
The operator wants three controlled variations without changing product truth.

### Filled variation prompt

```text
Create controlled BOSMAX variations from the approved base output.

Base task mode: VIDEO
Base branch: VIDEO + NONE
Product name: Minyak Warisan Cap Burung
Variant: 30ml WG40 Glass Bottle
Scale anchor: EXACTLY a compact 30ml oblong clear glass medicated oil bottle with a red cap, naturally hand-sized

Keep fixed:
- avatar identity
- product truth
- exact scale anchor
- platform
- language
- engine
- duration
- compliance class

Allowed variation axis:
- scene
- camera
- copy angle
- CTA tone

Variation count:
- 3

Rule:
- do not change the product geometry
- do not change the scale anchor
- do not switch engine or duration
- do not redesign known packaging
- return clearly separated variations
```

### Controlled variation examples

Variation A:
- home shelf intro
- trust-first dialogue

Variation B:
- in-hand demonstration
- benefit-first dialogue

Variation C:
- bedside / daily-carry setup
- heritage-first dialogue

---

## What This Dry Run Proves

### Proven
- the operator can normalize video fields without guessing
- the operator can choose a valid engine and duration cleanly
- the operator can launch the first fresh-video request with one structured ignition prompt
- the operator can repair without reopening reference-mode ambiguity
- the operator can ask for controlled variations while keeping engine and duration fixed

### Not proven by this dry run
- multi-block video math
- Google Flow FRAMES / INGREDIENTS logic
- Mode C handoff continuation
- sensitive dialogue authority behavior
- batch dispatcher behavior

Those should be tested in separate dry runs.

---

## Recommended Next Dry Runs

1. `IMAGE + SELLING_POSTER` for `Maverix Maxoil`
2. `VIDEO + NONE` for `Maverix Maxoil`
3. `VIDEO + NONE` for `BOSMAX Serum`
4. `VIDEO + IMAGE_REFERENCE` on a known direct product

---

## Final Law

If this dry run feels natural to the operator, the direct-product video lane is
working.

If operators still hesitate at:
- engine choice
- duration choice
- reference mode choice
- scale anchor choice

then the helper or ignition layer must be tightened before pushing them toward
more advanced routes.
