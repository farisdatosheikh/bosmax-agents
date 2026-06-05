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

## Resolver Source

The Notion Copywriting and Avatar resolver databases must import or sync from the BOSMAX ecosystem source, especially:

- `BOSMAX_PRODUCT_COPYWRITING_LIBRARY_FAMILY_v2.xlsx`
- `BOSMAX_COPYWRITING_ID_RESOLVER_v1.xlsx`
- `registries/copywriting_id_resolver.yaml`
- `BOSMAX_AVATAR_CONTEXT_RESOLVER_v1.xlsx`
- `registries/avatar_context_rotation.yaml`
- `SCRIPT_REGISTRY_UNIFIED.md`
- `SCRIPT_VARIANT_LIBRARY.md`
- `registries/dialogue_budget_corridor.yaml`

## Required Copywriting Resolver Fields

When Notion relates to a `Copywriting ID`, the downstream relation or rollup must pull:

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

## Required Avatar Resolver Fields

When Notion relates to an `Avatar Context ID`, the downstream relation or rollup must pull only:

- `Avatar_Context_ID`
- `Display_Name`
- `Persona_Label`
- `Gender`
- `Age_Range`
- `Silo_Allowed`
- `Product_Family_Allowed`
- `Scene_Label`
- `Mannequin_Label`
- `Camera_Style_Allowed`
- `Status`
- `Safe_Usage_Notes`

When Notion relates to an `Avatar Pool ID`, the downstream relation or rollup must pull only:

- `Pool_ID`
- `Display_Name`
- `Product_Family`
- `Silo`
- `Allowed_Avatar_Context_IDs`
- `Rotation_Mode`
- `No_Repeat_Window`
- `Minimum_Approved_Count`
- `Status`
- `Runtime_Allowed`
- `Safe_Usage_Notes`

## Downstream Rules

- Notion is downstream UI only.
- Default beginner flow = `COMMAND_CENTRE_PLUG_AND_PLAY`.
- Manual copy / avatar edits = `LEGACY_EXPERT_MODE`.
- Manual override posture = `MANUAL_OVERRIDE_REVIEW_ONLY`.
- Copywriting ID relation must resolve ecosystem-approved fields, not freeform Notion copy.
- Avatar Context ID relation must resolve ecosystem-approved persona + wardrobe + mannequin + scene context, not ad hoc operator assembly.
- Avatar Pool ID relation must remain repo-owned rotation logic only.
- Manual override must mark the run as `Needs Compliance Review`.
- STEALTH products must only expose approved `STEALTH` packs unless an operator intentionally sends the run to review.
- DIRECT products must only expose approved `DIRECT` packs unless an operator intentionally sends the run to review.
- Notion must not expose prompt fragment sources, biometric DNA, raw prompt fragments, private source paths, or P&C ecosystem logic.

## Command Centre Beginner View

The default Command Centre beginner copy selector must use:
- `NOTION_COMMAND_CENTRE_COPY_ID_VIEW`

It must not expose:
- `Hook`
- `USP_1`
- `USP_2`
- `USP_3`
- `CTA`

Full copy lines remain trusted-operator / legacy-expert surfaces only.

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
- Manual output blocks such as `AI-Ready Request Manual Output` must paste the exact repo-approved copywriting resolver payload only. Notion operators are not allowed to freestyle replacement lines for this lane.

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
- Do not let Notion become product-routing authority for registered, family-matched, on-the-fly, or review-only states.
- Do not sync `AD_HOC_GENERATED` on-the-fly rows into approved registry views unless a separate repo promotion happens first.

## MWCB Copy Pack Taxonomy Rules

**Taxonomy authority:** `registries/mwcb_copywriting_angle_taxonomy.yaml`

- MWCB Phase 1 copy packs are generated only for:
  - `MWCB-MCA01`
  - `MWCB-MCA03`
  - `MWCB-MCA07`
- A01–A20 in `products/CAP_BURUNG_MINYAK.yaml` are **raw source seeds only** — NOT approved final copy.
- `MCA_ID` and `Compliance_Risk` columns are now required on `PRODUCT_MW_CAP_BURUNG` and `FAMILY_TRAD_REMEDY_OIL`.
- **REVIEW_ONLY rows must not surface to Notion** unless operator explicitly overrides with `Needs Compliance Review` status.
- REVIEW_ONLY MWCB use cases remain blocked even after Phase 1 generation.
- Notion sync remains deferred until after Phase 1 workbook validation for this PR.
- Copy packs derived from REVIEW_ONLY MCAs (MWCB-MCA06) or REVIEW_ONLY use cases must never reach `APPROVED` or `LOCKED` status without independent compliance sign-off.
- Universal on-the-fly routing now lives in `registries/product_copy_router.yaml`, but this PR does not
  push any router fields, on-the-fly requests, or promotion flags into Notion.

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
