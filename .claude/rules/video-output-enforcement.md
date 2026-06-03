---
paths:
  - ".claude/skills/bosmax-script-generator.md"
  - ".claude/skills/bosmax-mode-c-executor.md"
  - ".claude/skills/bosmax-compliance-gate.md"
  - "BOSMAX_*VIDEO*.md"
  - "BOSMAX_HARD_ENGINE_CONTRACTS_v1.md"
  - "BOSMAX_CHATGPT_CLEAN_VIDEO_ROLE_MODEL_v1.md"
  - "BOSMAX_GROK_EXTENSION_SEAM_TEMPLATES_v1.md"
---

# Video Output Enforcement Supplement

Load this rule when editing or invoking the BOSMAX video generation and video audit lanes.

## Pre-Output Enforcement Checklist

```text
VISUAL ENFORCEMENT
☐ Visual scan complete
☐ Avatar source locked to USER_UPLOAD if human image exists
☐ Product source derived from uploaded image if packaging is clear
☐ No registry fallback override against visual evidence

SANDBOX ENFORCEMENT
☐ If registry miss + visual evidence clear -> visual-first sandbox active
☐ MINI-INTAKE asks only for fields not already proven by visual evidence
☐ No redundant category / packaging / cm questions if visual truth is enough
☐ sandbox_product_record or product_record is non-null before route dispatch

VIDEO ENFORCEMENT
☐ Engine confirmed
☐ Block math confirmed
☐ Storyboard presented
☐ Storyboard approved
☐ WPS budget declared per block
☐ pace_class declared
☐ BM commercial / UGC / recommendation video includes dialog unless explicitly waived
☐ GROK blocks stay at 6s or 10s only
☐ If image reference exists, persistence locks are declared

OUTPUT ENFORCEMENT
☐ Prompt follows uploaded visual truth
☐ Prompt follows actual packaging / scale / product class
☐ Dialog fits block duration
☐ No dead-air pacing that conflicts with content type
```

## Kill Switch

If any checklist item fails:

- do not emit the prompt
- abort, revise, or ask the exact missing question

## Output Shape Reminder

- keep operator-facing video output clean
- do not leak internal scaffolding or debug metadata
- for multi-block GROK, bridge continuity is mandatory
