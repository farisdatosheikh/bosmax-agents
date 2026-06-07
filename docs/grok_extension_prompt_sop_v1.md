# BOSMAX GROK Extension Prompt SOP v1

Date: 2026-06-07
Status: ACTIVE
Authority: BOSMAX senior systems architect

Related files:
- `docs/engine_extension_prompt_syntax_policy_v1.md`
- `BOSMAX_GROK_EXTENSION_SEAM_TEMPLATES_v1.md`
- `BOSMAX_VEO31_FLOW_CONTRACT_DECISION_v1.md`
- `registries/video_engine_duration_contracts.yaml`
- `samples/notion/video_multi_block_templates.yaml`

---

## 1. Scope

This SOP governs the authoring of final operator-facing prompt text for GROK
multi-block video extension chains within the BOSMAX system.

It covers:
- Block 1 prompt (generation)
- Block 2+ prompts (extension)
- Seam handling between blocks
- Identity reference conventions
- Speech resume timing
- Policy-banned phrases

It does NOT alter BOSMAX block duration contracts, GROK registry values, or
any runtime resolver behaviour.

---

## 2. BOSMAX GROK Production Contract

| Parameter | Value | Basis |
|---|---|---|
| Valid block durations | `6s` or `10s` | BOSMAX production-safety contract |
| Extension mechanism | Block chaining via GROK extension | Observed SuperGrok UI lane + xAI docs |
| Multi-block trigger | Target > 10s | ENGINE CONSTRAINT TABLE |
| Max observed chain total | 30s (SuperGrok app lane) | Observed empirical; not from xAI API docs |

**Important distinction:**

xAI documentation supports 2-10s extension durations in general terms for the
extension capability. BOSMAX production contract locks to `[6, 10]` for
production-safety and continuity control. Do not represent this as an xAI
capability limit.

A `GROK_FLEX_EXTEND` lane using xAI's broader duration range may be created in
a future PR after dedicated approval and testing. It is NOT available currently.

---

## 3. BOSMAX Default Block Distributions

| Total target | BOSMAX default | Notes |
|---|---|---|
| 12s | 2 × 6s | Only valid 6s combination |
| 16s | 10s + 6s | Only valid BOSMAX combination |
| 18s | 3 × 6s | Only valid 6s combination |
| 20s | 2 × 10s | Only valid BOSMAX combination |
| 30s | 3 × 10s | BOSMAX default; 5×6s alternate only on explicit operator request |

When a distribution is the only valid BOSMAX option, BOSMAX announces it
directly without asking. When an alternate exists (e.g. 30s: 3×10s vs. 5×6s),
BOSMAX defaults to the standard and offers the alternate only on explicit
operator request.

---

## 4. Seam Law — Core Rule

**BOSMAX GROK SEAM LAW:**

> Speech must resume within **0.5s–1.0s** of the seam between blocks.
> No dead air. No greeting restart. No product re-introduction.
> Block 2 picks up the sentence thread.

This means:

- Block 1 must end mid-thought or with a clear semantic bridge-out
- Block 2 must begin with the continuation of that thread within 0.5–1.0s
- There is no pause, re-greeting, or scene reset between blocks

The bridge-out and bridge-in are BOSMAX planning concepts.
They must NOT appear as literal field names in the operator-facing prompt text.

---

## 5. Identity and Product Reanchor Rules for GROK Extension

Unlike VEO_3_1_LITE CLIP_CHAIN, GROK extension **does not require** explicit
identity_reanchor or product_reanchor in Block 2.

The GROK extension model persists the visual state from Block 1. Explicit
reanchor language can introduce competing instructions that override the
model's own continuation.

| Field | Block 1 | Block 2+ |
|---|---|---|
| `identity_reanchor_required` | `false` | `false` |
| `product_reanchor_required` | `false` | `false` |

**Exception:** if identity drift is observed in testing, a brief optional
biometric descriptor (hair, build, outfit colour) may be added tactically.
This is NOT mandatory SOP and should not be applied as default.

---

## 6. Identity Reference Rules for GROK

GROK does not support `@CharacterName` syntax (this is a Google Flow feature).

Use concrete nouns:

Allowed:
```
the woman
the man
the presenter
the serum bottle
the product
```

Optional tactical biometric descriptor (when drift is a concern):
```
the woman in the hijab with a dark green top
```

Forbidden:
```
the character
the subject
the individual
the person
"exact same face"
"biometric anchor"
```

---

## 7. Policy-Banned Phrases for GROK Extension Prompt Text

The following phrases are BOSMAX policy-banned from GROK extension prompt text:

```
"continue from the last frame"
"continue from the previous clip"
"the video continues"
"[CONTINUES FROM BLOCK]"
"BLOCK X OF N"
"seamless continuation"
"exact same face"
"biometric anchor"
"bridge-in"
"bridge-out"
"previous_clip_final_second_state"
"identity_reanchor_required"
"product_reanchor_required"
"WPS budget"
```

Note: `[CONTINUES FROM BLOCK N]` is valid in the **internal block planning
YAML and Notion schema**. It is policy-banned only in the final operator-facing
prompt text that gets pasted into the GROK extension UI.

---

## 8. Internal Metadata (planning layer only)

These fields are required at the BOSMAX planning and Notion schema layer.
They must NOT appear verbatim in the operator-facing prompt text:

| Field | Where it lives |
|---|---|
| `[CONTINUES FROM BLOCK N]` | `child_prompt_output_rule` in block YAML |
| `BLOCK X OF N` | Section 8 in block planning (internal) |
| `speech_resume_window_seconds` | Block planning YAML |
| `bridge_in_required` | Block planning YAML |
| `bridge_out_required` | Block planning YAML |
| `identity_reanchor_required` | Block planning YAML |
| `product_reanchor_required` | Block planning YAML |
| WPS word counts | Planning layer |

These are enforced by the validator and used by the compliance gate. They do
not travel into the final prompt.

---

## 9. Seam Template Examples

The following examples are derived from `BOSMAX_GROK_EXTENSION_SEAM_TEMPLATES_v1.md`.

### Template A — Soft Household

**Block 1 ending (bridge-out setup):**
```
She holds the bottle up and says, "Dah cuba macam-macam tapi rasa macam tak..."
```

**Block 2 start (bridge-in, within 0.5–1.0s of seam):**
```
"...cukup lagi kan?" She smiles and opens the cap. Close-up on the product.
```

The speech thread is mid-sentence. The audience does not notice the cut.

---

### Template B — Direct Recommendation

**Block 1 ending:**
```
"Kalau nak kulit lebih lembap, satu benda je yang saya nak recommend..."
```

**Block 2 start:**
```
"...ni lah." She taps the bottle on her palm. "Dah guna tiga minggu, result
memang nampak." Medium shot. Product in foreground.
```

---

### Template C — Savage Sell-Through

**Block 1 ending:**
```
"Serious tak tipu — dah penat buang duit dengan produk yang..."
```

**Block 2 start:**
```
"...tak buat apa. Cuba yang ni sekali. RM[X] je, free shipping." She holds
the product directly to camera. Tight close-up. Direct eye contact.
```

---

## 10. Prompt Structure Guide for GROK Block 2

Block 2 operator-facing prompt text should contain:

1. **Speech continuation** — the next spoken line, picking up the thread immediately
2. **Presenter action** — gesture, product pick-up, or movement
3. **Product moment** — what the product does or is shown doing
4. **Shot type** — medium, close-up, tight, POV
5. **Lighting / tone** — one line confirming the space or shifting energy if needed

It should NOT contain:
- Any internal BOSMAX planning field names
- Any explicit continuity meta-phrases (policy-banned, section 7)
- Any re-greeting or scene reset
- Block index labels

---

## 11. Compliance Checklist Before Emitting GROK Extension Prompt

Before any GROK extension block prompt is emitted to the operator:

- [ ] No policy-banned continuity phrases present
- [ ] No internal metadata fields in prompt text
- [ ] Identity uses concrete noun (or tactical biometric descriptor only if justified)
- [ ] `@CharacterName` syntax NOT used (this is Flow-only)
- [ ] Speech resumes within 0.5–1.0s of seam — verified via block_plan timing
- [ ] No greeting restart in Block 2
- [ ] Block duration is `6s` or `10s` (BOSMAX production contract)
- [ ] No reference to `GROK_FLEX_EXTEND` — that lane does not yet exist
- [ ] Multi-block distribution confirmed before prompt generation begins

---

## 12. GROK_FLEX_EXTEND — Future Lane (Not Yet Active)

xAI documentation supports extension durations in the 2-10s range in general
capability terms. BOSMAX has not yet created a production lane for these
non-standard durations.

A `GROK_FLEX_EXTEND` lane will be created only after:

1. Dedicated testing of non-standard durations (e.g. 4s, 7s, 8s) against
   the BOSMAX seam law and speech-resume window
2. Explicit approval from BOSMAX senior architect
3. Registry entry created in `video_engine_duration_contracts.yaml`
4. SOP amendment to this document

Until then: production GROK block durations remain `[6, 10]` exclusively.
Do not use intermediate durations in BOSMAX outputs even if the GROK UI
or API would accept them.
