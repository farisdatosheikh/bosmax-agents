# BOSMAX AGENT HANDOFF SCHEMA v1
# Authority: BOSMAX Production Kernel
# Authors: Codex + Claude Cowork (shake-hand consensus)
# Status: CANONICAL — defines all inter-worker packet contracts
# Version: v1.0 | Date: 2026-06-03

---

## 1. PURPOSE

Every worker in the BOSMAX pipeline communicates exclusively through typed packets.

No prose handoff.
No memory-based assumptions.
No partial packets.

If a required field is null, the packet is INVALID. The session does not advance.

---

## 2. BASE PACKET STRUCTURE

All packets share this base:

```yaml
_base:
  schema_version:     "v1"            # must match current governor version
  packet_type:        string          # name of this packet type
  packet_id:          string          # session_id + "_" + packet_type
  producer:           string          # worker name that created this
  consumer:           string          # worker name that will consume this
  status:             PENDING         # PENDING | VALID | INVALID | ABORTED
  produced_at:        timestamp
  validation_errors:  []              # list of field-level errors
  abort_reason:       null            # populated if status = ABORTED
```

---

## 3. PACKET DEFINITIONS

---

### 3.1 intake_packet

**Producer:** Kernel
**Consumer:** Asset Intelligence Worker (if assets present) OR Route Resolver Worker

```yaml
intake_packet:
  # BASE
  schema_version:     "v1"
  packet_type:        "intake_packet"
  producer:           "kernel"
  consumer:           "asset_intelligence_worker | route_resolver_worker"
  status:             PENDING

  # REQUIRED
  raw_request:        string          # verbatim user input text
  detected_assets:                    # list of uploaded items
    - asset_id:       string
      asset_type:     IMAGE | VIDEO | FRAMES
      file_ref:       string          # reference to actual upload
  detected_modality_hint: null        # IMAGE | VIDEO | UNKNOWN — from text analysis
  platform_hint:      null            # TikTok | Shopee | Lazada | Meta | YouTube | null
  language_hint:      null            # Malay | English | null

  # DERIVED
  has_assets:         boolean         # true if detected_assets non-empty
  repair_mode:        false           # true if user is asking to fix a bad prompt
```

**Validity rule:** `raw_request` must be non-null. Status = VALID when all required fields resolved.

---

### 3.2 visual_truth_packet

**Producer:** Asset Intelligence Worker
**Consumer:** Route Resolver Worker, Storyboard Director Worker, Composition Director Worker, Prompt Compiler Worker, Compliance Auditor Worker

```yaml
visual_truth_packet:
  # BASE
  schema_version:     "v1"
  packet_type:        "visual_truth_packet"
  producer:           "asset_intelligence_worker"
  consumer:           "route_resolver_worker + storyboard_director_worker + prompt_compiler_worker + compliance_auditor_worker"
  status:             PENDING

  # SCAN METADATA
  assets_scanned:     integer         # must match len(intake_packet.detected_assets)
  scan_completeness:  FULL | PARTIAL | FAILED

  # AVATAR RECORDS (one per human detected)
  avatar_records:
    - avatar_index:   integer
      source:         USER_UPLOAD      # ALWAYS USER_UPLOAD when image provided
      locked:         true             # IMMUTABLE after this packet
      visual_dna:
        gender:               string
        ethnicity:            string   # read from visual, not assumed
        age_range:            string
        skin_tone:            string
        hijab:                boolean
        hijab_color:          string | null
        wardrobe_top:         string
        wardrobe_bottom:      string
        accessories:          []
        expression:           string
        posture:              string
        frame_position:       string   # e.g. "center, medium shot"

  # PRODUCT RECORDS (one per product detected)
  product_records:
    - product_index:  integer
      name_from_label:        string   # exact text from label in image
      brand_from_label:       string | null
      registry_status:        FOUND | NOT_FOUND | PARTIAL | UNCLEAR
      registry_match:         null | string  # product_id if FOUND
      packaging_summary:
        shape:        string
        color_primary:        string
        material_hint:        string | null
        closure_type:         string | null  # cap, stopper, roller, pump
      scale_estimate: string           # relative to hand/body, e.g. "both-hands brick-size"
      label_text_visible:     []       # list of text strings read from label
      sandbox_stub:           null | object  # populated if NOT_FOUND but label clear

  # SETTING
  scene_context:
    environment:      string           # indoor/outdoor
    lighting_class:   string           # bright/natural/moody/dark
    background_desc:  string

  # AMBIGUITY FLAG
  ambiguous_items:    []               # items needing user clarification before proceeding
```

**Validity rule:** `assets_scanned > 0`, at least one product_record or avatar_record resolved. Status = VALID when scan complete and ambiguous_items empty.

**Immutability rule:** Once status = VALID, no downstream worker may modify this packet.

---

### 3.3 route_decision_packet

**Producer:** Route Resolver Worker
**Consumer:** Engine Planner Worker (VIDEO) OR Composition Director Worker (IMAGE)

```yaml
route_decision_packet:
  # BASE
  schema_version:     "v1"
  packet_type:        "route_decision_packet"
  producer:           "route_resolver_worker"
  consumer:           "engine_planner_worker | composition_director_worker"
  status:             PENDING

  # REQUIRED
  task_mode:          IMAGE | VIDEO
  content_type:       UGC | PGC | HYBRID
  route:              A | B | C | D | REG | BULK | REPAIR
  risk_class:         DIRECT | SENSITIVE | HOUSEHOLD | TRADITIONAL | WELLNESS
  platform:           string
  language:           string

  # VIDEO-SPECIFIC
  reference_mode:     null | NONE | IMAGE_REFERENCE | VIDEO_REFERENCE | BOSMAX_IMAGE_HANDOFF

  # IMAGE-SPECIFIC
  image_goal:         null | VIDEO_SUPPORT | SELLING_POSTER
```

**Validity rule:** `task_mode`, `route`, `platform`, `language` must all be non-null.

---

### 3.4 engine_plan_packet

**Producer:** Engine Planner Worker
**Consumer:** Storyboard Director Worker, Prompt Compiler Worker, Compliance Auditor Worker

```yaml
engine_plan_packet:
  # BASE
  schema_version:     "v1"
  packet_type:        "engine_plan_packet"
  producer:           "engine_planner_worker"
  consumer:           "storyboard_director_worker + prompt_compiler_worker + compliance_auditor_worker"
  status:             PENDING

  # REQUIRED
  engine_id:          VEO_3_1_LITE | VEO_3_1 | KLING_3_0 | SEEDANCE_2_0 | GROK | GOOGLE_FLOW
  engine_mode:        T2V | FRAMES | INGREDIENTS | IMAGE | EXTENSION
  duration_total:     integer     # seconds
  block_count:        integer
  block_durations:    []          # e.g. [10, 6] for GROK 16s

  # WPS BUDGET (one entry per block)
  wps_budget_per_block: []        # e.g. [25, 15] words max per block (BM @ 2.5 WPS)

  # PACING
  pace_class:         BRISK_UGC | NATURAL_COMMERCIAL | CALM_EXPLAINER

  # CONTENT MODE
  content_mode:       T2V | FRAMES | INGREDIENTS | IMAGE

  # ENGINE NOTES
  engine_notes:       string      # e.g. "VEO_3_1_LITE: actual render 7s despite API 8s"
```

**Validity rule:** All required fields non-null. `block_durations` length must equal `block_count`. Each value in `block_durations` must be valid for the engine.

**GROK hard rules:**
- Each value in `block_durations` must be 6 or 10 only.
- No other values permitted regardless of user request.

---

### 3.5 storyboard_packet

**Producer:** Storyboard Director Worker
**Consumer:** Prompt Compiler Worker, Compliance Auditor Worker, Final Emitter Worker

```yaml
storyboard_packet:
  # BASE
  schema_version:     "v1"
  packet_type:        "storyboard_packet"
  producer:           "storyboard_director_worker"
  consumer:           "prompt_compiler_worker + compliance_auditor_worker + final_emitter_worker"
  status:             PENDING

  # USER APPROVAL GATE
  user_approved:      false       # Kernel sets true after user confirms
  user_approved_at:   null

  # COPY STRUCTURE
  copy_formula:       SELL_THROUGH_HPFRC | STORY_HSARC
  presentation_route: UGC | PGC | HYBRID
  full_dialogue_arc:  string      # complete dialogue across all blocks, continuous

  # BLOCKS (one per block)
  blocks:
    - block_number:   integer
      block_duration: integer     # seconds — must match engine_plan_packet
      shot_ladder:    []          # e.g. ["ECU product", "CU face", "MCU product-in-hand"]
      dialogue_slice: string      # this block's portion of full_dialogue_arc
      word_count:     integer     # must be ≤ wps_budget_per_block[block_number - 1]
      product_moment_timing: string  # e.g. "at 3s, product held up to camera"
      copy_arc_beat:  string      # e.g. "Hook", "Pain", "Friction", "Relief+Proof", "CTA"
      bridge_out:     null | string  # closing phrase connecting to next block
      bridge_in:      null | string  # opening phrase resuming from previous block
      end_state_visual: string    # exact visual description at end of block
```

**Validity rule:** `copy_formula`, `full_dialogue_arc` non-null. Each block's `word_count ≤ wps_budget`. `user_approved = true` before status becomes VALID for downstream.

**Immutability rule:** Once user_approved = true, no worker may modify this packet.

---

### 3.6 composition_packet

**Producer:** Poster Composition Director Worker
**Consumer:** Prompt Compiler Worker, Compliance Auditor Worker

```yaml
composition_packet:
  # BASE
  schema_version:     "v1"
  packet_type:        "composition_packet"
  producer:           "composition_director_worker"
  consumer:           "prompt_compiler_worker + compliance_auditor_worker"
  status:             PENDING

  # REQUIRED
  platform:           string
  image_goal:         VIDEO_SUPPORT | SELLING_POSTER

  # VISUAL HIERARCHY
  product_position:   string      # e.g. "center foreground, dominant"
  avatar_position:    string | null
  background_class:   string

  # COPY HIERARCHY
  headline:           string
  subhead:            string | null
  cta_text:           string

  # LOCKS
  scale_anchor:       string      # from visual_truth_packet
  negative_locks:     []          # platform-specific negative constraints
```

---

### 3.7 prompt_blocks_packet

**Producer:** Prompt Compiler Worker
**Consumer:** Compliance Auditor Worker, Final Emitter Worker

```yaml
prompt_blocks_packet:
  # BASE
  schema_version:     "v1"
  packet_type:        "prompt_blocks_packet"
  producer:           "prompt_compiler_worker"
  consumer:           "compliance_auditor_worker + final_emitter_worker"
  status:             PENDING

  # REQUIRED
  task_mode:          IMAGE | VIDEO
  engine_id:          string
  block_count:        integer

  # PROMPT BLOCKS
  prompt_blocks:
    - block_number:   integer
      block_duration: integer | null   # null for IMAGE
      raw_prompt_text: string          # the actual prompt content
      word_count_dialogue: integer     # words in spoken dialogue (VIDEO)
      overlay_flag:   NO_OVERLAY       # MUST be NO_OVERLAY unless operator explicitly requested overlay planning
      internal_scaffolding_present: false  # must be false before emission
```

**Validity rule:** Each `overlay_flag` must be `NO_OVERLAY`. `internal_scaffolding_present` must be false. `raw_prompt_text` non-empty for all blocks.

---

### 3.8 compliance_report_packet

**Producer:** Compliance Auditor Worker
**Consumer:** Final Emitter Worker (on PASS) OR Kernel (on ABORT)

```yaml
compliance_report_packet:
  # BASE
  schema_version:     "v1"
  packet_type:        "compliance_report_packet"
  producer:           "compliance_auditor_worker"
  consumer:           "final_emitter_worker | kernel"
  status:             PENDING

  # VERDICT
  verdict:            PASS | FAIL_HEALABLE | ABORT

  # AUDIT RESULTS
  checks_total:       integer
  checks_passed:      integer
  checks_failed:      integer

  failed_checks:      []          # list of failed check IDs
  healed_checks:      []          # list of auto-healed check IDs with heal action

  # ABORT DETAILS
  abort_reason:       null | string
  abort_stage:        null | string    # which state to route back to if healable
```

---

### 3.9 final_output_packet

**Producer:** Final Emitter Worker
**Consumer:** Kernel (for release to user)

```yaml
final_output_packet:
  # BASE
  schema_version:     "v1"
  packet_type:        "final_output_packet"
  producer:           "final_emitter_worker"
  consumer:           "kernel"
  status:             PENDING

  # REQUIRED
  output_shape:       CHATGPT_CLEAN_VIDEO | CHATGPT_CLEAN_IMAGE
  sections:
    visual_scan_summary:   string
    engine_contract:       string     # VIDEO only
    storyboard:            string     # VIDEO only
    composition_summary:   string     # IMAGE only
    prompt_blocks:         []         # one entry per block

  # INTEGRITY
  metadata_leaked:    false           # must be false
  internal_labels_present: false      # must be false
  ready_for_release:  false           # Kernel sets true
```

---

## 4. PACKET FLOW DIAGRAM

```
Kernel
  → [intake_packet]
  → Asset Intelligence Worker
  → [visual_truth_packet]
  → Route Resolver Worker
  → [route_decision_packet]
  ↓
  VIDEO lane:
    → Engine Planner Worker
    → [engine_plan_packet]
    → Storyboard Director Worker
    → [storyboard_packet] ← USER APPROVAL GATE
    → Prompt Compiler Worker
    → [prompt_blocks_packet]

  IMAGE lane:
    → Composition Director Worker
    → [composition_packet]
    → Prompt Compiler Worker
    → [prompt_blocks_packet]
  ↓
  → Compliance Auditor Worker
  → [compliance_report_packet]
  → Final Emitter Worker
  → [final_output_packet]
  → Kernel → USER
```

---

## 5. SCHEMA VERSIONING

Current version: `v1`

When schema changes:
- increment version in `BOSMAX_SOP_GOVERNOR_v1.md`
- update all affected packet definitions
- mark old field names as DEPRECATED with migration note
- existing sessions using old schema are grandfathered until session closes

---

## 6. PACKET IMMUTABILITY RULES

| Packet | Immutable after |
|---|---|
| `visual_truth_packet` | status = VALID |
| `route_decision_packet` | status = VALID |
| `engine_plan_packet` | status = VALID |
| `storyboard_packet` | user_approved = true |
| `composition_packet` | status = VALID |

Downstream workers that receive an immutable packet MUST NOT modify it. They may only read it.
