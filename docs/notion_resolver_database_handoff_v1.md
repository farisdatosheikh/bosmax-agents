# BOSMAX Notion Resolver Database Handoff v1

## Purpose

This spec defines the **sanitized Notion-facing resolver surfaces** for:

1. `Copywriting ID`
2. `Avatar Context ID`
3. `Avatar Pool ID`

Repo truth remains upstream.
Notion is **downstream UI only**.

---

## Update Direction

`repo → Notion` only

Allowed:
- sync sanitized resolver rows from `registries/copywriting_id_resolver.yaml`
- sync sanitized resolver rows from `registries/avatar_context_rotation.yaml`
- relate operator run rows to approved resolver IDs

Forbidden:
- Notion generating new IDs
- Notion editing Hook / USP / CTA as source truth
- Notion editing avatar DNA, mannequin logic, wardrobe compatibility, or pool logic as source truth
- Notion writing back into resolver YAML or source workbooks

---

## Database 1: Copywriting ID View

**Recommended source:** `NOTION_EXPORT_VIEW` from `BOSMAX_COPYWRITING_ID_RESOLVER_v1.xlsx`

### Allowed fields
- `Copywriting_ID`
- `Display_Name`
- `Product_Name`
- `Family_Name`
- `Lane`
- `Silo_Key`
- `Submode_Formula`
- `Angle`
- `Hook`
- `USP_1`
- `USP_2`
- `USP_3`
- `CTA`
- `Compliance`
- `Status`
- `Safe_Usage_Notes`

### Forbidden fields
- `Authority_Source`
- `Source_Script_Node`
- `Source_Variant_Hook_Node`
- `Source_Variant_Problem_Node`
- `Source_Variant_Solution_Node`
- `Source_Variant_CTA_Node`
- private source paths
- compliance internals or review heuristics beyond operator-safe `Compliance` / `Status`

---

## Database 2: Avatar Context ID View

**Recommended source:** `NOTION_EXPORT_VIEW` from `BOSMAX_AVATAR_CONTEXT_RESOLVER_v1.xlsx`

### Allowed fields
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

### Forbidden fields
- `Prompt_Fragment_Source`
- full biometric DNA
- raw YAML internals
- private source paths
- `Internal_Notes`
- compatibility math beyond the operator-safe labels above

---

## Database 3: Avatar Pool View

**Recommended source:** `ROTATION_POOLS` from `BOSMAX_AVATAR_CONTEXT_RESOLVER_v1.xlsx`

### Allowed fields
- `Pool_ID`
- `Display_Name`
- `Product_ID`
- `Product_Family`
- `Silo`
- `Allowed_Avatar_Context_IDs`
- `Rotation_Mode`
- `No_Repeat_Window`
- `Minimum_Approved_Count`
- `Status`
- `Runtime_Allowed`
- `Safe_Usage_Notes`

### Forbidden fields
- private registry source paths
- raw persona DNA
- prompt fragments
- internal selection logs

---

## Manual Override Behavior

If an operator manually overrides any resolved copywriting or avatar field:

- the run must be marked `Needs Compliance Review`
- the run must not be treated as READY from Notion alone
- resolver IDs remain the source pointer for the original approved row

Manual override without `Needs Compliance Review` is invalid.

---

## P&C Boundary

Notion must not expose:

- repo source file paths
- biometric DNA
- raw prompt fragments
- hidden provenance node chains
- private compliance logic
- P&C ecosystem logic

If a field is doubtful, keep it out of Notion and leave it in the repo-only registry.

---

## Operator Usage Contract

### Single avatar resolution

Use:
- `Copywriting ID`
- `Copywriting Mode = AUTO_RESOLVE`
- `Avatar Context ID`
- `Avatar Mode = AUTO_RESOLVE`

### Batch avatar rotation

Use:
- `Copywriting ID`
- `Copywriting Mode = AUTO_RESOLVE`
- `Avatar Pool ID`
- `Avatar Mode = AUTO_ROTATE`
- `Batch Count`
- `Rotation Rule = ROUND_ROBIN_NO_REPEAT`

Notion operators select approved IDs only.
The repo resolver injects Hook / USP / CTA / persona / wardrobe / mannequin / scene context downstream.
