"""
Validator for BOSMAX Batch Video Prompt Exporter v1.

Runs PASS and FAIL cases against build_batch_video_prompts.run_batch()
and export_rows(), then confirms that output files are actually written
to outputs/batch_prompts/.

Exit code 0 = all checks passed.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]

from build_batch_video_prompts import (  # noqa: E402
    ExporterError,
    OUTPUT_DIR,
    export_rows,
    run_batch,
)
from resolver_runtime import ResolverError  # noqa: E402


# ---------------------------------------------------------------------------
# Test helpers
# ---------------------------------------------------------------------------

def fail(message: str) -> None:
    print(f"VALIDATION FAILED: {message}")
    sys.exit(1)


def expect(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def expect_raises(callable_: Any, exc_type: type, label: str) -> None:
    caught = None
    try:
        callable_()
    except exc_type as exc:
        caught = exc
    except Exception as exc:  # noqa: BLE001
        fail(
            f"{label}: expected {exc_type.__name__} but got "
            f"{type(exc).__name__}: {exc}"
        )
    if caught is None:
        fail(f"{label}: expected {exc_type.__name__} but no exception was raised.")


# ---------------------------------------------------------------------------
# PASS — BOSMAX Serum STEALTH batch, 20 rows, COPY_FIXED
# ---------------------------------------------------------------------------

def test_bosmax_stealth_20_rows() -> None:
    payload: dict[str, Any] = {
        "product_workflow": "BOSMAX_SERUM_STEALTH",
        "platform": "TikTok",
        "engine": "GROK",
        "duration": "10s",
        "language": "Malay",
        "copywriting_mode": "AUTO_RESOLVE",
        "copywriting_id": "BOSMAX_SERUM_CP_0001",
        "avatar_pool_id": "BOSMAX_MALE_STEALTH_POOL_001",
        "avatar_mode": "AUTO_ROTATE",
        "batch_count": 20,
        "rotation_rule": "ROUND_ROBIN_NO_REPEAT",
    }
    rows = run_batch(payload)
    expect(len(rows) == 20, f"BOSMAX 20-row batch: expected 20 rows, got {len(rows)}")
    expect(
        all(r["route_status"] == "REGISTERED_PRODUCT" for r in rows),
        "BOSMAX batch: all rows must be REGISTERED_PRODUCT",
    )
    expect(
        all(r["product_id"] == "BOSMAX_SERUM" for r in rows),
        "BOSMAX batch: product_id must be BOSMAX_SERUM for all rows",
    )
    expect(
        all(r["product_workflow"] == "BOSMAX_SERUM_STEALTH" for r in rows),
        "BOSMAX batch: product_workflow must match",
    )
    expect(
        all(r["avatar_pool_id"] == "BOSMAX_MALE_STEALTH_POOL_001" for r in rows),
        "BOSMAX batch: avatar_pool_id must match",
    )
    print("PASS: bosmax_stealth_20_rows")


# ---------------------------------------------------------------------------
# PASS — MWCB DIRECT batch, 20 rows, COPY_FIXED
# ---------------------------------------------------------------------------

def test_mwcb_direct_20_rows() -> None:
    payload: dict[str, Any] = {
        "product_workflow": "MWCB_DIRECT",
        "platform": "TikTok",
        "engine": "VEO_3_1_LITE",
        "duration": "8s",
        "language": "Malay",
        "copywriting_mode": "AUTO_RESOLVE",
        "copywriting_id": "CAP_BURUNG_MINYAK_CP_0031",
        "avatar_pool_id": "MWCB_TRAD_REMEDY_POOL_001",
        "avatar_mode": "AUTO_ROTATE",
        "batch_count": 20,
        "rotation_rule": "ROUND_ROBIN_NO_REPEAT",
    }
    rows = run_batch(payload)
    expect(len(rows) == 20, f"MWCB 20-row batch: expected 20 rows, got {len(rows)}")
    expect(
        all(r["route_status"] == "REGISTERED_PRODUCT" for r in rows),
        "MWCB batch: all rows must be REGISTERED_PRODUCT",
    )
    expect(
        all(r["product_id"] == "CAP_BURUNG_MINYAK" for r in rows),
        "MWCB batch: product_id must be CAP_BURUNG_MINYAK for all rows",
    )
    expect(
        all(r["avatar_pool_id"] == "MWCB_TRAD_REMEDY_POOL_001" for r in rows),
        "MWCB batch: avatar_pool_id must match",
    )
    print("PASS: mwcb_direct_20_rows")


# ---------------------------------------------------------------------------
# PASS — COPY_FIXED repeats same copywriting ID for every row
# ---------------------------------------------------------------------------

def test_copy_fixed_repeats_correctly() -> None:
    payload: dict[str, Any] = {
        "product_workflow": "BOSMAX_SERUM_STEALTH",
        "platform": "TikTok",
        "engine": "GROK",
        "duration": "10s",
        "language": "Malay",
        "copywriting_mode": "COPY_FIXED",
        "copywriting_id": "BOSMAX_SERUM_CP_0002",
        "avatar_pool_id": "BOSMAX_MALE_STEALTH_POOL_001",
        "avatar_mode": "AUTO_ROTATE",
        "batch_count": 5,
        "rotation_rule": "ROUND_ROBIN_NO_REPEAT",
    }
    rows = run_batch(payload)
    expect(len(rows) == 5, f"COPY_FIXED: expected 5 rows, got {len(rows)}")
    expect(
        all(r["copywriting_id"] == "BOSMAX_SERUM_CP_0002" for r in rows),
        "COPY_FIXED: all rows must carry the same copywriting_id",
    )
    print("PASS: copy_fixed_repeats_correctly")


# ---------------------------------------------------------------------------
# PASS — COPY_ROTATE cycles copywriting IDs correctly
# ---------------------------------------------------------------------------

def test_copy_rotate_cycles_correctly() -> None:
    payload: dict[str, Any] = {
        "product_workflow": "BOSMAX_SERUM_STEALTH",
        "platform": "TikTok",
        "engine": "GROK",
        "duration": "10s",
        "language": "Malay",
        "copywriting_mode": "AUTO_RESOLVE",
        "copywriting_id_range": "BOSMAX_SERUM_CP_0001..BOSMAX_SERUM_CP_0003",
        "avatar_pool_id": "BOSMAX_MALE_STEALTH_POOL_001",
        "avatar_mode": "AUTO_ROTATE",
        "batch_count": 7,
        "rotation_rule": "ROUND_ROBIN_NO_REPEAT",
    }
    rows = run_batch(payload)
    expect(len(rows) == 7, f"COPY_ROTATE: expected 7 rows, got {len(rows)}")
    ids = [r["copywriting_id"] for r in rows]
    # Pattern with 3 IDs repeating: 0001,0002,0003,0001,0002,0003,0001
    expected_cycle = [
        "BOSMAX_SERUM_CP_0001",
        "BOSMAX_SERUM_CP_0002",
        "BOSMAX_SERUM_CP_0003",
        "BOSMAX_SERUM_CP_0001",
        "BOSMAX_SERUM_CP_0002",
        "BOSMAX_SERUM_CP_0003",
        "BOSMAX_SERUM_CP_0001",
    ]
    expect(
        ids == expected_cycle,
        f"COPY_ROTATE: expected {expected_cycle}, got {ids}",
    )
    print("PASS: copy_rotate_cycles_correctly")


# ---------------------------------------------------------------------------
# PASS — avatar_context_id comes from correct pool
# ---------------------------------------------------------------------------

def test_avatar_context_id_from_correct_pool() -> None:
    bosmax_pool_ids = {
        "BOSMAX_AVP_0001",
        "BOSMAX_AVP_0002",
        "BOSMAX_AVP_0003",
        "BOSMAX_AVP_0004",
        "BOSMAX_AVP_0005",
        "BOSMAX_AVP_0006",
        "BOSMAX_AVP_0007",
        "BOSMAX_AVP_0008",
    }
    mwcb_pool_ids = {
        "MWCB_DIRECT_AVP_0001",
        "MWCB_DIRECT_AVP_0002",
    }

    bosmax_rows = run_batch({
        "product_workflow": "BOSMAX_SERUM_STEALTH",
        "platform": "TikTok",
        "engine": "GROK",
        "duration": "10s",
        "language": "Malay",
        "copywriting_mode": "AUTO_RESOLVE",
        "copywriting_id": "BOSMAX_SERUM_CP_0001",
        "avatar_pool_id": "BOSMAX_MALE_STEALTH_POOL_001",
        "avatar_mode": "AUTO_ROTATE",
        "batch_count": 8,
        "rotation_rule": "ROUND_ROBIN_NO_REPEAT",
    })
    for row in bosmax_rows:
        expect(
            row["avatar_context_id"] in bosmax_pool_ids,
            f"BOSMAX pool: unexpected avatar_context_id {row['avatar_context_id']!r}",
        )

    mwcb_rows = run_batch({
        "product_workflow": "MWCB_DIRECT",
        "platform": "TikTok",
        "engine": "VEO_3_1_LITE",
        "duration": "8s",
        "language": "Malay",
        "copywriting_mode": "AUTO_RESOLVE",
        "copywriting_id": "CAP_BURUNG_MINYAK_CP_0031",
        "avatar_pool_id": "MWCB_TRAD_REMEDY_POOL_001",
        "avatar_mode": "AUTO_ROTATE",
        "batch_count": 4,
        "rotation_rule": "ROUND_ROBIN_NO_REPEAT",
    })
    for row in mwcb_rows:
        expect(
            row["avatar_context_id"] in mwcb_pool_ids,
            f"MWCB pool: unexpected avatar_context_id {row['avatar_context_id']!r}",
        )

    print("PASS: avatar_context_id_from_correct_pool")


# ---------------------------------------------------------------------------
# PASS — ON_THE_FLY session batch has copywriting_id=none and FORBIDDEN writeback
# ---------------------------------------------------------------------------

def test_on_the_fly_session_batch() -> None:
    payload: dict[str, Any] = {
        "product_workflow": "ON_THE_FLY_SESSION_ONLY",
        "platform": "TikTok",
        "engine": "GROK",
        "duration": "10s",
        "language": "Malay",
        "copywriting_id": "none",
        "copywriting_mode": "SESSION_ONLY_GENERATE",
        "registry_writeback": "FORBIDDEN",
        "batch_count": 3,
        "product_intake": {
            "product_name": "Portable Mini Blender",
            "category": "Kitchen Appliances",
            "target_user": "Busy working adults",
            "main_problem_solved": "Hard to blend at work",
            "main_benefit": "Portable blending anywhere",
            "product_format": "Electric handheld device",
            "product_size_or_scale": "Palm-sized",
            "compliance_class": "LOW",
            "visual_reference_status": "NONE",
        },
    }
    rows = run_batch(payload)
    expect(len(rows) == 3, f"ON_THE_FLY: expected 3 rows, got {len(rows)}")
    for row in rows:
        expect(
            row["copywriting_id"] == "none",
            f"ON_THE_FLY: copywriting_id must be 'none', got {row['copywriting_id']!r}",
        )
        expect(
            row["route_status"] == "ON_THE_FLY",
            f"ON_THE_FLY: route_status must be ON_THE_FLY, got {row['route_status']!r}",
        )
        expect(
            "registry_writeback: FORBIDDEN" in row["final_prompt_text"],
            "ON_THE_FLY: final_prompt_text must contain registry_writeback: FORBIDDEN",
        )
        expect(
            "copywriting_mode: SESSION_ONLY_GENERATE" in row["final_prompt_text"],
            "ON_THE_FLY: final_prompt_text must declare SESSION_ONLY_GENERATE",
        )
    print("PASS: on_the_fly_session_batch")


# ---------------------------------------------------------------------------
# PASS — invalid batch_count fails closed
# ---------------------------------------------------------------------------

def test_invalid_batch_count_fails_closed() -> None:
    base: dict[str, Any] = {
        "product_workflow": "BOSMAX_SERUM_STEALTH",
        "platform": "TikTok",
        "engine": "GROK",
        "duration": "10s",
        "language": "Malay",
        "copywriting_mode": "AUTO_RESOLVE",
        "copywriting_id": "BOSMAX_SERUM_CP_0001",
        "avatar_pool_id": "BOSMAX_MALE_STEALTH_POOL_001",
        "avatar_mode": "AUTO_ROTATE",
        "rotation_rule": "ROUND_ROBIN_NO_REPEAT",
    }

    # Zero batch_count
    expect_raises(
        lambda: run_batch({**base, "batch_count": 0}),
        ExporterError,
        "batch_count=0 must raise ExporterError",
    )

    # Negative batch_count
    expect_raises(
        lambda: run_batch({**base, "batch_count": -1}),
        ExporterError,
        "batch_count=-1 must raise ExporterError",
    )

    # Non-integer batch_count
    expect_raises(
        lambda: run_batch({**base, "batch_count": "twenty"}),
        ExporterError,
        "batch_count='twenty' must raise ExporterError",
    )

    print("PASS: invalid_batch_count_fails_closed")


# ---------------------------------------------------------------------------
# PASS — REVIEW_ONLY on-the-fly row blocks generation
# ---------------------------------------------------------------------------

def test_review_only_on_the_fly_blocks_generation() -> None:
    payload: dict[str, Any] = {
        "product_workflow": "ON_THE_FLY_SESSION_ONLY",
        "platform": "TikTok",
        "engine": "GROK",
        "duration": "10s",
        "language": "Malay",
        "copywriting_mode": "SESSION_ONLY_GENERATE",
        "registry_writeback": "FORBIDDEN",
        "batch_count": 2,
        "product_intake": [
            {
                "product_name": "Baby Formula Supplement",
                "category": "Baby Products",
                "compliance_class": "HIGH",
            },
            {
                "product_name": "Portable Blender",
                "category": "Kitchen",
                "compliance_class": "LOW",
            },
        ],
    }
    rows = run_batch(payload)
    expect(len(rows) == 2, f"REVIEW_ONLY mix: expected 2 rows, got {len(rows)}")
    expect(
        rows[0]["route_status"] == "BLOCKED_REVIEW_ONLY",
        f"REVIEW_ONLY row 0: expected BLOCKED_REVIEW_ONLY, got {rows[0]['route_status']!r}",
    )
    expect(
        "BLOCKED_REVIEW_ONLY" in rows[0]["final_prompt_text"],
        "REVIEW_ONLY row 0: final_prompt_text must carry BLOCKED_REVIEW_ONLY",
    )
    expect(
        rows[1]["route_status"] == "ON_THE_FLY",
        f"REVIEW_ONLY mix row 1: expected ON_THE_FLY, got {rows[1]['route_status']!r}",
    )
    print("PASS: review_only_on_the_fly_blocks_generation")


# ---------------------------------------------------------------------------
# FAIL — STEALTH request using MWCB avatar pool
# ---------------------------------------------------------------------------

def test_fail_stealth_using_mwcb_pool() -> None:
    payload: dict[str, Any] = {
        "product_workflow": "BOSMAX_SERUM_STEALTH",
        "platform": "TikTok",
        "engine": "GROK",
        "duration": "10s",
        "language": "Malay",
        "copywriting_mode": "AUTO_RESOLVE",
        "copywriting_id": "BOSMAX_SERUM_CP_0001",
        "avatar_pool_id": "MWCB_TRAD_REMEDY_POOL_001",  # wrong pool for STEALTH
        "avatar_mode": "AUTO_ROTATE",
        "batch_count": 5,
        "rotation_rule": "ROUND_ROBIN_NO_REPEAT",
    }
    expect_raises(
        lambda: run_batch(payload),
        ExporterError,
        "STEALTH workflow with MWCB pool must raise ExporterError",
    )
    print("PASS (fail-closed): stealth_using_mwcb_pool correctly blocked")


# ---------------------------------------------------------------------------
# FAIL — DIRECT request using BOSMAX stealth avatar pool
# ---------------------------------------------------------------------------

def test_fail_direct_using_bosmax_stealth_pool() -> None:
    payload: dict[str, Any] = {
        "product_workflow": "MWCB_DIRECT",
        "platform": "TikTok",
        "engine": "VEO_3_1_LITE",
        "duration": "8s",
        "language": "Malay",
        "copywriting_mode": "AUTO_RESOLVE",
        "copywriting_id": "CAP_BURUNG_MINYAK_CP_0031",
        "avatar_pool_id": "BOSMAX_MALE_STEALTH_POOL_001",  # wrong pool for DIRECT
        "avatar_mode": "AUTO_ROTATE",
        "batch_count": 5,
        "rotation_rule": "ROUND_ROBIN_NO_REPEAT",
    }
    expect_raises(
        lambda: run_batch(payload),
        ExporterError,
        "DIRECT workflow with BOSMAX stealth pool must raise ExporterError",
    )
    print("PASS (fail-closed): direct_using_bosmax_stealth_pool correctly blocked")


# ---------------------------------------------------------------------------
# FAIL — ON_THE_FLY tries registry_writeback allowed
# ---------------------------------------------------------------------------

def test_fail_on_the_fly_writeback_allowed() -> None:
    payload: dict[str, Any] = {
        "product_workflow": "ON_THE_FLY_SESSION_ONLY",
        "platform": "TikTok",
        "engine": "GROK",
        "duration": "10s",
        "language": "Malay",
        "copywriting_mode": "SESSION_ONLY_GENERATE",
        "registry_writeback": "ALLOWED",  # must be blocked
        "batch_count": 1,
        "product_intake": {"product_name": "Test Product", "compliance_class": "LOW"},
    }
    expect_raises(
        lambda: run_batch(payload),
        ExporterError,
        "ON_THE_FLY with registry_writeback=ALLOWED must raise ExporterError",
    )
    print("PASS (fail-closed): on_the_fly_writeback_allowed correctly blocked")


# ---------------------------------------------------------------------------
# FAIL — invalid copywriting ID
# ---------------------------------------------------------------------------

def test_fail_invalid_copywriting_id() -> None:
    payload: dict[str, Any] = {
        "product_workflow": "BOSMAX_SERUM_STEALTH",
        "platform": "TikTok",
        "engine": "GROK",
        "duration": "10s",
        "language": "Malay",
        "copywriting_mode": "AUTO_RESOLVE",
        "copywriting_id": "BOSMAX_SERUM_CP_9999",  # does not exist
        "avatar_pool_id": "BOSMAX_MALE_STEALTH_POOL_001",
        "avatar_mode": "AUTO_ROTATE",
        "batch_count": 2,
        "rotation_rule": "ROUND_ROBIN_NO_REPEAT",
    }
    expect_raises(
        lambda: run_batch(payload),
        ExporterError,
        "Invalid copywriting_id must raise ExporterError",
    )
    print("PASS (fail-closed): invalid_copywriting_id correctly blocked")


# ---------------------------------------------------------------------------
# FAIL — invalid avatar pool ID
# ---------------------------------------------------------------------------

def test_fail_invalid_avatar_pool_id() -> None:
    payload: dict[str, Any] = {
        "product_workflow": "BOSMAX_SERUM_STEALTH",
        "platform": "TikTok",
        "engine": "GROK",
        "duration": "10s",
        "language": "Malay",
        "copywriting_mode": "AUTO_RESOLVE",
        "copywriting_id": "BOSMAX_SERUM_CP_0001",
        "avatar_pool_id": "NONEXISTENT_POOL_XYZ",  # does not exist
        "avatar_mode": "AUTO_ROTATE",
        "batch_count": 2,
        "rotation_rule": "ROUND_ROBIN_NO_REPEAT",
    }
    expect_raises(
        lambda: run_batch(payload),
        ExporterError,
        "Invalid avatar_pool_id must raise ExporterError",
    )
    print("PASS (fail-closed): invalid_avatar_pool_id correctly blocked")


# ---------------------------------------------------------------------------
# Production-ready proof — actual files must be written
# ---------------------------------------------------------------------------

def test_files_written_to_output_dir() -> None:
    """
    Proves production-readiness: run_batch() + export_rows() must produce
    CSV, MD, and JSONL files under outputs/batch_prompts/.
    """
    import tempfile  # noqa: PLC0415

    payload: dict[str, Any] = {
        "product_workflow": "BOSMAX_SERUM_STEALTH",
        "platform": "TikTok",
        "engine": "GROK",
        "duration": "10s",
        "language": "Malay",
        "copywriting_mode": "AUTO_RESOLVE",
        "copywriting_id": "BOSMAX_SERUM_CP_0001",
        "avatar_pool_id": "BOSMAX_MALE_STEALTH_POOL_001",
        "avatar_mode": "AUTO_ROTATE",
        "batch_count": 5,
        "rotation_rule": "ROUND_ROBIN_NO_REPEAT",
    }
    rows = run_batch(payload)

    # Write to the canonical outputs/batch_prompts/ directory.
    paths = export_rows(rows, "BOSMAX_SERUM_STEALTH", OUTPUT_DIR)

    for fmt in ("csv", "jsonl", "md"):
        expect(fmt in paths, f"export_rows did not return a '{fmt}' path")
        expect(paths[fmt].exists(), f"output file does not exist: {paths[fmt]}")
        expect(paths[fmt].stat().st_size > 0, f"output file is empty: {paths[fmt]}")
        print(f"  [{fmt.upper():5s}] {paths[fmt]}")

    # Verify CSV has correct row count (header + N data rows).
    import csv as csv_mod  # noqa: PLC0415
    with paths["csv"].open(encoding="utf-8", newline="") as fh:
        reader = csv_mod.DictReader(fh)
        csv_rows = list(reader)
    expect(
        len(csv_rows) == 5,
        f"CSV row count mismatch: expected 5, got {len(csv_rows)}",
    )

    # Verify JSONL has one JSON object per line.
    import json as json_mod  # noqa: PLC0415
    with paths["jsonl"].open(encoding="utf-8") as fh:
        jsonl_rows = [json_mod.loads(line) for line in fh if line.strip()]
    expect(
        len(jsonl_rows) == 5,
        f"JSONL row count mismatch: expected 5, got {len(jsonl_rows)}",
    )

    print("PASS: files_written_to_output_dir")


# ---------------------------------------------------------------------------
# Sample YAML round-trip — load samples/batch/*.yaml and resolve
# ---------------------------------------------------------------------------

def test_sample_yaml_round_trip() -> None:
    import yaml as yaml_mod  # noqa: PLC0415

    sample_dir = ROOT / "samples" / "batch"
    for yaml_path in sorted(sample_dir.glob("*.yaml")):
        with yaml_path.open("r", encoding="utf-8") as fh:
            batch_input = yaml_mod.safe_load(fh) or {}
        try:
            rows = run_batch(batch_input)
        except ExporterError as exc:
            fail(f"Sample YAML {yaml_path.name} raised ExporterError: {exc}")
        expect(
            len(rows) > 0,
            f"Sample YAML {yaml_path.name} produced 0 rows",
        )
        print(f"  sample {yaml_path.name}: {len(rows)} row(s) ok")

    print("PASS: sample_yaml_round_trip")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    # PASS cases
    test_bosmax_stealth_20_rows()
    test_mwcb_direct_20_rows()
    test_copy_fixed_repeats_correctly()
    test_copy_rotate_cycles_correctly()
    test_avatar_context_id_from_correct_pool()
    test_on_the_fly_session_batch()
    test_invalid_batch_count_fails_closed()
    test_review_only_on_the_fly_blocks_generation()

    # FAIL cases (must raise ExporterError — we verify fail-closed behaviour)
    test_fail_stealth_using_mwcb_pool()
    test_fail_direct_using_bosmax_stealth_pool()
    test_fail_on_the_fly_writeback_allowed()
    test_fail_invalid_copywriting_id()
    test_fail_invalid_avatar_pool_id()

    # Production-ready proof
    test_files_written_to_output_dir()

    # Sample YAML round-trip
    test_sample_yaml_round_trip()

    print("\nVALIDATION PASSED")


if __name__ == "__main__":
    main()
