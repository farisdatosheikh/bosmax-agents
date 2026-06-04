# BOSMAX EXECUTION KERNEL CONTRACT v1

```
Authority:    BOSMAX Production Kernel
Status:       CANONICAL — all templates, validators, Notion samples, and AI agents defer here
Version:      v1.0
Date:         2026-06-05
Precondition: Every video template, Notion sample, Codex patch, Claude Code generation,
              and ChatGPT output test must pass every gate defined in this document
              before being marked READY or DONE.
```

---

## 1. Purpose

This contract is the top-level execution gate for all BOSMAX video, template, and runtime
work. It exists to prevent recurring primitive failures that occur when scattered authority
files are read selectively or ignored entirely.

**Problems this contract stops:**
- GROK 16s treated as one monolithic prompt instead of 10s + 6s
- VEO/Flow long duration emitted without a verified block contract
- WPS range ignored or dialogue underfilled / silent default applied
- Product scale anchor reused as Hook/Pain/USP/CTA copywriting
- STEALTH copy generated from generic commerce phrases instead of script authority
- Notion sample marked READY while formula/output path is stale
- Multi-block prompts generated without bridge-out / bridge-in
- Block 2 starting with dead air or a fresh greeting
- Avatar identity not re-anchored across blocks
- Product scale drifting in Clip 2 / Block 2
- AI agents claiming DONE without validator proof

This contract does not replace existing authority files. It defines what MUST be true
before any file, template, or AI output is treated as production-ready.

---

## 2. Authority Order

When any two sources conflict, the higher source wins. This order is absolute.

```
1. GitHub repo authority files (HIGHEST)
   ├── BOSMAX_RUNTIME_STATE_MACHINE_v1.md
   ├── BOSMAX_AGENT_HANDOFF_SCHEMA_v1.md
   ├── BOSMAX_SOP_GOVERNOR_v1.md
   ├── .claude/CLAUDE.md
   └── Individual skill files (lowest among repo docs)

2. registries/*.yaml
   ├── video_engine_duration_contracts.yaml
   ├── dialogue_budget_corridor.yaml
   └── stealth_copy_authority_map.yaml

3. Validator scripts (scripts/*.py)
   ├── validate_video_block_contracts.py
   └── validate_copywriting_ecosystem.py

4. Workbook source files
   └── BOSMAX_PRODUCT_COPYWRITING_LIBRARY_FAMILY_v2.xlsx

5. Notion downstream databases / templates

6. Manual output fields

7. AI-generated prose (LOWEST — never self-authorising)
```

**Notion is downstream UI only.**
- Notion may expose dropdowns, relations, rollups, manual output fields, and proof blocks.
- Notion may NOT invent engine math, copywriting, WPS budgets, avatar DNA, or product truth.
- Notion may NOT mark a template or run READY without a validator proof trace from the repo.
- A Notion formula result, rollup summary, or agent claim is not proof. Only a validator
  command with captured output is proof.

---

## 3. Kernel Readiness Gates

Every gate below defines a precondition. If any gate fails, production is blocked.
There are no partial-pass exceptions.

Gates:

| Gate ID                    | Short Name             |
|----------------------------|------------------------|
| G-01 ENGINE_DURATION        | Engine Duration        |
| G-02 EXECUTION_MODE         | Execution Mode         |
| G-03 WPS_DIALOGUE           | WPS Dialogue           |
| G-04 COPY_AUTHORITY         | Copy Authority         |
| G-05 PRODUCT_TRUTH          | Product Truth          |
| G-06 AVATAR_SOURCE          | Avatar Source          |
| G-07 MULTI_BLOCK_SEAM       | Multi-Block Seam       |
| G-08 NOTION_DOWNSTREAM_ONLY | Notion Downstream Only |
| G-09 VALIDATOR_PROOF        | Validator Proof        |
| G-10 SAMPLE_OUTPUT          | Sample Output          |
| G-11 MERGE_PROOF            | Merge Proof            |

---

## 4. ENGINE_DURATION_GATE (G-01)

**Purpose:** Force block plan resolution before any prompt is generated.

**Required inputs:**
- engine_id
- total_duration_seconds

**Pass condition:**
- engine_id exists in `registries/video_engine_duration_contracts.yaml`
- block_durations resolved deterministically (see canonical math below)
- each block duration is within the engine's allowed values

**Fail condition:**
- engine_id not in registry → ABORT
- total_duration_seconds not in engine's valid list → ABORT
- monolithic prompt emitted for a total duration that requires multiple blocks → ABORT
- any GROK block not 6s or 10s → ABORT
- GOOGLE_FLOW treated as ordinary clip-chain math → ABORT

**Current enforcement surface:**
- `registries/video_engine_duration_contracts.yaml` (canonical registry)
- `scripts/video_block_plan.py` (deterministic planner)
- `scripts/validate_video_block_contracts.py` (validator)
- `.claude/CLAUDE.md` ENGINE CONSTRAINT TABLE

**Validator coverage:** YES — for GROK, VEO_3_1, GOOGLE_FLOW, KLING_3_0, SEEDANCE_2_0.

**Notion impact:** Engine math displayed in Notion must originate from this registry.
Block count, block duration, and execution mode may not be edited free-form in Notion.

### Canonical Block Math

**GROK** (BOSMAX operating contract — not a claim about xAI public limits):
```
6s  → [6]
10s → [10]
12s → [6, 6]          ← only valid combination
16s → [10, 6]         ← only valid combination
18s → [6, 6, 6]       ← only valid combination
20s → [10, 10]        ← default
30s → [10, 10, 10]    ← default (alternate 5×6s only on explicit operator request)
```
Forbidden: `8s blocks`, `12s base + extension invented math`, monolithic 12/16/20/30s.

**VEO_3_1.CLIP_CHAIN** (PARTIAL_VERIFIED — BOSMAX READY_CLIP_MODE):
```
8s  → [8]
16s → [8, 8]
24s → [8, 8, 8]
32s → [8, 8, 8, 8]
40s → [8, 8, 8, 8, 8]
48s → [8, 8, 8, 8, 8, 8]
56s → [8, 8, 8, 8, 8, 8, 7]
```
Note: Dialog budget uses 7s per block (actual render), not 8s API value.
Authority: `BOSMAX_VEO31_FLOW_CONTRACT_DECISION_v1.md`.
Not a claim that Google documents these totals as one native monolithic clip.

**VEO_3_1_LITE** — LIVE GAP (see Section 15):
```
Defined in .claude/CLAUDE.md ENGINE CONSTRAINT TABLE: max 8s per block.
Absent from registries/video_engine_duration_contracts.yaml.
Status: UNDOCUMENTED_IN_REGISTRY — see Section 15 for treatment.
Dialog budget per block: use 7s (actual render), not 8s (API value).
```

**KLING_3_0** (VERIFIED / READY):
```
Valid block durations: [3, 5, 10, 15]
Single block only — supports_multi_block: false
```

**SEEDANCE_2_0** (VERIFIED / READY):
```
Valid block durations: [5, 10, 15]
Single block only — supports_multi_block: false
```

**GOOGLE_FLOW.FLOW_EXTEND** (PARTIAL_VERIFIED / MANUAL_REVIEW_ONLY):
```
This is NOT ordinary clip-chain math.
Flow Extend = previous-final-second continuation workflow.
Status: NEEDS_REVIEW — manual-review template only, not production-ready deterministic contract.
Required: Previous Clip Final Second State, Continuity Goal, Identity Reanchor,
          Product Reanchor, Audio Continuity Notes, Frame Bridge Notes.
```

---

## 5. EXECUTION_MODE_GATE (G-02)

**Purpose:** Lock each run to an explicit, named execution mode with defined field requirements.

**Canonical execution modes:**

| Mode                | Engine        | Multi-block | Frame bridge | Prev clip state | Identity/product re-anchor |
|---------------------|---------------|-------------|--------------|-----------------|----------------------------|
| SINGLE_BLOCK        | KLING/SEEDANCE| No          | No           | No              | No                         |
| GROK_EXTENSION      | GROK          | Yes         | No           | No              | Yes (bridge-in / bridge-out)|
| VEO31_CLIP_CHAIN    | VEO_3_1       | Yes         | Yes (24-frame bridge) | No | Yes (every block)          |
| FLOW_EXTEND         | GOOGLE_FLOW   | Yes         | Yes          | Yes (required)  | Yes                        |
| MANUAL_REVIEW_ONLY  | GOOGLE_FLOW   | Review only | Review only  | Review only     | Review only                |

**Pass condition:** execution_mode declared and fields match mode requirements above.

**Fail condition:** execution_mode absent → ABORT. Fields missing for declared mode → ABORT.

**Validator coverage:** YES (via validate_video_block_contracts.py for GROK and VEO_3_1).

**Notion impact:** `Multi-Block Execution Mode` field in `🎬 BOSMAX Video Runs` must match.

---

## 6. WPS_DIALOGUE_GATE (G-03)

**Purpose:** Prevent both underfilled dialogue (dead-air risk) and overfilled dialogue (lip-sync
risk) in BM commercial UGC video.

**Required inputs:**
- language
- pace_class
- total_duration_seconds (and per-block duration for multi-block)

**Pass condition:**
- WPS corridor exists in `registries/dialogue_budget_corridor.yaml`
- final dialogue word count: `target_min_words ≤ count ≤ target_max_words` (TARGET RANGE)
- per-block budget declared for every block in multi-block runs
- copy formula declared (SELL_THROUGH_HPFRC or STORY_HSARC)
- dialogue present for: BM commercial / UGC / TikTok recommendation / household sell-through

**Fail condition:**
- `pure visual`, `WPS: 0`, or `silent default` applied to BM commercial UGC → ABORT
- word_count < minimum_words → UNDERFILLED → ABORT
- word_count > hard_ceiling_words → HARD FAIL → ABORT
- per-block budget not declared for multi-block → ABORT
- copy_formula not declared for BM commercial → ABORT

**WPS corridor status labels:**
- `UNDERFILLED`: count < minimum_words
- `TARGET RANGE`: target_min_words ≤ count ≤ target_max_words
- `OVER SAFE`: safe_max_words < count ≤ hard_ceiling_words
- `HARD FAIL`: count > hard_ceiling_words

**For multi-block:** total duration budget is insufficient. Each block MUST carry its own
per-block budget. Underfilled blocks create dead-air / hallucinated filler risk. Overfilled
blocks create rushed speech / lip sync seam mismatch.

**Validator coverage:** YES — `validate_video_block_contracts.py` checks corridor coverage
and monotonicity for all BM/BRISK_UGC durations. Per-block budget injected by `video_block_plan.py`.

**Notion impact:** `Dialogue Budget`, `Block Dialogue Word Count` fields must reflect registry values,
not ad hoc operator estimates.

---

## 7. COPY_AUTHORITY_GATE (G-04)

**Purpose:** Prevent generic or AI-invented copy from appearing in STEALTH or DIRECT lanes.

**Approved sources:**

For BOSMAX Serum / BOSMAX Herbs STEALTH:
- `SCRIPT_REGISTRY_UNIFIED.md` (primary node: `male_health_vintage_car`)
- `SCRIPT_VARIANT_LIBRARY.md` (primary family: `EGO_01`)
- `registries/stealth_copy_authority_map.yaml` (validation lock)

For DIRECT products (MWCB, Jungle Girl, Maverix):
- `BOSMAX_PRODUCT_COPYWRITING_LIBRARY_FAMILY_v2.xlsx` (DIRECT sheets)
- `SCRIPT_REGISTRY_UNIFIED.md` where applicable

**Pass condition:**
- Every copy slot (Hook, Pain_or_Friction, USP_1–3, CTA) traces to an approved source.
- Source metadata fields present for STEALTH: `Source_Script_Node`, `Source_Variant_Hook_Node`,
  `Source_Variant_Problem_Node`, `Source_Variant_Solution_Node`, `Source_Variant_CTA_Node`.
- Copywriting_Formula ∈ {AIDA, PAS, HSO, HPAS, SAVAGE_HPAS}.
- Lane ∈ {DIRECT, STEALTH} — matches product silo.

**Fail condition:**
- Generic phrases used for BOSMAX Serum STEALTH: `saiz lip balm`, `botol hitam premium`,
  `senang simpan`, `travel-friendly`, or equivalent → ABORT
- Direct pronouns (`saya`, `anda`, `awak`, `kamu`) in STEALTH copy → ABORT
- Medical claims in STEALTH → ABORT
- Scale anchor (e.g., "EXACTLY lip balm size") used as Hook/Pain/USP/CTA → ABORT
- Any source metadata field blank for STEALTH → ABORT

**Scale anchor is product truth, not copywriting.** It lives in `products/*.yaml` and injects
into prompt composition only. It must NOT appear as a copy slot value.

**Validator coverage:** YES — `scripts/validate_copywriting_ecosystem.py` validates workbook STEALTH rows,
authority map integrity, and forbidden copy patterns.

**Notion impact:** `Copy Pack ID` relation must resolve from approved workbook rows only. Manual
override requires `Needs Compliance Review` status.

---

## 8. PRODUCT_TRUTH_GATE (G-05)

**Purpose:** Prevent product identity, scale, and packaging from drifting across blocks or
between image and text inputs.

**Canonical product truth source:** `products/*.yaml` (TIER 1). FASTMOSS workbook (TIER 2).

**Required fields per product/variant:**
- product_id, product_name
- scale_anchor_descriptor (MANDATORY for TikTok platform)
- packaging summary
- visual_truth (for sensitive products)
- image_prompt_locks (for sensitive products)

**Pass condition:**
- product truth resolved from TIER 1 or TIER 2 before any prompt is generated
- scale_anchor_descriptor present for TikTok platform
- product identity, label, packaging, and scale anchor match across every block
- visual uploaded image takes priority over text input and session memory (Priority Rule: Visual > Text > Memory)

**Fail condition:**
- scale_anchor_descriptor null + platform TikTok → WARN then ABORT if not resolved
- product identity from session memory overriding uploaded visual → ABORT
- product substitution (different product appearing in Block 2) → ABORT
- scale drift detected in Block 2 compared to Block 1 → ABORT

**Validator coverage:** NO — no standalone product truth drift validator exists yet.
Currently enforced via CLAUDE.md VISUAL INTAKE GATE and BOSMAX_RUNTIME_STATE_MACHINE_v1.md
STATE_ASSET_ANALYSIS (documentation enforcement only).
Registry-layer validator: `validate_product_truth_drift.py` — created in PR #5.

**Notion impact:** Product truth fields in Notion (packaging, scale anchor) must originate from
`products/*.yaml` entries, not free-typed by operators.

---

## 9. AVATAR_SOURCE_GATE (G-06)

**Purpose:** Prevent registry persona defaults from overriding uploaded avatar images, and ensure
avatar identity persists across all blocks.

**Avatar modes:**

**STANDARD (USER_UPLOAD):**
- Triggered when a human image is uploaded
- Avatar visual DNA extracted directly from uploaded image
- Registry personas (NORA/RIZAL/SARA/AZMAN/etc.) must NOT be substituted
- Priority rule: uploaded avatar visual > persona name in text > registry default

**HYBRID (REGISTRY):**
- Triggered when no avatar image uploaded and persona_id declared
- Avatar prompt fragment loaded from Avatar Registry
- avatar_record.source = "REGISTRY"
- Avatar identity must be re-anchored in every block for multi-block runs

**Pass condition:**
- avatar_record.source declared (USER_UPLOAD or REGISTRY)
- For USER_UPLOAD: visual DNA extracted (gender, ethnicity, wardrobe, hijab, skin tone, posture)
- For REGISTRY: avatar_id valid, prompt fragment loaded
- Multi-block: avatar identity re-anchored every block

**Fail condition:**
- avatar image uploaded but registry persona loaded instead → ABORT
- avatar_record.source null → ABORT
- Multi-block run with no avatar re-anchor declaration → ABORT

**Validator coverage:** PARTIAL — state machine (BOSMAX_RUNTIME_STATE_MACHINE_v1.md)
enforces this at STATE_ASSET_ANALYSIS. No standalone validator.
Future validator needed: `validate_avatar_registry_coverage.py`.

**Notion impact:** Avatar fields in Notion templates must reflect avatar_record.source.
Notion may not default to a registry persona if an image was uploaded.

---

## 10. MULTI_BLOCK_SEAM_GATE (G-07)

**Purpose:** Prevent seam failures between blocks — dead air, fresh greetings, avatar drift,
product scale drift, and dialogue disconnection.

**Required for all non-single-block runs:**

**For GROK extension blocks:**
- Non-final blocks: bridge-out phrase required
- Non-first blocks: bridge-in phrase required
- Speech must resume within 0.5s–1.0s of extension block start
- Opening motion: micro-continuation only (slight tilt, small nod, tiny hand adjustment)
- Forbidden: long silent repositioning, new intro, fresh greeting, dead-air pause
- Operator-facing prompts use `previous clip` language — not internal labels like `Block 1`
- First spoken clause must continue the same semantic thread from the previous clip

**For VEO_3_1.CLIP_CHAIN:**
- Frame bridge required (24-frame temporal bridge)
- Identity re-anchor required every block
- Product re-anchor required every block
- Previous clip first/last frame continuity required
- No fresh setup or silent beauty moment in non-first clips

**For GOOGLE_FLOW.FLOW_EXTEND (MANUAL_REVIEW_ONLY):**
- Previous Clip Final Second State required (exact description of ending frame/motion/audio)
- Continuation goal required
- Identity re-anchor required
- Product re-anchor required
- Audio continuity notes required
- Frame bridge notes required
- Status remains NEEDS_REVIEW — no production-ready deterministic math

**Dialogue metaphor rule:** A spoken metaphor (e.g., "vintage car analogy") must not become
a visual object. Metaphors are audio-layer constructs only.

**Pass condition:** All required seam fields declared and non-null for every non-first block.

**Fail condition:**
- Non-final block without bridge-out → ABORT
- Non-first block without bridge-in → ABORT
- Flow Extend without Previous Clip Final Second State → ABORT
- Block 2 opens with fresh greeting or re-introduction → ABORT
- Dialogue restarts from zero in Block 2 → ABORT

**Validator coverage:**
- GROK: YES (validate_video_block_contracts.py checks bridge-out, bridge-in, speech resume window)
- VEO_3_1.CLIP_CHAIN: YES (validator checks frame bridge, identity/product reanchor per block)
- GOOGLE_FLOW.FLOW_EXTEND: PARTIAL (validator confirms NEEDS_REVIEW status and requires
  previous_clip_final_second_state field, but cannot validate content quality)

**Notion impact:** `Bridge-Out`, `Bridge-In`, `Previous Clip End State`, `Speech Resume Window`,
`Seam Template` fields in `🎞️ BOSMAX Video Run Blocks` are mandatory for non-trivial blocks.

---

## 11. NOTION_DOWNSTREAM_GATE (G-08)

**Purpose:** Prevent Notion from becoming a source-of-truth surface that silently overrides
or replaces repo authority.

**What Notion MAY do:**
- Expose dropdowns for engine, platform, product, avatar, copy pack, status
- Relate to approved registry rows via `Copy Pack ID`
- Show rollups and formula results as read-only visibility aids
- Surface manual output fallback fields for pasting approved prompts
- Carry proof block sections (ENGINE CONTRACT SUMMARY, BLOCK PLAN SUMMARY, OUTPUT TEST REPORT)
- Expose child block records per block for multi-block runs

**What Notion MAY NOT do:**
- Invent engine block math (block durations must come from registry + planner)
- Generate or modify copywriting (Hook, Pain, USP, CTA)
- Declare WPS budgets without registry source
- Carry avatar visual DNA as an invention (must come from uploaded image or registry)
- Mark any run or template READY unless a validator proof is on file
- Use formula result or rollup result as a READY proof substitute
- Allow operators to free-type Lane (DIRECT/STEALTH), formula, or product truth fields

**Notion READY posture rules:**
- `READY` → validator command + output captured + all gates passed
- `NEEDS_REVIEW` → manual override, unverified Flow/VEO long-form, or missing validator run
- `PARTIAL` → some blocks ready, others still being validated

**Pass condition:** Notion surface reflects registry/repo truth. No invented fields.

**Fail condition:** Any READY status in Notion without a corresponding validator proof trace → BLOCK.

**Validator coverage:** NO — currently documentation-enforced only.
Future validator needed: `validate_notion_sample_readiness.py` or a Notion audit checklist.

---

## 12. VALIDATOR_PROOF_GATE (G-09)

**Purpose:** Eliminate "looks good" agent approvals and unsupported READY claims.

**What constitutes proof:**
- A validator command was run (e.g., `python scripts/validate_video_block_contracts.py`)
- The output was captured (showing VALIDATION PASSED or specific FAIL lines)
- The files checked are listed
- Any gaps or PARTIAL statuses are explicitly documented

**What does NOT constitute proof:**
- "I reviewed the file and it looks correct"
- "The logic follows the contract"
- "This matches the expected output"
- A Notion formula result showing a status value
- An AI summary describing what the validator would check

**Pass condition:** Validator run with VALIDATION PASSED output, on the correct branch, against
the actual file state.

**Fail condition:** Any DONE or READY claim without captured validator output → BLOCK.

**Validator coverage:** YES (this gate is self-referential — it requires other validators to pass).

---

## 13. SAMPLE_OUTPUT_GATE (G-10)

**Purpose:** Ensure no template is frozen without a tested, complete output sample.

**Before any template is marked READY, all of the following must exist:**

```
☐ Sample run record exists (parent + child blocks if multi-block)
☐ Block records exist for every block in multi-block runs
☐ Final prompt text exists for every block (not placeholder text)
☐ Compliance check passed for every block prompt
☐ Product truth check passed (scale, packaging, label match)
☐ Avatar check passed (source declared, identity re-anchored if multi-block)
☐ WPS audit passed for every block (dialogue word count in TARGET RANGE)
☐ Bridge-out / bridge-in text present for every seam
☐ Validator command output on file (VALIDATION PASSED)
☐ Notion page proof exists (page body with ENGINE CONTRACT SUMMARY, BLOCK PLAN SUMMARY,
   OUTPUT TEST REPORT)
```

**Validator coverage:** PARTIAL — validator scripts cover structural integrity but not final
prompt text quality or Notion page proof existence.

---

## 14. MERGE_PROOF_GATE (G-11)

**Purpose:** Prevent repo patches from being claimed complete without delivery verification.

**A repo patch is complete only when:**

```
☐ Branch pushed to remote
☐ PR opened OR clear blocker stated (with reason)
☐ Validator scripts run and VALIDATION PASSED captured
☐ No false Mandor claim (do not claim Mandor-Gate PASSED without running the validator)
☐ Merge SHA supplied after merge (not before)
☐ If Notion changed: Notion proof links supplied
☐ If new registries or scripts added: README or authority index updated
```

**Fail condition:** Any of the above absent → patch is INCOMPLETE, not DONE.

**Validator coverage:** Process gate — enforced by this contract and reviewed at merge time.

---

## 15. ENGINE ALIAS COMPLETENESS — VEO_3_1_LITE

**Status: PARTIAL_VERIFIED / READY_CLIP_MODE** (previously LIVE GAP — resolved in PR #4)

`VEO_3_1_LITE` was previously a LIVE GAP: defined in `.claude/CLAUDE.md` ENGINE CONSTRAINT
TABLE but absent from registry, planner, and validator. PR #4 closes this gap.

`VEO_3_1_LITE` is now present in:
- `registries/video_engine_duration_contracts.yaml` — PARTIAL_VERIFIED / READY_CLIP_MODE
- `scripts/video_block_plan.py` — deterministic clip-chain block planning
- `scripts/validate_video_block_contracts.py` — validator coverage with 7s budget assertion

**Contract rules:**

```
API block duration:        8s per request
Actual render duration:    approximately 7s per block
Dialogue budget:           uses 7s actual-render corridor (NOT the 8s API block value)
Multi-block trigger:       target > 8s
Valid totals:              8, 16, 24, 32, 40, 48, 56 seconds
Invalid durations:         rejected by planner (e.g. 14s → ValueError)
```

**Block math:**

```
8s  = [8]
16s = [8, 8]
24s = [8, 8, 8]
32s = [8, 8, 8, 8]
40s = [8, 8, 8, 8, 8]
48s = [8, 8, 8, 8, 8, 8]
56s = [8, 8, 8, 8, 8, 8, 8]
```

**Seam rules (inherits VEO_3_1.CLIP_CHAIN):**
- Frame bridge required on every non-first block
- Identity re-anchor required every block
- Product re-anchor required every block
- First/last frame continuity required

**Authority basis:** Same as VEO_3_1 (PARTIAL_VERIFIED). Clip-chain math validated by
`scripts/validate_video_block_contracts.py`.

**Interim rule removed:** VEO_3_1_LITE runs CAN now receive READY_CLIP_MODE status when
validator proof (`VALIDATION PASSED`) is captured for the run.

---

## 16. Current Enforcement Matrix

| Gate ID | Gate Name              | Repo authority file                                    | Current validator                    | Notion surface                        | Status          |
|---------|------------------------|--------------------------------------------------------|--------------------------------------|---------------------------------------|-----------------|
| G-01    | ENGINE_DURATION        | video_engine_duration_contracts.yaml + CLAUDE.md        | validate_video_block_contracts.py    | Block Duration, Block Count fields    | READY (all engines covered) |
| G-02    | EXECUTION_MODE         | video_engine_duration_contracts.yaml + RUNTIME_SM       | validate_video_block_contracts.py    | Multi-Block Execution Mode field      | PARTIAL         |
| G-03    | WPS_DIALOGUE           | dialogue_budget_corridor.yaml + HARD_ENGINE_CONTRACTS   | validate_video_block_contracts.py    | Dialogue Budget, Word Count fields    | PARTIAL (per-block standalone gap) |
| G-04    | COPY_AUTHORITY         | stealth_copy_authority_map.yaml + SCRIPT_REGISTRY       | validate_copywriting_ecosystem.py    | Copy Pack ID relation                 | READY for BOSMAX Serum STEALTH; PARTIAL globally |
| G-05    | PRODUCT_TRUTH          | products/*.yaml + VISUAL INTAKE GATE in CLAUDE.md       | validate_product_truth_drift.py      | Product fields in Video Runs          | PARTIAL (registry layer validated; prompt-level drift remains docs-only) |
| G-06    | AVATAR_SOURCE          | CLAUDE.md + RUNTIME_STATE_MACHINE_v1.md                 | validate_avatar_registry_coverage.py | Avatar Mode, Avatar Source fields     | PARTIAL (registry layer validated; USER_UPLOAD runtime + Notion mirror remain docs-only) |
| G-07    | MULTI_BLOCK_SEAM       | video_engine_duration_contracts.yaml + SEAM_TEMPLATES   | validate_video_block_contracts.py    | Bridge-Out, Bridge-In, Seam Template  | READY (GROK); PARTIAL (VEO); MANUAL_REVIEW (Flow) |
| G-08    | NOTION_DOWNSTREAM_ONLY | NOTION_COPY_PACK_HANDOFF + NOTION_MULTI_BLOCK_HANDOFF   | None (docs-only)                     | Block Status, READY posture fields    | PARTIAL         |
| G-09    | VALIDATOR_PROOF        | This contract + validate_*.py                           | validate_execution_kernel_contract.py (new) | QA Notes, proof block sections | PARTIAL         |
| G-10    | SAMPLE_OUTPUT          | NOTION_MULTI_BLOCK_HANDOFF + sample run specs           | None (docs-only)                     | Block Status, page proof sections     | PARTIAL         |
| G-11    | MERGE_PROOF            | This contract                                           | Process review                       | N/A                                   | PROCESS GATE    |

---

## 17. Required Next Validators

These validators do not yet exist. They must be created to close open PARTIAL statuses.

| Validator                               | Gate covered | Priority |
|-----------------------------------------|--------------|----------|
| ~~`validate_product_truth_drift.py`~~   | G-05         | CLOSED — PR #5 |
| ~~`validate_avatar_registry_coverage.py`~~ | G-06      | CLOSED — PR #7 |
| `validate_notion_sample_readiness.py`   | G-08, G-10   | MEDIUM   |
| `validate_wps_per_block.py`             | G-03         | MEDIUM   |
| `validate_flow_extend_proof.py`         | G-07         | LOW (manual review only posture retained) |

**Closed (no longer required):**
- `validate_execution_kernel_contract.py` — G-09 — created in PR #3
- VEO_3_1_LITE registry + validator — G-01, G-02 — VEO_3_1_LITE parity closed in PR #4
- `validate_product_truth_drift.py` — G-05 — registry-layer validator created in PR #5
- `validate_avatar_registry_coverage.py` — G-06 — registry-layer validator created in PR #7

---

## 18. Operational Law For AI Agents

Applies to: Codex, Claude Code, ChatGPT, any AI operating on this repo.

```
BEFORE generating any prompt, template, or output:
  ☐ Confirm engine_id is in registries/video_engine_duration_contracts.yaml
  ☐ Run scripts/video_block_plan.py for the target engine and duration
  ☐ Confirm block count and durations from planner output — do not invent
  ☐ Confirm WPS budget per block from dialogue_budget_corridor.yaml
  ☐ Confirm copy source from stealth_copy_authority_map.yaml (STEALTH) or workbook (DIRECT)
  ☐ Confirm product truth from products/*.yaml
  ☐ Confirm avatar source declared

BEFORE marking any file, template, or sample DONE or READY:
  ☐ Run validate_video_block_contracts.py and capture output
  ☐ Run validate_copywriting_ecosystem.py and capture output (if copy changed)
  ☐ Both must show VALIDATION PASSED
  ☐ Branch must be pushed to remote
  ☐ PR must be open or merge SHA supplied

DISCOVERY RULE:
  Do not ask the user to spoon-feed primitive engine rules or copy authority rules
  if the authority file already exists in this repo. Read the file. Apply the rule.

FAIL-CLOSED DEFAULT:
  If unsure whether a gate passes: mark NEEDS_REVIEW, not READY.
  Do not claim DONE if any gate is unvalidated.

NO GENERIC APPROVAL:
  Do not emit "looks good" or "this follows the contract" as a proof substitute.
  If a validator was not run: say "VALIDATOR NOT RUN — status is UNVERIFIED."
```

---

## 19. Fail-Closed Rules — Hard List

These conditions always block output. No exceptions, no workarounds.

```
ENGINE_DURATION:
  ☐ engine_id not in video_engine_duration_contracts.yaml → ABORT
  ☐ total_duration not valid for engine → ABORT
  ☐ monolithic prompt for multi-block required duration → ABORT
  ☐ any GROK block ≠ 6s or 10s → ABORT
  ☐ GOOGLE_FLOW treated as ordinary clip-chain math → ABORT
  ☐ VEO_3_1_LITE run claiming READY without registry entry → BLOCK

WPS / DIALOGUE:
  ☐ BM commercial UGC video with zero dialogue (unless explicit user request) → ABORT
  ☐ word_count < minimum_words → ABORT (UNDERFILLED)
  ☐ word_count > hard_ceiling_words → ABORT (HARD FAIL)
  ☐ copy_formula not declared for BM commercial → ABORT
  ☐ per-block budget not declared for multi-block → ABORT

COPY AUTHORITY:
  ☐ BOSMAX Serum STEALTH row with blank source metadata → ABORT
  ☐ generic packaging phrase in STEALTH copy slot → ABORT
  ☐ direct pronoun in STEALTH copy → ABORT
  ☐ medical claim in STEALTH copy → ABORT
  ☐ scale anchor text used as Hook/Pain/USP/CTA → ABORT

PRODUCT TRUTH:
  ☐ product substitution between blocks → ABORT
  ☐ scale drift detected between Block 1 and Block 2 → ABORT
  ☐ session memory product overriding uploaded visual product → ABORT

AVATAR SOURCE:
  ☐ avatar image uploaded but registry persona substituted → ABORT
  ☐ avatar_record.source null → ABORT

MULTI-BLOCK SEAM:
  ☐ non-final block without bridge-out → ABORT
  ☐ non-first block without bridge-in → ABORT
  ☐ Block 2 opens with fresh greeting or re-introduction → ABORT
  ☐ Flow Extend without Previous Clip Final Second State → ABORT
  ☐ dialogue restarts from zero in Block 2 → ABORT
  ☐ dialogue metaphor becomes visual object → ABORT

NOTION / READY CLAIMS:
  ☐ Notion READY status without validator proof → BLOCK
  ☐ formula result or rollup treated as proof → BLOCK
  ☐ VEO/Flow marked READY beyond evidence authority → BLOCK

AGENT / MERGE:
  ☐ DONE claimed without validator VALIDATION PASSED → BLOCK
  ☐ PR or branch SHA absent from merge report → BLOCK
  ☐ false Mandor-Gate PASSED label without running validator → BLOCK
```

---

## 20. Relationship To Existing Authority Files

This contract defines WHEN other authority files are consulted, not WHAT they say.
Existing authority files remain canonical for their domain.

| This contract section | Defers to                                              |
|-----------------------|--------------------------------------------------------|
| Engine duration math  | registries/video_engine_duration_contracts.yaml        |
| WPS corridors         | registries/dialogue_budget_corridor.yaml               |
| STEALTH copy rules    | registries/stealth_copy_authority_map.yaml             |
| Runtime state machine | BOSMAX_RUNTIME_STATE_MACHINE_v1.md                     |
| GROK seam templates   | BOSMAX_GROK_EXTENSION_SEAM_TEMPLATES_v1.md             |
| VEO/Flow decision     | BOSMAX_VEO31_FLOW_CONTRACT_DECISION_v1.md              |
| Notion handoff rules  | BOSMAX_NOTION_MULTI_BLOCK_VIDEO_HANDOFF_v1.md          |
| Copy pack rules       | BOSMAX_NOTION_COPY_PACK_HANDOFF_v1.md                  |
| Compliance audit      | .claude/skills/bosmax-compliance-gate.md               |
| Product registry      | products/*.yaml                                        |

**Priority when conflict exists:**
1. This contract (Kernel Contract)
2. BOSMAX_RUNTIME_STATE_MACHINE_v1.md
3. BOSMAX_AGENT_HANDOFF_SCHEMA_v1.md
4. .claude/CLAUDE.md
5. Individual skill files
