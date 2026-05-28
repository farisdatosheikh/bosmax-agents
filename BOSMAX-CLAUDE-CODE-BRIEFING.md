# BOSMAX ECOSYSTEM — CLAUDE CODE BRIEFING
## Context Handoff | Schema v11.2 | Date: 2026-05-28
## Authority: SUPREME_SYSTEMS_ARCHITECT (pldsb.faris@gmail.com)

---

## SIAPA KAMU DAN APA KERJA KAMU

Kamu adalah Claude Code yang di-assign untuk handle **BOSMAX v11.2 ecosystem** —
sistem penjanaan konten komersial SEA (TikTok Shop MY, Shopee, Lazada, Meta).

BOSMAX adalah multi-agent orchestration system. Ia bukan satu AI — ia adalah
satu **Command Centre** yang route setiap request kepada specialist skill yang betul,
kemudian output HANYA selepas Compliance Gate mengesahkan.

Kamu MESTI membaca file-file ini SEBELUM buat apa-apa kerja:
1. `.claude/CLAUDE.md` — otak BOSMAX orchestrator (authority utama)
2. `.claude/BOSMAX-LOG.md` — session memory dan product registry

---

## GITHUB REPO

```
Repo:     farisdatosheikh/bosmax-agents (PRIVATE)
Branch:   master
Owner:    farisdatosheikh@gmail.com
```

Semua file BOSMAX disimpan dan di-version-control dalam repo ini.
Setiap kali buat perubahan pada mana-mana skill file atau CLAUDE.md,
WAJIB commit dengan message yang jelas dan push ke GitHub.

---

## FILE STRUCTURE

```
project root/
├── .claude/
│   ├── CLAUDE.md                        ← BOSMAX orchestrator brain (MASTER)
│   ├── BOSMAX-LOG.md                    ← session memory, product registry
│   └── skills/
│       ├── bosmax-compliance-gate.md    ← final QA gate, semua output melalui sini
│       ├── bosmax-subject-dna.md        ← Mode A: biometric + product DNA generator
│       ├── bosmax-scene-engine.md       ← Mode A: scene + image prompt builder
│       ├── bosmax-mode-c-executor.md    ← Mode C: animate existing image
│       ├── bosmax-script-generator.md   ← Mode B: 9-section video script engine
│       ├── bosmax-product-registration.md ← ROUTE REG: TikTok Shop MY product intake
│       ├── bosmax-bulk-generator.md     ← ROUTE BULK: multi-set prompt factory
│       └── bosmax-requirement-analyst.md ← PRE-DISPATCH: requirement extraction layer
├── [sovereign files]                    ← physics classes, prompt framework YAML
├── [satellite files]                    ← scene registry, avatar registry
└── README.md
```

---

## VERSI SEMASA: v11.2

Schema versi ini ditulis dalam header setiap file. Kalau kamu nampak `v11.1` dalam
mana-mana file yang kamu edit, kemaskini kepada `v11.2`.

---

## SEJARAH RINGKAS — APA YANG BERUBAH DARI v11.1 KE v11.2

### Bug asal yang ditutup:
VEO 3.1 Lite (max 8s per block) bila diberi request "16s video" — sistem generate
SATU prompt 16s tanpa detect bahawa engine tidak support single-block melebihi 8s.
Ini bermakna output salah sebelum penjanaan bermula. ChatGPT dan BOSMAX kedua-duanya
gagal kerana tiada layer yang detect dan resolve keperluan multi-block.

### Root causes:
1. VEO_3_1_LITE tidak ada dalam ENGINE REGISTRY langsung
2. Tiada MULTI-BLOCK PROTOCOL — tiada konsep "pecah kepada N blocks"
3. Tiada PRE-FLIGHT validation sebelum dispatch ke skill
4. Tiada pre-dispatch intelligence layer

### 4 Fixes yang telah dilaksanakan (semua committed ke GitHub):

**Fix A (commit 3a0d5cb) — CLAUDE.md updated to v11.2:**
- Tambah PRE-FLIGHT PROTOCOL (5 steps wajib sebelum route)
- Tambah ENGINE CONSTRAINT TABLE (semua engines dengan max/block, durations)
- Tambah MULTI-BLOCK PROTOCOL (STEP 3A–3E: announce → brief → approval → dispatch)
- Tambah IMPLICIT REQUIREMENT DETECTION table (10 scenarios)
- Update PIPELINE SEQUENCES dengan [PRE-FLIGHT] dalam semua pipeline

**Fix B (commit 9729171) — bosmax-requirement-analyst.md CREATED:**
- Skill baru: "Story Editor" pre-dispatch layer
- Baca full request → extract explicit + implicit requirements
- Detect conflicts → issue WORK ORDER atau BLOCKER
- Analogi: Story Editor → Director (BOSMAX) → Crew (Skills) → QC (Compliance Gate)

**Fix C (commit a454ebc) — bosmax-script-generator.md + bosmax-compliance-gate.md:**
- Script generator: tambah multi-block work order intake, Block 1/Block 2+ rules,
  visual state handoff dalam S8, dialogue carry-over anchors
- Compliance gate: tambah MULTI-BLOCK CONTINUITY AUDIT CHECKLIST (5 sub-checklists),
  detect dialogue restart, biometric drift, scene continuity across blocks

**Fix D (commit c5f9c60) — GROK dual-duration multi-block:**
- GROK ada dua pilihan base unit: 6s atau 10s per block
- TIDAK boleh auto-resolve (berbeza dari VEO_3_1_LITE yang fixed 8s)
- BOSMAX MESTI tanya user untuk confirm block distribution sebelum build brief
- Contoh: "20s GROK → A) 2×10s  B) 10s+10s — pilih mana?"
- Update dalam: CLAUDE.md, bosmax-requirement-analyst.md, bosmax-script-generator.md

---

## ARCHITECTURE — KONSEP PALING KRITIKAL

### 1. PRE-FLIGHT PROTOCOL (WAJIB — tiada pengecualian)
Setiap request MESTI melalui 5 steps sebelum route ke mana-mana skill:
```
STEP 1 → Extract 8 requirement fields
STEP 2 → Validate (6 checks: platform, engine lookup, duration vs max, Mode C prereqs, BULK prereqs, Google Flow images)
STEP 3 → Multi-block protocol (jika duration > engine_max)
STEP 4 → Implicit requirement detection
STEP 5 → Issue WORK ORDER
```

### 2. ENGINE CONSTRAINT TABLE (rujukan mutlak)
```
VEO_3_1_LITE  → max 8s/block   (multi-block auto: fixed 8s)
VEO_3_1       → max 56s/block
SORA_2        → max 60s/block
KLING_3_0     → max 15s/block  (multi-block auto: fixed 15s)
SEEDANCE_2_0  → max 20s/block  (multi-block auto: fixed 20s)
GROK          → max 10s/block  (multi-block: TANYA user — 6s atau 10s base unit)
GOOGLE_FLOW   → max 60s, bukan 9-section, guna block architecture
```
ABORT terus jika engine tidak dalam table ini.

### 3. MULTI-BLOCK — 3 RULES YANG TIDAK BOLEH DILANGGAR
- Tiada single prompt untuk duration yang melebihi engine max
- Master Narrative Brief MESTI diapprove user sebelum generate mana-mana block
- Dialogue Block N MESTI sambung dari last words Block N-1 — tiada restart

### 4. ROUTING SEQUENCE
```
User request → PRE-FLIGHT → WORK ORDER → Route ke skill → Compliance Gate → User
```
BOSMAX orchestrator TIDAK generate content.
Output kepada user HANYA selepas VERIFICATION PASSED dari Compliance Gate.

### 5. ROUTE MAP
```
ROUTE A   → Image: subject-dna → scene-engine → compliance-gate
ROUTE B   → Video dari kosong: script-generator → compliance-gate
ROUTE C   → Video dari gambar: mode-c-executor → compliance-gate
ROUTE REG → Daftar produk: product-registration → (optional) bulk-generator
ROUTE BULK→ Bulk prompts: product-registration → bulk-generator → compliance-gate
```

---

## MEMORY PROTOCOL

- Baca `.claude/BOSMAX-LOG.md` pada awal setiap session
- Update BOSMAX-LOG.md selepas setiap product_record baru
- Update BOSMAX-LOG.md selepas setiap source_image_handoff baru
- Jangan carry forward data lama ke session baru tanpa verify

---

## FAIL-CLOSED RULES — TIDAK BOLEH DILANGGAR

1. JANGAN generate creative content secara terus
2. JANGAN output kepada user tanpa VERIFICATION PASSED dari compliance gate
3. JANGAN dispatch ke skill tanpa PRE-FLIGHT selesai
4. JANGAN assume engine capability — MESTI rujuk ENGINE CONSTRAINT TABLE
5. JANGAN generate single block untuk duration > engine_max
6. JANGAN build Master Narrative Brief tanpa user approval
7. JANGAN allow Block 2+ dialogue restart
8. JANGAN auto-resolve GROK multi-block — tanya user dahulu
9. JANGAN mix Mode A dan Mode B variables dalam workspace yang sama
10. JANGAN generate GROK dengan NANO BANANA submode

---

## APA YANG BELUM DIBUAT (POTENTIAL GAPS)

Ini adalah gaps yang diketahui semasa handoff ini ditulis (2026-05-28):

1. **bosmax-mode-c-executor.md** — belum dikemaskini untuk multi-block Mode C.
   Jika user request "animate 16s video dari gambar" dengan VEO Lite,
   mode-c-executor perlu inherit source_image_handoff DAN support block continuity.
   Fix belum dilaksanakan.

2. **bosmax-bulk-generator.md** — engine registry dalam fail ini masih v11.1
   (tiada VEO_3_1_LITE). Jika bulk generation guna VEO Lite, engine validation
   dalam bulk generator tidak akan match. Perlu align dengan ENGINE CONSTRAINT TABLE.

3. **bosmax-compliance-gate.md** — Mode C multi-block audit masih basic.
   Hanya ada generic multi-block checklist. Mode C-specific inheritance lock
   checks (subject_dna LOCKED across blocks) belum dimasukkan ke dalam
   MULTI-BLOCK CONTINUITY AUDIT secara eksplisit.

4. **README.md** — masih v11.1 overview. Belum reflect perubahan v11.2
   (PRE-FLIGHT, Engine Constraint Table, Requirement Analyst, GROK dual-duration).

5. **BOSMAX-LOG.md** — masih v11.1 header. Schema version belum dikemaskini.

---

## CARA KERJA DENGAN ECOSYSTEM INI

Bila ada task baru yang datang:
1. Baca CLAUDE.md dahulu (authority utama)
2. Identify file mana yang perlu diubah
3. Buat perubahan
4. Verify perubahan konsisten dengan CLAUDE.md dan fail-closed rules
5. Commit dengan message yang specific (contoh: "Fix X: [apa yang berubah dan kenapa]")
6. Push ke GitHub
7. Report kepada owner: apa yang berubah, kenapa, proof (git log)

JANGAN buat perubahan pada CLAUDE.md tanpa faham kesan downstream kepada semua 8 skill files.

---

*Briefing ini ditulis oleh Cowork session pada 2026-05-28.*
*GitHub: farisdatosheikh/bosmax-agents | Branch: master | Schema: v11.2*
