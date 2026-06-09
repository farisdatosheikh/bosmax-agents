# BOSMAX Video Render Format Guardrail v1

```yaml
Authority: BOSMAX video prompt runtime guardrail
Status: CANONICAL
Date: 2026-06-10
Applies To:
  - GROK video prompts
  - GOOGLE_FLOW.FLOW_EXTEND_UI prompts
  - image-to-video starter prompts
  - ready-frame animation prompts
  - product hero motion prompts
  - compact-carry / tray / pouch / handling proof prompts
```

## 1. Purpose

This guardrail prevents rendered video format and composition defects observed during BOSMAX testing:

- square 1:1 output when TikTok Shop vertical video was intended
- landscape or non-phone framing for TikTok Shop Malaysia assets
- secondary props becoming too dominant
- branded or distracting props interfering with product trust
- final frame ending without a stable product-visible close-up
- label readability lost because the product is not kept as the hero object

This document controls render-format wording. It does not change engine duration math, source-mode routing, product truth, copywriting authority, or motion occlusion law.

## 2. Universal Render Format Rule

All BOSMAX video prompts for TikTok Shop Malaysia must request:

```yaml
vertical_format: REQUIRED
aspect_ratio: 9:16
phone_format: full-screen TikTok Shop Malaysia mobile video
square_1_1_output: BLOCKED
landscape_output: BLOCKED
```

Required visible prompt wording:

```text
Create a vertical 9:16 TikTok Shop Malaysia video, full-screen phone format, not square, not 1:1.
```

## 3. Product Priority Rule

The product must remain the hero and first-read object.

```yaml
product_priority: product remains hero and first-read object
label_visibility: preserve readable label whenever possible
final_frame: stable product-visible close-up when the route includes CTA, product hero motion, image-to-video starter, ready frame continuation, compact-carry proof, or handling proof
```

Reject or repair if:

- prop becomes bigger than product without reason
- label is hidden by hand/prop for the core proof moment
- final second ends on pouch/tray/hand instead of product visibility
- product becomes background decoration

## 4. Secondary Prop Rule

Props such as pouch, tray, towel, drawer, shelf, bag, fabric, bedside item, grooming item, or nursery item must remain:

```yaml
secondary_props:
  scale: small / controlled
  branding: unbranded
  visual_priority: secondary
  purpose: support product scale, storage, routine, or trust cue only
```

Blocked unless explicitly required by the operator:

- branded pouch / branded bag / visible third-party logo
- prop covering product label
- prop becoming the CTA object
- prop dominating the frame
- prop implying medical proof, fake certification, or unrelated claim

## 5. Text Overlay Rule

Default:

```yaml
text_overlay: none unless the selected template explicitly requests overlay text
```

If overlay text is requested, it must not cover:

- product label
- hand/product scale proof
- face/identity cue if avatar is active
- final CTA button area if platform UI is expected

## 6. Engine-Specific Prompt Guidance

### GROK

All final GROK prompts must include:

```text
Create a vertical 9:16 TikTok Shop Malaysia UGC video, full-screen phone format, not square, not 1:1.
```

For prop scenes:

```text
Keep the pouch/tray/towel/drawer/shelf/bag/fabric small, neutral, unbranded, and secondary. The product remains the hero and the video ends on a stable product-visible close-up.
```

### GOOGLE_FLOW.FLOW_EXTEND_UI

All final Google Flow prompts must include:

```text
Vertical 9:16 TikTok Shop Malaysia mobile video, full-screen phone format, not square, not 1:1.
```

For still-image / ready-frame prompts:

```text
Preserve the product as the first-read object while animating the frame. Keep props secondary and unbranded. End on a stable product-visible close-up when the route is CTA, product hero, image-to-Flow starter, or handling proof.
```

## 7. Relation To Motion Occlusion Guardrail

Use this document together with:

```yaml
motion_guardrail: docs/video_motion_occlusion_guardrail_v1.md
```

Division of responsibility:

```yaml
video_render_format_guardrail_v1:
  controls:
    - vertical 9:16 format
    - not square / not 1:1
    - product hero composition
    - secondary unbranded props
    - stable product-visible final frame

video_motion_occlusion_guardrail_v1:
  controls:
    - first-frame hand/product anchor
    - product flash prevention
    - no standalone opening packshot
    - no full occlusion
    - no hide-and-retrieve
    - 70% product visibility during compact-carry proof
```

## 8. Validation Checklist

A prompt passes this guardrail when:

```yaml
vertical_9_16: PASS
not_square_1_1: BLOCKED
full_screen_phone_format: PASS
product_hero: PASS
secondary_props_unbranded: PASS
prop_not_dominant: PASS
stable_product_visible_close: PASS
label_visibility_prioritised: PASS
text_overlay_policy: PASS
```

## 9. Failure Handling

If a render returns square, prop-dominant, or weak product close:

1. add `vertical 9:16, full-screen phone format, not square, not 1:1`
2. reduce prop size and brand visibility
3. force product to remain first-read hero
4. require final stable product-visible close-up
5. remove unnecessary text overlays
6. rerender with combined render-format + motion-occlusion guardrail wording

## 10. Notion Mirror Rule

Notion templates may mirror this guardrail at parent and child page level.

Required mirrors:

- `03 — Video Google Flow Templates`
- `03A — BOSMAX Serum Google Flow Templates`
- `03B — Minyak Warisan Google Flow Templates`
- `03C — On-The-Fly Product Google Flow Templates`
- `05 — Video Grok Templates`
- `05A — BOSMAX Serum Grok Templates`
- `05B — Minyak Warisan Grok Templates`
- `05C — On-The-Fly Product Grok Templates`

Do not mark a rendered output as final-ready until actual output aspect ratio and final product visibility are inspected.
