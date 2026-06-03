# BOSMAX Notion Mini System — Codex Brief v1
# Author: Claude Cowork
# Date: 2026-06-03
# Status: TESTER CONFIRMED WORKING — ready to extend

---

## 1. KONTEKS

User mahu replace cara lama (delete + copy-paste prompt table) dengan mini system Notion
yang ada dropdown form. User isi 3 field, prompt auto-generate, terus copy-paste ke AI engine.

Tester sudah confirmed working pada:
https://www.notion.so/TEST-Cap-Burung-TikTok-Navy-3744775af48a816cb87dfb7327fab611

---

## 2. STRUKTUR YANG DIBINA

### Parent Page
- **BOSMAX COMMAND CENTRE**
  - Page ID: `36f4775af48a817685fde4c521952d81`
  - URL: https://app.notion.com/p/36f4775af48a817685fde4c521952d81

### Tester Page (child of Command Centre)
- **🧪 BOSMAX Mini System Tester**
  - Page ID: `3744775af48a815a9063d6a71d976f5b`
  - URL: https://app.notion.com/p/3744775af48a815a9063d6a71d976f5b

### Database 1 — Products Registry
- **🗂️ BOSMAX Products Registry**
  - Page ID: `cc7a260ffe9f4a6caef582544ea3dcfe`
  - Data Source ID: `45d05e4c-d12e-42bc-9485-8cc012dcb042`
  - URL: https://app.notion.com/p/cc7a260ffe9f4a6caef582544ea3dcfe

### Database 2 — Image Requests
- **📝 BOSMAX Image Requests**
  - Page ID: `1c6a550f40bb4f07b8fec78792da98d0`
  - Data Source ID: `129d8a1b-319c-41d4-ae2e-1122eb48ed06`
  - URL: https://app.notion.com/p/1c6a550f40bb4f07b8fec78792da98d0

---

## 3. SCHEMA — Products Registry

```sql
CREATE TABLE (
  "Name"        TITLE,           -- "BOSMAX Serum 5ML", "Minyak Warisan Cap Burung 30ML", dll
  "Kategori"    RICH_TEXT,       -- "Health & Wellness" | "Beauty & Personal Care"
  "Scale Anchor" RICH_TEXT,      -- exact scale anchor descriptor dari products/*.yaml
  "Silo"        SELECT('DIRECT':green, 'STEALTH':red),
  "Variant"     RICH_TEXT,       -- variant label ringkas
  "Product ID"  RICH_TEXT        -- registry key, e.g. "BOSMAX_SERUM_5ML"
)
```

### Products dalam Registry (5 records):
| Name | Product ID | Silo | Scale Anchor |
|------|------------|------|--------------|
| BOSMAX Serum 5ML | BOSMAX_SERUM_5ML | STEALTH | EXACTLY lip balm size, fit into fingers naturally |
| BOSMAX Serum 10ML | BOSMAX_SERUM_10ML | STEALTH | EXACTLY chapstick size, fit into fingers naturally |
| Minyak Warisan Cap Burung 30ML | CAP_BURUNG_30ML_WG40 | DIRECT | EXACTLY a small pocket-size 30ml rectangular clear glass medicated oil bottle with a red ribbed cap, shorter than the palm and only two fingers wide |
| Maverix Maxoil Set 5 Botol | MAVERIX_SET_5_BOTTLES | STEALTH | EXACTLY lip balm size per bottle, fit into fingers naturally, sold as a 5-bottle set |
| Minyak Jungle Girl 30ML | JUNGLE_GIRL_30ML_JG01 | DIRECT | EXACTLY a compact 30ml massage oil bottle size, naturally hand-sized |

---

## 4. SCHEMA — Image Requests

```sql
CREATE TABLE (
  "Request Name"        TITLE,
  "Platform"            SELECT('TikTok':blue, 'Shopee':orange, 'Lazada':purple, 'Meta':blue, 'YouTube Shorts':red),
  "Produk"              RELATION('45d05e4c-d12e-42bc-9485-8cc012dcb042'),  -- relation ke Products Registry
  "Produk Nama"         ROLLUP('Produk', 'Name', 'show_original'),
  "Produk Kategori"     ROLLUP('Produk', 'Kategori', 'show_original'),
  "Produk Scale Anchor" ROLLUP('Produk', 'Scale Anchor', 'show_original'),
  "Background Color"    SELECT('Navy Blue':blue, 'Gold':yellow, 'Sage Green':green, 'Cream White':default, 'Charcoal Black':gray, 'Rose Gold':pink, 'Deep Purple':purple),
  "Generated Prompt"    FORMULA(-- see Section 5 --),
  "Status"              SELECT('NEW':blue, 'IN_PROGRESS':yellow, 'DONE':green, 'ABORT':red),
  "Notes"               RICH_TEXT
)
```

### Views:
- `📋 New Image Request` — Form view (front door untuk user isi)
- `📊 All Requests` — Table view (overview semua requests)

---

## 5. FORMULA — Generated Prompt (CONFIRMED WORKING)

```
"Platform: " + prop("Platform") + "\nMode: A\nKategori: " + prop("Produk Kategori") + "\nProduk: " + prop("Produk Nama") + "\nScale anchor: " + prop("Produk Scale Anchor") + "\nBuat gambar komersial produk " + prop("Produk Nama") + ".\nSaiz produk: " + prop("Produk Scale Anchor") + "\nBackground: Clean gradient " + if(empty(prop("Background Color")), "[pilih warna]", prop("Background Color")) + " - premium look\nLighting: Soft studio lighting, highlight pada produk\nAngle: 3/4 view, slight elevation\nMood: Premium, trustworthy, clean\nPlatform target: " + prop("Platform")
```

### Output format (apabila semua field diisi):
```
Platform: TikTok
Mode: A
Kategori: Health & Wellness
Produk: Minyak Warisan Cap Burung 30ML
Scale anchor: EXACTLY a small pocket-size 30ml rectangular clear glass medicated oil bottle with a red ribbed cap, shorter than the palm and only two fingers wide
Buat gambar komersial produk Minyak Warisan Cap Burung 30ML.
Saiz produk: EXACTLY a small pocket-size 30ml rectangular clear glass medicated oil bottle with a red ribbed cap, shorter than the palm and only two fingers wide
Background: Clean gradient Navy Blue - premium look
Lighting: Soft studio lighting, highlight pada produk
Angle: 3/4 view, slight elevation
Mood: Premium, trustworthy, clean
Platform target: TikTok
```

---

## 6. CARA GUNA (USER FLOW)

1. Buka BOSMAX Image Requests → view "📋 New Image Request"
2. Isi Platform (dropdown)
3. Isi Produk (relation dropdown ke Products Registry)
4. Isi Background Color (dropdown)
5. Submit form
6. Buka record baru → copy field "Generated Prompt"
7. Paste ke AI engine (Claude Cowork/Codex/dll)

---

## 7. LESSONS LEARNED — CRITICAL UNTUK CODEX

### 7.1 Formula newlines — cara yang betul
JANGAN guna actual newline chars dalam DDL formula string.
GUNA `\n` sebagai escape sequence dalam parameter string (bukan newline char sebenar).

✅ Cara betul (dalam ALTER COLUMN SET):
```
ALTER COLUMN "Field" SET FORMULA('"line1\nline2\nline3"')
```
Bila parameter dihantar as-is (bukan JSON-encoded), `\n` sampai ke DDL sebagai dua char (backslash + n),
dan Notion formula engine interpret ia sebagai newline dalam output.

❌ Cara salah (bila \n jadi actual newline dalam DDL single-quoted string):
- Breaks DDL parser dengan error "Unterminated single-quoted string"

### 7.2 FORMULA dalam CREATE TABLE vs ADD/ALTER COLUMN
- `FORMULA(...)` dalam CREATE TABLE schema: lebih fragile, mudah fail
- `ALTER COLUMN "X" SET FORMULA(...)`: lebih reliable, gunakan ini untuk formula complex
- Strategy: buat database dulu tanpa formula, lepas tu ADD COLUMN atau ALTER COLUMN untuk formula

### 7.3 Rollup dalam formula
- Direct `prop("Rollup Property")` WORKS — returns string value apabila single record linked
- `join()` atau `format()` TIDAK DIPERLUKAN untuk rollup text/title properties
- Rollup values di-omit dalam Notion MCP API fetch response — mesti semak dalam UI

### 7.4 Relation field dalam create-pages
- Gunakan page URL (https://app.notion.com/p/...) bukan page ID sahaja
- Format: `"Produk": "https://app.notion.com/p/[page-id]"`

### 7.5 FORMULA DDL error "Expected `)` at position N"
- Biasanya disebabkan: actual newlines dalam formula string ATAU nested function yang complex
- Fix: simplify formula dulu → test → build up incrementally

---

## 8. NEXT STEPS — YANG PERLU DIBUAT

### Phase 2: Extend ke Video Request
Bina database baru **BOSMAX Video Requests** dengan fields:
- `Platform` (Select)
- `Produk` (Relation → Products Registry)
- `Engine` (Select: GROK | KLING_3_0 | VEO_3_1_LITE | VEO_3_1 | SEEDANCE_2_0 | GOOGLE_FLOW)
- `Duration` (Select: 6s | 8s | 10s | 12s | 15s | 16s | 20s | 30s)
- `Reference Mode` (Select: NONE | IMAGE_REFERENCE | VIDEO_REFERENCE | BOSMAX_IMAGE_HANDOFF)
- `Presentation Route` (Select: UGC | PGC | HYBRID)
- `Language` (Select: BM | EN | CN)
- `Produk Nama` + `Produk Scale Anchor` (Rollup dari Products)
- `Generated Prompt` (Formula — video script template)

### Phase 3: Product Registration Form
Bina form untuk daftar produk baru terus ke Products Registry.

### Phase 4: Claude Cowork Auto-Pickup (optional advanced)
Dengan Notion MCP yang dah connect, Claude Cowork boleh:
- Scan Image Requests untuk status = NEW
- Auto-run BOSMAX pipeline
- Update status ke IN_PROGRESS → DONE
- Write output balik ke record

---

## 9. BOSMAX WORKSPACE PAGE (untuk rujukan)

User ada dua main pages:
- BOSMAX COMMAND CENTRE: https://www.notion.so/BOSMAX-COMMAND-CENTRE-36f4775af48a817685fde4c521952d81
- BOSMAX WORKSPACE: https://www.notion.so/BOSMAX-WORKSPACE-3704775af48a807c9794c20967e79353

---

## 10. TOOL YANG DIGUNAKAN

Semua dibuat via **Notion MCP** (mcp__c62f9b60-2f4f-4d25-b6e7-a4c216a4f5b0):
- `notion-create-pages` — create page + populate database records
- `notion-create-database` — create database dengan DDL schema
- `notion-update-data-source` — ADD/ALTER COLUMN (critical untuk formula complex)
- `notion-create-view` — create Form view + Table view
- `notion-update-page` — update page content
- `notion-fetch` — read page/database state

---

*Brief ini dibuat oleh Claude Cowork selepas tester confirmed working pada 2026-06-03.*
*Untuk sambung tugasan: baca section 7 (lessons learned) dan section 8 (next steps) dahulu.*
