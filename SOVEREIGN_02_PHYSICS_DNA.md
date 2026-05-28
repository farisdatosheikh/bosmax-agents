- **metadata** (object):
  - **file_id** (string): `SOVEREIGN_02_PHYSICS_DNA`
  - **schema_version** (string): `v11.1`
  - **version_handshake** (string): `v11.1_GRAND_MASTER_SKELETON`
  - **last_edit_date** (string): `2026-03-05`
  - **authority** (string): `SUPREME_SYSTEMS_ARCHITECT`
- **material_physics** (object):
  - **CLASS_A** (object):
    - **refractive_index** (number): `1.45`
    - **air_gap_numeric** (string): `2.0mm`
    - **grip_type** (string): `[PHYSICS_LOCK_MANDATORY] PRECISION_PINCH`
    - **hoi_protocol** (string): `[CRITICAL_RULE_NON_OVERRIDEABLE] KINEMATIC_DISENTANGLEMENT`
    - **collision_mesh** (string): `INTEGRITY_LOCK`
  - **CLASS_B** (object):
    - **refractive_index** (number): `1.33`
    - **air_gap_numeric** (string): `1.5mm`
    - **grip_type** (string): `FULL_PALM_WRAP`
    - **hoi_protocol** (string): `[CRITICAL_RULE_NON_OVERRIDEABLE] KINEMATIC_DISENTANGLEMENT`
    - **collision_mesh** (string): `INTEGRITY_LOCK`
  - **CLASS_C** (object):
    - **refractive_index** (number): `1.5`
    - **air_gap_numeric** (string): `2.0mm`
    - **grip_type** (string): `TWO_HAND_CARRY`
    - **physics_enforcement** (object):
```json
{
  "gravity_tension": 0.95,
  "inertia_weight": 0.88
}
```

  - **CLASS_D** (object):
    - **refractive_index** (number): `1.2`
    - **air_gap_numeric** (string): `4.0mm`
    - **grip_type** (string): `DRAPE_AND_DISPLAY`
    - **fabric_physics** (object):
```json
{
  "cloth_bleeding_prevention": "4mm_air-gap_lock"
}
```

  - **CLASS_E** (object):
    - **refractive_index** (number): `1`
    - **air_gap_numeric** (string): `0.0mm`
    - **grip_type** (string): `ZERO_GRIP_STATIC_ONLY`
    - **displacement** (string): `ZERO_TOLERANCE`
  - **CLASS_GENERIC** (object):
    - **refractive_index** (number): `1.33`
    - **air_gap_numeric** (string): `1.5mm`
    - **grip_type** (string): `FULL_PALM_WRAP`
    - **hoi_protocol** (string): `[CRITICAL_RULE_NON_OVERRIDEABLE] KINEMATIC_DISENTANGLEMENT`
    - **collision_mesh** (string): `INTEGRITY_LOCK`
    - **inheritance_note** (string): `Safe fallback profile mirroring CLASS_B to prevent ERR_UNDEF_REF`
- **physics_prose_translation** (object):
  - **CLASS_A** (object):
    - **prose** (string): `extremely small lip-balm sized object held using a precise pinch grip between finger pads`
  - **CLASS_B** (object):
    - **prose** (string): `handheld object stabilized with a full palm wrap grip`
  - **CLASS_C** (object):
    - **prose** (string): `two-hand supported object requiring balanced grip`
  - **CLASS_D** (object):
    - **prose** (string): `flexible fabric material responding naturally to gravity and airflow`
  - **CLASS_E** (object):
    - **prose** (string): `static object placed on surface without hand interaction`
  - **CLASS_GENERIC** (object):
    - **prose** (string): `standard handheld object using neutral grip physics identical to palm-stabilized handling`
- **i2v_stitch_guard** (object):
  - **protocol_id** (string): `I2V_STITCH_GUARD_v11.1`
  - **objective** (string): `Autonomous stitching of marketplace static assets into character HOI`
  - **surface_normal_alignment** (object):
    - **enabled** (boolean): `true`
    - **tolerance_degrees** (number): `0.5`
    - **validation** (string): `ABORT IF surface_normal_deviation > 0.5_degrees`
  - **refractive_index_lock** (object):
    - **CLASS_A** (number): `1.45`
    - **CLASS_B** (number): `1.33`
    - **CLASS_C** (number): `1.5`
    - **CLASS_D** (number): `1.2`
    - **CLASS_E** (number): `1`
    - **CLASS_GENERIC** (number): `1.33`
  - **static_product_to_grip_stitch** (object):
    - **enabled** (boolean): `true`
    - **air_gap_enforcement** (string): `MAINTAIN_CLASS_SPECIFIC_GAP`
    - **validation** (string): `ABORT IF product_floats > 0.5mm`
    - **depth_map_requirement** (string): `Spatial Layout Representations + Bounding Boxes`
- **physics_constants** (object):
  - **gravity_tension** (number): `0.95`
  - **inertia_weight** (number): `0.88`
  - **tremor_frequency** (object):
    - **female** (string): `15Hz_PHYSIOLOGICAL_TREMOR`
    - **male** (string): `10Hz_HEAVY_MASS_TREMOR`
  - **latency_lock** (object):
    - **target_ms** (number): `10`
    - **tolerance_ms** (number): `2`
    - **application** (string): `VISEME_AUDIO_SYNCHRONIZATION`
- **lighting_standards** (object):
  - **kelvin_lock** (string): `5600K`
  - **luminance_manifold** (string): `LOCK_LUMINANCE_LEVELS_PERSISTENT`
  - **wb_stabilization** (string): `STABILIZE_WB_5600K`
  - **illumination_lock_source** (string): `FETCH FROM SOVEREIGN_02_PHYSICS_DNA.lighting_standards`
- **oral_physics** (object):
  - **viseme_sync** (string): `10ms_latency_lock`
  - **tone_tokens** (array):
    - Item 1:
      `arrogant_drawl`
    - Item 2:
      `staccato`
    - Item 3:
      `whispered_confession`
  - **wps_target_default** (number): `1.6`
  - **wps_hard_max** (number): `2`
  - **wps_kill_switch** (number): `3`
- **biometric_thresholds** (object):
  - **drift** (number): `0.05`
  - **identity_softening** (number): `0.02`
- **error_registry** (object):
  - **ERR_INVALID_PHYSICS_CLASS** (string): `Invalid physics_class value.`
  - **ERR_AIR_GAP_VIOLATION** (string): `Air-gap violation detected.`
  - **ERR_HOI_INTEGRITY_FAILURE** (string): `HOI integrity failure detected.`
  - **ERR_DIGIT_BLENDING** (string): `Finger-product mesh fusion detected. Enforce COLLISION_MESH_INTEGRITY.`
  - **ERR_VERTEX_DRIFTING** (string): `Vertex drifting detected.`
  - **ERR_KELVIN_DRIFT** (string): `Kelvin drift detected.`
  - **ERR_SEMANTIC_MERGING** (string): `Semantic merging detected.`
  - **ERR_BIOMETRIC_DRIFT** (string): `Biometric drift exceeded 0.05 threshold. Execute @Image1_REFRESH.`
  - **ERR_IDENTITY_SOFTENING** (string): `Identity softening threshold exceeded.`
  - **ERR_METADATA_LEAK** (string): `Metadata leak detected.`
  - **ERR_SSOT_DURATION_CONFLICT** (string): `Input duration not in engine-specific allowed list.`
  - **ERR_SCHEMA_MISMATCH** (string): `Schema version mismatch.`
  - **ERR_UNDEF_REF** (string): `Undefined reference.`
  - **FAIL_CLOSED_BIOMETRIC_DRIFT** (string): `Biometric drift threshold exceeded. Abort pipeline.`
  - **ERR_ENGINE_VERSION_MISMATCH** (string): `Engine version does not match BOSMAX v11.1 standards.`
  - **ERR_SEEDANCE_NOT_CONFIGURED** (string): `Seedance 2.0 selected but not configured in manifest.`
  - **ERR_KLING_HEURISTIC_VIOLATION** (string): `Kling 3.0 parameters exceed SSOT physical thresholds.`
  - **ERR_NANO_BANANA_BREACH** (string): `Forbidden submode (NANO BANANA) detected for engine GROK.`
- **validation_guards** (array):
  - Item 1:
    `ABORT IF physics_class NOT IN [CLASS_A, CLASS_B, CLASS_C, CLASS_D, CLASS_E, CLASS_GENERIC]`
  - Item 2:
    `ABORT IF air_gap < class_specific_minimum`
  - Item 3:
    `ABORT IF refractive_index != class_specific_value`
  - Item 4:
    `ABORT IF surface_normal_deviation > 0.5_degrees`
  - Item 5:
    `ABORT IF product_floats > 0.5mm`
  - Item 6:
    `ABORT IF digit_blending == TRUE`
  - Item 7:
    `ENFORCE: 2.0mm air-gap for CLASS_A`
  - Item 8:
    `ENFORCE: 1.5mm air-gap for CLASS_B`
  - Item 9:
    `ENFORCE: 2.0mm air-gap for CLASS_C`
  - Item 10:
    `ENFORCE: 4.0mm air-gap for CLASS_D`
  - Item 11:
    `ENFORCE: 0.0mm air-gap for CLASS_E`
  - Item 12:
    `ENFORCE: 1.5mm air-gap for CLASS_GENERIC`
  - Item 13:
    `ENFORCE: KINEMATIC_DISENTANGLEMENT on all CLASS_A/CLASS_B interactions`
  - Item 14:
    `ENFORCE: collision_mesh_integrity on all HOI`
  - Item 15:
    `ENFORCE: collision_mesh_integrity on all CLASS_A/CLASS_B interactions`
  - Item 16:
    `ABORT IF vertex_drifting == TRUE`
  - Item 17:
    `ABORT IF kelvin_drift > 50K`
  - Item 18:
    `ABORT IF semantic_merging == TRUE`
  - Item 19:
    `ENFORCE: 15Hz_PHYSIOLOGICAL_TREMOR (F)`
  - Item 20:
    `ENFORCE: 10Hz_HEAVY_MASS_TREMOR (M)`
  - Item 21:
    `ENFORCE: 10ms_latency_lock for viseme_sync`
  - Item 22:
    `ENFORCE: WPS_density <= 2.0 per scene interval (3.0 retained as absolute kill-switch)`
  - Item 23:
    `VALIDATE: lighting_standards.kelvin_lock == 5600K`
  - Item 24:
    `ENFORCE: schema_version == v11.1`
  - Item 25:
    `VALIDATE: version_handshake == v11.1_GRAND_MASTER_SKELETON`
  - Item 26:
    `ENFORCE: dna_reinjection_hop == 1 for every block boundary`
  - Item 27:
    `ENFORCE: supported_engines INCLUDE [VEO_3_1, SORA_2, KLING_3_0, SEEDANCE_2_0, GROK]`
  - Item 28:
    `VALIDATE: biometric_drift_threshold == 0.05 per SOV_03 Section 7`
  - Item 29:
    `VALIDATE: identity_softening_threshold == 0.02 per SOV_03 Section 7`
  - Item 30:
    `--- SSOT ENGINE HARD LOCKS ---`
  - Item 31:
    `ABORT IF engine_id == KLING_3_0 AND duration_target > 15s`
  - Item 32:
    `ABORT IF engine_id == SEEDANCE_2_0 AND duration_target > 20s`
  - Item 33:
    `ABORT IF engine_id == GROK AND duration_target NOT IN [6s, 10s]`
  - Item 34:
    `ABORT IF engine_id == GROK AND execution_submode == 'NANO BANANA'`
  - Item 35:
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
