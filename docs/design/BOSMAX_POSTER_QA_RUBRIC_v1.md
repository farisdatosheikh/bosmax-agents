# BOSMAX Poster QA Rubric v1

## Status

`DRAFT — PENDING PILOT TEST`

Defines scoring dimensions, pass gates, rejection conditions, and QA reporting
format for BOSMAX commercial poster outputs. Not yet injected into
`bosmax-compliance-gate` runtime.

---

## Purpose

Every BOSMAX commercial poster prompt and output must be scored before it is
released to the image generation engine (Prompt-Level QA) and before it is
released to the production queue or Notion template library (Output-Level QA).

This rubric is the canonical scoring authority. It eliminates the current state
where outputs are "technically correct but commercially weak" — a poster can pass
compliance checks and still fail as a commercial asset.

---

## Scoring Dimensions

Ten dimensions. Each scored 1–10. Total maximum = 100.

| # | Dimension | What it measures |
|---|---|---|
| 1 | Product Truth | Bottle geometry, cap, label text, product category correctness |
| 2 | Scale Proof | Does the composition prove the correct physical size without text? |
| 3 | Label Fidelity | Is the BOSMAX HERBS label readable and unaltered? |
| 4 | Commercial Clarity | Is the selling goal immediately clear to a cold viewer? |
| 5 | Scroll-Stop Power | Does the composition create visual tension that stops a scroll? |
| 6 | Design Originality | Is this a genuinely fresh composition, not a generic stock photo feel? |
| 7 | TikTok Readability | Does the design function within TikTok UI safe zones on a mobile screen? |
| 8 | Compliance Safety | Are all STEALTH / DIRECT compliance constraints met? |
| 9 | Prompt Completeness | Does the prompt contain all 12 required sections? (Prompt-Level QA only) |
| 10 | Variation Discipline | If a variant: does it stay within declared variation axes? |

---

## Score Scale

| Score | Definition |
|---|---|
| 10 | Exceptional. Best-in-class for BOSMAX production. Could be a hero asset. |
| 9 | Strong. Production-ready with no reservations. |
| 8 | Good. Meets standard. Minor improvements possible but not blocking. |
| 7 | Acceptable minimum. Passes gate but should be improved in next revision. |
| 6 | Below standard. Fixable. Do not release until addressed. |
| 5 | Significant gap. Requires template or prompt rewrite. |
| 4 or below | Fundamental failure. Reject. Do not attempt to patch. |

---

## Production Pass Gate

An output passes production QA if and only if ALL of the following are true:

1. **Overall score ≥ 82 / 100**
2. **No single dimension below 7**
3. **Product Truth ≥ 9**
4. **Label Fidelity ≥ 9**
5. **Compliance Safety ≥ 9**
6. **No hard gate failure** (see Hard Gates section)

If an output scores 90 overall but Label Fidelity = 6, it fails.
Overall score does not override dimension minimums.

---

## Hard Gates

These are binary pass/fail checks that override the scoring matrix entirely.
A hard gate failure = automatic reject regardless of total score.

| Gate | Check |
|---|---|
| HG-01 | Product geometry is correct (bottle shape, cap, body color) |
| HG-02 | Product label is present and readable |
| HG-03 | BOSMAX HERBS text is not garbled, mutated, or missing |
| HG-04 | Product is not misidentified as perfume / dropper / deodorant / cosmetic serum |
| HG-05 | No impossible hand anatomy (correct finger count, correct joints) |
| HG-06 | No explicit sexual implication in composition or avatar pose |
| HG-07 | No medical cure claim in overlay text |
| HG-08 | No guaranteed result language in overlay text |
| HG-09 | No fake badge or certification icon present |
| HG-10 | TikTok safe zone (top 8%, bottom 20%) is not blocked by primary product |
| HG-11 | No competitor product visible in frame |
| HG-12 | CTA or overlay text does not cover the product label |

All 12 hard gates must be PASS. A single hard gate FAIL = reject.

---

## Auto-Reject Conditions

These specific conditions trigger immediate rejection. They map to hard gates
and design skill rejection rules.

| Condition | Dimension hit | Gate |
|---|---|---|
| Wrong bottle geometry (not cylindrical tube) | Product Truth | HG-01 |
| Wrong cap (wrong color, wrong shape, missing) | Product Truth | HG-01 |
| Wrong body color (not white / off-white) | Product Truth | HG-01 |
| Label redesigned (different font, different background, repositioned) | Label Fidelity | HG-02 |
| BOSMAX HERBS label unreadable or mutated in product-truth templates | Label Fidelity | HG-03 |
| Bottle appears larger than lip balm scale unless intentional macro — and macro still lacks scale context | Scale Proof | HG-01 |
| Impossible hand anatomy (extra fingers, melted fingers, wrong joint count) | Product Truth | HG-05 |
| Explicit sexual implication | Compliance Safety | HG-06 |
| Medical cure / improvement claim in overlay | Compliance Safety | HG-07 |
| Fake badge or certification not in product_record | Compliance Safety | HG-09 |
| Guaranteed result language ("dijamin", "guaranteed", "100% works") | Compliance Safety | HG-08 |
| CTA or text overlay covering the BOSMAX HERBS label | Label Fidelity | HG-12 |
| TikTok UI safe-zone blocked by primary design content | TikTok Readability | HG-10 |
| Product reads as perfume, deodorant, dropper, or cosmetic serum | Product Truth | HG-04 |
| Competitor product visible in frame | Compliance Safety | HG-11 |

---

## Commercially Boring But Technically Correct Definition

An output is "Commercially Boring But Technically Correct" (CBTC) when:

- Product geometry is correct (passes Product Truth)
- Label is readable (passes Label Fidelity)
- Compliance is clean (passes Compliance Safety)
- BUT: the composition is generic, the visual mechanic is undefined, there is no
  scroll-stop tension, the layout follows no formula, and the design would be
  indistinguishable from any random product photo

CBTC outputs will typically score:
- Product Truth: 9
- Label Fidelity: 9
- Compliance Safety: 9
- Scale Proof: 6 or below (no scale proof established)
- Commercial Clarity: 5 (no clear commercial trigger)
- Scroll-Stop Power: 4 (generic composition)
- Design Originality: 4 (stock photo feel)
- TikTok Readability: 7 (safe zones ok but not optimised)
- **Total: ~62 — FAILS production gate**

This is the exact failure mode of v0.1 BOSMAX templates. This rubric is designed
to catch and reject CBTC outputs rather than releasing them as if they were
production-quality commercial assets.

---

## QA Checklist

### Prompt-Level QA (before submitting prompt to image engine)

Run before any prompt is submitted to an image generation model.

| Check | Pass condition |
|---|---|
| All 12 sections present | Section headers 1–12 all present |
| Section 2 matches product_truth_lock | Geometry, cap, label, color verbatim |
| Scale anchor verbatim in Section 3 | Exact string from product_record |
| Negative constraints non-empty | Section 10 has at least 5 constraints |
| Hand anatomy constraint present | If hand in composition: anatomically correct hand constraint in Section 10 |
| Compliance class matches Section 9 | STEALTH or DIRECT constraints are injected correctly |
| Text rendering mode correct | Section 8 reflects template_card.text_rendering_mode |
| Layout formula declared | Section 4 identifies the layout formula |
| Visual mechanic declared | Section 5 identifies the mechanic |
| No filler language | No "beautiful scene", "creative composition", or equivalent filler |
| Commercial tone present | Section 11 is specific, not generic |

All 11 checks must pass before prompt is submitted.

### Output-Level QA (after image is generated)

Run on each generated image before it is released to production or Notion.

| Check | Method |
|---|---|
| Bottle geometry correct | Visual inspection against product_record geometry |
| Cap present and correct | Visual inspection |
| Label readable | Check BOSMAX HERBS visible at 1× zoom on 1080×1920 |
| Scale proof established | Verify scale proof mechanic executed in composition |
| Safe zones clear | Overlay TikTok UI chrome wireframe and check collision |
| No hand anatomy failure | Visual inspection of finger count and joint articulation |
| No wrong product category | Confirm product does not look like perfume / dropper / deodorant |
| Overlay text (if any) not on label | Confirm CTA/text does not occlude label area |
| Commercial trigger evident | Can a cold viewer identify the selling goal in 1.5 seconds? |
| QA scoring: all 10 dimensions scored | Record score against each dimension |
| Dimension minimums met | No dimension below 7 |
| Product Truth ≥ 9 | Hard minimum |
| Label Fidelity ≥ 9 | Hard minimum |
| Compliance Safety ≥ 9 | Hard minimum |
| Overall ≥ 82 | Hard minimum |

### Variation Batch QA

Run when a batch of variants is generated from one master template card.

| Check | Pass condition |
|---|---|
| Variant count ≤ 5 per batch run | Enforce via Universal Variation Controller |
| Each variant declares changed axes | `Changed axes:` log present in each variant |
| Maximum 3 axes changed per variant | Reject if 4+ axes differ from master |
| No frozen control changed | Compare variant to master frozen_controls list |
| All variants score ≥ 77 | Within 5 points of master baseline |
| Variant template objective preserved | SCALE_PROOF templates still prove scale; etc. |
| No variant produces CBTC result | Apply full CBTC definition check to each variant |

---

## Pilot Test Protocol

Before releasing any template family to production, run a 5-variant pilot test.

```
PILOT TEST PROTOCOL v1

Step 1: Select one master Template Card (v1 schema)
Step 2: Run full prompt expansion (12-section format)
Step 3: Submit master prompt to image engine
Step 4: Score output against all 10 QA dimensions
Step 5: If master fails — identify failure dimensions, revise template card, repeat
Step 6: If master passes — generate 3 variants via Universal Variation Controller
Step 7: Score each variant
Step 8: Confirm all variants score within 5 points of master
Step 9: Confirm no variant produces a hard gate failure
Step 10: Document: master score, variant scores, change log per variant
Step 11: If pilot passes — template family approved for production scale
Step 12: If pilot fails — identify root cause (template card vs expansion contract
          vs model limitation) before scaling

Minimum pilot requirement before 01A rewrite: 5 template families × 5 outputs = 25
```

---

## Human Review Required Cases

Some outputs must be reviewed by a human operator before release,
regardless of automated QA score.

| Case | Reason |
|---|---|
| First output from a new template card | No baseline established yet |
| Any output with `creative_intensity = SCROLL_STOPPER` | Higher risk of safe-zone and compliance edge cases |
| Any output where model route is first-time use | Text fidelity and geometry unverified for that model |
| Any output containing overlay text near label area | Label occlusion risk |
| Any output where `compliance_class = HIGH` or `RED` | REVIEW_ONLY products — mandatory human gate |
| Any output that scores exactly 82 overall | Marginal pass; human spot-check recommended |
| Any variant that scores within 2 points of fail threshold | Trend risk across batch |

---

## Reporting Format

After each QA run, return a structured report in this format:

```
--- BOSMAX POSTER QA REPORT ---
Template: [template_set_id]
Output: [output_id or filename]
Run type: [MASTER / VARIANT N / BATCH]
Scored by: [AGENT / HUMAN]
Date: [YYYY-MM-DD]

DIMENSION SCORES:
  1. Product Truth:         [score] / 10
  2. Scale Proof:           [score] / 10
  3. Label Fidelity:        [score] / 10
  4. Commercial Clarity:    [score] / 10
  5. Scroll-Stop Power:     [score] / 10
  6. Design Originality:    [score] / 10
  7. TikTok Readability:    [score] / 10
  8. Compliance Safety:     [score] / 10
  9. Prompt Completeness:   [score] / 10
  10. Variation Discipline: [score] / 10

TOTAL: [sum] / 100

GATE RESULTS:
  Overall ≥ 82:               [PASS / FAIL]
  No dimension below 7:       [PASS / FAIL]
  Product Truth ≥ 9:          [PASS / FAIL]
  Label Fidelity ≥ 9:         [PASS / FAIL]
  Compliance Safety ≥ 9:      [PASS / FAIL]

HARD GATES: [ALL PASS / FAILED: HG-xx, HG-xx]

PRODUCTION VERDICT: [PASS — RELEASE TO PRODUCTION / FAIL — DO NOT RELEASE]

FAILURE NOTES (if FAIL):
  [Dimension or gate that caused failure]
  [Recommended action: revise template / revise prompt / reject and restart]

CBTC CHECK: [NOT CBTC / CBTC DETECTED — DO NOT RELEASE]
--- END QA REPORT ---
```
