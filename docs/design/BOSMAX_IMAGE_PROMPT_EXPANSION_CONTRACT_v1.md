# BOSMAX Image Prompt Expansion Contract v1

## Status

`DRAFT — PENDING PILOT TEST`

Defines how Claude Cowork / BOSMAX Agents must expand a v1 Template Card into
a full image generation prompt. Not yet injected into runtime skills.

---

## Purpose

A Template Card (defined in `BOSMAX_IMAGE_TEMPLATE_CARD_CONTRACT_v1.md`) is a
compact design specification. It cannot be pasted directly into an image generation
engine. This contract defines the rules, format, and quality gates that govern the
expansion of a Template Card into a Full Image Generation Prompt that is ready to use.

---

## Layer Architecture

Expansion flows through five sequential layers. Each layer has a defined input,
output, and authority.

```
Layer 1 — Template Card
  Input:  Operator completes Template Card fields
  Output: Structured card YAML
  Authority: BOSMAX_IMAGE_TEMPLATE_CARD_CONTRACT_v1

Layer 2 — Master Prompt Seed
  Input:  Template Card
  Output: Short-form prompt nucleus (English, ~80–120 words)
  Authority: This contract, Section: Master Prompt Seed Rules

Layer 3 — Full Image Generation Prompt
  Input:  Master Prompt Seed + product_record + subject_dna
  Output: Structured full prompt (12 required sections)
  Authority: This contract, Section: Full Master Prompt Output Format

Layer 4 — Universal Variation Controller
  Input:  Full Prompt + Template Card variation_axis + Variant Index
  Output: N variant prompts, each derived from the master
  Authority: This contract, Section: Universal Variation Controller Rules

Layer 5 — QA Gate
  Input:  Full Prompt + Variants
  Output: Pass / Fail per dimension
  Authority: BOSMAX_POSTER_QA_RUBRIC_v1
```

---

## Expansion Flow

```
START: Template Card confirmed complete
  ↓
STEP 1: Validate all required Template Card fields are non-null
  ↓
STEP 2: Confirm product_record available (from bosmax-product-intelligence)
  ↓
STEP 3: Confirm subject_dna available (if prompt_expansion_mode = COMPOSE_FROM_SUBJECT_DNA)
  ↓
STEP 4: Build Master Prompt Seed
  ↓
STEP 5: Expand to Full Image Generation Prompt (12-section format)
  ↓
STEP 6: Apply compliance constraints and negative constraint block
  ↓
STEP 7: QA Gate check (Prompt-Level QA from rubric)
  ↓
STEP 8: If variants requested — apply Universal Variation Controller
  ↓
STEP 9: Output to image generation engine or return to operator
END
```

---

## Input Requirements

All of the following must be resolved before expansion begins.

| Input | Source | Required |
|---|---|---|
| `template_card` | v1 Template Card YAML | YES |
| `product_record` | `bosmax-product-intelligence` | YES |
| `subject_dna` | `bosmax-subject-dna` | If `COMPOSE_FROM_SUBJECT_DNA` |
| `platform` | PRE-FLIGHT resolved | YES |
| `creative_intensity` | `template_card.creative_intensity` | YES |
| `compliance_class` | `product_record.compliance_class` | YES |
| `scale_anchor_descriptor` | `product_record.variant.scale_anchor` | YES |
| `language_mix` | `template_card.language_mix` | YES |
| `overlay_direction` | `template_card.overlay_direction` | YES |

**Fail conditions before expansion:**
- If `product_record` is null: STOP. Request product record.
- If `subject_dna` is required and null: STOP. Request subject_dna.
- If `template_card.template_role` is not `MASTER_PROMPT_SEED`: STOP.
  Warn operator that variants require a master card to exist first.
- If `scale_anchor_descriptor` is null and platform is TikTok: STOP.
  Cannot generate without scale proof for TikTok.

---

## Output Requirements

| Output | Description |
|---|---|
| `full_master_image_prompt` | 12-section English prompt, ready for image engine |
| `prompt_variants` | Array of variant prompts (one per variation axis combination) |
| `qa_checklist_result` | Per-dimension pass/fail scores |
| `source_image_handoff` | JSON passport (required if `output_required` includes it) |

---

## Prompt Expansion Rules

1. **Do not output another short YAML card** when a full prompt is requested.
   The output must be the full 12-section English prompt string.

2. **Do not summarise the template card** as the prompt. The prompt is an original
   natural-language construction built from the card fields, not a paraphrase of
   the card's YAML.

3. **Scale anchor descriptor must appear verbatim** in Section 3 (Product Scale and
   Geometry). Do not paraphrase it.

4. **Label text must appear verbatim** from `product_truth_lock.label_text`.
   Do not invent an alternate brand name.

5. **Negative constraint block is mandatory.** Section 10 must be present in every
   full prompt. Do not omit negative constraints to save tokens.

6. **No uncontrolled language.** The prompt must not contain filler phrases like
   "imagine a beautiful scene" or "a creative composition." Every sentence must
   serve a defined design function.

7. **Compliance constraints are injected from the compliance_class**, not invented.
   Use the exact constraint language from the STEALTH / DIRECT compliance tables.

8. **Text in image is controlled by `text_rendering_mode`.**
   - If `OVERLAY_ONLY`: do not include any text description in Sections 1–11.
     Only mention in Section 8 that text will be applied post-composite.
   - If `AI_RENDER`: describe the text element and include in Section 10:
     `no misspelled text, no garbled characters, no font mutation`.
   - If `NO_TEXT`: no text anywhere. Section 8 states `no text in image`.

9. **Background instruction must be specific**, not generic ("clean white background"
   is not specific enough). Describe material, tone, depth, and texture.

10. **Hand anatomy must be explicitly protected.** If a hand is in the composition,
    Section 10 must include: `anatomically correct hand, correct finger count,
    no melted or fused fingers, natural joint articulation`.

---

## Route-Aware Prompting

Different prompt expansion paths depending on `prompt_expansion_mode`:

### `GENERATE_FULL_MASTER_IMAGE_PROMPT`
Build the full prompt entirely from Template Card fields + product_record.
No subject_dna injection. Product-only or product-with-generic-hand composition.

### `COMPOSE_FROM_SUBJECT_DNA`
Inject subject_dna fields into the prompt's avatar description sections.
Avatar description in Section 1 must use exact subject_dna values:
- gender, ethnicity, age_range, wardrobe, accessories, skin_tone, expression

Do not invent avatar attributes. If subject_dna has null fields, ask for them.

### `OVERLAY_ONLY_POSTPROCESS`
Generate a clean image with no text. Section 8 declares:
`Text will be applied post-composite via overlay. No text in generated image.`
Full overlay spec (copy formula, font, position, language) is returned as a
separate overlay_spec JSON alongside the image prompt.

---

## Model Route Notes

These are notes on current text rendering fidelity by model. This section will
be updated as pilot test data accumulates.

| Model | Label text fidelity | Recommended mode |
|---|---|---|
| NANO_BANANA_PRO | Unverified at 5ml scale | `OVERLAY_ONLY` until pilot confirms |
| IMAGEN_3 | Unverified in BOSMAX production | `OVERLAY_ONLY` until pilot confirms |
| General note | Exact certification numbers and prices | Always `OVERLAY_ONLY` |
| General note | Short 1–2 word labels at large size | `AI_RENDER` acceptable with negative constraint |

If exact text rendering is required and the model route is unverified:
**recommend deterministic overlay/post-composite.** Do not attempt to render
critical exact text in-model for production unless pilot test has confirmed fidelity.

---

## Universal Variation Controller Rules

Variants are derived from the master prompt. They must obey these rules:

1. **Variants must preserve the template objective.** A SCALE_PROOF template must
   still prove scale in every variant. Changing layout formula to one that removes
   the hand invalidates the template objective.

2. **Variants may only mutate declared variation axes.** The `variation_axis` list
   in the Template Card is the only permitted mutation surface.

3. **A maximum of 3 variation axes may change between any two variants.**
   Changing 4+ axes produces a new template card, not a variant.

4. **Frozen controls are absolutely frozen.** The controller must check that no
   frozen field has changed between master and any variant.

5. **No uncontrolled randomization.** Do not generate "creative variations" that
   are not grounded in a declared variation axis.

6. **Variant index must be declared.** Every variant must carry:
   `variant_index: [N]` and `parent_template_set_id: [master_id]`.

7. **Variants must score within 5 QA points of the master.** A variant that scores
   below 77 when the master scored 82 is out of family tolerance and must be rejected.

8. **Variant batch limit:** Maximum 5 variants per master card per expansion run.
   For larger batches, use `bosmax-bulk-generator` with the variant plan protocol.

---

## Full Master Prompt Output Format

Every Full Image Generation Prompt must contain all 12 sections. Section names
are required headers. Content must be specific, operational English.

```
--- BOSMAX IMAGE PROMPT ---
Template: [template_set_id]
Product: [product_id] | [product_name] [variant]
Platform: [platform]
Intensity: [creative_intensity]
Expansion mode: [prompt_expansion_mode]

Section 1 — Output Spec
  [Image dimensions, format, aspect ratio]
  Standard: 9:16 vertical, 1080×1920px, photorealistic commercial photograph style

Section 2 — Product Reference Lock
  [Verbatim product geometry, cap, label, color from product_truth_lock]
  [Verbatim scale_anchor_descriptor from product_record]

Section 3 — Product Scale and Geometry
  [How scale is established in this specific composition]
  [Scale proof mechanic description]

Section 4 — Composition and Layout
  [Layout formula description — zone split, product position, avatar position]
  [Depth of field instruction]

Section 5 — Visual Mechanic
  [Named mechanic from design skill library]
  [Exact execution of mechanic in this scene]

Section 6 — Lighting and Surface
  [Light source, direction, quality]
  [Surface material, color, texture]

Section 7 — Background
  [Background material, tone, depth]
  [What is visible / not visible in background]

Section 8 — Overlay Direction
  [Text in image: NONE / specific overlay zone description]
  [If OVERLAY_ONLY: state that text is post-composite]

Section 9 — Compliance Boundaries
  [Compliance class: STEALTH / DIRECT]
  [Specific no-go list from compliance_class rules]

Section 10 — Negative Constraints
  [All must-not items: wrong geometry, wrong label, wrong anatomy,
   wrong product category, TikTok safe zone violations, etc.]

Section 11 — Final Commercial Tone
  [One sentence describing the emotional register and commercial feel]
  [Tied to creative_intensity and commercial_trigger]

Section 12 — QA Checklist Reference
  [States: output will be scored against BOSMAX_POSTER_QA_RUBRIC_v1]
  [States: minimum pass score for this template]
--- END PROMPT ---
```

---

## Prompt Variant Output Format

Each variant prompt uses the same 12-section format with:
- A header declaring: `VARIANT [N] of [TEMPLATE_SET_ID]`
- Only the changed sections explicitly rewritten
- All unchanged sections carried forward verbatim from master
- A change log at the end: `Changed: [list of variation axis applied]`

```
--- BOSMAX IMAGE PROMPT — VARIANT [N] ---
Parent: [template_set_id]
Variant index: [N]
Changed axes: [axis_1, axis_2, ...]

[Full 12-section prompt with changed sections rewritten]

Change log:
  - [axis]: [old value] → [new value]
--- END VARIANT ---
```

---

## QA Before Output

Before returning the full prompt to the operator, the expansion agent must run
the Prompt-Level QA checks from `BOSMAX_POSTER_QA_RUBRIC_v1`:

- Section 2 present and matches product_truth_lock
- Scale anchor descriptor verbatim in Section 3
- Section 10 negative constraints present and non-empty
- Compliance boundaries in Section 9 match compliance_class
- If hand in composition: hand anatomy constraint in Section 10
- If `OVERLAY_ONLY`: no text described in Sections 1–11

If any check fails: do not output the prompt. Report the failure with the
specific section and field that failed.

---

## Failure / Refusal Conditions

The expansion agent must STOP and report to operator (not silently proceed) if:

| Condition | Action |
|---|---|
| `product_record` is null | STOP. "product_record required. Run bosmax-product-intelligence." |
| `subject_dna` required and null | STOP. "subject_dna required for COMPOSE_FROM_SUBJECT_DNA mode." |
| `scale_anchor_descriptor` is null + TikTok platform | STOP. "scale_anchor_descriptor required for TikTok." |
| Exact text rendering required + model unverified | WARN. "Recommend OVERLAY_ONLY for this text element. Confirm route." |
| Compliance risk detected in overlay copy | STOP. "Compliance risk in overlay copy. Operator decision required before proceed." |
| `template_role` is not `MASTER_PROMPT_SEED` | STOP. "Cannot expand a VARIANT card as a master." |
| Variant axis count > 3 | STOP. "4+ axes changed — this is a new template, not a variant." |
| Frozen control changed in variant | STOP. "Frozen control [field] cannot change in a variant." |

---

## Operator Usage Flow

Typical operator session using this contract:

```
1. Operator confirms product_record exists (PRE-FLIGHT STEP 0)
2. Operator runs bosmax-subject-dna to get subject_dna
3. Operator selects or creates Template Card (v1 schema)
4. Operator requests: "Expand to full prompt"
5. Agent validates inputs, runs expansion, runs prompt-level QA
6. Agent returns: full_master_image_prompt + qa_checklist_result
7. Operator reviews and approves or requests adjustment
8. Operator requests: "Generate [N] variants"
9. Agent applies Universal Variation Controller, returns variant prompts
10. All prompts pass QA gate before release to image engine
```

---

## Example Expansion Skeleton

Input Template Card (abbreviated):
```yaml
template_set_id: BOSMAX_SERUM_SCALE_PROOF_001
visual_mechanic: 01_FINGERTIP_SCALE_PROOF
layout_formula: LF-01
creative_intensity: CONVERSION
product_truth_lock.scale_anchor_descriptor: "EXACTLY lip balm size, fit into fingers naturally"
text_rendering_mode: OVERLAY_ONLY
```

Output Full Prompt (abbreviated):

```
--- BOSMAX IMAGE PROMPT ---
Template: BOSMAX_SERUM_SCALE_PROOF_001
Product: BOSMAX_SERUM_5ML | BOSMAX Serum 5ml
Platform: TikTok
Intensity: CONVERSION
Expansion mode: COMPOSE_FROM_SUBJECT_DNA

Section 1 — Output Spec
  9:16 vertical, 1080×1920px. Photorealistic commercial photograph.
  High detail, shallow depth of field. No illustration, no flat design.

Section 2 — Product Reference Lock
  Small cylindrical tube, approximately 5ml volume. Twist-off cap, opaque white.
  White or off-white tube body. Label text: BOSMAX HERBS, centered on tube body.
  EXACTLY lip balm size, fit into fingers naturally.

Section 3 — Product Scale and Geometry
  Product held between index fingertip and thumb. Fingernail clearly visible.
  Bottle does not exceed the width of one finger segment from tip to first knuckle.
  Bottle is shorter than the distance from fingertip to second knuckle.

Section 4 — Composition and Layout
  LF-01: Lower-third hero. Avatar face partial in upper 35% of frame.
  Product held by right hand in lower 40%. Lower 20% of frame clear.
  Shallow depth of field — product sharp, face soft-focused.

Section 5 — Visual Mechanic
  01_FINGERTIP_SCALE_PROOF: Avatar fingertip contacts bottle cap.
  Fingernail visible. Scale proven by human finger proportion alone.

Section 6 — Lighting and Surface
  Soft natural window light, source left. Even fill on hand and product.
  No harsh shadows. No specular glare on label.
  Surface: clean off-white minimal background.

Section 7 — Background
  Soft off-white or warm neutral. No props. No texture patterns.
  Background blurred to near-white by depth of field.

Section 8 — Overlay Direction
  No text in generated image. Text will be applied post-composite.

Section 9 — Compliance Boundaries
  STEALTH: No body part targeting. No before/after imagery. No skin condition reference.
  No medical or improvement claims. No guaranteed result language.

Section 10 — Negative Constraints
  No wrong bottle shape. No perfume or dropper bottle geometry. No deodorant form.
  No redesigned label. No garbled label text. No missing cap. No oversized bottle.
  Anatomically correct hand: correct finger count, no melted or fused fingers,
  natural joint articulation.
  No TikTok safe-zone collision — top 8% and bottom 20% of frame must be clear.

Section 11 — Final Commercial Tone
  Confident and precise. Product truth presented without hype. Scale proof is
  quietly compelling — the viewer understands without being told.

Section 12 — QA Checklist Reference
  Score against BOSMAX_POSTER_QA_RUBRIC_v1.
  Minimum pass: overall 82, no dimension below 7.
  Product Truth, Label Fidelity, Compliance Safety must be 9 or above.
--- END PROMPT ---
```

---

## Non-Scope

This contract does not govern:

- Video prompt expansion (governed by `bosmax-script-generator`)
- Batch exporter logic (governed by `bosmax-bulk-generator`)
- Product registration (governed by `bosmax-product-registration`)
- Engine duration or multi-block logic (governed by CLAUDE.md engine table)
- Notion template formatting (governed by Notion export contracts)
- Post-composite overlay execution (tooling decision, not prompt contract)
- GA4 / analytics event tagging of generated images
