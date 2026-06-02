# BOSMAX Operator Dry Run v1
# Product: BOSMAX Serum
# Variant: 10ML
# Route: VIDEO + NONE
# Date: 2026-06-02
# Status: 10ML companion sensitive operator walkthrough

## Purpose

This file is the first `10ML` companion operator dry run for the BOSMAX
front-door workflow:
- `Input Helper`
- `Ignition`
- `Repair`
- `Variation`

This walkthrough proves that the taller standard-size BOSMAX Serum variant can
move through the same flagship sensitive lane without collapsing back into the
`5ML` silhouette.

The goal is not batch generation.
The goal is to prove that one operator can move through the `10ML` sensitive
fresh-video lane without guessing engine, duration, dialogue authority, or
scale anchor.

---

## Dry-Run Choice

### Product
- `BOSMAX Serum`

### Variant
- `10ML`

### Why this variant
- companion size to the hardened `5ML` flagship lane
- taller bottle read requires separate lock
- chapstick-size scale needs its own deterministic proof

### Branch chosen
- `VIDEO + NONE`

### Engine chosen
- `KLING_3_0`

### Duration chosen
- `10s`

### Why this engine-duration pair
- valid in current BOSMAX engine table
- already stable for the house sensitive lane
- enough room for one stealth hook, one confidence angle, and one CTA without forcing block split

---

## Step 1 — Input Helper Fill

The operator should fill the fields by reading `BOSMAX_INPUT_HELPER_v1.md`.

### Chosen values

| Field | Dry-run value |
|---|---|
| `task_mode` | `VIDEO` |
| `reference_mode` | `NONE` |
| `product_name` | `BOSMAX Serum` |
| `variant` | `10ML` |
| `platform` | `TikTok` |
| `language` | `Malay` |
| `category` | `Health & Wellness / Men's Health` |
| `scale_anchor` | `EXACTLY chapstick size, fit into fingers naturally` |
| `video_engine` | `KLING_3_0` |
| `duration_target` | `10s` |
| `avatar_image` | uploaded confident male lifestyle avatar |
| `product_image` | uploaded BOSMAX 10ML reference product image |
| `product_info_simple` | minyak roll-on lelaki standard size untuk rutin peribadi dan keyakinan, guna gaya stealth tanpa wording eksplisit |
| `scene_preference` | shelf intro to in-hand close demonstration |
| `formula_preference` | `PAS` |

### Operator check

This dry run is valid because:
- product is known
- variant is known
- scale anchor is exact
- engine is valid
- duration is valid
- stealth dialogue authority is known
- no reference mode ambiguity exists

---

## Step 2 — Ignition Prompt

### Final filled ignition prompt

```text
You are operating inside BOSMAX deterministic video flow.

Use BOSMAX product truth first.
Resolve dialogue authority before script generation.

Task mode: VIDEO
Reference mode: NONE
Platform: TikTok
Language: Malay

Product name: BOSMAX Serum
Variant: 10ML
Category: Health & Wellness / Men's Health
Scale anchor: EXACTLY chapstick size, fit into fingers naturally

Video engine: KLING_3_0
Duration target: 10s

Dialogue authority:
- mode: SCRIPT_REGISTRY
- silo: male_health_stealth_01
- variant family: EGO_01

Avatar input:
- uploaded confident male lifestyle avatar

Product input:
- uploaded BOSMAX 10ML product image for product-truth reference only

Product info simple:
- minyak roll-on lelaki standard size untuk rutin peribadi dan keyakinan
- gunakan stealth metaphor, bukan wording eksplisit

Scene preference:
- shelf intro to in-hand close demonstration

Formula preference:
- PAS

Required output:
1. Resolve the correct BOSMAX deterministic branch.
2. Validate engine and duration against BOSMAX rules.
3. Resolve dialogue authority from script registry.
4. Build one final video prompt only.
5. Return engine id, duration target, block plan, dialogue authority resolved, and product truth lock.
6. Preserve exact scale anchor literally.
```

### Expected BOSMAX path

- `VIDEO + NONE`
- known sensitive product
- no reference analysis required
- no multi-block required
- dialogue resolved through `SCRIPT_REGISTRY_UNIFIED.md` + `SCRIPT_VARIANT_LIBRARY.md`
- video prompt assembly through fresh sensitive video lane

---

## Step 3 — Example Repair Trigger

Assume the first output is almost correct but still has these issues:
- bottle reads too short and starts collapsing back toward the `5ML` silhouette
- dialogue sounds too flat
- branding readability is not strong enough in the hero beat

### Filled repair prompt

```text
Repair the previous BOSMAX output without changing the task mode or product truth.

Current task mode: VIDEO
Current branch: VIDEO + NONE
Product name: BOSMAX Serum
Variant: 10ML
Scale anchor: EXACTLY chapstick size, fit into fingers naturally

Preserve these locks:
- avatar identity
- product truth
- exact scale anchor
- script-registry dialogue authority
- current platform and language

Problems to repair:
- bottle reads too short and drifts toward the 5ML silhouette
- dialogue needs stronger stealth authority
- BOSMAX branding readability should improve in the hero beat

Repair rule:
1. Keep what is already correct.
2. Change only the failing parts.
3. Restate the exact product truth if scale, cap, label, or packaging drift happened.
4. Keep the video within the same engine and duration.
5. Return one repaired final prompt only.
```

---

## Step 4 — Variation Prompt

Assume the repaired video prompt is now approved.
The operator wants three controlled variations without changing product truth.

### Filled variation prompt

```text
Create controlled BOSMAX variations from the approved base output.

Base task mode: VIDEO
Base branch: VIDEO + NONE
Product name: BOSMAX Serum
Variant: 10ML
Scale anchor: EXACTLY chapstick size, fit into fingers naturally

Keep fixed:
- avatar identity
- product truth
- exact scale anchor
- platform
- language
- engine
- duration
- dialogue authority
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
- do not break stealth dialogue rules
- return clearly separated variations
```

### Controlled variation examples

Variation A:
- shelf intro
- routine-first dialogue

Variation B:
- in-hand close demonstration
- benefit-first dialogue

Variation C:
- premium dark close-up
- authority-first CTA

---

## What This Dry Run Proves

### Proven
- the operator can normalize `10ML` sensitive video fields without guessing
- the operator can keep `10ML` separate from the `5ML` silhouette
- the operator can launch a companion fresh-video request with one structured ignition prompt
- the operator can repair size drift without reopening route ambiguity
- the operator can ask for controlled variations while keeping engine, duration, and stealth authority fixed

### Not proven by this dry run
- multi-block video math
- Google Flow FRAMES / INGREDIENTS logic
- Mode C handoff continuation
- batch dispatcher behavior

Those should be tested in separate dry runs.

---

## Final Law

If this dry run feels natural to the operator, the `10ML` companion sensitive
fresh-video lane is working.

If operators still hesitate at:
- engine choice
- duration choice
- dialogue authority handling
- scale anchor choice

then the helper or ignition layer must be tightened before pushing them toward
more advanced sensitive routes.
