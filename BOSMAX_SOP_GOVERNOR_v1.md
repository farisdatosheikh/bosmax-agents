# BOSMAX SOP GOVERNOR v1
# Authority: Meta-Control Layer — above all runtime files
# Authors: Codex + Claude Cowork (shake-hand consensus)
# Status: CANONICAL — governs all authority file changes and propagation
# Version: v1.0 | Date: 2026-06-03

---

## 1. PURPOSE

The SOP Governor is the **meta-control layer** for BOSMAX.

It does not run requests.
It does not generate prompts.
It does not route anything.

It exists to:
- maintain the canonical SOP state
- control all changes to authority files
- prevent contamination when new laws are added
- enforce deprecation of old behavior
- resolve conflicts between files
- track schema versions
- declare what is live and what is dead

Without a Governor, every new patch risks contaminating the system.
The Governor is what makes patches safe.

---

## 2. AUTHORITY FILE REGISTRY

The Governor maintains this registry of all canonical authority files.

| File | Type | Version | Status |
|------|------|---------|--------|
| `BOSMAX_RUNTIME_STATE_MACHINE_v1.md` | Kernel Architecture | v1 | LIVE |
| `BOSMAX_AGENT_HANDOFF_SCHEMA_v1.md` | Packet Contracts | v1 | LIVE |
| `BOSMAX_SOP_GOVERNOR_v1.md` | Meta-Control | v1 | LIVE |
| `BOSMAX_TEST_HARNESS_v1.md` | Verification | v1 | LIVE |
| `.claude/CLAUDE.md` | Orchestrator | v11.6 | LIVE |
| `.claude/skills/bosmax-script-generator.md` | Worker Reference | v11.5 | LIVE |
| `.claude/skills/bosmax-compliance-gate.md` | Auditor Reference | v11.5 | LIVE |
| `.claude/skills/bosmax-requirement-analyst.md` | Analyst Reference | v11.4 | LIVE |
| `.claude/skills/bosmax-product-intelligence.md` | Product Lookup | v1.0 | LIVE |
| `.claude/skills/bosmax-scene-engine.md` | Scene Builder | v11.2 | LIVE |
| `.claude/skills/bosmax-subject-dna.md` | Avatar DNA | v11.2 | LIVE |
| `products/*.yaml` | Product Registry | varies | LIVE |
| `BOSMAX_HARD_ENGINE_CONTRACTS_v1.md` | Engine Law | v1 | LIVE |
| `BOSMAX_GROK_EXTENSION_SEAM_TEMPLATES_v1.md` | GROK Seam | v1 | LIVE |
| `BOSMAX_CHATGPT_CLEAN_VIDEO_ROLE_MODEL_v1.md` | Output Shape | v1 | LIVE |
| `BOSMAX_PROMPT_SELF_HEALING_CHECKLISTS_v1.md` | Repair | v1 | LIVE |
| `BOSMAX_ENGINE_SPECIFIC_SELF_HEALING_VARIANTS_v1.md` | Repair | v1 | LIVE |
| `BOSMAX_PRODUCT_SPECIFIC_SELF_HEALING_VARIANTS_v1.md` | Repair | v1 | LIVE |
| `BOSMAX_REPAIR_LANE_DECISION_TREE_v1.md` | Repair Routing | v1 | LIVE |
| `BOSMAX_SANDBOX_ON_THE_FLY_TEMPLATES_v1.md` | Sandbox | v1 | LIVE |

**Priority order when conflict exists between files:**
1. `BOSMAX_RUNTIME_STATE_MACHINE_v1.md` (highest — kernel)
2. `BOSMAX_AGENT_HANDOFF_SCHEMA_v1.md`
3. `BOSMAX_SOP_GOVERNOR_v1.md`
4. `BOSMAX_TEST_HARNESS_v1.md`
5. `.claude/CLAUDE.md`
6. Individual skill files
7. Helper / template files (lowest)

---

## 3. CHANGE CONTROL LAW

### 3.1 Who can propose changes

Anyone can identify a problem.
Only the Governor process can ratify a change.

### 3.2 Change categories

| Category | Definition | Approval required |
|---|---|---|
| PATCH | Fixes a wrong value, corrects drift, clarifies wording | Operator confirmation |
| MINOR | Adds new field to packet, adds new law, new product | Operator confirmation |
| MAJOR | Changes packet schema, changes state transitions, changes worker scope | Operator confirmation + Governor version bump |
| BREAKING | Removes a packet, renames a state, eliminates a worker | Operator confirmation + deprecation period |

### 3.3 Change steps (mandatory for MINOR and above)

1. **Identify**: state exactly what is changing and why
2. **Impact**: list which files are affected
3. **Draft**: write the change in the target file
4. **Propagate**: update all files that reference the changed element
5. **Log**: add entry to `BOSMAX-LOG.md`
6. **Commit**: commit all changed files together in one commit
7. **Governor update**: update this registry if file list changed

**HARD RULE: Never commit a partial change. All affected files must be updated in the same commit.**

### 3.4 Emergency patch law

If a critical failure is discovered in production (wrong prompt emitted, engine law violated, product truth broken):

1. Log the failure immediately in `BOSMAX-LOG.md`
2. Identify the responsible worker/file
3. Apply the minimal targeted fix
4. Run test harness cases affected by the change
5. Commit with `fix(bosmax):` prefix

Emergency patches skip nothing. They apply faster but still follow the same commit discipline.

---

## 4. DEPRECATION LAW

When a law, field, or behavior is being replaced:

### 4.1 Deprecation steps

1. Mark old element as `DEPRECATED` in its file with comment: `# DEPRECATED as of [date] — replaced by [new element]`
2. Add to deprecation map in this file (Section 5)
3. Keep the deprecated element for ONE full sprint (minimum 7 days)
4. Remove only after all references are updated and test harness confirms no regression

### 4.2 Hard deprecation rule

**You cannot remove a law without replacing it.**
If you remove a law without replacement, the system reverts to undefined behavior in that area. That is worse than the old law.

---

## 5. DEPRECATION MAP

Current deprecated elements:

| Deprecated element | Deprecated date | Reason | Replaced by |
|---|---|---|---|
| Direct prose handoff between skills | 2026-06-03 | Unreliable, inconsistent | Structured packet handoffs in `BOSMAX_AGENT_HANDOFF_SCHEMA_v1.md` |
| Single monolithic 16s GROK prompt | 2026-06-03 | Engine limit violation | Two separate block prompts (10s + 6s) |
| S9 overlay sections in video prompts | 2026-05-31 | AI burn-in text on video | `NO_OVERLAY` absolute rule in `BOSMAX_HARD_ENGINE_CONTRACTS_v1.md` |
| Ad-hoc AI dialogue for sensitive products | 2026-06-01 | Compliance risk | SCRIPT_REGISTRY_UNIFIED + SCRIPT_VARIANT_LIBRARY resolution |
| WPS values 1.6/2.0/3.0 (universal) | 2026-05-31 | Language-agnostic, incorrect | Language-specific WPS tables (BM: 2.5 safe max, EN: 3.0 safe max) |

---

## 6. CONFLICT RESOLUTION LAW

When two authority files say different things:

1. Identify which file has higher priority (see registry table above)
2. The higher-priority file wins
3. Update the lower-priority file to align
4. Log the conflict resolution in `BOSMAX-LOG.md`

**HARD RULE: Never leave a conflict unresolved. A system with two conflicting laws is a system with undefined behavior.**

Common conflict types and resolution:

| Conflict type | Resolution |
|---|---|
| CLAUDE.md says X, State Machine says Y | State Machine wins. Update CLAUDE.md. |
| Skill file says X, Handoff Schema says Y | Schema wins. Update skill file. |
| Old law in CLAUDE.md contradicts new engine law file | New engine law file wins if it post-dates CLAUDE.md update. Patch CLAUDE.md. |
| Two product YAML files have conflicting scale anchors | Last commit wins. Flag for operator review. |

---

## 7. SCHEMA VERSION MANAGEMENT

Current schema version: `v1`

Rules:
- All packets must declare `schema_version: "v1"`
- If packet schema changes, version increments to `v2`
- Both versions can coexist for one transition period
- After transition period, old version is deprecated

Version bump procedure:
1. Update `BOSMAX_AGENT_HANDOFF_SCHEMA_v1.md` → create `BOSMAX_AGENT_HANDOFF_SCHEMA_v2.md`
2. Update this Governor registry
3. Update state machine if transition rules change
4. Update all workers to produce new version
5. Keep v1 workers during transition period

---

## 8. PROPAGATION LAW

When a core element changes, propagation must happen to ALL affected files.

**Core element propagation map:**

| Element changed | Must propagate to |
|---|---|
| State definition | State Machine + any skill that describes that state |
| Packet field added | Schema + all workers that produce/consume that packet |
| Engine constraint changed | CLAUDE.md ENGINE_CONSTRAINT_TABLE + engine contracts file + compliance gate |
| Product registry changed | Product YAML + any benchmark/template using that product |
| WPS table changed | Script generator + compliance gate + CLAUDE.md storyboard gate |
| Avatar registry changed | Subject DNA skill + product YAML recommended_avatars |

**HARD RULE: No isolated patch. If you change X, you must find and update everything that depends on X.**

---

## 9. CONTAMINATION PREVENTION

Contamination happens when:
- a new law is added that contradicts an existing law
- a new file is added that repeats content already in another file
- a session caches old state and new state mixes in the same run

Prevention rules:

1. **Before adding a new law**: check if the law already exists somewhere
2. **Before adding a new file**: check if the content belongs in an existing file
3. **No duplicate law across files**: if law is in State Machine, do not repeat it verbatim in CLAUDE.md
4. **Cross-reference, don't copy**: files should reference each other, not duplicate each other
5. **New sessions always re-sync**: every new session must read current canonical files

---

## 10. GOVERNOR SELF-UPDATE LAW

When this Governor file itself needs updating:

1. Changes to the registry (add/remove files): immediate update, no deprecation period
2. Changes to change control law: operator confirmation required
3. Changes to priority order: operator confirmation required, log the reason

The Governor cannot deprecate itself. A new Governor version file must be created and the old one marked as SUPERSEDED.

---

## 11. MASS PRODUCTION READINESS CHECKLIST

Before declaring BOSMAX ready for mass production, verify:

```
☐ BOSMAX_RUNTIME_STATE_MACHINE_v1.md committed and live
☐ BOSMAX_AGENT_HANDOFF_SCHEMA_v1.md committed and live
☐ BOSMAX_SOP_GOVERNOR_v1.md committed and live
☐ BOSMAX_TEST_HARNESS_v1.md committed and live, minimum 10 cases defined
☐ All authority files at consistent versions (no v11.4 skills under v11.6 orchestrator)
☐ No unresolved conflicts in conflict map
☐ No deprecated elements still referenced in active files
☐ Test harness: all 10 test cases pass
☐ Operator has reviewed final output shape for at least 3 test cases manually
☐ Repair lanes tested: universal, engine-specific, product-specific, sandbox
```

Only when all items above are checked: BOSMAX mass production lock-down approved.
