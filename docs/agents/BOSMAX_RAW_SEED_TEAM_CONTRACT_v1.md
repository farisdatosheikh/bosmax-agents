# BOSMAX Raw Prompt Seed Team Contract
# Version: v1
# Authority: BOSMAX Systems Architecture
# Status: CONTRACT ONLY — no skill files exist yet
# Last updated: 2026-06-08

---

## 1. CURRENT STATUS

The Raw Prompt Seed Team **does not currently exist** as skill files.

- **Skill files:** None created. Planned for a future PR after this contract is reviewed.
- **Orchestrator wiring:** Not present. Will require a dedicated route when skill files exist.
- **Current operator behaviour:** Raw seeds are created manually by the operator and stored in Notion without governed structure, deduplication, or compliance pre-screening.

This contract defines the intended purpose, team structure, role boundaries, and output format for the Raw Prompt Seed Team.

---

## 2. PURPOSE

The Raw Prompt Seed Team's job is to **generate, validate, deduplicate, and format raw creative prompt seeds for the Notion seed library**.

It operates entirely upstream of the final prompt team. Its output is not deployment-ready — it is creative raw material that the final prompt team will later expand and enforce into a deployment-ready prompt when the operator brings it into a Claude Code session.

**Why this team is needed:**
- Without governed seed creation, the Notion library accumulates low-quality, duplicate, and compliance-risky seeds
- Ad hoc seed creation by operators produces inconsistent hook formulas, category mismatches, and scale errors that propagate into final prompts
- A governed seed team catches these problems at the input layer, which is cheaper than fixing them at the output layer

---

## 3. ROLE BOUNDARY — CRITICAL DISTINCTION

```
RAW SEED TEAM                        FINAL PROMPT TEAM
─────────────────────────────────    ──────────────────────────────────
Operates in: generative/exploratory   Operates in: structured enforcement mode
mode
Input: product brief + platform +     Input: raw seed OR live operator
category (open-ended)                 requirement (specific)
Output: raw creative seed → Notion    Output: deployment-ready final prompt → user
Job: brainstorm, pressure-test,       Job: expand, validate, enforce SOP,
     deduplicate, format for storage  audit, format for generator
Mode: creates seeds                   Mode: expands seeds
───────────────────────────────────  ──────────────────────────────────────
NOT a deployment pipeline            IS the deployment pipeline
NOT producing prompts for generators IS producing prompts for generators
NOT doing compliance audit           IS doing compliance audit (via gate)
```

**A seed is not a final prompt.**
**A final prompt is not a seed.**
These two systems must remain separate. A seed that bypasses the final prompt team and goes directly to the generator is an ungoverned output — it will not have scale anchor validation, compliance gate clearance, or engine-specific formatting.

---

## 4. RECOMMENDED FUTURE ROLES

### Role 1: Raw Prompt Seed Director
- **Purpose:** Orchestrates the seed team; decides creative direction per product/platform/category
- **Inputs:** Product brief, platform, target format (image/video), category
- **Outputs:** Creative direction brief for downstream seed team roles
- **Does NOT do:** Generate individual seeds, format for Notion, audit for duplicates

### Role 2: Commercial Idea Miner
- **Purpose:** Generates raw hook/angle/concept variants from the creative direction brief
- **Inputs:** Product brief, creative direction from seed director, silo class, formula type
- **Outputs:** 5–10 raw hook + angle variants per brief (unformatted, unvalidated)
- **Does NOT do:** Product truth validation, compliance check, Notion formatting

### Role 3: Product Truth Guard
- **Purpose:** Validates each raw seed against the product_record — catches scale errors, false claims, packaging misrepresentation before the seed enters Notion
- **Inputs:** Raw seeds from idea miner, product_record (from products/*.yaml)
- **Outputs:** Approved seeds (pass) or rejected seeds with reason
- **Key check:** scale_anchor_descriptor compliance; no superlative claims without product evidence

### Role 4: Compliance Risk Filter
- **Purpose:** Screens approved seeds for platform compliance risk (TikTok health claim rules, Shopee prohibited categories, Meta advertising policies)
- **Inputs:** Product-truth-approved seeds, compliance_class from product_record, target platform
- **Outputs:** Green seeds (safe), yellow seeds (caution with note), red seeds (rejected with reason)
- **Does NOT do:** Final compliance audit — that remains bosmax-compliance-gate's role at the final prompt stage

### Role 5: Variation Architect
- **Purpose:** Structures variation across the approved seed set — ensures the batch covers different silos, formulas, personas, and hooks without duplication
- **Inputs:** Compliance-filtered seed set
- **Outputs:** Variation-mapped seed set with silo, formula, persona, and hook tags per seed
- **Key rule:** No two seeds in the same batch may share the same hook + silo + formula combination

### Role 6: Duplicate / Boring Seed Auditor
- **Purpose:** Scans the variation-mapped seeds against the existing Notion library to detect exact duplicates, near-duplicates, and seeds that are too generic to generate distinctive final prompts
- **Inputs:** Variation-mapped seeds, operator-provided Notion library snapshot (or operator confirms library state)
- **Outputs:** Unique seeds (cleared for Notion) + rejected seeds with reason (duplicate / too generic)
- **Does NOT do:** Access Notion directly — operator provides library context

### Role 7: Notion Seed Pack Formatter
- **Purpose:** Formats all cleared seeds into the standard Notion seed schema for operator import
- **Inputs:** Cleared and deduplicated seeds with variation tags
- **Outputs:** Formatted seed pack (see Section 5 for schema)
- **Does NOT do:** Import to Notion directly — outputs a formatted block the operator pastes manually

---

## 5. RAW SEED OUTPUT FORMAT

Every seed produced by the Raw Prompt Seed Team must follow this schema:

```
────────────────────────────────────────────
SEED PACK | [Product Name] | [Platform] | [Date]
────────────────────────────────────────────

SEED [N]:
  Template Title:        [Short descriptive title — not a hook, not copy]
  Raw Creative Seed:     [The creative concept in natural language — 1–3 sentences
                          describing the angle, mood, scene, and persona idea]
  System Expansion Request: [What the operator should tell BOSMAX when bringing
                             this seed into a session — format, engine, duration,
                             language, any specific variation to test]

  Silo:                  [STEALTH / DIRECT / HYBRID]
  Formula tag:           [SELL_THROUGH_HPFRC / STORY_HSARC / OTHER]
  Persona tag:           [persona name or USER_UPLOAD if operator will supply image]
  Platform risk:         [GREEN / YELLOW (with note) / RED (rejected — not in pack)]
  Product truth status:  [PASSED / FLAGGED (with note)]
  Variation position:    [e.g., Hook variant 2 of 5 / Formula variant A]
────────────────────────────────────────────
```

**What this format is NOT:**
- It is not a YAML checklist for operator workflow management
- It is not a final prompt or a prompt draft
- It is not a compliance gate output
- It does not contain engine-specific formatting (no Section 1–9, no Google Flow blocks)
- It does not contain final dialogue scripts (those are built by the final prompt team)

---

## 6. HARD RULES FOR THE RAW SEED TEAM

```
MUST:
  ✅ Validate every seed against product_record before Notion entry
  ✅ Tag every seed with silo, formula, persona, and platform risk
  ✅ Deduplicate against existing library before formatting
  ✅ Reject seeds that are too generic to generate distinctive final prompts
  ✅ Format output using the seed schema in Section 5
  ✅ Declare all rejected seeds with reasons

MUST NOT:
  ❌ Generate final prompts or expand seeds to deployment-ready format
  ❌ Write directly to Notion (operator imports manually)
  ❌ Run compliance gate audit (that is bosmax-compliance-gate's role)
  ❌ Bypass product_record lookup
  ❌ Create seeds with no variation differentiation from existing library
  ❌ Use YAML checklist format as the operator-facing seed output
  ❌ Make unsupported product claims (even in raw seeds — Product Truth Guard catches these)
  ❌ Expand inside Notion — seeds go to Notion raw; expansion happens in Claude Cowork sessions only
```

---

## 7. INTEGRATION WITH FINAL PROMPT TEAM

When an operator brings a raw seed from Notion into a Claude Code session:

1. The operator pastes the seed (or its core concept) into the session
2. BOSMAX orchestrator processes it as a normal requirement — it does NOT know or care whether it came from the seed team or was typed fresh
3. PRE-FLIGHT runs as normal (product lookup, validation, route selection)
4. The seed's creative direction informs the storyboard or image brief but does not override product_record truth
5. The final prompt team expands, enforces, and audits
6. The compliance gate clears or aborts
7. The final prompt is delivered to the operator

The seed team and the final prompt team do not share a session. They are separate human-initiated workflows. The Notion seed library is the handoff point between them.

---

## 8. IMPLEMENTATION PLAN (FUTURE PR)

When the Raw Prompt Seed Team skill files are ready, the following will be created:

| Item | Action |
|------|--------|
| `.claude/skills/bosmax-raw-seed-director.md` | Create: seed team orchestrator |
| `.claude/skills/bosmax-commercial-idea-miner.md` | Create: hook/angle variant generator |
| `.claude/skills/bosmax-product-truth-guard.md` | Create: product claim validator for seeds |
| `.claude/skills/bosmax-compliance-risk-filter.md` | Create: platform risk screener for seeds |
| `.claude/skills/bosmax-variation-architect.md` | Create: variation structure enforcer |
| `.claude/skills/bosmax-seed-auditor.md` | Create: duplicate/boring seed detector |
| `.claude/skills/bosmax-notion-seed-formatter.md` | Create: Notion-ready seed pack formatter |
| `.claude/CLAUDE.md` | Update: add ROUTE SEED as a new named route |
| `docs/agents/BOSMAX_AGENT_ROLE_INVENTORY_v1.md` | Update: add Units 13–19 for seed team |
| `.claude/rules/cowork-operating-map.md` | Update: add seed team skill files to required inventory |

This is a separate PR from PR 29 and PR 30. Sequence: PR 29 (PR #27 wiring) → PR 30 (final output agent + orchestrator activation patch) → PR [seed team] (seed skill files).
