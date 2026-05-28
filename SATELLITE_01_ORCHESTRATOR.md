- **metadata** (object):
  - **file_id** (string): `SATELLITE_01_ORCHESTRATOR`
  - **schema_version** (string): `v11.1`
  - **version_handshake** (string): `v11.1_GRAND_MASTER_SKELETON`
  - **last_edit_date** (string): `2026-03-05`
  - **authority** (string): `SUPREME_SYSTEMS_ARCHITECT`
- **scene_block_orchestration** (object):
  - **BLOCK_1_HOOK** (object):
    - **objective** (string): `Capture attention within first 3s using PREDATOR_CORE hooks`
    - **wps_limit** (number): `2`
    - **visual_priority** (string): `Biometric Anchor DNA (Predator Alignment)`
    - **audio_priority** (string): `Tone Lock (arrogant_drawl/staccato)`
    - **supported_engines** (array):
```json
[
  "VEO_3_1",
  "SORA_2",
  "GROK",
  "KLING_3_0",
  "SEEDANCE_2_0"
]
```

  - **BLOCK_2_PROBLEM** (object):
    - **objective** (string): `Agitate pain point with STEALTH/DIRECT vocabulary`
    - **wps_limit** (number): `1.6`
    - **visual_priority** (string): `Product Physics & HOI`
    - **audio_priority** (string): `10ms Latency Lock`
    - **supported_engines** (array):
```json
[
  "VEO_3_1",
  "SORA_2"
]
```

  - **BLOCK_3_SOLUTION** (object):
    - **objective** (string): `Present USP with explicit physics_class grounding`
    - **wps_limit** (number): `1.6`
    - **visual_priority** (string): `Air-Gap Enforcement per physics_class`
    - **audio_priority** (string): `Viseme Sync`
    - **supported_engines** (array):
```json
[
  "VEO_3_1",
  "SORA_2",
  "SEEDANCE_2_0"
]
```

  - **BLOCK_4_CTA** (object):
    - **objective** (string): `Drive conversion with clear directive`
    - **wps_limit** (number): `2`
    - **visual_priority** (string): `Overlay & Typography (TikTok Shop Safe Zone)`
    - **audio_priority** (string): `Tone Lock (CONFIDENCE)`
    - **supported_engines** (array):
```json
[
  "VEO_3_1",
  "SORA_2",
  "GROK",
  "KLING_3_0"
]
```

  - **block_order_authority** (object):
    - **authoritative_sequence** (array):
```json
[
  "HOOK",
  "PROBLEM",
  "SOLUTION",
  "CTA"
]
```

    - **normalization_rule** (string): `IF variant_block == AGITATE THEN MERGE_INTO PROBLEM`
- **mode_routing** (object):
  - **MODE_A** (object):
    - **lane_authority** (string): `SEA_VISUAL_INTELLIGENCE_ENGINE`
    - **output_contract** (string): `MASTER_PROMPT_PLUS_METADATA_HANDOFF`
  - **MODE_B** (object):
    - **lane_authority** (string): `BOSMAX_v11_1_OMNI_ENGINE`
    - **output_contract** (string): `NINE_SECTION_VIDEO_SCRIPT`
  - **MODE_C** (object):
    - **lane_authority** (string): `SPECIAL_LANE`
    - **output_contract** (string): `MODE_A_METADATA_TO_MODE_B_VISUAL_LOCK`
    - **visual_authority** (string): `source_image_handoff`
    - **enforcement** (array):
```json
[
  "Sections_1_2_3_4 MUST hydrate from source_image_handoff before any scene_context fallback",
  "ABORT IF dialogue or copywriting introduces visual nouns not supported by source_image_handoff"
]
```

- **interval_math_configuration** (object):
  - **math_id** (string): `MATH_STITCH_V11_1`
  - **interval_formula** (string): `I = duration_target / scene_count`
  - **scene_count_default** (string): `AUTO_CALCULATE`
  - **max_duration** (number): `60`
  - **min_duration** (number): `5`
  - **duration_increment** (string): `ENGINE_SPECIFIC`
  - **stitching_math** (object):
    - **VEO_3_1** (string): `Max 8s per block (Deterministic DNA Re-injection)`
    - **SORA_2** (string): `Max 15s per block (Allowed durations: 10s, 15s, 20s, 25s, 30s, 45s, 60s)`
    - **GROK** (string): `Max 10s single block (Allowed durations: 6s, 10s; No sharding permitted)`
    - **KLING_3_0** (string): `Max 15s single block`
    - **SEEDANCE_2_0** (string): `Max 10s per block (20s via dual-block chaining)`
  - **validation** (array):
    - Item 1:
      `ABORT IF scene_count < 1`
    - Item 2:
      `ABORT IF engine_id == VEO_3_1 AND duration_target > 56s`
    - Item 3:
      `ABORT IF engine_id == SORA_2 AND duration_target NOT IN [10s, 15s, 20s, 25s, 30s, 45s, 60s]`
    - Item 4:
      `ABORT IF engine_id == GROK AND duration_target NOT IN [6s, 10s]`
    - Item 5:
      `ABORT IF engine_id == KLING_3_0 AND duration_target NOT IN [5s, 10s, 15s]`
    - Item 6:
      `ABORT IF engine_id == SEEDANCE_2_0 AND duration_target NOT IN [10s, 20s]`
    - Item 7:
      `ENFORCE: I >= 1.25 for minimum scene duration`
    - Item 8:
      `ENFORCE: max_words_per_scene_hard_max == FLOOR(I * 2.0)`
    - Item 9:
      `ENFORCE: max_words_per_scene_target == ROUND(I * 1.6)`
    - Item 10:
      `ABORT IF scene_density exceeds absolute_kill_switch FLOOR(I * 3.0)`
    - Item 11:
      `ABORT IF speech_expected == true AND spoken_coverage_ratio < 0.25`
    - Item 12:
      `ABORT IF speech_expected == true AND tail_silence_s exceeds duration-band limit from SOVEREIGN_03.pacing_governance`
    - Item 13:
      `ABORT IF speech_expected == true AND silence_gap_s exceeds duration-band limit from SOVEREIGN_03.pacing_governance`
- **cross_file_validation** (object):
  - **SOVEREIGN_01_VALIDATION** (object):
    - **manifest_id** (string): `SOVEREIGN_MANIFEST_v11.1`
    - **gate_registry** (array):
```json
[
  "GATE_000_MANIFEST_AUDIT",
  "GATE_050_COACHING_LAYER",
  "GATE_055_BIMODAL_LOCK",
  "GATE_056_HEADWEAR_WARDROBE_COMPAT",
  "GATE_057_AVATAR_CAMERA_COMPAT",
  "GATE_060_SANDBOX_AD_HOC",
  "GATE_091_NAME_SUBSTITUTION_ABORT",
  "GATE_092_WPS_RUNTIME_CHECK",
  "GATE_093_SILO_CONTAMINATION_SCRUB",
  "GATE_094_SSOT_DUR_CHECK",
  "GATE_097_9_SECTION_VALIDATOR"
]
```

    - **silo_definitions** (array):
```json
[
  "ENGINE_STEALTH",
  "ENGINE_DIRECT"
]
```

  - **SOVEREIGN_02_VALIDATION** (object):
    - **material_physics** (array):
```json
[
  "CLASS_A-E (Standardized Air-Gap & Refraction)"
]
```

    - **i2v_stitch_guard** (string): `I2V_STITCH_GUARD_v11.1`
  - **SOVEREIGN_03_VALIDATION** (object):
    - **quality_gates** (object):
```json
{
  "biometric_drift_threshold": 0.05,
  "identity_softening_threshold": 0.02
}
```

    - **pacing_governance_contract** (object):
```json
{
  "target_wps": 1.6,
  "hard_max_wps": 2,
  "absolute_kill_switch_wps": 3
}
```

  - **SATELLITE_03_VALIDATION** (object):
    - **archetypes** (string): `10 characters (DNA Locked)`
    - **micro_expressions** (array):
```json
[
  "PREDATOR_CORE",
  "AUTHENTIC_WHISPER"
]
```

    - **engine_duration_specs** (object):
```json
{
  "VEO_3_1": "max_duration=56s",
  "SORA_2": "allowed_durations=[10s, 15s, 20s, 25s, 30s, 45s, 60s]",
  "GROK": "allowed_durations=[6s, 10s]",
  "KLING_3_0": "allowed_durations=[5s, 10s, 15s]",
  "SEEDANCE_2_0": "allowed_durations=[10s, 20s]"
}
```

  - **SATELLITE_05_VALIDATION** (object):
    - **coaching_protocol_registry** (string): `15 atomic variables`
    - **interview_mode** (string): `SURGICAL_TRAJECTORY_ALIGNMENT`
    - **gate_integration** (string): `primary_gate=GATE_050_COACHING_LAYER | secondary_gates=[GATE_055_BIMODAL_LOCK, GATE_092_WPS_RUNTIME_CHECK, GATE_093_SILO_CONTAMINATION_SCRUB, GATE_094_SSOT_DUR_CHECK, GATE_095_VISUAL_DIALOGUE_ISOLATION, GATE_096_SCENE_CONTEXT_AUTHORITY_LOCK, GATE_097_9_SECTION_VALIDATOR]`
  - **MASTER_IGNITION_VALIDATION** (object):
    - **user_input** (string): `15 variables`
    - **engine_configuration** (string): `5 engines (VEO, SORA, GROK, KLING, SEEDANCE)`
    - **9_section_output_mandate** (string): `Biometric Anchor DNA | Lighting & Scene Physics | Camera & Framing | Visual Action | Product Physics | Dialogue | Audio Tone | Temporal Logic | Overlay`
- **gate_integration** (object):
  - **primary_gates** (array):
    - Item 1:
      `GATE_000_MANIFEST_AUDIT`
    - Item 2:
      `GATE_050_COACHING_LAYER`
    - Item 3:
      `GATE_055_BIMODAL_LOCK`
    - Item 4:
      `GATE_056_HEADWEAR_WARDROBE_COMPAT`
    - Item 5:
      `GATE_057_AVATAR_CAMERA_COMPAT`
    - Item 6:
      `GATE_060_SANDBOX_AD_HOC`
    - Item 7:
      `GATE_091_NAME_SUBSTITUTION_ABORT`
    - Item 8:
      `GATE_092_WPS_RUNTIME_CHECK`
    - Item 9:
      `GATE_093_SILO_CONTAMINATION_SCRUB`
    - Item 10:
      `GATE_094_SSOT_DUR_CHECK`
    - Item 11:
      `GATE_095_VISUAL_DIALOGUE_ISOLATION`
    - Item 12:
      `GATE_096_SCENE_CONTEXT_AUTHORITY_LOCK`
    - Item 13:
      `GATE_097_9_SECTION_VALIDATOR`
  - **secondary_gates** (array):
    - Item 1:
      `GATE_100`
    - Item 2:
      `GATE_101`
    - Item 3:
      `GATE_102`
    - Item 4:
      `GATE_103`
    - Item 5:
      `GATE_106`
  - **gate_logic** (array):
    - Item 1:
      `IF GATE_000_MANIFEST_AUDIT fails THEN ABORT(ERR_SCHEMA_MISMATCH)`
    - Item 2:
      `IF GATE_050_COACHING_LAYER fails THEN ABORT(ABORT_COACHING_INCOMPLETE)`
    - Item 3:
      `IF GATE_055_BIMODAL_LOCK fails THEN ABORT(ABORT_SILO_LEAK)`
    - Item 4:
      `IF GATE_056_HEADWEAR_WARDROBE_COMPAT fails THEN ABORT(ERR_GATE_VALIDATION_FAILURE)`
    - Item 5:
      `IF GATE_057_AVATAR_CAMERA_COMPAT fails THEN ABORT(ERR_GATE_VALIDATION_FAILURE)`
    - Item 6:
      `IF GATE_060_SANDBOX_AD_HOC fails THEN ABORT(ABORT_SANDBOX)`
    - Item 7:
      `IF GATE_091_NAME_SUBSTITUTION_ABORT fails THEN ABORT(ABORT_NAME_SUB)`
    - Item 8:
      `IF GATE_092_WPS_RUNTIME_CHECK fails THEN ABORT(ABORT_WPS_VIOLATION)`
    - Item 9:
      `IF GATE_093_SILO_CONTAMINATION_SCRUB fails THEN ABORT(ABORT_SILO_LEAK)`
    - Item 10:
      `IF GATE_094_SSOT_DUR_CHECK fails THEN ABORT(ERR_SSOT_DURATION_CONFLICT)`
    - Item 11:
      `IF GATE_095_VISUAL_DIALOGUE_ISOLATION fails THEN ABORT(ABORT_VISUAL_COPY_LEAK)`
    - Item 12:
      `IF GATE_096_SCENE_CONTEXT_AUTHORITY_LOCK fails THEN ABORT(ABORT_VISUAL_SCENE_OVERRIDE)`
    - Item 13:
      `IF GATE_097_9_SECTION_VALIDATOR fails THEN ABORT(ERR_SECTION_COUNT_MISMATCH)`
    - Item 14:
      `IF GATE_098_MODE_C_HANDOFF_LOCK fails THEN ABORT(ABORT_MODE_C_HANDOFF_LOCK)`
    - Item 15:
      `IF GATE_106_BLOCK_ORDER_NORMALIZATION fails THEN ABORT(ERR_CROSS_FILE_MISMATCH)`
    - Item 16:
      `IF all gates pass THEN PROCEED TO ORCHESTRATION`
- **output_sanitization** (object):
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

    - **pattern_regex** (string): `(\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\b)|(\b[0-9a-fA-F]{16,}\b)|($$(DEBUG|TRACE|INFO|WARN|ERROR)$$)|({{[^}]+}})`
    - **action** (string): `FAIL_CLOSED_ON_METADATA_LEAK`
    - **fallback_action** (string): `STRIP_SENSITIVE_TOKENS_AND_FAIL_CLOSED`
  - **biometric_thresholds** (object):
    - **drift** (number): `0.05`
    - **identity_softening** (number): `0.02`
- **error_registry** (object):
  - **ABORT_COACHING_INCOMPLETE** (string): `Atomic variables incomplete for coaching layer.`
  - **ABORT_NAME_SUB** (string): `Name/PII substitution detected.`
  - **ABORT_WPS_VIOLATION** (string): `WPS runtime validation failed.`
  - **ABORT_SILO_LEAK** (string): `Cross-silo vocabulary leak detected.`
  - **ABORT_SANDBOX** (string): `Coaching/sandbox gate violation detected.`
  - **ABORT_VISUAL_COPY_LEAK** (string): `Visual output contains object, prop, packaging, environment, or background element derived from dialogue or copywriting.`
  - **ABORT_VISUAL_SCENE_OVERRIDE** (string): `Dialogue, hook, USP, CTA, or metaphor vocabulary attempted to override user-selected scene_context.`
  - **ABORT_MODE_C_HANDOFF_LOCK** (string): `Mode C source image handoff is incomplete or inherited image DNA was overridden.`
  - **ABORT_DIALOGUE_TO_VISUAL_PROP_INSTANTIATION** (string): `Dialogue-only noun attempted to instantiate visual prop, packaging, object, background, or environment.`
  - **ABORT_METAPHOR_OBJECT_RENDER** (string): `Metaphor or copywriting vocabulary was literalized into physical visual output.`
  - **ERR_INVALID_SCENE_BLOCK** (string): `Invalid scene_block value.`
  - **ERR_INVALID_INTERVAL_MATH** (string): `Invalid interval math configuration.`
  - **ERR_CROSS_FILE_MISMATCH** (string): `Cross-file validation mismatch.`
  - **ERR_GATE_VALIDATION_FAILURE** (string): `Gate validation failure.`
  - **ERR_BIOMETRIC_DRIFT** (string): `Biometric drift exceeded 0.05 threshold.`
  - **ERR_IDENTITY_SOFTENING** (string): `Identity softening exceeded 0.02 threshold.`
  - **ERR_SILO_CONTAMINATION** (string): `Silo contamination detected (Bimodal Breach).`
  - **ERR_NAME_SUBSTITUTION_LEAK** (string): `Character name leak detected. Use DNA reference.`
  - **ERR_METADATA_LEAK** (string): `Metadata leak detected during surgical scrub.`
  - **ERR_SCHEMA_MISMATCH** (string): `Schema version mismatch. System requires v11.1.`
  - **ERR_ENGINE_VERSION_MISMATCH** (string): `Engine version does not match BOSMAX v11.1 standards.`
  - **ERR_SSOT_DURATION_CONFLICT** (string): `Input duration violates engine-specific block limits.`
  - **ERR_SECTION_COUNT_MISMATCH** (string): `Assembled output does not contain exactly 9 mandatory sections.`
  - **ERR_NANO_BANANA_BREACH** (string): `Forbidden submode (NANO BANANA) detected for engine GROK.`
- **validation_guards** (array):
  - Item 1:
    `ABORT IF scene_block NOT IN [HOOK, PROBLEM, SOLUTION, CTA]`
  - Item 2:
    `ABORT IF engine_id == VEO_3_1 AND duration_target > 56s`
  - Item 3:
    `ABORT IF engine_id == SORA_2 AND duration_target NOT IN [10s, 15s, 20s, 25s, 30s, 45s, 60s]`
  - Item 4:
    `ABORT IF engine_id == GROK AND duration_target NOT IN [6s, 10s]`
  - Item 5:
    `ABORT IF engine_id == KLING_3_0 AND duration_target NOT IN [5s, 10s, 15s]`
  - Item 6:
    `ABORT IF engine_id == SEEDANCE_2_0 AND duration_target NOT IN [10s, 20s]`
  - Item 7:
    `ENFORCE: wps_limit per scene_block (HOOK/CTA: 2.0, PROBLEM/SOLUTION: 1.6)`
  - Item 8:
    `VALIDATE: cross_file alignment v11.1`
  - Item 9:
    `ENFORCE: authoritative scene block sequence == [HOOK, PROBLEM, SOLUTION, CTA]`
  - Item 10:
    `ABORT IF AGITATE block is not normalized into PROBLEM before assembly`
  - Item 11:
    `ABORT IF GATE_092_WPS_RUNTIME_CHECK fails`
  - Item 12:
    `ABORT IF GATE_093_SILO_CONTAMINATION_SCRUB fails`
  - Item 13:
    `ABORT IF GATE_097_9_SECTION_VALIDATOR fails`
  - Item 14:
    `ABORT IF GATE_056_HEADWEAR_WARDROBE_COMPAT fails`
  - Item 15:
    `ABORT IF GATE_057_AVATAR_CAMERA_COMPAT fails`
  - Item 16:
    `ABORT IF GATE_095_VISUAL_DIALOGUE_ISOLATION fails`
  - Item 17:
    `ABORT IF GATE_096_SCENE_CONTEXT_AUTHORITY_LOCK fails`
  - Item 18:
    `ENFORCE: biometric_drift_threshold == 0.05`
  - Item 19:
    `ENFORCE: identity_softening_threshold == 0.02`
  - Item 20:
    `ENFORCE: surgical_scrub_v2 enabled`
  - Item 21:
    `ENFORCE: coaching_protocol_registry 15 atomic variables per SATELLITE_05`
  - Item 22:
    `ABORT IF engine_id == GROK AND execution_submode == 'NANO BANANA'`
  - Item 23:
    `ENFORCE: IF engine_id == VEO_3_1 THEN single_prompt_block_duration <= 8s`
  - Item 24:
    `ENFORCE: IF engine_id == SORA_2 THEN single_prompt_block_duration <= 15s`
  - Item 25:
    `ENFORCE: dna_reinjection_hop == 1 for every block boundary`
  - Item 26:
    `ABORT IF visual sections derive nouns, props, objects, packaging, background, or environment from dialogue or copywriting tokens`
  - Item 27:
    `ABORT IF dialogue vocabulary is used as visual scene completion authority`
  - Item 28:
    `ABORT IF dialogue-only noun instantiates prop, packaging, object, background, or environment`
  - Item 29:
    `ABORT IF metaphor or copywriting vocabulary is literalized into physical visual output`
  - Item 30:
    `ABORT IF selected scene_context is overridden by dialogue, hook, USP, CTA, or metaphor vocabulary`
  - Item 31:
    `ENFORCE: visual_sections source authority == [scene_context, SATELLITE_03_VISUAL_DECK, SOVEREIGN_02_PHYSICS_DNA]`
  - Item 32:
    `ENFORCE: Section_6 dialogue remains non-authoritative for Sections_1_2_3_4_5_7_8_9`
  - Item 33:
    `ABORT IF coach_handoff_payload_missing == true`
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
