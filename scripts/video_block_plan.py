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


def normalize_execution_mode(value: str | None) -> str | None:
    if value is None:
        return None
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


def get_block_map(mode_contract: dict[str, Any]) -> dict[int, list[int]]:
    return {
        int(key): [int(value) for value in values]
        for key, values in (mode_contract.get("default_total_to_blocks") or {}).items()
    }


def build_blocks(
    *,
    block_durations: list[int],
    total_duration_seconds: int,
    language: str,
    pace_class: str,
    bundle: RegistryBundle,
    seam_contract: dict[str, Any],
    role_defaults: dict[int, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    role_rows = role_defaults.get(total_duration_seconds, [])
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
                "requires_frame_bridge": bool(seam_contract.get("require_frame_bridge", index > 1)),
                "requires_identity_reanchor": bool(seam_contract.get("require_identity_reanchor_every_block", False)),
                "requires_product_reanchor": bool(seam_contract.get("require_product_reanchor_every_block", False)),
            }
        )
    return blocks


def build_legacy_verified_plan(
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

    block_map = get_block_map(engine_contract)
    block_durations = block_map.get(total_duration_seconds, [total_duration_seconds])
    total_budget = get_budget(bundle, language, pace_class, total_duration_seconds)
    role_defaults = {
        int(key): value
        for key, value in (engine_contract.get("block_role_defaults") or {}).items()
    }
    seam_contract = engine_contract.get("seam_contract", {})
    blocks = build_blocks(
        block_durations=block_durations,
        total_duration_seconds=total_duration_seconds,
        language=language,
        pace_class=pace_class,
        bundle=bundle,
        seam_contract=seam_contract,
        role_defaults=role_defaults,
    )

    return {
        "engine_id": engine_id,
        "execution_mode": engine_contract.get("execution_mode", "EXTENSION"),
        "authority_status": engine_contract["authority_status"],
        "notion_execution_status": engine_contract["notion_execution_status"],
        "total_duration_seconds": total_duration_seconds,
        "language": language.upper(),
        "pace_class": pace_class.upper(),
        "supports_multi_block": bool(engine_contract.get("supports_multi_block")),
        "block_count": len(block_durations),
        "block_durations_seconds": block_durations,
        "prompt_count": len(block_durations),
        "requires_frame_bridge": bool(seam_contract.get("require_frame_bridge", len(block_durations) > 1)),
        "requires_identity_reanchor": bool(seam_contract.get("require_identity_reanchor_every_block", False)),
        "requires_product_reanchor": bool(seam_contract.get("require_product_reanchor_every_block", False)),
        "requires_previous_clip_final_second": bool(seam_contract.get("require_previous_clip_final_second", False)),
        "status": "READY",
        "reason": "Verified BOSMAX execution contract.",
        "total_dialogue_budget": total_budget,
        "seam_contract": seam_contract,
        "blocks": blocks,
    }


def build_mode_plan(
    engine_id: str,
    total_duration_seconds: int,
    language: str,
    pace_class: str,
    engine_contract: dict[str, Any],
    mode_name: str,
    mode_contract: dict[str, Any],
    bundle: RegistryBundle,
    previous_clip_final_second_state: str | None = None,
) -> dict[str, Any]:
    mode_status = str(mode_contract.get("status", "NEEDS_REVIEW")).upper()
    valid_totals = {int(item) for item in mode_contract.get("valid_total_durations_seconds", [])}
    block_map = get_block_map(mode_contract)
    if valid_totals and total_duration_seconds not in valid_totals:
        raise ValueError(f"{engine_id}.{mode_name} does not allow total duration {total_duration_seconds}s")

    block_durations = block_map.get(total_duration_seconds)
    if block_durations is None:
        single_clip_durations = {int(item) for item in mode_contract.get("single_clip_durations_seconds", [])}
        if total_duration_seconds in single_clip_durations:
            block_durations = [total_duration_seconds]
        elif mode_status == "READY":
            raise ValueError(f"{engine_id}.{mode_name} is missing deterministic block math for {total_duration_seconds}s")
        else:
            block_durations = []

    seam_contract = mode_contract.get("seam_contract", {})
    role_defaults = {
        int(key): value
        for key, value in (mode_contract.get("block_role_defaults") or {}).items()
    }
    blocks = build_blocks(
        block_durations=block_durations,
        total_duration_seconds=total_duration_seconds,
        language=language,
        pace_class=pace_class,
        bundle=bundle,
        seam_contract=seam_contract,
        role_defaults=role_defaults,
    ) if block_durations else []

    status = "READY" if mode_status == "READY" else "NEEDS_REVIEW"
    reason = mode_contract.get("reason")
    if mode_name == "FLOW_EXTEND" and not previous_clip_final_second_state:
        status = "NEEDS_REVIEW"
        reason = (
            "FLOW_EXTEND requires previous_clip_final_second_state and remains manual-review only "
            "until direct Flow long-form execution proof is hardened."
        )
    elif status != "READY" and not reason:
        reason = engine_contract.get("review_reason", "Mode is not production-ready.")

    total_budget = bundle.budgets.get((language.upper(), pace_class.upper(), total_duration_seconds))
    return {
        "engine_id": engine_id,
        "execution_mode": mode_name,
        "authority_status": engine_contract["authority_status"],
        "notion_execution_status": engine_contract["notion_execution_status"],
        "total_duration_seconds": total_duration_seconds,
        "language": language.upper(),
        "pace_class": pace_class.upper(),
        "supports_multi_block": bool(engine_contract.get("supports_multi_block")),
        "block_count": len(block_durations),
        "block_durations_seconds": block_durations,
        "prompt_count": len(block_durations),
        "requires_frame_bridge": bool(seam_contract.get("require_frame_bridge", mode_name == "FLOW_EXTEND" or len(block_durations) > 1)),
        "requires_identity_reanchor": bool(seam_contract.get("require_identity_reanchor_every_block", mode_name == "FLOW_EXTEND")),
        "requires_product_reanchor": bool(seam_contract.get("require_product_reanchor_every_block", mode_name == "FLOW_EXTEND")),
        "requires_previous_clip_final_second": bool(
            seam_contract.get("require_previous_clip_final_second", mode_contract.get("requires_previous_clip_final_second", False))
        ),
        "status": status,
        "reason": reason,
        "total_dialogue_budget": total_budget,
        "decision_record": engine_contract.get("decision_record"),
        "required_fields": mode_contract.get("required_fields", []),
        "previous_clip_final_second_state": previous_clip_final_second_state,
        "seam_contract": seam_contract,
        "blocks": blocks,
    }


def build_plan(
    engine_id: str,
    total_duration_seconds: int,
    language: str = "BM",
    pace_class: str = "BRISK_UGC",
    execution_mode: str | None = None,
    previous_clip_final_second_state: str | None = None,
) -> dict[str, Any]:
    bundle = load_registry_bundle()
    contracts = bundle.contracts.get("engines", {})
    if engine_id not in contracts:
        raise ValueError(f"Unknown engine_id: {engine_id}")

    engine_contract = contracts[engine_id]
    if "execution_modes" in engine_contract:
        mode_name = normalize_execution_mode(execution_mode) or str(engine_contract.get("default_execution_mode", "")).upper()
        if not mode_name:
            raise ValueError(f"{engine_id} is missing default_execution_mode")
        execution_modes = engine_contract.get("execution_modes") or {}
        if mode_name not in execution_modes:
            raise ValueError(f"Unknown execution_mode for {engine_id}: {mode_name}")
        return build_mode_plan(
            engine_id=engine_id,
            total_duration_seconds=total_duration_seconds,
            language=language,
            pace_class=pace_class,
            engine_contract=engine_contract,
            mode_name=mode_name,
            mode_contract=execution_modes[mode_name],
            bundle=bundle,
            previous_clip_final_second_state=previous_clip_final_second_state,
        )

    authority_status = str(engine_contract.get("authority_status", "")).upper()
    if authority_status == "VERIFIED":
        return build_legacy_verified_plan(engine_id, total_duration_seconds, language, pace_class, engine_contract, bundle)
    raise ValueError(f"Unsupported authority_status for {engine_id}: {authority_status}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Resolve BOSMAX engine duration into deterministic block plan")
    parser.add_argument("--engine-id", required=True)
    parser.add_argument("--duration", required=True, type=int)
    parser.add_argument("--language", default="BM")
    parser.add_argument("--pace-class", default="BRISK_UGC")
    parser.add_argument("--execution-mode")
    parser.add_argument("--previous-clip-final-second-state")
    parser.add_argument("--format", choices=("json", "yaml"), default="yaml")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    plan = build_plan(
        engine_id=normalize_engine_id(args.engine_id),
        total_duration_seconds=int(args.duration),
        language=args.language,
        pace_class=args.pace_class,
        execution_mode=normalize_execution_mode(args.execution_mode),
        previous_clip_final_second_state=args.previous_clip_final_second_state,
    )
    if args.format == "json":
        print(json.dumps(plan, indent=2, ensure_ascii=False))
        return
    print(yaml.safe_dump(plan, sort_keys=False, allow_unicode=True))


if __name__ == "__main__":
    main()
