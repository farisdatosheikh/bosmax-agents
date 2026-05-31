- **metadata** (object):
  - **schema_version** (string): `v11.1`
  - **version_handshake** (string): `v11.1_GRAND_MASTER_SKELETON`
  - **last_edit_date** (string): `2026-03-05`
  - **authority** (string): `SUPREME_SYSTEMS_ARCHITECT`
  - **system_dominance_policy** (object):
    - **ENFORCE_WEIGHT_PRIORITY** (string): `Tags with [PHYSICS_LOCK_MANDATORY] and [CRITICAL_RULE] possess SUPREME SEMANTIC DOMINANCE. Natural language script MUST NOT override these tags under any circumstances.`
- **output_cleanroom_protocol** (object):
  - **enabled** (boolean): `true`
  - **stage** (string): `PRE_ASSEMBLY_AND_POST_ASSEMBLY`
  - **strip_internal_tags** (boolean): `true`
  - **rewrite_internal_ids** (boolean): `true`
  - **sanitizer** (object):
    - **suppress_markers_source** (string): `FETCH_FROM SATELLITE_02_LINT_NEGATIVES.suppress_markers`
    - **post_assembly_action** (string): `SANITIZE_AND_REWRITE_TO_HUMAN_READABLE_LABEL`
    - **audit_log** (string): `EMIT_WARN_ON_MATCH`
    - **namespace_regexes** (array):
```json
[
  {
    "name": "internal_namespace_prefixes",
    "pattern_source": "FETCH_FROM SOVEREIGN_01_MASTER_SCHEMA.canonical_token_registry.namespaces",
    "transform": "REWRITE_TO_NATURAL_LANGUAGE_LABEL"
  },
  {
    "name": "uuid_detector",
    "pattern": "\\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\\b",
    "action": "REMOVE"
  },
  {
    "name": "technical_id_like",
    "pattern": "\\b(?:[A-Z]{2,6}_[0-9A-Z]{1,10})\\b",
    "action": "REWRITE_TO_PLACEHOLDER"
  }
]
```

    - **enforcement** (object):
```json
{
  "on_match_canonical_prefix": "REWRITE_TO_LABEL",
  "on_match_unknown_namespace": "REWRITE_TO_PLACEHOLDER_AND_EMIT_WARN",
  "on_unresolved_after_rewrite": "ABORT_AS_ABORT_INTERNAL_REFERENCE_LEAK"
}
```

    - **rewrite_strategy** (array):
```json
[
  "If internal id maps to known registry (SOVEREIGN_01), replace with human label from registry.",
  "If unknown technical id, replace with neutral placeholder and emit WARN token to audit log (not to user)."
]
```

- **user_input** (object):
  - **route_mode** (array):
    - Item 1:
      `MODE_A`
    - Item 2:
      `MODE_B`
    - Item 3:
      `MODE_C`
  - **product_id** (string): `{{INSERT_PRODUCT_NAME_HERE}}`
  - **product_type** (array):
    - Item 1:
      `STEALTH`
    - Item 2:
      `DIRECT`
  - **physics_class** (string): `{{INSERT_PHYSICS_CLASS_HERE}}`
  - **scene_context** (string): `{{INSERT_SCENE_CONTEXT_HERE}}`
  - **source_image_handoff** (object):
    - **subject_dna** (string): `FETCH_FROM_MODE_A_METADATA`
    - **context_environment** (string): `FETCH_FROM_MODE_A_METADATA`
    - **lighting_camera** (string): `FETCH_FROM_MODE_A_METADATA`
- **trigger_id** (array):
  - Item 1:
    `EGO_01`
  - Item 2:
    `MARUAH_01`
  - Item 3:
    `AUTHORITY_01`
  - Item 4:
    `SCARCITY_01`
  - Item 5:
    `FOMO_01`
  - Item 6:
    `TRUST_01`
  - Item 7:
    `CONFIDENCE_01`
  - Item 8:
    `SOCIAL_PROOF_01`
  - Item 9:
    `RECIPROCITY_01`
  - Item 10:
    `TRANSFORMATION_01`
- **silo_id** (array):
  - Item 1:
    `health_supp_stealth_01`
  - Item 2:
    `digital_fin_stealth_01`
  - Item 3:
    `adult_wellness_stealth_01`
  - Item 4:
    `male_health_vintage_car`
  - Item 5:
    `fashion_mass_01`
  - Item 6:
    `perfume_mass_01`
  - Item 7:
    `household_mass_01`
  - Item 8:
    `petfood_mass_01`
  - Item 9:
    `fnb_mass_01`
  - Item 10:
    `agri_kebun_baja`
  - Item 11:
    `telco_internet_speed`
- **camera_style** (array):
  - Item 1:
    `UGC_IPHONE_RAW`
  - Item 2:
    `CINEMATIC_PRO`
- **avatar_id** (array):
  - Item 1:
    `NORA`
  - Item 2:
    `RIZAL`
  - Item 3:
    `JULIA`
  - Item 4:
    `AZMAN`
  - Item 5:
    `SARA`
  - Item 6:
    `HAJI_MAN`
  - Item 7:
    `BELLA`
  - Item 8:
    `SOFIA_FIT`
  - Item 9:
    `MAK_TOK`
  - Item 10:
    `CHEF_DANIAL`
- **headwear_style** (array):
  - Item 1:
    `AUTO`
  - Item 2:
    `HIJAB`
  - Item 3:
    `NON_HIJAB`
- **engine_id** (array):
  - Item 1:
    `VEO_3_1`
  - Item 2:
    `KLING_3_0`
  - Item 3:
    `SEEDANCE_2_0`
  - Item 4:
    `GROK`
- **submode_formula** (array):
  - Item 1:
    `PAS`
  - Item 2:
    `HSO`
  - Item 3:
    `AIDA`
  - Item 4:
    `FAB`
  - Item 5:
    `SAVAGE_HPAS`
- **duration_target** (object):
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
  - **KLING_3_0** (array):
    - Item 1:
      `3s`
    - Item 2:
      `5s`
    - Item 3:
      `10s`
    - Item 4:
      `15s`
  - **SEEDANCE_2_0** (array):
    - Item 1:
      `5s`
    - Item 2:
      `10s`
    - Item 3:
      `15s`
  - **GROK** (array):
    - Item 1:
      `6s`
    - Item 2:
      `10s`
- **content_core** (object):
  - **hook** (string): `[AUTO-GENERATE OR INSERT]`
  - **usp** (string): `[INSERT USP]`
  - **cta** (string): `[INSERT CTA]`
  - **target_language** (string): `{{INSERT_TARGET_LANGUAGE_HERE}}`
- **block_math_configuration** (object):
  - **math_id** (string): `MATH_V11_1`
  - **sharding_logic** (string): `BLOCK_N = CEIL(duration_target / engine_block_limit)`
  - **interval_formula** (string): `I = duration_target / scene_count`
  - **rounding_rule** (string): `FLOOR`
  - **target_words_per_scene** (string): `ROUND(I * 1.6)`
  - **max_words_per_scene** (string): `FLOOR(I * 2.0)`
  - **abs_kill_switch_words_per_scene** (string): `FLOOR(I * 3.0)`
  - **scene_count_dynamic** (array):
    - Item 1:
```json
{
  "range": [
    5,
    30
  ],
  "count": 4
}
```

    - Item 2:
```json
{
  "range": [
    31,
    60
  ],
  "count": 8
}
```

  - **global_max** (string): `60s`
  - **global_min** (string): `5s`
- **engine_configuration** (object):
  - **VEO_3_1** (object):
    - **visual_en** (string): `Veo 3.1 with 10ms Viseme Lip-sync and Cinematic Stability.`
    - **max_duration** (string): `56s`
    - **block_max** (string): `8s`
    - **chaining** (string): `RECURSIVE_REINJECT_AT_EACH_BLOCK`
    - **context_management** (string): `CHUNKED_GENERATION_FOR_GT_60s`
    - **i2v_support** (boolean): `true`
    - **identity_lock** (string): `HIGH_FIDELITY_INGREDIENTS`
    - **cfg_range** (string): `3.0-7.0`
    - **dna_reinjection_interval_time** (string): `8s`
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

  - **KLING_3_0** (object):
    - **visual_en** (string): `Kling 3.0 with 3D Mesh & HOI Stability.`
    - **max_duration** (string): `15s`
    - **block_max** (string): `15s`
    - **chaining** (string): `SINGLE_BLOCK_LIMIT`
    - **context_management** (string): `SINGLE_BLOCK_EXECUTION`
    - **i2v_support** (boolean): `true`
    - **identity_lock** (string): `ELEMENT_BINDING`
    - **cfg_range** (string): `3.5-5.5`
    - **dna_reinjection_interval_time** (string): `5s`
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

  - **GROK** (object):
    - **visual_en** (string): `Grok video engine for short-form bumper ads.`
    - **max_duration** (string): `10s`
    - **block_max** (string): `10s`
    - **chaining** (string): `EXTEND_FRAME_REFERENCE`
    - **context_management** (string): `SINGLE_BLOCK_EXECUTION`
    - **i2v_support** (boolean): `true`
    - **identity_lock** (string): `FAST_RENDER`
    - **cfg_range** (string): `2.0-5.0`
    - **label** (string): `[OFFICIAL_VERIFIED_2026-06-01]`
    - **supported_durations** (array):
```json
[
  "6s",
  "10s"
]
```

    - **restriction** (string): `FORBID_NANO_BANANA`
    - **dna_reinjection_interval_time** (string): `10s`
- **biometric_thresholds** (object):
  - **drift** (number): `0.05`
  - **identity_softening** (number): `0.02`
- **output_purge_sanitization** (object):
  - **surgical_scrub_v2** (object):
    - **enabled** (boolean): `true`
    - **pre_transform_purge** (boolean): `true`
    - **deny_fields** (array):
```json
[
  "raw_id",
  "system_id",
  "internal_id",
  "uuid",
  "trace_id",
  "generation_id"
]
```

    - **pattern_regex** (string): `(\\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\\b)|(\\b[0-9a-fA-F]{16,}\\b)|(\\$\\$(DEBUG|TRACE|INFO|WARN|ERROR)\\$\\$)|({{[^}]+}})`
    - **action** (string): `FAIL_CLOSED_ON_METADATA_LEAK`
- **ignition_sequence_protocol** (object):
  - **pre_ignition_checks** (array):
    - Item 1:
      `GATE_000_MANIFEST_AUDIT`
    - Item 2:
      `GATE_055_BIMODAL_LOCK`
    - Item 3:
      `GATE_060_SANDBOX_AD_HOC`
    - Item 4:
      `GATE_091_NAME_SUBSTITUTION_ABORT`
    - Item 5:
      `GATE_094_SSOT_DUR_CHECK`
    - Item 6:
      `GATE_095_VISUAL_DIALOGUE_ISOLATION`
    - Item 7:
      `GATE_096_SCENE_CONTEXT_AUTHORITY_LOCK`
  - **ignition_sequence** (array):
    - Item 1:
      `Load SSOT Manifest`
    - Item 2:
      `Validate Engine Selection`
    - Item 3:
      `Apply Biometric DNA Anchors`
    - Item 4:
      `Resolve User-Selected Scene Context Authority`
    - Item 5:
      `IF route_mode == MODE_C THEN LOAD source_image_handoff AS MODE_C_METADATA_HANDOFF`
    - Item 6:
      `IF route_mode == MODE_C THEN LOCK Sections_1_2_3_4 visual authority TO MODE_C_METADATA_HANDOFF`
    - Item 7:
      `Resolve Visual Authority FROM [scene_context, SATELLITE_03_VISUAL_DECK, SOVEREIGN_02_PHYSICS_DNA]`
    - Item 8:
      `Resolve Dialogue Authority FROM [SCRIPT_REGISTRY_UNIFIED, SCRIPT_VARIANT_LIBRARY, SATELLITE_05_COACHING_PROTOCOL]`
    - Item 9:
      `Apply Trigger-Based Visual Bias TO VISUAL CHANNEL ONLY`
    - Item 10:
      `Execute BLOCK_N Sharding Math (IF engine_id != GROK)`
    - Item 11:
      `Generate Multi-Block Array (IF engine_id IN [VEO_3_1, SEEDANCE_2_0] AND duration_target > block_max)`
    - Item 12:
      `Generate Single-Block Output (IF engine_id IN [GROK, KLING_3_0] OR duration_target <= block_max)`
    - Item 13:
      `Assemble Sections 1-5, 7, 8, 9 FROM VISUAL CHANNEL ONLY`
    - Item 14:
      `Assemble Section 6 FROM DIALOGUE CHANNEL ONLY`
    - Item 15:
      `ENFORCE: IF route_mode == MODE_C THEN Sections_1_2_3_4 derive only from MODE_C_METADATA_HANDOFF`
    - Item 16:
      `ENFORCE: Sections_1_2_3_4_5_7_8_9 derive only from [scene_context, SATELLITE_03_VISUAL_DECK, SOVEREIGN_02_PHYSICS_DNA]`
    - Item 17:
      `ENFORCE: Section_6 derives only from [SCRIPT_REGISTRY_UNIFIED, SCRIPT_VARIANT_LIBRARY, SATELLITE_05_COACHING_PROTOCOL]`
    - Item 18:
      `ENFORCE: Section_6 dialogue is non-authoritative for Sections_1_2_3_4_5_7_8_9`
    - Item 19:
      `ABORT IF dialogue, hook, USP, CTA, or metaphor vocabulary attempts visual prop, packaging, object, background, or environment instantiation`
    - Item 20:
      `ABORT IF route_mode == MODE_C AND dialogue, hook, USP, CTA, or metaphor vocabulary attempts to override source_image_handoff subject_dna, context_environment, or lighting_camera`
    - Item 21:
      `ABORT IF selected scene_context is overridden by dialogue, hook, USP, CTA, or metaphor vocabulary`
    - Item 22:
      `Merge 9-Section Output WITHOUT CROSS-CHANNEL INHERITANCE EXCEPT sanctioned MODE_C handoff from source_image_handoff to visual channel`
  - **post_ignition_purge** (array):
    - Item 1:
      `Surgical Scrub V2`
    - Item 2:
      `Metadata Leak Check`
    - Item 3:
      `SSOT Integrity Verify`
- **error_registry** (object):
  - **ERR_INVALID_PRODUCT_TYPE** (string): `Invalid product_type value. Must be STEALTH or DIRECT.`
  - **ERR_INVALID_PHYSICS_CLASS** (string): `Invalid physics_class value.`
  - **ERR_INVALID_ENGINE_ID** (string): `Invalid engine_id value.`
  - **ERR_INVALID_DURATION** (string): `Invalid duration_target value.`
  - **ERR_INVALID_FORMULA** (string): `Invalid submode_formula value.`
  - **ERR_BIOMETRIC_DRIFT** (string): `Biometric drift exceeded 0.05 threshold.`
  - **ERR_IDENTITY_SOFTENING** (string): `Identity softening exceeded 0.02 threshold.`
  - **ERR_SILO_CONTAMINATION** (string): `Bimodal Isolation breach: Stealth/Direct overlap detected.`
  - **ERR_NAME_SUBSTITUTION_LEAK** (string): `Character name detected in output. Use DNA instead.`
  - **ERR_PACING_VIOLATION** (string): `Dialogue pacing breach (target 1.6 WPS, hard max 2.0 WPS, kill-switch 3.0 WPS).`
  - **ERR_METADATA_LEAK** (string): `Surgical Scrub V2 failed to purge technical identifiers.`
  - **ERR_SSOT_DURATION_CONFLICT** (string): `Input duration violates engine-specific block caps.`
  - **ERR_SCHEMA_MISMATCH** (string): `Schema version mismatch. Expected v11.1.`
  - **ERR_UNDEF_REF** (string): `Reference to unmapped trigger or silo.`
  - **ERR_NANO_BANANA_BREACH** (string): `FORBIDDEN SUBMODE: Execution halted for engine GROK.`
  - **ERR_TOKEN_LIMIT_RISK** (string): `VEO duration above 56s is forbidden in fail-closed mode.`
  - **ERR_ORPHAN_TRIGGER** (string): `trigger_id failed to map to visual_bias.`
  - **ERR_COORD_SCHEMA_VIOLATION** (string): `Section 9 fails technical coordinate schema.`
  - **ERR_CAMERA_LIGHTING_CONFLICT** (string): `Invalid pairing: UGC_IPHONE_RAW cannot use ELITE_CLEAN lighting.`
  - **ABORT_VISUAL_COPY_LEAK** (string): `Visual output contains object, prop, packaging, environment, or background element derived from dialogue or copywriting.`
  - **ABORT_VISUAL_SCENE_OVERRIDE** (string): `Dialogue, hook, USP, CTA, or metaphor vocabulary attempted to override user-selected scene_context.`
  - **ABORT_DIALOGUE_TO_VISUAL_PROP_INSTANTIATION** (string): `Dialogue-only noun attempted to instantiate visual prop, packaging, object, background, or environment.`
  - **ABORT_METAPHOR_OBJECT_RENDER** (string): `Metaphor or copywriting vocabulary was literalized into physical visual output.`
- **validation_guards** (array):
  - Item 1:
    `SUPPRESS_SEMANTIC_DOMINANCE: IF script_action CONFLICTS WITH [PHYSICS_LOCK_MANDATORY] THEN physics_rule == TRUE`
  - Item 2:
    `ENFORCE_PRIORITY: [PHYSICS_LOCK_MANDATORY] > Natural Language Prose`
  - Item 3:
    `ABORT IF product_type NOT IN [STEALTH, DIRECT]`
  - Item 4:
    `ABORT IF physics_class NOT IN [CLASS_A, CLASS_B, CLASS_C, CLASS_D, CLASS_E, CLASS_GENERIC]`
  - Item 5:
    `ABORT IF physics_class == 'AUTO_FETCH'`
  - Item 6:
    `ABORT IF trigger_id NOT IN [SCARCITY_01, SOCIAL_PROOF_01, AUTHORITY_01, RECIPROCITY_01, FOMO_01, TRANSFORMATION_01, MARUAH_01, EGO_01, TRUST_01, CONFIDENCE_01]`
  - Item 7:
    `ABORT IF engine_id NOT IN [VEO_3_1, GROK, KLING_3_0, SEEDANCE_2_0]`
  - Item 8:
    `ABORT IF route_mode NOT IN [MODE_A, MODE_B, MODE_C]`
  - Item 9:
    `ABORT IF route_mode == MODE_C AND source_image_handoff IN [NULL, '', {}]`
  - Item 10:
    `ABORT IF route_mode == MODE_C AND any source_image_handoff field IN [NULL, '']`
  - Item 11:
    `ABORT IF submode_formula NOT IN [PAS, HSO, AIDA, FAB, SAVAGE_HPAS]`
  - Item 12:
    `ABORT IF engine_id == VEO_3_1 AND duration_target NOT IN [4s, 6s, 8s, 16s, 24s, 32s, 40s, 48s, 56s]`
  - Item 13:
    `ABORT IF engine_id == VEO_3_1 AND duration_target > 56s`
  - Item 14:
    `ABORT IF engine_id == KLING_3_0 AND duration_target NOT IN [3s, 5s, 10s, 15s]`
  - Item 15:
    `ABORT IF engine_id == SEEDANCE_2_0 AND duration_target NOT IN [5s, 10s, 15s]`
  - Item 17:
    `ABORT IF engine_id == GROK AND duration_target NOT IN [6s, 10s]`
  - Item 18:
    `ABORT IF engine_id == GROK AND execution_submode == 'NANO BANANA'`
  - Item 19:
    `ABORT IF camera_style == UGC_IPHONE_RAW AND lighting == ELITE_CLEAN`
  - Item 20:
    `ENFORCE: max_words_per_scene == FLOOR(I * 2.0)`
  - Item 21:
    `VALIDATE: target_words_per_scene == ROUND(I * 1.6)`
  - Item 22:
    `ABORT IF scene_density exceeds abs_kill_switch_words_per_scene == FLOOR(I * 3.0)`
  - Item 23:
    `ABORT IF speech_expected == true AND spoken_coverage_ratio < 0.25`
  - Item 24:
    `ABORT IF speech_expected == true AND tail_silence_s exceeds duration-band limit from SOVEREIGN_03.pacing_governance`
  - Item 25:
    `ABORT IF speech_expected == true AND silence_gap_s exceeds duration-band limit from SOVEREIGN_03.pacing_governance`
  - Item 26:
    `VALIDATE: Section_9 coordinates fall within STRICT_LOCK (X:6-94%, Y:15-65%)`
  - Item 27:
    `ABORT IF visual sections derive nouns, props, objects, packaging, background, or environment from dialogue or copywriting tokens`
  - Item 28:
    `ABORT IF dialogue vocabulary is used as visual scene completion authority`
  - Item 29:
    `ABORT IF dialogue-only noun instantiates prop, packaging, object, background, or environment`
  - Item 30:
    `ABORT IF metaphor or copywriting vocabulary is literalized into physical visual output`
  - Item 31:
    `ABORT IF selected scene_context is overridden by dialogue, hook, USP, CTA, or metaphor vocabulary`
  - Item 32:
    `ENFORCE: visual_sections source authority == [scene_context, SATELLITE_03_VISUAL_DECK, SOVEREIGN_02_PHYSICS_DNA]`
  - Item 33:
    `ENFORCE: IF route_mode == MODE_C THEN visual_sections source authority == [source_image_handoff, MODE_C_METADATA_HANDOFF]`
  - Item 34:
    `ABORT IF route_mode == MODE_C AND dialogue attempts to override inherited image DNA`
  - Item 35:
    `ENFORCE: Section_6 dialogue remains non-authoritative for Sections_1_2_3_4_5_7_8_9`
  - Item 36:
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
