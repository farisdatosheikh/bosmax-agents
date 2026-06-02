# BOSMAX Operator Dry Run v1
# Product: Minyak Warisan Cap Burung
# Date: 2026-06-02
# Status: Front-door operator walkthrough

## Purpose

This file is the first real operator dry run for the new BOSMAX front-door
workflow:
- `Input Helper`
- `Ignition`
- `Repair`
- `Variation`

The goal is not to generate 10 outputs.
The goal is to prove that one operator can move through the new front-door
system without guessing fields manually.

---

## Dry-Run Choice

### Product
- `Minyak Warisan Cap Burung`

### Why this product
- known direct product
- exact variant already locked
- exact scale anchor already locked
- no stealth-dialogue complication
- suitable for first front-door onboarding test

### Branch chosen
- `IMAGE + SELLING_POSTER`

### Why this branch
- easy for new operators to understand
- visibly demonstrates product truth and selling hierarchy
- does not require engine duration math

---

## Step 1 — Input Helper Fill

The operator should fill the fields by reading `BOSMAX_INPUT_HELPER_v1.md`.

### Chosen values

| Field | Dry-run value |
|---|---|
| `task_mode` | `IMAGE` |
| `image_goal` | `SELLING_POSTER` |
| `product_name` | `Minyak Warisan Cap Burung` |
| `variant` | `30ml WG40 Glass Bottle` |
| `platform` | `TikTok` |
| `language` | `Malay` |
| `category` | `Health & Wellness / Traditional Remedy` |
| `scale_anchor` | `EXACTLY a small pocket-size 30ml rectangular clear glass medicated oil bottle with a red ribbed cap, shorter than the palm and only two fingers wide` |
| `avatar_image` | uploaded female lifestyle avatar |
| `product_image` | uploaded product packshot |
| `scene_preference` | warm premium Malay household shelf mood |
| `copy_style_preference` | trust + heritage |

### Operator check

This dry run is valid because:
- product is known
- variant is known
- scale anchor is exact
- platform is known
- branch is deterministic

---

## Step 2 — Ignition Prompt

The operator now uses `BOSMAX_IGNITION_WORKFLOW_v1.md`.

### Final filled ignition prompt

```text
You are operating inside BOSMAX deterministic image flow.

Use BOSMAX product truth first.
Use uploaded avatar and product images as identity and product locks.

Task mode: IMAGE
Image goal: SELLING_POSTER
Platform: TikTok
Language: Malay

Product name: Minyak Warisan Cap Burung
Variant: 30ml WG40 Glass Bottle
Category: Health & Wellness / Traditional Remedy
Scale anchor: EXACTLY a small pocket-size 30ml rectangular clear glass medicated oil bottle with a red ribbed cap, shorter than the palm and only two fingers wide

Avatar input:
- uploaded female lifestyle avatar

Product input:
- uploaded Minyak Warisan Cap Burung product image

Scene preference:
- warm premium Malay household shelf mood

Copy style preference:
- trust + heritage

Required output:
1. Resolve the correct BOSMAX deterministic branch.
2. Build one final image prompt only.
3. Preserve product truth and exact scale anchor literally.
4. Return product truth lock, avatar truth lock, and negative lock block.
5. Embed selling hierarchy cleanly without turning the prompt into clutter.
```

### Expected BOSMAX path

- `IMAGE + SELLING_POSTER`
- known direct product
- product truth from registry
- prompt assembly through image lane

---

## Step 3 — Example Repair Trigger

Assume the first output is almost correct but still has these issues:
- bottle becomes slightly oversized
- cap drifts away from the correct red cap read
- layout is premium but the product is too small relative to the avatar

### Filled repair prompt

```text
Repair the previous BOSMAX output without changing the task mode or product truth.

Current task mode: IMAGE
Current branch: IMAGE + SELLING_POSTER
Product name: Minyak Warisan Cap Burung
Variant: 30ml WG40 Glass Bottle
Scale anchor: EXACTLY a small pocket-size 30ml rectangular clear glass medicated oil bottle with a red ribbed cap, shorter than the palm and only two fingers wide

Preserve these locks:
- avatar identity
- product truth
- exact scale anchor
- current platform and language

Problems to repair:
- bottle reads slightly oversized
- cap read is drifting away from the correct red cap truth
- poster hierarchy is fine but the product should be more readable

Repair rule:
1. Keep what is already correct.
2. Change only the failing parts.
3. Restate the exact product truth if scale, cap, label, or packaging drift happened.
4. Return one repaired final prompt only.
```

### What this repair is proving

The operator does not need to rewrite the whole prompt.
The operator only:
- keeps the branch fixed
- keeps the product fixed
- declares the error
- asks BOSMAX to repair surgically

---

## Step 4 — Variation Prompt

Assume the repaired poster is now approved.
The operator wants three controlled variations without changing product truth.

### Filled variation prompt

```text
Create controlled BOSMAX variations from the approved base output.

Base task mode: IMAGE
Base branch: IMAGE + SELLING_POSTER
Product name: Minyak Warisan Cap Burung
Variant: 30ml WG40 Glass Bottle
Scale anchor: EXACTLY a compact 30ml oblong clear glass medicated oil bottle with a red cap, naturally hand-sized

Keep fixed:
- avatar identity
- product truth
- exact scale anchor
- platform
- language
- compliance class

Allowed variation axis:
- scene
- camera
- copy angle
- lighting

Variation count:
- 3

Rule:
- do not change the product geometry
- do not change the scale anchor
- do not redesign known packaging
- return clearly separated variations
```

### Controlled variation examples

Variation A:
- hero shelf composition
- heritage-forward tone

Variation B:
- in-hand lifestyle composition
- household-trust tone

Variation C:
- close product + avatar layout
- benefit-first commercial tone

---

## What This Dry Run Proves

### Proven
- the operator can normalize fields without guessing
- the operator can launch the first request with one structured ignition prompt
- the operator can repair without restarting from zero
- the operator can ask for variations without opening full batch mode

### Not proven by this dry run
- multi-block video math
- Google Flow reference routes
- sensitive dialogue authority behavior
- batch dispatcher behavior

Those should be tested in separate dry runs.

---

## Recommended Next Dry Runs

1. `VIDEO + NONE` for `Minyak Warisan Cap Burung`
2. `IMAGE + SELLING_POSTER` for `Maverix Maxoil`
3. `VIDEO + NONE` for `BOSMAX Serum` or `Maverix Maxoil`
4. `VIDEO + IMAGE_REFERENCE` on a known direct product

---

## Final Law

If this dry run feels natural to the operator, the front-door layer is working.

If operators still hesitate at:
- engine choice
- branch choice
- scale anchor choice
- product status choice

then the helper layer must be tightened before adding more templates.
