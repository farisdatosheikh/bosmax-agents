---
paths:
  - ".claude/skills/*.md"
  - "products/*.yaml"
  - "BOSMAX_*_v1.md"
---

# Cowork Operating Map

This rule loads when working on BOSMAX skills, product registry files, or authority files.

## Primary Surfaces

- First read surface: `.claude/BOSMAX_CURRENT_STATE.md`
- Historical audit surface: `.claude/BOSMAX-LOG.md`
- Product authority surface: `products/*.yaml`

## Required Skill Files

The BOSMAX Cowork surface expects these files to exist in `.claude/skills/`:

1. `bosmax-compliance-gate.md`
2. `bosmax-subject-dna.md`
3. `bosmax-scene-engine.md`
4. `bosmax-mode-c-executor.md`
5. `bosmax-script-generator.md`
6. `bosmax-product-registration.md`
7. `bosmax-bulk-generator.md`
8. `bosmax-requirement-analyst.md`
9. `bosmax-product-intelligence.md`
10. `bosmax-image-analyst.md`
11. `bosmax-video-analyst.md`
12. `bosmax-commercial-poster-director.md`

## Product Registry Notes

- `products/_SCHEMA.yaml` is the schema reference
- each live product authority sits in its own YAML file
- `scale_anchor_descriptor` remains mandatory per variant
- do not duplicate product truth into orchestration prose

## Pipeline Sequences

```text
Full Image Pipeline (VIDEO_SUPPORT):
User -> BOSMAX [PRE-FLIGHT] -> bosmax-subject-dna
     -> bosmax-scene-engine
     -> bosmax-compliance-gate -> bosmax-final-output-agent -> User

Full Image Pipeline (SELLING_POSTER):
User -> BOSMAX [PRE-FLIGHT] -> bosmax-subject-dna
     -> bosmax-commercial-poster-director (selected_module_stack)
     -> bosmax-scene-engine [ingests subject_dna + selected_module_stack]
     -> bosmax-compliance-gate -> bosmax-final-output-agent -> User

NOTE: bosmax-scene-engine must NOT be called for SELLING_POSTER until
selected_module_stack is non-null. ABORT if selected_module_stack is null.

Full Video Pipeline (Mode B, single block):
User -> BOSMAX [PRE-FLIGHT] -> bosmax-script-generator
     -> bosmax-compliance-gate -> bosmax-final-output-agent -> User

Full Video Pipeline (Mode B, multi-block):
User -> BOSMAX [PRE-FLIGHT: MULTI-BLOCK TRIGGERED]
     -> BOSMAX [MASTER NARRATIVE BRIEF -> user approval]
     -> bosmax-script-generator [Block 1..N]
     -> bosmax-compliance-gate
     -> bosmax-final-output-agent -> User

Full Video Pipeline (Mode C):
User -> BOSMAX [PRE-FLIGHT] -> bosmax-mode-c-executor
     -> bosmax-compliance-gate -> bosmax-final-output-agent -> User

Full Product + Bulk Pipeline:
User -> BOSMAX [PRE-FLIGHT] -> bosmax-product-registration
     -> BOSMAX [PRE-FLIGHT] -> bosmax-bulk-generator
     -> bosmax-compliance-gate -> bosmax-final-output-agent -> User
```
