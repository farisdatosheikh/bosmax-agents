# BOSMAX ENGINE SPECS — ANALISIS PENUH
**Disediakan oleh:** Claude (Orchestrator)
**Tarikh:** 2026-06-01
**Sumber:** ChatGPT Deep Research (Official API docs only) + BOSMAX Ecosystem Scan
**Status:** SIAP UNTUK KELULUSAN BOSS → kemudian hantar ke Codex

---

## RINGKASAN EKSEKUTIF

Daripada 5 engines dalam BOSMAX, **4 engines ada specs yang salah atau tidak lengkap.**
Satu engine ada **DEPRECATION WARNING kritikal** yang perlu tindakan segera.

| Engine | Status | Keterukan |
|---|---|---|
| VEO_3_1 / Google Flow | ⚠️ PARTIAL WRONG | Durations missing, extension logic berbeza |
| GROK | 🔴 MAJOR WRONG | Max salah, range salah, ref images lebih |
| SEEDANCE_2_0 | 🔴 MAJOR WRONG | Max salah (20s→15s), presets salah |
| SORA_2 | 🔴 CRITICAL WRONG + ⚠️ DEPRECATED | Semua specs salah + API tutup 2026-09-24 |
| KLING_3_0 | 🟡 MINOR WRONG | API-vs-product conflict, "3s" missing |

---

## BAHAGIAN 1 — ANALISIS SETIAP ENGINE

---

### ENGINE 1: VEO_3_1 / GOOGLE FLOW

#### Perbandingan:

| Field | BOSMAX CLAIM | OFFICIAL (ChatGPT) | Verdict |
|---|---|---|---|
| Max per raw API call | 8s ✅ | 8s | BETUL |
| Allowed durations | [8s, 16s, 24s...56s] | **"4", "6", "8"** | ❌ SALAH — missing 4s & 6s |
| Multi-block max | 56s (7×8s) | Extension: 7s/block × 20 = **~148s** | ⚠️ KONSEP BETUL, MATH BERBEZA |
| Google Flow clip | N/A | **10s** (Flow UI layer) | ✅ Ini justify kenapa GOOGLE_FLOW = separate ID |
| referenceImages max | 3 | **3** | BETUL ✅ |
| VEO_3_1_LITE max | 8s | 8s, same durations, **no 4k, no extension** | BETUL ✅ |
| 1080p/4k requires | 8s | **8s mandatory** | BETUL ✅ |
| Extension duration/block | "8s per block" | **7s per extension** (bukan 8s!) | ⚠️ MINOR WRONG |

#### DIAGNOSIS:
1. **`durationSeconds: "4"` dan `"6"` tidak ada dalam BOSMAX** — ini missing valid API values
2. **Extension adds 7s** per call (bukan 8s) — BOSMAX math untuk multi-block VEO perlu adjust
3. **Google Flow 10s** = UI layer capability, VEO_3_1 raw API = 8s max. Dua layer berbeza ✅
4. NANO_BANANA_PRO / IMAGEN_3 tidak berkaitan dengan Veo API — ini adalah image engines

#### WHAT NEEDS FIX:
```
ADD "4s", "6s" ke VEO_3_1 supported_durations
NOTE extension = 7s/block (bukan 8s) — max 20 extensions = ~148s total
GOOGLE_FLOW separate ID KEKAL — betul ada dua layer
```

---

### ENGINE 2: GROK (xAI Grok Imagine Video)

#### Perbandingan:

| Field | BOSMAX CLAIM | OFFICIAL (ChatGPT) | Verdict |
|---|---|---|---|
| Max duration | **10s** | **15s** | 🔴 SALAH |
| Supported durations | [6s, 10s] | **1–15s (continuous range)** | 🔴 SALAH SEPENUHNYA |
| Aspect ratios | (tidak disebut) | 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3 | 🔴 MISSING |
| Resolution | (tidak disebut) | 480p default, 720p | 🔴 MISSING |
| Reference images max | (3 — assumed) | **7 reference images** (ref-to-video mode) | 🔴 SALAH |
| Reference-to-video cap | N/A | **10s max** bila guna reference images | ⚠️ NEW INFO |
| Video extension | N/A | **Yes — input 2-15s, extend by 2-10s** | NEW INFO |
| NANO BANANA | FORBIDDEN | **Not found in official docs** | ❓ UNVERIFIED |
| Model name | "GROK" | `grok-imagine-video` via `/v1/videos/generations` | INFO |

#### DIAGNOSIS:
1. **Max duration 15s (bukan 10s)** — BOSMAX underestimate kemampuan Grok
2. **Range 1-15s adalah continuous** — bukan preset [6s, 10s] sahaja
3. **Reference images boleh sampai 7** (bukan 3) — tapi bila guna ini, duration cap at 10s
4. **NANO BANANA** — tiada dalam official docs. Ini mungkin internal BOSMAX term atau community jargon. **Keep restriction tapi tukar label kepada [BOSMAX_INTERNAL_RESTRICTION]**
5. **Video extension wujud** — ini capability baru yang perlu added ke ecosystem

#### WHAT NEEDS FIX:
```
UPDATE GROK max_duration: 10s → 15s
UPDATE GROK supported_durations: [6s, 10s] → range 1-15s
ADD GROK aspect_ratios list
ADD GROK resolution specs
ADD GROK reference-to-video: max 7 images, capped at 10s
ADD GROK extension capability
RELABEL NANO_BANANA → [BOSMAX_INTERNAL_RESTRICTION]
```

---

### ENGINE 3: KLING 3.0

#### Perbandingan:

| Field | BOSMAX CLAIM | OFFICIAL (ChatGPT) | Verdict |
|---|---|---|---|
| Supported durations (API) | [5s, 10s, 15s] | **3s, 5s, 10s** (API ref) | ⚠️ CONFLICT |
| Max duration (API ref) | 15s | **10s** (API ref) | ⚠️ API ref says 10s |
| Max duration (product page) | 15s | **15s** (product/UI) | ✅ Product page betul |
| Label dalam BOSMAX | [BOSMAX_HEURISTIC] | — | ⚠️ BOSMAX sendiri akui tidak verified |
| "3s" duration | Tiada | **3s** valid (API ref) | 🔴 MISSING |

#### DIAGNOSIS:
1. **"3s" tidak ada dalam BOSMAX** — perlu ditambah
2. **API ref = 3s/5s/10s; Product page = up to 15s** — ada API-vs-product conflict
3. ChatGPT rekemen: **treat as 10s max** untuk API-safe validation sehingga API ref update ke 15s
4. BOSMAX mesti maintain dua layers: `KLING_3_0_API_SAFE` (max 10s) dan `KLING_3_0_UI` (max 15s)

#### WHAT NEEDS FIX:
```
ADD "3s" ke KLING_3_0 supported_durations
SET safe_api_max: 10s (dengan note: product page claims 15s, API ref unverified)
ADD note: [API_VS_PRODUCT_CONFLICT — validate before using 15s]
```

---

### ENGINE 4: SEEDANCE 2.0

#### Perbandingan:

| Field | BOSMAX CLAIM | OFFICIAL (ChatGPT) | Verdict |
|---|---|---|---|
| Max duration | **20s** | **15s** | 🔴 SALAH |
| Supported durations | [10s, 20s] | **4–15s variable range** | 🔴 SALAH SEPENUHNYA |
| Duration type | Fixed presets | **Variable/continuous** | 🔴 KONSEP SALAH |
| Aspect ratios | (tidak disebut) | 21:9, 16:9, 4:3, 1:1, 3:4, 9:16, adaptive | 🔴 MISSING |
| Multi-block cap | 20s via dual-block | N/A — variable range | ⚠️ Mungkin tidak perlu multi-block concept |

#### DIAGNOSIS:
1. **Max 20s adalah SALAH** — actual max adalah 15s
2. **[10s, 20s] fixed presets adalah SALAH** — duration adalah variable 4–15s
3. "20s" tidak wujud dalam SEEDANCE_2_0 — ini adalah **invented spec**
4. Kerana max sekarang 15s dan variable, multi-block concept untuk SEEDANCE mungkin tidak diperlukan

#### WHAT NEEDS FIX:
```
UPDATE SEEDANCE_2_0 max_duration: 20s → 15s
UPDATE SEEDANCE_2_0 supported_durations: [10s, 20s] → range [4s-15s] variable
REMOVE dual-block chaining concept (kerana max 15s, dalam single generation)
ADD aspect_ratios list
```

---

### ENGINE 5: SORA 2 — ⚠️ KRITIKAL: DEPRECATED!

#### Perbandingan:

| Field | BOSMAX CLAIM | OFFICIAL (ChatGPT) | Verdict |
|---|---|---|---|
| Max duration | **60s** | **20s** per clip | 🔴 SALAH (3× ganda lebih) |
| Block max | 15s | **20s** | 🔴 SALAH |
| Supported durations | [10,15,20,25,30,45,60s] | **"4","8","12","16","20"** | 🔴 SALAH SEPENUHNYA |
| Extension | N/A | **20s each, up to 6× = 120s total** | NEW INFO |
| API status | Active | **⚠️ DEPRECATED — shutdown 2026-09-24** | 🚨 KRITIKAL |

#### DIAGNOSIS:
1. **Semua SORA_2 specs dalam BOSMAX adalah salah** — perlu complete rewrite
2. **DEPRECATION WARNING**: OpenAI akan matikan Sora 2 API pada **24 September 2026** — kurang dari 4 bulan dari sekarang!
3. Durations sebenar: 4, 8, 12, 16, 20 saat (bukan 10,15,20,25,30,45,60)
4. Max per clip = 20s (bukan 60s)
5. Extension boleh reach 120s total (6×20s) — tapi ini extension, bukan single generation

#### WHAT NEEDS FIX:
```
🚨 ADD DEPRECATION WARNING: SORA_2 API shuts down 2026-09-24
UPDATE SORA_2 max_duration: 60s → 20s
UPDATE SORA_2 block_max: 15s → 20s
UPDATE SORA_2 supported_durations: [10,15,20,25,30,45,60s] → [4s,8s,12s,16s,20s]
ADD SORA_2 extension: 20s/block, max 6×, total 120s
DECISION REQUIRED: Adakah kita kekal guna SORA_2 atau remove dari ecosystem?
```

---

## BAHAGIAN 2 — MATRIX KEPUTUSAN LENGKAP

### Apa yang BETUL dalam BOSMAX (tiada perlu repair):
| Item | Status |
|---|---|
| VEO_3_1 block_max = 8s | ✅ BETUL |
| VEO_3_1 referenceImages max = 3 | ✅ BETUL |
| VEO_3_1 Lite = no extension | ✅ BETUL |
| GOOGLE_FLOW sebagai separate ID (UI layer) | ✅ BETUL |
| GATE_095 visual-dialog isolation | ✅ BETUL |
| image_guidance_scale = API-only | ✅ BETUL |
| dna_reinjection_hop concept (via referenceImages) | ✅ BETUL |
| GROK extension exists | ✅ BOSMAX dah betul (multi-block concept) |
| KLING max 5s/10s/15s concept | ✅ Partially betul (cuma 3s missing, 15s API-unverified) |

### Apa yang SALAH (perlu repair):
| Engine | Field | BOSMAX | Betul | Keterukan |
|---|---|---|---|---|
| VEO_3_1 | supported_durations | [8,16,24...56s] | Add "4s","6s"; extension=7s/block | ⚠️ MEDIUM |
| GROK | max_duration | 10s | **15s** | 🔴 HIGH |
| GROK | supported_durations | [6s,10s] | **1-15s range** | 🔴 HIGH |
| GROK | ref images | 3 | **7 (ref-to-video mode)** | 🔴 HIGH |
| KLING_3_0 | supported_durations | [5,10,15s] | Add "3s"; 15s = API-unverified | 🟡 LOW |
| SEEDANCE_2_0 | max_duration | **20s** | **15s** | 🔴 HIGH |
| SEEDANCE_2_0 | supported_durations | [10s,20s] | **4-15s variable** | 🔴 HIGH |
| SORA_2 | max_duration | **60s** | **20s** | 🔴 CRITICAL |
| SORA_2 | supported_durations | [10,15,20,25,30,45,60s] | **[4,8,12,16,20s]** | 🔴 CRITICAL |
| SORA_2 | API status | Active | **⚠️ DEPRECATED 2026-09-24** | 🚨 URGENT |

---

## BAHAGIAN 3 — SENARAI FILES YANG PERLU DIREPAIR

### FILES UTAMA (mengandungi engine specs):

```
1. MASTER_IGNITION_TEMPLATE.md
   → engine_configuration section
   → Affects: VEO_3_1, GROK, KLING_3_0, SEEDANCE_2_0, SORA_2
   → BIGGEST file to fix

2. .claude/CLAUDE.md
   → ENGINE CONSTRAINT TABLE
   → Affects: semua engines

3. SATELLITE_04_MAPPING_MATRIX.md
   → engine_duration_specs
   → Affects: semua engines

4. SATELLITE_05_COACHING_PROTOCOL.md
   → duration query string untuk user
   → Affects: semua engines

5. SOVEREIGN_01_MASTER_SCHEMA.md
   → ABORT logic lines
   → Affects: VEO_3_1, GROK, SEEDANCE_2_0, SORA_2

6. .claude/skills/bosmax-compliance-gate.md
   → engine table + ABORT checks
   → Affects: semua engines

7. .claude/skills/bosmax-script-generator.md
   → Engine sections
   → Affects: GROK, SORA_2

8. .claude/skills/bosmax-mode-c-executor.md
   → Engine caps table
   → Affects: GROK, SEEDANCE_2_0

9. .claude/skills/bosmax-bulk-generator.md
   → Engine table
   → Affects: GROK, SEEDANCE_2_0

10. .claude/skills/bosmax-requirement-analyst.md
    → Engine duration display
    → Affects: semua engines
```

---

## BAHAGIAN 4 — SOALAN KEPUTUSAN UNTUK BOSS

Sebelum Claude keluarkan Codex prompt, boss perlu putuskan:

### ❓ KEPUTUSAN 1: SORA_2 — Kekal atau Remove?
Sora 2 API akan **ditutup pada 24 September 2026** (kurang 4 bulan).
- **Pilihan A:** Kekal dalam ecosystem, tambah deprecation warning, plan migration
- **Pilihan B:** Remove SORA_2 dari BOSMAX engine list sekarang

### ❓ KEPUTUSAN 2: GROK duration — Range atau Presets?
Official GROK = continuous range 1-15s.
- **Pilihan A:** Guna range concept `min:1s, max:15s` (lebih fleksibel)
- **Pilihan B:** Set preset checkpoints e.g. [5s, 10s, 15s] untuk UI simplicity

### ❓ KEPUTUSAN 3: KLING_3_0 15s — Bold atau Conservative?
- **Pilihan A (Conservative):** Set max = 10s (API-verified) dengan note 15s UI-only
- **Pilihan B (Bold):** Kekal 15s, tambah warning [API_UNVERIFIED]

### ❓ KEPUTUSAN 4: SEEDANCE multi-block — Kekal atau Remove?
SEEDANCE max sekarang 15s dalam single generation.
- **Pilihan A:** Remove dual-block chaining (max 15s cukup, tiada perlu multi-block)
- **Pilihan B:** Kekal multi-block logic sebagai safety net

---

## BAHAGIAN 5 — APA YANG BERLAKU SETERUSNYA

```
Boss approve decisions di atas
           ↓
Claude keluarkan CODEX REPAIR PROMPT
(surgical, file-by-file, exact edits)
           ↓
Boss hantar ke Codex
           ↓
Codex repair files
           ↓
Boss forward hasil ke Claude untuk verify
           ↓
Claude approve → Git commit → Push ke GitHub
```

---

*Analisis v1.0 | Claude Orchestrator | 2026-06-01*
*Sumber: ChatGPT Deep Research (official API docs only, verified 2026-06-01)*
