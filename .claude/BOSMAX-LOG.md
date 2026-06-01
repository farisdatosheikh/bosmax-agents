# BOSMAX-LOG.md
## Session Memory & Product Registry
## BOSMAX v11.3 | Schema: GRAND_MASTER_SKELETON

---

## SESSION LOG

### Session 001 — 2026-05-21
**Status:** WORKSPACE SETUP COMPLETE
**Active Mode:** null
**Milestone:** Initial workspace setup verified. All files confirmed present.

| Item | Count | Status |
|------|-------|--------|
| Skill files | 7/7 | ✅ COMPLETE |
| Sovereign/Satellite files | 11/11 | ✅ COMPLETE |
| Image authority files | 9/9 | ✅ COMPLETE |
| Market intelligence files | 12/12 | ✅ COMPLETE |

**Notable events:**
- `Visual_Language_v1_STRICT.md` ditambah ke workspace root (menggantikan versi .yaml yang tidak hadir)
- `BOSMAX-MANIFEST.md` dikemaskini dengan status semua fail
- `.claude/BOSMAX-LOG.md` diinisialisasi

**Routing test result:**
- Request: "BOSMAX, aku nak daftar produk sabun muka untuk TikTok Shop."
- Route identified: ROUTE REG ✅
- Skill invoked: bosmax-product-registration ✅
- CLAUDE.md load: ✅
- Test verdict: **PASS**

---

## PRODUCT REGISTRY

⚠️ **PRODUCT REGISTRY TELAH DIPINDAH KE `products/` FOLDER (v11.2 Fix G)**

Semua product records kini dalam structured YAML files:
- `products/_SCHEMA.yaml` — schema reference
- `products/BOSMAX_SERUM.yaml` — BOSMAX Serum (5ML + 10ML variants)

Rujuk `bosmax-product-intelligence.md` untuk lookup protocol.
**Jangan tambah product records dalam fail ini.**

---

## IMAGE HANDOFF REGISTRY

*[Kosong — belum ada Mode A image dihasilkan]*

---

## PENDING TASKS

*[None]*

---

---

### Session 002 — 2026-05-26
**Status:** SCHEMA UPGRADE — v11.1.1 → v11.2
**Active Mode:** null
**Milestone:** Google Flow + GROK image reference integration (v11.1.1) + v11.2 gap closure.

**Files patched (v11.1.1 — Google Flow + GROK + Nano Banana + Imagen 3):**
- `CLAUDE.md` — Engine registry updated (GOOGLE_FLOW, NANO_BANANA_PRO, IMAGEN_3)
- `bosmax-script-generator.md` — Google Flow 4-mode architecture, GROK image reference syntax
- `bosmax-mode-c-executor.md` — Google Flow F2V/INGREDIENTS/IMAGE sub-modes
- `bosmax-compliance-gate.md` — Google Flow audit checklist (10 items)

**Files patched (v11.2 — gap closure):**
- `bosmax-bulk-generator.md` — VEO_3_1_LITE, GOOGLE_FLOW engine support, multi-block in bulk
- `bosmax-mode-c-executor.md` — Multi-block Mode C protocol, Block 2+ inheritance locks
- `bosmax-compliance-gate.md` — Mode C multi-block explicit inheritance checks
- `README.md` — Version updated to v11.2, bosmax-requirement-analyst.md added to structure
- `BOSMAX-LOG.md` — Schema version updated to v11.2

**Files confirmed already at v11.2 (from GitHub):**
- `CLAUDE.md` — Full PRE-FLIGHT PROTOCOL, ENGINE CONSTRAINT TABLE, MULTI-BLOCK PROTOCOL
- `bosmax-requirement-analyst.md` — NEW skill (v11.2 Fix B) — already present

**Skill file count:** 8/8 ✅ (bosmax-requirement-analyst.md ditambah)

---

---

### Session 003 — 2026-05-28
**Status:** v11.2 CROSS-FILE AUDIT COMPLETE + GROK MATH FIXES
**Active Mode:** null
**Milestone:** Full consistency audit across CLAUDE.md, bosmax-requirement-analyst.md, bosmax-script-generator.md, bosmax-compliance-gate.md. Critical GROK block math errors found and fixed.

**Audit scope (6 checks):**
1. Engine duration consistency — ✅ ALL CONSISTENT (VEO_3_1_LITE, KLING, SEEDANCE, GROK, GOOGLE_FLOW identical across all 4 files)
2. Multi-block trigger consistency — ✅ ALL CONSISTENT (same thresholds across orchestrator, analyst, generator, gate)
3. GROK special-case handling — ⚠️ BUGS FOUND AND FIXED (see below)
4. VEO_3_1_LITE 16s → 2×8s behavior — ✅ ALL CONSISTENT
5. Work Order → Script Generator → Compliance Gate chain — ✅ CHAIN INTACT
6. v11.1 section titles vs v11.2 schema — ⚠️ COSMETIC ONLY (section title headers still say "v11.1" in v11.2 files — intentional, titles unchanged from v11.1)

**GROK math bugs found and fixed:**

| Duration | Old (WRONG) | Fix (CORRECT) |
|----------|-------------|---------------|
| 12s | A) 2×6s B) 10s+6s ← 10+6=16≠12 ❌ | 2×6s only (only valid combo) |
| 18s | A) 3×6s B) 10s+6s+6s ← 10+6+6=22≠18 ❌ | 3×6s only (only valid combo) |
| 20s | A) 2×10s B) 10s+6s+6s ← 22≠20 ❌ | 2×10s only (only valid combo) |
| 30s | A) 3×10s B) 2×10s+10s ← same as A, missing 5×6s ❌ | A) 3×10s B) 5×6s |

**Files patched:**
- `CLAUDE.md` — GROK MULTI-BLOCK TRIGGER MATRIX corrected ✅
- `bosmax-requirement-analyst.md` — GROK contoh kombinasi corrected ✅

**Files confirmed clean (no changes needed):**
- `bosmax-script-generator.md` — v11.2 ✅ (no GROK combo examples, only uses distribution from work order)
- `bosmax-compliance-gate.md` — v11.2 ✅ (engine table correct, no combo examples)

---

### Session 004 — 2026-05-29
**Status:** FULL SYSTEM VERIFICATION — ALL WORKFLOWS CONFIRMED OPERATIONAL
**Active Mode:** null
**Milestone:** End-to-end workflow audit (Route A, B, C, A→C pipeline). All known gaps from briefing doc verified closed.

**Workflow audit results:**

| Workflow | Route | Status | Notes |
|----------|-------|--------|-------|
| Generate prompt gambar | ROUTE A | ✅ READY | subject-dna → scene-engine → gate |
| Generate prompt video dari kosong | ROUTE B | ✅ READY | script-generator → gate, multi-block supported |
| Generate prompt video dari gambar (A→C) | ROUTE A→C | ✅ READY | source_image_handoff locked, Mode C inherit |
| User upload gambar → video | ROUTE C | ✅ READY | Manual handoff intake via mode-c-executor |

**Known gaps from BOSMAX-CLAUDE-CODE-BRIEFING.md — verified status:**
- `bosmax-mode-c-executor.md` multi-block — ✅ CLOSED (Session 002)
- `bosmax-bulk-generator.md` VEO_3_1_LITE engine — ✅ CLOSED (Session 002)
- `bosmax-compliance-gate.md` Mode C multi-block inheritance lock — ✅ CLOSED (Session 002, lines 253–283)
- `README.md` v11.2 update — ✅ CLOSED (Session 002)
- `BOSMAX-LOG.md` schema version — ✅ CLOSED (Session 002)

**All 5 known gaps: CLOSED. Zero open gaps.**

**Files updated this session:**
- `BOSMAX-LOG.md` — Session 004 verification log
- `BOSMAX-CLAUDE-CODE-BRIEFING.md` — Known gaps section updated to reflect all gaps closed

---

### Session 004 (continued) — 2026-05-29
**Status:** Fix E — BULK QUALITY ENFORCEMENT + VARIATION CONDITIONS
**Milestone:** Bulk generator patched for quality consistency across N sets. Three variation conditions formalized.

**Problem addressed:**
AI quality degradation across bulk sets — Set 10 consistently shorter/lower quality than Set 1.
Three user-defined variation conditions needed explicit protocol.

**Root cause analysis:**
- No SET ELEMENT MANIFEST lock — AI could abbreviate without enforcement
- No variation_condition declaration — system didn't know if dialog/avatar should be locked
- No QUALITY GATE checkpoints — no mid-batch verification
- No ATOMIC GENERATION discipline — sets treated as flowing continuation, not standalone units

**Fixes implemented:**

| Fix | File | Change |
|-----|------|--------|
| VARIATION CONDITION PROTOCOL | `bosmax-bulk-generator.md` | 3 conditions declared before Variant Plan |
| SET ELEMENT MANIFEST | `bosmax-bulk-generator.md` | Extract element structure from Set 1, enforce on all sets |
| DIALOG LOCK PROTOCOL | `bosmax-bulk-generator.md` | Condition 1 & 2: S6 copied verbatim from Set 1 |
| AVATAR LOCK PROTOCOL | `bosmax-bulk-generator.md` | Condition 2: S1 biometrics frozen (threshold: 0.0) |
| ATOMIC GENERATION RULE | `bosmax-bulk-generator.md` | Each set standalone, element count ≥ Set 1 mandatory |
| QUALITY GATE (Set 3/6/9) | `bosmax-bulk-generator.md` | Element count check every 3 sets, regenerate if fail |
| BULK QUALITY CONSISTENCY CHECKS | `bosmax-compliance-gate.md` | Element count audit, dialog lock audit, avatar lock audit |
| QUALITY GATE DECLARATIONS check | `bosmax-compliance-gate.md` | Verify quality gate declarations in output |

**Enhancement backlog (noted for future):**
- **Dialogue Script Sheet** — Separate flat document listing full dialogue for all sets as one unit. User can review/edit dialogue in isolation before prompt generation begins. Reduces error, easier for copywriter review.

**Files patched:**
- `bosmax-bulk-generator.md` — VARIATION CONDITION PROTOCOL + new Steps 5-8
- `bosmax-compliance-gate.md` — BULK QUALITY CONSISTENCY CHECKS section

---

### Session 004 (continued) — Fix F: AUTO-HEAL PROTOCOL
**Status:** ABORT redesigned into two-tier system across all skill files
**Milestone:** System no longer abandons work mid-generation for fixable issues.

**Problem:** ABORT for fixable issues (dialog drift, element count, WPS, token leak) = system abandons work and returns incomplete output. User receives error instead of result.

**Architecture change:**
```
BEFORE: All rule violations → ABORT → report to user → stop
AFTER:
  Fixable issues → AUTO-HEAL → fix silently → log → continue → deliver result
  User input missing → HARD BLOCK → ABORT (still correct, cannot proceed)
```

**AUTO-HEAL REGISTRY (fixable without user):**
- Element count drift → expand to manifest
- Dialog drift (Cond 1/2) → copy from Set 1 verbatim
- Avatar drift (Cond 2) → restore Set 1 biometrics
- WPS over limit → trim dialogue
- Raw token leaked → replace with descriptor
- Character name leaked → replace with biometric DNA
- S9 coordinate out of zone → recalculate
- Visual noun in S6 → remove and rephrase
- Section count wrong → rebuild
- Multi-block anchor missing → extract and inject
- Re-introduction phrase in Block 2+ → remove, re-anchor

**HARD BLOCK stays as ABORT:**
- Missing mandatory user input (source_image, product_record, engine, platform, variation_condition)
- Engine/platform declared but invalid (system cannot guess intent)
- Auto-heal attempted and failed

**HEAL REPORT** emitted at end of output — transparent log of all auto-corrections made.

**Files patched:**
- `bosmax-compliance-gate.md` — AUTO-HEAL REGISTRY, two-tier VERDICT PROTOCOL, HARD BLOCK list
- `bosmax-bulk-generator.md` — FAIL-CLOSED RULES split into HARD BLOCK vs AUTO-HEAL
- `bosmax-script-generator.md` — FAIL-CLOSED RULES split into HARD BLOCK vs AUTO-HEAL

---

### Session 005 — 2026-05-29
**Status:** Fix G — PRODUCT INTELLIGENCE LAYER
**Milestone:** Product Librarian skill + structured YAML registry. System no longer asks user to re-explain own products.

**Problem addressed:**
User forced to explain product details on every request. No auto-lookup.
Product scale misrepresentation risk on TikTok (AI engines render wrong size).
Flat markdown product registry in BOSMAX-LOG.md — hard to maintain.

**Architecture added:**
```
PRE-FLIGHT STEP 0 (NEW):
  Request mentions product → bosmax-product-intelligence
  Lookup: TIER 1 (products/*.yaml) → TIER 2 (Fastmoss xlsx) → TIER 3 (Ask user)
  Returns: product_record + scale_anchor_descriptor
  scale_anchor_descriptor injected into ALL content generation skills
```

**scale_anchor_descriptor — why:**
Google Flow + GROK render products at arbitrary scale even with reference images.
TikTok penalises misleading product size in commercial content.
Physical reference keywords anchor AI to correct scale.

| Variant | scale_anchor_descriptor |
|---------|------------------------|
| BOSMAX 5ML | "EXACTLY lip balm size, fit into fingers naturally" |
| BOSMAX 10ML | "EXACTLY chapstick size, fit into fingers naturally" |

**Files created:**
- `bosmax-product-intelligence.md` — Product Librarian skill (Skill #9)
- `products/_SCHEMA.yaml` — Full product YAML schema with all fields
- `products/BOSMAX_SERUM.yaml` — BOSMAX Serum (5ML + 10ML variants)

**Files patched:**
- `CLAUDE.md` — STEP 0 added to PRE-FLIGHT, skill list updated to 9 skills, new fail-closed rules
- `BOSMAX-LOG.md` — Product registry section replaced with pointer to products/ folder

**Product registry count:** 1 product (BOSMAX_SERUM — 2 variants)

---

*BOSMAX v11.2 | Log updated: 2026-05-29*

---

### Session 006 — 2026-05-29
**Status:** AVATAR REGISTRY + WARDROBE RULE ENGINE + SHOT LIBRARY — SEEDED
**Active Mode:** null
**Milestone:** Biometric archetype registry, wardrobe rule engine, and shot library deployed. BOSMAX now supports multi-ethnicity SEA archetype lookup at runtime.

**Components created:**

| Component | Path | Count | Status |
|-----------|------|-------|--------|
| Avatar Schema | `avatars/_SCHEMA.yaml` | 1 | ✅ CREATED |
| Malay Female Archetype | `avatars/MALAY_FEMALE_YOUNG_01.yaml` | 1 | ✅ CREATED |
| Malay Male Archetype | `avatars/MALAY_MALE_YOUNG_01.yaml` | 1 | ✅ CREATED |
| Chinese Female Archetype | `avatars/CHINESE_FEMALE_YOUNG_01.yaml` | 1 | ✅ CREATED |
| Chinese Male Archetype | `avatars/CHINESE_MALE_YOUNG_01.yaml` | 1 | ✅ CREATED |
| Indian Female Archetype | `avatars/INDIAN_FEMALE_YOUNG_01.yaml` | 1 | ✅ CREATED |
| Indian Male Archetype | `avatars/INDIAN_MALE_YOUNG_01.yaml` | 1 | ✅ CREATED |
| Borneo Female Archetype | `avatars/BORNEO_FEMALE_YOUNG_01.yaml` | 1 | ✅ CREATED |
| Borneo Male Archetype | `avatars/BORNEO_MALE_YOUNG_01.yaml` | 1 | ✅ CREATED |
| Indonesia Female Archetype | `avatars/INDONESIA_FEMALE_YOUNG_01.yaml` | 1 | ✅ CREATED |
| Indonesia Male Archetype | `avatars/INDONESIA_MALE_YOUNG_01.yaml` | 1 | ✅ CREATED |
| Bangladesh Female Archetype | `avatars/BANGLADESH_FEMALE_YOUNG_01.yaml` | 1 | ✅ CREATED |
| Bangladesh Male Archetype | `avatars/BANGLADESH_MALE_YOUNG_01.yaml` | 1 | ✅ CREATED |
| Wardrobe Rule Engine | `wardrobes/WARDROBE_RULES.yaml` | ~104 rules | ✅ CREATED |
| Shot Library | `shots/SHOT_LIBRARY.yaml` | 13 shot codes | ✅ CREATED |

**Avatar archetypes seeded:** 12 (6 ethnicities × 2 genders)
**Wardrobe rules count:** ~104 (12 archetypes × 8+ occasions each)
**Shot codes count:** 13 (ECU, CU, MCU, MS, MLS, WS, OTS, POV, TOP_DOWN, MACRO, DUTCH, LOW_ANGLE, HIGH_ANGLE)

**Skill files patched:**
- `bosmax-subject-dna.md` — ETHNICITY ARCHETYPE REGISTRY LOOKUP section added (v11.2)
- `bosmax-scene-engine.md` — SHOT LIBRARY LOOKUP section added (v11.2)

**Architecture note:**
Ethnicity archetypes (MALAY_FEMALE_YOUNG_01, etc.) are SEPARATE from named campaign
avatars (NORA, SARA, RIZAL, etc.). Named avatars continue to work as before.
Archetypes are runtime-loaded from `avatars/[ID].yaml` with wardrobe resolved
from `wardrobes/WARDROBE_RULES.yaml` via (avatar_id, occasion, scene_context) key.

**Occasions covered in wardrobe rules:**
hari_raya_aidilfitri, hari_raya_aidiladha, chinese_new_year, deepavali,
gawai_kaamatan, hari_merdeka, malaysia_day, majlis_kahwin_guest, casual_everyday,
workplace_office, workplace_retail, outdoor_street, home_indoor, gym_active,
tiktok_trendy, shopee_lazada_clean

**Hijab policy enforced:**
- Malay Female: true (hijab default for commercial)
- Chinese Female: false
- Indian Female: false
- Borneo Female: false
- Indonesia Female: true
- Bangladesh Female: true

---

### Session 007 — 2026-05-29
**Status:** PRODUCT REGISTRATION — CAP_BURUNG_MINYAK
**Active Mode:** REG
**Milestone:** Minyak Cap Burung didaftarkan dalam product registry dengan 20 copywriting angles.

**Product registered:**

| Field | Value |
|-------|-------|
| Product ID | CAP_BURUNG_MINYAK |
| Product Name | Minyak Cap Burung |
| Brand | Cap Burung |
| Heritage | Sejak 1958 |
| Category | Health & Wellness — Traditional Remedy |
| Variant | 30ML Square Glass Roll-On |
| Scale Anchor | "EXACTLY standard roll-on deodorant size, fit snugly in closed palm" |
| Benefits count | 14 (dari label produk) |
| Copywriting angles | 20 sets (A01–A20) |

**Copywriting angles breakdown:**

| Range | Coverage |
|-------|----------|
| A01–A14 | 14 angles terus dari 14 manfaat label produk |
| A15 | Travel Essential (multi-benefit convenience angle) |
| A16 | Warisan 1958 / Heritage Trust |
| A17 | Satu Botol Banyak Kegunaan (value proposition) |
| A18 | Postnatal Recovery Comprehensive |
| A19 | Baby & Kids Care |
| A20 | Wanita Aktif / Busy Mom |

**Avatar recommendations disertakan dalam YAML:**
- Primary archetypes: MALAY_FEMALE_YOUNG_01, MALAY_MALE_YOUNG_01
- Named avatars: SARA (informational), JULIA (postnatal), BELLA (lifestyle), MAK_TOK (heritage), AZMAN (active male)

**Files created:**
- `products/CAP_BURUNG_MINYAK.yaml` — full product registry + 20 copywriting sets

**Pending (kemaskini bila sedia):**
- TikTok Shop product_id dan shop_name
- Fastmoss data (avg_price, orders, revenue)
- subject_dna dan source_image_handoff (selepas Mode A)

---

*BOSMAX v11.2 | Log updated: 2026-05-29*

---

### Session 008 — 2026-05-31
**Status:** v11.3 PATCH — 3 CRITICAL FIXES
**Active Mode:** null
**Milestone:** Video script quality fixes based on real output analysis.

**Root cause per issue:**

| Issue | Root Cause | Fix |
|-------|-----------|-----|
| Text overlay muncul dalam video | Section 9 active — AI generate overlay yang video engine burn-in terus | S9 DEACTIVATED — output NO_OVERLAY sahaja |
| Dialog tak habis dalam video | Tiada dialog pre-budget dikira sebelum tulis S6 — AI masuk Hook+3USP+CTA tanpa check WPS ceiling | DIALOG PRE-BUDGET block wajib: FLOOR(duration × 1.6) words max, priority Hook > CTA > USP |
| GROK render botol terlalu besar | image_strength 0.80 tidak cukup kuat — GROK reinterpret scale secara agresif | SCALE_AUTHORITY_OVERRIDE block + image_strength 0.90 + explicit negative scale prompts |

**Diagnosis contoh (8s video @ 1.6 WPS):**
- Word budget: FLOOR(8 × 1.6) = 12 words maximum
- ChatGPT output dialog sebelum fix: 43 words = 5.4 WPS (jauh exceed kill-switch 3.0)
- Selepas fix: Hook (8w) + CTA (2w) = 10 words ✅

**Files patched:**
- `bosmax-script-generator.md` — v11.2 → v11.3 (S9 deactivated, Dialog Pre-Budget, GROK Scale Override)
- `bosmax-mode-c-executor.md` — S9 deactivated (consistency patch)

---

*BOSMAX v11.3 | Log updated: 2026-05-31*

### Session 009 — 2026-05-31
**Status:** WPS GOVERNANCE OVERHAUL — LANGUAGE-SPECIFIC TABLES
**Active Mode:** null
**Milestone:** Old WPS values (1.6/2.0/3.0) deprecated. Replaced with verified language-specific tables.

**Root cause:**
Old values tidak mengambil kira kepadatan suku kata BM (3–4 suku kata/perkataan).
1.6 WPS terlalu konservatif, 3.0 WPS kill-switch terlalu tinggi untuk BM.

**New WPS values (VERIFIED):**

| Language | Optimum | Safe Max | Hard Ceiling |
|----------|---------|----------|--------------|
| BM | 2.2 WPS | 2.5 WPS | 2.8 WPS |
| EN | 2.6 WPS | 3.0 WPS | ~3.3 WPS |
| ID | 2.2 WPS | 2.6 WPS | ~2.9 WPS |
| ZH | 2.2 CPS | 2.6 CPS | ~2.9 CPS |
| HI | 2.0 WPS | 2.4 WPS | ~2.7 WPS |
| BN | 2.0 WPS | 2.4 WPS | ~2.7 WPS |
| AR | 1.8 WPS | 2.2 WPS | ~2.5 WPS |

**Key impact — BM 8s dialog budget:**
- SEBELUM: FLOOR(8 × 1.6) = 12 words (too tight)
- SELEPAS: FLOOR(8 × 2.5) = 20 words (correct — matches table)

**Files patched:**
- bosmax-script-generator.md — WPS Governance full replacement, BLOCK MATH, DIALOG PRE-BUDGET, S6 instructions, OUTPUT CONTRACT S8, AUTO-HEAL rules

*BOSMAX v11.3 | Log updated: 2026-05-31*

---

### Session 010 — 2026-05-31
**Status:** CAP BURUNG — PACKAGING + LABEL DNA FIX
**Active Mode:** null
**Milestone:** Correct packaging and label visual identity captured from actual product photo.

**Root cause:**
Prompt template kata "stainless steel roller ball on top" — AI tunjuk roller ball exposed.
Tiada label DNA dalam prompt — AI reka label hijau botanical sendiri.
Produk sebenar (rujuk TikTok photo): sepia/kraft vintage label, burung terbang, black dome cap tertutup.

**Corrections:**

| Field | SALAH (sebelum) | BETUL (selepas) |
|-------|----------------|----------------|
| Cap | "stainless steel roller ball on top" | "black rounded dome cap — TERTUTUP, roller ball hidden" |
| Label color | (tiada spec → AI generate hijau) | Warm sepia/tan/kraft paper tone — FORBIDDEN: green, white, botanical green |
| Bird design | (AI generate hinggap atas dahan) | Soaring bird IN FLIGHT, wings spread, inside circular medallion |
| Label text | (AI generate "MINYAK CAP BURUNG" sahaja) | "CAP BURUNG (BIRD BRAND)" + "MINYAK CAP HERBAL OIL" + "30ML" + "ESTD 2023" |
| Oil color | "clear amber-tinted" (vague) | Warm amber/golden-brown visible through clear glass |

**Files patched:**
- products/CAP_BURUNG_MINYAK.yaml — packaging_type, packaging_color, scale_anchor_descriptor, label_dna field baru
- Notion: CAP BURUNG MINYAK Plug & Play Templates — all Poster A1-A5 updated + all scale anchor references

*BOSMAX v11.3 | Log updated: 2026-05-31*

---

### Session 011 — 2026-06-01
**Status:** CAP BURUNG — LATEST BOTTLE TRUTH SYNC
**Active Mode:** null
**Milestone:** Product registry diselaraskan dengan latest approved Minyak Cap Burung bottle render.

**Authority source:**
- Latest approved product image: smooth plain black cap, closed bottle
- Oil color: translucent emerald herbal green
- Label/sticker: current dark green + cream + gold layout remains locked

**Supersession note:**
Session 010 mencerminkan truth lama yang digunakan semasa pembaikan sebelumnya.
Authority semasa untuk generation image/video kini digantikan dengan bottle state berikut:

| Field | Authority semasa |
|-------|------------------|
| Cap | Plain smooth black cap — TERTUTUP, no ribbing, no grooves, roller ball hidden |
| Oil color | Translucent emerald herbal green — distinct from darker sticker green |
| Scale read | Compact mini perfume-bottle size — natural one-hand read, NOT deodorant-sized |
| Label | Dark forest green outer panel + cream center + gold border |
| Bird | Perched on leafy branch — NOT flying |

**Files patched:**
- `products/CAP_BURUNG_MINYAK.yaml` — packaging descriptor, prompt keywords, image prompt locks, negative locks

*BOSMAX v11.3 | Log updated: 2026-06-01*

---

### Session 013 — 2026-06-01
**Status:** CAP BURUNG — WG40 BOTTLE GEOMETRY AUTHORITY RESET
**Active Mode:** null
**Milestone:** Product truth diselaraskan semula kepada botol sebenar WG40 30ml clear glass bottle dengan red cap dan stopper.

**Authority source:**
- Product description supplied by operator for real packaging geometry
- Bottle type: WG40 30ml Glass Bottle Clear with Red Cap & Stopper
- Technical dimensions: 9.4cm full height, 6cm height to neck, 3.7cm length, 2.1cm width, 18mm cap

**Supersession note:**
Session 011 memegang truth peralihan yang masih salah pada closure logic dan bottle silhouette.
Authority semasa untuk generation poster, avatar+product, dan video kini digantikan dengan state berikut:

| Field | Authority semasa |
|-------|------------------|
| Bottle geometry | WG40 30ml oblong / rectangular clear flint glass bottle |
| Cap | Red ribbed screw cap |
| Closure logic | Internal stopper / plug hidden under cap — NOT roller ball, NOT roll-on |
| Scale read | EXACTLY classic 30ml minyak angin bottle size — 9.4cm tall, fits naturally in one hand or small bag |
| Label | Dark forest green outer panel + cream center + gold border |
| Bird | Perched on leafy branch — NOT flying |
| Oil color | Translucent emerald herbal green |

**Files patched:**
- `products/CAP_BURUNG_MINYAK.yaml` — product_type, packaging descriptor, application method, variant identity, scale anchor, prompt keywords, image prompt locks, negative locks, summary copy

*BOSMAX v11.3 | Log updated: 2026-06-01*

---

### Session 012 — 2026-06-01
**Status:** UNIVERSAL COMMERCIAL DESIGN SKILL INSTALLED
**Active Mode:** null
**Milestone:** BOSMAX ecosystem kini ada skill universal untuk elevate brief lemah menjadi poster prompt bertaraf senior commercial designer + copywriter.

**What was added:**
- Installed repo skill: `bosmax-commercial-poster-director.md`
- Portable export file: `BOSMAX_UNIVERSAL_COMMERCIAL_DESIGN_SKILL.md`

**Purpose:**
- User boleh tulis prompt malas, ringkas, atau tak berstruktur
- Skill akan normalize platform, selling angle, visual hierarchy, product truth, and negative locks
- Output akhir mesti terasa seperti kerja senior designer dan product copywriter, bukan generic prompt writer

**Coverage:**
- Universal across products, categories, and platforms
- Sesuai untuk Codex, Claude, Manus, Gemini, dan mana-mana AI yang menerima fail instruction

*BOSMAX v11.3 | Log updated: 2026-06-01*
