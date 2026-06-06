# BOSMAX Batch Multi-Block Output Contract v1

## Status

```
SUPPORTED_CONTRACT_DESIGN / NOT_IMPLEMENTED_IN_EXPORTER_YET
```

The row shape defined here is the authoritative design for future multi-block batch
output. The current `build_batch_video_prompts.py` exporter emits single-block rows
only. This contract must be implemented before multi-block batch export can be used
in production.

---

## Motivation

A batch of 20 videos at 2 blocks each produces 40 video prompt units. Without a
structured parent/child row design, downstream operators cannot reconstruct which
child blocks belong to which video or in what order to feed them to the engine.

---

## Row Types

### Parent row (one per video in the batch)

| Field | Type | Description |
|---|---|---|
| `prompt_id` | string | E.g. `BOSMAX_SERUM_BATCH_0001` |
| `row_index` | integer | 1-based position in the batch |
| `product_workflow` | string | Workflow identifier |
| `product_id` | string | Registry product ID or `none` |
| `product_name` | string | Human-readable name or `none` |
| `block_count` | integer | Number of child blocks for this video |
| `total_duration` | string | E.g. `"20s"` |
| `engine` | string | Engine ID |
| `platform` | string | Platform |
| `language` | string | Language |
| `parent_copywriting_id` | string | Resolved copywriting ID for the video |
| `parent_avatar_context_id` | string | Resolved avatar context ID for the video |
| `route_status` | string | REGISTERED_PRODUCT / ON_THE_FLY / BLOCKED_REVIEW_ONLY |
| `row_type` | string | `PARENT` |

### Child block row (M rows per parent)

| Field | Type | Description |
|---|---|---|
| `block_prompt_id` | string | E.g. `BOSMAX_SERUM_BATCH_0001_BLK_1` |
| `row_index` | integer | Parent's row_index |
| `block_index` | integer | 1-based block position within the video |
| `block_count` | integer | Total blocks for the parent video |
| `block_duration` | string | Duration of this block, e.g. `"8s"` |
| `total_duration` | string | Total duration for the parent video |
| `engine` | string | Engine ID |
| `platform` | string | Platform |
| `language` | string | Language |
| `block_role` | string | HOOK / BODY / RELIEF / CTA |
| `bridge_in_required` | boolean | true if block_index > 1 |
| `bridge_out_required` | boolean | true if block_index < block_count |
| `identity_reanchor_required` | boolean | Per engine contract (VEO/GOOGLE_FLOW: true for non-first) |
| `product_reanchor_required` | boolean | Per engine contract (VEO/GOOGLE_FLOW: true for non-first) |
| `previous_clip_final_second_state` | boolean | GOOGLE_FLOW FLOW_EXTEND_UI non-first blocks: true |
| `parent_copywriting_id` | string | Inherited from parent row |
| `parent_avatar_context_id` | string | Inherited from parent row |
| `final_block_prompt_text` | string | Full structured prompt for this block |
| `row_type` | string | `CHILD_BLOCK` |

---

## Scale examples

```
20 videos × 2 blocks = 20 parent rows + 40 child block rows = 60 total rows
20 videos × 3 blocks = 20 parent rows + 60 child block rows = 80 total rows
```

---

## Engine-specific block contract notes

### GROK (EXTENSION mode)

- Valid block durations: 6s and 10s only
- Non-final blocks: `bridge_out_required = true`
- Non-first blocks: `bridge_in_required = true`
- Speech must resume within 0.5s–1.0s of seam
- identity_reanchor_required: false (avatar established in Block 1)
- product_reanchor_required: false (product established in Block 1)
- No internal labels (Block 1, Block 2) in prompt text
- No re-introduction or fresh greeting in non-first blocks

### VEO_3_1_LITE (CLIP_CHAIN mode)

- Block duration: 8s API / 7s actual render
- Dialogue budget uses 7s corridor
- Non-first blocks: `bridge_in_required = true`
- All blocks: `identity_reanchor_required = true`
- All blocks: `product_reanchor_required = true`
- All non-first blocks: `requires_frame_bridge = true`

### GOOGLE_FLOW FLOW_EXTEND_UI

- Block duration: 8s
- Non-first blocks: `bridge_in_required = true`
- Non-first blocks: `requires_previous_clip_final_second = true`
- All blocks: `identity_reanchor_required = true`
- All blocks: `product_reanchor_required = true`
- runtime_proof_fields_pending: ["previous_clip_final_second_state"] for multi-block

---

## Block role assignment rules

| block_index | block_count | Typical block_role |
|---|---|---|
| 1 | any | HOOK |
| 2 | 2 | CTA |
| 2 | 3 | BODY |
| 3 | 3 | CTA |
| 2 | 4+ | BODY |
| N-1 | N | RELIEF |
| N | N | CTA |

---

## Output files (future)

When implemented, the exporter will write:
- `batch_multiblock_{WORKFLOW}_{timestamp}.csv` — flat rows (parent + child interleaved)
- `batch_multiblock_{WORKFLOW}_{timestamp}.jsonl` — one JSON object per row
- `batch_multiblock_{WORKFLOW}_{timestamp}.md` — Markdown table

---

## Fail-closed rules

- Child block prompts MUST NOT be emitted without a corresponding parent row
- Block 1 of each video is generated from zero (no bridge-in)
- Block 2+ must declare `[CONTINUES FROM BLOCK N-1]` at the top
- Visual start state of block N = visual end state of block N-1 (LOCKED)
- Dialogue is continuous across blocks — no restart
- `NO_OVERLAY` in Section 9 of every block — hard rule, no exceptions
- BLOCKED_REVIEW_ONLY parent rows produce no child blocks

---

## References

- `docs/prompt_template_readiness_contract_v1.md`
- `registries/video_engine_duration_contracts.yaml`
- `scripts/video_block_plan.py`
- `scripts/validate_video_block_contracts.py`
- `samples/notion/batch_multi_block_templates.yaml`
