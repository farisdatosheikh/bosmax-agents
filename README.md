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

---

## Changelog

**v11.2** — PRE-FLIGHT PROTOCOL, ENGINE CONSTRAINT TABLE (VEO_3_1_LITE ditambah), MULTI-BLOCK PROTOCOL (Master Narrative Brief), IMPLICIT REQUIREMENT DETECTION, bosmax-requirement-analyst.md (skill baru). Multi-block support untuk Mode C. Bulk generator dikemaskini dengan VEO_3_1_LITE dan GOOGLE_FLOW.

**v11.1.1** — Google Flow 4 modes, GROK image reference methodology, NANO_BANANA_PRO dan IMAGEN_3 sebagai image-only engines, bosmax-compliance-gate Google Flow audit checklist.

**v11.1** — Initial release. Tujuh skill files. Enam engines (VEO_3_1, KLING_3_0, SEEDANCE_2_0, GROK, GOOGLE_FLOW).

---

*BOSMAX v11.2 | Schema: GRAND_MASTER_SKELETON | Private — All Rights Reserved*
