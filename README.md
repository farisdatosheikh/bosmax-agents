# BOSMAX v11.2 — Commercial Content Command Centre

**BOSMAX** adalah sistem penjanaan konten komersial untuk pasaran SEA (TikTok Shop MY, Shopee, Lazada, Meta).

Sistem ini mengorkestrasi pipeline imej, video, dan pendaftaran produk menggunakan arkitektur multi-agent fail-closed.

---

## Struktur Sistem

`
BOSMAX/
├── .claude/
│   ├── CLAUDE.md                    ← Orchestrator brain (routing logic)
│   ├── BOSMAX-LOG.md                ← Session memory & product registry
│   └── skills/
│       ├── bosmax-compliance-gate.md     ← Final quality auditor
│       ├── bosmax-subject-dna.md         ← Character visual identity (Mode A)
│       ├── bosmax-scene-engine.md        ← Scene & lighting engine (Mode A)
│       ├── bosmax-mode-c-executor.md     ← Image-to-video inheritance (Mode C)
│       ├── bosmax-script-generator.md    ← Video script builder (Mode B)
│       ├── bosmax-product-registration.md ← TikTok Shop MY product intake
│       ├── bosmax-bulk-generator.md      ← Bulk prompt factory (T2V/FRAMES/INGREDIENTS/IMAGE)
│       └── bosmax-requirement-analyst.md ← Pre-dispatch intelligence layer (v11.2)
├── BOSMAX_DETERMINISTIC_FLOW_v1.md  ← Phase-1 newbie-facing single-output authority
├── BOSMAX_BATCH_LANE_v1.md          ← Phase-2 deterministic batch authority
├── BOSMAX_BATCH_TEMPLATE_SET_v1.md  ← Production-ready batch intake templates
├── BOSMAX_INPUT_HELPER_v1.md        ← Front-door field helper for operators
├── BOSMAX_IGNITION_WORKFLOW_v1.md   ← Front-door ignition / repair / variation templates
├── BOSMAX_OPERATOR_DRY_RUN_MINYAK_WARISAN_CAP_BURUNG_v1.md ← First real front-door operator walkthrough
├── BOSMAX_BATCH_RUN_EXAMPLE_MINYAK_WARISAN_CAP_BURUNG_v1.md ← First real batch benchmark
├── BOSMAX_BATCH_RUN_EXAMPLE_VIDEO_FRESH_MINYAK_WARISAN_CAP_BURUNG_v1.md ← First real video batch benchmark
├── BOSMAX_BATCH_RUN_EXAMPLE_MIXED_DETERMINISTIC_MINYAK_WARISAN_CAP_BURUNG_v1.md ← First real mixed batch benchmark
├── BOSMAX_BATCH_RUN_EXAMPLE_MULTI_PRODUCT_CONTROLLED_MINYAK_WARISAN_CAP_BURUNG_JUNGLE_GIRL_v1.md ← First real multi-product batch benchmark
├── BOSMAX_BATCH_RUN_EXAMPLE_VIDEO_FRESH_MAVERIX_MAXOIL_v1.md ← First sensitive Maverix video benchmark
├── BOSMAX_BATCH_RUN_EXAMPLE_MULTI_PRODUCT_CONTROLLED_SENSITIVE_BOSMAX_SERUM_MAVERIX_MAXOIL_v1.md ← First sensitive multi-product benchmark
├── BOSMAX_BATCH_RUN_EXAMPLE_IMAGE_SENSITIVE_MAVERIX_MAXOIL_v1.md ← First sensitive image benchmark
├── SOVEREIGN_01_MASTER_SCHEMA.md    ← Master system schema
├── SOVEREIGN_02_PHYSICS_DNA.md      ← Physics DNA authority
├── SOVEREIGN_03_CORE_LOGIC.md       ← Core logic rules
├── SATELLITE_01_ORCHESTRATOR.md     ← Satellite orchestrator
├── Visual_Language_v1_STRICT.yaml   ← Visual language authority
├── Prompt_Framework_v1_STRICT.yaml  ← Prompt framework rules
├── Model_Behaviour_v1_STRICT.yaml   ← Model behaviour rules
├── Platform_Specs_v1_STRICT.yaml    ← Platform spec reference
└── SCRIPT_REGISTRY_UNIFIED.md       ← Unified script registry
`

---

## Pipeline Routes

| Route | Trigger | Pipeline |
|-------|---------|----------|
| **A** | Image generation | Subject DNA → Scene Engine → Compliance Gate |
| **B** | Video dari zero | [PRE-FLIGHT] → Requirement Analyst → Script Generator → Compliance Gate |
| **C** | Video dari gambar sedia ada | [PRE-FLIGHT] → Requirement Analyst → Mode-C Executor → Compliance Gate |
| **REG** | Daftar produk TikTok Shop | Product Registration |
| **BULK** | 10–50 prompt sets | Product Registration → Bulk Generator → Variant Plan → Deterministic Expansion → Compliance Gate |

**Multi-block support:** VEO_3_1_LITE, KLING_3_0, SEEDANCE_2_0, GROK — auto-triggered apabila duration_target > engine max/block.

---

## Engines

**Video:** VEO_3_1_LITE | VEO_3_1 | KLING_3_0 | SEEDANCE_2_0 | GROK | GOOGLE_FLOW

**Image:** NANO_BANANA_PRO | IMAGEN_3

---

## Cara Guna

Sistem ini direka untuk dijalankan melalui **Claude Cowork** dengan .claude/CLAUDE.md sebagai orchestrator.

Semua output melalui bosmax-compliance-gate sebelum sampai kepada pengguna.

**Phase-1 deterministic flow:** rujuk `BOSMAX_DETERMINISTIC_FLOW_v1.md`.
Fail ini mendefinisikan front-door newbie flow untuk:
- `IMAGE → VIDEO_SUPPORT | SELLING_POSTER`
- `VIDEO → NONE | IMAGE_REFERENCE | VIDEO_REFERENCE | BOSMAX_IMAGE_HANDOFF`

**Front-door field helper:** rujuk `BOSMAX_INPUT_HELPER_v1.md`.
Fail ini menormalkan field intake supaya operator tidak perlu teka:
- platform
- category wording
- variant
- exact scale anchor
- engine normalization
- Google Flow / GROK mode hints

**Front-door ignition workflow:** rujuk `BOSMAX_IGNITION_WORKFLOW_v1.md`.
Fail ini menyediakan operator-ready flow untuk:
- `IGNITION`
- `REPAIR`
- `VARIATION`

**First real front-door dry run:** rujuk `BOSMAX_OPERATOR_DRY_RUN_MINYAK_WARISAN_CAP_BURUNG_v1.md`.
Fail ini menunjukkan satu walkthrough operator sebenar untuk:
- `Minyak Warisan Cap Burung`
- `IMAGE + SELLING_POSTER`
- `Input Helper → Ignition → Repair → Variation`
- sebelum naik ke batch lane

**Phase-2 deterministic batch lane:** rujuk `BOSMAX_BATCH_LANE_v1.md`.
Fail ini mendefinisikan batch sebagai planner/dispatcher di atas single-output flow:
- `BATCH_IMAGE_SUPPORT`
- `BATCH_IMAGE_SELLING`
- `BATCH_VIDEO_FRESH`
- `BATCH_MIXED_DETERMINISTIC`

**Production-ready batch templates:** rujuk `BOSMAX_BATCH_TEMPLATE_SET_v1.md`.
Fail ini mengandungi ready-copy intake blocks untuk:
- `BATCH_IMAGE_SUPPORT`
- `BATCH_IMAGE_SELLING`
- `BATCH_VIDEO_FRESH`
- `BATCH_MIXED_DETERMINISTIC`
- `BATCH_MULTI_PRODUCT_CONTROLLED`

**First real batch benchmark:** rujuk `BOSMAX_BATCH_RUN_EXAMPLE_MINYAK_WARISAN_CAP_BURUNG_v1.md`.
Fail ini menunjukkan satu contoh batch sebenar untuk:
- `Minyak Warisan Cap Burung`
- `BATCH_IMAGE_SELLING`
- `10` outputs
- complete intake block + approved Variant Plan example

**Companion video benchmark:** rujuk `BOSMAX_BATCH_RUN_EXAMPLE_VIDEO_FRESH_MINYAK_WARISAN_CAP_BURUNG_v1.md`.
Fail ini menunjukkan satu contoh batch sebenar untuk:
- `Minyak Warisan Cap Burung`
- `BATCH_VIDEO_FRESH`
- `KLING_3_0`
- `10s`
- `10` outputs
- complete intake block + approved Variant Plan example

**Companion mixed benchmark:** rujuk `BOSMAX_BATCH_RUN_EXAMPLE_MIXED_DETERMINISTIC_MINYAK_WARISAN_CAP_BURUNG_v1.md`.
Fail ini menunjukkan satu contoh batch sebenar untuk:
- `Minyak Warisan Cap Burung`
- `BATCH_MIXED_DETERMINISTIC`
- `5 × IMAGE + VIDEO_SUPPORT`
- `5 × VIDEO + NONE`
- `KLING_3_0`
- `10s`
- `10` outputs
- complete intake block + approved Variant Plan example

**Companion multi-product benchmark:** rujuk `BOSMAX_BATCH_RUN_EXAMPLE_MULTI_PRODUCT_CONTROLLED_MINYAK_WARISAN_CAP_BURUNG_JUNGLE_GIRL_v1.md`.
Fail ini menunjukkan satu contoh batch sebenar untuk:
- `Minyak Warisan Cap Burung`
- `Minyak Jungle Girl`
- `BATCH_MULTI_PRODUCT_CONTROLLED`
- `IMAGE_ONLY`
- `10` outputs
- complete intake block + approved Variant Plan example

**Direct product registry addition:** `products/JUNGLE_GIRL_MINYAK.yaml` kini wujud sebagai authority provisional yang dipromote dari FASTMOSS tier-2 untuk benchmark multi-product rendah risiko.

**Sensitive Maverix benchmark:** rujuk `BOSMAX_BATCH_RUN_EXAMPLE_VIDEO_FRESH_MAVERIX_MAXOIL_v1.md`.
Fail ini menunjukkan satu contoh batch sensitif sebenar untuk:
- `Maverix Maxoil`
- `BATCH_VIDEO_FRESH`
- `KLING_3_0`
- `10s`
- `10` outputs
- dialogue authority: `male_health_stealth_01 / EGO_01`

**Sensitive multi-product benchmark:** rujuk `BOSMAX_BATCH_RUN_EXAMPLE_MULTI_PRODUCT_CONTROLLED_SENSITIVE_BOSMAX_SERUM_MAVERIX_MAXOIL_v1.md`.
Fail ini menunjukkan satu contoh batch sensitif dua produk untuk:
- `BOSMAX Serum`
- `Maverix Maxoil`
- `BATCH_MULTI_PRODUCT_CONTROLLED`
- `VIDEO_ONLY`
- `10` outputs
- shared stealth dialogue authority

**Sensitive product registry addition:** `products/MAVERIX_MAXOIL.yaml` kini wujud sebagai authority sensitive-product tier-1 yang di-bind terus kepada `SCRIPT_REGISTRY_UNIFIED.md` dan `SCRIPT_VARIANT_LIBRARY.md`.

**Sensitive Maverix image benchmark:** rujuk `BOSMAX_BATCH_RUN_EXAMPLE_IMAGE_SENSITIVE_MAVERIX_MAXOIL_v1.md`.
Fail ini menunjukkan satu contoh image benchmark sensitif sebenar untuk:
- `Maverix Maxoil`
- `BATCH_IMAGE_SELLING`
- `10` outputs
- reference-bound product truth from actual FastMoss product images

**Front-door lock-down sequence:**
1. gunakan `BOSMAX_INPUT_HELPER_v1.md` untuk isi field dengan betul
2. gunakan `BOSMAX_IGNITION_WORKFLOW_v1.md` untuk first prompt
3. jika output hampir betul, guna repair template
4. jika output sudah betul, guna variation template
5. jika perlu banyak outputs, naik ke batch lane

---

## Changelog

**v11.2** — PRE-FLIGHT PROTOCOL, ENGINE CONSTRAINT TABLE (VEO_3_1_LITE ditambah), MULTI-BLOCK PROTOCOL (Master Narrative Brief), IMPLICIT REQUIREMENT DETECTION, bosmax-requirement-analyst.md (skill baru). Multi-block support untuk Mode C. Bulk generator dikemaskini dengan VEO_3_1_LITE dan GOOGLE_FLOW.

**v11.1.1** — Google Flow 4 modes, GROK image reference methodology, NANO_BANANA_PRO dan IMAGEN_3 sebagai image-only engines, bosmax-compliance-gate Google Flow audit checklist.

**v11.1** — Initial release. Tujuh skill files. Enam engines (VEO_3_1, KLING_3_0, SEEDANCE_2_0, GROK, GOOGLE_FLOW).

---

*BOSMAX v11.2 | Schema: GRAND_MASTER_SKELETON | Private — All Rights Reserved*
