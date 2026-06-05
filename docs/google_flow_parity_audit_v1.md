# GOOGLE_FLOW Parity Audit v1

Date: 2026-06-05

Purpose:
- compare BOSMAX long-duration execution surfaces
- keep GOOGLE_FLOW operator structure comparable to GROK without flattening engine differences

Official evidence reviewed on 2026-06-05:
- Google Flow Help
- Vertex AI Veo Extend docs
- Google Veo / Flow announcement

---

## 1. Parity Table

| Execution Surface | Allowed Block Durations | Valid Total Durations | WPS Budget Duration | Child Block Rows | Bridge-In / Bridge-Out | Previous Final-Second Required | Identity Reanchor | Product Reanchor | Sample Proof | Validator Coverage | Notion Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `GROK_EXTENSION` | `6`, `10` | `6, 10, 12, 16, 18, 20, 30` | per block | required for multi-block | yes / yes | no | yes | yes | yes | `validate_video_block_contracts.py`, `validate_wps_per_block.py` | `READY` |
| `VEO_3_1.CLIP_CHAIN` | `8` | `8, 16, 24, 32, 40, 48, 56` | `8` per block | required for multi-block | yes / yes | no | yes | yes | yes | `validate_video_block_contracts.py`, `validate_wps_per_block.py` | `READY_CLIP_MODE` |
| `VEO_3_1_LITE.CLIP_CHAIN` | `8` API | `8, 16, 24, 32, 40, 48, 56` | `7` actual-render per block | required for multi-block | yes / yes | no | yes | yes | yes | `validate_video_block_contracts.py`, `validate_wps_per_block.py` | `READY_CLIP_MODE` |
| `GOOGLE_FLOW.FLOW_EXTEND_UI` | `8` | `8, 16, 24, 32, 40, 48, 56` | `8` per block | required for multi-block | yes / yes | yes on continuation blocks | yes | yes | yes | `validate_video_block_contracts.py`, `validate_wps_per_block.py`, `validate_notion_sample_readiness.py`, `validate_flow_extend_proof.py` | `READY_REVIEWED_FLOW_EXTEND` |
| `GOOGLE_FLOW.FLOW_EXTEND_VERTEX` | `7` | `7, 14, 21, 28, 35, 42, 49, 56` | `7` per block | required for multi-block | yes / yes | yes on continuation blocks | yes | yes | no dedicated reviewed lane yet | `validate_video_block_contracts.py` structural only | `NEEDS_REVIEW` |

---

## 2. Google Flow Block Tables

### Flow UI

| Total | Block Split |
|---|---|
| `8s` | `[8]` |
| `16s` | `[8, 8]` |
| `24s` | `[8, 8, 8]` |
| `32s` | `[8, 8, 8, 8]` |
| `40s` | `[8, 8, 8, 8, 8]` |
| `48s` | `[8, 8, 8, 8, 8, 8]` |
| `56s` | `[8, 8, 8, 8, 8, 8, 8]` |

### Vertex

| Total | Block Split |
|---|---|
| `7s` | `[7]` |
| `14s` | `[7, 7]` |
| `21s` | `[7, 7, 7]` |
| `28s` | `[7, 7, 7, 7]` |
| `35s` | `[7, 7, 7, 7, 7]` |
| `42s` | `[7, 7, 7, 7, 7, 7]` |
| `49s` | `[7, 7, 7, 7, 7, 7, 7]` |
| `56s` | `[7, 7, 7, 7, 7, 7, 7, 7]` |

---

## 3. Operator Consequence

Google Flow is now operationally clear at the BOSMAX structure layer:
- parent video run is mandatory
- child block rows are mandatory
- per-block WPS is mandatory
- continuation blocks must carry previous-final-second state
- identity and product reanchors remain mandatory

What stays different from GROK:
- block math is Flow-specific, not `10/6`
- continuation depends on the prior clip final second
- Vertex remains documented but not reviewed-ready

---

## 4. Shared Resolver Payload

Copywriting and avatar resolver behavior remains shared across:
- GROK
- VEO_3_1
- VEO_3_1_LITE
- GOOGLE_FLOW

Only these surfaces change by engine:
- duration ladder
- per-block WPS duration
- seam law
- readiness status
