from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "registries" / "video_engine_duration_contracts.yaml"
DIALOGUE_BUDGET_PATH = ROOT / "registries" / "dialogue_budget_corridor.yaml"


@dataclass(frozen=True)
class RegistryBundle:
    contracts: dict[str, Any]
    budgets: dict[tuple[str, str, int], dict[str, Any]]


def normalize_engine_id(value: str) -> str:
    return value.strip().upper()


def load_registry_bundle() -> RegistryBundle:
    contracts = yaml.safe_load(CONTRACT_PATH.read_text(encoding="utf-8")) or {}
    budget_data = yaml.safe_load(DIALOGUE_BUDGET_PATH.read_text(encoding="utf-8")) or {}
    budgets: dict[tuple[str, str, int], dict[str, Any]] = {}
    for item in budget_data.get("corridors", []):
        key = (str(item["language"]).upper(), str(item["pace_class"]).upper(), int(item["duration_seconds"]))
        budgets[key] = item
    return RegistryBundle(contracts=contracts, budgets=budgets)


def get_budget(bundle: RegistryBundle, language: str, pace_class: str, duration_seconds: int) -> dict[str, Any]:
    key = (language.upper(), pace_class.upper(), duration_seconds)
    if key not in bundle.budgets:
        raise ValueError(f"Missing dialogue budget corridor for {language}/{pace_class}/{duration_seconds}s")
    return bundle.budgets[key]


def build_verified_plan(
    engine_id: str,
    total_duration_seconds: int,
    language: str,
    pace_class: str,
    engine_contract: dict[str, Any],
    bundle: RegistryBundle,
) -> dict[str, Any]:
    totals = {int(item) for item in engine_contract.get("valid_total_durations_seconds", [])}
    if total_duration_seconds not in totals:
        raise ValueError(f"{engine_id} does not allow total duration {total_duration_seconds}s")

    block_map = {
        int(key): [int(value) for value in values]
        for key, values in (engine_contract.get("default_total_to_blocks") or {}).items()
    }
    block_durations = block_map.get(total_duration_seconds, [total_duration_seconds])
    total_budget = get_budget(bundle, language, pace_class, total_duration_seconds)
    role_defaults = {
        int(key): value
        for key, value in (engine_contract.get("block_role_defaults") or {}).items()
    }
    role_rows = role_defaults.get(total_duration_seconds, [])
    seam_contract = engine_contract.get("seam_contract", {})

    blocks: list[dict[str, Any]] = []
    for index, block_duration in enumerate(block_durations, start=1):
        role_meta = next((item for item in role_rows if int(item["block_index"]) == index), {})
        block_budget = get_budget(bundle, language, pace_class, block_duration)
        blocks.append(
            {
                "block_index": index,
                "block_duration_seconds": block_duration,
                "block_role": role_meta.get("role", "GENERAL"),
                "requires_seam": index > 1 or index < len(block_durations),
                "bridge_out_required": bool(role_meta.get("bridge_out_required", index < len(block_durations))),
                "bridge_in_required": bool(role_meta.get("bridge_in_required", index > 1)),
                "speech_resume_window_seconds": seam_contract.get("speech_resume_window_seconds") if index > 1 else None,
                "dialogue_budget": block_budget,
            }
        )

    return {
        "engine_id": engine_id,
        "authority_status": engine_contract["authority_status"],
        "notion_execution_status": engine_contract["notion_execution_status"],
        "total_duration_seconds": total_duration_seconds,
        "language": language.upper(),
        "pace_class": pace_class.upper(),
        "supports_multi_block": bool(engine_contract.get("supports_multi_block")),
        "block_count": len(block_durations),
        "block_durations_seconds": block_durations,
        "total_dialogue_budget": total_budget,
        "seam_contract": seam_contract,
        "blocks": blocks,
    }


def build_proposed_plan(
    engine_id: str,
    total_duration_seconds: int,
    language: str,
    pace_class: str,
    engine_contract: dict[str, Any],
    bundle: RegistryBundle,
) -> dict[str, Any]:
    constraints = engine_contract.get("proposed_constraints", {})
    block_max = int(constraints.get("proposed_single_block_max_seconds", 8))
    if total_duration_seconds <= 0:
        raise ValueError("total_duration_seconds must be positive")

    remaining = total_duration_seconds
    blocks: list[int] = []
    while remaining > 0:
        block = min(block_max, remaining)
        blocks.append(block)
        remaining -= block

    block_rows: list[dict[str, Any]] = []
    for index, block_duration in enumerate(blocks, start=1):
        budget = bundle.budgets.get((language.upper(), pace_class.upper(), block_duration))
        block_rows.append(
            {
                "block_index": index,
                "block_duration_seconds": block_duration,
                "block_role": "PROPOSED_REVIEW_ONLY",
                "requires_seam": index > 1 or index < len(blocks),
                "bridge_out_required": index < len(blocks),
                "bridge_in_required": index > 1,
                "speech_resume_window_seconds": {"min": 0.5, "max": 1.0} if index > 1 else None,
                "dialogue_budget": budget,
            }
        )

    total_budget = bundle.budgets.get((language.upper(), pace_class.upper(), total_duration_seconds))
    return {
        "engine_id": engine_id,
        "authority_status": engine_contract["authority_status"],
        "notion_execution_status": engine_contract["notion_execution_status"],
        "total_duration_seconds": total_duration_seconds,
        "language": language.upper(),
        "pace_class": pace_class.upper(),
        "supports_multi_block": bool(engine_contract.get("supports_multi_block")),
        "block_count": len(blocks),
        "block_durations_seconds": blocks,
        "total_dialogue_budget": total_budget,
        "review_reason": engine_contract.get("review_reason"),
        "proposed_constraints": constraints,
        "blocks": block_rows,
    }


def build_plan(engine_id: str, total_duration_seconds: int, language: str = "BM", pace_class: str = "BRISK_UGC") -> dict[str, Any]:
    bundle = load_registry_bundle()
    contracts = bundle.contracts.get("engines", {})
    if engine_id not in contracts:
        raise ValueError(f"Unknown engine_id: {engine_id}")

    engine_contract = contracts[engine_id]
    authority_status = str(engine_contract.get("authority_status", "")).upper()
    if authority_status == "VERIFIED":
        return build_verified_plan(engine_id, total_duration_seconds, language, pace_class, engine_contract, bundle)
    if authority_status == "NEEDS_REVIEW":
        return build_proposed_plan(engine_id, total_duration_seconds, language, pace_class, engine_contract, bundle)
    raise ValueError(f"Unsupported authority_status for {engine_id}: {authority_status}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Resolve BOSMAX engine duration into deterministic block plan")
    parser.add_argument("--engine-id", required=True)
    parser.add_argument("--duration", required=True, type=int)
    parser.add_argument("--language", default="BM")
    parser.add_argument("--pace-class", default="BRISK_UGC")
    parser.add_argument("--format", choices=("json", "yaml"), default="yaml")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    plan = build_plan(
        engine_id=normalize_engine_id(args.engine_id),
        total_duration_seconds=int(args.duration),
        language=args.language,
        pace_class=args.pace_class,
    )
    if args.format == "json":
        print(json.dumps(plan, indent=2, ensure_ascii=False))
        return
    print(yaml.safe_dump(plan, sort_keys=False, allow_unicode=True))


if __name__ == "__main__":
    main()
