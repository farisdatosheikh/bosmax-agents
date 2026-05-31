- **metadata** (object):
  - **file_id** (string): `SATELLITE_05_COACHING_PROTOCOL`
  - **schema_version** (string): `v11.1`
  - **version_handshake** (string): `v11.1_GRAND_MASTER_SKELETON`
  - **last_edit_date** (string): `2026-03-05`
  - **authority** (string): `SUPREME_SYSTEMS_ARCHITECT`
- **coaching_protocol_registry** (object):
  - **protocol_id** (string): `CP_REG_V11_1`
  - **interview_mode** (string): `SURGICAL_TRAJECTORY_ALIGNMENT`
  - **trigger_gate** (string): `GATE_050_COACHING_LAYER`
  - **atomic_variables_required** (number): `15`
  - **language_context_selector** (object):
    - **MALAY** (object):
```json
{
  "STEALTH": "CONVERSATIONAL_STEALTH",
  "DIRECT": "PROFESSIONAL_DIRECT"
}
```

  - **query_flow** (array):
    - Item 1:
```json
{
  "variable": "product_id",
  "query": "Apakah ID Produk atau Nama Unik untuk aset ini?",
  "validation": "REGEX_ALPHANUMERIC",
  "required": true
}
```

    - Item 2:
```json
{
  "variable": "product_type",
  "query": "Adakah ini produk STEALTH atau DIRECT?",
  "validation": "ENUM:[STEALTH, DIRECT]",
  "required": true
}
```

    - Item 3:
```json
{
  "variable": "physics_class",
  "query": "Sahkan physics_class secara eksplisit (CLASS_A, CLASS_B, CLASS_C, CLASS_D, CLASS_E, CLASS_GENERIC):",
  "validation": "ENUM:[CLASS_A, CLASS_B, CLASS_C, CLASS_D, CLASS_E, CLASS_GENERIC]",
  "required": true,
  "fallback_logic": {
    "description": "Resolve missing physics_class safely before generation.",
    "rule": "IF physics_class == NULL OR physics_class == '' THEN SET physics_class = 'CLASS_GENERIC'"
  },
  "fail_closed_guard": {
    "description": "Abort if final physics_class not in allowed enumeration.",
    "rule": "ABORT IF physics_class NOT IN [CLASS_A, CLASS_B, CLASS_C, CLASS_D, CLASS_E, CLASS_GENERIC]"
  }
}
```

    - Item 4:
```json
{
  "variable": "trigger_id",
  "query": "Apakah emosi utama? (MARUAH_01, EGO_01, TRUST_01, CONFIDENCE_01)",
  "validation": "FETCH FROM MASTER_IGNITION_TEMPLATE.trigger_id",
  "required": true,
  "mapping_note": "EGO_01/MARUAH_01 -> PREDATOR_CORE | TRUST_01/CONFIDENCE_01 -> AUTHENTIC_WHISPER"
}
```

    - Item 5:
```json
{
  "variable": "avatar_id",
  "query": "Siapa watak yang sesuai? Pilih avatar_id daripada registry archetypes (FETCH FROM SATELLITE_03_VISUAL_DECK.archetypes).",
  "validation": "FETCH FROM SATELLITE_03_VISUAL_DECK.archetypes",
  "required": true
}
```

    - Item 6:
```json
{
  "variable": "headwear_style",
  "query": "Pilihan headwear? (AUTO, HIJAB, NON_HIJAB)",
  "validation": "ENUM:[AUTO, HIJAB, NON_HIJAB]",
  "required": true
}
```

    - Item 7:
```json
{
  "variable": "wardrobe",
  "query": "Pilih wardrobe daripada registry wardrobe_collections.",
  "validation": "FETCH FROM SATELLITE_03_VISUAL_DECK.wardrobe_collections",
  "required": true
}
```

    - Item 8:
```json
{
  "variable": "avatar_position",
  "query": "Pilih avatar_position daripada registry authoritative mapping.",
  "validation": "FETCH FROM SATELLITE_04_MAPPING_MATRIX.avatar_position_camera_compatibility",
  "required": true
}
```

    - Item 9:
```json
{
  "variable": "camera_behavior",
  "query": "Pilih camera_behavior daripada registry SATELLITE_03.camera_behavior.",
  "validation": "FETCH FROM SATELLITE_03_VISUAL_DECK.camera_behavior",
  "required": true
}
```

    - Item 10:
```json
{
  "variable": "scene_context",
  "query": "Pilih scene_context daripada registry SATELLITE_03.scenes (contoh: CTX_KITCHEN_MODERN).",
  "validation": "FETCH FROM SATELLITE_03_VISUAL_DECK.scenes",
  "required": true
}
```

    - Item 11:
```json
{
  "variable": "engine_id",
  "query": "Engine video mana? (VEO_3_1, GROK, KLING_3_0, SEEDANCE_2_0)",
  "validation": "ENUM:[VEO_3_1, GROK, KLING_3_0, SEEDANCE_2_0]",
  "required": true
}
```

    - Item 12:
```json
{
  "variable": "submode_formula",
  "query": "Formula skrip? (PAS, HSO, AIDA, FAB, SAVAGE_HPAS)",
  "validation": "ENUM:[PAS, HSO, AIDA, FAB, SAVAGE_HPAS]",
  "required": true
}
```

    - Item 13:
```json
{
  "variable": "duration_target",
  "query": "Berapa saat? [VEO_3_1: 4s,6s,8s,16s-56s | GROK: 6s,10s | KLING_3_0: 3s,5s,10s,15s | SEEDANCE_2_0: 5s,10s,15s]",
  "validation": "FETCH FROM MASTER_IGNITION_TEMPLATE.duration_target",
  "required": true
}
```

    - Item 14:
```json
{
  "variable": "target_language",
  "query": "Bahasa dialog sasaran? (contoh: Malay, English)",
  "validation": "REQUIRED_NON_EMPTY_STRING",
  "required": true
}
```

    - Item 15:
```json
{
  "variable": "content_core",
  "query": "Masukkan Hook, USP, dan CTA utama.",
  "sub_fields": [
    "hook",
    "usp",
    "cta"
  ],
  "validation": "MIN_LENGTH_20_CHARS",
  "required": true
}
```

- **trajectory_level_alignment_script** (object):
  - **protocol_id** (string): `TLAS_V11_1`
  - **step_1_identity_handshake** (object):
    - **action** (string): `Lock product_id and avatar_id DNA`
    - **source** (string): `SATELLITE_03.archetypes`
    - **validation** (string): `ENFORCE: dna_stability_lock :: biometric_drift_threshold == 0.05`
  - **step_1b_headwear_style_wardrobe_compatibility** (object):
    - **action** (string): `Validate headwear_style and wardrobe against authoritative avatar compatibility registries`
    - **source** (string): `SATELLITE_03.headwear_wardrobe_compatibility_matrix + SATELLITE_03.archetypes`
    - **validation** (string): `ABORT IF headwear_style NOT IN SATELLITE_03.headwear_wardrobe_compatibility_matrix.[avatar_id].allowed_headwear OR wardrobe NOT IN SATELLITE_03.archetypes.[avatar_id].wardrobe_preference`
  - **step_1c_avatar_position_camera_mapping** (object):
    - **action** (string): `Validate avatar_position to camera_behavior compatibility`
    - **source** (string): `SATELLITE_04_MAPPING_MATRIX.avatar_position_camera_compatibility`
    - **validation** (string): `ABORT IF camera_behavior NOT IN SATELLITE_04_MAPPING_MATRIX.avatar_position_camera_compatibility.[avatar_position].allowed_camera_behaviors`
  - **step_2_deterministic_physics_class_resolution** (object):
    - **action** (string): `Resolve physics_class from explicit input with deterministic CLASS_GENERIC fallback only when empty`
    - **source** (string): `SATELLITE_03_VISUAL_DECK.props`
    - **validation** (string): `ABORT IF physics_class remains unresolved after fallback`
  - **step_3_bimodal_silo_lock** (object):
    - **action** (string): `Enforce Silo Vocabulary (Stealth vs. Direct)`
    - **source** (string): `SOVEREIGN_01_MASTER_SCHEMA.silo_vocabulary_authority`
    - **validation** (string): `FATAL_ERROR IF terminology_leak detected`
  - **step_4_deterministic_block_sharding** (object):
    - **action** (string): `Calculate Engine-Aware Sharding (BLOCK_N)`
    - **formula** (string): `IF engine_supports_multi_block THEN BLOCK_N = CEIL(duration_target / engine_block_limit) ELSE BLOCK_N = 1`
    - **source** (string): `SATELLITE_04_MAPPING_MATRIX.temporal_chaining_bridge`
    - **validation** (string): `ABORT IF engine_id IN [GROK, KLING_3_0] AND BLOCK_N > 1`
- **validation_guards** (array):
  - Item 1:
    `ABORT IF atomic_variables < 15`
  - Item 2:
    `ABORT IF product_type NOT IN [STEALTH, DIRECT]`
  - Item 3:
    `ABORT IF physics_class NOT IN [CLASS_A, CLASS_B, CLASS_C, CLASS_D, CLASS_E, CLASS_GENERIC]`
  - Item 4:
    `ABORT IF physics_class == 'AUTO_FETCH'`
  - Item 5:
    `ABORT IF trigger_id NOT IN [MARUAH_01, EGO_01, TRUST_01, CONFIDENCE_01]`
  - Item 6:
    `ABORT IF avatar_id NOT IN SATELLITE_03.archetypes`
  - Item 7:
    `ABORT IF headwear_style NOT IN [AUTO, HIJAB, NON_HIJAB]`
  - Item 8:
    `ABORT IF wardrobe NOT IN SATELLITE_03.wardrobe_collections`
  - Item 9:
    `ABORT IF avatar_position NOT IN SATELLITE_04_MAPPING_MATRIX.avatar_position_camera_compatibility`
  - Item 10:
    `ABORT IF camera_behavior NOT IN SATELLITE_03.camera_behavior`
  - Item 11:
    `ABORT IF scene_context NOT IN SATELLITE_03.scenes`
  - Item 12:
    `ABORT IF target_language == NULL OR target_language == ''`
  - Item 13:
    `ABORT IF headwear_style NOT IN SATELLITE_03.headwear_wardrobe_compatibility_matrix.[avatar_id].allowed_headwear`
  - Item 14:
    `ABORT IF wardrobe NOT IN SATELLITE_03.archetypes.[avatar_id].wardrobe_preference`
  - Item 15:
    `ABORT IF camera_behavior NOT IN SATELLITE_04_MAPPING_MATRIX.avatar_position_camera_compatibility.[avatar_position].allowed_camera_behaviors`
  - Item 16:
    `ABORT IF language_context_selector missing for target_language/product_type`
  - Item 17:
    `ABORT IF engine_id NOT IN [VEO_3_1, GROK, KLING_3_0, SEEDANCE_2_0]`
  - Item 18:
    `ABORT IF submode_formula NOT IN [PAS, HSO, AIDA, FAB, SAVAGE_HPAS]`
  - Item 19:
    `ABORT IF engine_id == VEO_3_1 AND duration_target NOT IN [4s, 6s, 8s, 16s, 24s, 32s, 40s, 48s, 56s]`
  - Item 20:
    `ABORT IF engine_id == VEO_3_1 AND duration_target > 56s`
  - Item 21:
    `ABORT IF engine_id == GROK AND duration_target NOT IN [6s, 10s]`
  - Item 22:
    `ABORT IF engine_id == KLING_3_0 AND duration_target NOT IN [3s, 5s, 10s, 15s]`
  - Item 23:
    `ABORT IF engine_id == SEEDANCE_2_0 AND duration_target NOT IN [5s, 10s, 15s]`
  - Item 24:
    `ENFORCE: Bimodal Lock Check (STEALTH vs DIRECT)`
  - Item 26:
    `VALIDATE: biometric_drift_threshold == 0.05`
  - Item 27:
    `VALIDATE: identity_softening_threshold == 0.02`
  - Item 28:
    `ABORT IF engine_id == GROK AND execution_submode == 'NANO BANANA'`
  - Item 29:
    `ABORT IF engine_id == GROK AND duration_target > 10s`
  - Item 30:
    `ABORT IF engine_id == KLING_3_0 AND duration_target > 15s`
  - Item 31:
    `ABORT IF GATE_095_VISUAL_DIALOGUE_ISOLATION fails`
  - Item 32:
    `ABORT IF GATE_096_SCENE_CONTEXT_AUTHORITY_LOCK fails`
  - Item 33:
    `ABORT IF GATE_092_WPS_RUNTIME_CHECK fails`
  - Item 34:
    `ABORT IF GATE_093_SILO_CONTAMINATION_SCRUB fails`
  - Item 35:
    `ABORT IF GATE_097_9_SECTION_VALIDATOR fails`
  - Item 36:
    `ABORT IF dialogue-derived noun, hook-derived noun, USP-derived noun, CTA-derived noun, or metaphor vocabulary is allowed to instantiate prop, packaging, object, background, or environment`
  - Item 37:
    `ABORT IF scene_context authority is overridden by dialogue-side or copywriting-side vocabulary`
  - Item 38:
    `ABORT IF dialogue vocabulary is used as visual scene completion authority`
  - Item 39:
    `ABORT IF metaphor or copywriting vocabulary is literalized into physical visual output`
  - Item 40:
    `ENFORCE: coaching output may shape dialogue only, never visual asset selection`
  - Item 41:
    `ABORT IF coaching_output_handoff_missing == true`
  - Item 42:
    `ENFORCE: scene_context remains sole authority for visual environment selection`
  - Item 43:
    `ENFORCE: Section_6 dialogue remains non-authoritative for Sections_1_2_3_4_5_7_8_9`
  - Item 44:
    `ENFORCE: 9-section output titles match BOSMAX v11.1 OMNI ENGINE VIDEO GENERATION SYSTEM.txt`
- **error_registry** (object):
  - **ERR_SILO_CONTAMINATION** (string): `Bimodal Isolation breach: Stealth/Direct overlap detected.`
  - **ERR_BIOMETRIC_DRIFT** (string): `Biometric drift exceeded 0.05 threshold. Execute @Image1_REFRESH.`
  - **ERR_SSOT_DURATION_CONFLICT** (string): `Input duration violates engine-specific block caps.`
  - **ERR_NANO_BANANA_BREACH** (string): `FORBIDDEN SUBMODE: Execution halted for engine GROK.`
  - **ERR_SCHEMA_MISMATCH** (string): `Schema version mismatch. Expected v11.1.`
  - **ERR_TOKEN_LIMIT_RISK** (string): `VEO duration above 56s is forbidden in fail-closed mode.`
  - **ABORT_WPS_VIOLATION** (string): `WPS runtime validation failed.`
  - **ERR_SECTION_COUNT_MISMATCH** (string): `Assembled output does not contain exactly 9 mandatory sections.`
  - **ERR_ORPHAN_TRIGGER** (string): `trigger_id failed to map to visual_bias.`
  - **ERR_INVALID_HEADWEAR_STYLE** (string): `Invalid headwear_style selection.`
  - **ERR_INVALID_WARDROBE** (string): `Invalid wardrobe selection.`
  - **ERR_INVALID_AVATAR_POSITION** (string): `Invalid avatar_position selection.`
  - **ERR_INVALID_CAMERA_BEHAVIOR** (string): `Invalid camera_behavior selection.`
  - **ERR_LANGUAGE_CONTEXT_MISSING** (string): `language_context_selector missing for target_language/product_type.`
  - **ABORT_VISUAL_COPY_LEAK** (string): `Visual output contains object, prop, packaging, environment, or background element derived from dialogue or copywriting.`
  - **ABORT_VISUAL_SCENE_OVERRIDE** (string): `Dialogue, hook, USP, CTA, or metaphor vocabulary attempted to override user-selected scene_context.`
  - **ABORT_DIALOGUE_TO_VISUAL_PROP_INSTANTIATION** (string): `Dialogue-only noun attempted to instantiate visual prop, packaging, object, background, or environment.`
  - **ABORT_METAPHOR_OBJECT_RENDER** (string): `Metaphor or copywriting vocabulary was literalized into physical visual output.`
- **gate_integration** (object):
  - **primary_gate** (string): `GATE_050_COACHING_LAYER`
  - **secondary_gates** (array):
    - Item 1:
      `GATE_055_BIMODAL_LOCK`
    - Item 2:
      `GATE_092_WPS_RUNTIME_CHECK`
    - Item 3:
      `GATE_093_SILO_CONTAMINATION_SCRUB`
    - Item 4:
      `GATE_094_SSOT_DUR_CHECK`
    - Item 5:
      `GATE_095_VISUAL_DIALOGUE_ISOLATION`
    - Item 6:
      `GATE_096_SCENE_CONTEXT_AUTHORITY_LOCK`
    - Item 7:
      `GATE_097_9_SECTION_VALIDATOR`
  - **gate_logic** (array):
    - Item 1:
      `IF GATE_050_COACHING_LAYER triggered THEN EXECUTE coaching_protocol_registry`
    - Item 2:
      `IF GATE_092_WPS_RUNTIME_CHECK fails THEN ABORT(ABORT_WPS_VIOLATION)`
    - Item 3:
      `IF GATE_093_SILO_CONTAMINATION_SCRUB fails THEN ABORT(ABORT_SILO_LEAK)`
    - Item 4:
      `IF GATE_095_VISUAL_DIALOGUE_ISOLATION fails THEN ABORT(ABORT_VISUAL_COPY_LEAK)`
    - Item 5:
      `IF GATE_096_SCENE_CONTEXT_AUTHORITY_LOCK fails THEN ABORT(ABORT_VISUAL_SCENE_OVERRIDE)`
    - Item 6:
      `IF GATE_097_9_SECTION_VALIDATOR fails THEN ABORT(ERR_SECTION_COUNT_MISMATCH)`
    - Item 7:
      `IF engine_supports_multi_block AND duration_target > engine_block_limit THEN EXECUTE deterministic_block_sharding`
    - Item 8:
      `IF coaching output attempts visual asset selection THEN ABORT(ABORT_VISUAL_COPY_LEAK)`
    - Item 9:
      `IF all validations pass THEN PROCEED TO 9_SECTION_GENERATION`
- **9_section_output_mandate** (object):
  - **mandate_id** (string): `MANDATE_V11_1`
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
