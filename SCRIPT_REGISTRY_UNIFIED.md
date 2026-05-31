- **metadata** (object):
  - **file_id** (string): `SCRIPT_REGISTRY_UNIFIED`
  - **schema_version** (string): `v11.1`
  - **version_handshake** (string): `v11.1_GRAND_MASTER_SKELETON`
  - **last_edit_date** (string): `2026-03-05`
  - **fail_closed** (boolean): `true`
  - **file_manifest_limit** (string): `DYNAMIC`
  - **file_manifest_source** (string): `FETCH COUNT FROM SOVEREIGN_01_MASTER_SCHEMA.required_files_in_order`
  - **authority** (string): `SUPREME_SYSTEMS_ARCHITECT`
  - **namespace** (string): `SCRIPT_REGISTRY`
  - **role** (string): `LEAD_COPY_ARCHITECT`
- **invariants** (object):
  - **rules** (array):
    - Item 1:
      `All dialogue must follow fail-closed pacing (target 1.6 WPS, hard max 2.0 WPS, absolute kill-switch 3.0 WPS).`
    - Item 2:
      `ENFORCE: Pacing must follow Hook <= 2.0 WPS, Body/Problem <= 1.6 WPS, CTA <= 2.0 WPS.`
    - Item 3:
      `ENFORCE: language_tone_rules execution before dialogue assembly.`
    - Item 4:
      `Stealth scripts MUST include micro-expression tags synced to SOVEREIGN_03.savage_integrity_engine.`
    - Item 5:
      `Oral Physics: Viseme sync must match 10ms_latency_lock (SOVEREIGN_02).`
    - Item 6:
      `FETCH FROM SOVEREIGN_03_CORE_LOGIC.expansion_protocol.enforcement_level must be 100% for Total Lockdown.`
    - Item 7:
      `GATE_091 Name Substitution must execute BEFORE script generation.`
    - Item 8:
      `ENFORCE: Script narrative pacing must adapt to camera_mode. If UGC_IPHONE_RAW, script must feel raw, ad-hoc, and authentic. If CINEMATIC_PRO, script must match professional pacing.`
    - Item 9:
      `ENFORCE: Section 9 must follow strict Technical Schema mapping (COORD: X:%, Y:%).`
    - Item 10:
      `ENFORCE: Visual action and dialogue descriptions MUST bow to [PHYSICS_LOCK_MANDATORY] constraints. Do not generate actions (e.g., 'tightly grasping') if it conflicts with Class A 'PRECISION_PINCH' physics rules.`
    - Item 11:
      `IF camera_behavior IN [CAM_036, CAM_037] THEN SET target_wps = 1.4`
- **language_tone_rules** (object):
  - **description** (string): `Enforce language style based on silo_id and target language.`
  - **rules** (array):
    - Item 1:
```json
{
  "condition": "IF TL == 'Malay' AND silo_id == 'STEALTH'",
  "enforcement": "use_conversational_slang",
  "examples": [
    "aku",
    "kau",
    "lah",
    "weh"
  ]
}
```

    - Item 2:
```json
{
  "condition": "IF TL == 'Malay' AND silo_id == 'DIRECT'",
  "enforcement": "use_professional_fluency",
  "restrictions": [
    "NO slang tokens",
    "NO street register"
  ],
  "tone_reference": "FETCH FROM SATELLITE_02_LINT_NEGATIVES.linguistic_guards.pronoun_policy"
}
```

    - Item 3:
```json
{
  "condition": "IF TL == 'Malay' AND silo_id == 'DIRECT'",
  "enforcement": "use_contextual_tone",
  "tone_selection_source": "FETCH FROM SATELLITE_05_COACHING_PROTOCOL.language_context_selector"
}
```

    - Item 4:
```json
{
  "default": "FOLLOW dialogue_tone_only FROM SATELLITE_05_COACHING_PROTOCOL.language_context_selector"
}
```

    - Item 5:
```json
{
  "condition": "IF TL == 'Malay' AND silo_id == 'baby_maternity'",
  "enforcement": "use_gentle_caring_tone",
  "examples": [
    "sayang",
    "manja",
    "selesa",
    "pelukan"
  ]
}
```

    - Item 6:
```json
{
  "condition": "IF TL == 'Malay' AND silo_id == 'beauty_personal_care'",
  "enforcement": "use_glam_confidence_tone",
  "examples": [
    "seri",
    "glow",
    "aura",
    "yakin"
  ]
}
```

    - Item 7:
```json
{
  "condition": "IF TL == 'Malay' AND silo_id == 'fashion_accessories'",
  "enforcement": "use_stylish_exclusive_tone",
  "examples": [
    "kemas",
    "mahal",
    "upgrade",
    "exclusive"
  ]
}
```

    - Item 8:
```json
{
  "condition": "IF TL == 'Malay' AND silo_id == 'home_living'",
  "enforcement": "use_cozy_comfort_tone",
  "examples": [
    "cozy",
    "tenang",
    "upgrade ruang",
    "selesa"
  ]
}
```

    - Item 9:
```json
{
  "condition": "IF TL == 'Malay' AND silo_id == 'muslim_fashion'",
  "enforcement": "use_polite_modest_tone",
  "examples": [
    "sopan",
    "menutup aurat",
    "material sejuk"
  ]
}
```

    - Item 10:
```json
{
  "condition": "IF TL == 'Malay' AND silo_id == 'pet_supplies'",
  "enforcement": "use_caring_playful_tone",
  "examples": [
    "si bulu",
    "sihat bertenaga",
    "nutrisi lengkap"
  ]
}
```

    - Item 11:
```json
{
  "condition": "IF TL == 'Malay' AND silo_id == 'health'",
  "enforcement": "use_trustworthy_clinical_tone",
  "examples": [
    "kesihatan optimum",
    "ikhtiar",
    "kelulusan KKM"
  ]
}
```

    - Item 12:
```json
{
  "condition": "IF TL == 'Malay' AND silo_id == 'male_health_stealth_01'",
  "enforcement": "use_savage_mechanic_metaphor",
  "examples": [
    "tork",
    "piston",
    "overhaul",
    "tiang seri"
  ]
}
```

    - Item 13:
```json
{
  "condition": "IF TL == 'Malay' AND silo_id == 'female_health_stealth_01'",
  "enforcement": "use_botanical_elegance_metaphor",
  "examples": [
    "mekar",
    "seri",
    "sutera",
    "embun"
  ]
}
```

- **error_registry** (object):
  - **ABORT_PACING_VIOLATION** (string): `Dialogue density exceeds hard max 2.0 WPS (or absolute kill-switch 3.0 WPS) for interval (I).`
  - **ABORT_SILO_LEAK** (string): `Bimodal Isolation breach: Stealth/Direct overlap detected.`
  - **ABORT_PLACEHOLDER_LEAK** (string): `Unresolved technical markers {{ }} or [ ] detected in final prose.`
  - **ABORT_NAME_SUBSTITUTION_LEAK** (string): `Character name detected in output. Convert to biometric DNA.`
  - **ABORT_MEDICAL_CLAIM_VIOLATION** (string): `Forbidden medical claim term detected. Block generation per ENGINE_BANS.`
  - **ABORT_PRONOUN_VIOLATION** (string): `Pronoun policy breach detected. Check SAT_02.linguistic_guards.`
  - **ABORT_SSOT_DUR_VIOLATION** (string): `Engine duration exceeds SSOT physical limit (v11.1).`
  - **ABORT_ROBOTIC_MALAY** (string): `Robotic/Formal Malay detected in Stealth mode.`
  - **ABORT_DIALOGUE_TO_VISUAL_PROP_INSTANTIATION** (string): `Dialogue-only noun attempted to instantiate visual prop, packaging, object, background, or environment.`
  - **ABORT_METAPHOR_OBJECT_RENDER** (string): `Metaphor or silo vocabulary was literalized into physical visual output.`
  - **ABORT_VISUAL_SCENE_OVERRIDE** (string): `Dialogue or metaphor vocabulary attempted to override user-selected scene_context.`
  - **ABORT_INTERNAL_REFERENCE_LEAK** (object):
    - **description** (string): `Internal BOSMAX registry or system reference leaked into narrative output.`
    - **trigger_pattern_source** (string): `FETCH FROM SOVEREIGN_01_MASTER_SCHEMA.canonical_token_registry`
    - **suppress_markers_source** (string): `FETCH_FROM SATELLITE_02_LINT_NEGATIVES.technical_marker_suppression.suppress_markers`
    - **trigger_action** (array):
```json
[
  "ON_MATCH (PRE_ASSEMBLY): PREVENT_INSERTION_AND_REWRITE (MAP_TO_LABEL)",
  "ON_MATCH (POST_ASSEMBLY): SANITIZE_AND_REWRITE_PROSE"
]
```

    - **enforcement_action** (string): `ABORT_GENERATION_AND_REWRITE_PROSE_IF_UNREWRITABLE`
    - **audit** (string): `EMIT_DETAILED_AUDIT_RECORD`
  - **ABORT_TECHNICAL_ID_EXPOSURE** (object):
    - **description** (string): `Technical system identifiers exposed in narrative output.`
    - **trigger_patterns** (array):
```json
[
  "CLASS_A",
  "CLASS_B",
  "CLASS_C",
  "CLASS_D",
  "CLASS_E",
  "SAVAGE_",
  "AUTHENTIC_",
  "SEQ_",
  "SHOT_",
  "GAUM",
  "PACAK",
  "SUBUR",
  "HARDNESS",
  "DOMINANCE"
]
```

    - **enforcement_action** (string): `SANITIZE_AND_REWRITE_TO_NATURAL_LANGUAGE`
  - **ERR_SCHEMA_MISMATCH** (string): `Data does not conform to Master Schema v11.1.`
  - **ERR_UNDEF_REF** (string): `Reference to unmapped trigger or silo in SATELLITE_04.`
  - **ERR_VOCAB_FALLBACK_v11.1** (string): `Product type fallback applied. DIRECT safe vocab enforced.`
  - **ERR_NANO_BANANA_BREACH** (string): `Forbidden submode (NANO BANANA) detected for engine GROK.`
  - **ERR_ENGINE_VERSION_MISMATCH** (string): `Engine version does not match BOSMAX v11.1 standards.`
  - **ERR_SEEDANCE_NOT_CONFIGURED** (string): `Seedance 2.0 selected but not configured in manifest.`
  - **ERR_KLING_HEURISTIC_VIOLATION** (string): `Kling 3.0 parameters exceed SSOT physical thresholds.`
  - **ERR_SSOT_DURATION_CONFLICT** (string): `Input duration not in engine-specific allowed list.`
  - **ERR_TOKEN_LIMIT_RISK** (string): `VEO duration above 56s is forbidden in fail-closed mode.`
  - **ERR_COORD_SCHEMA_VIOLATION** (string): `Section 9 fails technical coordinate schema (Missing X,Y mapping).`
  - **ERR_CAMERA_LIGHTING_CONFLICT** (string): `Invalid pairing: UGC_IPHONE_RAW cannot use STUDIO_5600K lighting.`
- **dialogue_assembly_rules** (object):
  - **protocol** (string): `SCENE_BASED_ORCHESTRATION`
  - **authority_boundary** (object):
    - **dialogue_scope_only** (boolean): `true`
    - **visual_instantiation_forbidden** (boolean): `true`
    - **forbidden_visual_effects** (array):
```json
[
  "NO_PROP_INSTANTIATION",
  "NO_PACKAGING_INSTANTIATION",
  "NO_OBJECT_RENDER",
  "NO_BACKGROUND_OVERRIDE",
  "NO_ENVIRONMENT_OVERRIDE",
  "NO_SCENE_CONTEXT_OVERRIDE"
]
```

    - **enforcement** (string): `FAIL_CLOSED`
  - **expansion_mode** (object):
    - **primary** (string): `TEMPLATE_DRIVEN`
    - **template_source** (string): `SCRIPT_VARIANT_LIBRARY.variant_library`
    - **expansion_steps** (array):
```json
[
  "FETCH template by submode_formula and silo",
  "FILL slots with coaching_protocol atomic_variables and canonical labels",
  "APPLY micro-expression expansion mapping (see SATELLITE_03.micro_expression_map)",
  "RUN sanitizer (MASTER_IGNITION.output_cleanroom_protocol) in PRE_ASSEMBLY mode",
  "ASSEMBLE scene block respecting WPS limits",
  "MARK dialogue output as NON_AUTHORITATIVE_FOR_VISUAL"
]
```

    - **fallback** (object):
```json
{
  "mode": "LIMITED_HEURISTIC",
  "max_words": 20,
  "constraints": [
    "No insertion of technical ids or raw registry names",
    "All generated phrases must pass sanitizer_patterns",
    "No dialogue noun may instantiate prop, packaging, object, environment, or background"
  ]
}
```

  - **expansion_validation** (object):
    - **enforce_db_driven** (boolean): `true`
    - **abort_on_template_missing** (boolean): `true`
    - **abort_on_visual_cross_inheritance** (boolean): `true`
- **pronoun_enforcement** (object):
  - **protocol** (string): `SAT_02_LINGUISTIC_GUARDS_ALIGNMENT`
  - **protocol_source** (string): `FETCH FROM SATELLITE_02_LINT_NEGATIVES.linguistic_guards`
  - **stealth_mode** (object):
    - **allowed** (array):
```json
[
  "aku",
  "kau",
  "jantan",
  "bro",
  "abang",
  "kita"
]
```

    - **forbidden** (array):
```json
[
  "saya",
  "anda",
  "awak",
  "kamu"
]
```

    - **forced_reference** (string): `CONTEXT_DEPENDENT`
    - **forced_reference_source** (string): `FETCH FROM SATELLITE_02_LINT_NEGATIVES.linguistic_guards.pronoun_policy.stealth`
    - **description** (string): `Pronoun policy for ENGINE_STEALTH mode per SAT_02`
  - **direct_mode** (object):
    - **allowed** (array):
```json
[
  "saya",
  "anda",
  "kita",
  "tuan",
  "puan"
]
```

    - **forbidden** (array):
```json
[
  "aku",
  "kau",
  "lu",
  "gua",
  "weh",
  "doh",
  "abang"
]
```

    - **forced_reference** (string): `SAYA`
    - **forced_reference_source** (string): `FETCH FROM SATELLITE_02_LINT_NEGATIVES.linguistic_guards.pronoun_policy.direct`
    - **description** (string): `Pronoun policy for ENGINE_DIRECT mode per SAT_02`
  - **validation_guards** (array):
    - Item 1:
      `ABORT IF stealth_mode uses direct pronouns`
    - Item 2:
      `ABORT IF direct_mode uses stealth pronouns`
    - Item 3:
      `ENFORCE: pronoun_policy_lock per execution_mode`
- **stealth_narrative_library** (object):
  - **male_health_vintage_car** (object):
    - **silo_id** (string): `male_health_vintage_car`
    - **silo_id_source** (string): `FETCH FROM SOVEREIGN_01_MASTER_SCHEMA.silo_vocabulary_authority`
    - **trigger_ids** (array):
```json
[
  "MARUAH_01",
  "EGO_01",
  "AUTHORITY_01",
  "SCARCITY_01",
  "TRANSFORMATION_01"
]
```

    - **trigger_ids_source** (string): `FETCH FROM MASTER_IGNITION_TEMPLATE.trigger_id`
    - **eligible_avatars** (array):
```json
[
  "NORA",
  "JULIA",
  "RIZAL",
  "AZMAN"
]
```

    - **eligible_avatars_source** (string): `FETCH FROM SATELLITE_03_VISUAL_DECK.archetypes`
    - **formula_templates** (object):
```json
{
  "PAS": {
    "structure": "{user_hook} | [PROBLEM] -> [AGITATE] -> [SOLUTION] | {user_usp} | {user_cta}",
    "structure_source": "FETCH FROM SOVEREIGN_03_CORE_LOGIC.copy_dna_layer.formula_assembly_templates.PAS",
    "tone_enforcement_stealth": "MANDATORY: Gunakan kiasan kasar alat pertukangan/mekanikal STEALTH (cangkul karat, piston semput, gearbox sangkut, enjin kong, tiang layu) dari SCRIPT_VARIANT_LIBRARY.variant_library",
    "tone_enforcement_direct": "MANDATORY: Gunakan direct EGO/MARUAH kick DIRECT (bau macam tak mandi, malu la, pakai branded tapi bau peluh, konfiden hilang) dari SCRIPT_VARIANT_LIBRARY.variant_library",
    "scripts": [
      {
        "id": "STEALTH_CAR_PAS_001",
        "timestamp": "[00:00 - 00:08]",
        "hook": "[narrowed_eyes] Enjin nampak garang, tapi baru ram sikit dah semput. Lemah!",
        "problem": "[dismissive_lip_curl] Malu la bang, bini baru masuk gear satu, abang dah tersadai tepi jalan. Minyak bocor ke?",
        "agitate": "[chin_up_judgemental_stare] Sembang nak ride jauh. Tapi ekzos asap putih. Kelakar! Baru nak memotong, batang shaft dah goyang.",
        "solution": "[shrug_dismissive] Overhaul gearbox tu pakai minyak padu ni. Masuk gear licin, pick-up terus pacak.",
        "usp": "Servis piston abang tu. Biar naik tegang, tork mencanak sampai pagi. Tak ada istilah 'enjin kong'.",
        "cta": "[point_at_camera] SERVIS 'ENJIN' SEKARANG. Tekan beg kuning.",
        "expansion_mandate": {
          "min_words": 50,
          "ratio": "1:5",
          "description": "Expand with biometric DNA: 15Hz tremor, 38-C elevation, 2mm air-gap on product HOI"
        }
      },
      {
        "id": "STEALTH_CAR_PAS_002",
        "timestamp": "[00:08 - 00:16]",
        "hook": "[asymmetric_mocking_smirk] Sembang nak tune-up. Tapi mounting pun dah longgar. Sedih!",
        "problem": "[narrowed_eyes] Ingat boleh drag race. Sekali warming up pun tak lepas. Piston dah kena carbon deposit.",
        "agitate": "[chin_up_judgemental_stare] Mileage hancur, tork hilang, pickup kurang. Macam mana nak potong lane kanan?",
        "solution": "[shrug_dismissive] Restore balik dengan formula ni. Karburetor bersih, ekzos lancar, enjin nyanyi.",
        "usp": "Mekanik pun pakai ni. Bengkel pun recommend. Konfirm mounting ketat balik.",
        "cta": "[point_at_camera] DAPATKAN SEKARANG. Jangan tunggu enjin kong.",
        "expansion_mandate": {
          "min_words": 50,
          "ratio": "1:5",
          "description": "Expand with physics DNA: CLASS_A rigid-body, kinematic_disentanglement, collision_mesh_integrity"
        }
      }
    ]
  },
  "HSO": {
    "structure": "{user_hook} | [HOOK] -> [STORY] -> [OFFER] | {user_usp} | {user_cta}",
    "structure_source": "FETCH FROM SOVEREIGN_03_CORE_LOGIC.copy_dna_layer.formula_assembly_templates.HSO",
    "tone_enforcement_stealth": "MANDATORY: Gunakan kiasan kasar alat pertukangan/mekanikal STEALTH (cangkul karat, piston semput, gearbox sangkut, enjin kong, tiang layu) dari SCRIPT_VARIANT_LIBRARY.variant_library",
    "tone_enforcement_direct": "MANDATORY: Gunakan direct EGO/MARUAH kick DIRECT (bau macam tak mandi, malu la, pakai branded tapi bau peluh, konfiden hilang) dari SCRIPT_VARIANT_LIBRARY.variant_library",
    "scripts": [
      {
        "id": "STEALTH_CAR_HSO_001",
        "timestamp": "[00:00 - 00:08]",
        "hook": "[narrowed_eyes] Abang ingat piston abang power lagi ke?",
        "story": "[dismissive_lip_curl] Sekali ram, asap je keluar, batang piston tak naik-naik pun. Malu la dengan orang rumah, baru masuk gear satu, enjin dah semput.",
        "offer": "[chin_up_judgemental_stare] Kalau tak servis pakai minyak padu ni, silap haribulan kena overhaul satu badan.",
        "usp": "Tork mantap, mileage jimat, pickup responsif. Tak ada lagi istilah 'tengah jalan tersadai'.",
        "cta": "[point_at_camera] Servis 'enjin' abang sekarang kat beg kuning.",
        "expansion_mandate": {
          "min_words": 50,
          "ratio": "1:5",
          "description": "Expand with oral_physics: 10ms_latency_lock, vowel_elongation, jaw_dropdown"
        }
      }
    ]
  },
  "AIDA": {
    "structure": "{user_hook} | [ATTENTION] -> [INTEREST] -> [DESIRE] -> [ACTION] | {user_usp} | {user_cta}",
    "tone_enforcement_stealth": "MANDATORY: Gunakan kiasan kasar alat pertukangan/mekanikal STEALTH (cangkul karat, piston semput, gearbox sangkut, enjin kong, tiang layu) dari SCRIPT_VARIANT_LIBRARY.variant_library",
    "tone_enforcement_direct": "MANDATORY: Gunakan direct EGO/MARUAH kick DIRECT (bau macam tak mandi, malu la, pakai branded tapi bau peluh, konfiden hilang) dari SCRIPT_VARIANT_LIBRARY.variant_library",
    "scripts": [
      {
        "id": "STEALTH_CAR_AIDA_001",
        "timestamp": "[00:00 - 00:08]",
        "attention": "[narrowed_eyes] Attention: Enjin abang dah ada bunyi bising ke?",
        "interest": "[dismissive_lip_curl] Interest: mounting longgar, gear box bunyi, radiator panas.",
        "desire": "[chin_up_judgemental_stare] Desire: Bayangkan enjin nyanyi, tork mencanak, mileage jimat.",
        "action": "[point_at_camera] Action: Klik beg kuning sebelum terlambat.",
        "usp": "Overhaul lengkap, spare part original, mekanik certified.",
        "cta": "Jangan tunggu rosak baru nak servis.",
        "expansion_mandate": {
          "min_words": 50,
          "ratio": "1:5",
          "description": "Expand with camera_behavior: SHOT_CRASH_ZOOM_REVEAL, sensor_noise_injection"
        }
      }
    ]
  }
}
```

    - **validation_guards** (array):
```json
[
  "ABORT IF forbidden_name_tokens detected (GATE_091)",
  "ENFORCE: pronoun_enforcement.stealth_mode",
  "VALIDATE: silo_vocabulary alignment per SOV_01"
]
```

  - **agri_kebun_baja** (object):
    - **silo_id** (string): `agri_kebun_baja`
    - **silo_id_source** (string): `FETCH FROM SOVEREIGN_01_MASTER_SCHEMA.silo_vocabulary_authority`
    - **trigger_ids** (array):
```json
[
  "TRANSFORMATION_01",
  "SCARCITY_01",
  "AUTHORITY_01",
  "MARUAH_01"
]
```

    - **trigger_ids_source** (string): `FETCH FROM MASTER_IGNITION_TEMPLATE.trigger_id`
    - **eligible_avatars** (array):
```json
[
  "NORA",
  "JULIA",
  "RIZAL",
  "MAK_TOK"
]
```

    - **eligible_avatars_source** (string): `FETCH FROM SATELLITE_03_VISUAL_DECK.archetypes`
    - **formula_templates** (object):
```json
{
  "PAS": {
    "structure": "{user_hook} | [PROBLEM] -> [AGITATE] -> [SOLUTION] | {user_usp} | {user_cta}",
    "structure_source": "FETCH FROM SOVEREIGN_03_CORE_LOGIC.copy_dna_layer.formula_assembly_templates.PAS",
    "tone_enforcement_stealth": "MANDATORY: Gunakan kiasan kasar alat pertukangan/mekanikal STEALTH (cangkul karat, piston semput, gearbox sangkut, enjin kong, tiang layu) dari SCRIPT_VARIANT_LIBRARY.variant_library",
    "tone_enforcement_direct": "MANDATORY: Gunakan direct EGO/MARUAH kick DIRECT (bau macam tak mandi, malu la, pakai branded tapi bau peluh, konfiden hilang) dari SCRIPT_VARIANT_LIBRARY.variant_library",
    "scripts": [
      {
        "id": "STEALTH_AGRI_PAS_001",
        "timestamp": "[00:00 - 00:08]",
        "hook": "[narrowed_eyes] Terung abang tu dah layu ke? Kena hujan sikit dah tunduk. Sedih!",
        "problem": "[dismissive_lip_curl] Ingat boleh tuai hasil, rupanya batang pokok pun tak larat nak berdiri.",
        "agitate": "[chin_up_judgemental_stare] Macam mana nak merimbun? Tanah gersang, akar tak tunjang, daun kuning.",
        "solution": "[shrug_dismissive] Siram baja booster ni. Esok pagi konfirm batang pacak keras macam tiang seri.",
        "usp": "Baja pekat, akar kuat, hasil mencanak. Baru puas hati tengok kebun.",
        "cta": "[point_at_camera] SUBURKAN 'KEBUN' SEKARANG. Tekan beg kuning.",
        "expansion_mandate": {
          "min_words": 50,
          "ratio": "1:5",
          "description": "Expand with biometric DNA: skin_texture, wisdom_lines, 8Hz calm_respiration_tremor"
        }
      }
    ]
  },
  "HSO": {
    "structure": "{user_hook} | [HOOK] -> [STORY] -> [OFFER] | {user_usp} | {user_cta}",
    "structure_source": "FETCH FROM SOVEREIGN_03_CORE_LOGIC.copy_dna_layer.formula_assembly_templates.HSO",
    "scripts": [
      {
        "id": "STEALTH_AGRI_HSO_001",
        "timestamp": "[00:00 - 00:08]",
        "hook": "[narrowed_eyes] Tengok 'terung' abang tu, lembik semacam je.",
        "story": "[dismissive_lip_curl] Kena hujan sikit dah tunduk layu, macam mana nak tuai hasil? Tanah kalau tak cukup baja, memang batang pokok takkan keras.",
        "offer": "[chin_up_judgemental_stare] Nak bagi pacak balik macam tiang seri, kena siram dengan baja booster ni.",
        "usp": "Akar tunjang kuat, daun hijau merimbun, hasil tanaman mencanak.",
        "cta": "[point_at_camera] Bagi keras balik 'kebun' abang, tekan beg kuning.",
        "expansion_mandate": {
          "min_words": 50,
          "ratio": "1:5",
          "description": "Expand with scene_context: CTX_KAMPUNG_VERANDAH, 5600K_raw_sunlight"
        }
      }
    ]
  }
}
```

    - **validation_guards** (array):
```json
[
  "ABORT IF forbidden_name_tokens detected (GATE_091)",
  "ENFORCE: pronoun_enforcement.stealth_mode",
  "VALIDATE: silo_vocabulary alignment per SOV_01"
]
```

  - **baby_maternity** (object):
    - **silo_id** (string): `baby_maternity`
    - **silo_id_source** (string): `FETCH FROM SOVEREIGN_01_MASTER_SCHEMA.silo_vocabulary_authority`
    - **trigger_ids** (array):
```json
[
  "COMFORT_01",
  "SAFETY_01",
  "SLEEP_01"
]
```

    - **formula_templates** (object):
```json
{
  "PAS": {
    "structure": "{user_hook} | [PROBLEM] -> [AGITATE] -> [SOLUTION] | {user_usp} | {user_cta}",
    "tone_enforcement_stealth": "MANDATORY: Gunakan kiasan lembut/penjagaan (kulit sensitif, tidur lena, pelukan ibu) dari SCRIPT_VARIANT_LIBRARY.variant_library",
    "expansion_mandate": {
      "min_words": 50,
      "ratio": "1:5"
    }
  }
}
```

  - **beauty_personal_care** (object):
    - **silo_id** (string): `beauty_personal_care`
    - **silo_id_source** (string): `FETCH FROM SOVEREIGN_01_MASTER_SCHEMA.silo_vocabulary_authority`
    - **trigger_ids** (array):
```json
[
  "GLOW_UP_01",
  "CONFIDENCE_01",
  "AURA_01"
]
```

    - **formula_templates** (object):
```json
{
  "PAS": {
    "structure": "{user_hook} | [PROBLEM] -> [AGITATE] -> [SOLUTION] | {user_usp} | {user_cta}",
    "tone_enforcement_stealth": "MANDATORY: Gunakan kiasan kecantikan/keyakinan (seri wajah, aura bintang, glow up) dari SCRIPT_VARIANT_LIBRARY.variant_library",
    "expansion_mandate": {
      "min_words": 50,
      "ratio": "1:5"
    }
  }
}
```

  - **fashion_accessories** (object):
    - **silo_id** (string): `fashion_accessories`
    - **silo_id_source** (string): `FETCH FROM SOVEREIGN_01_MASTER_SCHEMA.silo_vocabulary_authority`
    - **trigger_ids** (array):
```json
[
  "STYLE_01",
  "EXCLUSIVE_01",
  "TREND_01"
]
```

    - **formula_templates** (object):
```json
{
  "PAS": {
    "structure": "{user_hook} | [PROBLEM] -> [AGITATE] -> [SOLUTION] | {user_usp} | {user_cta}",
    "tone_enforcement_stealth": "MANDATORY: Gunakan kiasan gaya/eksklusif (nampak mahal, kemas, upgrade look) dari SCRIPT_VARIANT_LIBRARY.variant_library",
    "expansion_mandate": {
      "min_words": 50,
      "ratio": "1:5"
    }
  }
}
```

  - **home_living** (object):
    - **silo_id** (string): `home_living`
    - **silo_id_source** (string): `FETCH FROM SOVEREIGN_01_MASTER_SCHEMA.silo_vocabulary_authority`
    - **trigger_ids** (array):
```json
[
  "COZY_01",
  "COMFORT_01",
  "DECOR_01"
]
```

    - **formula_templates** (object):
```json
{
  "PAS": {
    "structure": "{user_hook} | [PROBLEM] -> [AGITATE] -> [SOLUTION] | {user_usp} | {user_cta}",
    "tone_enforcement_stealth": "MANDATORY: Gunakan kiasan keselesaan/ruang (rumah tenang, upgrade ruang, vibe premium) dari SCRIPT_VARIANT_LIBRARY.variant_library",
    "expansion_mandate": {
      "min_words": 50,
      "ratio": "1:5"
    }
  }
}
```

- **gate_091_name_substitution_check** (object):
  - **gate_id** (string): `GATE_091_NAME_SUBSTITUTION_ABORT`
  - **gate_id_source** (string): `FETCH FROM SOVEREIGN_01_MASTER_SCHEMA.gate_registry.GATE_091_NAME_SUBSTITUTION_ABORT`
  - **forbidden_name_tokens** (array):
    - Item 1:
      `Nora`
    - Item 2:
      `Rizal`
    - Item 3:
      `Azman`
    - Item 4:
      `Mak_Tok`
    - Item 5:
      `Julia`
    - Item 6:
      `Sara`
    - Item 7:
      `Bella`
    - Item 8:
      `Sofia_Fit`
    - Item 9:
      `Haji_Man`
    - Item 10:
      `Chef_Danial`
  - **detection_method** (string): `REGEX_SCAN_OUTPUT`
  - **enforcement_mandate** (string): `Convert ID to Biometric Blueprint (pores, hydration 0.9, philtrum)`
  - **abort_code** (string): `ABORT_NAME_SUBSTITUTION_LEAK`
  - **validation_guards** (array):
    - Item 1:
      `ABORT IF forbidden_name_tokens detected in any script`
    - Item 2:
      `ENFORCE: Convert all character IDs to biometric DNA descriptors`
    - Item 3:
      `VALIDATE: regex_scan_output on all final prose before render`
- **expansion_placeholders** (object):
  - **protocol** (string): `SOV_03_EXPANSION_PROTOCOL_ALIGNMENT`
  - **protocol_source** (string): `FETCH FROM SOVEREIGN_03_CORE_LOGIC.expansion_protocol`
  - **min_words** (string): `FETCH FROM SOVEREIGN_03_CORE_LOGIC.expansion_protocol.min_words`
  - **ratio** (string): `FETCH FROM SOVEREIGN_03_CORE_LOGIC.expansion_protocol.ratio`
  - **enforcement_level** (string): `FETCH FROM SOVEREIGN_03_CORE_LOGIC.expansion_protocol.enforcement_level`
  - **validation_guards** (array):
    - Item 1:
      `ENFORCE: min_words == 50 for all expansion_placeholders`
    - Item 2:
      `ENFORCE: ratio == 1:5 for all content expansion`
    - Item 3:
      `ABORT IF summarization == DETECTED`
    - Item 4:
      `VALIDATE: enforcement_level == 100% for Total Lockdown`
- **multimodal_stitching** (object):
  - **video_mode** (object):
    - **temporal_stitching** (string): `EXECUTE: Stitching Protocol per PROJECT_INSTRUCTION.PacingGuard.Logic`
    - **oral_physics** (string): `FETCH FROM SOVEREIGN_02_PHYSICS_DNA.oral_physics MATCHING physics_mode.`
    - **interval_sync** (string): `SYNC_TO_INTERVAL_I`
    - **interval_sync_source** (string): `FETCH FROM MASTER_IGNITION.block_math_configuration`
  - **image_mode** (object):
    - **hoi_interaction** (string): `APPLY: kinematic_disentanglement AND collision_mesh_integrity.`
    - **gap_enforcement** (string): `MANDATORY: 2mm air-gap per SOVEREIGN_02.CLASS_A.`
  - **poster_mode** (object):
    - **spatial_hierarchy** (string): `ENFORCE: SATELLITE_02.safe_zone_matrix.TIKTOK_SHOP.`
  - **validation_guards** (array):
    - Item 1:
      `ENFORCE: temporal_stitching on all video_mode scripts`
    - Item 2:
      `VALIDATE: hoi_interaction on all image_mode scripts`
    - Item 3:
      `ENFORCE: spatial_hierarchy on all poster_mode scripts`
- **validation_guards** (array):
  - Item 1:
    `ABORT IF product_type == DIRECT AND keyword IN [piston, enjin, cangkul, pancang, batang, semput, gearbox, signal 1 bar]`
  - Item 2:
    `ABORT IF product_type == STEALTH AND keyword IN DIRECT_safe_vocab`
  - Item 3:
    `ABORT IF script.word_count > (duration_target * 2.0)`
  - Item 4:
    `ABORT IF script.word_count > (duration_target * 3.0) [ABSOLUTE_KILL_SWITCH]`
  - Item 5:
    `ABORT IF speech_expected == true AND spoken_coverage_ratio < 0.25`
  - Item 6:
    `ABORT IF speech_expected == true AND speech_timestamps_missing == true`
  - Item 7:
    `ABORT IF speech_expected == true AND tail_silence_s exceeds duration-band limit from SOVEREIGN_03.pacing_governance`
  - Item 8:
    `ABORT IF speech_expected == true AND silence_gap_s exceeds duration-band limit from SOVEREIGN_03.pacing_governance`
  - Item 9:
    `ENFORCE: Surgical Scrub V2 on all final output prose.`
  - Item 10:
    `VERIFY: SATELLITE_03 expressions match SOVEREIGN_03.savage_integrity_engine`
  - Item 11:
    `ABORT IF forbidden_name_tokens detected in any script (GATE_091)`
  - Item 12:
    `ENFORCE: pronoun_enforcement per execution_mode`
  - Item 13:
    `VALIDATE: expansion_placeholders min_words == 50`
  - Item 14:
    `ENFORCE: FETCH FROM SOVEREIGN_03_CORE_LOGIC.expansion_protocol.ratio = 1:5 expansion`
  - Item 15:
    `ABORT IF timestamp_syntax not in [START_TIME - END_TIME] format`
  - Item 16:
    `VALIDATE: silo_id alignment per SOVEREIGN_01.silo_vocabulary_authority`
  - Item 17:
    `ENFORCE: avatar_id alignment per SATELLITE_03.archetypes`
  - Item 18:
    `ABORT IF dialogue noun is used to instantiate prop, packaging, object, background, or environment in visual sections`
  - Item 19:
    `ABORT IF metaphor vocabulary from silo_metaphor_matrix is literalized into physical visual output`
  - Item 20:
    `ABORT IF dialogue output attempts to override scene_context selected by user`
  - Item 21:
    `ENFORCE: dialogue output is NON_AUTHORITATIVE_FOR_VISUAL`
  - Item 22:
    `ENFORCE: dialogue channel may influence wording only, never visual asset selection`
  - Item 23:
    `ABORT IF keyword IN [SCRIPT_VARIANT_LIBRARY, SOVEREIGN_, SATELLITE_, MASTER_IGNITION, FETCH FROM]`
  - Item 24:
    `ABORT IF keyword IN [CLASS_A, CLASS_B, CLASS_C, CLASS_D, CLASS_E, CAM_, CTX_, SHOT_, W_, TEMP_, SAVAGE_, AUTHENTIC_]`
  - Item 25:
    `ABORT IF physics_class == 'AUTO_FETCH' AT FINAL_ASSEMBLY_STAGE`
  - Item 26:
    `ENFORCE: coaching_protocol.fallback_logic must resolve AUTO_FETCH before assembly`
  - Item 27:
    `ENFORCE: dna_reinjection_hop == 1 for every block boundary`
  - Item 28:
    `MAP: IF MASTER_IGNITION_TEMPLATE.dna_reinjection_interval_time EXISTS FOR engine_id THEN derive dna_reinjection_hop = CEIL(duration_target_seconds / parse_seconds(MASTER_IGNITION_TEMPLATE.dna_reinjection_interval_time[engine_id]))`
  - Item 29:
    `VALIDATE: dna_reinjection_interval_time format == '<integer>s'`
  - Item 30:
    `--- SSOT ENGINE SPECIFIC LOCKS ---`
  - Item 31:
    `ABORT IF engine_id == KLING_3_0 AND duration_target > 15s`
  - Item 32:
    `ABORT IF engine_id == SEEDANCE_2_0 AND duration_target > 15s`
  - Item 33:
    `ABORT IF engine_id == GROK AND duration_target NOT IN FETCH_FROM MASTER_IGNITION_TEMPLATE.engine_configuration.GROK.supported_durations`
  - Item 34:
    `ENFORCE: IF engine_id == GROK THEN SINGLE_BLOCK_EXECUTION_ONLY`
  - Item 35:
    `ABORT IF engine_id == GROK AND duration_target > 10s`
  - Item 36:
    `ABORT IF engine_id == GROK AND execution_submode == 'NANO BANANA'`
  - Item 37:
    `ENFORCE: 10ms_latency_lock for viseme_sync on CAM_036, CAM_037`
  - Item 38:
    `ENFORCE: Script pacing adapts to camera_mode. UGC_IPHONE_RAW requires raw authentic script. CINEMATIC_PRO requires professional pacing.`
  - Item 39:
    `VALIDATE: schema_version == v11.1`
