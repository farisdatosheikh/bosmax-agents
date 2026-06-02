# BOSMAX Ignition Workflow v1
# Date: 2026-06-02
# Status: Front-door ignition authority

## Purpose

This file defines the BOSMAX front-door ignition workflow for operators.

The workflow has three steps only:
1. `IGNITION`
2. `REPAIR`
3. `VARIATION`

Use `BOSMAX_INPUT_HELPER_v1.md` first before filling any template in this file.

---

## Workflow Law

### Step 1 — IGNITION
Use this when starting from zero.

### Step 2 — REPAIR
Use this when the first output is close but still wrong.

### Step 3 — VARIATION
Use this when the first output is approved and you want controlled alternatives.

If the operator already wants many outputs, move to:
- `BOSMAX_BATCH_TEMPLATE_SET_v1.md`
- `BOSMAX_BATCH_LANE_v1.md`

---

## Template 1 — IMAGE IGNITION

Use for:
- `IMAGE + VIDEO_SUPPORT`
- `IMAGE + SELLING_POSTER`

```text
You are operating inside BOSMAX deterministic image flow.

Use BOSMAX product truth first.
Use uploaded avatar and product images as identity and product locks.

Task mode: IMAGE
Image goal: [VIDEO_SUPPORT or SELLING_POSTER]
Platform: [TikTok / Shopee / Lazada / Meta]
Language: [Malay / English]

Product name: [PRODUCT NAME]
Variant: [VARIANT]
Category: [CATEGORY]
Scale anchor: [EXACT SCALE ANCHOR]

Avatar input:
- [SHORT AVATAR DESCRIPTION OR "uploaded avatar image"]

Product input:
- [SHORT PRODUCT DESCRIPTION OR "uploaded product image"]

Scene preference:
- [SCENE OR BLANK]

Copy style preference:
- [SOFT / DIRECT / PREMIUM / TRUST / HERITAGE]

Required output:
1. Resolve the correct BOSMAX deterministic branch.
2. Build one final image prompt only.
3. Preserve product truth and exact scale anchor literally.
4. Return product truth lock, avatar truth lock, and negative lock block.
5. If image_goal = VIDEO_SUPPORT, keep the prompt continuity-friendly for later video generation.
6. If image_goal = SELLING_POSTER, embed selling hierarchy cleanly without turning the prompt into clutter.
```

---

## Template 2 — VIDEO IGNITION

Use for:
- `VIDEO + NONE`
- `VIDEO + IMAGE_REFERENCE`
- `VIDEO + VIDEO_REFERENCE`
- `VIDEO + BOSMAX_IMAGE_HANDOFF`

```text
You are operating inside BOSMAX deterministic video flow.

Use BOSMAX product truth first.
Resolve dialogue authority before script generation.

Task mode: VIDEO
Reference mode: [NONE / IMAGE_REFERENCE / VIDEO_REFERENCE / BOSMAX_IMAGE_HANDOFF]
Platform: [TikTok / Shopee / Lazada / Meta / YouTube Shorts]
Language: [Malay / English]

Product name: [PRODUCT NAME]
Variant: [VARIANT]
Category: [CATEGORY]
Scale anchor: [EXACT SCALE ANCHOR]

Video engine: [VEO_3_1_LITE / VEO_3_1 / KLING_3_0 / SEEDANCE_2_0 / GROK / GOOGLE_FLOW]
Duration target: [VALID DURATION]

Avatar input:
- [SHORT AVATAR DESCRIPTION OR "uploaded avatar image"]

Product input:
- [SHORT PRODUCT DESCRIPTION OR "uploaded product image"]

Product info simple:
- [SHORT BENEFIT OR PRODUCT CONTEXT]

Scene preference:
- [SCENE OR BLANK]

Formula preference:
- [PAS / HSO / AIDA / FAB / SAVAGE_HPAS OR BLANK]

Required output:
1. Resolve the correct BOSMAX deterministic branch.
2. Validate engine and duration against BOSMAX rules.
3. If the product is sensitive, resolve dialogue authority from the script registry layer first.
4. Build one final video prompt or a multi-block plan if duration requires it.
5. Return engine id, duration target, block plan, product truth lock, and dialogue authority summary.
```

---

## Template 3 — GOOGLE FLOW IGNITION OVERLAY

Use this only when `video_engine = GOOGLE_FLOW`.

```text
Google Flow content mode: [T2V / FRAMES / INGREDIENTS]

If T2V:
- build a Google Flow text-to-video prompt

If FRAMES:
- confirm 2 images are available

If INGREDIENTS:
- confirm 3 images are available

Google Flow requirement:
- keep BOSMAX product truth stable across the whole sequence
- preserve the exact scale anchor
- declare image-guidance logic only if the route truly needs it
- do not collapse Flow-specific structure into generic 9-section output
```

---

## Template 4 — GROK IGNITION OVERLAY

Use this only when `video_engine = GROK`.

```text
GROK rule:
- valid base durations are 6s or 10s per block
- if target duration is above 10s, resolve block distribution first
- do not assume the block split

If total target needs multiple blocks:
- present the distribution
- build the master narrative brief first
- only then generate the block prompts
```

---

## Template 5 — REPAIR TEMPLATE

Use after one draft already exists but still has errors.

```text
Repair the previous BOSMAX output without changing the task mode or product truth.

Current task mode: [IMAGE or VIDEO]
Current branch: [IMAGE + VIDEO_SUPPORT / IMAGE + SELLING_POSTER / VIDEO + NONE / etc.]
Product name: [PRODUCT NAME]
Variant: [VARIANT]
Scale anchor: [EXACT SCALE ANCHOR]

Preserve these locks:
- avatar identity
- product truth
- exact scale anchor
- current platform and language

Problems to repair:
- [ISSUE 1]
- [ISSUE 2]
- [ISSUE 3]

Repair rule:
1. Keep what is already correct.
2. Change only the failing parts.
3. Restate the exact product truth if scale, cap, label, or packaging drift happened.
4. If the product is sensitive, do not break stealth dialogue compliance.
5. Return one repaired final prompt only.
```

---

## Template 6 — VARIATION TEMPLATE

Use only after the base output is already approved.

```text
Create controlled BOSMAX variations from the approved base output.

Base task mode: [IMAGE or VIDEO]
Base branch: [DETERMINISTIC BRANCH]
Product name: [PRODUCT NAME]
Variant: [VARIANT]
Scale anchor: [EXACT SCALE ANCHOR]

Keep fixed:
- avatar identity
- product truth
- exact scale anchor
- platform
- language
- compliance class

Allowed variation axis:
- [scene]
- [camera]
- [copy angle]
- [CTA tone]
- [lighting]

Variation count:
- [3 / 5 / 10]

Rule:
- do not change the product geometry
- do not change the scale anchor
- do not drift into a different compliance lane
- do not redesign known packaging
- return clearly separated variations
```

---

## Template 7 — MINI-BATCH VARIATION BRIDGE

Use this when the operator wants a few controlled alternatives but does not
need the full batch lane yet.

```text
Use the approved ignition output as the base.
Generate [3 / 5] controlled variations only.
Do not open full batch planning.
Keep product truth and scale anchor fixed.
Only rotate the approved variation axes.
```

---

## Final Rule

`BOSMAX_INPUT_HELPER_v1.md` tells the operator what to fill.

This file tells the operator how to ask BOSMAX:
- first ignition
- then repair
- then variation

If the operator jumps straight to large-volume generation, move to the batch
lane instead of stretching ignition prompts beyond their purpose.
