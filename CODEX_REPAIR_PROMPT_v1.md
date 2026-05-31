# BOSMAX ENGINE SPECS — CODEX REPAIR PROMPT v1.0
**Authority:** Claude Orchestrator
**Tarikh:** 2026-06-01
**Verified by:** Boss (first-hand check 2:59 AM 1/6/2026) + ChatGPT Deep Research (official API docs)

---

## ARAHAN KEPADA CODEX

Anda dikehendaki melakukan surgical in-place edits pada fail-fail BOSMAX ecosystem.
**Jangan rewrite fail.** Buat perubahan tepat seperti yang dinyatakan sahaja.
**Jangan ubah mana-mana bahagian lain** selain daripada yang disenaraikan.
Selepas selesai setiap fail, commit dengan message yang dinyatakan.

---

## RINGKASAN PERUBAHAN

| Engine | Perubahan |
|---|---|
| **SORA_2** | REMOVE sepenuhnya dari semua files |
| **KLING_3_0** | Tambah "3s"; buang label [BOSMAX_HEURISTIC] → ganti [OFFICIAL_VERIFIED_2026-06-01] |
| **SEEDANCE_2_0** | max 20s→15s; durations [10s,20s]→[5s,10s,15s]; buang dual-block concept; update label |
| **GROK** | Buang label [EXTERNAL_ENGINE_ADDED] → ganti [OFFICIAL_VERIFIED_2026-06-01] |
| **VEO_3_1** | Tambah "4s" dan "6s" ke supported_durations |

---

## FILE 1: `MASTER_IGNITION_TEMPLATE.md`

### REPAIR 1A — Remove SORA_2 dari engine_id list

**FIND:**
```
  - **SORA_2** (array):
    - Item 1:
      `10s`
    - Item 2:
      `15s`
    - Item 3:
      `20s`
    - Item 4:
      `25s`
    - Item 5:
      `30s`
    - Item 6:
      `45s`
    - Item 7:
      `60s`
```
**REPLACE WITH:** _(delete entire block)_

---

### REPAIR 1B — Remove SORA_2 dari engine_configuration

**FIND:**
```
  - **SORA_2** (object):
    - **visual_en** (string): `Sora 2 with Spatiotemporal Physics Simulation.`
    - **max_duration** (string): `60s`
    - **block_max** (string): `15s`
    - **chaining** (string): `UI_DRAFT_STITCHING_SEQUENCE`
    - **context_management** (string): `MULTI_BLOCK_STITCHING_FOR_GT_BLOCK_MAX`
    - **i2v_support** (boolean): `true`
    - **identity_lock** (string): `WORLD_CONSISTENCY`
    - **cfg_range** (string): `4.0-6.0`
    - **special_case** (string): `60s = MULTI_BLOCK_STITCHED_OUTPUT`
    - **dna_reinjection_interval_time** (string): `15s`
    - **supported_durations** (array):
```json
[
  "10s",
  "15s",
  "20s",
  "25s",
  "30s",
  "45s",
  "60s"
]
```
```
**REPLACE WITH:** _(delete entire block)_

---

### REPAIR 1C — Update KLING_3_0 supported_durations + label

**FIND:**
```
    - **label** (string): `[BOSMAX_HEURISTIC]`
    - **note** (string): `HARD_LOCK_15S_TO_PREVENT_BIOMETRIC_DRIFT`
    - **supported_durations** (array):
```json
[
  "5s",
  "10s",
  "15s"
]
```
```
**REPLACE WITH:**
```
    - **label** (string): `[OFFICIAL_VERIFIED_2026-06-01]`
    - **note** (string): `HARD_LOCK_15S_TO_PREVENT_BIOMETRIC_DRIFT`
    - **supported_durations** (array):
```json
[
  "3s",
  "5s",
  "10s",
  "15s"
]
```
```

---

### REPAIR 1D — Update SEEDANCE_2_0 specs

**FIND:**
```
  - **SEEDANCE_2_0** (object):
    - **visual_en** (string): `Seedance 2.0 with 2K Texture & Multi-shot Consistency.`
    - **max_duration** (string): `20s`
    - **block_max** (string): `10s`
    - **chaining** (string): `EXTEND_FRAME_REFERENCE`
    - **context_management** (string): `DUAL_BLOCK_CHAINING_IF_GT_10S`
    - **i2v_support** (boolean): `true`
    - **identity_lock** (string): `WORLD_ID`
    - **cfg_range** (string): `4.0-6.5`
    - **dna_reinjection_interval_time** (string): `5s`
    - **label** (string): `[EXTERNAL_ENGINE_ADDED]`
    - **supported_durations** (array):
```json
[
  "10s",
  "20s"
]
```
```
**REPLACE WITH:**
```
  - **SEEDANCE_2_0** (object):
    - **visual_en** (string): `Seedance 2.0 with 2K Texture & Multi-shot Consistency.`
    - **max_duration** (string): `15s`
    - **block_max** (string): `15s`
    - **chaining** (string): `SINGLE_BLOCK_EXECUTION`
    - **context_management** (string): `SINGLE_BLOCK_EXECUTION`
    - **i2v_support** (boolean): `true`
    - **identity_lock** (string): `WORLD_ID`
    - **cfg_range** (string): `4.0-6.5`
    - **dna_reinjection_interval_time** (string): `5s`
    - **label** (string): `[OFFICIAL_VERIFIED_2026-06-01]`
    - **supported_durations** (array):
```json
[
  "5s",
  "10s",
  "15s"
]
```
```

---

### REPAIR 1E — Update GROK label

**FIND:**
```
    - **label** (string): `[EXTERNAL_ENGINE_ADDED]`
    - **supported_durations** (array):
```json
[
  "6s",
  "10s"
]
```

    - **restriction** (string): `FORBID_NANO_BANANA`
```
**REPLACE WITH:**
```
    - **label** (string): `[OFFICIAL_VERIFIED_2026-06-01]`
    - **supported_durations** (array):
```json
[
  "6s",
  "10s"
]
```

    - **restriction** (string): `FORBID_NANO_BANANA`
```

---

### REPAIR 1F — Update VEO_3_1 supported_durations

**FIND:**
```
    - **supported_durations** (array):
```json
[
  "8s",
  "16s",
  "24s",
  "32s",
  "40s",
  "48s",
  "56s"
]
```

  - **SORA_2** (object):
```
**REPLACE WITH:**
```
    - **supported_durations** (array):
```json
[
  "4s",
  "6s",
  "8s",
  "16s",
  "24s",
  "32s",
  "40s",
  "48s",
  "56s"
]
```

  - **SORA_2** (object):
```
*(Note: SORA_2 object akan sudah dibuang dalam REPAIR 1B — pastikan backtick closing betul selepas VEO_3_1 block)*

---

### REPAIR 1G — Update duration_target KLING_3_0

**FIND:**
```
  - **KLING_3_0** (array):
    - Item 1:
      `5s`
    - Item 2:
      `10s`
    - Item 3:
      `15s`
```
**REPLACE WITH:**
```
  - **KLING_3_0** (array):
    - Item 1:
      `3s`
    - Item 2:
      `5s`
    - Item 3:
      `10s`
    - Item 4:
      `15s`
```

---

### REPAIR 1H — Update duration_target SEEDANCE_2_0

**FIND:**
```
  - **SEEDANCE_2_0** (array):
    - Item 1:
      `10s`
    - Item 2:
      `20s`
```
**REPLACE WITH:**
```
  - **SEEDANCE_2_0** (array):
    - Item 1:
      `5s`
    - Item 2:
      `10s`
    - Item 3:
      `15s`
```

---

### REPAIR 1I — Update duration_target VEO_3_1

**FIND:**
```
  - **VEO_3_1** (array):
    - Item 1:
      `8s`
    - Item 2:
      `16s`
    - Item 3:
      `24s`
    - Item 4:
      `32s`
    - Item 5:
      `40s`
    - Item 6:
      `48s`
    - Item 7:
      `56s`
```
**REPLACE WITH:**
```
  - **VEO_3_1** (array):
    - Item 1:
      `4s`
    - Item 2:
      `6s`
    - Item 3:
      `8s`
    - Item 4:
      `16s`
    - Item 5:
      `24s`
    - Item 6:
      `32s`
    - Item 7:
      `40s`
    - Item 8:
      `48s`
    - Item 9:
      `56s`
```

---

### REPAIR 1J — Update ABORT logic (remove SORA_2, update KLING & SEEDANCE)

**FIND:**
```
    `ABORT IF engine_id NOT IN [VEO_3_1, GROK, SORA_2, KLING_3_0, SEEDANCE_2_0]`
```
**REPLACE WITH:**
```
    `ABORT IF engine_id NOT IN [VEO_3_1, GROK, KLING_3_0, SEEDANCE_2_0]`
```

---

**FIND:**
```
    `ABORT IF engine_id == VEO_3_1 AND duration_target NOT IN [8s, 16s, 24s, 32s, 40s, 48s, 56s]`
```
**REPLACE WITH:**
```
    `ABORT IF engine_id == VEO_3_1 AND duration_target NOT IN [4s, 6s, 8s, 16s, 24s, 32s, 40s, 48s, 56s]`
```

---

**FIND:**
```
    `ABORT IF engine_id == SORA_2 AND duration_target NOT IN [10s, 15s, 20s, 25s, 30s, 45s, 60s]`
```
**REPLACE WITH:** _(delete this line entirely)_

---

**FIND:**
```
    `ABORT IF engine_id == KLING_3_0 AND duration_target NOT IN [5s, 10s, 15s]`
```
**REPLACE WITH:**
```
    `ABORT IF engine_id == KLING_3_0 AND duration_target NOT IN [3s, 5s, 10s, 15s]`
```

---

**FIND:**
```
    `ABORT IF engine_id == SEEDANCE_2_0 AND duration_target NOT IN [10s, 20s]`
```
**REPLACE WITH:**
```
    `ABORT IF engine_id == SEEDANCE_2_0 AND duration_target NOT IN [5s, 10s, 15s]`
```

---

### REPAIR 1K — Update multi-block logic (remove SORA_2)

**FIND:**
```
      `Generate Multi-Block Array (IF engine_id IN [VEO_3_1, SORA_2, SEEDANCE_2_0] AND duration_target > block_max)`
```
**REPLACE WITH:**
```
      `Generate Multi-Block Array (IF engine_id IN [VEO_3_1, SEEDANCE_2_0] AND duration_target > block_max)`
```

---

**COMMIT MESSAGE:** `fix(master-ignition): remove SORA_2, update KLING/SEEDANCE/VEO/GROK specs [verified 2026-06-01]`

---

## FILE 2: `.claude/CLAUDE.md`

### REPAIR 2A — Update ENGINE CONSTRAINT TABLE

**FIND:**
```
║ VEO_3_1          ║ 56s      ║ 8,16,24,32,40,48,56s         ║ Standard 9-section script    ║
```
**REPLACE WITH:**
```
║ VEO_3_1          ║ 56s      ║ 4,6,8,16,24,32,40,48,56s     ║ Standard 9-section script    ║
```

---

**FIND:**
```
║ SORA_2           ║ 60s      ║ 10,15,20,25,30,45,60s        ║ Standard 9-section script    ║
```
**REPLACE WITH:** _(delete this entire row)_

---

**FIND:**
```
║ KLING_3_0        ║ 15s      ║ 5,10,15s                     ║ Standard 9-section script    ║
```
**REPLACE WITH:**
```
║ KLING_3_0        ║ 15s      ║ 3,5,10,15s                   ║ Standard 9-section script    ║
```

---

**FIND:**
```
║ SEEDANCE_2_0     ║ 20s      ║ 10,20s                       ║ Standard 9-section script    ║
║                  ║          ║                              ║ MULTI-BLOCK jika target > 20s║
```
**REPLACE WITH:**
```
║ SEEDANCE_2_0     ║ 15s      ║ 5,10,15s                     ║ Standard 9-section script    ║
```

---

### REPAIR 2B — Update IMPLICIT REQUIREMENT DETECTION table

**FIND:**
```
| "[X]s + SEEDANCE_2_0" | X > 20s → multi-block | Trigger STEP 3 |
```
**REPLACE WITH:**
```
| "[X]s + SEEDANCE_2_0" | X > 15s → multi-block | Trigger STEP 3 |
```

---

### REPAIR 2C — Remove SORA_2 dari MULTI-BLOCK TRIGGER MATRIX

**FIND:**
```
  GROK SPECIAL CASE — SEBELUM announce ke user:
```
*(Search for any SORA_2 references in the multi-block section and delete those lines)*

Specifically, find and delete any line containing `SORA_2` within the ENGINE CONSTRAINT TABLE section and MULTI-BLOCK TRIGGER MATRIX section.

---

### REPAIR 2D — Update engine validation check

**FIND:**
```
  Jika req_mode = B atau C dan req_engine = null → STOP. Tanya engine.
```
*(No change here, but search below for SORA_2 in ABORT IF lines)*

**FIND:**
```
  ABORT IF engine_id == SORA_2 AND duration_target NOT IN FETCH_FROM MASTER_IGNITION_TEMPLATE.duration_target
```
**REPLACE WITH:** _(delete this line if it exists)_

---

**COMMIT MESSAGE:** `fix(claude-md): remove SORA_2, update engine constraint table [verified 2026-06-01]`

---

## FILE 3: `.claude/skills/bosmax-compliance-gate.md`

### REPAIR 3A — Update engine table

**FIND:**
```
| VEO_3_1 | 56s | 8s, 16s, 24s, 32s, 40s, 48s, 56s | Standard 9-section |
| SORA_2 | 60s | 10s, 15s, 20s, 25s, 30s, 45s, 60s | Standard 9-section |
| KLING_3_0 | 15s | 5s, 10s, 15s | MULTI-BLOCK jika target > 15s |
| SEEDANCE_2_0 | 20s | 10s, 20s | MULTI-BLOCK jika target > 20s |
| GROK | 10s | 6s, 10s | MULTI-BLOCK jika target > 10s — FORBIDDEN: NANO BANANA |
```
**REPLACE WITH:**
```
| VEO_3_1 | 56s | 4s, 6s, 8s, 16s, 24s, 32s, 40s, 48s, 56s | Standard 9-section |
| KLING_3_0 | 15s | 3s, 5s, 10s, 15s | MULTI-BLOCK jika target > 15s |
| SEEDANCE_2_0 | 15s | 5s, 10s, 15s | SINGLE-BLOCK (max 15s) |
| GROK | 10s | 6s, 10s | MULTI-BLOCK jika target > 10s — FORBIDDEN: NANO BANANA |
```

---

### REPAIR 3B — Update engine_id valid list

**FIND:**
```
☐ engine_id valid: VEO_3_1_LITE | VEO_3_1 | SORA_2 | KLING_3_0 | SEEDANCE_2_0 | GROK | GOOGLE_FLOW
```
**REPLACE WITH:**
```
☐ engine_id valid: VEO_3_1_LITE | VEO_3_1 | KLING_3_0 | SEEDANCE_2_0 | GROK | GOOGLE_FLOW
```

---

### REPAIR 3C — Update ABORT checks in compliance gate

Find ALL instances of:
- `SORA_2` in ABORT logic lines → **delete those lines**
- `duration_target NOT IN [10s, 20s]` for SEEDANCE → update to `[5s, 10s, 15s]`
- `duration_target NOT IN [5s, 10s, 15s]` for KLING → update to `[3s, 5s, 10s, 15s]`
- `duration_target NOT IN [8s, 16s, 24s...]` for VEO_3_1 → add 4s and 6s

---

**COMMIT MESSAGE:** `fix(compliance-gate): remove SORA_2, update engine duration tables [verified 2026-06-01]`

---

## FILE 4: `SATELLITE_04_MAPPING_MATRIX.md`

### REPAIR 4A — Update engine_duration_specs

**FIND:**
```
  "VEO_3_1": "max_duration=56s",
  "SORA_2": "allowed_durations=[10s, 15s, 20s, 25s, 30s, 45s, 60s]",
  "GROK": "allowed_durations=[6s, 10s]",
  "KLING_3_0": "allowed_durations=[5s, 10s, 15s]",
  "SEEDANCE_2_0": "allowed_durations=[10s, 20s]"
```
**REPLACE WITH:**
```
  "VEO_3_1": "allowed_durations=[4s, 6s, 8s, 16s, 24s, 32s, 40s, 48s, 56s]",
  "GROK": "allowed_durations=[6s, 10s]",
  "KLING_3_0": "allowed_durations=[3s, 5s, 10s, 15s]",
  "SEEDANCE_2_0": "allowed_durations=[5s, 10s, 15s]"
```

---

### REPAIR 4B — Update engine block notes

**FIND:**
```
    - **VEO_3_1** (string): `Max 8s per block (Deterministic DNA Re-injection)`
    - **SORA_2** (string): `Max 15s per block (Allowed durations: 10s, 15s, 20s, 25s, 30s, 45s, 60s)`
    - **GROK** (string): `Max 10s single block (Allowed durations: 6s, 10s; No sharding permitted)`
    - **KLING_3_0** (string): `Max 15s single block`
    - **SEEDANCE_2_0** (string): `Max 10s per block (20s via dual-block chaining)`
```
**REPLACE WITH:**
```
    - **VEO_3_1** (string): `Max 8s per raw API block. Allowed: 4s, 6s, 8s (single block); 16s–56s via multi-block chaining`
    - **GROK** (string): `Max 10s single block (Allowed durations: 6s, 10s; No sharding permitted)`
    - **KLING_3_0** (string): `Max 15s single block (Allowed: 3s, 5s, 10s, 15s)`
    - **SEEDANCE_2_0** (string): `Max 15s single block (Allowed: 5s, 10s, 15s)`
```

---

### REPAIR 4C — Update all ABORT logic in SATELLITE_04

Find and apply:
- Remove all lines with `SORA_2` in ABORT conditions
- Update KLING_3_0 valid durations to `[3s, 5s, 10s, 15s]`
- Update SEEDANCE_2_0 valid durations to `[5s, 10s, 15s]`
- Update VEO_3_1 valid durations to add `4s` and `6s`

**COMMIT MESSAGE:** `fix(satellite-04): remove SORA_2, update engine specs [verified 2026-06-01]`

---

## FILE 5: `SATELLITE_05_COACHING_PROTOCOL.md`

### REPAIR 5A — Update duration query string for user

**FIND:**
```
  "query": "Berapa saat? [VEO_3_1: 8s-56s | SORA_2: 10s, 15s, 20s, 25s, 30s, 45s, 60s | GROK: 6s, 10s | KLING_3_0: 5s, 10s, 15s | SEEDANCE_2_0: 10s, 20s]",
```
**REPLACE WITH:**
```
  "query": "Berapa saat? [VEO_3_1: 4s,6s,8s,16s-56s | GROK: 6s,10s | KLING_3_0: 3s,5s,10s,15s | SEEDANCE_2_0: 5s,10s,15s]",
```

---

### REPAIR 5B — Update engine_id query

**FIND:**
```
  "query": "Engine video mana? (VEO_3_1, SORA_2, GROK, KLING_3_0, SEEDANCE_2_0)",
  "validation": "ENUM:[VEO_3_1, SORA_2, GROK, KLING_3_0, SEEDANCE_2_0]",
```
**REPLACE WITH:**
```
  "query": "Engine video mana? (VEO_3_1, GROK, KLING_3_0, SEEDANCE_2_0)",
  "validation": "ENUM:[VEO_3_1, GROK, KLING_3_0, SEEDANCE_2_0]",
```

---

### REPAIR 5C — Update ABORT logic in SATELLITE_05

Find and apply:
- Remove all `SORA_2` ABORT lines
- Update KLING_3_0 durations to include `3s`
- Update SEEDANCE_2_0 durations to `[5s, 10s, 15s]`
- Update VEO_3_1 durations to include `4s` and `6s`

**COMMIT MESSAGE:** `fix(satellite-05): remove SORA_2 from coaching prompts, update duration queries [verified 2026-06-01]`

---

## FILE 6: `SOVEREIGN_01_MASTER_SCHEMA.md`

### REPAIR 6A — Remove SORA_2 from supported_engines arrays

Find ALL occurrences of supported_engines arrays that include SORA_2, example:
```json
{
  "supported_engines": [
    "VEO_3_1",
    "SORA_2",
    "GROK",
    "KLING_3_0",
    "SEEDANCE_2_0"
  ]
}
```
**REPLACE ALL SUCH ARRAYS WITH:**
```json
{
  "supported_engines": [
    "VEO_3_1",
    "GROK",
    "KLING_3_0",
    "SEEDANCE_2_0"
  ]
}
```

### REPAIR 6B — Update ABORT logic

**FIND:**
```
    `ABORT IF engine_id == SORA_2 AND duration_target NOT IN FETCH_FROM MASTER_IGNITION_TEMPLATE.duration_target`
```
**REPLACE WITH:** _(delete this line)_

**FIND:**
```
    `ABORT IF engine_id == KLING_3_0 AND duration_target > 15s`
```
*(Keep this — 15s confirmed correct)*

**FIND:**
```
    `ABORT IF engine_id == SEEDANCE_2_0 AND duration_target > 20s`
```
**REPLACE WITH:**
```
    `ABORT IF engine_id == SEEDANCE_2_0 AND duration_target > 15s`
```

---

**COMMIT MESSAGE:** `fix(sovereign-01): remove SORA_2, update SEEDANCE max trigger [verified 2026-06-01]`

---

## FILE 7: `.claude/skills/bosmax-script-generator.md`

### REPAIR 7A — Update engine table in script generator

**FIND (approximate — search for this table):**
```
| SORA_2 | 60s | 10,15,20,25,30,45,60s | Standard 9-section script |
```
**REPLACE WITH:** _(delete this row)_

**FIND:**
```
engine_id             → VEO_3_1_LITE | VEO_3_1 | SORA_2 | KLING_3_0 |
```
**REPLACE WITH:**
```
engine_id             → VEO_3_1_LITE | VEO_3_1 | KLING_3_0 |
```

*(Search for all other SORA_2 references in this file and remove them)*

---

**COMMIT MESSAGE:** `fix(script-generator): remove SORA_2 from engine list [verified 2026-06-01]`

---

## FILE 8: `.claude/skills/bosmax-mode-c-executor.md`

### REPAIR 8A — Update engine table

**FIND:**
```
| SEEDANCE_2_0 | 20s | ...
```
*(search for SEEDANCE row in engine table)*
**REPLACE:** Update max dari 20s → 15s, durations [10s,20s] → [5s,10s,15s]

**FIND any SORA_2 references:** → **delete**

---

**COMMIT MESSAGE:** `fix(mode-c-executor): remove SORA_2, update SEEDANCE max [verified 2026-06-01]`

---

## FILE 9: `.claude/skills/bosmax-bulk-generator.md`

### REPAIR 9A — Update engine table

**FIND:**
```
| SEEDANCE_2_0 | 20s | ...
```
**REPLACE:** Update max 20s → 15s, durations → [5s,10s,15s]

**FIND any SORA_2 references:** → **delete**

**FIND:**
```
| "[X]s + SEEDANCE_2_0" | X > 20s → multi-block | Trigger STEP 3 |
```
**REPLACE WITH:**
```
| "[X]s + SEEDANCE_2_0" | X > 15s → multi-block | Trigger STEP 3 |
```

---

**COMMIT MESSAGE:** `fix(bulk-generator): remove SORA_2, update SEEDANCE max [verified 2026-06-01]`

---

## FILE 10: `.claude/skills/bosmax-requirement-analyst.md`

### REPAIR 10A — Update engine display and SORA_2 removal

Search for all references to:
- `SORA_2` → **delete/remove**
- SEEDANCE duration `20s` → update to `15s`
- KLING duration list → add `3s`
- VEO_3_1 duration list → add `4s` and `6s`

---

**COMMIT MESSAGE:** `fix(requirement-analyst): remove SORA_2, update engine duration displays [verified 2026-06-01]`

---

## FINAL GIT COMMIT (selepas semua files selesai)

```
git add -A
git commit -m "ENGINE SPECS OVERHAUL v1.0: remove SORA_2 (deprecated), verified KLING/SEEDANCE/GROK/VEO specs from official docs [2026-06-01]"
git push origin master
```

---

## VERIFICATION CHECKLIST UNTUK CODEX

Selepas selesai semua repairs, run search ini untuk confirm:

```
grep -r "SORA_2" .claude/ MASTER_IGNITION_TEMPLATE.md SATELLITE_04_MAPPING_MATRIX.md SATELLITE_05_COACHING_PROTOCOL.md SOVEREIGN_01_MASTER_SCHEMA.md
```
**Expected result: 0 matches (SORA_2 fully removed)**

```
grep -r "20s" .claude/skills/ | grep -i "seedance"
```
**Expected result: 0 matches (20s removed from SEEDANCE)**

```
grep -r '"4s"' MASTER_IGNITION_TEMPLATE.md
```
**Expected result: 2 matches (VEO_3_1 duration_target + engine_configuration)**

---

*Codex Repair Prompt v1.0 | Authority: Claude Orchestrator | 2026-06-01*
*Verified specs: Boss first-hand 2:59AM + ChatGPT Deep Research official API docs*
