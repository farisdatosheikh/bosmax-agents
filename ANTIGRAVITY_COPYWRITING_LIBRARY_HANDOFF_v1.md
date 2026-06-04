# ANTIGRAVITY COPYWRITING LIBRARY HANDOFF v2

## Objective

Continue filling the **family-based** BOSMAX copywriting workbook:

- `BOSMAX_PRODUCT_COPYWRITING_LIBRARY_FAMILY_v2.xlsx`

This workbook supplements:

- `SCRIPT_REGISTRY_UNIFIED.md`
- `SCRIPT_VARIANT_LIBRARY.md`

It is **not** a runtime-authority replacement.

---

## Read Order

Before filling anything, read these sheets in order:

1. `README_OR_RULES`
2. `PRODUCT_FAMILY_MAPPING`
3. `DEDUPED_PRODUCT_FAMILIES`
4. `PRODUCT_BOSMAX_SERUM`
5. `PRODUCT_MW_CAP_BURUNG`
6. relevant `FAMILY_*` sheets only

Meaning:

- `RAW_FASTMOSS_PRODUCTS` = intake evidence only
- `PRODUCT_FAMILY_MAPPING` = 300 raw listings mapped into deduped product families
- `DEDUPED_PRODUCT_FAMILIES` = one row per reusable product family
- `PRODUCT_*` and `FAMILY_*` sheets = the real copywriting fill surface

---

## Hard Boundaries

Do **not** change:

- workbook architecture
- sheet names
- canonical column order
- `Family_Code`
- `Family_Name`
- flagship product scale truth
- family routing logic already established in `PRODUCT_FAMILY_MAPPING`
- authority boundary between workbook and script registry

Do **not**:

- edit `RAW_FASTMOSS_PRODUCTS`
- rewrite `PRODUCT_FAMILY_MAPPING`
- rewrite `DEDUPED_PRODUCT_FAMILIES`
- collapse `PRODUCT_BOSMAX_SERUM` into generic family sheet
- collapse `PRODUCT_MW_CAP_BURUNG` into generic family sheet
- replace workbook metadata with ad-hoc columns
- turn one row into multiple formulas or formula dumps

---

## Allowed Fill Surface

You may fill and expand only inside:

- `PRODUCT_BOSMAX_SERUM`
- `PRODUCT_MW_CAP_BURUNG`
- visible `FAMILY_*` library sheets

You may fill only these fields:

- `Type_of_Content`
- `Silo_Key`
- `Angle`
- `Hook`
- `Pain_or_Friction`
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

only for clean row organization.

---

## Family Logic

This workbook is no longer organized by brand or raw marketplace listing.

It is organized by **product family**:

- many men perfume brands -> one `Perfume Lelaki` family
- many women perfume brands -> one `Perfume Wanita` family
- many stealth male external oil brands -> one `Male Sensitive External Oil` family
- many similar bawal listings -> one `Tudung Bawal` family

Antigravity must write copy that is:

- reusable across brands inside the same family
- not overfit to one listing title
- commercially usable for the whole family mechanism

---

## Row Contract

One row must represent:

- one coherent angle
- one hook
- one pain or friction
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

- keep `PRODUCT_BOSMAX_SERUM` in `STEALTH`
- keep `PRODUCT_MW_CAP_BURUNG` in `DIRECT`
- preserve Bosmax 5ml vs 10ml distinction
- preserve MWCB `30ml WG40` bottle truth

### 2. Strategic family sheets second

Then prioritize:

- `FAMILY_MALE_EXT_OIL`
- `FAMILY_TRAD_REMEDY_OIL`
- `FAMILY_MEN_PERFUME`
- `FAMILY_WOMEN_PERFUME`
- `FAMILY_UNISEX_PERFUME`
- `FAMILY_HAIR_SHAMPOO`
- `FAMILY_HAIR_OIL`
- `FAMILY_TUDUNG_BAWAL`
- `FAMILY_KAMBING_PERAP`

### 3. High-density family sheets third

Then continue sheets with clear density in the workbook such as:

- `FAMILY_MAKEUP`
- `FAMILY_SNACKS`
- `FAMILY_WOMEN_JERSEY`
- `FAMILY_SPORTSWEAR`
- `FAMILY_BEDSHEET_SET`
- `FAMILY_STORAGE_BOX`

---

## Content Rules

### For STEALTH lanes

- use euphemistic or metaphor-safe copy
- keep tone aligned with sensitive-product handling
- do not rewrite stealth products into blunt explicit copy
- remain compatible with script-registry direction

### For DIRECT lanes

- use direct consumer-facing problem/benefit language
- keep hooks understandable without registry knowledge
- make sure `Pain_or_Friction` is a real inconvenience, not a duplicate hook
- optimize for TikTok Shop conversion clarity

### Formula use

Choose exactly one formula per row:

- `AIDA`
- `PAS`
- `HSO`
- `HPAS`
- `SAVAGE_HPAS`

Do not stack formulas in one cell.

---

## Output Quality Standard

Every filled row should feel:

- commercially usable
- family-appropriate
- category-consistent
- non-placeholder
- reusable across multiple brands in the same family

Hooks should be distinct from one another.  
USP triplets should not repeat the same idea three times.  
CTA should match the row tone.

---

## Escalation Rule

If a new listing does not fit any visible `FAMILY_*` sheet:

- first check `DEDUPED_PRODUCT_FAMILIES`
- if family already exists there but has no sheet, note it in `Notes`
- do **not** invent a new structure on your own

If you believe a family should be collapsed further:

- write the recommendation in `Notes`
- do not rewrite mapping tables directly

---

## Success Condition

This handoff is successful when:

- flagship sheets become richer and more reusable
- strategic family sheets become true cross-brand copy libraries
- raw/mapping/master layers remain untouched
- workbook remains family-based, not brand-listing-based
- runtime authority remains outside the workbook
