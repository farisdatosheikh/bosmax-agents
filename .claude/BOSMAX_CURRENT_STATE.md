# BOSMAX_CURRENT_STATE.md
## BOSMAX v11.10 — Current Operating Snapshot

Read this file first at session start.
Open `BOSMAX-LOG.md` only if this snapshot is insufficient or a historical audit is required.

---

## Core State

- Active orchestrator schema: `v11.10`
- Active posture: deterministic front-door + deterministic batch lane
- Mandatory gates active:
  - `VISUAL INTAKE GATE`
  - `PRE-FLIGHT PROTOCOL`
  - `STORYBOARD GATE`
  - `PRE-OUTPUT FAIL-CLOSED ENFORCEMENT`
- Video defaults hardened:
  - BM commercial / recommendation / household UGC requires dialog unless user explicitly asks for silent/montage/text-only output
  - GROK operating contract remains BOSMAX-locked to `6s` or `10s` per block
  - video overlays remain forbidden by default unless user explicitly asks for overlay planning

---

## Read Order

1. `BOSMAX_CURRENT_STATE.md`
2. `products/*.yaml` if a product is mentioned
3. Relevant `.claude/skills/*.md` only after route is resolved
4. `BOSMAX-LOG.md` only for historical reasoning, patch provenance, or old decisions not captured here

---

## Active Registry Snapshot

Registered products in `products/`:

- `BOSMAX_SERUM`
  - Sensitive stealth lane
  - Variants: `5ML`, `10ML`
- `MINYAK_WARISAN_TOK_CAP_BURUNG_25ML`  ← ACTIVE (v11.10)
  - Canonical product name: **Minyak Warisan Tok Cap Burung**
  - Accepted aliases: Minyak Warisan Cap Burung, Cap Burung, Tok Cap Burung
  - Direct-product traditional remedy lane (DIRECT)
  - Variant: `25ML_GREEN_GLASS_BOTTLE`
  - Current packaging truth: 25ml transparent green-tinted glass, red ribbed screw cap (NO roll-on, NO WG40)
  - Active product truth source: `products/MINYAK_WARISAN_TOK_CAP_BURUNG_25ML.yaml`
  - Template reference: `templates/poster/03A-P1_PRODUCT_ONLY_COPY_LANDBANK_POSTER.md`
  - Notion intake: 100-row Copywriting Landbank, ANG-01 through ANG-10
- `CAP_BURUNG_MINYAK`  ← LEGACY — DO NOT USE
  - registry_status: LEGACY_DO_NOT_USE
  - superseded_by: MINYAK_WARISAN_TOK_CAP_BURUNG_25ML
  - Product intelligence will skip this file — see products/CAP_BURUNG_MINYAK.yaml
- `MAVERIX_MAXOIL`
  - Sensitive stealth lane
  - Variant: `SET_5_BOTTLES`
- `JUNGLE_GIRL_MINYAK`
  - Provisional direct-product benchmark lane
  - Variant: `30ML_JG01`

No product currently has locked `subject_dna` or `last_source_image_handoff` in `products/*.yaml`.

---

## Latest High-Value Milestones

- `2026-06-14`: v11.10 ecosystem cleanup — Notion row intake adapter wired, legacy file blocked, subhook + operator_scene_direction added, canonical naming enforced, 03A-P1 template role clarified
- `2026-06-11`: MINYAK_WARISAN_TOK_CAP_BURUNG_25ML registered (active product registry for 25ml green glass bottle)
- `2026-06-03`: UGC / PGC / HYBRID authority stack installed
- `2026-06-03`: Grok capability wording normalized
- `2026-06-03`: Grok extension seam templates installed
- `2026-06-03`: ChatGPT clean video role model installed
- `2026-06-03`: hard anti-stupidity contracts installed
- `2026-06-03`: product-specific self-healing variants installed
- `2026-06-03`: engine-specific self-healing variants installed
- `2026-06-03`: runtime kernel architecture files installed
- `2026-06-03`: visual intake gate + storyboard gate + visual-first sandbox enforcement installed

---

## Current Operational Assumptions

- Product truth lives in `products/*.yaml`, not in session memory prose.
- `BOSMAX-LOG.md` is append-only historical memory, not the default read surface.
- If uploaded visual evidence conflicts with prior memory, visual evidence wins.
- If registry is missing but product truth is visually obvious, use visual-first sandbox and ask only the missing minimum.
- If route is ambiguous, ask one sharp clarification question and stop.

---

## Pending State

- Pending tasks: none recorded
- Image handoff registry: no active handoff locked in product YAML
- Known blocker in this repo structure:
  - `graphify-out/` missing
  - `docs/MODULE_STATUS.yaml` missing
  - treat this workspace as live `.claude` orchestration + product registry surface, not a full Mandor Node lane

---

## When To Open BOSMAX-LOG.md

Open the historical log only when you need:

- exact chronology of patches
- rationale for an older authority decision
- proof of when a lane or registry was introduced
- an audit trail for changes not summarized above
