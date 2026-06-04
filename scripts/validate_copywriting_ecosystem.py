from __future__ import annotations

import sys
from pathlib import Path

import yaml
from openpyxl import load_workbook

from stealth_copy_authority import (
    AUTHORITY_MAP_PATH,
    FORBIDDEN_DIRECT_PRONOUNS,
    FORBIDDEN_MEDICAL_CLAIMS,
    GENERIC_BANNED_PHRASES,
    STEALTH_SOURCE_HEADERS,
    STEALTH_WORKBOOK_SHEETS,
    contains_term,
    validate_stealth_blob,
)

ROOT = Path(__file__).resolve().parents[1]
WORKBOOK_PATH = ROOT / "BOSMAX_PRODUCT_COPYWRITING_LIBRARY_FAMILY_v2.xlsx"
REGISTRY_PATH = ROOT / "registries" / "dialogue_budget_corridor.yaml"
PAIN_HEADER = "Pain_or_Friction"
REQUIRED_PRIORITY_SHEETS = [
    "PRODUCT_BOSMAX_SERUM",
    "PRODUCT_MW_CAP_BURUNG",
    "FAMILY_MALE_EXT_OIL",
    "FAMILY_TRAD_REMEDY_OIL",
]
VALID_FORMULAS = {"AIDA", "PAS", "HSO", "HPAS", "SAVAGE_HPAS"}
VALID_LANES = {"DIRECT", "STEALTH"}
PLACEHOLDER_TOKENS = ("tbd", "placeholder", "hook 1", "usp 1", "cta 1", "lorem ipsum")


def normalize(value: object) -> str:
    if value is None:
        return ""
    return " ".join(str(value).split()).strip()


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def validate_workbook():
    if not WORKBOOK_PATH.exists():
        fail(f"Workbook missing: {WORKBOOK_PATH}")

    workbook = load_workbook(WORKBOOK_PATH, data_only=True)
    missing_sheets = [name for name in REQUIRED_PRIORITY_SHEETS if name not in workbook.sheetnames]
    if missing_sheets:
        fail(f"Required sheets missing: {', '.join(missing_sheets)}")

    row_counts: dict[str, int] = {}
    for sheet_name in workbook.sheetnames:
        if not (sheet_name.startswith("PRODUCT_") or sheet_name.startswith("FAMILY_")):
            continue

        ws = workbook[sheet_name]
        headers = [normalize(cell.value) for cell in ws[1]]
        if "Hook" not in headers or "CTA" not in headers:
            continue
        header_index = {header: idx for idx, header in enumerate(headers)}
        required = {"Row_ID", "Hook", "USP_1", "USP_2", "USP_3", "CTA", "Copywriting_Formula", "Silo_Key", "Type_of_Content", PAIN_HEADER}
        if sheet_name in STEALTH_WORKBOOK_SHEETS:
            required.update(STEALTH_SOURCE_HEADERS)
        missing_headers = [header for header in required if header not in header_index]
        if missing_headers:
            fail(f"{sheet_name} missing headers: {', '.join(missing_headers)}")

        rows_checked = 0
        for row in ws.iter_rows(min_row=2, values_only=True):
            hook = normalize(row[header_index["Hook"]])
            usp_1 = normalize(row[header_index["USP_1"]])
            usp_2 = normalize(row[header_index["USP_2"]])
            usp_3 = normalize(row[header_index["USP_3"]])
            cta = normalize(row[header_index["CTA"]])
            formula = normalize(row[header_index["Copywriting_Formula"]])
            silo_key = normalize(row[header_index["Silo_Key"]])
            lane = normalize(row[header_index["Type_of_Content"]])
            pain = normalize(row[header_index[PAIN_HEADER]])
            row_id = normalize(row[header_index["Row_ID"]])
            authority_source = normalize(row[header_index["Authority_Source"]]) if "Authority_Source" in header_index else ""

            populated = any((hook, usp_1, usp_2, usp_3, cta))
            if not populated:
                continue

            rows_checked += 1
            if not pain:
                fail(f"{sheet_name} {row_id} has content but blank {PAIN_HEADER}")
            if formula not in VALID_FORMULAS:
                fail(f"{sheet_name} {row_id}: invalid formula '{formula}'")
            if lane not in VALID_LANES:
                fail(f"{sheet_name} {row_id}: invalid lane '{lane}'")
            if not silo_key:
                fail(f"{sheet_name} {row_id}: blank Silo_Key")

            row_blob = " | ".join([hook, pain, usp_1, usp_2, usp_3, cta]).lower()
            if any(token in row_blob for token in PLACEHOLDER_TOKENS):
                fail(f"{sheet_name} {row_id}: obvious placeholder text detected")

            if sheet_name == "PRODUCT_BOSMAX_SERUM" and lane != "STEALTH":
                fail(f"{sheet_name} {row_id}: BOSMAX Serum must remain STEALTH")
            if sheet_name == "PRODUCT_MW_CAP_BURUNG" and lane != "DIRECT":
                fail(f"{sheet_name} {row_id}: MW Cap Burung must remain DIRECT")
            if sheet_name == "FAMILY_MALE_EXT_OIL" and lane != "STEALTH":
                fail(f"{sheet_name} {row_id}: FAMILY_MALE_EXT_OIL must remain STEALTH")
            if sheet_name == "FAMILY_TRAD_REMEDY_OIL" and lane != "DIRECT":
                fail(f"{sheet_name} {row_id}: FAMILY_TRAD_REMEDY_OIL must remain DIRECT")

            if sheet_name in STEALTH_WORKBOOK_SHEETS:
                if "SCRIPT_REGISTRY_UNIFIED.md" not in authority_source or "SCRIPT_VARIANT_LIBRARY.md" not in authority_source:
                    fail(f"{sheet_name} {row_id}: stealth authority source missing script-registry lock")

                source_metadata = {
                    header: normalize(row[header_index[header]])
                    for header in STEALTH_SOURCE_HEADERS
                }
                blanks = [header for header, value in source_metadata.items() if not value]
                if blanks:
                    fail(f"{sheet_name} {row_id}: blank stealth source metadata {', '.join(blanks)}")

                row_blob = " | ".join([hook, pain, usp_1, usp_2, usp_3, cta])
                issues = validate_stealth_blob(row_blob)
                if issues:
                    fail(f"{sheet_name} {row_id}: {'; '.join(issues)}")

                lowered = row_blob.lower()
                if any(contains_term(lowered, pronoun) for pronoun in FORBIDDEN_DIRECT_PRONOUNS):
                    fail(f"{sheet_name} {row_id}: forbidden direct pronoun detected")
                if any(contains_term(lowered, claim) for claim in FORBIDDEN_MEDICAL_CLAIMS):
                    fail(f"{sheet_name} {row_id}: forbidden medical claim detected")
                if any(contains_term(lowered, phrase) for phrase in GENERIC_BANNED_PHRASES):
                    fail(f"{sheet_name} {row_id}: generic packaging phrase detected")

        row_counts[sheet_name] = rows_checked

    return row_counts


def validate_registry() -> None:
    if not REGISTRY_PATH.exists():
        fail(f"Dialogue budget registry missing: {REGISTRY_PATH}")

    with REGISTRY_PATH.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    corridors = data.get("corridors", [])
    if not isinstance(corridors, list) or not corridors:
        fail("Dialogue budget registry has no corridors list")

    bm_brisk = {
        entry["duration_seconds"]: entry
        for entry in corridors
        if entry.get("language") == "BM" and entry.get("pace_class") == "BRISK_UGC"
    }
    required_durations = [6, 8, 10, 12, 15, 16, 20, 24, 30]
    missing = [str(duration) for duration in required_durations if duration not in bm_brisk]
    if missing:
        fail(f"BM/BRISK_UGC durations missing: {', '.join(missing)}")

    for duration in required_durations:
        entry = bm_brisk[duration]
        chain = [
            entry["minimum_words"],
            entry["target_min_words"],
            entry["target_max_words"],
            entry["safe_max_words"],
            entry["hard_ceiling_words"],
        ]
        if chain != sorted(chain):
            fail(f"Budget monotonicity failed for duration {duration}s: {chain}")


def validate_stealth_authority_map() -> None:
    if not AUTHORITY_MAP_PATH.exists():
        fail(f"Stealth authority map missing: {AUTHORITY_MAP_PATH}")

    with AUTHORITY_MAP_PATH.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    bosmax = (data or {}).get("products", {}).get("BOSMAX_SERUM")
    if not bosmax:
        fail("Stealth authority map missing products.BOSMAX_SERUM")

    if bosmax.get("copywriting_mode") != "script_registry_and_variant_only":
        fail("Stealth authority map copywriting_mode must remain script_registry_and_variant_only")

    metadata_headers = bosmax.get("workbook_source_metadata", [])
    if list(metadata_headers) != list(STEALTH_SOURCE_HEADERS):
        fail("Stealth authority map workbook_source_metadata drift detected")


def main() -> None:
    row_counts = validate_workbook()
    validate_registry()
    validate_stealth_authority_map()

    print("VALIDATION PASSED")
    print(f"Workbook: {WORKBOOK_PATH}")
    print(f"Registry: {REGISTRY_PATH}")
    print(f"Stealth Authority Map: {AUTHORITY_MAP_PATH}")
    for sheet_name in sorted(row_counts):
        if row_counts[sheet_name]:
            print(f"{sheet_name}: {row_counts[sheet_name]} populated rows validated")


if __name__ == "__main__":
    main()
