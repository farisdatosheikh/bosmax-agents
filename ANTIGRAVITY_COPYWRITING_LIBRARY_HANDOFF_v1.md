# ANTIGRAVITY COPYWRITING LIBRARY HANDOFF v1

## Objective

Continue filling `BOSMAX_PRODUCT_COPYWRITING_LIBRARY_v1.xlsx` as an operator-facing
copywriting library that supplements:

- `SCRIPT_REGISTRY_UNIFIED.md`
- `SCRIPT_VARIANT_LIBRARY.md`

This workbook is **not** a runtime-authority replacement.

---

## Primary File

- Workbook to continue: `BOSMAX_PRODUCT_COPYWRITING_LIBRARY_v1.xlsx`

---

## Hard Boundaries

Do **not** change:

- workbook architecture
- sheet names
- canonical column order
- flagship product scale truth
- taxonomy routing logic
- archetype codes
- authority boundary between workbook and script registry

Do **not**:

- delete `INDEX`, `README_OR_RULES`, or `TAXONOMY_MASTER`
- collapse flagship sheets into generic archetype sheets
- replace workbook metadata with ad-hoc new columns
- overwrite `Authority_Source` unless a stronger verified source is explicitly supplied
- turn one row into multiple formulas or formula dumps

---

## Allowed Fill Surface

You may fill and expand only these fields:

- `Type_of_Content`
- `Silo_Key`
- `Angle`
- `Hook`
- `USP_1`
- `USP_2`
- `USP_3`
- `CTA`
- `Copywriting_Formula`
- `Notes`

You may also assign:

- `Angle_ID`
- `Hook_ID`
- `CTA_ID`
- `Status`

only to keep rows internally organized.

---

## Row Contract

One row must represent:

- one coherent angle
- one hook
- one USP triplet
- one CTA
- one chosen formula

Do not create rows that contain:

- multiple formulas in one cell
- placeholder text like `Hook 1`, `cta 1`, `usp 1`
- blank `Type_of_Content`
- blank `Silo_Key`

---

## Priority Order

### 1. Flagship sheets first

Expand these first:

- `PRODUCT_BOSMAX_SERUM`
- `PRODUCT_MW_CAP_BURUNG`

Requirements:

- keep Bosmax Serum as `STEALTH`
- keep Minyak Warisan as `DIRECT`
- preserve Bosmax 5ml vs 10ml scale distinction
- preserve MWCB 30ml WG40 bottle truth

### 2. Archetype sheets second

Then continue with archetype families, especially:

- `ARCH_STEALTH_MASSAGE_OIL`
- `ARCH_TRADITIONAL_REMEDY_DIRECT`
- `ARCH_MEN_PERFUME`
- `ARCH_WOMEN_PERFUME`
- `ARCH_UNISEX_PERFUME`
- `ARCH_BEAUTY_CONFIDENCE`
- `ARCH_BODY_CARE_FRESHNESS`
- `ARCH_FASHION_STYLE_FIT`

---

## Content Rules

### For STEALTH lanes

- use euphemistic or metaphor-safe copy
- keep tone aligned with the product’s sensitive lane
- do not rewrite stealth products into blunt explicit copy
- if relevant, stay compatible with script-registry direction

### For DIRECT lanes

- use direct consumer-facing problem/benefit language
- keep hooks understandable without registry knowledge
- optimize for TikTok Shop conversion clarity

### Formula use

Choose exactly one formula per row:

- `AIDA`
- `PAS`
- `HSO`
- `HPAS`
- `SAVAGE_HPAS`

Use the formula that best matches the row’s tone and lane. Do not stack formulas in a single row.

---

## Output Quality Standard

Every filled row should feel:

- commercially usable
- product-type appropriate
- category-consistent
- non-placeholder
- reusable across similar products in the same archetype

Hooks should be distinct from one another.  
USP triplets should not repeat the same idea three times with different wording.  
CTA should match the tone and urgency of the row.

---

## Escalation Rule

If a product family seems to need a brand-new archetype:

- do not improvise a new workbook structure
- propose the new archetype as a candidate using the same column schema
- keep the recommendation in `Notes` first unless explicit approval is given

---

## Success Condition

This handoff is successful when:

- flagship sheets contain richer, non-placeholder copy rows
- archetype sheets become genuinely reusable libraries
- workbook structure remains stable
- runtime authority remains outside the workbook
