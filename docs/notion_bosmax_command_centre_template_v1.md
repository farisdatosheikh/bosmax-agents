# BOSMAX Command Centre Notion Template v1

## Purpose

This document defines the **default BOSMAX Command Centre Plug & Play Notion page**.

Default audience:
- beginner operator
- newbie operator
- high-speed operator

These users should not need to understand:
- internal copywriting architecture
- avatar resolver internals
- mannequin / wardrobe / scene context composition
- backend compliance and runtime logic

Repo/backend remains source truth.
Notion remains downstream UI only.

---

## Page Structure

`BOSMAX Command Centre`

1. `Plug & Play Video Prompt Template`
2. `Product Workflows`
3. `Copywriting ID Mini Database`
4. `Avatar Context ID Mini Database`
5. `Avatar Pool ID Mini Database`
6. `Batch Production Template`
7. `Legacy Expert Mode / Manual Override Notice`
8. `Operator Rules`

---

## 1. Plug & Play Video Prompt Template

This is the default single prompt template for beginner operators:

```yaml
Platform: TikTok
Mode: B
Engine: VEO_3_1_LITE
Duration: 8s
Submode formula: SAVAGE_HPAS
Silo: STEALTH
Avatar Context ID: BOSMAX_AVP_0001
Avatar Mode: AUTO_RESOLVE
Camera style: UGC_IPHONE_RAW
Language: Malay
Produk: BOSMAX Serum 5ML
Scale anchor: EXACTLY lip balm size, fit into fingers naturally
Physics class: CLASS_A
Copywriting ID: BOSMAX_SERUM_CP_0001
Copywriting Mode: AUTO_RESOLVE
Compliance: STEALTH_METAPHOR_REQUIRED
```

Command Centre default rule:
- user selects approved IDs only
- user does not manually type Hook / USP / CTA / Avatar / Mannequin / Wardrobe / Scene

---

## 2. Product Workflows

Registered-product and session-only workflows must remain explicit:

### BOSMAX Serum / STEALTH Registered Product

```yaml
Workflow: BOSMAX Serum / STEALTH Registered Product
Copywriting View: NOTION_COMMAND_CENTRE_BOSMAX_STEALTH_COPY_ID_VIEW
Workbook Alias: CC_BSMX_ST_COPY
Copywriting ID: BOSMAX_SERUM_CP_0001
Copywriting Mode: AUTO_RESOLVE
Avatar Context ID: BOSMAX_AVP_0001
Avatar Mode: AUTO_RESOLVE
Registry Writeback: ALLOWED_REGISTERED_PRODUCT_ONLY
```

### Minyak Warisan Cap Burung / DIRECT Registered Product

```yaml
Workflow: Minyak Warisan Cap Burung / DIRECT Registered Product
Copywriting View: NOTION_COMMAND_CENTRE_MWCB_DIRECT_COPY_ID_VIEW
Workbook Alias: CC_MWCB_DIR_COPY
Copywriting ID: CAP_BURUNG_MINYAK_CP_0031
Copywriting Mode: AUTO_RESOLVE
Avatar Context ID: MWCB_DIRECT_AVP_0001
Avatar Mode: AUTO_RESOLVE
Registry Writeback: ALLOWED_REGISTERED_PRODUCT_ONLY
```

### ON_THE_FLY Product / SESSION_ONLY

```yaml
Workflow: ON_THE_FLY Product / SESSION_ONLY
Copywriting ID: none
Copywriting Mode: SESSION_ONLY_GENERATE
Registry Writeback: FORBIDDEN
Risky or Review-Only Product: BLOCK_GENERATION
```

Hard rule:
- risky or review-only product posture must fail closed into manual review
- ON_THE_FLY output must never be promoted into workbook or approved registry from Notion

---

## 3. Copywriting ID Mini Database

Default source:
- `NOTION_COMMAND_CENTRE_COPY_ID_VIEW`

Product-specific Command Centre sources:
- `NOTION_COMMAND_CENTRE_BOSMAX_STEALTH_COPY_ID_VIEW`
- `NOTION_COMMAND_CENTRE_MWCB_DIRECT_COPY_ID_VIEW`

Workbook aliases:
- `NOTION_COMMAND_CENTRE_COPY_ID_VIEW` -> `CC_COPY_ID_VIEW`
- `NOTION_COMMAND_CENTRE_BOSMAX_STEALTH_COPY_ID_VIEW` -> `CC_BSMX_ST_COPY`
- `NOTION_COMMAND_CENTRE_MWCB_DIRECT_COPY_ID_VIEW` -> `CC_MWCB_DIR_COPY`

Allowed fields:
- `Copywriting_ID`
- `Display_Name`
- `Product_Name`
- `Family_Name`
- `Lane`
- `Submode_Formula`
- `Compliance`
- `Status`
- `Safe_Usage_Notes`

Forbidden in this beginner view:
- `Hook`
- `USP_1`
- `USP_2`
- `USP_3`
- `CTA`
- provenance nodes
- source paths
- compliance internals

---

## 4. Avatar Context ID Mini Database

Default source:
- `NOTION_COMMAND_CENTRE_AVATAR_ID_VIEW`

Allowed fields:
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

Registered MWCB direct avatar support:
- `MWCB_DIRECT_AVP_0001`
- `MWCB_DIRECT_AVP_0002`

---

## 5. Avatar Pool ID Mini Database

Default source:
- `NOTION_COMMAND_CENTRE_AVATAR_POOL_VIEW`

Allowed fields:
- `Pool_ID`
- `Display_Name`
- `Product_ID`
- `Product_Family`
- `Silo`
- `Rotation_Mode`
- `No_Repeat_Window`
- `Minimum_Approved_Count`
- `Status`
- `Safe_Usage_Notes`

Registered MWCB direct batch pool:
- `MWCB_TRAD_REMEDY_POOL_001`

---

## 6. Batch Production Template

This is the default batch template:

```yaml
Platform: TikTok
Mode: B
Engine: VEO_3_1_LITE
Duration: 8s
Submode formula: SAVAGE_HPAS
Silo: STEALTH
Avatar Pool ID: BOSMAX_MALE_STEALTH_POOL_001
Avatar Mode: AUTO_ROTATE
Camera style: UGC_IPHONE_RAW
Language: Malay
Produk: BOSMAX Serum 5ML
Scale anchor: EXACTLY lip balm size, fit into fingers naturally
Physics class: CLASS_A
Copywriting ID: BOSMAX_SERUM_CP_0001
Copywriting Mode: AUTO_RESOLVE
Compliance: STEALTH_METAPHOR_REQUIRED
Batch Count: 20
Rotation Rule: ROUND_ROBIN_NO_REPEAT
```

---

## 7. Legacy Expert Mode / Manual Override Notice

The old workflow remains available only as:
- `LEGACY_EXPERT_MODE`
- `MANUAL_OVERRIDE_REVIEW_ONLY`

This includes manual editing of:
- `Hook`
- `USP_1`
- `USP_2`
- `USP_3`
- `CTA`
- `Avatar`
- `Mannequin`
- `Wardrobe`
- `Scene`

Hard rule:
- any manual override must be marked `Needs Compliance Review`

This workflow is not the default Command Centre flow.

---

## 8. Operator Rules

- Use the Command Centre Plug & Play template by default.
- Use the product workflow that matches the route result exactly: STEALTH registered, DIRECT registered, or ON_THE_FLY session-only.
- Select approved IDs from mini databases only.
- Do not treat Notion as source truth.
- Do not expose backend/provenance/private compliance data in beginner mini databases.
- Do not create or edit reusable registry truth from ON_THE_FLY output.
- Do not bypass risky/review-only blocking by forcing `SESSION_ONLY_GENERATE`.
- Use `LEGACY_EXPERT_MODE` only for trusted operators and review-only exceptions.
- Manual override without `Needs Compliance Review` is invalid.
