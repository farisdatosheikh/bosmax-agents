# BOSMAX MULTI-IMAGE BROLL CONTRACT v1

Authority file for handling many uploaded images in AI product video workflows.

Purpose:
- stop prompt conflict when users upload many images
- define authority hierarchy for product, avatar, environment, and B-roll
- distinguish what Grok can do well vs what Google Flow Ingredients can do better

---

## 1. Asset Classes

Every uploaded image must be classified into one of these:

### A. Product Truth Image

Controls:
- packaging geometry
- label hierarchy
- cap / lid / body structure
- true color
- scale anchor
- object identity

This is the highest authority image.

### B. Hero Identity Image

Controls:
- face identity
- outfit class
- hand class
- body scale
- overall human anchor

### C. Environment Image

Controls:
- room or outdoor context
- lighting mood
- background geometry
- material atmosphere

### D. Texture / Style Image

Controls:
- finish
- tone
- texture cues
- polish direction

### E. B-roll Support Image

Controls:
- secondary context
- lifestyle support
- alternative angle inspiration

This is lowest authority.

---

## 2. Authority Order

If two uploaded images conflict, BOSMAX must resolve by this order:

1. `Product Truth Image`
2. `Hero Identity Image`
3. `Environment Image`
4. `Texture / Style Image`
5. `B-roll Support Image`

No lower-ranked image may override a higher-ranked image.

---

## 3. Multi-Image Good Cases

Many images help when they show:
- the same product from multiple valid angles
- the same avatar in the same identity/outfit class
- the same environment from complementary angles
- supporting detail needed for inserts or macro proof

Many images do not help when they show:
- different packaging revisions
- different outfits that imply a new identity
- mood images that contradict the real product truth
- random inspiration boards mixed with operational references

---

## 4. B-roll Law

B-roll images should only be used if they help:
- prove a spoken point
- support a context line
- provide seam masking
- give a short insert beat without weakening product truth

B-roll should not be used as:
- filler to make video feel busy
- replacement for proof
- license to drift from the product or avatar truth

---

## 5. Grok vs Google Flow Ingredients

### GROK

Best treated as:
- reference pool
- identity support
- object support
- loose continuity support

Not safe to treat as:
- deterministic shot scheduler from many images
- exact per-second B-roll editor

Grok can benefit from many references, but BOSMAX should treat them as:
- priority anchors
- not timeline commands

### GOOGLE FLOW / INGREDIENTS

Best treated as:
- stronger compositing workflow
- stronger ingredient-based scene construction
- better candidate for multi-image creative assembly

Still not safe to treat as:
- exact non-linear editor timeline
- perfect guaranteed shot orchestration from ingredients alone

Google Flow Ingredients is the preferred engine when:
- user uploads many reference images
- multiple asset classes need to coexist
- object + character + environment all matter together

---

## 6. Engine Routing Rule

If user uploads:
- one hero image + one product image → `GROK` or `GOOGLE_FLOW` both viable
- many product/scene/support images → prefer `GOOGLE_FLOW Ingredients`
- many images but route requires hard commercial continuity → prefer segmented workflow with clear beat planning

If B-roll matters heavily:
- prefer planned beat-by-beat assembly
- do not rely on one giant prompt to "figure it out"

---

## 7. Segmented Workflow Rule

When many images exist, BOSMAX should think in:
- `hero beat`
- `proof beat`
- `context beat`
- `B-roll support beat`
- `CTA beat`

This means:
- classify images first
- assign each image to a beat purpose
- then choose the engine

Do not dump all images into one undifferentiated prompt.

---

## 8. Conflict Handling

If uploaded images conflict:
- choose highest authority asset
- declare the lower asset as support-only or discard it

Examples:
- product label A vs product label B → product truth image wins
- creator face A vs creator face B → hero identity image wins
- premium mood image contradicts real product context → mood image loses

---

## 9. BOSMAX Operator Requirement

Before generating video from many images, BOSMAX should declare:
- asset count
- asset classes
- authority order
- engine choice
- whether B-roll is:
  - none
  - light support
  - heavy support

If `heavy support`, BOSMAX should prefer a segmented shot plan rather than a single monolithic prompt.
