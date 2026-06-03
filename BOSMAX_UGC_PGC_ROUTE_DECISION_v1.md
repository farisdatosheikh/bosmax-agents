# BOSMAX UGC PGC ROUTE DECISION v1

Authority file for choosing the correct video presentation lane.

Purpose:
- stop random mixing between UGC and PGC
- clarify when BOSMAX should use `UGC`, `PGC`, or `HYBRID`
- reduce style drift before prompt generation begins

---

## 1. Core Definitions

### UGC

Use when the sales job depends on:
- relatability
- practical recommendation
- human-scale friction removal
- native social-commerce feel

Default characteristics:
- creator-visible
- gesture-led
- talk-to-camera or POV
- practical spoken rhythm
- fast proof

### PGC

Use when the sales job depends on:
- clean product truth
- premium object framing
- controlled visual hierarchy
- tighter compliance
- prestige or launch feel

Default characteristics:
- product-led
- cleaner composition
- tighter lighting discipline
- lower dependence on synthetic persona performance

### HYBRID

Use when both are needed:
- UGC open for relatability
- PGC proof for object trust

This is often the strongest default for AI-generated product video.

---

## 2. Decision Tree

### Choose UGC when:

- the product is low-risk
- the product solves a daily practical problem
- the buyer needs to feel "someone like me uses this"
- the product benefits from friction-removal language
- the category is household, kitchen, storage, gadget accessory, or practical commodity

### Choose PGC when:

- the category is sensitive, health-adjacent, premium, or visually precise
- the packaging truth matters more than creator relatability
- the product needs prestige, cleanliness, or technical clarity
- the risk of fake-testimonial interpretation is high

### Choose HYBRID when:

- the product needs both trust and conversion speed
- you want creator-native engagement but still need strong product inserts
- the category is moderate-risk and cannot rely on synthetic testimony alone

---

## 3. Category Routing

| Category | Default Route | Why |
|----------|---------------|-----|
| Household | `UGC` or `HYBRID` | Practical utility and proof carry the sale |
| Kitchen / storage / cleaning | `UGC` or `HYBRID` | Daily friction removal is strongest in creator-native framing |
| Gadget / accessory | `HYBRID` | Needs both demo utility and clear object proof |
| Beauty | `HYBRID` or `PGC` | Human framing helps, but product/application truth must stay tight |
| Fashion | `UGC` or `HYBRID` | Depends on whether the sale is about styling or brand polish |
| Wellness | `PGC` or `HYBRID` | Compliance and trust risk are high |
| Traditional / herbal | `PGC` or educator-style `HYBRID` | Avoid fake lived-experience proof |
| Sensitive products | `PGC` or educator-style `HYBRID` | Needs maximum control and minimum fake-testimonial risk |

---

## 4. Copy Style By Route

### UGC

Best formulas:
- `SELL_THROUGH_HPFRC`
- `STORY_HSARC`

Tone:
- direct
- practical
- compressed
- believable

### PGC

Best formulas:
- direct benefit explanation
- controlled authority explainer
- feature/advantage/proof/CTA

Tone:
- restrained
- cleaner
- more product-first
- less slang-dependent

### HYBRID

Best pattern:
- open like UGC
- prove like PGC
- close like direct-response commerce

---

## 5. Visual Grammar By Route

### UGC default

- MCU / Medium / POV / Hand Detail
- visible gestures
- conversational eye-line
- faster beat changes

### PGC default

- product hero
- insert
- close detail
- controlled push-in
- cleaner frame symmetry

### HYBRID default

- creator-facing hook
- then insert / hand detail / POV / product hero proof
- then creator or object-led CTA close

---

## 6. Route Red Flags

### UGC red flags

- synthetic persona sounds like fake customer testimony
- premium object truth becomes secondary
- too much talking with not enough proof

### PGC red flags

- beautiful but empty
- object shown but no practical meaning
- too static or too sterile for social-commerce context

### HYBRID red flags

- route confusion
- both human and product fight for dominance
- overcutting without clear beat purpose

---

## 7. BOSMAX Default Rules

If user does not specify route:

- household / practical product → default `HYBRID`
- beauty / gadget / fashion → default `HYBRID`
- premium launch → default `PGC`
- wellness / traditional / sensitive → default `PGC` or educator-style `HYBRID`

If product truth is fragile:
- prefer `PGC` or `HYBRID`

If creator relatability is the main hook:
- prefer `UGC` or `HYBRID`

---

## 8. Output Requirement

Before storyboard, BOSMAX should declare:
- `presentation_route = UGC | PGC | HYBRID`
- `why this route was chosen`

This must happen before detailed beat design.
