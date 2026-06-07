# BOSMAX Image Template Card Contract v1

## Status

`DRAFT — PENDING PILOT TEST`

Defines the upgraded schema for BOSMAX image Template Cards. Supersedes the
informal v0.1 field set used in 01A Notion pages. Not yet injected into Notion
or validators.

---

## Purpose

Define the complete field contract for a BOSMAX Image Template Card at v1.0.
This contract is the authority for:

- What fields every image template card must contain
- What each field means and what values are allowed
- How v0.1 legacy fields must be mapped or split
- How template cards relate to prompt expansion and QA layers

---

## Why v0.1 Cards Are Not Enough

The current 01A template cards contain:

| v0.1 Field | Problem |
|---|---|
| `Design Angle` | Too vague — mixes multiple design concepts into one free-text string |
| `Visual Direction` | Undefined structure — each card uses different wording |
| `Allowed Variations` | No distinction between frozen controls and mutation axes |
| `Do Not Change` | Is a note, not an enforced contract |
| No layout formula | Agent has no structured instruction on zone split |
| No visual mechanic ID | No way to reference the mechanics library |
| No QA target | No pass/fail gate defined per template |
| No creative intensity | No declared commercial ambition per template |

v0.1 cards produce routing-correct but commercially weak outputs. This contract
fixes the design intelligence gap.

---

## Contract Layer Definitions

| Layer | File / Source | Role |
|---|---|---|
| Template Card | This contract | Declares design objective and constraints |
| Master Prompt Seed | Generated from Template Card | Short-form prompt nucleus |
| Full Image Generation Prompt | Expanded from Seed | Ready-to-paste full prompt |
| Universal Variation Controller | Template Card variation axes | Governs what variants may change |
| QA Gate | `BOSMAX_POSTER_QA_RUBRIC_v1` | Scores and gates output |

---

## Required Template Card Fields

Every v1 Image Template Card must contain all of the following fields.
Fields marked `FROZEN` cannot be changed between variants within the same family.

| Field | Required | FROZEN | Description |
|---|---|---|---|
| `template_set_id` | YES | FROZEN | Unique identifier for this template family |
| `template_name` | YES | — | Human-readable name |
| `template_role` | YES | FROZEN | Always `MASTER_PROMPT_SEED` for canonical cards |
| `prompt_expansion_mode` | YES | FROZEN | How agent expands this card to a full prompt |
| `product_id` | YES | FROZEN | From `product_record.product_id` |
| `product_truth_lock` | YES | FROZEN | JSON object — frozen product attributes |
| `creative_intensity` | YES | FROZEN | `SAFE` / `CONVERSION` / `SCROLL_STOPPER` |
| `template_family` | YES | FROZEN | Taxonomy classification |
| `commercial_trigger` | YES | — | What commercial desire this template activates |
| `hero_proof` | YES | — | The primary proof element the image delivers |
| `visual_mechanic` | YES | — | Mechanic ID from the design skill mechanics library |
| `layout_formula` | YES | FROZEN | Formula ID from the design skill layout library |
| `shot_spec` | YES | — | Camera distance, angle, and framing instruction |
| `light_strategy` | YES | — | Lighting setup description |
| `surface_strategy` | YES | — | Background and surface material instruction |
| `scale_proof_rule` | YES | FROZEN | How scale anchor is proven in this template |
| `hand_pose_rule` | conditional | — | Required if human hand is in composition |
| `safe_zone_rule` | YES | FROZEN | Which layout zones must remain clear |
| `overlay_direction` | YES | — | What overlay content is allowed, if any |
| `language_mix` | YES | — | `BM_ONLY` / `EN_ONLY` / `BM_EN_MIX` / `NONE` |
| `text_rendering_mode` | YES | FROZEN | `OVERLAY_ONLY` / `AI_RENDER` / `NO_TEXT` |
| `reference_handling` | YES | FROZEN | How reference images are to be used |
| `frozen_controls` | YES | FROZEN | Explicit list of fields that cannot vary between variants |
| `variation_axis` | YES | — | Explicit list of fields that may vary between variants |
| `rejection_rule` | YES | FROZEN | Template-specific auto-reject trigger |
| `output_required` | YES | — | Expected output type(s) from this card |
| `qa_score_target` | YES | FROZEN | Minimum overall QA score for this template |

---

## Deprecated / Demoted Fields

These v0.1 fields are superseded by v1 fields. They must not appear as primary
fields in v1 cards. They may be kept as `legacy_notes` for migration reference.

| v0.1 Field | Replacement in v1 |
|---|---|
| `Design Angle` | Split into: `commercial_trigger` + `hero_proof` + `visual_mechanic` |
| `Visual Direction` | Split into: `layout_formula` + `shot_spec` + `light_strategy` + `surface_strategy` + `safe_zone_rule` |
| `Allowed Variations` | Replaced by: `frozen_controls` + `variation_axis` + mutation limit rules |
| `Do Not Change` | Replaced by: `product_truth_lock` (FROZEN) + `rejection_rule` |
| Free-text `Notes` field | Must be structured as `open_questions` array or removed |

---

## Field Definitions

### `template_set_id`
Format: `BOSMAX_[PRODUCT_CODE]_[FAMILY_CODE]_[SEQUENTIAL_NUMBER]`
Example: `BOSMAX_SERUM_TRUTH_MACRO_001`

### `template_role`
Only one value is allowed for canonical cards: `MASTER_PROMPT_SEED`
Variants generated from a master card carry role `VARIANT`.

### `prompt_expansion_mode`
Tells the agent how to expand this card into a full prompt.

| Value | Meaning |
|---|---|
| `GENERATE_FULL_MASTER_IMAGE_PROMPT` | Agent builds the full structured prompt |
| `COMPOSE_FROM_SUBJECT_DNA` | Agent injects subject_dna before composing |
| `OVERLAY_ONLY_POSTPROCESS` | Agent generates clean image; text applied post-composite |

### `product_truth_lock`

JSON object with FROZEN attributes extracted from `product_record`.

```json
{
  "product_id": "BOSMAX_SERUM_5ML",
  "product_name": "BOSMAX Serum",
  "variant": "5ml",
  "bottle_geometry": "small cylindrical tube, approximately 5ml volume",
  "cap_type": "twist-off cap, opaque white",
  "body_color": "white or off-white tube body",
  "label_text": "BOSMAX HERBS",
  "label_placement": "centered on tube body",
  "scale_anchor_descriptor": "EXACTLY lip balm size, fit into fingers naturally",
  "compliance_class": "STEALTH"
}
```

### `creative_intensity`

| Value | Definition |
|---|---|
| `SAFE` | Factual, calm, trust-building. No visual tension. Works for cold audiences. |
| `CONVERSION` | Clear commercial hierarchy. CTA visible. Price or offer present. |
| `SCROLL_STOPPER` | Maximum visual tension. Unexpected composition. Forces a pause in scroll. |

### `template_family`

| Value | Description |
|---|---|
| `TRUTH_MACRO` | Primary goal: prove product is exactly as described |
| `SCALE_PROOF` | Primary goal: prove product is the correct physical size |
| `CARRY_CONTEXT` | Primary goal: prove product fits in daily life / pocket carry |
| `NIGHT_RITUAL` | Primary goal: position product in daily routine context |
| `COMMERCE_IMPACT` | Primary goal: drive immediate purchase action |

### `visual_mechanic`
Must reference a mechanic ID from `BOSMAX_COMMERCIAL_POSTER_DESIGN_SKILL_v1.md`
mechanic library (e.g. `01_FINGERTIP_SCALE_PROOF`, `11_RIM_LIGHT_BLACK_SEPARATION`).

### `layout_formula`
Must reference a formula ID from `BOSMAX_COMMERCIAL_POSTER_DESIGN_SKILL_v1.md`
layout formula library (e.g. `LF-01`, `LF-05`).

### `scale_proof_rule`
Must be a complete sentence describing how scale anchor is visually proven.
Example: `Bottle held between index finger and thumb; fingernail visible; bottle
does not exceed width of single finger segment; reference object absent.`

### `safe_zone_rule`
Must declare which zones are clear.
Example: `Top 8% clear. Bottom 20% clear. Right column above 50% clear for TikTok
engagement buttons.`

### `overlay_direction`
Declares what overlay copy is permitted on this template.

| Value | Meaning |
|---|---|
| `NONE` | No overlay text in this template |
| `HEADLINE_RAIL_ONLY` | One line of hook copy in top safe-zone rail only |
| `FOOTER_BAR_ONLY` | One line in footer offer bar only |
| `BADGE_CLUSTER` | CTA badge cluster in bottom-right safe zone only |
| `FULL_OVERLAY_PERMITTED` | Full overlay planning via `text_rendering_mode = OVERLAY_ONLY` |

### `text_rendering_mode`

| Value | Meaning |
|---|---|
| `OVERLAY_ONLY` | No text in generation prompt; all text applied post-composite |
| `AI_RENDER` | Text described in prompt; agent must include anti-mutation constraint |
| `NO_TEXT` | No text in image at all; purely visual |

### `reference_handling`

| Value | Meaning |
|---|---|
| `NO_REFERENCE` | Template has no reference image; build from card fields only |
| `CONCEPT_DNA_ONLY` | Reference used for visual structure only; all identity replaced |
| `SUBJECT_DNA_INJECT` | subject_dna from bosmax-subject-dna injected into scene |

### `rejection_rule`
Template-specific hard reject. Must be a clear conditional statement.
Example: `REJECT if bottle appears larger than thumb width, OR if cap is missing,
OR if product category reads as cosmetic serum / perfume / dropper.`

### `qa_score_target`
Format: `overall: [integer] | no_dimension_below: [integer]`
Standard target: `overall: 82 | no_dimension_below: 7`
Truth-critical templates: `overall: 88 | no_dimension_below: 8`

---

## Allowed Enums Summary

| Field | Allowed Values |
|---|---|
| `template_role` | `MASTER_PROMPT_SEED`, `VARIANT` |
| `prompt_expansion_mode` | `GENERATE_FULL_MASTER_IMAGE_PROMPT`, `COMPOSE_FROM_SUBJECT_DNA`, `OVERLAY_ONLY_POSTPROCESS` |
| `creative_intensity` | `SAFE`, `CONVERSION`, `SCROLL_STOPPER` |
| `template_family` | `TRUTH_MACRO`, `SCALE_PROOF`, `CARRY_CONTEXT`, `NIGHT_RITUAL`, `COMMERCE_IMPACT` |
| `text_rendering_mode` | `OVERLAY_ONLY`, `AI_RENDER`, `NO_TEXT` |
| `reference_handling` | `NO_REFERENCE`, `CONCEPT_DNA_ONLY`, `SUBJECT_DNA_INJECT` |
| `overlay_direction` | `NONE`, `HEADLINE_RAIL_ONLY`, `FOOTER_BAR_ONLY`, `BADGE_CLUSTER`, `FULL_OVERLAY_PERMITTED` |
| `language_mix` | `BM_ONLY`, `EN_ONLY`, `BM_EN_MIX`, `NONE` |

---

## BOSMAX Serum Example Card v1

```yaml
template_set_id: BOSMAX_SERUM_SCALE_PROOF_001
template_name: "BOSMAX Serum — Fingertip Scale Proof Master"
template_role: MASTER_PROMPT_SEED
prompt_expansion_mode: COMPOSE_FROM_SUBJECT_DNA
product_id: BOSMAX_SERUM_5ML

product_truth_lock:
  product_id: BOSMAX_SERUM_5ML
  product_name: "BOSMAX Serum"
  variant: "5ml"
  bottle_geometry: "small cylindrical tube, approximately 5ml volume"
  cap_type: "twist-off cap, opaque white"
  body_color: "white or off-white tube body"
  label_text: "BOSMAX HERBS"
  label_placement: "centered on tube body"
  scale_anchor_descriptor: "EXACTLY lip balm size, fit into fingers naturally"
  compliance_class: STEALTH

creative_intensity: CONVERSION
template_family: SCALE_PROOF

commercial_trigger: >
  Viewer instinctively doubts an online product's size. This template resolves
  that doubt before it forms, converting skepticism into a purchase decision.

hero_proof: >
  Avatar fingertip contacts the bottle cap. Fingernail clearly visible.
  Bottle fits between fingertip and first knuckle. Scale proven without text.

visual_mechanic: "01_FINGERTIP_SCALE_PROOF"
layout_formula: "LF-01"

shot_spec: >
  MCU (mid-close-up). Hand and product dominate lower 40% of frame. Avatar
  face partial or cropped in upper 35%. Camera angle: slightly above hand level.
  Shallow depth of field — product sharp, background soft.

light_strategy: >
  Soft natural window light from left. Fills hand and bottle uniformly.
  No harsh shadows. No reflection glare on product label.

surface_strategy: >
  Clean minimal background. Light off-white or warm neutral tone. No props
  except the hand and product. No busy textures.

scale_proof_rule: >
  Bottle must be visibly smaller than the width of a single finger segment.
  Fingernail must be visible to confirm human scale. No scale-anchor object
  (lip balm, coin) required — finger itself is the anchor.

hand_pose_rule: >
  Right hand preferred. Thumb and index finger pinch bottle gently at mid-body.
  Other fingers softly relaxed, not rigid. Nails clean, no nail art.

safe_zone_rule: >
  Top 8% of frame: clear. Bottom 20% of frame: clear.
  Right edge above 35% vertical: clear (TikTok engagement buttons).

overlay_direction: HEADLINE_RAIL_ONLY
language_mix: BM_EN_MIX
text_rendering_mode: OVERLAY_ONLY

reference_handling: SUBJECT_DNA_INJECT

frozen_controls:
  - product_id
  - product_truth_lock
  - compliance_class
  - template_family
  - visual_mechanic
  - layout_formula
  - scale_proof_rule
  - safe_zone_rule
  - text_rendering_mode

variation_axis:
  - background_color_tone
  - avatar_wardrobe_color
  - lighting_temperature
  - hand_pose_minor_adjustment
  - overlay_copy_text

rejection_rule: >
  REJECT if: bottle appears larger than thumb width; OR cap missing; OR label
  text garbled; OR product reads as cosmetic serum / perfume / dropper / deodorant;
  OR impossible hand anatomy; OR TikTok safe zone blocked by product content.

output_required:
  - full_master_image_prompt
  - source_image_handoff

qa_score_target: "overall: 82 | no_dimension_below: 7"
```

---

## Template Family Taxonomy

| Family | Primary goal | Typical layout | Typical intensity |
|---|---|---|---|
| `TRUTH_MACRO` | Prove product ingredients / authenticity | LF-07, LF-02 | SAFE |
| `SCALE_PROOF` | Prove product is physically the correct size | LF-01, LF-09 | CONVERSION |
| `CARRY_CONTEXT` | Prove product fits in daily carry / pocket | LF-11, LF-09 | CONVERSION |
| `NIGHT_RITUAL` | Position product in nightly routine | LF-06, LF-01 | SAFE to CONVERSION |
| `COMMERCE_IMPACT` | Drive immediate purchase action | LF-05, LF-06, LF-15 | SCROLL_STOPPER |

Minimum recommended cards per family for sustainable variation: 3 masters × 3 variants = 9 images.

---

## Creative Intensity Mix

For a balanced TikTok product content set, the recommended intensity mix is:

| Intensity | Proportion | Rationale |
|---|---|---|
| `SAFE` | 40% | Cold audience trust-building; low skip rate |
| `CONVERSION` | 40% | Warm audience nudge; direct commerce signal |
| `SCROLL_STOPPER` | 20% | Broad reach hooks; high visual tension |

Do not publish only `SCROLL_STOPPER` intensity — it reads as desperation at scale
and reduces trust for new audiences.

---

## Validation Expectations

When the validator layer is extended to cover image template cards (future PR):

- All required fields must be non-null
- `template_role` must be exactly `MASTER_PROMPT_SEED` for canonical cards
- `product_id` must resolve in `products/*.yaml`
- `visual_mechanic` must resolve in the mechanics library
- `layout_formula` must resolve in the layout formula library
- `compliance_class` must match `product_record.compliance_class`
- `qa_score_target` must be parseable and >= 82 overall

These checks are not yet in runtime validators. They are defined here as the
future validator contract.

---

## Migration Plan for 01A

The 01A Notion template pages must be rewritten from v0.1 to v1.0.
This is a separate PR. The migration steps are:

1. Read each 01A card and identify the implied commercial trigger.
2. Map the free-text "Design Angle" to one `commercial_trigger` sentence and one `hero_proof` sentence.
3. Map the free-text "Visual Direction" to a `layout_formula` ID and `shot_spec`.
4. Identify the implied `visual_mechanic` and assign a mechanic ID.
5. Populate `frozen_controls` and `variation_axis` explicitly.
6. Replace "Do Not Change" with `product_truth_lock` JSON and `rejection_rule`.
7. Add `qa_score_target`.
8. Validate against this contract.
9. Submit 01A rewrite PR with before/after comparison.

Do not start migration until this contract is approved and pilots are complete.
