# BOSMAX Batch Prompt Exporter v1

## Purpose

Resolves a batch input YAML into structured prompt rows (CSV / Markdown / JSONL) using the existing `resolver_runtime` contracts without modifying any resolver internals. Designed as a narrow output-layer over the registered product and session-only pipelines.

---

## Supported Workflows

| `product_workflow` | Silo | Copy mode | Avatar pool |
|---|---|---|---|
| `BOSMAX_SERUM_STEALTH` | STEALTH | COPY_FIXED or COPY_ROTATE | `BOSMAX_MALE_STEALTH_POOL_001` |
| `MWCB_DIRECT` | DIRECT | COPY_FIXED or COPY_ROTATE | `MWCB_TRAD_REMEDY_POOL_001` |
| `ON_THE_FLY_SESSION_ONLY` | — | SESSION_ONLY_GENERATE | none |

Pool cross-contamination is fail-closed: a STEALTH workflow cannot use a DIRECT pool and vice versa.

---

## Input Schema (YAML)

### Registered product batch (BOSMAX_SERUM_STEALTH / MWCB_DIRECT)

```yaml
product_workflow:     BOSMAX_SERUM_STEALTH   # or MWCB_DIRECT
batch_count:          20                     # positive integer, required

engine:               GROK
duration:             "10s"
platform:             TikTok
language:             BM

# Choose one copy mode:
copywriting_mode:     AUTO_RESOLVE
copywriting_id:       BOSMAX_SERUM_CP_0001          # COPY_FIXED — same ID all rows
# OR:
copywriting_id_range: "BOSMAX_SERUM_CP_0001..BOSMAX_SERUM_CP_0003"  # COPY_ROTATE
# OR:
copywriting_id_list:  [BOSMAX_SERUM_CP_0001, BOSMAX_SERUM_CP_0002]  # COPY_ROTATE

avatar_pool_id:       BOSMAX_MALE_STEALTH_POOL_001
rotation_rule:        ROUND_ROBIN_NO_REPEAT
```

### Session-only batch (ON_THE_FLY_SESSION_ONLY)

```yaml
product_workflow:   ON_THE_FLY_SESSION_ONLY
batch_count:        5

copywriting_mode:   SESSION_ONLY_GENERATE
registry_writeback: FORBIDDEN               # hard contract — any other value fails closed

engine:             GROK
duration:           "10s"
platform:           TikTok
language:           BM

product_intake:                             # list (one per row) or single dict (repeated)
  - product_name:        "Portable Blender"
    category:            "Kitchen Gadget"
    target_user:         "Busy professionals"
    main_problem_solved: "On-the-go blending"
    main_benefit:        "USB-rechargeable, 30-second blend"
    compliance_class:    LOW               # HIGH / REVIEW_ONLY / RED → BLOCKED_REVIEW_ONLY
```

---

## Output Schema

Each row in the output files contains these columns:

| Column | Description |
|---|---|
| `prompt_id` | Unique row identifier (e.g. `BOSMAX_SERUM_BATCH_0001`) |
| `row_index` | 1-based integer |
| `product_workflow` | Workflow name |
| `product_id` | Registry product ID or `none` |
| `product_name` | Human-readable product name or `none` |
| `copywriting_id` | Resolved copywriting ID or `none` |
| `avatar_context_id` | Resolved avatar context ID or `none` |
| `avatar_pool_id` | Pool used or `none` |
| `engine` | Video engine from input |
| `duration` | Duration from input |
| `platform` | Platform from input |
| `language` | Language from input |
| `route_status` | `REGISTERED_PRODUCT`, `ON_THE_FLY`, or `BLOCKED_REVIEW_ONLY` |
| `final_prompt_text` | Full structured prompt text (or `BLOCKED_REVIEW_ONLY: <reason>`) |

Output files are written to `outputs/batch_prompts/` as:
- `batch_prompts_{WORKFLOW}_{timestamp}.csv`
- `batch_prompts_{WORKFLOW}_{timestamp}.jsonl`
- `batch_prompts_{WORKFLOW}_{timestamp}.md`

---

## Commands

```bash
# Run the exporter on a sample YAML
python scripts/build_batch_video_prompts.py samples/batch/bosmax_serum_stealth_batch.yaml

# Dry run (resolve rows, print summary, do not write files)
python scripts/build_batch_video_prompts.py samples/batch/bosmax_serum_stealth_batch.yaml --dry-run

# Custom output directory
python scripts/build_batch_video_prompts.py samples/batch/mwcb_direct_batch.yaml --output-dir /tmp/export

# Run the exporter validator
python scripts/validate_batch_video_prompt_exporter.py
```

---

## Limitations

- **No new registry structures** — the exporter reads from existing `resolver_runtime` registries only. Do not add product-specific logic here; extend the registries instead.
- **ON_THE_FLY output is session-only** — rows with `route_status: ON_THE_FLY` must never be written back into the approved copywriting or avatar registries.
- **Hook / USP / CTA fields are not exposed** — beginner-facing batch input only accepts the fields listed above. Full copywriting copy pack is resolved internally by `resolver_runtime`.
- **Batch count limit** — no hard cap enforced at the exporter layer, but BOSMAX operator guidance is max 50 rows per run for registered products.
- **No multi-product mixing** — a single batch YAML targets one `product_workflow`. For mixed-product batches, run one YAML per product and concatenate outputs.
- **Blocked rows are included in output** — `BLOCKED_REVIEW_ONLY` rows are written to CSV/JSONL/Markdown with `route_status: BLOCKED_REVIEW_ONLY` so the operator can review and exclude them before use.
