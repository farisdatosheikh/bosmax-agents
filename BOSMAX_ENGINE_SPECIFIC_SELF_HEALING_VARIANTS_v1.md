# BOSMAX ENGINE-SPECIFIC SELF-HEALING VARIANTS v1

Authority file for engine-tuned repair reminder prompts.

Use this layer after `BOSMAX_PROMPT_SELF_HEALING_CHECKLISTS_v1.md` when the
operator wants a harder repair prompt tailored to the specific AI engine that
failed.

---

## 1. Purpose

Universal self-healing prompts are useful, but some failures are engine-shaped:
- `ChatGPT` often needs stronger commercial density and stricter anti-generic enforcement
- `Gemini` often needs stronger scale, packaging, and anti-hero-object enforcement
- `Grok` often needs stronger visual persistence, storyboard, block math, and pace enforcement

This file gives the operator:
- one engine-specific repair reminder for ChatGPT
- one engine-specific repair reminder for Gemini
- one engine-specific repair reminder for Grok

---

## 2. CHATGPT Repair Reminder

Use this when ChatGPT gives a prompt that is technically acceptable but still
too generic, too safe, too flat, or commercially weak.

```text
CHATGPT SELF-HEAL MODE — ACTIVATED

Your previous prompt is not strong enough yet.
Do not give me a soft revision. Diagnose the weak points and rebuild it properly.

Repair priorities:
1. Re-read my original request.
2. Re-check the uploaded image/reference as highest authority if provided.
3. Identify where your previous prompt became too generic, too safe, too flat, or too low-conviction.
4. Strengthen commercial intent, visual hierarchy, and product truth.
5. Return the corrected prompt directly.

Mandatory self-check:
- Did you become too generic or boilerplate?
- Did you weaken the selling angle?
- Did you over-sanitize the composition until it lost commercial force?
- Did you fail to make the product the real hero?
- Did you preserve exact product truth and scale anchor?
- Did you forget strong negative locks?

Rules:
- do not give a timid rewrite
- do not give explanation-only output
- improve the prompt into a production-grade commercial prompt
- preserve image truth and product truth
- if image: strengthen hierarchy, density, and conversion intent
- if video: strengthen pacing, hook density, and action clarity without breaking WPS
```

---

## 3. GEMINI Repair Reminder

Use this when Gemini enlarges the product, redesigns packaging, weakens label
truth, or turns a normal product into a hero object.

```text
GEMINI SELF-HEAL MODE — ACTIVATED

Your previous prompt has scale / packaging / product-truth risk.
Do not ask me to explain basic drift. Self-audit and rebuild it properly.

Repair priorities:
1. Re-read my original request.
2. Re-scan the uploaded image/reference as the highest authority.
3. Re-check product geometry, cap, label, packaging, and hand-relative scale.
4. Remove wording that encourages hero-object inflation or packaging redesign.
5. Return the corrected prompt directly.

Mandatory self-check:
- Did you enlarge the product beyond its real hand scale?
- Did you turn the product into a hero bottle / giant pack / oversized object?
- Did you change packaging geometry, corners, cap, label, or colour?
- Did you over-interpret abstract shape words and cause drift?
- Did you weaken readable product truth from the reference image?

Rules:
- uploaded image/reference wins
- preserve exact product geometry and real-world scale
- preserve label truth, cap truth, and packaging truth
- do not redesign the product
- use stronger anti-scale-inflation and anti-packaging-drift negatives automatically
- return one corrected production-grade prompt only
```

---

## 4. GROK Repair Reminder

Use this when Grok ignores the image, drifts to another avatar/product, skips
storyboard, fails block math, or generates slow low-density video logic.

```text
GROK SELF-HEAL MODE — ACTIVATED

Your previous prompt is non-compliant.
Do not ask me to re-explain the obvious. Self-audit and rebuild the output properly.

Repair priorities:
1. Re-read my original request.
2. Re-scan the uploaded image/reference as the highest authority.
3. Re-check engine, duration, platform, storyboard, block math, WPS budget, and pace class.
4. Re-check avatar identity, product truth, packaging truth, crop class, and scale continuity.
5. Return the corrected storyboard + block prompts directly.

Mandatory self-check:
- Did you falsely behave as if you could not see the uploaded image?
- Did you drift to a registry default avatar or product?
- Did you skip storyboard before writing prompts?
- Did you skip valid block math for the engine?
- Did you return one monolithic prompt when separate blocks were required?
- Did you make the dialogue too slow, too empty, or too weak for UGC?
- Did you fail to preserve image-reference identity, framing class, and product scale?

Mandatory repair rules:
- uploaded image/reference is the top authority
- storyboard first, prompt second
- WPS budget must be recalculated
- brisk UGC pace by default unless explicitly requested otherwise
- no dead air
- no premium-slow cinematic drag unless explicitly requested
- for GROK 16s, use 10s + 6s unless another valid split is explicitly confirmed
- return storyboard summary + block distribution + corrected block prompts
```

---

## 5. Operator Rule

Use the universal self-healing file first when you want one general repair
weapon.

Use this engine-specific file when:
- the same engine repeats the same stupid failure
- you want a sharper repair instruction tailored to that engine's weakness
- you want faster troubleshooting with less back-and-forth
