# BOSMAX ECOSYSTEM — TASK BRIEFING
## Task: Avatar Registry + Wardrobe Rule Engine
## Authority: SUPREME_SYSTEMS_ARCHITECT (pldsb.faris@gmail.com)
## Date: 2026-05-29 | Schema: GRAND_MASTER_SKELETON v11.2

---

## BACA INI DULU SEBELUM BUAT APA-APA

Baca fail-fail ini secara berurutan sebelum mula:
1. `.claude/CLAUDE.md` — BOSMAX orchestrator brain (authority utama)
2. `.claude/BOSMAX-LOG.md` — session memory
3. `products/_SCHEMA.yaml` — contoh pattern YAML yang digunakan dalam projek ni
4. `products/BOSMAX_SERUM.yaml` — contoh product YAML yang dah siap

Pastikan kamu faham pattern dan naming convention yang dah wujud sebelum create fail baru.

---

## GITHUB REPO

```
Repo:   farisdatosheikh/bosmax-agents (PRIVATE)
Branch: master
```

Setiap kali siap buat perubahan, WAJIB commit dengan message yang jelas dan push ke GitHub.

---

## BUSINESS PROBLEM

BOSMAX system sekarang boleh generate content (image + video prompts) untuk TikTok Shop MY.
Tapi apabila user request untuk generate content, sistem terpaksa describe avatar dari scratch
setiap kali — tiada registry untuk lock biometric DNA avatar.

Tanpa avatar registry:
- Condition 2 bulk generation (avatar locked) tidak boleh enforce properly
- Character consistency merentas video sets tidak terjamin
- Wardrobe tidak ada anchor kepada budaya/occasion — AI interpret sendiri, hasilnya inconsistent

---

## TASK — APA YANG PERLU DIBINA

### BAHAGIAN 1 — Avatar Biometric Registry

Bina fail YAML untuk **12 avatar archetypes** berikut dalam folder `avatars/`:

```
avatars/
  _SCHEMA.yaml                    ← template schema (buat dulu)
  MALAY_FEMALE_YOUNG_01.yaml
  MALAY_MALE_YOUNG_01.yaml
  CHINESE_FEMALE_YOUNG_01.yaml
  CHINESE_MALE_YOUNG_01.yaml
  INDIAN_FEMALE_YOUNG_01.yaml
  INDIAN_MALE_YOUNG_01.yaml
  BORNEO_FEMALE_YOUNG_01.yaml
  BORNEO_MALE_YOUNG_01.yaml
  INDONESIA_FEMALE_YOUNG_01.yaml
  INDONESIA_MALE_YOUNG_01.yaml
  BANGLADESH_FEMALE_YOUNG_01.yaml
  BANGLADESH_MALE_YOUNG_01.yaml
```

**Setiap avatar YAML mesti ada fields ini:**

```yaml
avatar_id: ""             # e.g. MALAY_FEMALE_YOUNG_01
ethnicity: ""             # Malay / Chinese / Indian / Borneo / Indonesian / Bangladeshi
gender: ""                # Female / Male
age_range: ""             # e.g. "20-28"
persona_name: ""          # Nama persona (bukan nama sebenar) — e.g. "Aina"

# BIOMETRIC DNA — untuk AI image/video engine
skin_tone: ""             # e.g. "warm medium brown, NC35 equivalent"
face_shape: ""            # e.g. "oval with soft jawline"
eye_shape: ""             # e.g. "almond-shaped, dark brown iris"
nose: ""                  # e.g. "soft button nose, medium bridge"
lips: ""                  # e.g. "naturally full, medium pigmentation"
hair_texture: ""          # e.g. "straight, fine, black"
hair_length: ""           # e.g. "shoulder-length"
hair_style_default: ""    # e.g. "loose straight, centre parted"
build: ""                 # e.g. "slim, 160cm, proportionate"
distinguishing_features: []  # e.g. ["small beauty mark below right eye"]

# PERSONA TRAITS — untuk copywriting tone match
personality_keywords: []  # e.g. ["friendly", "relatable", "aspirational"]
speaks_language: []       # e.g. ["BM", "English"]
content_style: ""         # e.g. "everyday lifestyle, beauty routine, product demo"

# WARDROBE BASE (default — overridden by WARDROBE_RULES.yaml per occasion)
default_wardrobe: ""      # e.g. "casual everyday — baju t-shirt, jeans, minimal accessories"
hijab_wearing: null       # true / false / null (not applicable)

# METADATA
created_date: ""
last_updated: ""
notes: ""
```

**Panduan biometric untuk setiap ethnicity** (guna ini sebagai reference baseline):

```
MALAY (Female/Male):
  skin_tone: warm medium brown (NC30-NC40 range)
  facial features: soft rounded features, almond eyes, medium nose bridge
  hair: straight to wavy, dark black/dark brown
  Female: tudung/hijab common (hijab_wearing: true untuk default)
  Male: short-cropped hair common

CHINESE (Female/Male):
  skin_tone: light to medium, cool-neutral undertone (NC15-NC25)
  facial features: oval face, single/double eyelid (specify), delicate features
  hair: straight fine black hair (Female: various lengths; Male: short neat)

INDIAN (Female/Male):
  skin_tone: warm medium to deep (NC40-NC50, warm undertone)
  facial features: defined brow arch, large expressive eyes, fuller lips
  hair: thick black hair, wavy to straight
  Female: bindi optional (default: no bindi for commercial content)

BORNEO (Female/Male):
  skin_tone: warm medium brown, slight golden undertone
  facial features: broad forehead, round face, wider nose bridge, bright eyes
  hair: thick straight black hair
  note: Dayak/Kadazan/Iban features — distinct from Peninsular Malay

INDONESIAN (Female/Male):
  skin_tone: warm medium, NC30-NC35 Javanese baseline
  facial features: soft oval face, gentle features, similar to Malay with subtle distinctions
  hair: straight fine black
  Female: hijab common (hijab_wearing: true)

BANGLADESHI (Female/Male):
  skin_tone: warm medium to deep brown (NC35-NC45)
  facial features: defined features, prominent eyes, structured jawline
  hair: thick wavy-straight black
  Female: hijab common OR long flowing black hair (hijab_wearing: variable)
```

---

### BAHAGIAN 2 — Wardrobe Rule Engine

Bina fail: `wardrobes/WARDROBE_RULES.yaml`

Ini adalah lookup table: `ethnicity + gender + occasion + scene_context → outfit_descriptor`

**Occasions yang mesti di-cover:**

```yaml
occasions:
  # PERAYAAN
  - hari_raya_aidilfitri
  - hari_raya_aidiladha
  - chinese_new_year
  - deepavali
  - gawai_kaamatan          # Borneo specific
  - hari_merdeka            # Aug 31
  - malaysia_day            # Sep 16
  - hari_guru
  - majlis_kahwin_guest     # Wedding guest
  - majlis_kahwin_bride_groom  # Main wedding pair (jarang tapi perlu)

  # HARIAN
  - casual_everyday
  - workplace_office
  - workplace_retail        # Kedai, counter sales
  - outdoor_street
  - home_indoor
  - gym_active

  # PLATFORM CONTEXT
  - tiktok_trendy           # Gen Z vibes, more expressive
  - shopee_lazada_clean     # Clean, trustworthy, product-focus
```

**Format setiap wardrobe rule:**

```yaml
- ethnicity: Malay
  gender: Female
  occasion: hari_raya_aidilfitri
  scene_context: home_indoor
  outfit_descriptor: >
    Baju kurung moden in soft pastel (mint green / blush pink / lilac),
    matching tudung bawal neatly pinned, subtle gold accessories,
    light festive makeup, clean pressed fabric
  colour_palette: ["soft pastel", "mint green", "blush pink", "lilac", "gold accent"]
  avoid: ["denim", "t-shirt", "athleisure", "heavy dark colours"]
  notes: "Raya home scene — warm, family-friendly, approachable"
```

**Minimum rules yang perlu ada:**
- Semua 12 ethnicity/gender combinations
- Minimum 8 occasions setiap combination
- Total minimum: ~96 rules (boleh lebih)

---

### BAHAGIAN 3 — Shot Library

Bina fail: `shots/SHOT_LIBRARY.yaml`

Ini adalah standardized camera shot codes yang digunakan dalam S2 (camera direction) script generator.

**Minimum shots yang perlu ada:**

```yaml
shots:
  - code: ECU
    name: Extreme Close-Up
    descriptor: "Face fills entire frame, eyes and nose only visible, intimate and intense"
    best_for: ["emotion reveal", "product texture detail", "eye contact hook"]

  - code: CU
    name: Close-Up
    descriptor: "Full face frame, chin to forehead, expressions clearly readable"
    best_for: ["testimonial", "product application on face", "reaction shot"]

  - code: MCU
    name: Medium Close-Up
    descriptor: "Head to mid-chest, standard talking head, approachable and direct"
    best_for: ["product demo", "speaking to camera", "hook delivery"]

  - code: MS
    name: Medium Shot
    descriptor: "Waist up, full arm movement visible, body language readable"
    best_for: ["product unboxing", "demonstrating use", "lifestyle context"]

  - code: MLS
    name: Medium Long Shot
    descriptor: "Knees up, full outfit visible, walking or movement possible"
    best_for: ["fashion/wardrobe reveal", "entering scene", "full body product hold"]

  - code: WS
    name: Wide Shot
    descriptor: "Full body in environment, setting clearly established"
    best_for: ["scene establishing", "outdoor product use", "lifestyle setting"]

  - code: OTS
    name: Over-The-Shoulder
    descriptor: "Camera behind and over one shoulder, subject faces product or mirror"
    best_for: ["mirror scenes", "product comparison", "applying to skin"]

  - code: POV
    name: Point of View
    descriptor: "Camera as the viewer's eyes, direct first-person perspective"
    best_for: ["unboxing", "product pickup from surface", "immersive demo"]

  - code: TOP_DOWN
    name: Top-Down / Flat Lay
    descriptor: "Camera directly above subject or product on flat surface"
    best_for: ["product arrangement", "ingredient flat lay", "texture shot"]

  - code: MACRO
    name: Macro / Detail Shot
    descriptor: "Extreme detail on product texture, skin surface, or material quality"
    best_for: ["product quality proof", "ingredient close-up", "before/after skin"]
```

---

### BAHAGIAN 4 — Update BOSMAX Ecosystem

Selepas semua files di-create, update fail-fail berikut:

**A. `.claude/skills/bosmax-subject-dna.md`**
- Tambah section: "AVATAR REGISTRY LOOKUP"
- Bila avatar_id disebut → load dari `avatars/[ID].yaml` instead of asking user
- Wardrobe → load dari `wardrobes/WARDROBE_RULES.yaml` based on (avatar_id, occasion, scene_context)

**B. `.claude/skills/bosmax-scene-engine.md`**
- Tambah section: "SHOT LIBRARY LOOKUP"
- Bila camera direction diperlukan → reference `shots/SHOT_LIBRARY.yaml` codes
- S2 in script should use shot codes (e.g., "MCU → CU as product revealed")

**C. `.claude/BOSMAX-LOG.md`**
- Tambah Session 006 log entry
- Record: avatar registry seeded (12 archetypes), wardrobe rules (N rules), shot library (N shots)

**D. `BOSMAX-CLAUDE-CODE-BRIEFING.md`**
- Update FILE STRUCTURE section — tambah `avatars/`, `wardrobes/`, `shots/` folders

---

## SCOPE & CONSTRAINTS

**IN SCOPE:**
- 12 avatar YAML files (one per archetype, `_01` suffix — room for future `_02`, `_03`)
- `avatars/_SCHEMA.yaml` — template
- `wardrobes/WARDROBE_RULES.yaml` — minimum 96 rules
- `shots/SHOT_LIBRARY.yaml` — minimum 10 shot codes
- Updates ke 4 ecosystem files listed above
- Commit dan push ke GitHub

**OUT OF SCOPE (jangan buat sekarang):**
- `bosmax-data-librarian` agent — tidak diperlukan lagi sekarang
- Avatar portrait images — bukan text file, luar scope
- More than 1 avatar per archetype (`_02`, `_03`) — seed dulu dengan `_01`
- Wardrobe rules untuk non-Malaysian cultures — focus MY + ID + BD market

**QUALITY STANDARD:**
- Biometric descriptors mesti specific dan actionable untuk AI image/video engine
- Jangan tulis vague descriptors seperti "average build" atau "normal features"
- Setiap descriptor mesti boleh di-inject terus ke dalam S1 (character description) tanpa edit
- Wardrobe rules mesti culturally accurate — verify mengikut pengetahuan budaya SEA

---

## PROOF REQUIRED

Sebelum declare selesai:

1. `ls avatars/` → tunjuk 13 files (12 avatars + 1 schema)
2. `ls wardrobes/` → tunjuk WARDROBE_RULES.yaml
3. `ls shots/` → tunjuk SHOT_LIBRARY.yaml
4. Count wardrobe rules → confirm ≥ 96 entries
5. Count shot codes → confirm ≥ 10 entries
6. `git log --oneline -3` → confirm commit SHA dan push
7. `git diff origin/master HEAD` → empty (fully in sync)

---

## COMMIT FORMAT

```
Avatar+Wardrobe Registry: Seed 12 avatar archetypes + wardrobe rules + shot library

- NEW: avatars/_SCHEMA.yaml
- NEW: avatars/[12 files] — biometric DNA per ethnicity/gender
- NEW: wardrobes/WARDROBE_RULES.yaml — [N] rules (ethnicity × occasion × context)
- NEW: shots/SHOT_LIBRARY.yaml — [N] standardized camera shot codes
- PATCH: bosmax-subject-dna.md — avatar registry lookup
- PATCH: bosmax-scene-engine.md — shot library lookup
- PATCH: BOSMAX-LOG.md — Session 006 log
- PATCH: BOSMAX-CLAUDE-CODE-BRIEFING.md — file structure update
```

---

## GIT PUSH INSTRUCTION — PENTING

**JANGAN guna `git add` dari bash sandbox** — ada bug dengan index.lock yang menyebabkan
bad commit. Guna Windows PowerShell MCP untuk semua git operations:

```powershell
# Cara betul:
Set-Location "C:\Users\USER\Desktop\Claude Cowork Bosmax Agents"
git add avatars/ wardrobes/ shots/ .claude/ BOSMAX-CLAUDE-CODE-BRIEFING.md
git commit -m "[message]"
git push origin master
```

Kalau ada lock error:
```powershell
Get-ChildItem ".git" -Filter "*.lock" -Recurse | Remove-Item -Force
# Kemudian retry commit/push
```

---

*Briefing ditulis: 2026-05-29 | Task: Avatar + Wardrobe Registry Build*
*GitHub: farisdatosheikh/bosmax-agents | Branch: master | Schema: v11.2*
