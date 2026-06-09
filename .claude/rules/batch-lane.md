---
paths:
  - ".claude/skills/bosmax-bulk-generator.md"
  - "BOSMAX_BATCH*.md"
  - "MASTER_IGNITION_TEMPLATE.md"
  - "BOSMAX_INPUT_HELPER_v1.md"
  - "BOSMAX_IGNITION_WORKFLOW_v1.md"
---

# Batch Lane Supplement

Use this rule only when working on BOSMAX batch planning, batch examples, or the bulk generator lane.

## Official Batch Types

```yaml
BATCH_IMAGE_SUPPORT:
  every_row_resolves_to: "IMAGE + VIDEO_SUPPORT"

BATCH_IMAGE_SELLING:
  every_row_resolves_to: "IMAGE + SELLING_POSTER"

BATCH_VIDEO_FRESH:
  every_row_resolves_to: "VIDEO + NONE"

BATCH_MIXED_DETERMINISTIC:
  description: "controlled mix of deterministic rows"
  rule: "each row still resolves to one valid deterministic job"
```

## Batch Intake Contract

```yaml
Universal:
  batch_goal
  total_output_count
  product_scope
  platform
  language
  batch_variation_mode
  angle_lock
  semantic_intent
  copy_variant_count
  visual_variation_level

IMAGE batches:
  image_mix

VIDEO batches:
  video_mix
  video_engine
  duration_target

MIXED batches:
  image_count
  video_count
  image_mix
  video_mix
```

## Batch Variation Modes

```yaml
COPY_VARIANT_BATCH:
  meaning: "one locked angle, one locked semantic intent, multiple wording variants"
  default_when: "one clear angle + multiple poster/image outputs"
  drift_forbidden:
    - angle meaning
    - product truth
    - benefit direction
    - compliance class
    - target user mental block

ANGLE_ROTATION_BATCH:
  meaning: "multiple commercial angles intentionally rotated"
  allowed_when:
    - multiple angles provided
    - user explicitly asks for angle exploration

VISUAL_VARIANT_BATCH:
  meaning: "same angle and copy direction, composition varies"

MATRIX_BATCH:
  meaning: "controlled angle x copy x visual matrix"
  default_status: "NEEDS_REVIEW unless explicit"
```

## Batch Hard Rules

- Batch is not a new creative mode.
- Batch must build Variant Plan first.
- Every row in Variant Plan must resolve to a deterministic single-output route.
- Do not emit batch prompts before Variant Plan is approved.
- `VIDEO + BOSMAX_IMAGE_HANDOFF` inside a batch is valid only if the handoff pool truly exists.
- If one clear angle is given for multiple poster/image outputs, default to `COPY_VARIANT_BATCH`, not `ANGLE_ROTATION_BATCH`.
