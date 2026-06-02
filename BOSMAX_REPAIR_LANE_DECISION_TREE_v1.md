# BOSMAX REPAIR LANE DECISION TREE v1

Authority file for choosing the correct repair / prompt-correction lane fast.

Use this page when the operator asks:
- prompt mana patut guna sekarang?
- bila guna universal?
- bila guna engine-specific?
- bila guna product-specific?
- bila terus guna sandbox/on-the-fly?

---

## 1. Short Rule

Use the lightest lane that can solve the problem.

Escalation order:
1. `UNIVERSAL SELF-HEALING`
2. `ENGINE-SPECIFIC SELF-HEALING`
3. `PRODUCT-SPECIFIC SELF-HEALING`
4. `SANDBOX / ON-THE-FLY`

Do not jump to the heaviest lane first unless the failure is obviously tied to
that lane.

---

## 2. Decision Tree

### Case A — Prompt wrong, but problem is general

Use:
- `BOSMAX_PROMPT_SELF_HEALING_CHECKLISTS_v1.md`

Typical signs:
- prompt lemah
- prompt generic
- AI skip obvious negative locks
- AI bagi output tak cukup kemas
- AI minta user explain semua error satu-satu

Use this first when:
- you do not yet know whether the problem is engine-shaped or product-shaped
- you just want one general repair weapon

---

### Case B — Prompt wrong because the engine has a known behavior problem

Use:
- `BOSMAX_ENGINE_SPECIFIC_SELF_HEALING_VARIANTS_v1.md`

Typical signs:
- `ChatGPT` terlalu generic / terlalu safe / terlalu low-conviction
- `Gemini` inflate scale / redesign packaging / hero-object bias
- `Grok` ignore image / skip storyboard / wrong block math / slow pace / weak WPS density

Use this when:
- the same engine repeats the same stupid failure
- universal repair still too broad
- you want a repair reminder targeted to the engine's weakness

---

### Case C — Prompt wrong because the product truth keeps drifting

Use:
- `BOSMAX_PRODUCT_SPECIFIC_SELF_HEALING_VARIANTS_v1.md`

Typical signs:
- `MWCB`:
  - wrong bottle shape
  - wrong red cap
  - wrong perched bird artwork
  - wrong label colours
  - oversized bottle
- `BOSMAX Serum`:
  - wrong 5ML / 10ML scale
  - deodorant / perfume drift
  - black stealth packaging broken
  - sensitive dialogue lane broken
- `Maverix`:
  - wrong bottle count
  - wrong set structure
  - horse-logo / masculine packaging drift
  - stealth masculine tone broken

Use this when:
- the product keeps drifting in the same way
- engine-specific repair is still not precise enough
- you want the AI to audit exact product truth before rewriting

---

### Case D — Product is unknown or not in registry

Use:
- `BOSMAX_SANDBOX_ON_THE_FLY_TEMPLATES_v1.md`

Typical signs:
- product not found in `products/*.yaml`
- product not found in FastMoss
- user still wants immediate image/video generation
- uploaded image clearly shows product label / packaging / scale clues

Use this when:
- the issue is not mainly “repair old prompt”
- the issue is “AI needs enough product truth now to proceed”
- you need `visual-first sandbox` or `mini-intake shortcut`

---

## 3. Fast Matrix

| Situation | Correct lane |
|---|---|
| Prompt salah secara umum | `UNIVERSAL SELF-HEALING` |
| ChatGPT terlalu generic | `ENGINE-SPECIFIC → ChatGPT` |
| Gemini besarkan produk | `ENGINE-SPECIFIC → Gemini` |
| Grok skip storyboard / block math / pace | `ENGINE-SPECIFIC → Grok` |
| MWCB packaging / scale rosak | `PRODUCT-SPECIFIC → MWCB` |
| BOSMAX Serum variant / stealth rosak | `PRODUCT-SPECIFIC → BOSMAX Serum` |
| Maverix set structure / stealth rosak | `PRODUCT-SPECIFIC → Maverix` |
| Produk belum ada dalam registry | `SANDBOX / ON-THE-FLY` |

---

## 4. Practical Operator Flow

If prompt/output is bad:

1. Ask:
   - adakah ini masalah umum?
   - masalah engine?
   - masalah product truth?
   - atau produk unknown?

2. Pick the first matching lane:
   - general → universal
   - engine-shaped → engine-specific
   - product-shaped → product-specific
   - unknown product → sandbox/on-the-fly

3. If still not fixed:
   - escalate one layer heavier

Example:
- Grok salah pacing + salah block math + ignore image
  → start at `ENGINE-SPECIFIC → Grok`
- Gemini salah scale untuk MWCB
  → if mainly engine inflation: `ENGINE-SPECIFIC → Gemini`
  → if still wrong on MWCB bottle truth: escalate to `PRODUCT-SPECIFIC → MWCB`
- Produk baru tak ada registry, tapi gambar clear
  → `SANDBOX / ON-THE-FLY`

---

## 5. Final Rule

Do not make the operator think too much.

If the failure source is obvious:
- choose the matching lane directly

If the failure source is not obvious:
- start with `UNIVERSAL SELF-HEALING`
- then escalate only if needed
