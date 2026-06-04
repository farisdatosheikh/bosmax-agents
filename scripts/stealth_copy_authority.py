from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_REGISTRY_PATH = ROOT / "SCRIPT_REGISTRY_UNIFIED.md"
VARIANT_LIBRARY_PATH = ROOT / "SCRIPT_VARIANT_LIBRARY.md"
AUTHORITY_MAP_PATH = ROOT / "registries" / "stealth_copy_authority_map.yaml"
PRODUCT_YAML_PATH = ROOT / "products" / "BOSMAX_SERUM.yaml"

STEALTH_WORKBOOK_SHEETS = ("PRODUCT_BOSMAX_SERUM", "FAMILY_MALE_EXT_OIL")
STEALTH_SOURCE_HEADERS = [
    "Source_Script_Node",
    "Source_Variant_Hook_Node",
    "Source_Variant_Problem_Node",
    "Source_Variant_Solution_Node",
    "Source_Variant_CTA_Node",
]
GENERIC_BANNED_PHRASES = (
    "saiz lip balm",
    "chapstick",
    "botol hitam premium",
    "travel-friendly",
    "travel friendly",
    "selit dalam poket",
    "senang simpan",
    "ringkas, senang",
    "premium-black",
    "formula herba pekat",
    "melancarkan darah",
    "menyerap cepat",
    "packaging pocket-size",
    "pocket-size",
    "pocket size",
)
FORBIDDEN_DIRECT_PRONOUNS = ("saya", "anda", "awak", "kamu")
FORBIDDEN_MEDICAL_CLAIMS = (
    "melancarkan darah",
    "ubat",
    "merawat",
    "menyembuhkan",
    "mati pucuk",
    "erektil",
    "kebas",
)
REQUIRED_STEALTH_TOKENS = (
    "tork",
    "piston",
    "overhaul",
    "tiang seri",
    "enjin",
    "gear",
    "gearbox",
    "semput",
    "blackout",
    "starter",
    "jentera",
    "turbo",
    "cangkul",
    "pancang",
    "bateri",
)


@dataclass(frozen=True)
class SourceEntry:
    node: str
    text: str


def normalize(value: object) -> str:
    if value is None:
        return ""
    return " ".join(str(value).split()).strip()


def contains_term(text: str, term: str) -> bool:
    pattern = re.compile(rf"(?<![A-Za-z0-9_]){re.escape(term.lower())}(?![A-Za-z0-9_])")
    return pattern.search(text.lower()) is not None


def scrub_registry_text(text: str) -> str:
    cleaned = re.sub(r"\[[^\]]+\]\s*", "", normalize(text))
    cleaned = cleaned.replace("Attention:", "").replace("Interest:", "").replace("Desire:", "").replace("Action:", "")
    cleaned = cleaned.replace("'ENJIN'", "enjin").replace('"ENJIN"', "enjin")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def title_fragment(text: str, limit: int = 56) -> str:
    compact = scrub_registry_text(text)
    compact = compact.rstrip(".!?")
    return compact[:limit].strip()


def _extract_named_json(markdown: str, primary: str, secondary: str) -> dict[str, Any]:
    primary_match = re.search(
        rf"^\s*-\s+\*\*{re.escape(primary)}\*\* \(object\):\s*$",
        markdown,
        flags=re.MULTILINE,
    )
    if primary_match is None:
        raise ValueError(f"Missing primary node: {primary}")

    tail = markdown[primary_match.end() :]
    secondary_match = re.search(
        rf"^\s*-\s+\*\*{re.escape(secondary)}\*\* \(object\):\s*$",
        tail,
        flags=re.MULTILINE,
    )
    if secondary_match is None:
        raise ValueError(f"Missing secondary node: {primary}.{secondary}")

    after = tail[secondary_match.end() :]
    block_match = re.search(r"```json\s*(\{.*?\})\s*```", after, flags=re.DOTALL)
    if block_match is None:
        raise ValueError(f"Missing JSON block for node: {primary}.{secondary}")

    return json.loads(block_match.group(1))


def load_product_contract() -> dict[str, Any]:
    return yaml.safe_load(PRODUCT_YAML_PATH.read_text(encoding="utf-8"))


def load_authority_map() -> dict[str, Any]:
    return yaml.safe_load(AUTHORITY_MAP_PATH.read_text(encoding="utf-8"))


def load_formula_templates() -> dict[str, Any]:
    text = SCRIPT_REGISTRY_PATH.read_text(encoding="utf-8")
    primary_match = re.search(
        r"^\s*-\s+\*\*male_health_vintage_car\*\* \(object\):\s*$",
        text,
        flags=re.MULTILINE,
    )
    if primary_match is None:
        raise ValueError("Missing script registry node: male_health_vintage_car")

    tail = text[primary_match.end() :]
    formula_match = re.search(r"^\s*-\s+\*\*formula_templates\*\* \(object\):\s*$", tail, flags=re.MULTILINE)
    if formula_match is None:
        raise ValueError("Missing script registry formula_templates block")

    after = tail[formula_match.end() :]
    block_match = re.search(r"```json\s*(\{.*?\})\s*```", after, flags=re.DOTALL)
    if block_match is None:
        raise ValueError("Missing formula_templates JSON block")

    return json.loads(block_match.group(1))


def load_variant_primary() -> dict[str, Any]:
    return _extract_named_json(VARIANT_LIBRARY_PATH.read_text(encoding="utf-8"), "male_health_vintage_car", "EGO_01")


def load_variant_sparse() -> dict[str, Any]:
    return _extract_named_json(VARIANT_LIBRARY_PATH.read_text(encoding="utf-8"), "male_health_stealth_01", "EGO_01")


def source_cells() -> list[dict[str, str]]:
    formula_templates = load_formula_templates()
    primary = load_variant_primary()
    sparse = load_variant_sparse()["dialogue_payload"]

    hooks = [SourceEntry(f"variant_library.male_health_vintage_car.EGO_01.hooks.{item['id']}", item["text"]) for item in primary["hooks"]]
    problems = [SourceEntry(f"variant_library.male_health_vintage_car.EGO_01.problems.{item['id']}", item["text"]) for item in primary["problems"]]
    solutions = [SourceEntry(f"variant_library.male_health_vintage_car.EGO_01.solutions.{item['id']}", item["text"]) for item in primary["solutions"]]
    ctas = [SourceEntry(f"variant_library.male_health_vintage_car.EGO_01.cta.{item['id']}", item["text"]) for item in primary["cta"]]

    sparse_hook = SourceEntry(
        f"variant_library.male_health_stealth_01.EGO_01.dialogue_payload.hooks.{sparse['hooks'][0]['id']}",
        sparse["hooks"][0]["text"],
    )
    sparse_problem = SourceEntry(
        f"variant_library.male_health_stealth_01.EGO_01.dialogue_payload.problems.{sparse['problems'][0]['id']}",
        sparse["problems"][0]["text"],
    )

    formula_cycle = [
        ("PAS", "STEALTH_CAR_PAS_001"),
        ("SAVAGE_HPAS", "STEALTH_CAR_PAS_002"),
        ("HSO", "STEALTH_CAR_HSO_001"),
        ("AIDA", "STEALTH_CAR_AIDA_001"),
    ]
    script_lookup = {
        "STEALTH_CAR_PAS_001": formula_templates["PAS"]["scripts"][0],
        "STEALTH_CAR_PAS_002": formula_templates["PAS"]["scripts"][1],
        "STEALTH_CAR_HSO_001": formula_templates["HSO"]["scripts"][0],
        "STEALTH_CAR_AIDA_001": formula_templates["AIDA"]["scripts"][0],
    }

    rows: list[dict[str, str]] = []
    for idx in range(30):
        formula, script_id = formula_cycle[idx % len(formula_cycle)]
        script = script_lookup[script_id]
        hook_entry = hooks[idx % len(hooks)]
        problem_entry = problems[idx % len(problems)]
        solution_entry = solutions[idx % len(solutions)]
        cta_entry = ctas[idx % len(ctas)]

        if idx == 0:
            hook_entry = sparse_hook
            problem_entry = sparse_problem

        if script_id.startswith("STEALTH_CAR_PAS"):
            usp_1 = scrub_registry_text(script["solution"])
            usp_2 = scrub_registry_text(script["usp"])
            usp_3 = solution_entry.text
            angle = f"{formula} stealth reset | {title_fragment(hook_entry.text, 30)}"
        elif script_id == "STEALTH_CAR_HSO_001":
            usp_1 = scrub_registry_text(script["story"])
            usp_2 = scrub_registry_text(script["offer"])
            usp_3 = solution_entry.text
            angle = f"{formula} stealth restore | {title_fragment(problem_entry.text, 30)}"
        else:
            usp_1 = scrub_registry_text(script["interest"])
            usp_2 = scrub_registry_text(script["desire"])
            usp_3 = scrub_registry_text(script["usp"])
            angle = f"{formula} stealth ignition | {title_fragment(hook_entry.text, 30)}"

        rows.append(
            {
                "Angle": angle,
                "Hook": hook_entry.text,
                "Pain_or_Friction": problem_entry.text,
                "USP_1": usp_1,
                "USP_2": usp_2,
                "USP_3": usp_3,
                "CTA": cta_entry.text,
                "Copywriting_Formula": formula,
                "Authority_Source": "products/BOSMAX_SERUM.yaml + SCRIPT_REGISTRY_UNIFIED.md + SCRIPT_VARIANT_LIBRARY.md + registries/stealth_copy_authority_map.yaml",
                "Source_Script_Node": f"SCRIPT_REGISTRY_UNIFIED.md::male_health_vintage_car.formula_templates.{script_id}",
                "Source_Variant_Hook_Node": hook_entry.node,
                "Source_Variant_Problem_Node": problem_entry.node,
                "Source_Variant_Solution_Node": solution_entry.node,
                "Source_Variant_CTA_Node": cta_entry.node,
                "Notes": f"STEALTH authority locked to {script_id} + variant library nodes only.",
            }
        )

    return rows


def build_product_sheet_rows() -> list[dict[str, Any]]:
    product = load_product_contract()
    variants = product["variants"]
    source_rows = source_cells()
    rows: list[dict[str, Any]] = []

    for idx, source in enumerate(source_rows):
        variant = variants[idx % len(variants)]
        row_no = idx + 1
        rows.append(
            {
                "Row_ID": f"PRODUCT_BOSMAX_SERUM_R{row_no:03d}",
                "Family_Code": "FAMILY_MALE_EXT_SENSITIVE_OIL",
                "Family_Name": "Male Sensitive External Oil",
                "Product_ID_Optional": product["product_id"],
                "Product_Name_Optional": product["product_name"],
                "SKU_Optional": "",
                "Category": product["category"],
                "Sub_Category": product["sub_category"],
                "Product_Type": product["product_type"],
                "UOM": "Bottle",
                "Product_Size": variant["variant_name"],
                "Product_Scale": variant["scale_anchor_descriptor"],
                "Type_of_Content": "STEALTH",
                "Silo_Key": product["dialogue_authority"]["silo_id"],
                "Angle_ID": f"PRODUCT_BOSMAX_SERUM_ANG_{row_no:03d}",
                "Angle": source["Angle"],
                "Hook_ID": f"PRODUCT_BOSMAX_SERUM_HOOK_{row_no:03d}",
                "Hook": source["Hook"],
                "Pain_or_Friction": source["Pain_or_Friction"],
                "USP_1": source["USP_1"],
                "USP_2": source["USP_2"],
                "USP_3": source["USP_3"],
                "CTA_ID": f"PRODUCT_BOSMAX_SERUM_CTA_{row_no:03d}",
                "CTA": source["CTA"],
                "Copywriting_Formula": source["Copywriting_Formula"],
                "Authority_Source": source["Authority_Source"],
                "Source_Script_Node": source["Source_Script_Node"],
                "Source_Variant_Hook_Node": source["Source_Variant_Hook_Node"],
                "Source_Variant_Problem_Node": source["Source_Variant_Problem_Node"],
                "Source_Variant_Solution_Node": source["Source_Variant_Solution_Node"],
                "Source_Variant_CTA_Node": source["Source_Variant_CTA_Node"],
                "Fastmoss_Reference": "STEALTH authority locked to script registry + variant library only.",
                "Status": "SEED_READY",
                "Notes": f"{variant['variant_id']} authority-locked stealth copy row.",
            }
        )

    return rows


def build_family_sheet_rows() -> list[dict[str, Any]]:
    source_rows = source_cells()
    rows: list[dict[str, Any]] = []

    for idx, source in enumerate(source_rows):
        row_no = idx + 1
        rows.append(
            {
                "Row_ID": f"FAMILY_MALE_EXT_OIL_R{row_no:03d}",
                "Family_Code": "FAMILY_MALE_EXT_SENSITIVE_OIL",
                "Family_Name": "Male Sensitive External Oil",
                "Product_ID_Optional": "",
                "Product_Name_Optional": "",
                "SKU_Optional": "",
                "Category": "Health & Wellness",
                "Sub_Category": "Men's Health / Vitaliti Lelaki",
                "Product_Type": "Sensitive stealth massage oil family",
                "UOM": "VARIES",
                "Product_Size": "VARIES_BY_BRAND",
                "Product_Scale": "SEE_ACTUAL_PRODUCT_TRUTH",
                "Type_of_Content": "STEALTH",
                "Silo_Key": "male_health_stealth_01",
                "Angle_ID": f"FAMILY_MALE_EXT_OIL_ANG_{row_no:03d}",
                "Angle": source["Angle"],
                "Hook_ID": f"FAMILY_MALE_EXT_OIL_HOOK_{row_no:03d}",
                "Hook": source["Hook"],
                "Pain_or_Friction": source["Pain_or_Friction"],
                "USP_1": source["USP_1"],
                "USP_2": source["USP_2"],
                "USP_3": source["USP_3"],
                "CTA_ID": f"FAMILY_MALE_EXT_OIL_CTA_{row_no:03d}",
                "CTA": source["CTA"],
                "Copywriting_Formula": source["Copywriting_Formula"],
                "Authority_Source": source["Authority_Source"],
                "Source_Script_Node": source["Source_Script_Node"],
                "Source_Variant_Hook_Node": source["Source_Variant_Hook_Node"],
                "Source_Variant_Problem_Node": source["Source_Variant_Problem_Node"],
                "Source_Variant_Solution_Node": source["Source_Variant_Solution_Node"],
                "Source_Variant_CTA_Node": source["Source_Variant_CTA_Node"],
                "Fastmoss_Reference": "STEALTH family copy blocked from Fastmoss generic row inheritance.",
                "Status": "SEED_READY",
                "Notes": "Family stealth row resolved from registry + variant library only.",
            }
        )

    return rows


def validate_stealth_blob(text: str) -> list[str]:
    lowered = normalize(text).lower()
    issues: list[str] = []

    if any(contains_term(lowered, phrase) for phrase in GENERIC_BANNED_PHRASES):
        issues.append("generic packaging or convenience phrasing detected")
    if any(contains_term(lowered, pronoun) for pronoun in FORBIDDEN_DIRECT_PRONOUNS):
        issues.append("direct pronoun leakage detected")
    if any(contains_term(lowered, claim) for claim in FORBIDDEN_MEDICAL_CLAIMS):
        issues.append("medical claim leakage detected")
    if not any(token in lowered for token in REQUIRED_STEALTH_TOKENS):
        issues.append("required stealth metaphor vocabulary missing")
    return issues
