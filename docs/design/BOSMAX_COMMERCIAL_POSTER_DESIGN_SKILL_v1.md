# BOSMAX Commercial Poster Design Skill v1

## Status

`DRAFT — PENDING PILOT TEST`

Not yet injected into runtime. Defines canonical design intelligence for BOSMAX
commercial poster generation. Target skill: `bosmax-commercial-poster-director`.

---

## Purpose

Defines the BOSMAX-original design intelligence layer that converts a populated
Template Card into a commercially effective, compliance-safe, TikTok-ready
vertical 9:16 poster prompt.

This is not a public prompt library. It is a BOSMAX-owned design system built for:
- High-volume SEA commercial poster production
- TikTok Shop MY product truth compliance
- BOSMAX Serum product constraints (lip-balm scale, stealth silo)
- Repeatable variation across a template family without design drift

---

## Business Problem

Current BOSMAX image template cards (v0.1 / 01A series) are routing/spec cards.
They identify product, avatar, platform, and compliance class, but they do not
encode:

- Which visual mechanic produces scroll-stop
- How to place product and avatar to create conversion hierarchy
- Which layout formula to apply for a given selling goal
- How to control scale proof without text
- How to vary without breaking template objective
- How to score output quality before release

This skill closes that gap. Without it, BOSMAX cannot scale image production beyond
manual senior creative review on every output.

---

## Scope

- Commercial poster design mechanics
- Vertical 9:16 layout formulas for TikTok Shop MY
- Overlay / copy formula library (compliance-safe)
- Product truth lock rules
- Scale proof visual rules
- Safe-zone rules for TikTok UI
- Text rendering decision rules
- Variation discipline (what can mutate, what is frozen)
- QA scoring integration with `BOSMAX_POSTER_QA_RUBRIC_v1`
- Model-aware prompt expansion (see `BOSMAX_IMAGE_PROMPT_EXPANSION_CONTRACT_v1`)

---

## Non-Scope

- Video script generation
- Batch template structure
- Engine duration contracts
- Flow/Grok extension policy
- Notion import outputs
- Product registration
- Product copy / copywriting formulas (those live in copywriting registries)
- Social media caption writing
- Photo retouching or post-production

---

## Core Operating Principle

**The image is the salesperson.**

Every design decision — layout, lighting, scale proof, visual mechanic — must
serve one of three commercial functions:

1. **Truth** — prove the product is exactly what it claims to be
2. **Desire** — make the viewer want to own it in the next 1.5 seconds
3. **Action** — remove the final friction to tap the purchase link

If a design element does not serve at least one of these three functions, it is
decorative weight and should be eliminated or subordinated.

---

## BOSMAX Constraint Stack

These constraints are non-negotiable and override all other design choices.

| Constraint | Rule |
|---|---|
| Product geometry lock | Bottle shape, cap, color, and label placement cannot be altered |
| Label fidelity | BOSMAX HERBS label must be readable at 1× actual product size in the composition |
| Scale anchor enforcement | BOSMAX Serum 5ml = lip balm size; 10ml = chapstick size. Visual must prove this. Both variants: slim black cylindrical roll-on bottle. Do not render as white, pastel, or any other color. |
| Stealth silo compliance | No explicit body part claims; no before/after skin lesion imagery |
| No medical claims | No cure, no improvement guarantee, no diagnostic language |
| No fake certification | No invented badges, no fake halal/ISO icons unless product_record confirms real cert |
| No competitor presence | Object comparison must compare to household objects (coin, lip balm), never a named competitor product |
| No CTA over label | Call-to-action text or badge must not cover the product label area |
| TikTok safe-zone | UI chrome at top ~8% and bottom ~25% of 9:16 frame must remain navigable |
| No label redesign | Background, font, or color of actual product label cannot be changed in the prompt |

---

## Skill Inputs

Required before this skill can execute:

| Input | Source | Required |
|---|---|---|
| `product_record` | `bosmax-product-intelligence` or registry | YES |
| `scale_anchor_descriptor` | `product_record.variant.scale_anchor` | YES |
| `subject_dna` | `bosmax-subject-dna` | YES for avatar-present posters |
| `template_card` | Upgraded v1 Template Card | YES |
| `platform` | PRE-FLIGHT resolved | YES |
| `creative_intensity` | Template Card field | YES |
| `compliance_class` | `product_record.compliance_class` | YES |
| `language_mix` | Template Card field | YES |

---

## Skill Outputs

| Output | Format | Destination |
|---|---|---|
| `full_master_image_prompt` | English string, structured sections | Image generation engine |
| `prompt_variants` | Array of variant strings | Batch / variation queue |
| `qa_checklist_result` | Pass/Fail per dimension | `bosmax-compliance-gate` |

> **Future integration note (out of scope for this document):** `source_image_handoff`
> JSON generation (Mode C passport / VIDEO_SUPPORT goal) is the responsibility of
> `bosmax-scene-engine`, not this design skill. This skill governs design intelligence
> only. See `CLAUDE.md` Route C and Route A pipeline sequences for the handoff contract.

---

## Commercial Poster Mechanics Library

These are BOSMAX-canonical visual mechanics. Each mechanic has a defined
commercial function, a recommended product placement, and a safe-zone impact score.

### SCALE PROOF GROUP

**01 — Fingertip Scale Proof**
Avatar fingertip contacts the bottle. Fingernail visible. Bottle fits between tip
and first knuckle. Proves lip-balm scale without text.
Best for: BOSMAX Serum 5ml truth posts.

**02 — Thumb-Pad Width Proof**
Bottle rests flat on thumb pad. Width clearly less than thumb width.
Best for: emphasising compact portability.

**03 — Pocket Reveal**
Hand extracts bottle from pocket, jeans texture or blazer pocket frame visible.
Proves carry-anywhere scale and discretion in one image.
Best for: BOSMAX Serum stealth silo, lifestyle truthfulness.

**04 — Slip-Pouch Reveal**
Bottle emerging from a small toiletry pouch or makeup bag. Scale context from
zipper teeth and fabric weave.
Best for: travel narrative, gifting context.

**05 — Macro Label Proof**
Extreme macro of label area fills 30–50% of frame. BOSMAX HERBS text is readable.
Batch number or ingredient line visible. Proves authenticity and production quality.
Best for: trust-building, anti-counterfeit messaging.

**06 — Cap Seam Proof**
Close-up where cap-to-body seam is visible and crisp. No bleeding, no deformation.
Light catching the seam geometry confirms plastic/resin quality.
Best for: premium feel within a budget product position.

### LAYOUT MECHANICS GROUP

**07 — Lower-Third Billboard Hero**
Product placed in lower third. Upper two thirds carry avatar expression or
lifestyle context. Maximum face real-estate for emotional connection.
Best for: avatar-led conversion posts.

**08 — Micro Product / Massive Negative Space**
Product small in frame, surrounded by clean background space. Text can float.
Counter-intuitive scroll-stop through whitespace contrast.
Best for: premium positioning, hero-price reveal.

**09 — Diagonal Hand Entry**
Hand enters from a bottom or side corner at a diagonal. Creates motion implication
and directs eye toward product in opposing corner.
Best for: energy and pace without actual animation.

**10 — Macro-to-Packshot Stack**
Top 60% is extreme macro (texture, skin, material). Bottom 40% snaps to clean
packshot with label prominent.
Best for: ingredient/efficacy trust then product close.

### LIGHT AND SURFACE GROUP

**11 — Rim-Light Black Separation**
Dark background with single rim light source tracing the bottle silhouette.
Product appears to float. Premium feel, zero distractions.
Best for: SCROLL_STOPPER intensity tier.

**12 — Controlled Reflection Strip**
Single narrow horizontal reflection of product visible on surface below it.
Symmetry implies premium retail aesthetic.
Best for: CONVERSION tier, clean surface backgrounds.

**13 — Texture Contrast Stage**
Product placed on a surface with contrasting texture (smooth glass on rough
marble, smooth bottle on woven rattan). Tension between textures creates
visual interest with no extra objects.
Best for: lifestyle premium without cluttered props.

**14 — Night-Routine Sink/Bedside Edge**
Product on bathroom sink edge or bedside table, low ambient light, warm tone.
Context implies daily ritual and habit formation.
Best for: routine-building narrative, night skincare.

### PROOF AND TRUST GROUP

**15 — Object Comparison Without Competitor**
Product beside a coin, SIM card, or lip balm (generic, unbranded). Scale
established without mentioning any competitor product.
Best for: size truth, "surprisingly small" moment.

**16 — Badge-Led Proof Lock**
Small trust badges (count-sold, star rating, "Original MY") anchored at bottom
safe zone. Not over the label. Not fake.
Best for: social proof layer in CONVERSION tier.

**17 — Visual Metaphor Shadow**
Product casts a shadow shaped like a related object (leaf, water drop, crescent).
Adds narrative without explicit text claim.
Best for: stealth silo organic association.

### COMMERCE AND CTA GROUP

**18 — CTA Badge Cluster**
Small CTA group (price, offer, link icon) anchored in bottom-right corner, inside
TikTok safe-zone, in a compact 3-element cluster. Never overlapping label.
Best for: conversion-layer templates.

**19 — Safe-Zone Headline Rail**
Single strong headline text bar in top-left safe zone, between 8% and 20% from
top. Two lines maximum. Large, bold, contrast.
Best for: hook copy on poster.

**20 — Lower-Footer Offer Bar**
Horizontal band at bottom of frame (above TikTok UI chrome). Price, offer code,
or one-line CTA. Contained, readable, not touching the label.
Best for: price reveal, flash sale overlays.

**21 — Corner Hand-Entry with Offer Badge**
Hand enters from corner with product, small offer badge near product cap.
Combines scale proof with commerce signal in one composition.
Best for: dual-function CONVERSION posts.

---

## Vertical 9:16 Layout Formula Library

These are the canonical BOSMAX layout formulas for TikTok 9:16 (1080×1920).
Each formula has a defined zone split, role per zone, and recommended use case.

**LF-01 — Lower-Third Hero**
```
Zone A (0–35%):  Avatar face / expression or lifestyle context
Zone B (35–65%): Product prominently placed, scale proven
Zone C (65–85%): Copy or empty negative space
Zone D (85–100%): TikTok UI safe zone — CLEAR
```
Use: avatar-led product truth posts.

**LF-02 — Centre Spine Monolith**
```
Zone A (0–15%):  TikTok safe zone — clear except logo
Zone B (15–50%): Product centered, large, vertical spine
Zone C (50–75%): Supporting copy or proof element
Zone D (75–85%): CTA or badge
Zone E (85–100%): TikTok safe zone — CLEAR
```
Use: single-product hero, minimum distraction.

**LF-03 — Left Rail Headline**
```
Left column (0–40% width): Text, headline, copy rail
Right column (40–100% width): Product or avatar visual
```
Use: bilingual copy-heavy posts (BM + EN).

**LF-04 — Right Rail Headline**
```
Left column (0–60% width): Product or avatar visual
Right column (60–100% width): Text, headline, copy rail
```
Use: right-to-left reading scan audiences; price reveal right.

**LF-05 — Top Proof / Middle Hero / Bottom CTA**
```
Zone A (0–25%):  Proof element (macro, badge, scale object)
Zone B (25–65%): Product hero in full
Zone C (65–80%): CTA text or offer bar
Zone D (80–100%): TikTok UI safe zone — CLEAR
```
Use: trust-first conversion templates.

**LF-06 — Hero Middle / Footer Commerce Bar**
```
Zone A (0–20%):  Headline rail (safe-zone compliant)
Zone B (20–75%): Product + avatar hero
Zone C (75–85%): Commerce bar (price, link, CTA)
Zone D (85–100%): TikTok UI safe zone — CLEAR
```
Use: conversion-optimised product launch posts.

**LF-07 — Macro Over Packshot**
```
Zone A (0–55%):  Extreme macro (texture, skin, ingredient visual)
Zone B (55–80%): Product packshot, label readable
Zone C (80–100%): TikTok safe zone / minimal copy
```
Use: ingredient trust → product reveal.

**LF-08 — Diagonal Descent**
```
Visual element descends from top-left to bottom-right at ~30° angle.
Product sits at terminus of diagonal in lower-right quadrant.
Background is clean gradient or solid.
```
Use: motion energy, directional eye flow toward product.

**LF-09 — Corner Hand Entry**
```
Hand enters from bottom-left or top-right corner.
Product occupies centre or opposing corner.
Diagonal implied by arm/wrist direction.
```
Use: pocket reveal, carry proof, energy shots.

**LF-10 — Negative-Space Cathedral**
```
Zone A (0–20%):  Clean background — top clear
Zone B (20–80%): Isolated product, centred, high negative space ratio
Zone C (80–100%): Minimal one-line CTA or clean — TikTok UI safe
```
Use: premium price anchor, prestige positioning.

**LF-11 — Pocket Window Reveal**
```
Full frame: jeans, jacket, or bag pocket context
Product visible emerging from pocket opening in centre of frame
Background context surrounds the pocket
```
Use: scale and stealth silo carry proof.

**LF-12 — Split Proof / Offer**
```
Left 50%:  Proof visual (hand + product, macro, badge cluster)
Right 50%: Offer / copy / price
```
Use: value justification posts, "why this price" narrative.

**LF-13 — Badge Dock Hero**
```
Zone A (0–15%):  Trust badge strip or headline
Zone B (15–80%): Product hero
Zone C (80–85%): Badge dock — icon row (sold count, rating, origin)
Zone D (85–100%): TikTok UI safe zone — CLEAR
```
Use: social proof conversion posts.

**LF-14 — Sidecar Facts**
```
Main column (0–65% width):  Product or avatar visual
Sidecar column (65–100% width): Stacked fact chips or ingredient callouts
```
Use: ingredient disclosure, multi-USP proof.

**LF-15 — Lower Billboard with Cropped Hero**
```
Zone A (0–50%):  Avatar cropped — face and torso, no feet
Zone B (50–75%): Product billboard placement — large, angled
Zone C (75–85%): Price/offer bar
Zone D (85–100%): TikTok UI safe zone — CLEAR
```
Use: sale/promo posts, avatar-commerce hybrid.

---

## Copy Overlay Formula Library

These are compliance-safe overlay copy formulas for BOSMAX Serum (STEALTH silo).
All examples are for BM + EN mix as default for TikTok Shop MY.

**Safe neutral examples (always permitted — no product_record verification required):**

**CO-01** — `Saiz poket. Selesa bawa.` / `Pocket size. Comfortable to carry.`
**CO-02** — `5ML roll-on. Sebesar lip balm.` / `5ML roll-on. Lip balm size.`
**CO-03** — `Kecil macam lip balm. Muat dalam poket.` / `Small as lip balm. Fits in your pocket.`
**CO-04** — `Label jelas. Botol kemas.` / `Clear label. Neat bottle.`
**CO-05** — `Saiz kecil. Detail premium.` / `Small size. Premium detail.`
**CO-06** — `Kecil. Kemas. Private.`
**CO-07** — `Tap tengok detail.` / `Tap to see details.`
**CO-08** — `Buka shop, check dulu.` / `Open shop, check first.`
**CO-09** — `Mudah dibawa ke mana sahaja.` / `Easy to carry anywhere.`
**CO-10** — `Percayakan kualiti BOSMAX.` / `Trust BOSMAX quality.`
**CO-11** — `Kuantiti terhad. Order sekarang.` / `Limited quantity. Order now.`
**CO-12** — `Percubaan pertama? Dapatkan harga pengenalan.` / `First try? Get intro price.`
**CO-13** — `Set 2 botol. Jimat lebih.` / `2-bottle set. Save more.`
**CO-14** — `Harga rasmi RM [X]. Diskaun sehingga RM [Y].` / `Official price RM [X]. Discount up to RM [Y].`
**CO-15** — `Muat dalam pouch. Sesuai untuk travel.` / `Fits in your pouch. Perfect for travel.`
**CO-16** — `Produk asal BOSMAX. Elak tiruan.` / `Original BOSMAX product. Avoid imitations.`

**`PRODUCT_RECORD_REQUIRED` — use ONLY if verified in `product_record`:**

**CO-PR-01** — `Disahkan halal.` / `Halal verified.`
*(only if `product_record.certifications` confirms halal certification)*

**CO-PR-02** — `Ramuan semulajadi. Formulasi tepat.` / `Natural ingredients. Precise formula.`
*(only if `product_record` confirms natural/herbal formulation claim)*

**CO-PR-03** — `Sesuai untuk semua jenis kulit.` / `Suitable for all skin types.`
*(only if `product_record` confirms this claim — not for STEALTH_METAPHOR_REQUIRED class)*

**CO-PR-04** — `Tanpa bahan berbahaya.` / `Free from harmful ingredients.`
*(only if `product_record` or lab cert confirms — do not present generically)*

**CO-PR-05** — `Original Malaysia. Dirumus di Malaysia.` / `Authentic Malaysian. Formulated in Malaysia.`
*(only if `product_record` confirms Malaysian formulation)*

**CO-PR-06** — `Lebih [N] ulasan bintang 5.` / `Over [N] five-star reviews.`
*(only if `product_record.total_orders` or verified review count confirms)*

**CO-PR-07** — `Terlaris minggu ini.` / `Bestseller this week.`
*(only if Fastmoss data or TikTok Shop rank data is confirmed in `product_record`)*

**CO-PR-08** — `Rutin harian. Kesan yang nyata.` / `Daily routine. Visible results.`
*(use carefully — "visible results" is on the compliance edge; only if product_record or silo permits)*

**Forbidden copy patterns (STEALTH_METAPHOR_REQUIRED compliance):**
- `Hilangkan...` (eliminate/remove — implies cure)
- `Sembuh...` (cures — medical claim)
- `Kurangkan parut...` (reduce scars — before/after claim)
- `Dijamin...` (guaranteed — result guarantee)
- `Lebih cerah dalam X hari` (brighter in X days — timeline guarantee)
- Any reference to specific skin conditions or body parts by name
- Any explicit male health / intimate benefit claim without STEALTH metaphor filter

---

## Product Truth Lock Rules

1. `product_name`, `product_variant`, and `label_text` from `product_record` are
   read-only inputs. They cannot be altered in any prompt.
2. The bottle shape descriptor from `product_record.geometry` must appear verbatim
   in the prompt negative constraints section.
3. Scale anchor descriptor must appear in Section 3 (Product Scale and Geometry)
   of the full prompt.
4. If `product_record` is missing, this skill MUST abort and request it.
5. Label color, font style, and placement on the bottle are frozen. No prompt
   instruction may suggest "redesign" or "reimagine" the label.
6. The cap type and color from `product_record` must match the prompt description.
7. If the product appears in the generated image as a different product category
   (perfume, dropper, deodorant), that is an auto-reject condition.

---

## Reference Handling Rules

When `reference_mode = IMAGE_REFERENCE` or `VIDEO_REFERENCE`:

1. Extract concept DNA (visual structure, composition, lighting mood, mechanics)
   from the reference only.
2. Replace all product identity entirely with the BOSMAX product.
3. Replace all avatar identity with the BOSMAX subject_dna.
4. Do not carry over any text, logo, brand, or overlay from the reference.
5. Do not carry over compliance class from the reference — inject BOSMAX compliance_class.
6. Do not describe the reference's product in the generated prompt.
7. A→B separation is absolute: reference = visual structure source only.

---

## Text Rendering Rules

TikTok Shop poster context requires careful decisions about text in the image vs
text applied as overlay post-generation.

| Situation | Recommended approach |
|---|---|
| Short bilingual hook (1–2 lines) | Overlay/post-composite (deterministic, pixel-accurate) |
| Long copy rail (3+ lines) | Overlay/post-composite only |
| Exact price / offer code | Overlay/post-composite only |
| Brand name in scene prop (not on product) | AI image render acceptable if unambiguous |
| Product label text | AI image render (from product_record lock) — but treat as decorative, confirm with macro |
| Badge icons (generic stars, check mark) | AI render acceptable for simple icons |
| Certification number / Halal cert code | Overlay/post-composite only — AI cannot guarantee exact numerals |

If `text_rendering_mode = OVERLAY_ONLY` in the Template Card, no text instruction
should be included in the generation prompt. Text will be applied post-composite.

If `text_rendering_mode = AI_RENDER`, the prompt may describe text elements but
must include in the negative constraint: `no misspelled text, no garbled characters,
no font mutation`.

---

## Safe-Zone Rules

TikTok 9:16 UI chrome occupies predictable screen areas on most devices.

| Zone | Approximate frame position | Rule |
|---|---|---|
| Top status + account name | Top 8% of frame | Keep clear of primary design elements |
| Left navigation icons | Left edge, 15–85% vertical range | Keep primary product away from hard left edge |
| Right engagement buttons | Right edge, 35–85% vertical range | Avoid placing CTA badges in this column |
| Bottom caption + CTA bar | Bottom 20–25% of frame | No essential product content below 80% |
| Bottom TikTok navigation | Bottom 10% of frame | Always clear — hard rule |

Design content must be composed to function within the safe zone, not assume
the viewer controls cropping.

---

## Compliance Micro-Rules

These are the zero-tolerance rules that trigger auto-reject in QA.

- No skin before/after split imagery
- No body part targeting language in overlay text (e.g. "for your face", "neck area")
- No numerical improvement claim ("10× more hydration", "reduces by 70%")
- No timeline claim ("see results in 7 days")
- No certification imagery unless `product_record.certifications` contains the cert
- No competitor product visible in frame
- No explicit body part implied by camera angle on human model
- No imagery that implies a medical treatment or clinical procedure
- No price shown unless `product_record.pricing` contains the price

---

## Variation Discipline

Variation is controlled. Only approved axes may mutate between variants within
a template family.

**Frozen controls (must not change between variants):**
- Product geometry
- Scale anchor description
- Label text and placement
- Compliance class
- Template role (MASTER_PROMPT_SEED vs variant)
- Layout formula number

**Approved variation axes per template (declared in Template Card):**
- Background color / tone
- Avatar wardrobe color
- Lighting temperature (warm ↔ cool)
- Prop or surface texture (within surface_strategy)
- Hand pose (within hand_pose_rule)
- Copy overlay text (within CO formula library)
- Crop tightness (within shot_spec range)

**Mutation limits:**
- A maximum of 3 variation axes may change between any two variants in a family.
- Changing 4+ axes produces a new template, not a variant.
- Variants within a family must score within 5 points of the master on the QA rubric.

---

## Rejection Rules

Output must be rejected (not released to production) if any of the following are true:

- Bottle appears as wrong product category
- Cap shape deformed or missing
- Label text garbled, missing, or mutated
- Product appears larger than 1.5× the scale anchor descriptor allows
  unless explicitly in a macro composition that still preserves scale context
- Hand anatomy impossible (extra fingers, melted fingers, wrong joint count)
- TikTok safe-zone hard-blocked by primary product content
- Any compliance micro-rule violated
- QA total score below 82
- Any single dimension below 7
- Product Truth, Label Fidelity, or Compliance Safety below 9

---

## Relationship to Notion Template Pages

The Notion 01A template pages are currently v0.1 seed cards. They encode
routing/spec data but not design intelligence.

This skill defines what each 01A card must be upgraded to include when the
01A rewrite PR is executed:
- `commercial_trigger` field
- `hero_proof` field
- `visual_mechanic` field (from mechanic library above)
- `layout_formula` field (from layout formula library above)
- `overlay_direction` field
- `frozen_controls` list
- `variation_axis` list
- `qa_score_target` field

The 01A rewrite is a separate PR. This document is the prerequisite contract.

---

## Relationship to Claude Cowork / BOSMAX Agents

This skill is the design intelligence authority for:
- `bosmax-scene-engine` — must reference layout formula and visual mechanic from this skill
- `bosmax-commercial-poster-director` — implements this skill directly
- `bosmax-compliance-gate` — QA rubric is derived from this skill's rejection rules
- `bosmax-bulk-generator` — variation discipline section governs batch axis selection

PRE-FLIGHT protocol in `CLAUDE.md` governs routing. This skill governs design
quality after routing is complete.

---

## Relationship to Future Repo Skills

This document is v1. Future versions will add:
- Additional mechanics for Shopee / Lazada platform layout differences
- Male avatar mechanics library (currently female-dominant examples)
- Multi-product comparison mechanics (when product registry grows)
- Animated GIF / cinemagraph variant mechanics

---

## Implementation Sequence

1. ✅ This document — Design Skill Contract (current PR)
2. ⬜ `BOSMAX_IMAGE_TEMPLATE_CARD_CONTRACT_v1.md` — template schema upgrade
3. ⬜ `BOSMAX_IMAGE_PROMPT_EXPANSION_CONTRACT_v1.md` — expansion rules
4. ⬜ `BOSMAX_POSTER_QA_RUBRIC_v1.md` — scoring and rejection gates
5. ⬜ Pilot: 5 template families × 5 variants = 25 output pilot test
6. ⬜ 01A rewrite PR — upgrade existing Notion templates to v1 schema
7. ⬜ `bosmax-commercial-poster-director` skill implementation
8. ⬜ Notion mirror of skill contract

---

## Open Questions

| ID | Question | Owner | Priority |
|---|---|---|---|
| OQ-01 | Can NANO_BANANA_PRO reliably render BOSMAX HERBS label without mutation at 5ml scale? Needs pilot test. | Eng | HIGH |
| OQ-02 | Is IMAGEN_3 available for BOSMAX production use? Pricing and access tier TBC. | Ops | HIGH |
| OQ-03 | Should CO formulas be stored in a separate YAML file for agent lookup, or remain in this doc? | Arch | MEDIUM |
| OQ-04 | Male avatar mechanics library — when? BOSMAX Serum may have male-audience segments. | Creative | MEDIUM |
| OQ-05 | Should `variation_axis` be a hard enum list per template family or free-declared per card? | Arch | MEDIUM |
| OQ-06 | What is the minimum QA score threshold for sandbox/pilot outputs vs production outputs? | QA | LOW |
