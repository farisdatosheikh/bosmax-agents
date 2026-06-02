# BOSMAX Deterministic Flow v1
# Date: 2026-06-02
# Status: Phase 1 authority spec

## Objective

This spec defines the BOSMAX phase-1 deterministic flow for **one output at a time**.

It is the foundation that every later batch lane must reuse.

The target is not "maximum flexibility."
The target is:
- minimal user input
- deterministic routing
- stable authority resolution
- one clean image prompt or one clean video prompt per run

---

## Phase-1 Principle

Single-output stability comes first.

Order of operations:
1. lock one deterministic image output
2. lock one deterministic video output
3. normalize authority surfaces
4. only then open batch prompt generation under `BOSMAX_BATCH_LANE_v1.md`

---

## User-Facing Modes

Users should not be forced to think in BOSMAX internal route names.

### Mode 1 — IMAGE
User intent:
- generate clean image for later video use
- generate selling poster

### Mode 2 — VIDEO
User intent:
- generate a new video prompt from avatar + product
- generate a video prompt inspired by reference image/video

---

## Shared Intake Contract

### Universal fields
- `task_mode`: `IMAGE` | `VIDEO`
- `avatar_image`
- `product_image`
- `product_name`
- `platform`
- `language`

### IMAGE-only fields
- `image_goal`: `VIDEO_SUPPORT` | `SELLING_POSTER`

### VIDEO-only fields
- `video_engine`
- `duration_target`
- `product_info_simple`
- `reference_mode`: `NONE` | `IMAGE_REFERENCE` | `VIDEO_REFERENCE` | `BOSMAX_IMAGE_HANDOFF`

### Optional fields
- `scene_preference`
- `copy_style_preference`
- `cta_style_preference`

---

## Authority Resolution Order

### Product truth
1. `products/*.yaml`
2. FastMoss workbook surfaces
3. user input fallback

### Dialogue truth
- default products: `product_record.copywriting`
- sensitive products: `dialogue_authority -> SCRIPT_REGISTRY_UNIFIED.md + SCRIPT_VARIANT_LIBRARY.md`

### Image / visual truth
- direct user uploads
- BOSMAX `subject_dna`
- BOSMAX `source_image_handoff`
- Route D concept extraction if reference media exists

---

## Deterministic Route Resolution

### IMAGE mode

#### Case A — `image_goal = VIDEO_SUPPORT`
Purpose:
- clean avatar + product image
- minimal selling text
- maximum continuity value for later video generation

Internal route:
1. `bosmax-product-intelligence`
2. `bosmax-subject-dna`
3. `bosmax-scene-engine`
4. `bosmax-compliance-gate`

Output:
- `master_image_prompt`
- `source_image_handoff`
- `product_truth_lock`
- `avatar_truth_lock`

#### Case B — `image_goal = SELLING_POSTER`
Purpose:
- sales-oriented poster
- avatar + product + selling hierarchy

Internal route:
1. `bosmax-product-intelligence`
2. optional `bosmax-image-analyst` if reference image supplied
3. `bosmax-subject-dna`
4. `bosmax-scene-engine`
5. `bosmax-compliance-gate`

Output:
- `master_poster_prompt`
- `source_image_handoff`
- `product_truth_lock`
- `avatar_truth_lock`
- selling hierarchy embedded in the prompt body

---

### VIDEO mode

#### Case A — `reference_mode = NONE`
Purpose:
- generate a fresh video prompt from avatar + product + product authority

Internal route:
1. `bosmax-product-intelligence`
2. resolve dialogue authority
3. BOSMAX pre-flight duration / engine validation
4. `bosmax-script-generator`
5. `bosmax-compliance-gate`

#### Case B — `reference_mode = IMAGE_REFERENCE`
Purpose:
- user uploads image and wants a similar concept for their own product

Internal route:
1. `bosmax-image-analyst`
2. `bosmax-product-intelligence`
3. compatibility checks
4. `bosmax-script-generator`
5. `bosmax-compliance-gate`

Important:
- generic uploaded images are **not** Mode C by default
- Mode C is reserved for BOSMAX `source_image_handoff`

#### Case C — `reference_mode = VIDEO_REFERENCE`
Purpose:
- user uploads video/frames and wants the same concept rebuilt for Product B

Internal route:
1. `bosmax-video-analyst`
2. `bosmax-product-intelligence`
3. compatibility checks
4. `bosmax-script-generator`
5. `bosmax-compliance-gate`

#### Case D — `reference_mode = BOSMAX_IMAGE_HANDOFF`
Purpose:
- user already has BOSMAX-generated image DNA and wants locked video continuity

Internal route:
1. BOSMAX pre-flight verifies `source_image_handoff`
2. `bosmax-mode-c-executor`
3. `bosmax-compliance-gate`

---

## Known vs Unknown Product Logic

### Known product
If resolved from registry or FastMoss:
- use stored scale anchor
- use stored packaging truth
- use stored compliance class
- use stored dialogue authority

### Unknown product
Do not hard-block too early.
Build a fallback card:
- name
- estimated category
- estimated form factor
- temporary scale anchor
- temporary compliance class
- generated copywriting fallback

Then allow one deterministic output and offer registry registration afterwards.

---

## Output Contracts

### IMAGE output contract
- `prompt_final`
- `prompt_mode`
- `image_goal`
- `product_truth_lock`
- `avatar_truth_lock`
- `negative_lock_block`
- `source_image_handoff`

### VIDEO output contract
- `prompt_final` or `block_prompts[]`
- `engine_id`
- `duration_target`
- `reference_mode`
- `block_plan`
- `dialogue_authority_resolved`
- `product_truth_lock`
- `visual_lock`
- `continuity_lock` when multi-block

---

## Batch Gate

Batch generation may only open after all of the following are stable:
- image mode deterministic for `VIDEO_SUPPORT`
- image mode deterministic for `SELLING_POSTER`
- video mode deterministic for `reference_mode = NONE`
- video mode deterministic for `reference_mode = IMAGE_REFERENCE`
- video mode deterministic for `reference_mode = VIDEO_REFERENCE`
- output contracts accepted as final authority

Until then, batch mode is architecture-prohibited.

Once all gates pass:
- batch planning authority moves to `BOSMAX_BATCH_LANE_v1.md`
- batch rows must expand back into the deterministic single-output contracts above

---

## Out of Scope for Phase 1

- uncontrolled batch prompt generation before plan approval
- new engine registry files
- broad orchestrator rewrites
- Notion sync before repo behavior is locked

---

## Repository Surfaces Expected To Reflect This Spec

- `BOSMAX_BATCH_LANE_v1.md`
- `.claude/CLAUDE.md`
- `.claude/skills/bosmax-bulk-generator.md`
- `.claude/skills/bosmax-scene-engine.md`
- `.claude/skills/bosmax-script-generator.md`
- `.claude/skills/bosmax-image-analyst.md`
- `.claude/skills/bosmax-video-analyst.md`
- `.claude/BOSMAX-LOG.md`
