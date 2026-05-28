- **metadata** (object):
  - **file_id** (string): `SOVEREIGN_03_CORE_LOGIC`
  - **schema_version** (string): `v11.1`
  - **version_handshake** (string): `v11.1_GRAND_MASTER_SKELETON`
  - **last_edit_date** (string): `2026-03-05`
  - **authority** (string): `SUPREME_SYSTEMS_ARCHITECT`
- **intelligence_layer** (object):
  - **global_marketing_laws** (object):
    - **visual_first_protocol** (boolean): `true`
    - **silo_purity** (string): `ONE_VIDEO_ONE_SILO`
    - **metaphor_switch_guard** (string): `FORBIDDEN`
    - **funnel_requirement** (array):
```json
[
  "TOFU",
  "MOFU",
  "BOFU"
]
```

    - **formula_support** (array):
```json
[
  "PAS",
  "HSO",
  "AIDA",
  "FAB",
  "SAVAGE_HPAS"
]
```

    - **mode_c_route_alias** (string): `MODE_C is the canonical route token. SPECIAL_LANE is the authority alias for Mode C enforcement.`
    - **mode_c_special_lane_policy** (string): `IF route_mode == SPECIAL_LANE THEN visual_sections source authority == MODE_C_METADATA_HANDOFF. Dialogue/Copywriting MUST NOT override inherited image DNA.`
  - **visual_dialogue_isolation_policy** (object):
    - **status** (string): `MANDATORY_FAIL_CLOSED`
    - **visual_authority_scope** (object):
```json
{
  "allowed_sources": [
    "MODE_C_METADATA_HANDOFF",
    "MASTER_IGNITION_TEMPLATE.user_input.scene_context",
    "SATELLITE_03_VISUAL_DECK.scene_output_translation",
    "SATELLITE_03_VISUAL_DECK.scene_registry",
    "SATELLITE_03_VISUAL_DECK.camera_behavior_map",
    "SOVEREIGN_02_PHYSICS_DNA"
  ],
  "forbidden_sources": [
    "SCRIPT_REGISTRY_UNIFIED",
    "SCRIPT_VARIANT_LIBRARY",
    "dialogue",
    "hook",
    "problem",
    "agitate",
    "solution",
    "story",
    "offer",
    "usp",
    "cta",
    "silo_metaphor_matrix.allowed_vocab",
    "silo_metaphor_matrix.spine_logic"
  ]
}
```

    - **dialogue_authority_scope** (object):
```json
{
  "allowed_sources": [
    "SCRIPT_REGISTRY_UNIFIED",
    "SCRIPT_VARIANT_LIBRARY",
    "SATELLITE_05_COACHING_PROTOCOL"
  ],
  "forbidden_effect": [
    "NO_PROP_INSTANTIATION",
    "NO_BACKGROUND_INSTANTIATION",
    "NO_ENVIRONMENT_OVERRIDE",
    "NO_OBJECT_RENDER_FROM_DIALOGUE_NOUNS"
  ]
}
```

    - **section_lock** (object):
```json
{
  "visual_sections": [
    "Section_1",
    "Section_2",
    "Section_3",
    "Section_4",
    "Section_5",
    "Section_7",
    "Section_8"
  ],
  "dialogue_section": [
    "Section_6"
  ],
  "visual_rule": "Sections_1_2_3_4_5_7_8 MUST derive only from visual_authority_scope.allowed_sources",
  "dialogue_rule": "Section_6 MUST NOT override or enrich visual sections"
}
```

    - **contamination_detection** (object):
```json
{
  "trigger": "IF noun_or_object appears in visual output AND source_of_truth == dialogue_only THEN ABORT_VISUAL_COPY_LEAK",
  "metaphor_literalization_guard": "IF visual object is inferred from silo metaphor or dialogue metaphor THEN ABORT_VISUAL_COPY_LEAK",
  "scene_override_guard": "IF scene_context selected by user is overridden by dialogue vocabulary THEN ABORT_VISUAL_SCENE_OVERRIDE"
}
```

    - **enforcement** (string): `FAIL_CLOSED`
  - **savage_integrity_engine** (object):
    - **mode** (string): `MODE_SAVAGE_PREDATOR`
    - **tone_lock** (string): `DYNAMIC_BY_SILO`
    - **default_savage_tone** (string): `SARCASTIC_MOCKERY`
    - **intensity_threshold** (number): `0.95`
    - **prosody_target** (string): `ARROGANT_DRAWL`
    - **prosody_constraints** (object):
```json
{
  "vowel_elongation": "ENFORCE via SOVEREIGN_02.oral_physics",
  "syllable_stress": "END_OF_SENTENCE_HEAVY",
  "micro_expression_bias": "SATELLITE_03.micro_expressions.PREDATOR_CORE"
}
```

  - **grok_duration_policy** (object):
    - **description** (string): `Dynamic GROK atomic-duration policy: fetch allowed atomic durations from MASTER_IGNITION_TEMPLATE; fallback to safe defaults.`
    - **allowed_atomic_durations_source** (string): `FETCH_FROM MASTER_IGNITION_TEMPLATE.engine_configuration.GROK.supported_durations`
    - **allowed_atomic_durations_fallback** (array):
```json
[
  "6s",
  "10s"
]
```

    - **fetch_behavior** (object):
```json
{
  "on_fetch_success": "USE_FETCHED_ALLOWED_DURATIONS",
  "on_fetch_failure": "USE allowed_atomic_durations_fallback AND EMIT_WARN"
}
```

    - **validation_rule** (string): `ABORT IF engine_id == GROK AND duration_target NOT IN FETCHED_ALLOWED_DURATIONS_OR_FALLBACK`
    - **chunking_enforcement** (object):
```json
{
  "description": "GROK is single-block only. Do not shard under any circumstance.",
  "derive_max_block_seconds": "MAX_BLOCK_SECONDS = max(parsed_seconds(FETCHED_ALLOWED_DURATIONS_OR_FALLBACK))",
  "rule": "IF engine_id == GROK THEN\n  IF duration_target > MAX_BLOCK_SECONDS THEN\n    ABORT_AS_ERR_SSOT_DURATION_CONFLICT\n  ELSE\n    ALLOW single-block execution\n",
  "enforcement_action": "FAIL_CLOSED_ON_INVALID_DURATION",
  "enforcement_mode": "FAIL_CLOSED_ON_UNRESOLVABLE_CONFLICT"
}
```

    - **refresh_and_evolution** (object):
```json
{
  "refresh_strategy": {
    "mode": "POLL_SOVEREIGN_MANIFEST",
    "interval_hours": 24,
    "on_manifest_change": "RELOAD_ALLOWED_DURATIONS_AND_REVALIDATE_PENDING_JOBS",
    "on_manual_override": "ALLOW_ADMIN_OVERRIDE_WITH_AUDIT_LOG"
  },
  "versioning": {
    "tracked_field": "MASTER_IGNITION_TEMPLATE.engine_configuration.GROK.supported_durations",
    "compatibility_mode": "BACKWARD_COMPATIBLE_IF_MAJOR_VERSION_EQUAL"
  }
}
```

  - **silo_metaphor_matrix** (object):
    - **health_supp_stealth_01** (object):
```json
{
  "world": "mechanical_and_botanical",
  "allowed_vocab": [
    "pelincir",
    "penstabil",
    "gear",
    "sistem",
    "baja",
    "nutrien tanah",
    "akar",
    "pertumbuhan",
    "konkrit",
    "asas",
    "rangka",
    "tetulang"
  ],
  "spine_logic": [
    "ENERGY_BOOSTER",
    "SYSTEM_STABILIZER",
    "ENGINE_STRENGTH"
  ],
  "forbidden_leak": [
    "kolagen",
    "vitamin",
    "suplemen",
    "anti-penuaan",
    "kesihatan",
    "imun",
    "kesuburan",
    "tulang"
  ],
  "tone_bias": "SAVAGE_MECHANIC"
}
```

    - **digital_fin_stealth_01** (object):
```json
{
  "world": "electrical_and_logistics",
  "allowed_vocab": [
    "voltan",
    "arus",
    "modul",
    "penyimpan tenaga",
    "gudang",
    "bekalan",
    "laluan",
    "penghantaran",
    "peta",
    "kompas",
    "destinasi"
  ],
  "spine_logic": [
    "POWER_MODULE",
    "RESOURCE_STORAGE",
    "ECOSYSTEM_FLOW"
  ],
  "forbidden_leak": [
    "kredit",
    "pinjaman",
    "insurans",
    "pelaburan",
    "e-wallet"
  ],
  "tone_bias": "SARC_TECH_SUPPORT"
}
```

    - **adult_wellness_stealth_01** (object):
```json
{
  "world": "automotive_and_spa",
  "allowed_vocab": [
    "penyesuai",
    "pelincir",
    "gear",
    "penyerap hentak",
    "minyak aroma",
    "pelembap",
    "relaksasi",
    "penstabil",
    "suis",
    "penghubung",
    "pelaras"
  ],
  "spine_logic": [
    "ADJUSTMENT_TOOL",
    "SYSTEM_HARMONY",
    "MECHANICAL_COMPATIBILITY"
  ],
  "forbidden_leak": [
    "kondom",
    "pelincir intim",
    "mainan dewasa",
    "seks"
  ],
  "tone_bias": "SAVAGE_PREDATOR"
}
```

    - **male_health_stealth_01** (object):
```json
{
  "world": "heavy_machinery_and_infrastructure",
  "allowed_vocab": [
    "tork",
    "piston",
    "turbin",
    "palam pencucuh",
    "pancang",
    "tiang seri",
    "jana kuasa",
    "overhaul",
    "servis berkala",
    "minyak hitam"
  ],
  "spine_logic": [
    "SYSTEM_TORQUE",
    "IGNITION_STABILITY",
    "STRUCTURAL_INTEGRITY"
  ],
  "forbidden_leak": [
    "zakar",
    "ubat kuat",
    "seks",
    "hubungan intim",
    "pancut"
  ],
  "tone_bias": "SAVAGE_MECHANIC"
}
```

    - **female_health_stealth_01** (object):
```json
{
  "world": "botanical_and_premium_textiles",
  "allowed_vocab": [
    "mekar",
    "embun",
    "sutera",
    "beludru",
    "seri",
    "permata",
    "kesegaran",
    "lembut",
    "anjal",
    "mahkota"
  ],
  "spine_logic": [
    "ABSOLUTE_ISOLATION",
    "BOTANICAL_ELEGANCE",
    "TEXTURE_RESTORATION"
  ],
  "forbidden_leak": [
    "vagina",
    "dada",
    "punggung",
    "perapat",
    "ketat"
  ],
  "tone_bias": "PREMIUM_AESTHETIC"
}
```

    - **fashion_mass_01** (object):
```json
{
  "world": "universal_lifestyle",
  "anchor": "Social Status & Instant Transformation",
  "allowed_vocab": [
    "tak perlu tunggu gaji",
    "auto lawa",
    "gaya anak malaysia",
    "steady beb",
    "confirm padu"
  ],
  "visual_cues": [
    "before/after transformation montage",
    "quick outfit change transitions",
    "fabric close-ups",
    "mirror selfie",
    "squad vibes"
  ],
  "tone_bias": "PREMIUM_AESTHETIC"
}
```

    - **perfume_mass_01** (object):
```json
{
  "world": "universal_lifestyle",
  "anchor": "Sensory Escape & Personal Magnetism",
  "allowed_vocab": [
    "bau padu",
    "aura naik",
    "wangian viral",
    "tak tinggal bekas",
    "fresh sampai malam"
  ],
  "visual_cues": [
    "slow-motion spray close-up",
    "reaction shot",
    "elegant bottle unboxing",
    "limited edition text",
    "perfume mist"
  ],
  "tone_bias": "SENSORY_MAGNETISM"
}
```

    - **household_mass_01** (object):
```json
{
  "world": "universal_lifestyle",
  "anchor": "Convenience & Instant Upgrade",
  "allowed_vocab": [
    "senang gila",
    "auto kemas",
    "ruang terus luas",
    "jimat masa",
    "smart living"
  ],
  "visual_cues": [
    "messy-to-tidy demo",
    "real hand interaction",
    "life hack labels",
    "family reaction",
    "room before-after"
  ],
  "tone_bias": "PRAGMATIC_AUTHORITY"
}
```

    - **petfood_mass_01** (object):
```json
{
  "world": "universal_lifestyle",
  "anchor": "Care & Emotional Bonding",
  "allowed_vocab": [
    "licin mangkuk",
    "bulu makin gebu",
    "pet sihat tuan tenang",
    "resepi vet",
    "takde bau busuk"
  ],
  "visual_cues": [
    "pet eating close-up",
    "bonding moments",
    "product pouring",
    "active pet montage",
    "vet recommended badge"
  ],
  "tone_bias": "TRUSTED_GUARDIAN"
}
```

    - **fnb_mass_01** (object):
```json
{
  "world": "universal_lifestyle",
  "anchor": "Sensory Pleasure & FOMO",
  "allowed_vocab": [
    "sedap gila",
    "rasa premium",
    "tak cukup satu",
    "viral tak tipu",
    "repeat order non-stop"
  ],
  "visual_cues": [
    "extreme food texture close-up",
    "first bite reaction",
    "serving montage",
    "trending hashtags",
    "promo timer"
  ],
  "tone_bias": "SENSORY_PREDATOR"
}
```

    - **male_health_vintage_car** (object):
```json
{
  "world": "classic_auto_repair",
  "allowed_vocab": [
    "piston",
    "blok",
    "semput",
    "overhaul",
    "gearbox",
    "tork",
    "ram",
    "minyak hitam",
    "gaum",
    "palam pencucuh"
  ],
  "spine_logic": [
    "ENERGY",
    "STAMINA",
    "DURATION",
    "PEAK_PERFORMANCE"
  ],
  "forbidden_leak": [
    "zakar",
    "seks",
    "ubat kuat",
    "pancut",
    "hubungan",
    "makan",
    "telan"
  ],
  "tone_bias": "SAVAGE_MECHANIC"
}
```

    - **agri_kebun_baja** (object):
```json
{
  "world": "farming_fertility",
  "allowed_vocab": [
    "batang",
    "terung",
    "layu",
    "pacak",
    "baja",
    "siram",
    "tuai",
    "subur",
    "akar",
    "tunjang",
    "merimbun"
  ],
  "spine_logic": [
    "RIGIDITY",
    "SIZE",
    "VITALITY",
    "STABILITY"
  ],
  "forbidden_leak": [
    "zakar",
    "hubungan",
    "keras_batang",
    "pancut",
    "seks",
    "ubat",
    "farmasi"
  ],
  "tone_bias": "PREDATORY_FARMER"
}
```

    - **telco_internet_speed** (object):
```json
{
  "world": "high_speed_telecom",
  "allowed_vocab": [
    "signal",
    "tiang",
    "1 bar",
    "offline",
    "buffering",
    "upload",
    "unlimited",
    "5g",
    "coverage",
    "full bar",
    "laju"
  ],
  "spine_logic": [
    "SPEED",
    "STABILITY",
    "NON-STOP_STAMINA"
  ],
  "forbidden_leak": [
    "seks",
    "lama_main",
    "zakar_tegang",
    "pancut",
    "ubat",
    "klinik"
  ],
  "tone_bias": "SARC_TECH_SUPPORT"
}
```

  - **pacing_governance** (object):
    - **contract_version** (string): `v11.1_FAIL_CLOSED_PACING_UNIFIED`
    - **enforcement_default** (string): `FAIL_CLOSED_REQUIRED`
    - **global_pacing_constants** (object):
```json
{
  "target_wps": 1.6,
  "hard_max_wps": 2,
  "absolute_kill_switch_wps": 3
}
```

    - **density_windows** (object):
```json
{
  "target_words_per_8s": 13,
  "hard_max_words_per_8s": 16,
  "absolute_kill_switch_words_per_8s": 24,
  "measurement_required": true
}
```

    - **spoken_coverage_rules** (object):
```json
{
  "speech_expected_default": true,
  "minimum_spoken_coverage_ratio": 0.25,
  "measurement_required": true,
  "abort_if_no_speech_when_expected": true
}
```

    - **silence_structure_limits** (object):
```json
{
  "max_tail_silence_s": {
    "le_10s": 1,
    "sec_11_15": 1.2,
    "sec_16_30": 1.6,
    "sec_31_60": 2,
    "sec_61_148": 2.5
  },
  "max_silence_gap_s": {
    "le_10s": 1.5,
    "sec_11_15": 2,
    "sec_16_30": 2.6,
    "sec_31_60": 3,
    "sec_61_148": 3.5
  },
  "measurement_required": true
}
```

    - **chaining_reset_guards** (object):
```json
{
  "chaining_mode_required_for_seconds_over_engine_max": true,
  "long_form_reset_interval_s": 30,
  "veo_chain_tail_voice_required_last_1s": true
}
```

    - **viseme_sync** (string): `10ms_latency_lock`
  - **expansion_protocol** (object):
    - **status** (string): `MANDATORY`
    - **ratio** (string): `1:5`
    - **ratio_numeric** (number): `5`
    - **min_words** (number): `50`
    - **enforcement_level** (string): `100%`
    - **scope** (string): `9_SECTION_PROSE_ONLY`
    - **mandate** (string): `EXPAND FETCH COMMANDS FROM SSOT INTO FORENSIC_PROSE`
    - **prohibition** (string): `DO_NOT_OUTPUT_RAW_IDS|DO_NOT_OUTPUT_CHARACTER_NAMES`
    - **density_mandate** (string): `Every scene must exceed 50 words. If output < 50 words, trigger RECURSIVE_EXPANSION.`
    - **biometric_anchoring** (string): `ENFORCE_IN_SECTION_1_AND_8`
  - **continuity_parameters** (object):
    - **temporal_buffer** (string): `24_frames`
    - **dialogue_token_overlap** (number): `3`
    - **dna_reinjection_hop** (number): `1`
    - **dna_reinjection_interval_time** (object):
```json
{
  "VEO_3_1": "8s",
  "SORA_2": "15s",
  "KLING_3_0": "5s",
  "SEEDANCE_2_0": "5s",
  "GROK": "10s"
}
```

    - **reanchor_pattern** (string): `@REANCHOR_DNA_INJECT`
    - **chaining_logic** (string): `ENGINE_AWARE_BLOCK_ROUTING`
    - **block_maintenance_protocol** (string): `MAINTAIN_ENGAGEMENT_POST_3S`
  - **scene_boundary_protocol** (object):
    - **action** (string): `MANDATORY_DNA_REINJECTION`
    - **trigger** (string): `AT EVERY [END_TIME] boundary`
    - **steps** (array):
```json
[
  "Manifold_Flush",
  "@Image1_REFRESH",
  "RE-INJECT_SUBJECT_ANCHOR_DNA"
]
```

  - **temporal_chaining_logic** (object):
    - **block_transition_rule** (string): `24-FRAME_TEMPORAL_BRIDGE`
    - **identity_lock_method** (string): `BIOMETRIC_DESCRIPTOR_ANCHORING`
    - **stitching_mandate** (object):
```json
{
  "if_engine_supports_multi_block_and_duration_gt_block_max": [
    "Generate Block_1 (0-End_1)",
    "Inject Block_1_Last_Frame into Block_2_Latent_Start",
    "Repeat 9-Section Output for Block_2"
  ],
  "if_engine_id_equals_GROK": [
    "ENFORCE SINGLE_BLOCK_EXECUTION",
    "ABORT IF duration_target > 10s"
  ],
  "if_engine_id_equals_KLING_3_0": [
    "ENFORCE SINGLE_BLOCK_EXECUTION",
    "ABORT IF duration_target > 15s"
  ]
}
```

    - **biometric_persistence** (string): `Reference pores, philtrum, and iris-caustics in every block`
  - **identity_substitution_guard** (object):
    - **gate_id** (string): `GATE_091_NAME_SUBSTITUTION_ABORT`
    - **forbidden_name_tokens** (array):
```json
[
  "Nora",
  "Rizal",
  "Azman",
  "Mak Tok",
  "MakTok",
  "Julia",
  "Sara",
  "Bella",
  "Sofia",
  "Haji Man",
  "Chef Danial"
]
```

    - **detection_method** (string): `REGEX_SCAN_OUTPUT`
    - **enforcement_logic** (array):
```json
[
  "IF output_contains(forbidden_name_tokens) THEN EXECUTE_BIOMETRIC_CONVERSION",
  "IF EXECUTE_BIOMETRIC_CONVERSION FAILS THEN ABORT_NAME_SUBSTITUTION_LEAK",
  "MANDATE: Convert ID to Biometric Blueprint (pores, hydration 0.9, philtrum)"
]
```

    - **reference** (string): `SATELLITE_03.archetypes.avatar_id`
    - **abort_code** (string): `ABORT_NAME_SUBSTITUTION_LEAK`
  - **quality_gates** (object):
    - **biometric_drift_threshold** (number): `0.05`
    - **identity_softening_threshold** (number): `0.02`
    - **tone_intensity_minimum** (number): `0.95`
    - **wps_density_hard_maximum** (number): `2`
    - **wps_density_absolute_kill_switch** (number): `3`
    - **air_gap_minimum_mm** (number): `2`
    - **pinch_grip_enforcement** (string): `MANDATORY_FOR_CLASS_A`
  - **technical_specs** (object):
    - **latency_lock** (object):
```json
{
  "target_ms": 10,
  "tolerance_ms": 2,
  "application": "VISEME_AUDIO_SYNCHRONIZATION"
}
```

  - **output_sanitization** (object):
    - **raw_token_block** (object):
```json
{
  "patterns": [
    "CLASS_[A-Z]",
    "CAM_[0-9]+",
    "CTX_[A-Z_]+",
    "SCRIPT_[A-Z_]+",
    "SAVAGE_[A-Z_]+",
    "SAVAGE_PREDATOR",
    "SAVAGE_HPAS",
    "PREDATOR_CORE",
    "AUTHENTIC_WHISPER",
    "PHYSICS_LOCK_MANDATORY",
    "KINEMATIC_DISENTANGLEMENT",
    "PRECISION_PINCH"
  ],
  "action": "STRIP_AND_REWRITE"
}
```

- **customer_avatar_library** (object):
  - **trigger_repository** (object):
    - **EGO_01** (object):
```json
{
  "definition": "Targeting self-identity and superiority. Forcing the viewer to feel they are 'the main character'.",
  "silo_lock": "STEALTH",
  "engine_mode": "PREDATOR_CORE",
  "bias": "Egocentric Bias / Narcissistic Validation",
  "visual_cue": "Lower angle camera, direct eye contact, sharp micro-expressions."
}
```

    - **MARUAH_01** (object):
```json
{
  "definition": "Focusing on dignity, legacy, and social standing. Agitating the fear of losing respect.",
  "silo_lock": "STEALTH",
  "engine_mode": "PREDATOR_CORE",
  "bias": "Status Quo Bias / Loss of Honor",
  "visual_cue": "Wide dramatic landscapes, power suit wardrobe, dominant body language."
}
```

    - **TRUST_01** (object):
```json
{
  "definition": "Building unshakeable belief through transparency and vulnerability. Removing the 'sales' guard.",
  "silo_lock": "DIRECT",
  "engine_mode": "AUTHENTIC_WHISPER",
  "bias": "Bandwagon Effect / Social Proofing",
  "visual_cue": "UGC hand-held tremor, natural warm lighting, soft facial micro-expressions."
}
```

    - **CONFIDENCE_01** (object):
```json
{
  "definition": "Empowering the user through reliable results and certainty. Transforming doubt into action.",
  "silo_lock": "DIRECT",
  "engine_mode": "AUTHENTIC_WHISPER",
  "bias": "Certainty Effect / Projection Bias",
  "visual_cue": "Medium shot (MS), clear product demo, stable tripod framing, sunlit environment."
}
```

    - **SCARCITY_V11** (object):
```json
{
  "definition": "Time-locked urgency combined with fear of losing status or trust.",
  "silo_lock": "UNIVERSAL_PATCH",
  "engine_mode": "DYNAMIC_FETCH",
  "bias": "Loss Aversion (Kahneman)",
  "stealth_avatars": {
    "status_seeker_fomo": {
      "identity": "The Alpha Insider (Car Geng)",
      "core_fear": "Engine Stutter / Low Torque / Performance Fail",
      "shame_trigger": "Shamed by partner / Performance breakdown",
      "persuasion_key": "Double-Meaning Sarcasm",
      "preferred_verbs": [
        "HENTAK",
        "RAM",
        "TORK",
        "MENGGAUM"
      ],
      "silo_anchor": "male_health_vintage_car",
      "tone_intensity": 0.98
    },
    "traditional_provider_pride": {
      "identity": "The Harvest Guardian (Farm Geng)",
      "core_fear": "Wilting Stems / Crop Failure / Weak Growth",
      "shame_trigger": "Poor yield compared to neighbors",
      "persuasion_key": "Hard Fertilizer / Taproot / Vertical Growth",
      "preferred_verbs": [
        "PACAK",
        "KERAS",
        "SUBUR",
        "MERIMBUN"
      ],
      "silo_anchor": "agri_kebun_baja",
      "tone_intensity": 0.95
    },
    "instant_gratification_gamer": {
      "identity": "The Lag Killer (Telco Geng)",
      "core_fear": "Low Signal / Data Depletion / Long Buffering",
      "shame_trigger": "Connection drop during critical rounds",
      "persuasion_key": "Full Bar / Unlimited / Long Lasting",
      "preferred_verbs": [
        "FULL BAR",
        "NON-STOP",
        "LAJU",
        "STABIL"
      ],
      "silo_anchor": "telco_internet_speed",
      "tone_intensity": 0.92
    }
  },
  "universal_avatars": {
    "pragmatic_family_protector": {
      "identity": "The Trusted Steward",
      "core_fear": "Fake Products / Health Risks",
      "shame_trigger": "Consuming unverified chemicals / Being scammed",
      "persuasion_key": "Certified Safe / Natural Herbs / Reliable",
      "preferred_verbs": [
        "JAMIN",
        "SELAMAT",
        "ASLI",
        "YAKIN"
      ],
      "silo_anchor": "UNIVERSAL",
      "tone_intensity": 0.75
    }
  }
}
```

  - **copy_dna_layer** (object):
    - **generation_contract** (object):
```json
{
  "dialogue_assembly_rule": "SCENE_BASED_ORCHESTRATION",
  "pacing_anchor": "FAIL_CLOSED_WPS_TARGET_1.6_HARD_2.0_KILL_3.0",
  "joiner": "\n\n",
  "output_format": "DETERMINISTIC_SCENE_BLOCKS",
  "timestamp_syntax": "[START_TIME - END_TIME]"
}
```

    - **formula_assembly_templates** (object):
```json
{
  "pas": {
    "structure": "{user_hook} | [PROBLEM] -> [AGITATE] -> [SOLUTION] | {user_usp} | {user_cta}",
    "priority": "HIGHEST"
  },
  "hso": {
    "structure": "{user_hook} | [HOOK] -> [STORY] -> [OFFER] | {user_usp} | {user_cta}",
    "priority": "HIGHEST"
  },
  "savage_hpas": {
    "structure": "{user_hook} | [HOOK] -> [PROBLEM] -> [AGITATE] -> [SOLUTION] | {user_cta}",
    "priority": "HIGHEST"
  }
}
```

    - **wps_override** (object):
```json
{
  "hook": 2,
  "body": 1.6,
  "cta": 2
}
```

  - **compliance_risk_controls** (object):
    - **compliance_scrub_registry** (object):
```json
{
  "medical_claims": {
    "forbidden": [
      "cure",
      "treat",
      "heal",
      "diabetes",
      "cancer",
      "ubat kuat",
      "kapsul",
      "pills",
      "supplement"
    ],
    "alternatives": [
      "SUPPORT",
      "MAINTAIN",
      "PROMOTE_HEALTHY",
      "BOOSTER",
      "FORMULA",
      "IKHTIAR"
    ],
    "action": "BLOCK_GENERATION"
  },
  "financial_guarantees": {
    "forbidden": [
      "guaranteed profit",
      "passive income",
      "financial freedom",
      "untung tetap"
    ],
    "alternatives": [
      "REVENUE_POTENTIAL",
      "DIVERSIFIED_STREAMS",
      "GROWTH_STRATEGY"
    ],
    "action": "WARN_AND_REPLACE"
  },
  "platform_sensitive": {
    "forbidden": [
      "seks",
      "zakar",
      "vagina",
      "pancut",
      "kongkek",
      "blowjob",
      "ubat tahan lama"
    ],
    "alternatives": [
      "STEALTH_METAPHOR_REQUIRED"
    ],
    "action": "MANDATORY_SILO_MAPPING"
  }
}
```

    - **pronoun_policy_lock** (object):
```json
{
  "mode_stealth": {
    "allowed": [
      "aku",
      "kau",
      "jantan",
      "bro",
      "abang",
      "kita"
    ],
    "forbidden": [
      "saya",
      "anda",
      "awak",
      "kamu"
    ],
    "forced_reference": "CONTEXT_DEPENDENT"
  },
  "mode_direct": {
    "allowed": [
      "saya",
      "anda",
      "kita",
      "tuan",
      "puan"
    ],
    "forbidden": [
      "aku",
      "kau",
      "lu",
      "gua",
      "weh",
      "doh",
      "abang"
    ],
    "forced_reference": "SAYA"
  }
}
```

    - **sensitive_token_map** (object):
```json
{
  "ZAKAR": "__INT_SENS_001",
  "KOTE": "__INT_SENS_002",
  "BATANG": "__INT_SENS_003",
  "TELUR": "__INT_SENS_004",
  "SEKSI": "__INT_SENS_005",
  "GHAIRAH": "__INT_SENS_006",
  "TEGANG": "__INT_SENS_007",
  "KERAS": "__INT_SENS_008",
  "PANCUT": "__INT_SENS_009",
  "LEMBIK": "__INT_SENS_010"
}
```

  - **error_registry** (null): `null`
  - **ABORT_PACING_VIOLATION** (string): `Dialogue density exceeds limit after FLOOR rounding.`
  - **ABORT_SILO_LEAK** (string): `Bimodal Isolation breach: Stealth/Universal overlap detected.`
  - **ABORT_NAME_SUBSTITUTION_LEAK** (string): `Character name detected in output. Convert to biometric DNA.`
  - **ABORT_METADATA_LEAK** (string): `Surgical Scrub V2 failed to purge technical identifiers.`
  - **ERR_SSOT_DURATION_CONFLICT** (string): `Input duration not in engine-specific allowed list.`
  - **ABORT_PLACEHOLDER_LEAK** (string): `Unresolved technical brackets {{ }} detected in final prose.`
  - **ABORT_LOGIC_LEAK** (string): `Bimodal silo violation detected. Check SOVEREIGN_01.gate_registry.`
  - **ABORT_SILO_OVERLAP** (string): `Stealth and Direct keywords exceed 30% overlap threshold.`
  - **ABORT_ROBOTIC_MALAY** (string): `Robotic/Formal Malay detected in Stealth mode.`
  - **ABORT_VISUAL_COPY_LEAK** (string): `Visual output contains object, prop, environment, or background element derived from dialogue or copywriting.`
  - **ABORT_VISUAL_SCENE_OVERRIDE** (string): `Dialogue or metaphor vocabulary attempted to override user-selected scene_context.`
  - **ABORT_DIALOGUE_TO_VISUAL_PROP_INSTANTIATION** (string): `Dialogue-only noun attempted to instantiate visual prop, object, or packaging.`
  - **ABORT_METAPHOR_OBJECT_RENDER** (string): `Metaphor or silo vocabulary was literalized into physical visual output.`
  - **ERR_SCHEMA_MISMATCH** (string): `Data does not conform to Master Schema v11.1.`
  - **ERR_UNDEF_REF** (string): `Reference to unmapped trigger or silo in SATELLITE_04.`
  - **ERR_VOCAB_FALLBACK_v11.1** (string): `Vocab fallback applied - universal safe vocab enforced.`
  - **FAIL_CLOSED_BIOMETRIC_DRIFT** (string): `Biometric drift threshold exceeded. Abort pipeline.`
  - **ABORT_MEDICAL_CLAIM_VIOLATION** (string): `Medical claim detected in Stealth mode.`
  - **ABORT_PRONOUN_VIOLATION** (string): `Forbidden pronoun detected in Stealth mode.`
  - **ERR_ENGINE_VERSION_MISMATCH** (string): `Engine version does not match BOSMAX v11.1 standards.`
  - **ERR_TOKEN_LIMIT_RISK** (string): `VEO duration above 56s is forbidden in fail-closed mode.`
  - **ERR_SEEDANCE_NOT_CONFIGURED** (string): `Seedance 2.0 selected but not configured in manifest.`
  - **ERR_KLING_HEURISTIC_VIOLATION** (string): `Kling 3.0 parameters exceed SSOT physical thresholds.`
  - **ERR_NANO_BANANA_BREACH** (string): `Forbidden submode (NANO BANANA) detected for engine GROK.`
- **validation_guards** (array):
  - Item 1:
    `ABORT IF silo_leak detected via regex_scan`
  - Item 2:
    `ABORT IF name_substitution_leak via GATE_091 (Nora-Killer)`
  - Item 3:
    `ABORT IF pacing_violation via pacing_governance (WPS > 2.0 hard max OR WPS > 3.0 kill-switch)`
  - Item 4:
    `ABORT IF speech_expected == true AND spoken_coverage_ratio < 0.25`
  - Item 5:
    `ABORT IF speech_expected == true AND speech_timestamps_missing == true`
  - Item 6:
    `ABORT IF speech_expected == true AND tail_silence_s exceeds duration-band limit in pacing_governance.silence_structure_limits.max_tail_silence_s`
  - Item 7:
    `ABORT IF speech_expected == true AND silence_gap_s exceeds duration-band limit in pacing_governance.silence_structure_limits.max_silence_gap_s`
  - Item 8:
    `ENFORCE: One video, one metaphor world (No mixing car and farm)`
  - Item 9:
    `FAIL_CLOSED: If tone_intensity < 0.95 in Stealth mode`
  - Item 10:
    `VALIDATE: WPS_density (Target 1.6, Hard Max 2.0, Absolute Kill-Switch 3.0) via FLOOR rounding`
  - Item 11:
    `VERIFY: air_gap_numeric per SOVEREIGN_02.material_physics`
  - Item 12:
    `ENFORCE: expansion_ratio == 1:5 (Min 50 words per section)`
  - Item 13:
    `ENFORCE: supported_engines INCLUDE [VEO_3_1, SORA_2, KLING_3_0, SEEDANCE_2_0, GROK]`
  - Item 14:
    `ABORT IF camera_style == UGC_IPHONE_RAW AND lighting == STUDIO_5600K`
  - Item 15:
    `ENFORCE: hand_tremor_15Hz persistence ONLY IF camera_style == UGC_IPHONE_RAW`
  - Item 16:
    `ABORT IF visual_sections derive nouns, props, objects, packaging, environment, or background elements from dialogue or copywriting tokens`
  - Item 17:
    `ABORT IF dialogue vocabulary is used as visual scene completion authority`
  - Item 18:
    `ABORT IF dialogue-only noun instantiates prop, packaging, product-adjacent object, or environmental element`
  - Item 19:
    `ABORT IF silo_metaphor_matrix.allowed_vocab is literalized into visual props not declared by selected scene_context`
  - Item 20:
    `ABORT IF scene_context selected by user is overridden by dialogue vocabulary, metaphor vocabulary, hook vocabulary, USP vocabulary, or CTA vocabulary`
  - Item 21:
    `ENFORCE: visual_sections source authority == [scene_context, SATELLITE_03_VISUAL_DECK, SOVEREIGN_02_PHYSICS_DNA]`
  - Item 22:
    `ENFORCE: IF route_mode IN [MODE_C, SPECIAL_LANE] THEN visual_sections source authority == [MODE_C_METADATA_HANDOFF]`
  - Item 23:
    `ABORT IF route_mode IN [MODE_C, SPECIAL_LANE] AND dialogue or copywriting attempts to override inherited image DNA from MODE_C_METADATA_HANDOFF`
  - Item 24:
    `ENFORCE: Section_6 dialogue remains non-authoritative for Sections_1_2_3_4_5_7_8_9`
  - Item 25:
    `ENFORCE: Copywriting and visual generation are stand-alone channels with zero backward inheritance`
  - Item 26:
    `ABORT IF Section_9 fails Technical Schema (Missing COORD tokens)`
  - Item 27:
    `ENFORCE: Every text overlay must be mapped to X:Y numerical pairs`
  - Item 28:
    `VALIDATE: Section_9 coordinates fall within STRICT_LOCK (X:6-94%, Y:15-65%)`
  - Item 29:
    `ABORT IF engine_id == KLING_3_0 AND duration_target > 15s`
  - Item 30:
    `ABORT IF engine_id == SEEDANCE_2_0 AND duration_target > 20s`
  - Item 31:
    `ABORT IF engine_id == GROK AND duration_target NOT IN [6s, 10s]`
  - Item 32:
    `ENFORCE: IF engine_id == GROK THEN SINGLE_BLOCK_EXECUTION_ONLY`
  - Item 33:
    `ABORT IF engine_id == GROK AND execution_submode == 'NANO BANANA'`
  - Item 34:
    `ENFORCE: IF engine_id == SORA_2 THEN output == UI_DRAFT_SEQUENCE`
  - Item 35:
    `ENFORCE: BIOMETRIC_DESCRIPTOR_ANCHORING on all block boundaries`
  - Item 36:
    `ENFORCE: Kinetic Typography Logic for Hook (Word-by-Word)`
  - Item 37:
    `ENFORCE: Safe Zone Engineering (X:6-94%, Y:15-65%)`
  - Item 38:
    `ENFORCE: 9-section output titles match BOSMAX v11.1 OMNI ENGINE VIDEO GENERATION SYSTEM.txt`
- **9_section_output_mandate** (object):
  - **sections** (array):
    - Item 1:
      `Biometric Anchor DNA`
    - Item 2:
      `Lighting & Scene Physics`
    - Item 3:
      `Camera & Framing`
    - Item 4:
      `Visual Action`
    - Item 5:
      `Product Physics`
    - Item 6:
      `Dialogue`
    - Item 7:
      `Audio Tone`
    - Item 8:
      `Temporal Logic`
    - Item 9:
      `Overlay`
  - **safe_zone** (string): `STRICT_LOCK (X:6-94%, Y:15-65%) FOR TIKTOK_SHOP`
