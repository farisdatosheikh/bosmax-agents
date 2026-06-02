# BOSMAX PROMPT SELF-HEALING CHECKLISTS v1

Authority file for operator-side reminder prompts when an AI returns a weak,
wrong, incomplete, drifted, or non-compliant image/video prompt and the user
does not want to explain every error manually.

Purpose:
- user copy-pastes one reminder checklist
- AI must self-audit the previous prompt/output
- AI must troubleshoot and refine the prompt itself
- AI must not ask the user to list every mistake one by one unless a real
  blocker remains

---

## 1. Universal Law

Use these reminder checklists when:
- the AI ignored the uploaded image
- the AI drifted to the wrong avatar or wrong product
- the AI ignored scale truth or packaging truth
- the AI skipped storyboard or block math
- the AI exceeded WPS budget or made the pacing slow
- the AI returned one monolithic video prompt where block prompts were required
- the AI produced generic, internship-grade, or low-density commercial output

Hard law:
- the AI must diagnose its own mistakes first
- the AI must compare the previous prompt against the user request and the
  uploaded image/reference
- the AI must return the corrected prompt directly
- the AI must not ask the user to repeat obvious information already present in
  the image, previous prompt, or request

---

## 2. IMAGE Reminder Checklist Prompt

User copies this when the image prompt is wrong.

```text
SELF-HEAL IMAGE PROMPT MODE — ACTIVATED

Do not ask me to explain all the mistakes one by one.
Your job now is to self-audit the previous image prompt and repair it properly.

Use this enforcement chain:

1. Re-read my original request.
2. Re-scan the uploaded image/reference as the highest authority.
3. Compare your previous prompt against:
   - avatar identity truth
   - product identity truth
   - packaging truth
   - scale truth
   - scene / framing truth
   - platform use case
4. List the mistakes you detect yourself.
5. Fix the prompt fully and return the corrected final prompt only.

Mandatory self-check:
- Did you ignore the uploaded image?
- Did you drift to the wrong avatar/persona?
- Did you drift to the wrong product or registry default?
- Did you change packaging shape, cap, label, or colour?
- Did you inflate or shrink the product scale incorrectly?
- Did you output a generic poster instead of the requested image type?
- Did you weaken the selling hierarchy or visual hierarchy?
- Did you fail to preserve readable branding / label logic?
- Did you forget negative locks?

Rules:
- uploaded image/reference wins over session memory and registry defaults
- do not ask me to restate what is already clear in the image
- do not output analysis only
- return one corrected production-grade image prompt
- if needed, include stronger negative locks and scale anchors automatically
```

---

## 3. VIDEO Reminder Checklist Prompt

User copies this when the video prompt is wrong.

```text
SELF-HEAL VIDEO PROMPT MODE — ACTIVATED

Do not ask me to explain all the mistakes one by one.
Your job now is to self-audit the previous video prompt and repair it properly.

Use this enforcement chain:

1. Re-read my original request.
2. Re-scan the uploaded image/reference as the highest authority if one was provided.
3. Re-check engine, duration, and platform.
4. Rebuild storyboard and block math if required.
5. Recalculate WPS budget and pacing.
6. Compare your previous prompt against the required video contract.
7. Return the corrected block prompts directly.

Mandatory self-check:
- Did you ignore the uploaded image/reference?
- Did you drift to the wrong avatar/persona?
- Did you drift to the wrong product or registry default?
- Did you skip storyboard before writing the prompt?
- Did you skip engine block math?
- Did you return one monolithic prompt when separate blocks were required?
- Did you exceed safe WPS budget?
- Did you make the pacing too slow or leave too much dead air?
- Did you fail to preserve product scale, packaging, and framing continuity?
- Did you forget dialogue authority / stealth rules / negative locks?

Mandatory repair rules:
- For multi-block video, return:
  - storyboard summary
  - block distribution
  - corrected block prompt 1
  - corrected block prompt 2
  - continue for all blocks if more than 2
- For GROK 16s, use 10s + 6s unless a different valid split is explicitly confirmed
- Use brisk UGC pace by default for recommendation-style TikTok videos
- Remove dead air, filler pauses, and weak low-density dialogue
- Keep uploaded image/reference as the top authority for identity, product truth, crop class, and scale
- Do not ask me to repeat obvious data already visible in the image or request
- Do not output theory only
- Return the corrected production-grade video prompt set
```

---

## 4. Fast Failure Classes

Use these internally when repairing:

### IMAGE failure classes
- `IDENTITY_DRIFT`
- `PRODUCT_DRIFT`
- `PACKAGING_DRIFT`
- `SCALE_DRIFT`
- `HIERARCHY_WEAK`
- `NEGATIVE_LOCK_MISSING`
- `WRONG_IMAGE_MODE`

### VIDEO failure classes
- `VISUAL_AUTHORITY_IGNORED`
- `PRODUCT_OR_AVATAR_FALLBACK_DRIFT`
- `STORYBOARD_SKIPPED`
- `BLOCK_MATH_INVALID`
- `WPS_OVER_BUDGET`
- `PACE_TOO_SLOW`
- `CONTINUITY_DRIFT`
- `DIALOGUE_AUTHORITY_BROKEN`

---

## 5. Operator Rule

If the first prompt is wrong:
- use the `IMAGE Reminder Checklist Prompt` for image work
- use the `VIDEO Reminder Checklist Prompt` for video work

This is a repair accelerator.
It exists so the operator does not waste time writing a long complaint for basic
AI mistakes that should have been self-diagnosed.
