# BOSMAX HARD ENGINE CONTRACTS v1

Authority file for the anti-stupidity lane.

This file exists to stop repeated low-IQ failures from engine drift, sandbox
friction, fake block math, and dialogue-less commercial video prompts.

---

## 1. Universal Hard Law

For commercial UGC video:
- uploaded image/reference is the highest visual authority
- engine math must be valid before any prompt is emitted
- storyboard must exist before block prompts are emitted
- dialogue must exist for BM commercial / recommendation / household UGC video
- pre-output checklist must PASS before release

Forbidden defaults:
- `pure visual`
- `no dialog`
- `WPS: 0`
- registry fallback drift
- fake scale reinterpretation
- slow elegant dead-air pacing for TikTok UGC unless explicitly requested

---

## 2. GROK Hard Contract

### Valid duration law

`GROK` only accepts these block durations:
- `6s`
- `10s`

Valid total examples:
- `12s` → `6s + 6s`
- `16s` → `10s + 6s`
- `20s` → `10s + 10s`

Forbidden:
- `12s base + 8s extension`
- `8s + 8s`
- monolithic `20s` block
- any extension math invented ad hoc

### Dialogue law

If the user asks for:
- `BM`
- `commercial`
- `UGC`
- `TikTok`
- `recommendation`

then the Grok prompt must include:
- spoken dialogue
- WPS budget
- pace class
- action density

`pure visual no dialog` is forbidden unless the user explicitly asks:
- silent montage
- music-only
- text-only

### Output shape law

Required output order:
1. visual scan summary
2. engine contract summary
3. storyboard
4. block prompt 1
5. block prompt 2+ jika ada

Never emit one giant Grok prompt if the duration requires multiple blocks.

### Seam continuity law

For BM commercial UGC extension:
- Block 1 should end speaking close to the final frame
- Block 2 should resume speech within the first `0.5s–1.0s`
- do not waste the seam on long silent action before dialogue continues
- use only micro-continuation action at the opening of Block 2

---

## 3. Claude Low-Friction Sandbox Contract

If the uploaded image already proves:
- product identity from label/logo
- packaging class
- approximate scale class
- avatar identity

then Claude must:
- build `visual_product_stub`
- proceed with visual-first sandbox
- ask only the truly missing fields

Claude must not:
- ask category questions if product class is already obvious enough for prompt generation
- ask packaging questions if packaging is already visible
- ask size in `cm` if the useful scale truth is relative-to-hand/body
- ask the user to restate what is already visible in the image

Low-friction default:
- if platform and language are already specified by user, proceed directly
- if not specified, ask only that

---

## 4. Gemini Anti-Drift Contract

Gemini must be forced to preserve:
- same face identity
- same outfit/hijab/body class
- same product class
- same label text hierarchy
- same framing class unless storyboard explicitly changes it
- same product-to-hand/body ratio

Gemini-specific negatives:
- no hero-object inflation
- no oversized bottle/box drift
- no packaging redesign
- no replacing household pack with bottle/pouch/cosmetic item
- no avatar beautification drift into a different person

If visual reference is strong, Gemini must behave as a preservation engine,
not as a reinterpretation engine.

---

## 5. Final Pre-Output Kill-Switch

Do not release the prompt unless every item passes.

```text
☐ uploaded image/reference was actually scanned
☐ no false claim that the image could not be seen
☐ no registry fallback drift
☐ product truth matches uploaded visual
☐ avatar truth matches uploaded visual
☐ scale truth matches uploaded visual
☐ engine is confirmed
☐ block math is valid for the engine
☐ storyboard exists
☐ storyboard is approved
☐ WPS budget is declared
☐ pace_class is declared
☐ if BM commercial UGC video: dialogue is present
☐ if engine = GROK: every block is only 6s or 10s
☐ if engine = GROK: no fake extension math
☐ if image-to-video: persistence lock is present
```

---

## 6. Operator Shortcut

Use this file when:
- Grok invents invalid duration math
- Gemini drifts product scale or avatar
- Claude wastes time with redundant sandbox questions
- any AI emits BM commercial UGC video without dialogue
- any AI leaks metadata/debug scaffolding in the final operator-facing prompt

This file is a hard correction layer, not a brainstorming layer.
