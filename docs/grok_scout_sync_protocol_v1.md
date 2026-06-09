# BOSMAX Grok Scout Sync Protocol v1

```yaml
Authority: BOSMAX external scout / render-test governance
Status: CANONICAL
Date: 2026-06-10
Applies To:
  - external Grok scouting agents
  - GitHub-only sync checks
  - Notion-limited sync checks
  - rendered-output test reports
  - prompt stress tests using PR_42 motion occlusion guardrail
```

## 1. Purpose

This protocol controls how an external Grok scouting agent may participate in BOSMAX testing when it has GitHub access but may not have Notion access.

It prevents four failure modes observed during the first Grok sync report:

- treating Notion `NO_ACCESS` as if all Notion pages are actually `HOLD`
- expanding BOSMAX Serum from `5ML` to `5ML / 10ML` without source proof
- over-claiming broad file/workbook audits that were not requested
- claiming full ecosystem sync when only GitHub was verified

## 2. Supreme Commander Model

```yaml
ChatGPT: Supreme Commander / strategist / final auditor
Grok: External scouting agent / render prompt tester / GitHub-side scout
GitHub: source of truth
Notion: downstream operator mirror / execution surface
```

Grok may report findings. Grok may not promote readiness, edit production authority, or treat its own output as proof.

## 3. Access Status Rules

Grok must declare access separately:

```yaml
github_access: YES | NO
notion_access: YES | NO
local_file_access: YES | NO
```

If Notion is not accessible, Grok must write:

```text
Notion Access: NO_ACCESS. Notion content is unverifiable by this scout.
```

Grok must not write:

```text
All Notion pages are HOLD.
```

Correct wording:

```text
Notion pages are UNVERIFIED_BY_GROK due to NO_ACCESS. This is not the same as actual HOLD status. Only pages already designated by the Supreme Commander / repo / provided task context as HOLD may be labelled HOLD.
```

## 4. Product Truth Precision

Current BOSMAX active product truth for this lane:

```yaml
product: BOSMAX Serum 5ML / BOSMAX HERBS Herbal Oil Roll On
size: 5ML only
```

Grok must not mention `10ML` unless it directly verifies a current registry, product file, or operator instruction that explicitly adds `10ML`.

Blocked wording:

```text
BOSMAX Serum 5ML/10ML
```

Required wording:

```text
BOSMAX Serum 5ML
```

## 5. PR #42 Awareness Requirement

Before running any BOSMAX small-product render test, Grok must verify or be provided the current motion guardrail:

```yaml
repo: MFR-Marketing-Resources/bosmax-agents
pr: 42
title: "[VIDEO_MOTION_OCCLUSION_GUARDRAIL] Add anti-flash small product guardrail"
merge_sha: 74f38ffdd0019a1047b52a9a32d68a4cf58a22c7
guardrail_doc: docs/video_motion_occlusion_guardrail_v1.md
```

If Grok cannot verify PR #42, it must continue using only the guardrail text provided by the Supreme Commander and mark GitHub verification as partial.

## 6. Motion Occlusion Guardrail Summary

For small-product video testing, Grok must apply:

```yaml
first_frame_anchor: REQUIRED
product_reference_use: product truth only, not standalone opening packshot
standalone_product_flash: BLOCKED
sudden_object_appearance: BLOCKED
duplicate_product: BLOCKED
full_pouch_pocket_drawer_bag_fabric_hand_occlusion: BLOCKED unless high-risk accepted
hide_and_retrieve_motion: BLOCKED
minimum_product_visibility: "70% during compact-carry / tray / handling proof"
preferred_short_clip_motion: product already visible -> show beside prop -> stable product-visible close
```

## 7. Notion Scope Control

If Grok has no Notion access, it may only use Notion facts supplied by the Supreme Commander as provided context.

Grok must label them as:

```yaml
notion_status_source: SUPREME_COMMANDER_PROVIDED_CONTEXT
notion_direct_verification_by_grok: NO
```

Grok may not claim direct Notion verification unless it can actually fetch the page content.

## 8. Safe / Hold Page Language

Use these labels only as directed:

```yaml
SAFE_TO_USE:
  - 03A BOSMAX Serum Google Flow Templates
  - 03B Minyak Warisan Google Flow Templates
  - 03C On-The-Fly Product Google Flow Templates
  - 05A BOSMAX Serum Grok Templates
  - 05B Minyak Warisan Grok Templates
  - 05C On-The-Fly Product Grok Templates

HOLD:
  - 04 Video Google Flow Batch Prompt Templates
  - 06 Video Grok Batch Prompt Templates
```

If Grok cannot access Notion, it should not downgrade 03A/03B/03C/05A/05B/05C to HOLD. It should write `UNVERIFIED_BY_GROK` instead.

## 9. Over-Scouting Control

Grok must answer the assigned scouting question only.

Do not add broad claims like:

```text
All attached project files and workbooks were cross-checked exactly.
```

unless the task explicitly asked for a broad file inventory audit and Grok provides a file-by-file evidence table.

Allowed concise wording:

```text
Additional files were visible but not deeply audited because they were outside this sync task.
```

## 10. Output Verdict Labels

Use only one final verdict:

```yaml
SYNCED_READY_FOR_SCOUTING: GitHub and Notion both verified, no material gaps
PARTIAL_SYNC_GITHUB_READY_NOTION_UNVERIFIED: GitHub verified, Notion NO_ACCESS
PARTIAL_SYNC_NEEDS_SUPREME_REVIEW: material uncertainty needs ChatGPT audit
NOT_SYNCED_NO_ACCESS: GitHub and Notion unavailable
```

For the current state after PR #42:

```yaml
expected_external_grok_verdict_if_no_notion_access: PARTIAL_SYNC_GITHUB_READY_NOTION_UNVERIFIED
```

## 11. Allowed Next Tasks After Partial Sync

If GitHub is verified but Notion is not accessible, Grok may proceed only with:

- GitHub-side guardrail stress test
- prompt output critique against `docs/video_motion_occlusion_guardrail_v1.md`
- rendered video defect report
- anti-glitch re-render prompt recommendation

Grok may not proceed with:

- Notion mirror audit
- Notion page claims
- Notion editing
- GitHub editing
- batch page 04 / 06 activation
- full ecosystem PASS claim

## 12. Required Correction If Grok Mentions 10ML

If Grok outputs `BOSMAX Serum 5ML/10ML`, repair immediately:

```text
Correction: current active BOSMAX product for this lane is BOSMAX Serum 5ML only. Remove 10ML unless a current verified registry/source explicitly says otherwise.
```

## 13. Required Correction If Grok Labels All Notion Pages HOLD

Repair immediately:

```text
Correction: Notion NO_ACCESS means pages are UNVERIFIED_BY_GROK, not HOLD. Only page 04 and page 06 are HOLD / NOT_YET_IMPLEMENTED by current operator context.
```

## 14. Required Correction If Grok Overclaims Broad Audit

Repair immediately:

```text
Correction: broad workbook/project-file audit was not requested. Limit report to repo, PR #42, guardrail doc, module status, and explicitly provided Notion context.
```

## 15. Minimal Sync Prompt For Future Runs

```text
You are BOSMAX Grok Scout. Read docs/grok_scout_sync_protocol_v1.md and docs/video_motion_occlusion_guardrail_v1.md first. Verify GitHub PR #42 and guardrail status. If Notion is inaccessible, mark Notion as UNVERIFIED_BY_GROK, not HOLD. Current BOSMAX product is BOSMAX Serum 5ML only unless verified otherwise. Do not overclaim broad file audits. Return only GitHub verification, Notion access status, guardrail understanding, risks, and final verdict.
```
