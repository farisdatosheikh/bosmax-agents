# BOSMAX CHATGPT CLEAN VIDEO ROLE MODEL v1

Authority file for operator-facing video prompt structure.

Purpose:
- make ChatGPT-style clean prompt output the canonical role model
- stop Claude-style metadata leakage
- stop Grok extension lag from late dialogue restarts

---

## 1. Why This Exists

ChatGPT-style BOSMAX outputs are currently the cleanest operator-facing shape:
- visual scan first
- engine contract second
- storyboard third
- block prompts after that
- minimal debug noise
- no leaked internal scaffolding

This file makes that shape canonical.

---

## 2. Required Output Shape

For operator-facing final video prompt output, use this order:

1. `VISUAL SCAN COMPLETE`
2. `[ENGINE] ENGINE CONTRACT`
3. `STORYBOARD`
4. `BLOCK 1 PROMPT` or `COPY-PASTE PROMPT` jika single-block
5. `BLOCK 2 PROMPT` and later blocks if needed

Do not front-load the final answer with:
- internal governance chatter
- redundant blocker talk
- hidden system labels
- debug-style scaffolding the operator does not need

---

## 3. Clean Output Rules

Mandatory:
- language clear
- duration clear
- block math clear
- full storyboard first
- WPS budget clear
- pace_class clear
- copy_formula clear
- product truth clear
- final prompt immediately usable
- no text overlay content

Forbidden in operator-facing output:
- `metadata_json_handoff`
- `validation_flags`
- `rule_id`
- `layer_b`
- `safe_zone`
- `product_scale_class`
- raw token families
- internal control prose that is useful only to BOSMAX internals

---

## 4. GROK Block-2 Continuity Rule

For `GROK` multi-block commercial UGC video:
- Block 2 must feel like a real continuation, not a reset
- dialogue should resume within the first `0.5s–1.0s`
- do not spend the first `2s–3s` on silent product action unless explicitly requested
- opening movement should be micro-continuity only:
  - slight tilt
  - slight nod
  - slight hand adjustment
  - small return-to-camera motion

Bad seam:
- Block 1 ends speaking
- Block 2 opens with long silent action
- dialogue only starts much later
- lipsync feels late or detached

Good seam:
- Block 1 ends with speech near final frame
- Block 2 opens from the same pose
- speech resumes almost immediately
- action supports the speech instead of delaying it
- the same spoken idea is still moving across the seam

For `GROK` duration defaults:
- `20s` must default to `2 x 10s`
- `30s` must default to `3 x 10s`
- do not output monolithic 20s/30s prompts
- only use alternate distributions if the operator explicitly requests them

---

## 4B. No Overlay Absolute Rule

For BOSMAX video outputs:
- no text overlay
- no CTA badges
- no subtitles styling instructions
- no safe-zone coordinate mapping

If the operator wants overlay planning, that must be a separate post-production task,
not part of the video generation prompt.

---

## 5. BM Commercial UGC Dialogue Rule

If the request is:
- BM
- commercial
- recommendation
- TikTok UGC

then:
- dialogue is mandatory
- natural conversational Malay is preferred
- practical spoken rhythm beats premium cinematic silence
- default copy formula must be declared:
  - `SELL_THROUGH_HPFRC` for direct-response selling
  - `STORY_HSARC` for softer storytelling with conversion intent

Minimum commercial copy payload:
- hook in the first spoken line
- pain or friction before the payoff
- one concrete reason-to-believe
- CTA

`pure visual` only if the user explicitly wants:
- silent montage
- music-only
- text-only sequence

---

## 6. Adoption Rule

Use this file as the role model whenever:
- ChatGPT output is clearly better than Claude/Grok/Gemini output shape
- the operator wants cleaner, more direct, more copy-paste-ready prompts
- multi-block Grok prompts need tighter seam continuity
- BM UGC dialogue needs stronger sell-through structure
