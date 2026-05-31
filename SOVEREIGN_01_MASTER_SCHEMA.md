- **metadata** (object):
  - **file_id** (string): `SOVEREIGN_01_MASTER_SCHEMA`
  - **schema_version** (string): `v11.1`
  - **version_handshake** (string): `v11.1_GRAND_MASTER_SKELETON`
  - **last_edit_date** (string): `2026-03-05`
  - **authority** (string): `SUPREME_SYSTEMS_ARCHITECT`
- **master_index_policy** (object):
  - **manifest_id** (string): `SOVEREIGN_MANIFEST_v11.1`
  - **required_files_in_order** (array):
    - Item 1:
      `SOVEREIGN_01_MASTER_SCHEMA.yaml`
    - Item 2:
      `SOVEREIGN_02_PHYSICS_DNA.yaml`
    - Item 3:
      `SOVEREIGN_03_CORE_LOGIC.yaml`
    - Item 4:
      `SATELLITE_01_ORCHESTRATOR.yaml`
    - Item 5:
      `SATELLITE_02_LINT_NEGATIVES.yaml`
    - Item 6:
      `SATELLITE_03_VISUAL_DECK.yaml`
    - Item 7:
      `SATELLITE_04_MAPPING_MATRIX.yaml`
    - Item 8:
      `SATELLITE_05_COACHING_PROTOCOL.yaml`
    - Item 9:
      `MASTER_IGNITION_TEMPLATE.yaml`
    - Item 10:
      `SCRIPT_REGISTRY_UNIFIED.yaml`
    - Item 11:
      `SCRIPT_VARIANT_LIBRARY.yaml`
  - **canonical_token_registry** (object):
    - **namespaces** (array):
```json
[
  {
    "prefix": "CLASS_"
  },
  {
    "prefix": "PROP_"
  },
  {
    "prefix": "CAM_"
  },
  {
    "prefix": "TRG_"
  },
  {
    "prefix": "DNA_"
  },
  {
    "prefix": "SCRIPT_"
  },
  {
    "prefix": "CTX_"
  },
  {
    "prefix": "SHOT_"
  },
  {
    "prefix": "W_"
  },
  {
    "prefix": "TEMP_"
  }
]
```

    - **policy** (array):
```json
[
  "Do not allow raw namespace prefixes to appear in final prose.",
  "All internal ids MUST be rewritten via canonical translation functions prior to output (see output_cleanroom_protocol)."
]
```

- **gate_registry** (object):
  - **GATE_000_MANIFEST_AUDIT** (object):
    - **description** (string): `Verify manifest integrity and required_files_in_order match available files`
    - **logic** (string): `COMPARE manifest.required_files_in_order TO repo.available_files`
    - **logic_source** (string): `FETCH FROM SOVEREIGN_01_MASTER_SCHEMA.master_index_policy.required_files_in_order`
    - **abort_code** (string): `ABORT_MANIFEST`
  - **GATE_050_COACHING_LAYER** (object):
    - **description** (string): `Coaching protocol ad-hoc gate for atomic variable collection`
    - **logic** (string): `VALIDATE atomic_variables >= 15 before generation`
    - **logic_source** (string): `FETCH FROM SATELLITE_05_COACHING_PROTOCOL.coaching_protocol_registry`
    - **abort_code** (string): `ABORT_COACHING_INCOMPLETE`
  - **GATE_055_BIMODAL_LOCK** (object):
    - **description** (string): `Enforce silo isolation and engine compatibility for STEALTH vs DIRECT generation`
    - **logic** (string): `VALIDATE product_type routes to correct silo authority and supported engine list without cross-silo contamination`
    - **logic_source** (string): `FETCH FROM SOVEREIGN_01_MASTER_SCHEMA.silo_vocabulary_authority + SOVEREIGN_03_CORE_LOGIC.intelligence_layer.global_marketing_laws`
    - **abort_code** (string): `ABORT_SILO_LEAK`
    - **mappings** (object):
```json
{
  "ENGINE_STEALTH": {
    "supported_engines": [
      "VEO_3_1",
      "GROK",
      "KLING_3_0",
      "SEEDANCE_2_0"
    ]
  },
  "ENGINE_DIRECT": {
    "supported_engines": [
      "VEO_3_1",
      "GROK",
      "KLING_3_0",
      "SEEDANCE_2_0"
    ]
  }
}
```

  - **GATE_056_HEADWEAR_WARDROBE_COMPAT** (object):
    - **description** (string): `Validate avatar-specific headwear and wardrobe compatibility`
    - **logic** (string): `CROSS_CHECK user_input.avatar_id + user_input.headwear_style AGAINST SATELLITE_03_VISUAL_DECK.headwear_wardrobe_compatibility_matrix AND user_input.wardrobe AGAINST SATELLITE_03_VISUAL_DECK.archetypes.[avatar_id].wardrobe_preference`
    - **logic_source** (string): `FETCH FROM SATELLITE_03_VISUAL_DECK.headwear_wardrobe_compatibility_matrix + SATELLITE_03_VISUAL_DECK.archetypes`
    - **abort_code** (string): `ABORT_HEADWEAR_WARDROBE_COMPAT`
  - **GATE_057_AVATAR_CAMERA_COMPAT** (object):
    - **description** (string): `Validate avatar_position to camera_behavior compatibility`
    - **logic** (string): `CROSS_CHECK user_input.avatar_position + user_input.camera_behavior AGAINST SATELLITE_04_MAPPING_MATRIX.avatar_position_camera_compatibility`
    - **logic_source** (string): `FETCH FROM SATELLITE_04_MAPPING_MATRIX.avatar_position_camera_compatibility`
    - **abort_code** (string): `ABORT_AVATAR_CAMERA_COMPAT`
  - **GATE_091_NAME_SUBSTITUTION_ABORT** (object):
    - **description** (string): `Abort on name/PII substitution`
    - **mappings** (object):
```json
{
  "forbidden_tokens": 11
}
```

    - **abort_code** (string): `ABORT_NAME_SUB`
  - **GATE_092_WPS_RUNTIME_CHECK** (object):
    - **description** (string): `WPS runtime validation gate`
    - **logic** (string): `VALIDATE pacing against SOVEREIGN_03_CORE_LOGIC.pacing_governance (target 1.6 WPS, hard max 2.0 WPS, absolute kill-switch 3.0 WPS)`
    - **abort_code** (string): `ABORT_WPS_VIOLATION`
  - **GATE_093_SILO_CONTAMINATION_SCRUB** (object):
    - **description** (string): `Silo vocabulary contamination check`
    - **logic** (string): `SCAN output for cross-silo vocabulary leaks`
    - **abort_code** (string): `ABORT_SILO_LEAK`
  - **GATE_094_SSOT_DUR_CHECK** (object):
    - **description** (string): `Enforce engine-specific physical duration limits`
    - **logic** (string): `CROSS_CHECK user_input.duration_target AGAINST MASTER_IGNITION_TEMPLATE.engine_configuration`
    - **logic_source** (string): `FETCH FROM MASTER_IGNITION_TEMPLATE.engine_configuration`
    - **abort_code** (string): `ERR_SSOT_DURATION_CONFLICT`
  - **GATE_095_VISUAL_DIALOGUE_ISOLATION** (object):
    - **description** (string): `Abort if visual sections derive props, objects, packaging, background, or environment from dialogue/copywriting authority`
    - **logic** (string): `ABORT IF visual_sections reference dialogue-derived nouns, metaphor-derived nouns, hook-derived nouns, USP-derived nouns, or CTA-derived nouns not declared in scene_context, SATELLITE_03_VISUAL_DECK, or SOVEREIGN_02_PHYSICS_DNA`
    - **logic_source** (string): `FETCH FROM SOVEREIGN_03_CORE_LOGIC.visual_dialogue_isolation_policy + MASTER_IGNITION_TEMPLATE.ignition_sequence_protocol + SCRIPT_REGISTRY_UNIFIED.dialogue_assembly_rules`
    - **abort_code** (string): `ABORT_VISUAL_COPY_LEAK`
  - **GATE_096_SCENE_CONTEXT_AUTHORITY_LOCK** (object):
    - **description** (string): `Abort if user-selected scene_context is overridden by dialogue, metaphor, hook, USP, or CTA vocabulary`
    - **logic** (string): `ABORT IF scene_context authority for Sections_1_2_3_4_5_7_8_9 is overridden by dialogue-side vocabulary or copywriting-side vocabulary`
    - **logic_source** (string): `FETCH FROM MASTER_IGNITION_TEMPLATE.ignition_sequence_protocol + SOVEREIGN_03_CORE_LOGIC.visual_dialogue_isolation_policy + SATELLITE_03_VISUAL_DECK.scene_output_translation`
    - **abort_code** (string): `ABORT_VISUAL_SCENE_OVERRIDE`
  - **GATE_097_9_SECTION_VALIDATOR** (object):
    - **description** (string): `Fail-closed validator for assembled nine-section output compliance`
    - **logic** (string): `COUNT assembled_output.sections == 9 AND EXACT_MATCH assembled_output.section_titles AGAINST MASTER_IGNITION_TEMPLATE.9_section_output_mandate.sections`
    - **logic_source** (string): `FETCH FROM MASTER_IGNITION_TEMPLATE.9_section_output_mandate.sections`
    - **abort_code** (string): `ERR_SECTION_COUNT_MISMATCH`
  - **GATE_098_MODE_C_HANDOFF_LOCK** (object):
    - **description** (string): `Validate Mode C source_image_handoff completeness and inherited visual authority lock`
    - **logic** (string): `IF route_mode == MODE_C THEN VALIDATE source_image_handoff.subject_dna + source_image_handoff.context_environment + source_image_handoff.lighting_camera are present AND ABORT if dialogue/copywriting attempts override ELSE SKIP`
    - **logic_source** (string): `FETCH FROM MASTER_IGNITION_TEMPLATE.user_input.source_image_handoff + SOVEREIGN_03_CORE_LOGIC.intelligence_layer.global_marketing_laws.mode_c_special_lane_policy`
    - **abort_code** (string): `ABORT_MODE_C_HANDOFF_LOCK`
  - **GATE_060_SANDBOX_AD_HOC** (object):
    - **description** (string): `Coaching/sandbox ad-hoc gate`
    - **abort_code** (string): `ABORT_SANDBOX`
- **silo_vocabulary_authority** (object):
  - **meta** (object):
    - **target_silo** (string): `FETCH FROM MASTER_IGNITION.user_input.product_type`
    - **forced_silo** (string): `IF meta.target_silo == 'STEALTH' THEN FETCH FROM SOVEREIGN_01_MASTER_SCHEMA.silo_vocabulary_authority.silo_definitions.ENGINE_STEALTH ELSE FETCH FROM SOVEREIGN_01_MASTER_SCHEMA.silo_vocabulary_authority.silo_definitions.ENGINE_DIRECT`
    - **schema_version** (string): `v11.1`
  - **supported_engines** (array):
    - Item 1:
      `VEO_3_1`
    - Item 2:
      `GROK`
    - Item 3:
      `KLING_3_0`
    - Item 4:
      `SEEDANCE_2_0`
  - **silo_definitions** (object):
    - **ENGINE_STEALTH** (object):
```json
{
  "supported_engines": [
    "VEO_3_1",
    "GROK",
    "KLING_3_0",
    "SEEDANCE_2_0"
  ],
  "forbidden_pronouns": [
    "saya",
    "anda",
    "awak",
    "kamu"
  ]
}
```

    - **ENGINE_DIRECT** (object):
```json
{
  "supported_engines": [
    "VEO_3_1",
    "GROK",
    "KLING_3_0",
    "SEEDANCE_2_0"
  ],
  "forbidden_pronouns": [
    "aku",
    "kau",
    "lu",
    "gua",
    "weh",
    "doh",
    "abang"
  ]
}
```

- **error_registry** (object):
  - **ABORT_MANIFEST** (string): `Manifest integrity validation failed.`
  - **ABORT_COACHING_INCOMPLETE** (string): `Atomic variables incomplete for coaching layer.`
  - **ABORT_NAME_SUB** (string): `Name/PII substitution detected.`
  - **ABORT_WPS_VIOLATION** (string): `Pacing runtime validation failed (hard max 2.0 WPS or kill-switch 3.0 WPS breached).`
  - **ABORT_SILO_LEAK** (string): `Cross-silo vocabulary leak detected.`
  - **ABORT_HEADWEAR_WARDROBE_COMPAT** (string): `Headwear and wardrobe combination is not allowed for selected avatar.`
  - **ABORT_AVATAR_CAMERA_COMPAT** (string): `avatar_position and camera_behavior combination is not allowed.`
  - **ABORT_SANDBOX** (string): `Coaching/sandbox gate violation detected.`
  - **ABORT_VISUAL_COPY_LEAK** (string): `Visual output contains object, prop, packaging, environment, or background element derived from dialogue or copywriting.`
  - **ABORT_VISUAL_SCENE_OVERRIDE** (string): `Dialogue, metaphor, hook, USP, or CTA vocabulary attempted to override user-selected scene_context.`
  - **ABORT_DIALOGUE_TO_VISUAL_PROP_INSTANTIATION** (string): `Dialogue-only noun attempted to instantiate visual prop, packaging, object, background, or environment.`
  - **ABORT_METAPHOR_OBJECT_RENDER** (string): `Metaphor or copywriting vocabulary was literalized into physical visual output.`
  - **ERR_INVALID_AVATAR_ID** (string): `Invalid avatar_id value.`
  - **ERR_INVALID_SILO_ANCHOR** (string): `Invalid silo_anchor value.`
  - **ERR_INVALID_ENGINE_TARGET** (string): `Invalid engine_target value.`
  - **ERR_INVALID_PRODUCT_CLASS** (string): `Invalid product_class value.`
  - **ERR_INVALID_SCENE_CONTEXT** (string): `Invalid scene_context value.`
  - **ERR_INVALID_WARDROBE_SET** (string): `Invalid wardrobe_set value.`
  - **ERR_BIOMETRIC_DRIFT** (string): `Biometric drift exceeded 0.05 threshold. Execute @Image1_REFRESH.`
  - **ERR_IDENTITY_SOFTENING** (string): `Identity softening exceeded 0.02 threshold. Abort pipeline.`
  - **ERR_MICRO_EXPRESSION_MISMATCH** (string): `Micro-expression mismatch detected.`
  - **ERR_CAMERA_BEHAVIOR_CONFLICT** (string): `Camera behavior conflict detected.`
  - **ERR_SANDBOX_VIOLATION** (string): `Sandbox logic violation detected.`
  - **ERR_IDENTITY_PERSISTENCE_FAILURE** (string): `Identity persistence failure detected.`
  - **ERR_METADATA_LEAK** (string): `Metadata leak detected.`
  - **ERR_SSOT_VIOLATION** (string): `SSOT violation detected.`
  - **ERR_SCHEMA_MISMATCH** (string): `Schema version mismatch.`
  - **ERR_UNDEF_REF** (string): `Undefined reference.`
  - **FAIL_CLOSED_BIOMETRIC_DRIFT** (string): `Biometric drift threshold exceeded. Abort pipeline.`
  - **FAIL_CLOSED_ON_METADATA_LEAK** (string): `Metadata leak detected. Strip sensitive tokens and fail closed.`
  - **ERR_ENGINE_VERSION_MISMATCH** (string): `Engine version does not match BOSMAX v11.1 standards.`
  - **ERR_SEEDANCE_NOT_CONFIGURED** (string): `Seedance 2.0 selected but not configured in manifest.`
  - **ERR_KLING_HEURISTIC_VIOLATION** (string): `Kling 3.0 parameters exceed SSOT physical thresholds.`
  - **ERR_VOCAB_FALLBACK_v11.1** (string): `Vocab fallback applied - direct safe vocab enforced.`
  - **ERR_NANO_BANANA_BREACH** (string): `Forbidden submode (NANO BANANA) detected for engine GROK.`
  - **ERR_SSOT_DURATION_CONFLICT** (string): `Input duration not in engine-specific allowed list.`
  - **ERR_SECTION_COUNT_MISMATCH** (string): `Assembled output does not contain exactly 9 mandatory sections.`
  - **ABORT_MODE_C_HANDOFF_LOCK** (string): `Mode C source image handoff is incomplete or inherited image DNA was overridden.`
- **validation_guards** (array):
  - Item 1:
    `--- MANIFEST INTEGRITY GUARDS (3) ---`
  - Item 2:
    `VALIDATE: manifest_id == SOVEREIGN_MANIFEST_v11.1`
  - Item 3:
    `ENFORCE: required_files_in_order has 13 files`
  - Item 4:
    `VALIDATE: required_files_in_order uses full filenames (no aliases)`
  - Item 5:
    `--- GATE REGISTRY GUARDS (13) ---`
  - Item 6:
    `VALIDATE: gate_registry has GATE_000_MANIFEST_AUDIT`
  - Item 7:
    `VALIDATE: gate_registry has GATE_050_COACHING_LAYER`
  - Item 8:
    `VALIDATE: gate_registry has GATE_055_BIMODAL_LOCK`
  - Item 9:
    `VALIDATE: gate_registry has GATE_056_HEADWEAR_WARDROBE_COMPAT`
  - Item 10:
    `VALIDATE: gate_registry has GATE_057_AVATAR_CAMERA_COMPAT`
  - Item 11:
    `VALIDATE: gate_registry has GATE_060_SANDBOX_AD_HOC`
  - Item 12:
    `VALIDATE: gate_registry has GATE_091_NAME_SUBSTITUTION_ABORT`
  - Item 13:
    `VALIDATE: gate_registry has GATE_092_WPS_RUNTIME_CHECK`
  - Item 14:
    `VALIDATE: gate_registry has GATE_093_SILO_CONTAMINATION_SCRUB`
  - Item 15:
    `VALIDATE: gate_registry has GATE_094_SSOT_DUR_CHECK`
  - Item 16:
    `VALIDATE: gate_registry has GATE_095_VISUAL_DIALOGUE_ISOLATION`
  - Item 17:
    `VALIDATE: gate_registry has GATE_096_SCENE_CONTEXT_AUTHORITY_LOCK`
  - Item 18:
    `VALIDATE: gate_registry has GATE_097_9_SECTION_VALIDATOR`
  - Item 19:
    `VALIDATE: gate_registry has GATE_098_MODE_C_HANDOFF_LOCK`
  - Item 20:
    `--- SILO VOCABULARY GUARDS (3) ---`
  - Item 21:
    `ENFORCE: silo_vocabulary_authority has 2 silo_definitions`
  - Item 22:
    `VALIDATE: ENGINE_STEALTH forbidden_pronouns (4 pronouns)`
  - Item 23:
    `VALIDATE: ENGINE_DIRECT forbidden_pronouns (7 pronouns)`
  - Item 24:
    `--- ERROR REGISTRY GUARDS (3) ---`
  - Item 25:
    `ENFORCE: error_registry has 17+ codes`
  - Item 26:
    `VALIDATE: error_registry includes all abort_code values declared in gate_registry`
  - Item 27:
    `VALIDATE: error_codes match PROJECT_INSTRUCTION ErrorRegistry`
  - Item 28:
    `--- METADATA LEAK PREVENTION GUARDS (3) ---`
  - Item 29:
    `ENFORCE: surgical_scrub_v2 enabled`
  - Item 30:
    `VALIDATE: deny_fields has 6 fields (raw_id, system_id, internal_id, uuid, trace_id, generation_id)`
  - Item 31:
    `ENFORCE: pre_transform_purge == true`
  - Item 32:
    `--- SSOT INTEGRITY GUARDS (4) ---`
  - Item 33:
    `ENFORCE: FETCH FROM syntax for all SSOT values`
  - Item 34:
    `VALIDATE: all labels present ([SSOT_INTERNAL], [BOSMAX_HEURISTIC], [EXTERNAL_ENGINE_ADDED])`
  - Item 35:
    `ENFORCE: schema_version == v11.1`
  - Item 36:
    `VALIDATE: version_handshake == v11.1_GRAND_MASTER_SKELETON`
  - Item 37:
    `--- CROSS-FILE VALIDATION GUARDS (2) ---`
  - Item 38:
    `VALIDATE: cross-file alignment per SOVEREIGN_01 manifest`
  - Item 39:
    `ENFORCE: all required_files_in_order accessible and parseable`
  - Item 40:
    `--- ENGINE SUPPORT GUARDS (3) ---`
  - Item 41:
    `ENFORCE: supported_engines INCLUDE KLING_3_0 for v11.1`
  - Item 42:
    `ENFORCE: supported_engines INCLUDE SEEDANCE_2_0 for v11.1`
  - Item 43:
    `ENFORCE: supported_engines INCLUDE GROK for v11.1`
  - Item 44:
    `--- BIOMETRIC THRESHOLD GUARDS (2) ---`
  - Item 45:
    `VALIDATE: biometric_drift_threshold == 0.05 per SOV_03 Section 7`
  - Item 46:
    `VALIDATE: identity_softening_threshold == 0.02 per SOV_03 Section 7`
  - Item 47:
    `--- VISUAL / DIALOGUE ISOLATION GUARDS (5) ---`
  - Item 48:
    `ABORT IF visual sections derive nouns, props, objects, packaging, background, or environment from dialogue or copywriting tokens`
  - Item 49:
    `ABORT IF dialogue vocabulary is used as visual scene completion authority`
  - Item 50:
    `ABORT IF dialogue-only noun instantiates prop, packaging, object, background, or environment`
  - Item 51:
    `ABORT IF metaphor or copywriting vocabulary is literalized into physical visual output`
  - Item 52:
    `ABORT IF selected scene_context is overridden by dialogue, metaphor, hook, USP, or CTA vocabulary`
  - Item 53:
    `--- SSOT CRITICAL DURATION & SUBMODE GUARDS ---`
  - Item 54:
    `ABORT IF engine_id == KLING_3_0 AND duration_target > 15s`
  - Item 55:
    `ABORT IF engine_id == SEEDANCE_2_0 AND duration_target > 15s`
  - Item 56:
    `ABORT IF engine_id == GROK AND duration_target NOT IN FETCH_FROM MASTER_IGNITION_TEMPLATE.engine_configuration.GROK.supported_durations`
  - Item 57:
    `ABORT IF engine_id == GROK AND execution_submode == 'NANO BANANA'`
  - Item 58:
    `--- 9-SECTION OUTPUT GUARD (1) ---`
  - Item 59:
    `ENFORCE: 9-section output titles match BOSMAX v11.1 OMNI ENGINE VIDEO GENERATION SYSTEM.txt`
