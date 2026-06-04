# BOSMAX NOTION COPY PACK HANDOFF v1

## Purpose

This file exists so Claude Cowork can update Notion later without changing BOSMAX source truth.

## Authority Order

1. BOSMAX repo / local ecosystem
2. Workbook and registries inside this repo
3. Notion downstream UI

Notion is **not** allowed to invent copywriting or become the source of truth.

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
