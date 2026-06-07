# BOSMAX Google Flow Extend Prompt SOP v1

Date: 2026-06-07
Status: ACTIVE
Authority: BOSMAX senior systems architect

Related files:
- `docs/engine_extension_prompt_syntax_policy_v1.md`
- `docs/google_flow_parity_audit_v1.md`
- `BOSMAX_VEO31_FLOW_CONTRACT_DECISION_v1.md`
- `registries/video_engine_duration_contracts.yaml`

---

## 1. Scope

This SOP governs the authoring of final operator-facing prompt text for:

- `GOOGLE_FLOW.FLOW_EXTEND_UI` — Google Flow Extend via the Flow web UI
- `GOOGLE_FLOW.FLOW_EXTEND_VERTEX` — Vertex AI Veo Extend (provisional; NEEDS_REVIEW)

It does NOT cover the base generation prompt for Block 1 of a Flow video.
Block 1 follows the standard BOSMAX 9-section script format.

---

## 2. How Google Flow Extend Works

**Official documented behaviour (verified 2026-06-05):**

Google Flow Extend continues a video from its prior clip. The engine uses the
**final second of the prior clip** as its continuation basis. The operator
provides a text prompt describing what should happen next.

This means:
- The engine already "knows" the visual state at the end of Block 1
- The prompt should describe the NEXT action, not repeat or describe the
  current visual state
- Explicit continuity meta-phrases such as "continue from" are redundant
  because the engine handles continuation natively

**Vertex AI Veo Extend (provisional):**

Vertex AI Veo Extend accepts a 1-30s input video and produces a 7s extension.
This surface is documented in Vertex AI official docs. BOSMAX treats this as
NEEDS_REVIEW pending a dedicated proof lane.

---

## 3. Block Duration by Surface

| Surface | Production block duration | WPS basis | Notes |
|---|---|---|---|
| `FLOW_EXTEND_UI` | 8s | 8s | Flow UI; 8s per extend step |
| `FLOW_EXTEND_VERTEX` | 7s | 7s | Vertex docs; NEEDS_REVIEW |

---

## 4. Internal Metadata (stays internal, never in prompt text)

The following fields exist in BOSMAX block planning and Notion schema.
They must NOT appear verbatim in the final prompt text that the operator
pastes into the Google Flow UI:

| Field | Where it lives | Why it must NOT enter prompt |
|---|---|---|
| `previous_clip_final_second_state` | Block planning YAML | Flow uses this natively; verbalising it is redundant and may add noise |
| `bridge_in_required: true` | Block planning YAML | Planning flag only |
| `[CONTINUES FROM BLOCK N]` | Child prompt output rule (internal) | BOSMAX planner notation; not a Flow instruction |
| `BLOCK X OF N` | Section 8 (internal) | BOSMAX block audit label; not engine instruction |
| `identity_reanchor_required` | Block planning YAML | Planning flag only |
| `product_reanchor_required` | Block planning YAML | Planning flag only |
| `WPS budget` / word counts | Planning layer | Planning metadata only |

---

## 5. Identity Reference Rules for Flow Extend

### When a named ingredient exists in the current Flow project

Use the `@` reference syntax:

```
@NadiaCooks picks up the product bottle and turns it toward the camera.
```

```
@MinyakBotol rotates slowly as she holds it up against the kitchen light.
```

### When no named ingredient exists

Use a concrete noun. Do NOT use generic placeholder tokens.

Allowed:
```
the man
the woman
the presenter
the product bottle
the serum bottle
```

Forbidden (policy-banned generic tokens):
```
the character
the subject
the individual
the person
```

Rationale: generic tokens give Flow no grounding. The engine may drift visual
identity across extension blocks when anchored only to a generic noun.

---

## 6. Policy-Banned Phrases for Flow Extend Prompt Text

The following phrases are BOSMAX policy-banned from Flow Extend prompt text.
They are not an officially documented Google hard ban; they are BOSMAX-imposed
to prevent semantic noise and avoid redundancy with the engine's own
continuation mechanism.

```
"continue from the last frame"
"continue from the previous clip"
"continue from where we left off"
"the video continues"
"seamless continuation"
"exactly the same face"
"biometric anchor"
"[CONTINUES FROM BLOCK]"
"BLOCK X OF N"
"bridge-in"
"bridge-out"
"previous_clip_final_second_state"
```

---

## 7. What to Write Instead

The Flow Extend prompt should describe only:

1. **What the presenter does next** — action, movement, gesture
2. **What the product does next** — reveal, rotation, pick-up, pour
3. **Camera** — angle change, zoom direction, hold on subject
4. **Setting continuity** — if needed, one phrase confirming the same space
5. **Dialogue or speech intent** — if the video has speech, the next spoken content
6. **Emotional tone** — expression, pace, energy

### Examples

#### BAD (policy-banned, do not use):
```
Continue from the last frame. The video continues seamlessly. Exact same face
and identity. She picks up the product.
```

#### GOOD:
```
The woman reaches across the kitchen counter and picks up the small serum bottle.
She holds it close to the camera with a confident smile. Warm natural light.
Medium close-up. Soft ambient audio.
```

---

#### BAD (internal metadata leaked, do not use):
```
[CONTINUES FROM BLOCK 1] — BLOCK 2 OF 2. Bridge-in: she continues talking.
previous_clip_final_second_state: woman standing at kitchen counter.
She says "...cubaan la dulu."
```

#### GOOD:
```
She looks directly at the camera and says "Cubaan la dulu, confirm tak menyesal."
She sets the bottle down gently on the counter. Close-up on the bottle.
Soft kitchen lighting. Calm, warm tone.
```

---

## 8. Multi-Block Sequence Rules for Flow Extend

When generating a multi-block Flow video (e.g. 2 or 3 extension steps):

| Rule | Requirement |
|---|---|
| Block 1 | Generated as normal BOSMAX 9-section script; no extension-specific rules apply |
| Block 2+ | Apply this SOP; prompt starts with the next action directly |
| Visual continuity | Flow engine uses the prior clip's final second; do NOT describe the start state |
| Dialogue continuity | Continue the semantic thread; do NOT restart greeting or hook |
| Identity anchor | Use `@CharacterName` if asset exists; otherwise concrete noun |
| Internal fields | All block planning fields stay in YAML and Notion; none enter prompt text |

---

## 9. FLOW_EXTEND_VERTEX Notes (Provisional)

Vertex AI Veo Extend documentation confirms:

- Input: 1-30s video clip
- Output: 7s extension per call
- API parameter: `video` (input), `prompt` (text description)
- `image_guidance_scale` does NOT exist in the Vertex API — it is a UI-only parameter
  in the Flow web app. Do NOT include this in Vertex API calls.

BOSMAX provisional rules for Vertex prompt text:

- Same policy-banned phrases as Flow UI (section 6)
- Same identity reference rules (section 5)
- Same metadata separation rules (section 4)
- WPS basis for Vertex: 7s per block (7s actual extension duration)

Status: NEEDS_REVIEW — do not promote to production until a dedicated Vertex
proof lane is added to the BOSMAX repo.

---

## 10. Compliance Checklist Before Emitting Flow Extend Prompt

Before any Flow Extend prompt is emitted to the operator:

- [ ] No policy-banned continuity phrases present
- [ ] No internal metadata fields (`previous_clip_final_second_state`, `[CONTINUES FROM BLOCK]`, etc.) in prompt text
- [ ] Identity reference uses `@CharacterName` or concrete noun — not generic token
- [ ] Prompt describes next action, not current visual state from prior clip
- [ ] Dialogue continues semantic thread — no greeting restart
- [ ] Surface declared correctly (FLOW_EXTEND_UI vs. FLOW_EXTEND_VERTEX)
- [ ] WPS budget applied correctly (8s for UI, 7s for Vertex)
