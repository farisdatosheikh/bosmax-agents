# BOSMAX Input Helper v1
# Date: 2026-06-02
# Status: Front-door operator helper authority

## Purpose

This file is the BOSMAX front-door helper layer for operators who do not want
to guess BOSMAX fields manually.

Use this helper before:
- any ignition prompt
- any repair prompt
- any variation prompt
- any batch intake block

This file is not the product registry.
This file is the operator-facing field guide that normalizes valid values.

---

## Core Rule

Always decide these items in order:
1. `known product` or `unknown product`
2. `task_mode`
3. `task branch`
4. `platform`
5. `engine` if video
6. `duration` if video
7. `scale anchor`

If the product is already known, use registry truth.
Do not freestyle the scale anchor for known TikTok products.

---

## Product Status Helper

### Known direct products
- `Minyak Warisan Cap Burung`
- `Minyak Jungle Girl`

### Known sensitive products
- `BOSMAX Serum`
- `BOSMAX Herbs`
- `Maverix Maxoil`

### Unknown product
If the product is not in BOSMAX registry yet:
- use temporary category wording
- use a temporary scale anchor
- keep the first run deterministic
- register the product afterwards if the lane is worth keeping

---

## Canonical Task Fields

### Universal
- `task_mode`: `IMAGE` | `VIDEO`
- `product_name`
- `variant`
- `platform`
- `language`
- `avatar_image`
- `product_image`

### IMAGE-only
- `image_goal`: `VIDEO_SUPPORT` | `SELLING_POSTER`

### VIDEO-only
- `video_engine`
- `duration_target`
- `reference_mode`: `NONE` | `IMAGE_REFERENCE` | `VIDEO_REFERENCE` | `BOSMAX_IMAGE_HANDOFF`
- `product_info_simple`
- `copywriting_id` when using repo-approved copy
- `copywriting_mode`: `AUTO_RESOLVE`
- `avatar_context_id` for fixed avatar package runs
- `avatar_pool_id` for batch avatar rotation runs
- `avatar_mode`: `AUTO_RESOLVE` | `AUTO_ROTATE`
- `batch_count` for rotation runs
- `rotation_rule`: `ROUND_ROBIN_NO_REPEAT`

### Optional
- `scene_preference`
- `formula_preference`
- `copy_style_preference`
- `cta_style_preference`

---

## Platform Helper

| Field | Valid values | Notes |
|---|---|---|
| `platform` | `TikTok` | default commercial priority |
| `platform` | `Shopee` | listing / poster friendly |
| `platform` | `Lazada` | listing / poster friendly |
| `platform` | `Meta` | ads / feed / lifestyle |
| `platform` | `YouTube Shorts` | video-first |

If the platform is `TikTok`, keep the scale anchor literal.

---

## Category Helper

This is an operator helper only.
Known products should still follow registry category truth.

| Use case | Safe category wording |
|---|---|
| direct minyak angin / traditional remedy | `Health & Wellness / Traditional Remedy` |
| sensitive male oil / confidence lane | `Health & Wellness / Men's Health` |
| sensitive female care | `Health & Wellness / Women's Health` |
| cosmetic / serum / beauty | `Beauty & Personal Care` |
| herbal ingredient story | `Health & Wellness / Herbal Care` |

If unsure, choose the broadest honest category first.

---

## Known Variants And Scale Anchors

### Direct products

| Product | Variant | Scale anchor |
|---|---|---|
| `Minyak Warisan Cap Burung` | `30ml WG40 Glass Bottle` | `EXACTLY a small pocket-size 30ml rectangular clear glass medicated oil bottle with a red ribbed cap, shorter than the palm and only two fingers wide` |
| `Minyak Jungle Girl` | `30ml Massage Oil JG01` | `EXACTLY a compact 30ml massage oil bottle size, naturally hand-sized` |

### Sensitive products

| Product | Variant | Scale anchor |
|---|---|---|
| `BOSMAX Serum` | `5ml Travel Size` | `EXACTLY lip balm size, fit into fingers naturally` |
| `BOSMAX Serum` | `10ml Standard Size` | `EXACTLY chapstick size, fit into fingers naturally` |
| `Maverix Maxoil` | `Limited Premium Set (5 Bottles)` | `EXACTLY lip balm size per bottle, fit into fingers naturally, sold as a 5-bottle set` |

For known products, do not rewrite these anchors into vague wording.

---

## Image Engine Helper

### BOSMAX canonical image engines

| Operator wording | BOSMAX canonical value | Status |
|---|---|---|
| `Nano banana pro` | `NANO_BANANA_PRO` | live |
| `Imagen 3` | `IMAGEN_3` | live |

### External operator labels that are not current canonical repo IDs

| Operator wording | Current handling |
|---|---|
| `Nano banana 2` | not a canonical BOSMAX engine id yet; normalize manually before use |
| `ChatGPT image 2.0` | external provider wording, not a BOSMAX canonical engine id |
| `Grok imagine photo` | external provider wording, not a BOSMAX canonical image engine id |

If a provider label is not in the BOSMAX engine table, normalize it before
building prompts. Do not write mixed unofficial engine names into authority
templates.

---

## Video Engine Helper

| BOSMAX engine | Allowed durations | Notes |
|---|---|---|
| `VEO_3_1_LITE` | `8s` per block | multi-block if target exceeds 8s |
| `VEO_3_1` | `8,16,24,32,40,48,56s` | long-form supported |
| `KLING_3_0` | `5,10,15s` | stable benchmark lane |
| `SEEDANCE_2_0` | `5,10,15s` | fixed block math |
| `GROK` | `6s` or `10s` per block | user must confirm block distribution if multi-block |
| `GOOGLE_FLOW` | up to `60s` | use content mode specific logic |

### Google Flow content-mode helper

| Need | BOSMAX content mode | Reminder |
|---|---|---|
| fresh text-to-video | `T2V` | no image anchor required |
| two-image anchor route | `FRAMES` | requires 2 images |
| three-image anchor route | `INGREDIENTS` | requires 3 images |

### Grok helper

`GROK` is the canonical BOSMAX engine id.
If the operator says:
- `Grok Imagine`
- `Grok Imagine agent mode`

normalize the provider wording first, then still decide the BOSMAX front-door
mode:
- `VIDEO + NONE`
- `VIDEO + IMAGE_REFERENCE`
- `VIDEO + VIDEO_REFERENCE`

There is no separate canonical repo engine id for `Grok agent mode` right now.

---

## Front-Door Route Helper

### IMAGE

| User intent | Use |
|---|---|
| clean still image for later video | `IMAGE + VIDEO_SUPPORT` |
| commercial poster with hierarchy | `IMAGE + SELLING_POSTER` |

### VIDEO

| User intent | Use |
|---|---|
| fresh prompt from avatar + product | `VIDEO + NONE` |
| rebuild from uploaded image | `VIDEO + IMAGE_REFERENCE` |
| rebuild from uploaded video / frames | `VIDEO + VIDEO_REFERENCE` |
| continue from BOSMAX image handoff | `VIDEO + BOSMAX_IMAGE_HANDOFF` |

Hard rule:
- generic uploaded image reference is not Mode C
- true Mode C requires BOSMAX `source_image_handoff`

---

## Minimal Fill Checklists

### Registered resolver single-avatar run

- `product_name`
- `variant`
- `platform`
- `language`
- `video_engine`
- `duration_target`
- `copywriting_id`
- `copywriting_mode = AUTO_RESOLVE`
- `avatar_context_id`
- `avatar_mode = AUTO_RESOLVE`
- `camera_style`
- `physics_class`

This is now the default beginner flow:
- `COMMAND_CENTRE_PLUG_AND_PLAY`

### Registered resolver batch run

- `product_name`
- `variant`
- `platform`
- `language`
- `video_engine`
- `duration_target`
- `copywriting_id`
- `copywriting_mode = AUTO_RESOLVE`
- `avatar_pool_id`
- `avatar_mode = AUTO_ROTATE`
- `batch_count`
- `rotation_rule = ROUND_ROBIN_NO_REPEAT`
- `camera_style`
- `physics_class`

### Legacy manual run

Only use for:
- trusted expert operator
- review-only exception

Label:
- `LEGACY_EXPERT_MODE`
- `MANUAL_OVERRIDE_REVIEW_ONLY`

If manual Hook / USP / CTA / Avatar / Mannequin / Wardrobe / Scene fields are edited:
- mark `Needs Compliance Review`

### IMAGE checklist
- product name
- variant
- platform
- language
- image goal
- avatar image
- product image
- exact scale anchor

### VIDEO checklist
- product name
- variant
- platform
- language
- video engine
- duration target
- reference mode
- avatar image
- product image
- exact scale anchor

### Sensitive-product extra checklist
- compliance stays stealth-safe
- dialogue authority must come from registry / script library
- do not freestyle explicit anatomy language

---

## Final Operator Law

Use this helper to fill fields.
Use `BOSMAX_IGNITION_WORKFLOW_v1.md` to build the actual request prompt.

Do not jump straight from product image to freestyle prompt writing when the
product is already known in BOSMAX registry.
