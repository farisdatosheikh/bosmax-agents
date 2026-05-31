# BOSMAX CONFLICT REGISTER v1.0
**Disediakan oleh:** Claude (Orchestrator)
**Tarikh:** 2026-06-01
**Tujuan:** Pre-loaded register untuk cross-reference dengan ChatGPT Deep Research results
**Status:** AWAITING OFFICIAL VERIFICATION

---

## CARA GUNA DOKUMEN INI

Apabila ChatGPT Deep Research siap, compare setiap item dalam register ini dengan dapatan rasmi.
Setiap item ada `BOSMAX_CLAIM` vs `OFFICIAL_ANSWER` (kosong — tunggu ChatGPT).
Claude akan isi `OFFICIAL_ANSWER` dan tentukan `ACTION_REQUIRED`.

---

## RINGKASAN EXECUTIVE

| Kategori | Bilangan Isu | Status |
|---|---|---|
| 🔴 KRITIKAL — Engine specs mungkin salah | 4 | Perlu verify |
| 🟡 SEDERHANA — Tiada dalam SSOT files | 2 | Perlu verify |
| 🟢 BETUL — Sudah dihandle dengan baik | 4 | Confirmed |

---

## BAHAGIAN 1 — ENGINE DURATION SPECS
### (Ini yang paling kritikal — semua ABORT logic bersandar pada ini)

---

### ISSUE #001 — VEO_3_1: Adakah 56s valid atau hanya 8s per API call?
**Keutamaan:** 🔴 KRITIKAL
**Files yang terjejas:** `MASTER_IGNITION_TEMPLATE.md`, `SATELLITE_04_MAPPING_MATRIX.md`, `SATELLITE_05_COACHING_PROTOCOL.md`, `SOVEREIGN_01_MASTER_SCHEMA.md`, `.claude/CLAUDE.md`

**BOSMAX_CLAIM:**
```
VEO_3_1:
  max_duration: 56s
  block_max: 8s
  supported_durations: [8s, 16s, 24s, 32s, 40s, 48s, 56s]
  chaining: RECURSIVE_REINJECT_AT_EACH_BLOCK
```
Ertinya BOSMAX menganggap 56s dicapai dengan chaining 7 × 8s blocks.

**SOALAN UNTUK CHATGPT:**
1. Adakah Veo 3.1 API (`durationSeconds`) hanya terima "4", "6", "8" sahaja?
2. Adakah "4s" valid? BOSMAX tidak list ini langsung.
3. Adakah official API sokong video extension/chaining untuk hasilkan >8s?
4. Apakah perbezaan antara Veo 3.1 standard vs Veo 3.1 Lite dari segi duration?
5. Adakah Google Flow UI mampu render >8s berbanding raw API?

**OFFICIAL_ANSWER:** _(kosong — isi selepas ChatGPT research)_

**JIKA SALAH — FILES YANG PERLU DIREPAIR:**
- `MASTER_IGNITION_TEMPLATE.md` → engine_configuration.VEO_3_1.supported_durations
- `SATELLITE_04_MAPPING_MATRIX.md` → engine_duration_specs
- `SATELLITE_05_COACHING_PROTOCOL.md` → duration query string
- `SOVEREIGN_01_MASTER_SCHEMA.md` → ABORT logic lines
- `.claude/CLAUDE.md` → ENGINE CONSTRAINT TABLE (VEO_3_1 row)

---

### ISSUE #002 — VEO_3_1: Adakah "4s" duration valid?
**Keutamaan:** 🔴 KRITIKAL
**Files yang terjejas:** Sama seperti #001

**BOSMAX_CLAIM:**
```
VEO_3_1 supported_durations: [8s, 16s, 24s, 32s, 40s, 48s, 56s]
# "4s" TIDAK ADA dalam list ini
```

**SOALAN UNTUK CHATGPT:**
- Adakah Veo 3.1 API sokong `durationSeconds: "4"`?
- Kalau ya, mengapa BOSMAX tidak ada 4s dalam list?

**OFFICIAL_ANSWER:** _(kosong)_

**JIKA SALAH — ACTION:**
- Tambah "4s" ke `supported_durations` di semua files berkenaan
- Update ABORT logic: tambah `4s` sebagai valid value

---

### ISSUE #003 — GROK: 6s dan 10s — sumber adalah heuristic, bukan rasmi
**Keutamaan:** 🔴 KRITIKAL
**Files yang terjejas:** `MASTER_IGNITION_TEMPLATE.md`, `.claude/CLAUDE.md`, semua skills

**BOSMAX_CLAIM:**
```
GROK:
  max_duration: 10s
  supported_durations: [6s, 10s]
  label: [EXTERNAL_ENGINE_ADDED]  ← BOSMAX sendiri akui ini bukan verified
  restriction: FORBID_NANO_BANANA
```
Label `[EXTERNAL_ENGINE_ADDED]` bermakna ia **tidak disahkan dari sumber rasmi**.

**SOALAN UNTUK CHATGPT:**
1. Adakah xAI / Grok ada official API untuk video generation?
2. Berapa duration yang disokong? 6s? 10s? Lain-lain?
3. Apakah `NANO BANANA` dari perspektif Grok official?
4. Adakah Grok sokong I2V (image-to-video)?

**OFFICIAL_ANSWER:** _(kosong)_

**JIKA SALAH — FILES YANG PERLU DIREPAIR:**
- `MASTER_IGNITION_TEMPLATE.md` → engine_configuration.GROK
- `.claude/CLAUDE.md` → ENGINE CONSTRAINT TABLE (GROK row)
- `.claude/skills/bosmax-compliance-gate.md` → engine table
- `.claude/skills/bosmax-script-generator.md` → GROK section

---

### ISSUE #004 — KLING_3_0: 5s/10s/15s — ditandai [BOSMAX_HEURISTIC]
**Keutamaan:** 🔴 KRITIKAL
**Files yang terjejas:** `MASTER_IGNITION_TEMPLATE.md`, `.claude/CLAUDE.md`, semua skills

**BOSMAX_CLAIM:**
```
KLING_3_0:
  max_duration: 15s
  supported_durations: [5s, 10s, 15s]
  label: [BOSMAX_HEURISTIC]  ← BOSMAX sendiri akui ini heuristic!
  note: HARD_LOCK_15S_TO_PREVENT_BIOMETRIC_DRIFT
```
Label `[BOSMAX_HEURISTIC]` bermakna **ini adalah anggaran BOSMAX, bukan specs rasmi**.

**SOALAN UNTUK CHATGPT:**
1. Apakah official duration options untuk Kling 3.0? (5s? 10s? 15s? Lain?)
2. Adakah ada perbezaan antara Kling 2.1 dan 3.0 dari segi duration?
3. Adakah Kling sokong multi-block/extension untuk >15s?

**OFFICIAL_ANSWER:** _(kosong)_

**JIKA SALAH — FILES YANG PERLU DIREPAIR:**
- `MASTER_IGNITION_TEMPLATE.md` → engine_configuration.KLING_3_0
- `.claude/CLAUDE.md` → ENGINE CONSTRAINT TABLE (KLING_3_0 row)

---

### ISSUE #005 — SEEDANCE_2_0: 10s/20s — ditandai [EXTERNAL_ENGINE_ADDED]
**Keutamaan:** 🟡 SEDERHANA
**Files yang terjejas:** `MASTER_IGNITION_TEMPLATE.md`, `.claude/CLAUDE.md`

**BOSMAX_CLAIM:**
```
SEEDANCE_2_0:
  max_duration: 20s
  supported_durations: [10s, 20s]
  label: [EXTERNAL_ENGINE_ADDED]  ← bukan verified
  block_max: 10s
  chaining: EXTEND_FRAME_REFERENCE
```

**SOALAN UNTUK CHATGPT:**
1. Apakah official duration untuk Seedance 2.0 dari ByteDance?
2. Adakah 10s dan 20s betul, atau ada nilai lain?
3. Adakah Seedance 2.0 sudah publicly released dengan official API?

**OFFICIAL_ANSWER:** _(kosong)_

---

### ISSUE #006 — SORA_2: 10s–60s — perlu semak dengan OpenAI official
**Keutamaan:** 🟡 SEDERHANA
**Files yang terjejas:** `MASTER_IGNITION_TEMPLATE.md`, `.claude/CLAUDE.md`

**BOSMAX_CLAIM:**
```
SORA_2:
  max_duration: 60s
  block_max: 15s
  supported_durations: [10s, 15s, 20s, 25s, 30s, 45s, 60s]
  chaining: UI_DRAFT_STITCHING_SEQUENCE
```

**SOALAN UNTUK CHATGPT:**
1. Apakah official duration list untuk Sora 2 dari OpenAI?
2. Adakah 60s achievable via single call atau stitching sahaja?
3. Apakah `block_max` per API call untuk Sora 2?

**OFFICIAL_ANSWER:** _(kosong)_

---

## BAHAGIAN 2 — PARAMETER API

---

### ISSUE #007 — GOOGLE_FLOW: Tiada dalam MASTER_IGNITION / SOVEREIGN files
**Keutamaan:** 🔴 KRITIKAL (structural gap)
**Files yang terjejas:** `MASTER_IGNITION_TEMPLATE.md`, `SOVEREIGN_01_MASTER_SCHEMA.md`

**BOSMAX_CLAIM:**
```
GOOGLE_FLOW wujud dalam:
  - .claude/CLAUDE.md (ENGINE CONSTRAINT TABLE)
  - .claude/skills/bosmax-bulk-generator.md
  - .claude/skills/bosmax-compliance-gate.md
  - .claude/skills/bosmax-mode-c-executor.md

GOOGLE_FLOW TIDAK ADA dalam:
  - MASTER_IGNITION_TEMPLATE.md → engine_configuration ← GAP!
  - SOVEREIGN_01_MASTER_SCHEMA.md → supported_engines ← GAP!
  - SATELLITE_05_COACHING_PROTOCOL.md → engine query ← GAP!
```

**MASALAH:** SSOT (Single Source of Truth) files tidak ada GOOGLE_FLOW.
Skill files ada tapi SOVEREIGN/SATELLITE tier tidak ada → inconsistency.

**SOALAN UNTUK CHATGPT:**
1. Adakah "Google Flow" adalah nama UI untuk VideoFX atau ada API tersendiri?
2. Adakah Google Flow menggunakan Veo 3.1 sebagai backend engine?
3. Apakah perbezaan T2V, FRAMES, INGREDIENTS dalam Google Flow context?
4. Berapa maximum duration untuk Google Flow?

**ACTION REQUIRED (tanpa menunggu ChatGPT — structural fix):**
- Tambah GOOGLE_FLOW ke `MASTER_IGNITION_TEMPLATE.md` → engine_configuration
- Tambah GOOGLE_FLOW ke `SOVEREIGN_01_MASTER_SCHEMA.md` → supported_engines list
- Tambah GOOGLE_FLOW ke `SATELLITE_05_COACHING_PROTOCOL.md` → engine query

---

### ISSUE #008 — image_guidance_scale: Sudah BETUL dihandle
**Keutamaan:** 🟢 BETUL
**Status:** CONFIRMED RESOLVED

**BOSMAX_CLAIM:**
```
NOTE dalam .claude/skills/bosmax-mode-c-executor.md:
"image_guidance_scale tidak wujud dalam Veo 3.1 API — UI only, no official value"

NOTE dalam .claude/skills/bosmax-compliance-gate.md:
"image_guidance_scale: SKIP CHECK — parameter ini tidak wujud dalam Veo 3.1 API."
```

**KESIMPULAN:** BOSMAX sudah betul — parameter ini adalah UI-only, bukan API parameter.
NotebookLM's research pun sahkan ini. **Tiada repair diperlukan.**

---

### ISSUE #009 — GATE_095 (Visual-Dialog Isolation): Sudah BETUL dihandle
**Keutamaan:** 🟢 BETUL
**Status:** CONFIRMED RESOLVED

**BOSMAX_CLAIM:**
```
SOVEREIGN_03_CORE_LOGIC.md → visual_dialogue_isolation_policy:
  status: MANDATORY_FAIL_CLOSED
  forbidden_sources: [dialogue, hook, problem, agitate, solution...]
  forbidden_effect: [NO_PROP_INSTANTIATION, NO_BACKGROUND_INSTANTIATION...]
```

**KESIMPULAN:** GATE_095 sudah fully implemented dalam SOVEREIGN_03.
Dialog diasingkan dari visual prompt. **Tiada repair diperlukan.**

---

### ISSUE #010 — dna_reinjection_hop: Perlu verify API support
**Keutamaan:** 🟡 SEDERHANA
**Files yang terjejas:** `MASTER_IGNITION_TEMPLATE.md`, `.claude/skills/bosmax-script-generator.md`

**BOSMAX_CLAIM:**
```
dna_reinjection_hop: "inject DNA token pada setiap block boundary"
identity_lock: HIGH_FIDELITY_INGREDIENTS
referenceImages: max 3 (untuk Veo 3.1)
```

**SOALAN UNTUK CHATGPT:**
1. Adakah Veo 3.1 API `referenceImages` (max 3) sokong character consistency merentas chained clips?
2. Bagaimana cara rasmi untuk maintain character identity merentas multiple Veo 3.1 clips?
3. Adakah ada `dna_reinjection` atau equivalent dalam official Veo API?

**OFFICIAL_ANSWER:** _(kosong)_

---

### ISSUE #011 — NANO BANANA: Perlu verify apa sebenarnya dari Grok
**Keutamaan:** 🟡 SEDERHANA
**Files yang terjejas:** `.claude/CLAUDE.md`, `SOVEREIGN_01_MASTER_SCHEMA.md`

**BOSMAX_CLAIM:**
```
BOSMAX forbids "NANO BANANA" submode untuk GROK.
ERR_NANO_BANANA_BREACH: FORBIDDEN SUBMODE
```

**SOALAN UNTUK CHATGPT:**
1. Dari perspektif Grok/xAI official, apakah "Nano" mode?
2. Mengapa ia bermasalah untuk commercial video generation?
3. Adakah ada nama rasmi untuk submode ini?

**OFFICIAL_ANSWER:** _(kosong)_

---

## BAHAGIAN 3 — STRUCTURAL GAPS (Tiada dalam SSOT)

---

### ISSUE #012 — manual_senibina_prompt_v1.pdf: Bukan conflict, tapi mismatch context
**Keutamaan:** 🟢 CLARIFICATION ONLY

**DIAGNOSIS:**
File PDF ini adalah dokumen **tutorial/reference** dari third-party (bukan official API docs).
Ia menunjukkan teknik untuk platform tersebut dari perspektif UI user, bukan API developer.

**Teknik dalam PDF yang BETUL secara API:**
- 9-section structure → BOSMAX adopt ini ✅
- referenceImages untuk character consistency → BOSMAX guna ini ✅
- dialog diasingkan dari visual → GATE_095 enforce ini ✅

**Teknik dalam PDF yang TIDAK SESUAI untuk BOSMAX automation:**
- Manual frame-grabbing → BOSMAX gantikan dengan dna_reinjection_hop ✅
- Dialog terus dalam visual prompt → BOSMAX forbid via GATE_095 ✅

**KESIMPULAN:** PDF ini tidak bercanggah dengan BOSMAX. BOSMAX sudah upgrade semua manual teknik kepada automated equivalents. **Tiada repair diperlukan untuk PDF conflict.**

---

## BAHAGIAN 4 — CHECKLIST UNTUK CLAUDE (POST-CHATGPT)

Bila boss forward hasil ChatGPT Deep Research, Claude akan:

```
□ Verify ISSUE #001 → VEO_3_1 duration caps
□ Verify ISSUE #002 → "4s" missing from VEO_3_1?
□ Verify ISSUE #003 → GROK 6s/10s official?
□ Verify ISSUE #004 → KLING_3_0 [BOSMAX_HEURISTIC] — betul atau salah?
□ Verify ISSUE #005 → SEEDANCE_2_0 duration official?
□ Verify ISSUE #006 → SORA_2 duration list official?
□ Verify ISSUE #007 → GOOGLE_FLOW API vs UI — structural gap fix
□ Verify ISSUE #010 → dna_reinjection via referenceImages API?
□ Verify ISSUE #011 → NANO BANANA official name?
```

Selepas verify, Claude akan output:
1. **REPAIR LIST** — senarai exact edits per file
2. **PURGE LIST** — specs yang salah, kena delete
3. **CODEX PROMPT** — surgical edit instructions untuk Codex

---

## BAHAGIAN 5 — FILES YANG MUNGKIN TERJEJAS (Pre-mapped)

| File | Issues | Kemungkinan Action |
|---|---|---|
| `MASTER_IGNITION_TEMPLATE.md` | #001,#002,#003,#004,#005,#006,#007 | UPDATE engine_configuration |
| `.claude/CLAUDE.md` | #001,#002,#003,#004,#005,#006 | UPDATE ENGINE CONSTRAINT TABLE |
| `SOVEREIGN_01_MASTER_SCHEMA.md` | #001,#003,#004,#007 | UPDATE ABORT logic + supported_engines |
| `SATELLITE_04_MAPPING_MATRIX.md` | #001,#003,#004 | UPDATE engine_duration_specs |
| `SATELLITE_05_COACHING_PROTOCOL.md` | #001,#003,#004,#007 | UPDATE duration query + engine list |
| `.claude/skills/bosmax-compliance-gate.md` | #003,#004,#007 | UPDATE engine table |
| `.claude/skills/bosmax-script-generator.md` | #003 | UPDATE GROK section |
| `.claude/skills/bosmax-mode-c-executor.md` | #003,#007 | UPDATE engine caps |
| `.claude/skills/bosmax-bulk-generator.md` | #003,#007 | UPDATE engine table |

---

*Dokumen ini akan dikemaskini oleh Claude selepas ChatGPT Deep Research results diterima.*
*Version: v1.0 | Next update: v1.1 (post-ChatGPT verification)*
