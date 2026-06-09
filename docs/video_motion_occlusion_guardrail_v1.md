# BOSMAX Video Motion Occlusion Guardrail v1

```yaml
Authority: BOSMAX video prompt runtime guardrail
Status: CANONICAL
Scope:
  - GROK single-block 6s / 10s clips
  - GROK multi-block extension clips
  - GOOGLE_FLOW.FLOW_EXTEND_UI clips
  - image-to-video starter prompts
  - small-product scale proof scenes
Date: 2026-06-10
```

## 1. Purpose

This guardrail prevents rendered video defects observed during live BOSMAX testing:

- first-second product flash before hand/action appears
- product appearing as a standalone packshot before UGC handling begins
- small product identity drift after pouch/pocket occlusion
- hide-and-retrieve motion causing object reconstruction glitch
- duplicate bottle / sudden object reappearance during compact-carry proof

This document is a prompt/runtime guardrail. It does not change engine duration math, WPS budgets, copywriting authority, product truth, or source-mode routing.

## 2. Applies When

Apply this guardrail whenever a video prompt involves:

- a small product such as BOSMAX Serum 5ML
- hand-held product demonstration
- pouch, pocket, drawer, bag, tray, or other occlusion-prone prop
- image-to-video or source-frame animation
- a 6s CTA / close where product must stay visible
- compact carry / discreet storage / scale-proof movement

## 3. First-Frame Anchor Rule

For small-product UGC, the first visible frame must already contain the intended product/action pose.

Use:

```text
The first visible frame already shows the presenter hand holding the product near camera.
```

Do not use an opening motion that lets the model create a separate packshot first.

Reject or repair if the prompt allows:

- standalone product-only flash before the hand appears
- sudden object appearance
- duplicate product at the start
- product reference interpreted as an opening shot instead of product truth

Recommended wording:

```text
Use the uploaded product reference image only as product truth, not as an opening packshot. The first visible frame must already show the hand holding the product near camera.
```

## 4. Small Product Occlusion Rule

Small products must not fully disappear behind or inside props during short CTA / scale-proof clips.

Allowed:

- place product beside pouch
- rest product half-on pouch opening
- hold product over pouch without hiding it
- show pouch as secondary prop only
- keep at least 70% of the product visible during carry proof

Blocked unless the operator explicitly accepts higher render risk:

- fully insert product into pouch / pocket / drawer
- pull product back out after full occlusion
- hide-and-retrieve motion
- fast hand jump that covers the label and body
- product disappearing behind fingers or fabric for more than a moment

## 5. One-Way Motion Rule For 6s CTA

A 6s CTA should use one simple motion path.

Preferred motion:

```text
hand already holding product -> show beside pouch -> stable final close-up
```

Avoid:

```text
product-only flash -> hand appears -> put product into pouch -> pull product out -> final close-up
```

Rationale: too many state changes in 6s increase product identity drift and object reconstruction artifacts.

## 6. Engine-Specific Guidance

### GROK

For GROK 6s / 10s clips, add the anti-glitch motion rule directly inside the final operator-facing prompt.

Required wording for pouch / compact-carry scenes:

```text
Anti-glitch motion rule: the first visible frame already shows the hand holding the product near camera. Do not start with a standalone product-only packshot. No product flash, no sudden object appearance, no jump cut, no duplicate product. Keep the product visible at all times. Do not fully insert the product into the pouch and do not pull it back out from inside the pouch. Only place the product beside the pouch or rest it half-on the pouch opening while at least 70% of the product remains visible. Use one continuous hand motion with no object hiding or reappearing.
```

### GOOGLE_FLOW.FLOW_EXTEND_UI

For Flow / Veo-style image-to-video or extend prompts, prefer an approved starting frame that already shows the intended hand/product pose.

Recommended wording:

```text
Animate this exact starting frame. The starting frame already shows the hand holding the product beside the pouch. Preserve first-frame composition, hand position, product scale, label, lighting, and scene layout. Do not create a standalone product-only opening shot. Do not hide the product inside the pouch. Keep at least 70% of the product visible throughout the clip.
```

## 7. Validation Checklist

A prompt passes this guardrail when:

```yaml
first_frame_anchor: PASS
standalone_product_flash: BLOCKED
small_product_full_occlusion: BLOCKED
hide_and_retrieve_motion: BLOCKED
product_visible_minimum: "70% during compact-carry proof"
duplicate_product: BLOCKED
one_way_motion_for_6s_cta: PASS
product_label_visibility: PRIORITISED
```

## 8. Failure Handling

If a rendered output still shows flash/glitch:

1. remove full pouch insertion
2. remove pull-out / retrieve motion
3. force first frame to already include hand + product
4. switch from pure product reference to ready-frame/source-frame starter
5. reduce movement to beside-pouch or half-on-pouch cue
6. rerender using a tighter one-way motion prompt

## 9. Notion Mirror Rule

Notion templates may mirror this guardrail, but Notion remains downstream UI only.

Mirror first into:

- `05A — BOSMAX Serum Grok Templates` / 6s Punchy CTA
- BOSMAX Grok image handoff / source-frame templates
- BOSMAX Google Flow CTA / image-to-Flow starter templates

Do not mark Notion prompts READY solely from the mirror. Render evidence or output-quality validation must remain explicit.
