# CLAUDE Notion Handover v1

Author: Codex  
Date: 2026-06-04  
Status: ready for Claude execution

## Objective

Complete the remaining Notion UI configuration for the BOSMAX hybrid mini-system.

Codex has already patched the live Notion architecture through MCP.
What remains is mainly `form-view configuration` inside the Notion UI.

---

## Live Pages and Databases

### Tester Page

- `🧪 BOSMAX Mini System Tester`
- URL: `https://app.notion.com/p/3744775af48a815a9063d6a71d976f5b`

### Existing Database

- `🗂️ BOSMAX Products Registry`
- URL: `https://app.notion.com/p/cc7a260ffe9f4a6caef582544ea3dcfe`
- Data source: `collection://45d05e4c-d12e-42bc-9485-8cc012dcb042`

### New Database Created by Codex

- `🧩 BOSMAX Product Families`
- URL: `https://app.notion.com/p/774c055432aa4df19cb6fc12577de07e`
- Data source: `collection://8fa7b82a-a32e-43af-af22-a598a3ccb8b3`

### Patched Existing Database

- `📝 BOSMAX Image Requests`
- URL: `https://app.notion.com/p/1c6a550f40bb4f07b8fec78792da98d0`
- Data source: `collection://129d8a1b-319c-41d4-ae2e-1122eb48ed06`

### New Database Created by Codex

- `🎬 BOSMAX Video Requests`
- URL: `https://app.notion.com/p/7135ffe5a5ef47d8afedb1d9f2d51399`
- Data source: `collection://2b7d6cca-471a-4277-b0cb-4eed83cb15a8`

---

## What Codex Already Completed

### 1. Tester page updated

The page content now explains the hybrid model:

- `PRODUCT` lane for exact product truth
- `FAMILY` lane for reusable cross-brand logic

The page now links all four surfaces:

- Products Registry
- Product Families
- Image Requests
- Video Requests

### 2. New `Product Families` database created

Seeded strategic rows:

- `FAMILY_MALE_EXT_SENSITIVE_OIL`
- `FAMILY_TRADITIONAL_REMEDY_OIL`
- `FAMILY_WOMEN_PERFUME`
- `FAMILY_UNISEX_PERFUME`
- `FAMILY_TUDUNG_BAWAL`
- `FAMILY_MAKEUP_COSMETICS`
- `FAMILY_SNACKS`

### 3. `Image Requests` patched to hybrid architecture

Added fields:

- `Request Scope`
- `Product Family`
- `Family Name`
- `Family Code`
- `Family Type of Content`
- `Family Silo Key`

`Generated Prompt` has already been changed to become scope-aware:

- if `PRODUCT`, it uses exact product truth
- if `FAMILY`, it uses family logic and family silo

### 4. `Video Requests` database created

Fields already created:

- `Request Scope`
- `Platform`
- `Produk`
- `Product Family`
- `Produk Nama`
- `Produk Scale Anchor`
- `Family Name`
- `Family Code`
- `Family Type of Content`
- `Family Silo Key`
- `Engine`
- `Duration`
- `Reference Mode`
- `Presentation Route`
- `Language`
- `Generated Prompt`
- `Status`
- `Notes`

`Generated Prompt` formula is already installed.

### 5. Views already created

#### Product Families

- `📚 Family Registry`

#### Image Requests

- `🧭 Scope-Aware Requests`
- `📋 New Hybrid Image Request`

#### Video Requests

- `📊 All Video Requests`
- `📋 New Video Request`

---

## What Is Still Incomplete

This is the key remaining gap:

### Form questions are not fully configured in the Notion UI

Through MCP, Codex could create the form views, but the current metadata still shows only:

- `Title -> Request Name`

Meaning:

- schema is correct
- database properties exist
- formulas exist
- views exist
- but the `form-question experience` still needs manual UI configuration

This is the part Claude should finish.

---

## Claude Task

### A. Finish `📋 New Hybrid Image Request`

Open:

- `📝 BOSMAX Image Requests`
- view: `📋 New Hybrid Image Request`

Configure the form so operator can fill:

1. `Request Name`
2. `Request Scope`
3. `Produk`
4. `Product Family`
5. `Platform`
6. `Background Color`
7. `Notes`

Desired operator behavior:

- if `Request Scope = PRODUCT`, operator chooses `Produk`
- if `Request Scope = FAMILY`, operator chooses `Product Family`

If Notion cannot do conditional hiding cleanly in this form:

- leave both visible
- add helper copy in form description:
  - `Jika PRODUCT, isi Produk`
  - `Jika FAMILY, isi Product Family`

### B. Finish `📋 New Video Request`

Open:

- `🎬 BOSMAX Video Requests`
- view: `📋 New Video Request`

Configure the form so operator can fill:

1. `Request Name`
2. `Request Scope`
3. `Produk`
4. `Product Family`
5. `Platform`
6. `Engine`
7. `Duration`
8. `Reference Mode`
9. `Presentation Route`
10. `Language`
11. `Notes`

Desired operator behavior:

- if `Request Scope = PRODUCT`, operator chooses `Produk`
- if `Request Scope = FAMILY`, operator chooses `Product Family`

If conditional form logic is weak:

- keep both visible
- add helper text exactly like image form

### C. Sanity-test prompt generation

Create at least these test records:

#### Image tests

1. `PRODUCT` test:
- product = one exact flagship item
- verify `Generated Prompt` mentions exact product truth

2. `FAMILY` test:
- family = `FAMILY_MALE_EXT_SENSITIVE_OIL`
- verify `Generated Prompt` mentions family logic and family silo

#### Video tests

1. `PRODUCT` test:
- choose exact product
- verify prompt includes engine, duration, route, and exact product lane

2. `FAMILY` test:
- choose `FAMILY_WOMEN_PERFUME` or `FAMILY_TUDUNG_BAWAL`
- verify prompt resolves to family lane, not exact SKU logic

### D. Do not restructure the architecture

Claude must **not**:

- delete existing databases
- revert hybrid architecture
- collapse family registry back into product registry
- rewrite formulas unless broken
- turn everything into product-only again

Claude should only:

- finish UI form configuration
- improve labels / helper copy / descriptions if useful
- verify operator flow

---

## Important Hybrid Logic

This system is now intentionally hybrid:

- `Products Registry` = exact product truth
- `Product Families` = reusable cross-brand copy/prompt logic

That split must remain intact.

Examples:

- `Bosmax Serum 5ml` and `Bosmax Serum 10ml` remain product truth
- `Bosmax / Maverix / Big Boss-type male external oils` collapse under one family logic
- many women perfume brands collapse into one family logic
- many bawal brands collapse into one family logic

---

## Suggested Claude Deliverable

Claude should return:

1. confirmation that both forms are fully configured
2. screenshots or exact notes of visible form questions
3. verification that generated prompts behave correctly for both:
   - `PRODUCT`
   - `FAMILY`
4. any UI limitation found in Notion form logic

---

## Verdict

Codex has already completed the architecture patch.

Claude should now finish the final `operator-facing form UX` inside Notion UI.

This is not a rebuild task.
This is a finishing-and-verification task.
