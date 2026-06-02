# BOSMAX Batch Lane v1
# Date: 2026-06-02
# Status: Phase 2 authority spec

## Objective

This spec opens the BOSMAX batch lane **only after** single-output deterministic
image and video flows are already locked.

Batch is not a new creative mode.
Batch is a deterministic orchestration layer that:
- ingests one batch brief
- builds a Variant Plan
- expands each row into one deterministic single-output job
- packages the results into a prompt pack

---

## Authority Prerequisite

Batch may run only when the following are already accepted as stable:
- `IMAGE + VIDEO_SUPPORT`
- `IMAGE + SELLING_POSTER`
- `VIDEO + NONE`
- `VIDEO + IMAGE_REFERENCE`
- `VIDEO + VIDEO_REFERENCE`
- output contracts from `BOSMAX_DETERMINISTIC_FLOW_v1.md`

`VIDEO + BOSMAX_IMAGE_HANDOFF` is valid in batch only when a real BOSMAX
handoff pool already exists.

---

## Official Batch Types

### 1. `BATCH_IMAGE_SUPPORT`
- every row resolves to `IMAGE + VIDEO_SUPPORT`

### 2. `BATCH_IMAGE_SELLING`
- every row resolves to `IMAGE + SELLING_POSTER`

### 3. `BATCH_VIDEO_FRESH`
- every row resolves to `VIDEO + NONE`

### 4. `BATCH_MIXED_DETERMINISTIC`
- controlled mix of deterministic rows
- may combine image and video rows
- each row must still resolve to one valid deterministic single-output path

---

## Batch Intake Contract

### Universal fields
- `batch_goal`: `IMAGE_ONLY` | `VIDEO_ONLY` | `MIXED`
- `total_output_count`
- `platform`
- `language`
- `product_scope`: `SINGLE_PRODUCT` | `MULTI_PRODUCT`

### Single-product fields
- `product_name`
- `product_variant` (optional)
- `product_images[]` (optional but preferred)

### Multi-product fields
- `product_list[]`
  - `product_name`
  - `variant` (optional)
  - `target_count` (optional)
  - `product_image` (optional)

### IMAGE batch fields
- `image_mix`
  - `% VIDEO_SUPPORT`
  - `% SELLING_POSTER`

### VIDEO batch fields
- `video_mix`
  - `% NONE`
  - `% IMAGE_REFERENCE`
  - `% VIDEO_REFERENCE`
  - `% BOSMAX_IMAGE_HANDOFF`
- `video_engine`
- `duration_target`

### MIXED batch fields
- `image_count`
- `video_count`
- `image_mix`
- `video_mix`

### Optional control fields
- `avatar_pool`
- `scene_pool`
- `reference_pool`
- `copy_angle_pool`
- `cta_style_pool`
- `max_variants_per_angle`

---

## Batch Classification

### Class A — Simple batch
- single product
- single engine
- single duration
- one platform
- one language

### Class B — Structured mixed batch
- single product
- image + video rows
- deterministic mix declared up front

### Class C — Multi-product batch
- multiple products
- possibly mixed compliance classes
- planner must isolate rows cleanly by product truth and authority class

Phase-2 priority:
- fully support Class A
- support Class B with guardrails
- support Class C only through explicit row planning

---

## Variant Plan Protocol

Batch generation must never jump straight to prompt emission.

### Step 1 — normalize the request
- resolve known vs unknown products
- validate scale anchors
- validate engine and duration
- validate reference availability when requested

### Step 2 — build deterministic distribution
Examples:
- `50 IMAGE_ONLY` -> `30 VIDEO_SUPPORT` + `20 SELLING_POSTER`
- `40 VIDEO_ONLY` -> `25 NONE` + `10 IMAGE_REFERENCE` + `5 VIDEO_REFERENCE`

### Step 3 — assign controlled variation buckets
- avatar rotation
- scene rotation
- copy angle rotation
- CTA rotation
- camera / styling rotation

### Step 4 — emit a row-based Variant Plan
Each row must contain:
- `job_id`
- `product_name`
- `variant`
- `task_mode`
- `submode`
- `engine_id` when video
- `duration_target` when video
- `reference_mode`
- `avatar_id`
- `scene_id`
- `copy_angle_id`
- `scale_anchor`
- `compliance_class`
- `status`

### Step 5 — wait for approval
No prompt expansion before the Variant Plan is approved.

---

## Deterministic Expansion Rule

Every approved row must expand into exactly one deterministic job:

- `IMAGE + VIDEO_SUPPORT`
- `IMAGE + SELLING_POSTER`
- `VIDEO + NONE`
- `VIDEO + IMAGE_REFERENCE`
- `VIDEO + VIDEO_REFERENCE`
- `VIDEO + BOSMAX_IMAGE_HANDOFF`

Batch does not invent a new prompt grammar.
Batch dispatches rows into the already approved single-output flow.

---

## Known vs Unknown Product Rule

### Known product
- use registry truth directly
- use stored scale anchor
- use stored compliance class
- use stored dialogue authority

### Unknown product
- build a fallback product card
- mark rows as `GENERATED_FALLBACK`
- separate these rows clearly in the Variant Plan
- allow user approval with warning

---

## Sensitive Product Rule

For sensitive products such as `BOSMAX Herbs / BOSMAX Serum`:
- product truth remains in product registry
- dialogue authority must resolve through:
  - `SCRIPT_REGISTRY_UNIFIED.md`
  - `SCRIPT_VARIANT_LIBRARY.md`
- batch variation may rotate approved stealth families or angle buckets
- batch must not freestyle sensitive-product dialogue outside that authority lane

---

## Batch Output Contract

Every batch run must produce three artifacts:

### 1. `batch_plan`
- `batch_id`
- `request_summary`
- `variant_rows[]`
- `approval_status`

### 2. `batch_prompt_pack`
Each item must include:
- `job_id`
- `prompt_final`
- `task_mode`
- `submode`
- `product_name`
- `variant`
- `engine_id` when video
- `duration_target` when video
- `avatar_lock`
- `product_truth_lock`
- `negative_lock_block`
- `dialogue_authority_resolved` when video
- `source_image_handoff` when produced

### 3. `batch_summary`
- `total_jobs`
- `image_jobs`
- `video_jobs`
- `failed_jobs`
- `blocked_jobs`
- `failure_reasons`
- `products_covered`
- `engines_covered`

---

## Approval Gates

### Gate 1 — intake validation
- product known or fallback accepted
- scale anchor present
- engine valid
- duration valid
- count sane

### Gate 2 — Variant Plan approval
- user approves or edits the plan

### Gate 3 — final packaging audit
- missing prompts
- invalid rows
- missing scale anchors
- unresolved compliance

---

## Batch Size Rule

Recommended rollout:
- 10
- 25
- 50

Do not jump to 200 in one raw run during the early phase.
Safer production scaling:
- `4 x 50`
- `5 x 40`

This makes diagnosis, reruns, and compliance auditing easier.

---

## Out of Scope

- open-ended random variation
- uncontrolled mixed-engine chaos in one simple batch
- uncontrolled mixed-compliance classes without row isolation
- freeform copywriting overrides for sensitive products
- direct prompt emission before Variant Plan approval

---

## Repository Surfaces Expected To Reflect This Spec

- `BOSMAX_DETERMINISTIC_FLOW_v1.md`
- `.claude/CLAUDE.md`
- `.claude/skills/bosmax-bulk-generator.md`
- `README.md`
- `.claude/BOSMAX-LOG.md`
