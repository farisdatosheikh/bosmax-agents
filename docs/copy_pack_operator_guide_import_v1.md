# CopyPack Operator Guide — Static Import (v1)

## Why this exists

The Notion CopyPack Guide was originally implemented using **formula properties**
for operator-facing metadata (Angle Label, Use Case, Best For, Tone, Claim Risk,
Do/Do Not, Production Readiness, Operator Note, Compliance Note, Formula,
Formula Meaning).

Formula properties are **computed, not editable per row**. In the live database
they mirror `Display_Name` verbatim, which produces dirty, truncated operator
labels (e.g. fragments of internal hooks) instead of clean operator guidance.
This is also structurally unfixable from outside Notion: formula expressions are
served via `formulaCode://` URLs, which are not readable or writable through the
available integration surface.

**Fix:** replace the formula-driven layer with a static, hand-curated CSV that
can be imported once and edited per-row going forward like any normal Notion
property.

## What this guide is — and is not

This guide is **operator metadata only**. It tells an operator which angle a
CopyPack ID belongs to, what it's for, what tone/risk class it carries, and what
to do / not do with it.

It is explicitly **not** a content source. It contains no creative copy that
could be lifted directly into a script or post.

### Excluded by design (DO NOT list)

The following are intentionally absent from every row and from this guide as a
whole:

- Hook
- USP_1 / USP_2 / USP_3
- CTA
- Source nodes / source script nodes / source variant nodes
- Backend prompt fragments
- Authority source references
- Display_Name (and any truncated fragment of it)
- Any other Pain & Compliance (P&C) internal logic

These exclusions mirror the `forbidden_notion_fields` / `notion_safe_fields`
contract already declared in `registries/copywriting_id_resolver.yaml`.

## Source of truth

All structural fields (`CopyPack ID`, `Product Name`, `Product ID`, `Lane`,
`Formula`, `Status`) are read directly from
`registries/copywriting_id_resolver.yaml` (read-only — this guide does not
modify that registry). All `Guide *` columns are newly authored, operator-safe
content written specifically for this guide; none of it is copied from existing
hook/USP/CTA/angle copy.

## Scope — 96 rows

| Product | ID range | Count | Lane |
|---|---|---|---|
| BOSMAX Serum | `BOSMAX_SERUM_CP_0001` – `BOSMAX_SERUM_CP_0030` | 30 | STEALTH |
| Minyak Warisan Cap Burung | `CAP_BURUNG_MINYAK_CP_0001` – `CAP_BURUNG_MINYAK_CP_0066` | 66 | DIRECT |

## Columns (17, in order)

1. `CopyPack ID`
2. `Product Name`
3. `Product ID`
4. `Lane`
5. `Formula`
6. `Formula Meaning`
7. `Guide Angle Label`
8. `Guide Use Case`
9. `Guide Best For`
10. `Guide Tone`
11. `Guide Claim Risk`
12. `Guide Do`
13. `Guide Do Not`
14. `Guide Production Readiness`
15. `Guide Operator Note`
16. `Guide Compliance Note`
17. `Status`

## Formula Meaning reference

| Formula | Meaning |
|---|---|
| `PAS` | Problem → Agitation → Solution |
| `AIDA` | Attention → Interest → Desire → Action |
| `HSO` | Hook → Story → Offer |
| `SAVAGE_HPAS` | High-pressure hook with Problem → Agitation → Solution structure |
| `HPAS` | Hook → Problem → Agitation → Solution — the base structure that `SAVAGE_HPAS` escalates with a higher-pressure opening hook |

`HPAS` appears among the 66 MWCB rows as a valid `Submode_Formula` select option
that the operator brief did not define verbatim. Its meaning above is derived to
stay consistent with the user-supplied `SAVAGE_HPAS` definition (same PAS core,
without the "high-pressure" escalation). `HPFRC` does **not** appear in any of
the 96 target rows, so no derivation was required for it.

## Label families used

### BOSMAX Serum (STEALTH lane) — 10 allowed families, cycled across 30 rows

Private Confidence Reset · Discreet Night Routine · Premium Masculine Self-Care ·
Soft Stealth Reminder · Batch Hook Variant · Stealth Routine Angle · Confidence
Recovery Angle · Personal Care Cue · Low-Key Masculine Reminder · Premium Reset
Positioning

All STEALTH labels avoid explicit sexual language, medical claims, raw hook
fragments, and truncated `Display_Name` fragments. Every label maps to safe,
metaphor-level framing consistent with the `STEALTH_METAPHOR_REQUIRED`
compliance class.

### Minyak Warisan Cap Burung (DIRECT lane) — 8 allowed families, cycled across 66 rows

Traditional Household Comfort · Sapuan Luar Comfort Cue · Warm Heritage Relief
Positioning · Family Routine Angle · Pocket Traditional Oil Cue · Everyday
External-Use Comfort · Heritage Trust Angle · Practical Home-Use Reminder

All DIRECT labels use traditional household-comfort language and avoid
cure/treat/heal medical wording or any claim that the product removes illness.

## Production Readiness mapping

`Guide Production Readiness` is derived from each row's registry `Status`:

- `SEED_READY` → "Seed-ready - review with compliance lead before scaled use"
- `APPROVED` → "Approved - cleared for production use under current compliance class"

## How to import into Notion

1. Open the canonical CopyPack database.
2. Use Notion's CSV import (or "Merge with CSV" if matching by `CopyPack ID`).
3. Map each CSV column to a **text-type** Notion property (not formula).
   If the existing `Guide *` properties are formula-type, they must first be
   converted to plain text/select properties in Notion — this guide does not
   change the runtime resolver or any existing CopyPack YAML, so that schema
   change is an in-app step for the database owner.
4. Re-run the validator (below) against the CSV before every import to confirm
   the contract still holds.

## Validation

Run:

```
python scripts/validate_copy_pack_operator_guide_import.py
```

The validator checks: CSV exists, exactly 96 rows, 30 BOSMAX rows, 66 MWCB rows,
all 17 required columns present and ordered, no Hook/USP/CTA/source columns, no
forbidden words (`cure`, `treat`, `heal`, explicit sexual terms, and the known
dirty label fragments `Piston`, `Aban`, `Penggera`, `Ego`, `Alpha`), non-empty
`Guide Angle Label` and `Guide Operator Note` per row, and `Status` populated
per row.

## File locations

- CSV: `outputs/notion_import/COPY_PACK_OPERATOR_GUIDE_IMPORT_v1.csv`
- This doc: `docs/copy_pack_operator_guide_import_v1.md`
- Validator: `scripts/validate_copy_pack_operator_guide_import.py`
