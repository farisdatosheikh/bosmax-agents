- **metadata** (object):
  - **file_id** (string): `SATELLITE_02_LINT_NEGATIVES`
  - **schema_version** (string): `v11.1`
  - **version_handshake** (string): `v11.1_GRAND_MASTER_SKELETON`
  - **last_edit_date** (string): `2026-03-05`
  - **authority** (string): `SUPREME_SYSTEMS_ARCHITECT`
- **negative_prompt_registry** (object):
  - **KLING_3_0_KILL_LIST** (object):
    - **vertex_drifting** (string): `[mesh_jitter]`
    - **digit_blending** (string): `[fused_fingers]`
    - **kelvin_drift** (string): `[color_shift]`
    - **semantic_merging** (string): `[object_absorption]`
    - **additional_negatives** (array):
```json
[
  "no background artifacts",
  "no lens flares",
  "no UI elements",
  "no extra fingers",
  "no deformed hands",
  "no melting edges",
  "no fused objects"
]
```

  - **SEEDANCE_2_0_KILL_LIST** (object):
    - **vertex_drifting** (string): `[latent_drift]`
    - **digit_blending** (string): `[digit_merging]`
    - **kelvin_drift** (string): `[temp_instability]`
    - **semantic_merging** (string): `[texture_leak]`
    - **additional_negatives** (array):
```json
[
  "no texture pop-in",
  "no flickering pores",
  "no fabric morphing",
  "no extra fingers",
  "no deformed hands"
]
```

  - **VEO_3_1_KILL_LIST** (object):
    - **vertex_drifting** (string): `[temporal_instability]`
    - **digit_blending** (string): `[hand_artifacts]`
    - **kelvin_drift** (string): `[wb_drift]`
    - **semantic_merging** (string): `[prompt_bleed]`
    - **additional_negatives** (array):
```json
[
  "no frame inconsistencies",
  "no identity drift",
  "no motion blur artifacts",
  "no viseme desync"
]
```

  - **SORA_2_KILL_LIST** (object):
    - **vertex_drifting** (string): `[physics_hallucination]`
    - **digit_blending** (string): `[mesh_fusion]`
    - **kelvin_drift** (string): `[lighting_inconsistency]`
    - **semantic_merging** (string): `[causality_break]`
    - **additional_negatives** (array):
```json
[
  "no physical impossibilities",
  "no fluid simulation errors",
  "no temporal paradoxes",
  "no stitching artifacts"
]
```

  - **GROK_KILL_LIST** (object):
    - **vertex_drifting** (string): `[temporal_instability]`
    - **digit_blending** (string): `[identity_drift]`
    - **kelvin_drift** (string): `[prompt_bleed]`
    - **semantic_merging** (string): `[background_hallucination]`
    - **logic_lock** (string): `FORBID_NANO_BANANA_TOKENS`
    - **additional_negatives** (array):
```json
[
  "no background artifacts",
  "no identity drift",
  "no short-form instability",
  "no google_gemini_artifacts"
]
```

  - **global_anti_morph** (array):
    - Item 1:
      `[vertex_drifting]`
    - Item 2:
      `[mesh_jitter]`
    - Item 3:
      `[digit_merging]`
    - Item 4:
      `[fused_fingers]`
    - Item 5:
      `[identity_drift]`
    - Item 6:
      `[background_hallucination]`
    - Item 7:
      `[texture_leak]`
    - Item 8:
      `[prompt_bleed]`
  - **visual_copy_contamination_kill_list** (object):
    - **semantic_merging** (string): `[dialogue_to_visual_instantiation]`
    - **metaphor_literalization** (string): `[metaphor_object_render]`
    - **scene_override** (string): `[scene_context_override]`
    - **additional_negatives** (array):
```json
[
  "do not render spoken nouns as physical props",
  "do not convert dialogue keywords into objects",
  "do not literalize metaphor language into products, packaging, tools, fertilizer bags, plants, engines, or environmental assets",
  "background and props must follow selected scene_context only",
  "ignore hook, USP, CTA, and dialogue nouns for object generation",
  "do not add agriculture, workshop, medical, or mechanical objects unless explicitly present in scene_context",
  "no dialogue-driven prop generation",
  "no copywriting-driven background completion"
]
```

- **engine_block_limits** (object):
  - **KLING_3_0** (object):
    - **max_duration_seconds** (number): `15`
  - **SEEDANCE_2_0** (object):
    - **max_duration_seconds** (number): `20`
  - **VEO_3_1** (object):
    - **max_block_seconds** (number): `8`
  - **SORA_2** (object):
    - **max_block_seconds** (number): `15`
  - **GROK** (object):
    - **max_duration_seconds** (number): `10`
- **metadata_leak_prevention** (object):
  - **pattern_source** (string): `FETCH_FROM MASTER_IGNITION_TEMPLATE.output_cleanroom_protocol.sanitizer`
  - **enforce_stage** (array):
    - Item 1:
      `PRE_ASSEMBLY`
    - Item 2:
      `POST_ASSEMBLY`
  - **uuid_pattern** (string): `\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\b`
  - **system_id_pattern** (object):
    - **hex_16plus** (string): `\b[0-9a-fA-F]{16,}\b`
    - **numeric_12plus** (string): `\b\d{12,}\b`
    - **job_id_format** (string): `\b(job|run|request|trace)_[a-zA-Z0-9]{8,}\b`
  - **debug_marker_pattern** (object):
    - **log_levels** (string): `\[(DEBUG|TRACE|INFO|WARN|ERROR)\]`
    - **underscore_markers** (string): `__DEBUG__[\s\S]*?__END_DEBUG__`
    - **bracket_markers** (string): `<DEBUG>[\s\S]*?</DEBUG>`
  - **placeholder_pattern** (string): `\{\{[^}]+\}\}`
  - **actions** (object):
    - **on_uuid_match** (string): `REMOVE`
    - **on_system_id_like_match** (string): `REWRITE_TO_PLACEHOLDER_AND_AUDIT`
    - **on_debug_marker_match** (string): `REMOVE_AND_AUDIT`
    - **on_placeholder_match** (string): `FAIL_CLOSED_IF_UNRESOLVED`
  - **audit_log** (string): `ENABLED`
- **surgical_scrub_v2** (object):
  - **enabled** (boolean): `true`
  - **pre_transform_purge** (boolean): `true`
  - **deny_fields** (array):
    - Item 1:
      `raw_id`
    - Item 2:
      `system_id`
    - Item 3:
      `internal_id`
    - Item 4:
      `uuid`
    - Item 5:
      `trace_id`
    - Item 6:
      `generation_id`
  - **pattern_regex** (string): `FETCH_FROM MASTER_IGNITION_TEMPLATE.output_cleanroom_protocol.sanitizer`
  - **action** (string): `FAIL_CLOSED_ON_METADATA_LEAK`
- **suppress_markers** (object):
  - **description** (string): `Canonical list of internal tokens and tags to remove/suppress before output.`
  - **tokens** (array):
    - Item 1:
      `SSOT_INTERNAL`
    - Item 2:
      `BOSMAX_HEURISTIC`
    - Item 3:
      `EXTERNAL_ENGINE_ADDED`
    - Item 4:
      `PHYSICS_LOCK_MANDATORY`
    - Item 5:
      `CRITICAL_RULE_NON_OVERRIDEABLE`
    - Item 6:
      `CTX_`
    - Item 7:
      `SHOT_`
    - Item 8:
      `PROP_`
    - Item 9:
      `TRG_`
    - Item 10:
      `DNA_`
    - Item 11:
      `SCRIPT_`
    - Item 12:
      `CAM_`
    - Item 13:
      `CLASS_`
    - Item 14:
      `W_`
    - Item 15:
      `TEMP_`
  - **enforcement** (object):
    - **pre_assembly** (string): `REMOVE_AND_REWRITE`
    - **post_assembly** (string): `SANITIZE_AND_ABORT_IF_UNREWRITABLE`
- **linguistic_guards** (object):
  - **pronoun_policy** (object):
    - **stealth** (object):
```json
{
  "forbidden_pronouns": [
    "saya",
    "anda",
    "awak",
    "kamu"
  ],
  "allowed_pronouns": [
    "aku",
    "kau",
    "jantan",
    "bro",
    "abang",
    "kita"
  ]
}
```

    - **direct** (object):
```json
{
  "forbidden_pronouns": [
    "aku",
    "kau",
    "lu",
    "gua",
    "weh",
    "doh",
    "abang"
  ],
  "allowed_pronouns": [
    "saya",
    "anda",
    "kita",
    "tuan",
    "puan"
  ]
}
```

- **silo_vocabulary_scrubbing** (object):
  - **STEALTH_SILO_SCRUB** (object):
    - **forbidden_pronouns** (array):
```json
[
  "saya",
  "anda",
  "awak",
  "kamu"
]
```

    - **allowed_pronouns** (array):
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

    - **forbidden_claims** (array):
```json
[
  "cure",
  "treat",
  "heal",
  "ubat kuat",
  "kapsul",
  "pills",
  "supplement"
]
```

    - **allowed_alternatives** (array):
```json
[
  "SUPPORT",
  "MAINTAIN",
  "PROMOTE_HEALTHY",
  "BOOSTER",
  "FORMULA",
  "IKHTIAR"
]
```

  - **DIRECT_SILO_SCRUB** (object):
    - **forbidden_pronouns** (array):
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

    - **allowed_pronouns** (array):
```json
[
  "saya",
  "anda",
  "kita",
  "tuan",
  "puan"
]
```

    - **forbidden_claims** (array):
```json
[
  "jaminan kualiti",
  "100% berkesan",
  "tanpa kesan sampingan"
]
```

    - **allowed_alternatives** (array):
```json
[
  "REVENUE_POTENTIAL",
  "DIVERSIFIED_STREAMS",
  "GROWTH_STRATEGY"
]
```

- **technical_marker_suppression** (object):
  - **enabled** (boolean): `true`
  - **suppress_markers** (array):
    - Item 1:
      `CTX_`
    - Item 2:
      `SHOT_`
    - Item 3:
      `PROP_`
    - Item 4:
      `TRG_`
    - Item 5:
      `DNA_`
    - Item 6:
      `SCRIPT_`
    - Item 7:
      `CAM_`
    - Item 8:
      `CLASS_`
    - Item 9:
      `W_`
    - Item 10:
      `TEMP_`
    - Item 11:
      `[SSOT_INTERNAL]`
    - Item 12:
      `[BOSMAX_HEURISTIC]`
    - Item 13:
      `[EXTERNAL_ENGINE_ADDED]`
    - Item 14:
      `[PHYSICS_LOCK_MANDATORY]`
    - Item 15:
      `[CRITICAL_RULE_NON_OVERRIDEABLE]`
  - **suppress_patterns** (array):
    - Item 1:
      `[START_TIME - END_TIME]`
    - Item 2:
      `{{user_hook}}`
    - Item 3:
      `{{user_usp}}`
    - Item 4:
      `{{user_cta}}`
    - Item 5:
      `[[FETCH_FROM_SSOT]]`
    - Item 6:
      `<<INJECT_DNA>>`
  - **semantic_token_suppression** (object):
    - **enabled** (boolean): `true`
    - **patterns** (array):
```json
[
  "\\bSCN_[0-9]{3}\\b",
  "\\bCAM_[0-9]{3}\\b",
  "\\bCLASS_[A-E]\\b",
  "\\bPREDATOR_CORE\\b",
  "\\bAUTHENTIC_WHISPER\\b",
  "\\bUGC_IPHONE_RAW\\b",
  "\\bCINEMATIC_PRO\\b",
  "\\bSORA block\\b",
  "\\bVEO block\\b",
  "\\bGROK block\\b",
  "\\bKLING block\\b",
  "\\bSEEDANCE block\\b",
  "\\bGAUM\\b",
  "\\bPACAK\\b",
  "\\bSUBUR\\b",
  "\\bHARDNESS\\b",
  "\\bDOMINANCE\\b"
]
```

    - **action** (string): `REWRITE_TO_PROSE_CONTEXT`
- **error_registry** (object):
  - **ERR_NEGATIVE_PROMPT_MISSING** (string): `Negative prompt registry is empty.`
  - **ERR_METADATA_LEAK_DETECTED** (string): `Metadata leak detected in output.`
  - **ERR_UUID_NOT_PURGED** (string): `UUID pattern not purged.`
  - **ERR_SYSTEM_ID_LEAK** (string): `System ID pattern detected.`
  - **ERR_DEBUG_MARKER_FOUND** (string): `Debug marker found in output.`
  - **ERR_PLACEHOLDER_NOT_FILLED** (string): `Unresolved placeholder detected.`
  - **ERR_SILO_VOCAB_VIOLATION** (string): `Silo vocabulary violation detected.`
  - **ERR_PRONOUN_LEAK** (string): `Forbidden pronoun detected.`
  - **ERR_MEDICAL_CLAIM_LEAK** (string): `Medical claim detected in Stealth mode.`
  - **ERR_SSOT_VIOLATION** (string): `SSOT violation detected.`
  - **ERR_SCHEMA_MISMATCH** (string): `Schema version mismatch.`
  - **ERR_UNDEF_REF** (string): `Undefined reference.`
  - **ERR_DIALOGUE_TO_VISUAL_INSTANTIATION** (string): `Dialogue-only noun triggered visual prop, object, packaging, or environment generation.`
  - **ERR_METAPHOR_OBJECT_RENDER** (string): `Metaphor or copywriting vocabulary was literalized into physical visual output.`
  - **ERR_SCENE_CONTEXT_OVERRIDE** (string): `Dialogue or copywriting vocabulary attempted to override selected scene_context.`
  - **FAIL_CLOSED_BIOMETRIC_DRIFT** (string): `Biometric drift threshold exceeded. Abort pipeline.`
  - **FAIL_CLOSED_ON_METADATA_LEAK** (string): `Metadata leak detected. Strip sensitive tokens and fail closed.`
  - **ERR_ENGINE_VERSION_MISMATCH** (string): `Engine version does not match BOSMAX v11.1 standards.`
  - **ERR_SEEDANCE_NOT_CONFIGURED** (string): `Seedance 2.0 selected but not configured in manifest.`
  - **ERR_KLING_HEURISTIC_VIOLATION** (string): `Kling 3.0 parameters exceed SSOT physical thresholds.`
- **validation_guards** (array):
  - Item 1:
    `ABORT IF negative_prompt_registry == EMPTY`
  - Item 2:
    `ABORT IF metadata_leak_prevention.pattern_source == EMPTY`
  - Item 3:
    `ABORT IF surgical_scrub_v2.enabled == false`
  - Item 4:
    `ENFORCE: pre_transform_purge == true`
  - Item 5:
    `VALIDATE: silo_vocabulary_scrubbing alignment per SOVEREIGN_01`
  - Item 6:
    `ENFORCE: STEALTH_SILO_SCRUB forbidden_pronouns (4 pronouns)`
  - Item 7:
    `ENFORCE: DIRECT_SILO_SCRUB forbidden_pronouns (7 pronouns)`
  - Item 8:
    `ABORT IF suppress_markers == EMPTY`
  - Item 9:
    `ENFORCE: suppress_markers INCLUDE CTX_, SHOT_, CAM_, CLASS_, W_, TEMP_`
  - Item 10:
    `VALIDATE: engine_kill_lists alignment per SSOT Forensic Audit`
  - Item 11:
    `ENFORCE: KLING_3_0_KILL_LIST hard_lock == 15s`
  - Item 12:
    `ENFORCE: SEEDANCE_2_0_KILL_LIST hard_lock == 20s`
  - Item 13:
    `ENFORCE: GROK_KILL_LIST hard_lock == 10s`
  - Item 14:
    `ENFORCE: GROK_KILL_LIST forbids NANO_BANANA tokens`
  - Item 15:
    `VALIDATE: biometric_drift_threshold == 0.05 per SOV_03 Section 7`
  - Item 16:
    `VALIDATE: identity_softening_threshold == 0.02 per SOV_03 Section 7`
  - Item 17:
    `VALIDATE: duration_target must resolve against engine-specific allowed values from MASTER_IGNITION_TEMPLATE`
  - Item 18:
    `ENFORCE: 9-section output titles match BOSMAX v11.1 OMNI ENGINE VIDEO GENERATION SYSTEM.txt`
  - Item 19:
    `ABORT IF dialogue-only noun triggers visual prop, packaging, object, background, or environment generation`
  - Item 20:
    `ABORT IF hook, USP, CTA, problem, agitate, solution, or dialogue vocabulary is used for visual asset completion`
  - Item 21:
    `ABORT IF metaphor vocabulary is literalized into fertilizer bags, tools, machines, plants, roots, soil, engines, signals, or medical objects`
  - Item 22:
    `ABORT IF selected scene_context is overridden by dialogue or copywriting vocabulary`
  - Item 23:
    `ENFORCE: visual asset generation must follow selected scene_context only`
  - Item 24:
    `ENFORCE: visual_copy_contamination_kill_list additional_negatives must be injected into final engine negative prompt`
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
