from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
COPYWRITING_REGISTRY_PATH = ROOT / "registries" / "copywriting_id_resolver.yaml"
AVATAR_REGISTRY_PATH = ROOT / "registries" / "avatar_context_rotation.yaml"

ALLOWED_RUNTIME_STATUSES = {"APPROVED", "LOCKED", "SEED_READY"}
COPYWRITING_NOTION_SAFE_FIELDS = [
    "copywriting_id",
    "display_name",
    "product_name",
    "family_name",
    "lane",
    "silo_key",
    "submode_formula",
    "angle",
    "hook",
    "usp_1",
    "usp_2",
    "usp_3",
    "cta",
    "compliance",
    "status",
    "safe_usage_notes",
]
AVATAR_NOTION_SAFE_FIELDS = [
    "avatar_context_id",
    "display_name",
    "persona_label",
    "gender",
    "age_range",
    "silo_allowed",
    "product_family_allowed",
    "scene_label",
    "mannequin_label",
    "camera_style_allowed",
    "status",
    "safe_usage_notes",
]


class ResolverError(RuntimeError):
    pass


def normalize_text(value: object) -> str:
    if value is None:
        return ""
    return " ".join(str(value).split()).strip()


def normalize_key(value: object) -> str:
    text = normalize_text(value).upper()
    text = re.sub(r"[^A-Z0-9]+", "_", text)
    return text.strip("_")


def normalize_alias(value: object) -> str:
    return normalize_key(value)


def _ensure_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [normalize_text(item) for item in value if normalize_text(item)]
    text = normalize_text(value)
    if not text:
        return []
    if text.startswith("[") and text.endswith("]"):
        inner = text[1:-1]
        return [segment.strip().strip("'\"") for segment in inner.split(",") if segment.strip()]
    return [segment.strip() for segment in text.split("|") if segment.strip()]


def _manual_override_guard(manual_override: bool, review_status: str | None) -> None:
    if manual_override and normalize_text(review_status) != "Needs Compliance Review":
        raise ResolverError(
            "Manual override detected without review status 'Needs Compliance Review'."
        )


@lru_cache(maxsize=1)
def load_copywriting_registry() -> dict[str, Any]:
    with COPYWRITING_REGISTRY_PATH.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


@lru_cache(maxsize=1)
def load_avatar_registry() -> dict[str, Any]:
    with AVATAR_REGISTRY_PATH.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def _copywriting_alias_index(registry: dict[str, Any]) -> dict[str, str]:
    index: dict[str, str] = {}
    for row in registry.get("alias_map", []):
        alias = normalize_key(row.get("alias"))
        canonical = normalize_text(row.get("canonical_id"))
        if alias and canonical:
            index[alias] = canonical
    for pack in registry.get("copy_packs", []):
        canonical = normalize_text(pack.get("copywriting_id"))
        if canonical:
            index[normalize_key(canonical)] = canonical
            for alias in pack.get("aliases", []):
                index[normalize_key(alias)] = canonical
    return index


def normalize_copywriting_id(copywriting_id: str, registry: dict[str, Any] | None = None) -> str:
    registry = registry or load_copywriting_registry()
    alias_index = _copywriting_alias_index(registry)
    normalized = normalize_key(copywriting_id)
    canonical = alias_index.get(normalized)
    if not canonical:
        raise ResolverError(f"Copywriting ID not found: {copywriting_id}")
    return canonical


def _copywriting_pack_index(registry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        normalize_text(pack.get("copywriting_id")): pack
        for pack in registry.get("copy_packs", [])
        if normalize_text(pack.get("copywriting_id"))
    }


def assert_copywriting_pack_runtime(
    pack: dict[str, Any],
    *,
    expected_template_lane: str | None = None,
    expected_template_silo: str | None = None,
    manual_override: bool = False,
    review_status: str | None = None,
) -> None:
    _manual_override_guard(manual_override, review_status)

    copywriting_id = normalize_text(pack.get("copywriting_id")) or "<unknown>"
    status = normalize_text(pack.get("status"))
    runtime_allowed = bool(pack.get("runtime_allowed"))
    lane = normalize_text(pack.get("lane")).upper()
    silo_key = normalize_text(pack.get("silo_key"))
    product_silo = normalize_text(pack.get("product_silo")).upper()

    if runtime_allowed and status not in ALLOWED_RUNTIME_STATUSES:
        raise ResolverError(
            f"{copywriting_id} has invalid runtime status '{status}'."
        )
    if not runtime_allowed:
        raise ResolverError(f"{copywriting_id} is not runtime allowed.")

    if expected_template_lane and lane != normalize_text(expected_template_lane).upper():
        raise ResolverError(
            f"{copywriting_id} lane mismatch: expected {expected_template_lane}, got {lane}."
        )

    if expected_template_silo and silo_key != normalize_text(expected_template_silo):
        raise ResolverError(
            f"{copywriting_id} silo mismatch: expected {expected_template_silo}, got {silo_key}."
        )

    if product_silo and lane and product_silo != lane:
        raise ResolverError(
            f"{copywriting_id} product silo mismatch: product requires {product_silo}, pack lane is {lane}."
        )

    if pack.get("require_provenance_nodes"):
        missing_nodes = [
            field
            for field in (
                "source_script_node",
                "source_variant_hook_node",
                "source_variant_problem_node",
                "source_variant_solution_node",
                "source_variant_cta_node",
            )
            if not normalize_text(pack.get(field))
        ]
        if missing_nodes:
            raise ResolverError(
                f"{copywriting_id} missing required provenance nodes: {', '.join(missing_nodes)}."
            )


def resolve_copywriting_id(
    copywriting_id: str,
    *,
    expected_template_lane: str | None = None,
    expected_template_silo: str | None = None,
    manual_override: bool = False,
    review_status: str | None = None,
    registry: dict[str, Any] | None = None,
) -> dict[str, Any]:
    registry = registry or load_copywriting_registry()
    canonical = normalize_copywriting_id(copywriting_id, registry)
    pack = _copywriting_pack_index(registry).get(canonical)
    if pack is None:
        raise ResolverError(f"Copywriting ID not found: {copywriting_id}")
    assert_copywriting_pack_runtime(
        pack,
        expected_template_lane=expected_template_lane,
        expected_template_silo=expected_template_silo,
        manual_override=manual_override,
        review_status=review_status,
    )
    return dict(pack)


def sanitize_copywriting_for_notion(pack: dict[str, Any]) -> dict[str, Any]:
    return {field: pack.get(field) for field in COPYWRITING_NOTION_SAFE_FIELDS}


def _avatar_pack_index(registry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        normalize_key(pack.get("avatar_context_id")): pack
        for pack in registry.get("avatar_context_packs", [])
        if normalize_text(pack.get("avatar_context_id"))
    }


def _avatar_pool_index(registry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        normalize_key(pool.get("pool_id")): pool
        for pool in registry.get("rotation_pools", [])
        if normalize_text(pool.get("pool_id"))
    }


def assert_avatar_context_pack_runtime(
    pack: dict[str, Any],
    *,
    expected_template_silo: str | None = None,
    expected_product_family: str | None = None,
    expected_camera_style: str | None = None,
    physics_class: str | None = None,
    manual_override: bool = False,
    review_status: str | None = None,
) -> None:
    _manual_override_guard(manual_override, review_status)

    avatar_context_id = normalize_text(pack.get("avatar_context_id")) or "<unknown>"
    status = normalize_text(pack.get("status"))
    runtime_allowed = bool(pack.get("runtime_allowed"))

    if runtime_allowed and status not in ALLOWED_RUNTIME_STATUSES:
        raise ResolverError(
            f"{avatar_context_id} has invalid runtime status '{status}'."
        )
    if not runtime_allowed:
        raise ResolverError(f"{avatar_context_id} is not runtime allowed.")

    silo_allowed = {
        normalize_text(item).upper() for item in _ensure_list(pack.get("silo_allowed"))
    }
    product_family_allowed = {
        normalize_key(item) for item in _ensure_list(pack.get("product_family_allowed"))
    }
    camera_style_allowed = {
        normalize_key(item) for item in _ensure_list(pack.get("camera_style_allowed"))
    }
    compatible_physics_classes = {
        normalize_key(item) for item in _ensure_list(pack.get("compatible_physics_classes"))
    }

    if expected_template_silo and normalize_text(expected_template_silo).upper() not in silo_allowed:
        raise ResolverError(
            f"{avatar_context_id} silo mismatch: {expected_template_silo} not in {sorted(silo_allowed)}."
        )

    if expected_product_family and normalize_key(expected_product_family) not in product_family_allowed:
        raise ResolverError(
            f"{avatar_context_id} product family mismatch: {expected_product_family} not in {sorted(product_family_allowed)}."
        )

    if expected_camera_style and normalize_key(expected_camera_style) not in camera_style_allowed:
        raise ResolverError(
            f"{avatar_context_id} camera style mismatch: {expected_camera_style} not in {sorted(camera_style_allowed)}."
        )

    if physics_class and normalize_key(physics_class) not in compatible_physics_classes:
        raise ResolverError(
            f"{avatar_context_id} mannequin incompatibility: physics class {physics_class} not in {sorted(compatible_physics_classes)}."
        )


def resolve_avatar_context_id(
    avatar_context_id: str,
    *,
    expected_template_silo: str | None = None,
    expected_product_family: str | None = None,
    expected_camera_style: str | None = None,
    physics_class: str | None = None,
    manual_override: bool = False,
    review_status: str | None = None,
    registry: dict[str, Any] | None = None,
) -> dict[str, Any]:
    registry = registry or load_avatar_registry()
    pack = _avatar_pack_index(registry).get(normalize_key(avatar_context_id))
    if pack is None:
        raise ResolverError(f"Avatar Context ID not found: {avatar_context_id}")
    assert_avatar_context_pack_runtime(
        pack,
        expected_template_silo=expected_template_silo,
        expected_product_family=expected_product_family,
        expected_camera_style=expected_camera_style,
        physics_class=physics_class,
        manual_override=manual_override,
        review_status=review_status,
    )
    return dict(pack)


def _build_round_robin_sequence(
    approved_packs: list[dict[str, Any]],
    batch_count: int,
    no_repeat_window: int,
) -> list[dict[str, Any]]:
    if not approved_packs:
        raise ResolverError("No approved avatar context packs available for rotation.")

    sequence: list[dict[str, Any]] = []
    cursor = 0
    pool_size = len(approved_packs)

    while len(sequence) < batch_count:
        candidate = approved_packs[cursor % pool_size]
        recent_ids = {
            normalize_text(item.get("avatar_context_id"))
            for item in sequence[-no_repeat_window:]
        }
        candidate_id = normalize_text(candidate.get("avatar_context_id"))

        if candidate_id in recent_ids:
            found = None
            for offset in range(pool_size):
                trial = approved_packs[(cursor + offset) % pool_size]
                trial_id = normalize_text(trial.get("avatar_context_id"))
                if trial_id not in recent_ids:
                    found = trial
                    cursor = cursor + offset + 1
                    break
            if found is None:
                raise ResolverError(
                    "Pool rotation failed: no candidate available outside the configured no-repeat window."
                )
            sequence.append(found)
            continue

        sequence.append(candidate)
        cursor += 1

    return sequence


def resolve_avatar_pool(
    avatar_pool_id: str,
    *,
    batch_count: int,
    rotation_rule: str,
    expected_template_silo: str | None = None,
    expected_product_family: str | None = None,
    expected_camera_style: str | None = None,
    physics_class: str | None = None,
    manual_override: bool = False,
    review_status: str | None = None,
    registry: dict[str, Any] | None = None,
) -> dict[str, Any]:
    registry = registry or load_avatar_registry()
    pool = _avatar_pool_index(registry).get(normalize_key(avatar_pool_id))
    if pool is None:
        raise ResolverError(f"Avatar Pool ID not found: {avatar_pool_id}")

    _manual_override_guard(manual_override, review_status)

    pool_id = normalize_text(pool.get("pool_id"))
    status = normalize_text(pool.get("status"))
    runtime_allowed = bool(pool.get("runtime_allowed"))
    minimum_approved_count = int(pool.get("minimum_approved_count") or 0)
    no_repeat_window = int(pool.get("no_repeat_window") or 0)
    pool_rotation_mode = normalize_text(pool.get("rotation_mode"))

    if runtime_allowed and status not in ALLOWED_RUNTIME_STATUSES:
        raise ResolverError(f"{pool_id} has invalid runtime status '{status}'.")
    if not runtime_allowed:
        raise ResolverError(f"{pool_id} is not runtime allowed.")
    if normalize_key(pool_rotation_mode) != normalize_key(rotation_rule):
        raise ResolverError(
            f"{pool_id} rotation rule mismatch: expected {pool_rotation_mode}, got {rotation_rule}."
        )
    if batch_count <= 0:
        raise ResolverError("Batch Count must be greater than 0 for AUTO_ROTATE.")

    approved_packs: list[dict[str, Any]] = []
    for avatar_context_id in pool.get("allowed_avatar_context_ids", []):
        approved_packs.append(
            resolve_avatar_context_id(
                avatar_context_id,
                expected_template_silo=expected_template_silo,
                expected_product_family=expected_product_family,
                expected_camera_style=expected_camera_style,
                physics_class=physics_class,
                registry=registry,
            )
        )

    if len(approved_packs) < minimum_approved_count:
        raise ResolverError(
            f"{pool_id} has fewer approved rows than required: {len(approved_packs)} < {minimum_approved_count}."
        )

    if no_repeat_window <= 0:
        raise ResolverError(f"{pool_id} no_repeat_window must be greater than 0.")
    if len(approved_packs) < min(batch_count, no_repeat_window):
        raise ResolverError(
            f"{pool_id} cannot satisfy no-repeat window {no_repeat_window} with only {len(approved_packs)} approved packs."
        )

    sequence = _build_round_robin_sequence(approved_packs, batch_count, no_repeat_window)

    for index, pack in enumerate(sequence):
        current_id = normalize_text(pack.get("avatar_context_id"))
        recent_ids = [
            normalize_text(item.get("avatar_context_id"))
            for item in sequence[max(0, index - no_repeat_window) : index]
        ]
        if current_id in recent_ids:
            raise ResolverError(
                f"{pool_id} repeat-window violation at position {index + 1}: {current_id} repeated inside the last {no_repeat_window} selections."
            )

    return {
        "pool": dict(pool),
        "approved_packs": approved_packs,
        "sequence": sequence,
        "sequence_ids": [normalize_text(pack.get("avatar_context_id")) for pack in sequence],
    }


def sanitize_avatar_for_notion(pack: dict[str, Any]) -> dict[str, Any]:
    return {field: pack.get(field) for field in AVATAR_NOTION_SAFE_FIELDS}
