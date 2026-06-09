---
name: bosmax-dialogue-wps-enforcer
description: >
  BOSMAX dialogue WPS hard gate. Invoke before final video prompt output for
  any spoken-dialogue lane so underfilled or over-ceiling dialogue never
  reaches the clean operator-facing prompt.
---

# BOSMAX DIALOGUE WPS ENFORCER — SKILL
## Role: Universal pre-output dialogue corridor gate
## Schema: v1 | Authority: SUPREME_SYSTEMS_ARCHITECT

---

## TRIGGER

Run this skill **before final video prompt output** whenever `dialogue_required = YES`.
This applies to all video engines, not only GROK:

- GROK
- GOOGLE_FLOW / FLOW_EXTEND_UI
- VEO
- KLING
- SEEDANCE
- any future BOSMAX video engine with spoken dialogue

---

## INPUT

```
engine_id
total_duration_seconds
block_plan
block_duration
language
pace_class
dialogue_required
candidate_dialogue_by_block
```

`candidate_dialogue_by_block` is the exact spoken line draft for each block before final prompt assembly.

---

## ENFORCEMENT STEPS

1. Resolve the active block plan from `registries/video_engine_duration_contracts.yaml`.
2. Resolve the matching per-block corridor from `registries/dialogue_budget_corridor.yaml`.
3. Count words for each candidate dialogue block.
4. Mark block status:
   - `UNDERFILLED`
   - `TARGET_RANGE`
   - `OVER SAFE`
   - `HARD FAIL`
5. If any block is `UNDERFILLED`, rewrite internally before final output.
6. If any block exceeds the `hard ceiling`, rewrite internally before final output.
7. Final prompt can only receive the exact approved dialogue line after every block passes corridor audit.

---

## OUTPUT

```
PASS
REWRITE_REQUIRED
BLOCKED
```

- `PASS` = every block passed and the final prompt may receive the exact approved dialogue line
- `REWRITE_REQUIRED` = at least one block is recoverable but still needs rewrite
- `BLOCKED` = final output must stop because a required dialogue block remains invalid

---

## ROUTE LAW

For TikTok Shop Malaysia UGC videos with `dialogue_required = YES` and total duration above 10 seconds:

- default route = `AVATAR_PRODUCT_UGC`
- product-only / no-avatar route allowed only on explicit operator request, 6s CTA close, silent route, or avatar-free image-to-video continuation

---

## FINAL PROMPT LAW

The final clean prompt must stay operator-facing and natural.
Do not expose WPS metadata, validator proof, per-block tables, or hidden budget labels in the prompt body.
Only the exact approved dialogue line may be forwarded into final prompt assembly.
