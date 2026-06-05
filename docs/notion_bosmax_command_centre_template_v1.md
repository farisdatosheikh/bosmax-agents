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
2. `Copywriting ID Mini Database`
3. `Avatar Context ID Mini Database`
4. `Avatar Pool ID Mini Database`
5. `Batch Production Template`
6. `Legacy Expert Mode / Manual Override Notice`
7. `Operator Rules`

---

## 1. Plug & Play Video Prompt Template

This is the default single prompt template:

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

## 2. Copywriting ID Mini Database

Default source:
- `NOTION_COMMAND_CENTRE_COPY_ID_VIEW`

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

## 3. Avatar Context ID Mini Database

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

---

## 4. Avatar Pool ID Mini Database

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

---

## 5. Batch Production Template

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

## 6. Legacy Expert Mode / Manual Override Notice

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

## 7. Operator Rules

- Use the Command Centre Plug & Play template by default.
- Select approved IDs from mini databases only.
- Do not treat Notion as source truth.
- Do not expose backend/provenance/private compliance data in beginner mini databases.
- Use `LEGACY_EXPERT_MODE` only for trusted operators and review-only exceptions.
- Manual override without `Needs Compliance Review` is invalid.
