# BOSMAX v11.1 — Commercial Content Command Centre

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
│       └── bosmax-bulk-generator.md      ← Bulk prompt factory (T2V/FRAMES/INGREDIENTS/IMAGE)
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
| **B** | Video dari zero | Script Generator → Compliance Gate |
| **C** | Video dari gambar sedia ada | Mode-C Executor → Compliance Gate |
| **REG** | Daftar produk TikTok Shop | Product Registration |
| **BULK** | 10–50 prompt sets | Product Registration → Bulk Generator → Compliance Gate |

---

## Engines

**Video:** VEO_3_1 | SORA_2 | KLING_3_0 | SEEDANCE_2_0 | GROK | GOOGLE_FLOW

**Image:** NANO_BANANA_PRO | IMAGEN_3

---

## Cara Guna

Sistem ini direka untuk dijalankan melalui **Claude Cowork** dengan .claude/CLAUDE.md sebagai orchestrator.

Semua output melalui osmax-compliance-gate sebelum sampai kepada pengguna.

---

*BOSMAX v11.1 | Schema: GRAND_MASTER_SKELETON | Private — All Rights Reserved*
