# BOSMAX Visual Ads Layout Kernel v1

## Status

`ACTIVE — PR #32A`

Single source of truth for commercial poster ad archetype definitions, module
stacks, product dominance rules, and compliance-safe copy pools.

Target consumers:
- `bosmax-commercial-poster-director.md` — archetype selection + module stack assembly
- `bosmax-scene-engine.md` — render zone translation
- `bosmax-compliance-gate.md` — module completeness audit

---

## Core Operating Principle

**The image is the salesperson, not the decorator.**

Every module in a poster serves one of three commercial functions:

1. **Truth** — prove the product is exactly what it claims to be
2. **Desire** — make the viewer want it within 1.5 seconds
3. **Action** — remove final friction to tap the purchase link

Any element that does not serve at least one of these three functions is
decorative weight and must be eliminated or subordinated.

---

## Product Dominance Rule — Universal (All Archetypes)

```
PRODUCT_DOMINANCE_RULE:
  Product must be the FIRST-READ element in the composition.
  First-read = viewer eye lands on product before any text within 0.5 seconds.

  Enforcement:
  - Product placed at optical centre or golden ratio focal point
  - Product receives highest contrast, sharpest focus, cleanest light
  - No text block may be taller than product in frame
  - No benefit chip stack may be wider than product dominance zone
  - Scale object (key/hand/pocket) placed adjacent — never overlapping product label
  - Headline font size must not exceed 40% of product height in frame

FORBIDDEN across all archetypes:
  - Text headline taller than product
  - Benefit chip stack wider than product
  - Background element competing with product for first-read position
  - Canva-style giant headline that pushes product to supporting role
  - Text-first layout where product is subordinate
```

---

## Typography Restraint Rule — Universal (All Archetypes)

```
TYPOGRAPHY_RESTRAINT_RULE:
  Hook/headline:    bold, high contrast, max 5–6 words, top zone
  Benefit chips:    small pill/badge shape, factual text only, 2–3 chips max
  CTA:              button shape, restrained size, bottom zone
  Support line:     optional, smaller than hook, single line

FORBIDDEN:
  - Headline that screams louder than product
  - Font size that makes product feel like a footnote
  - More than 3 benefit chips (unless archetype explicitly permits more)
  - Chip text that implies efficacy, medical result, or unverified claim
  - CTA larger than or equal to product in visual weight
```

---

## Compliance-Safe Copy Pool — BOSMAX Serum (All Archetypes)

```
HOOK_FAMILY_SCALE:
  "MUAT POKET. TAK RIBET."
  "BOTOL KECIL. SENANG BAWA."
  "KECIL. KEMAS. MUDAH BAWA."
  "5ML. MUAT KE MANA-MANA."

HOOK_FAMILY_PRIVATE:
  "BAWA PRIVATE. SIMPAN SENANG."
  "MASUK POKET. TAK NAMPAK."
  "SENANG BAWA. SENANG SIMPAN."

HOOK_FAMILY_PREMIUM:
  "BOSMAX HERBS."
  "HERBAL OIL ROLL ON."
  "AUTHENTIC. ORIGINAL."

BENEFIT_CHIPS_ALLOWED:
  "5ML Roll-On"
  "Mudah Bawa"
  "Senang Simpan"
  "Muat Poket"
  "Private Carry"
  "Herbal Oil Roll On"
  "BOSMAX HERBS"
  "Kecil & Kemas"

BENEFIT_CHIPS_FORBIDDEN:
  "Berkesan"          — efficacy implication
  "Relief"            — medical claim territory
  "Tak Panas"         — unverified product claim
  "Cepat Rasa"        — sensory/efficacy claim
  "Legakan"           — medical territory
  "Tahan Lama"        — durability claim without proof
  "Fast Absorbing"    — unverified
  "Non-Sticky"        — unverified
  Any before/after    — hard reject for BOSMAX Serum
  Any body-effect     — stealth silo breach

CTA_POOL:
  "Tap Tengok Harga"
  "Klik Untuk Lihat Harga"
  "Tap Untuk Tahu Lebih"
  "Klik Lihat Offer"       — only if promo confirmed by operator
  "Beli 1 Percuma 1"       — only if promo confirmed by operator
```

---

## Archetype Definitions

### ARCHETYPE A — SCALE_PROOF_AD

```
Selling job:
  Prove product is smaller than viewer expects.
  Viewer must understand scale within 1.5 seconds without reading any text.

Visual anchor:
  Hand / finger / key / coin scale comparison object adjacent to product.

Module stack:
  [1] HOOK_CHIP      — from HOOK_FAMILY_SCALE, max 5 words, top zone
  [2] PRODUCT_HERO   — product centred, scale object beside/below it
  [3] CHIP_STACK     — 3 chips from: "5ML Roll-On" / "Muat Poket" / "Senang Simpan"
  [4] CTA_BUTTON     — from CTA_POOL, bottom zone
  [5] TRUST_LABEL    — product label readable, no fake badge

Layout zones (9:16):
  Hook:           top 10–15% of frame
  Product hero:   centre 50–60%, first-read dominant
  Chip stack:     lower third, below product
  CTA button:     bottom 10–15%
  Scale object:   adjacent to product, within product zone

Copy pool anchor:
  Hook → HOOK_FAMILY_SCALE
  Chips → "5ML Roll-On" + "Muat Poket" + "Senang Simpan"
  CTA → "Tap Tengok Harga" or "Klik Untuk Lihat Harga"

Compliance:
  No medical claim / no sexual cue / no before-after / no fake promo
  Scale object must be household object (key, lip balm, coin) — never competitor product

REJECT if:
  - No scale object present
  - No benefit chips present
  - Product is not first-read element
  - Text dominates product in frame area
```

---

### ARCHETYPE B — PRIVATE_CARRY_AD

```
Selling job:
  Position product as pocket-safe, private, carry-anywhere.

Visual anchor:
  Product partially revealed from pocket, pouch, or bag.

Module stack:
  [1] HOOK_CHIP      — from HOOK_FAMILY_PRIVATE, max 4 words
  [2] PRODUCT_HERO   — product in/near pocket or pouch, label visible
  [3] CHIP_STACK     — 3 chips: "Muat Poket" / "Private Carry" / "5ML Roll-On"
  [4] CTA_BUTTON     — from CTA_POOL
  [5] TRUST_LABEL    — BOSMAX HERBS label readable even if product partially concealed

Layout zones (9:16):
  Hook:           top 10–15%
  Lifestyle scene: mid 45–55%, product hero within scene
  Chip stack:     lower third
  CTA button:     bottom 10–15%

Copy pool anchor:
  Hook → HOOK_FAMILY_PRIVATE
  Chips → "Muat Poket" + "Private Carry" + "5ML Roll-On"
  CTA → "Tap Tengok Harga"

Compliance:
  No sexual metaphor / no body-effect claim / no explicit vitality language
  Product label must be identifiable — not fully concealed

REJECT if:
  - Product label not visible
  - Body-effect language in chips or hook
  - Sexual/vitality implication detected
```

---

### ARCHETYPE C — PREMIUM_TRUST_AD

```
Selling job:
  Build credibility. Factual, clean, restrained premium feel.

Visual anchor:
  Product on surface or held, label dominant, clean environment.

Module stack:
  [1] PRODUCT_HERO   — clean product hero, label fills minimum 25% of frame
  [2] FACTUAL_CHIPS  — 2–3 chips: "BOSMAX HERBS" / "Herbal Oil Roll On" / "5ML Roll-On"
  [3] RESTRAINED_HOOK — short, confident, from HOOK_FAMILY_PREMIUM
  [4] CTA_BUTTON     — "Klik Untuk Lihat Harga"
  [5] NO_BADGE       — no promo badge unless promo confirmed by operator

Layout zones (9:16):
  Product:        60% of frame, label prominent
  Chips:          right column or lower cluster, restrained size
  Hook:           top, smaller than standard — premium restraint
  CTA:            bottom

Copy pool anchor:
  Hook → HOOK_FAMILY_PREMIUM
  Chips → factual only: "BOSMAX HERBS" / "Herbal Oil Roll On" / "5ML Roll-On"
  CTA → "Klik Untuk Lihat Harga"

Compliance:
  No fake certification / no invented proof chip / no star rating without data source

REJECT if:
  - Fake halal / MAL / NPRA badge present
  - Invented rating or review chip
  - Non-factual chip language
```

---

### ARCHETYPE D — PROMO_AD

```
Selling job:
  Drive immediate purchase with a verified offer.

Prerequisite:
  promo_confirmed = true in product_record OR operator has explicitly stated active promo.
  HARD BLOCK if promo not confirmed — do not generate PROMO_AD without confirmation.

Visual anchor:
  Product hero + offer badge.

Module stack:
  [1] PROMO_BADGE    — "Beli 1 Percuma 1" ONLY if operator confirmed
  [2] PRODUCT_HERO   — product dominant, badge must not cover label
  [3] CHIP_STACK     — "5ML Roll-On" / "Mudah Bawa" / "Senang Simpan"
  [4] HOOK_CHIP      — urgency hook, max 4 words
  [5] CTA_BUTTON     — "Tap Untuk Claim Offer"

Layout zones (9:16):
  Promo badge:    top-right burst or top banner — must not cover product label
  Product hero:   centre dominant
  Chips:          lower third
  CTA:            bottom

Copy pool anchor:
  Hook → urgency variant from HOOK_FAMILY_SCALE
  Chips → "5ML Roll-On" + "Mudah Bawa" + "Senang Simpan"
  CTA → "Tap Untuk Claim Offer"

Compliance:
  HARD BLOCK if promo_confirmed = false

REJECT if:
  - Promo badge present but operator has not confirmed active promo
  - Product label covered by badge
  - Fake discount percentage
```

---

### ARCHETYPE E — UGC_SCALE_AD

```
Selling job:
  Natural proof — real scale, TikTok-organic feel, hand-held product.

Visual anchor:
  Hand holding product in natural context. Scale is obvious from hand proportion.

Module stack:
  [1] HAND_SCALE     — product in natural hand grip, label visible
  [2] SOFT_HOOK      — casual BM-native hook from HOOK_FAMILY_SCALE
  [3] MINIMAL_CHIPS  — 2 chips max: "5ML Roll-On" + one from allowed pool
  [4] CTA_BUTTON     — "Klik Untuk Tengok Harga"
  [5] NATURAL_ENV    — no studio feel; background natural or contextual

Layout zones (9:16):
  Hand + product: mid dominant
  Hook:           top, casual weight (not bold-commercial style)
  Chips:          minimal, bottom cluster
  CTA:            bottom

Copy pool anchor:
  Hook → HOOK_FAMILY_SCALE (casual register)
  Chips → "5ML Roll-On" + ONE of: "Mudah Bawa" / "Muat Poket" / "Kecil & Kemas"
  CTA → "Klik Untuk Tengok Harga"

Compliance:
  No face required / no sexual cue / no body-effect language
  Product label must be visible — not cropped, not blurred

REJECT if:
  - Pure product photo with no human scale element → route to SCALE_PROOF_AD instead
  - "Berkesan" or any efficacy chip present
  - More than 2 benefit chips
  - Body or sexual implication in visual or copy
```

---

## Module Completeness Matrix

| Archetype | Hook | Product Hero | Chips | CTA | Scale Object | Promo Badge |
|---|---|---|---|---|---|---|
| SCALE_PROOF_AD | ✅ required | ✅ required | ✅ required (3) | ✅ required | ✅ required | ❌ forbidden unless confirmed |
| PRIVATE_CARRY_AD | ✅ required | ✅ required | ✅ required (3) | ✅ required | ➖ optional | ❌ forbidden unless confirmed |
| PREMIUM_TRUST_AD | ✅ required | ✅ required | ✅ required (2–3 factual) | ✅ required | ❌ not applicable | ❌ forbidden unless confirmed |
| PROMO_AD | ✅ required | ✅ required | ✅ required (3) | ✅ required | ➖ optional | ✅ required (only if confirmed) |
| UGC_SCALE_AD | ✅ required | ✅ required | ✅ required (2 max) | ✅ required | ✅ required (hand) | ❌ forbidden unless confirmed |

---

## Reject Conditions — Universal

```
REJECT poster output if any of the following are true:

CBTC_REJECT:
  Output is product + headline + CTA only with no benefit chips
  and no module stack elements beyond basic three
  and image_goal = SELLING_POSTER

TEXT_FIRST_REJECT:
  Text block is taller than product in frame
  OR headline visual weight exceeds product visual weight

PRODUCT_PHOTO_ONLY_REJECT:
  No commercial modules present
  Output looks like product photography, not an ad

MISSING_CTA_REJECT:
  No CTA element when archetype requires CTA

MISSING_CHIPS_REJECT:
  No benefit chips when archetype requires chips

FAKE_CLAIM_REJECT:
  Any chip or copy contains unverified claim (efficacy, medical, certifications)

FAKE_PROMO_REJECT:
  Promo badge present but promo_confirmed = false in product_record

LABEL_COVERED_REJECT:
  Product label not readable — covered by badge, chip, or text element
```

---

## Version

```
kernel_version: v1
status: ACTIVE
pr: #32A
governs: BOSMAX commercial poster generation (SELLING_POSTER image_goal)
authority: SUPREME_SYSTEMS_ARCHITECT
consumers:
  - bosmax-commercial-poster-director.md
  - bosmax-scene-engine.md
  - bosmax-compliance-gate.md
```
