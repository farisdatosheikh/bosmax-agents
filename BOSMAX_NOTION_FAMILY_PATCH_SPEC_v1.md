# BOSMAX Notion Family Patch Spec v1

Author: Codex  
Date: 2026-06-04  
Status: ready for Notion implementation

## 1. Decision

Do **not** continue the old Notion mini-system `as-is`.

Keep what already works, but patch the architecture so it matches the current
family-based BOSMAX copywriting system in:

- `BOSMAX_PRODUCT_COPYWRITING_LIBRARY_FAMILY_v2.xlsx`

Reason:

- the old Notion tester was built around `product registry` only
- the current BOSMAX workbook is now `family-based`
- if Notion remains product-only, new request routing will drift away from the
  actual BOSMAX copywriting authority

## 2. What Stays

Keep these existing Notion surfaces:

- `BOSMAX COMMAND CENTRE`
- `BOSMAX Mini System Tester`
- `BOSMAX Products Registry`
- `BOSMAX Image Requests`

Keep the current `Products Registry` concept because it is still useful for:

- exact product truth
- exact variant truth
- exact scale anchors
- flagship-specific prompt generation

Examples:

- `BOSMAX Serum 5ML`
- `BOSMAX Serum 10ML`
- `Minyak Warisan Cap Burung 30ML`
- `Maverix Maxoil Set 5 Botol`
- `Minyak Jungle Girl 30ML`

## 3. What Must Be Added

Add a new database:

- `BOSMAX Product Families`

This becomes the Notion mirror of the workbook sheet:

- `DEDUPED_PRODUCT_FAMILIES`

Examples of families to seed first:

- `FAMILY_MALE_EXT_SENSITIVE_OIL`
- `FAMILY_TRADITIONAL_REMEDY_OIL`
- `FAMILY_WOMEN_PERFUME`
- `FAMILY_UNISEX_PERFUME`
- `FAMILY_TUDUNG_BAWAL`
- `FAMILY_MAKEUP_COSMETICS`
- `FAMILY_SNACKS`

## 4. Required Architecture Change

The Notion request layer must support **two request scopes**:

- `PRODUCT`
- `FAMILY`

Meaning:

- use `PRODUCT` when operator needs exact flagship truth or exact variant truth
- use `FAMILY` when operator wants reusable copy or prompt logic across similar
  brands/listings

This is the key patch. Without it, the Notion system will remain out of date.

## 5. Database A — BOSMAX Product Families

Create database:

- `🧩 BOSMAX Product Families`

Purpose:

- family-level routing
- cross-brand reusable copy/prompt logic
- bridge between Fastmoss collapse logic and Notion request forms

Suggested schema:

```sql
CREATE TABLE (
  "Name"                 TITLE,
  "Family Code"          RICH_TEXT,
  "Worksheet Name"       RICH_TEXT,
  "Type of Content"      SELECT('DIRECT':green, 'STEALTH':red),
  "Silo Key Default"     RICH_TEXT,
  "Default Formula"      SELECT('AIDA':blue, 'PAS':orange, 'HSO':purple, 'HPAS':pink, 'SAVAGE_HPAS':red),
  "Category Family"      RICH_TEXT,
  "Commercial Mechanic"  RICH_TEXT,
  "Mapped Product Count" NUMBER,
  "Flagship Link"        RICH_TEXT,
  "Authority Source"     RICH_TEXT,
  "Notes"                RICH_TEXT
)
```

Seed first from workbook `DEDUPED_PRODUCT_FAMILIES`:

| Name | Family Code | Type of Content | Silo Key Default |
|------|-------------|-----------------|------------------|
| Male Sensitive External Oil | FAMILY_MALE_EXT_SENSITIVE_OIL | STEALTH | male_health_stealth_01 |
| Traditional Remedy Oil | FAMILY_TRADITIONAL_REMEDY_OIL | DIRECT | traditional_remedy_direct |
| Perfume Wanita | FAMILY_WOMEN_PERFUME | DIRECT | women_perfume_direct |
| Perfume Unisex | FAMILY_UNISEX_PERFUME | DIRECT | unisex_perfume_direct |
| Tudung Bawal | FAMILY_TUDUNG_BAWAL | DIRECT | tudung_bawal_direct |
| Makeup | FAMILY_MAKEUP_COSMETICS | DIRECT | makeup_direct |
| Snek | FAMILY_SNACKS | DIRECT | snack_direct |

## 6. Database B — Patch Existing Image Requests

Do **not** replace the current database.

Patch existing:

- `📝 BOSMAX Image Requests`

### Add fields

```sql
ALTER TABLE ADD COLUMN "Request Scope" SELECT('PRODUCT':blue, 'FAMILY':purple)
ALTER TABLE ADD COLUMN "Product Family" RELATION('<BOSMAX Product Families Data Source ID>')
ALTER TABLE ADD COLUMN "Family Name" ROLLUP('Product Family', 'Name', 'show_original')
ALTER TABLE ADD COLUMN "Family Code" ROLLUP('Product Family', 'Family Code', 'show_original')
ALTER TABLE ADD COLUMN "Family Type of Content" ROLLUP('Product Family', 'Type of Content', 'show_original')
ALTER TABLE ADD COLUMN "Family Silo Key" ROLLUP('Product Family', 'Silo Key Default', 'show_original')
```

### Existing fields to keep

- `Platform`
- `Produk`
- `Produk Nama`
- `Produk Kategori`
- `Produk Scale Anchor`
- `Background Color`
- `Generated Prompt`
- `Status`
- `Notes`

### Operator rule

- if `Request Scope = PRODUCT`, operator fills `Produk`
- if `Request Scope = FAMILY`, operator fills `Product Family`

### Generated Prompt formula — image request

Replace old product-only formula with scope-aware formula:

```text
"Platform: " + prop("Platform") +
"\nMode: A" +
"\nRequest scope: " + if(empty(prop("Request Scope")), "[pilih scope]", prop("Request Scope")) +
"\nKategori: " +
if(
  prop("Request Scope") == "FAMILY",
  prop("Family Name"),
  prop("Produk Kategori")
) +
"\nProduk / Family: " +
if(
  prop("Request Scope") == "FAMILY",
  prop("Family Name"),
  prop("Produk Nama")
) +
"\nSilo: " +
if(
  prop("Request Scope") == "FAMILY",
  prop("Family Silo Key"),
  ""
) +
"\nScale anchor: " +
if(
  prop("Request Scope") == "FAMILY",
  "[resolve from chosen product if exact product visual needed]",
  prop("Produk Scale Anchor")
) +
"\nBuat gambar komersial untuk " +
if(
  prop("Request Scope") == "FAMILY",
  "family " + prop("Family Name"),
  "produk " + prop("Produk Nama")
) +
".\nBackground: Clean gradient " +
if(empty(prop("Background Color")), "[pilih warna]", prop("Background Color")) +
" - premium look" +
"\nLighting: Soft studio lighting, highlight pada subject" +
"\nAngle: 3/4 view, slight elevation" +
"\nMood: Premium, trustworthy, clean" +
"\nPlatform target: " + prop("Platform")
```

### Why this formula changes

Because `family` requests often do **not** want exact packaging/variant truth.
They want reusable direction first.

The old formula assumed every request must resolve to one exact product.

## 7. Database C — New Video Requests

Create new database:

- `🎬 BOSMAX Video Requests`

This should be created **after** `BOSMAX Product Families` exists.

Suggested schema:

```sql
CREATE TABLE (
  "Request Name"            TITLE,
  "Request Scope"           SELECT('PRODUCT':blue, 'FAMILY':purple),
  "Platform"                SELECT('TikTok':blue, 'Shopee':orange, 'Lazada':purple, 'Meta':blue, 'YouTube Shorts':red),
  "Produk"                  RELATION('<Products Registry Data Source ID>'),
  "Product Family"          RELATION('<Product Families Data Source ID>'),
  "Produk Nama"             ROLLUP('Produk', 'Name', 'show_original'),
  "Produk Scale Anchor"     ROLLUP('Produk', 'Scale Anchor', 'show_original'),
  "Family Name"             ROLLUP('Product Family', 'Name', 'show_original'),
  "Family Code"             ROLLUP('Product Family', 'Family Code', 'show_original'),
  "Family Type of Content"  ROLLUP('Product Family', 'Type of Content', 'show_original'),
  "Family Silo Key"         ROLLUP('Product Family', 'Silo Key Default', 'show_original'),
  "Engine"                  SELECT('GROK':red, 'KLING_3_0':orange, 'VEO_3_1_LITE':yellow, 'VEO_3_1':green, 'SEEDANCE_2_0':blue, 'GOOGLE_FLOW':purple),
  "Duration"                SELECT('6s':gray, '8s':gray, '10s':gray, '12s':gray, '15s':gray, '16s':gray, '20s':gray, '30s':gray),
  "Reference Mode"          SELECT('NONE':default, 'IMAGE_REFERENCE':blue, 'VIDEO_REFERENCE':purple, 'BOSMAX_IMAGE_HANDOFF':red),
  "Presentation Route"      SELECT('UGC':green, 'PGC':orange, 'HYBRID':purple),
  "Language"                SELECT('BM':red, 'EN':blue, 'CN':yellow),
  "Generated Prompt"        FORMULA,
  "Status"                  SELECT('NEW':blue, 'IN_PROGRESS':yellow, 'DONE':green, 'ABORT':red),
  "Notes"                   RICH_TEXT
)
```

### Video prompt logic

Use one formula only after database creation via `ALTER COLUMN ... SET FORMULA(...)`.

Formula strategy:

- if `Request Scope = PRODUCT`, include exact product and exact scale anchor
- if `Request Scope = FAMILY`, include family, family silo, route, engine, and
  reusable commercial logic

Core output fields:

- platform
- request scope
- product or family target
- engine
- duration
- reference mode
- presentation route
- language
- silo
- scale anchor or fallback note

## 8. Database D — Optional Product Registration Form

Create later, not now:

- `➕ BOSMAX Product Registration`

Reason:

- tonight the highest ROI is fixing request routing
- registration form can wait until request surfaces stop drifting

## 9. Minimum Implementation Order

Follow this order exactly:

1. Keep old `Products Registry`
2. Create `BOSMAX Product Families`
3. Seed strategic family rows
4. Patch `BOSMAX Image Requests` with `Request Scope` + family relation
5. Update `Generated Prompt` to become scope-aware
6. Create `BOSMAX Video Requests`
7. Only after that, consider product registration form

## 10. Immediate Seed Set

If only a small implementation window is available, seed these families first:

- `FAMILY_MALE_EXT_SENSITIVE_OIL`
- `FAMILY_TRADITIONAL_REMEDY_OIL`
- `FAMILY_WOMEN_PERFUME`
- `FAMILY_UNISEX_PERFUME`
- `FAMILY_TUDUNG_BAWAL`

This is enough to make the Notion system match the latest BOSMAX lanes.

## 11. What Not To Do

Do **not**:

- rebuild the whole tester from zero
- delete the working image request form
- make everything family-only
- make everything product-only
- treat copywriting workbook rows as direct Notion records one-to-one

The correct model is hybrid:

- `product registry` for exact product truth
- `family registry` for reusable prompt/copy logic

## 12. Practical Verdict

Best path:

- patch old Notion system first
- then extend to video

Wrong path:

- continue Claude Phase 2 exactly as originally designed without family support

That would hard-code old assumptions into the new BOSMAX operating layer.
