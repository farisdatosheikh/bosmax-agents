# BOSMAX NOTION COPY PACK HANDOFF v1

## Purpose

This file exists so Claude Cowork can update Notion later without changing BOSMAX source truth.

## Authority Order

1. `BOSMAX_EXECUTION_KERNEL_CONTRACT_v1.md` ← top-level gate (COPY_AUTHORITY_GATE G-04)
2. BOSMAX repo / local ecosystem
3. Workbook and registries inside this repo
4. Notion downstream UI

Notion is **not** allowed to invent copywriting or become the source of truth.
All template READY claims must pass BOSMAX_EXECUTION_KERNEL_CONTRACT_v1.md before being marked production-ready.

## Copy Pack Source

The Notion Copywriting Pack Registry must import or sync from the BOSMAX ecosystem source, especially:

- `BOSMAX_PRODUCT_COPYWRITING_LIBRARY_FAMILY_v2.xlsx`
- `SCRIPT_REGISTRY_UNIFIED.md`
- `SCRIPT_VARIANT_LIBRARY.md`
- `registries/dialogue_budget_corridor.yaml`

## Required Copy Pack Fields

When Notion relates to a `Copy Pack ID`, the downstream relation or rollup must pull:

- `Angle`
- `Hook`
- `Pain_or_Friction`
- `USP_1`
- `USP_2`
- `USP_3`
- `CTA`
- `Copywriting_Formula`
- `Silo_Key`
- `Lane`
- `Status`

`Lane` must follow the ecosystem truth (`DIRECT` or `STEALTH`). Do not let operators free-type a new lane in Notion.

## Downstream Rules

- Notion is downstream UI only.
- Copy Pack ID relation must resolve ecosystem-approved fields, not freeform Notion copy.
- Manual override must mark the run as `Needs Compliance Review`.
- STEALTH products must only expose approved `STEALTH` packs unless an operator intentionally sends the run to review.
- DIRECT products must only expose approved `DIRECT` packs unless an operator intentionally sends the run to review.

## Hard Rules For BOSMAX Serum / BOSMAX Herbs STEALTH

- `BOSMAX_SERUM` and BOSMAX Herbs aliases must resolve copywriting from:
  - `SCRIPT_REGISTRY_UNIFIED.md`
  - `SCRIPT_VARIANT_LIBRARY.md`
  - `registries/stealth_copy_authority_map.yaml`
- Do not let Notion reuse product scale anchors, packaging convenience, or carry-size descriptors as `Hook`, `Pain_or_Friction`, `USP_1`, `USP_2`, `USP_3`, or `CTA`.
- Required row provenance for these STEALTH packs:
  - `Source_Script_Node`
  - `Source_Variant_Hook_Node`
  - `Source_Variant_Problem_Node`
  - `Source_Variant_Solution_Node`
  - `Source_Variant_CTA_Node`
- If any one of those provenance fields is blank, the Notion row is invalid and must be treated as `Needs Compliance Review`.
- Do not accept generic convenience copy such as `saiz lip balm`, `botol hitam premium`, `senang simpan`, `travel-friendly`, or equivalent wording for BOSMAX Serum STEALTH packs.
- Do not accept formal direct pronouns (`saya`, `anda`, `awak`, `kamu`) in BOSMAX Serum STEALTH copy packs.
- Do not accept medical claims in downstream STEALTH copy packs.
- Manual output blocks such as `AI-Ready Request Manual Output` must paste the exact repo-approved copy pack fields only. Notion operators are not allowed to freestyle replacement lines for this lane.

## Dialogue Budget Corridor

The Dialogue Budget Corridor must also be imported or synced from repo source:

- `registries/dialogue_budget_corridor.yaml`

Notion WPS / dialogue check must compare final dialogue word count against:

- `minimum_words`
- `target_min_words`
- `target_max_words`
- `safe_max_words`
- `hard_ceiling_words`

If dialogue is below `minimum_words`, the system should recommend:

1. expand dialogue
2. reduce duration
3. add intentional visual proof beats

## Required Notion Status Outputs

The Notion downstream view should show:

- `UNDERFILLED`
- `TARGET RANGE`
- `OVER SAFE`
- `HARD FAIL`

## Compliance Posture

- Do not let Notion generate new copy packs as if they were approved source rows.
- Do not let Notion infer STEALTH vs DIRECT from operator memory.
- Do not leave `Pain_or_Friction` only in Notion.
- Do not leave dialogue budget logic only in Notion.

## Flow Extend Proof Authority

Flow Extend proof is governed by `scripts/validate_flow_extend_proof.py` and `registries/flow_extend_proof.yaml`.

Rules:
- Flow Extend requires previous-final-second continuation proof. It is not ordinary 8+8 clip-chain math.
- FLOW_EXTEND remains MANUAL_REVIEW_ONLY until proof fields are complete.
- Formula result handles and omitted rollups are not proof.

## Per-Block WPS Authority

Per-block WPS is validated by `scripts/validate_wps_per_block.py`.

Rules:
- Multi-block outputs must not use total-duration WPS only.
- GROK 16s uses separate 10s and 6s budgets.
- VEO_3_1_LITE 8s API blocks use 7s actual-render dialogue budget.
- GOOGLE_FLOW.FLOW_EXTEND remains MANUAL_REVIEW_ONLY.

## Sample Readiness Authority

Notion sample READY status must be backed by `registries/notion_sample_readiness.yaml`.

`formulaResult://...` and `<omitted />` rollups are not accepted as proof.
Live Notion pages remain downstream UI. `GOOGLE_FLOW.FLOW_EXTEND` remains `MANUAL_REVIEW_ONLY`.

Validator: `scripts/validate_notion_sample_readiness.py`
