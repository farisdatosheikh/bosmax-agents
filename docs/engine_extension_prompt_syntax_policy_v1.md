# BOSMAX Engine Extension Prompt Syntax Policy v1

Date: 2026-06-07
Status: ACTIVE
Authority: BOSMAX senior systems architect

Related files:
- `BOSMAX_VEO31_FLOW_CONTRACT_DECISION_v1.md`
- `docs/google_flow_parity_audit_v1.md`
- `docs/google_flow_extend_prompt_sop_v1.md`
- `docs/grok_extension_prompt_sop_v1.md`
- `BOSMAX_GROK_EXTENSION_SEAM_TEMPLATES_v1.md`
- `registries/video_engine_duration_contracts.yaml`

---

## 1. Purpose

This policy document defines what belongs in final engine-visible prompt text
versus what belongs in BOSMAX internal planning and continuity metadata.

The problem it solves:

BOSMAX block planning requires rich internal metadata — previous clip final-second
state, bridge-in phrases, bridge-out phrases, `[CONTINUES FROM BLOCK N]` markers,
WPS budgets, block role identifiers, and continuity proofs. This metadata is
essential for BOSMAX planning, Notion handoff schema, validator checks, and
operator auditing.

However, these internal planning fields must not leak verbatim into the final
text that operators paste into engine UIs such as Google Flow Extend or GROK
extension. Different engines behave differently when they encounter explicit
meta-continuity language in the prompt-visible surface. For Flow Extend, the
engine already uses the prior clip's final second as its continuation basis;
injecting phrases like "continue from the last frame" is redundant at best and
may compete with the engine's own continuation mechanism.

This policy establishes a clean, engine-specific rule for each relevant surface.

---

## 2. Scope

This policy applies to:

| Engine Surface | Coverage |
|---|---|
| `GOOGLE_FLOW.FLOW_EXTEND_UI` | Full policy rules |
| `GOOGLE_FLOW.FLOW_EXTEND_VERTEX` | Provisional rules (NEEDS_REVIEW surface) |
| `VEO_3_1.CLIP_CHAIN` | Prompt-visible guidance |
| `VEO_3_1_LITE.CLIP_CHAIN` | Prompt-visible guidance |
| `GROK_EXTENSION` | Full policy rules |

Out of scope: `KLING_3_0`, `SEEDANCE_2_0`, `NANO_BANANA_PRO`, `IMAGEN_3`.
These engines are K.I.V. or image-only and are not addressed by this policy.

---

## 3. Core Separation: Internal Metadata vs Final Prompt Text

### 3.1 Internal BOSMAX metadata (never in final prompt text)

These fields are required at the planning, Notion schema, and validator layer.
They must NOT appear verbatim in operator-facing engine prompt text:

- `previous_clip_final_second_state` values
- `bridge_in_required` / `bridge_out_required` field names
- `[CONTINUES FROM BLOCK N]` markers
- `BLOCK X OF N` section identifiers
- Block role names (`HOOK`, `CTA`, `BODY`, `FRICTION_PROOF`, etc.)
- WPS budget numbers
- `identity_reanchor_required: true` field names
- `product_reanchor_required: true` field names
- `copywriting_id` values
- `avatar_pool_id` values
- `template_id` values
- Validator proof fields

### 3.2 Final prompt text (what enters the engine UI)

Final engine-visible prompt text should describe only:

- What the presenter/avatar does next
- Camera angle or movement
- Product motion or reveal
- Spatial setting and lighting continuity
- Spoken dialogue or speech timing intent
- Emotional tone of the scene
- Identity reference (using correct engine-appropriate syntax)

---

## 4. Engine-Specific Policy Matrix

| Engine Surface | Explicit meta-continuity phrases in prompt? | [CONTINUES FROM BLOCK] in prompt? | Identity tokens | Internal fields allowed in prompt? |
|---|---|---|---|---|
| `GOOGLE_FLOW.FLOW_EXTEND_UI` | Policy-banned | Policy-banned | `@CharacterName` or concrete noun | Never |
| `GOOGLE_FLOW.FLOW_EXTEND_VERTEX` | Policy-banned (provisional) | Policy-banned | Same as Flow UI | Never |
| `VEO_3_1.CLIP_CHAIN` | Avoid where final prompt text exists | Policy-banned | Concrete noun description | Never |
| `VEO_3_1_LITE.CLIP_CHAIN` | Avoid where final prompt text exists | Policy-banned | Concrete noun description | Never |
| `GROK_EXTENSION` | Not mandatory; preferred avoidance | Policy-banned | Concrete noun; optional brief biometric descriptor when critical | Never |

---

## 5. Official Evidence vs BOSMAX Policy — Distinction

BOSMAX makes the following explicit distinction between documented official
platform behaviour and BOSMAX-imposed internal policy:

### Official evidence (verified on 2026-06-05):

- Google Flow Extend uses the final second of the prior clip as its continuation
  basis. This is documented in the official Google Flow Help.
- Vertex AI Veo Extend accepts a 1-30s input video and produces a 7s extension.
  This is documented in Vertex AI official docs.
- GROK supports extension from prior clips. xAI documentation supports 2-10s
  extension durations in general capability terms.

### BOSMAX policy (repo-internal):

- BOSMAX policy-bans explicit continuity meta-phrases in final prompt text for
  Google Flow and GROK. This is a BOSMAX-imposed rule, not an officially
  documented Google or xAI hard ban.
- The rationale is that these phrases are redundant (Flow already handles
  continuation internally) and may introduce semantic noise.
- BOSMAX maintains the narrower production contract of `[6, 10]` for GROK
  block durations, even though xAI capability may support broader ranges.
  This is a production-safety contract, not a claim about xAI limits.

Do not represent BOSMAX policy as an official Google or xAI requirement when
communicating with operators.

---

## 6. Policy-Banned Phrases

The following phrases are policy-banned from final engine-visible prompt text
across all extension surfaces covered by this policy:

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

Note: the seam intent conveyed by these phrases is correct and necessary for
planning. The ban applies only to their verbatim presence in final prompt text.
The underlying continuity goal is achieved through the engine's own continuation
mechanism and through correct internal BOSMAX planning fields.

---

## 7. Identity Reference Policy

### 7.1 Google Flow (FLOW_EXTEND_UI and FLOW_EXTEND_VERTEX)

- Use `@CharacterName` or `@IngredientName` when that named asset exists inside
  the current Flow project.
- If no named ingredient exists, use a concrete noun:
  - `the man`
  - `the woman`
  - `the product bottle`
  - `the presenter`
- Policy-banned generic tokens:
  - `the character`
  - `the subject`
  - `the individual`
  - `the person`

Rationale: generic tokens provide Flow no useful grounding information and may
cause identity drift across extension blocks.

### 7.2 VEO_3_1 and VEO_3_1_LITE (CLIP_CHAIN)

- Use concrete noun descriptions for the presenter and product.
- Identity and product reanchor fields are required at the internal/planning
  layer on every continuation block.
- Do not use VEO-internal identity tokens that have no official documented basis.

### 7.3 GROK_EXTENSION

- Use concrete noun descriptions by default.
- Brief optional biometric-style descriptor (hair, build, outfit) is permitted
  as a tactical tool when identity consistency is at risk across blocks.
- It is not mandatory SOP and should not be injected into every GROK prompt.

---

## 8. Duration Posture Summary

| Engine Surface | Production block duration | Basis |
|---|---|---|
| `GROK_EXTENSION` | `6s` or `10s` per BOSMAX block | BOSMAX production-safety contract |
| `VEO_3_1.CLIP_CHAIN` | `8s` per block | Verified clip primitive |
| `VEO_3_1_LITE.CLIP_CHAIN` | `8s` API / `7s` actual-render WPS | Verified with render-lag note |
| `GOOGLE_FLOW.FLOW_EXTEND_UI` | `8s` per extend step | Reviewed Flow UI evidence |
| `GOOGLE_FLOW.FLOW_EXTEND_VERTEX` | `7s` per extend step | Vertex docs; NEEDS_REVIEW |

GROK note: xAI capability documentation supports broader extension durations
(2-10s extension range in general terms). BOSMAX production contract stays `[6, 10]`
for production safety. A `GROK_FLEX_EXTEND` lane may be created only after
separate approval and testing.

---

## 9. What This Policy Does NOT Change

This policy does not change any of the following:

- `VEO_3_1.CLIP_CHAIN` readiness — remains READY
- `VEO_3_1_LITE.CLIP_CHAIN` readiness — remains READY
- `GOOGLE_FLOW.FLOW_EXTEND_UI` readiness — remains READY_REVIEWED_FLOW_EXTEND
- `GOOGLE_FLOW.FLOW_EXTEND_VERTEX` status — remains NEEDS_REVIEW
- GROK production duration contract — remains `[6, 10]`
- Any duration registry values in `registries/video_engine_duration_contracts.yaml`
- Any runtime resolver behavior
- Any validator logic
- Any sample templates
- KLING_3_0 or SEEDANCE_2_0 status
- Internal metadata requirements (previous_clip_final_second_state, bridge-in,
  bridge-out, WPS, identity/product reanchor) — all remain required internally

---

## 10. Future Patch Sequence

| Item | Trigger | Action |
|---|---|---|
| `GROK_FLEX_EXTEND` lane | Separate approval + testing of broader xAI duration range | Create new registry entry and SOP |
| `GOOGLE_FLOW.FLOW_EXTEND_VERTEX` promotion | Dedicated proof lane added to repo | Update readiness in registry + decision record |
| `KLING_3_0` sample templates | Explicit in-scope decision | Add to `samples/notion/` and validator coverage |
| `SEEDANCE_2_0` sample templates | Explicit in-scope decision | Add to `samples/notion/` and validator coverage |
| Prompt syntax validator | Future sprint | Add CHECK for policy-banned phrases in sample template prompt_text fields |
