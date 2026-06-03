from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.worksheet import Worksheet


ROOT = Path(r"C:\Users\USER\Desktop\Claude Cowork Bosmax Agents")
SOURCE_WORKBOOK = Path(r"C:\Users\USER\Downloads\Product_copywriting_library.xlsx")
OUTPUT_WORKBOOK = Path(r"C:\Users\USER\Downloads\Product_copywriting_library_IMPLEMENTED.xlsx")
FASTMOSS_WORKBOOK = ROOT / "FASTMOSS_COMBINED_10_FILES_WORKBOOK.xlsx"
FLAGSHIP_SHEET_BOSMAX = "PRODUCT_BOSMAX_SERUM"
FLAGSHIP_SHEET_MWCB = "PRODUCT_MW_CAP_BURUNG"

WORKING_HEADERS = [
    "Row_ID",
    "Archetype_Code",
    "Archetype_Name",
    "Product_ID_Optional",
    "Product_Name_Optional",
    "SKU_Optional",
    "Category",
    "Sub_Category",
    "Product_Type",
    "UOM",
    "Product_Size",
    "Product_Scale",
    "Type_of_Content",
    "Silo_Key",
    "Angle_ID",
    "Angle",
    "Hook_ID",
    "Hook",
    "USP_1",
    "USP_2",
    "USP_3",
    "CTA_ID",
    "CTA",
    "Copywriting_Formula",
    "Authority_Source",
    "Fastmoss_Reference",
    "Status",
    "Notes",
]

TAXONOMY_HEADERS = [
    "Archetype_Code",
    "Archetype_Name",
    "Worksheet_Name",
    "Type_of_Content",
    "Silo_Key_Default",
    "Default_Formula",
    "Category_Family",
    "Sub_Category_Family",
    "Representative_Product_Type",
    "Mapped_Product_Count",
    "Representative_Products",
    "Flagship_Link",
    "Authority_Source",
    "Notes",
]

INDEX_HEADERS = ["Sheet_Name", "Role", "Fill_Owner", "Description"]

READ_ME_ROWS = [
    ("Workbook Role", "Operator-facing copywriting library that supplements SCRIPT_REGISTRY_UNIFIED.md and SCRIPT_VARIANT_LIBRARY.md."),
    ("Authority Boundary", "Runtime-sensitive dialogue authority stays in script registry and variant library. Workbook is a structured library and Antigravity input surface."),
    ("Row Contract", "One row = one coherent angle-hook pair with one USP triplet, one CTA, and one chosen formula."),
    ("Antigravity Scope", "Antigravity should fill or expand Type_of_Content, Silo_Key, Angle, Hook, USP_1-3, CTA, Copywriting_Formula, and Notes only."),
    ("Do Not Use", "Do not treat placeholder copy as final. Do not overwrite flagship product truth from products/*.yaml."),
    ("Status Values", "SEED_READY, ANTIGRAVITY_FILL_PENDING, REVIEW_REQUIRED, APPROVED, LOCKED"),
    ("Formula Values", "AIDA, PAS, HSO, HPAS, SAVAGE_HPAS"),
    ("Type_of_Content Values", "DIRECT, STEALTH"),
]

HEADER_FILL = PatternFill("solid", fgColor="1F4E78")
SUB_HEADER_FILL = PatternFill("solid", fgColor="D9EAF7")
TAXONOMY_FILL = PatternFill("solid", fgColor="5B9BD5")
FLAGSHIP_FILL = PatternFill("solid", fgColor="C00000")
ARCHETYPE_FILL = PatternFill("solid", fgColor="70AD47")
WHITE_FONT = Font(color="FFFFFF", bold=True)
BOLD_FONT = Font(bold=True)
WRAP_ALIGNMENT = Alignment(wrap_text=True, vertical="top")

FORMULA_OPTIONS = ["AIDA", "PAS", "HSO", "HPAS", "SAVAGE_HPAS"]
TYPE_OF_CONTENT_OPTIONS = ["DIRECT", "STEALTH"]
STATUS_OPTIONS = ["SEED_READY", "ANTIGRAVITY_FILL_PENDING", "REVIEW_REQUIRED", "APPROVED", "LOCKED"]

MANDATORY_ARCHETYPES: dict[str, dict[str, str]] = {
    "ARCH_STEALTH_MASSAGE_OIL": {
        "name": "Stealth Massage Oil",
        "type_of_content": "STEALTH",
        "silo_key": "male_health_stealth_generic",
        "default_formula": "PAS",
        "category_family": "Health & Wellness",
        "sub_category_family": "Men's Health / Vitaliti Lelaki",
        "notes": "Mandatory archetype parent for BOSMAX Serum and future stealth massage-oil lanes.",
        "flagship_link": FLAGSHIP_SHEET_BOSMAX,
        "authority_source": "products/BOSMAX_SERUM.yaml + script registry surfaces",
    },
    "ARCH_TRADITIONAL_REMEDY_DIRECT": {
        "name": "Traditional Remedy Direct",
        "type_of_content": "DIRECT",
        "silo_key": "traditional_remedy_direct",
        "default_formula": "PAS",
        "category_family": "Health & Wellness",
        "sub_category_family": "Traditional Remedy / Minyak Urut",
        "notes": "Mandatory archetype parent for Minyak Warisan Cap Burung and future direct remedy lanes.",
        "flagship_link": FLAGSHIP_SHEET_MWCB,
        "authority_source": "products/CAP_BURUNG_MINYAK.yaml",
    },
    "ARCH_MEN_PERFUME": {
        "name": "Men Perfume Direct",
        "type_of_content": "DIRECT",
        "silo_key": "men_perfume_direct",
        "default_formula": "AIDA",
        "category_family": "Beauty & Personal Care",
        "sub_category_family": "Perfume",
        "notes": "Mandatory archetype for future men perfume routing and Antigravity fill.",
        "flagship_link": "",
        "authority_source": "FASTMOSS_COMBINED_10_FILES_WORKBOOK.xlsx::Copywriting_Product_Map",
    },
    "ARCH_WOMEN_PERFUME": {
        "name": "Women Perfume Direct",
        "type_of_content": "DIRECT",
        "silo_key": "women_perfume_direct",
        "default_formula": "AIDA",
        "category_family": "Beauty & Personal Care",
        "sub_category_family": "Perfume",
        "notes": "Mandatory archetype for future women perfume routing and Antigravity fill.",
        "flagship_link": "",
        "authority_source": "FASTMOSS_COMBINED_10_FILES_WORKBOOK.xlsx::Copywriting_Product_Map",
    },
}


@dataclass
class Archetype:
    code: str
    name: str
    worksheet_name: str
    type_of_content: str
    silo_key: str
    default_formula: str
    category_family: str
    sub_category_family: str
    notes: str


def normalize_spaces(value: str | None) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def slugify(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", value.upper()).strip("_")
    return re.sub(r"_+", "_", cleaned)[:40] or "GENERIC"


def excel_sheet_name(name: str) -> str:
    if len(name) <= 31:
        return name

    if name == "PRODUCT_MINYAK_WARISAN_CAP_BURUNG":
        return FLAGSHIP_SHEET_MWCB

    candidate = name
    replacements = {
        "ELECTRICAL": "ELEC",
        "EQUIPMENT": "EQUIP",
        "SUPPLIES": "SUPPLY",
        "CLOTHING": "CLOTH",
        "OUTDOOR": "OUTDR",
        "SPORT": "SPRT",
    }
    for old, new in replacements.items():
        candidate = candidate.replace(old, new)

    return candidate[:31]


def title_case_key(value: str) -> str:
    value = normalize_spaces(value)
    if not value:
        return ""
    return value.replace("&", "and")


def safe_yaml_load(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def infer_type_of_content(category: str, sub_category: str, product_type: str, product_name: str) -> str:
    text = " ".join([category, sub_category, product_type, product_name]).lower()
    stealth_keywords = [
        "men's health",
        "vitaliti lelaki",
        "male health",
        "feminine care",
        "female health",
        "intimate",
        "sensitif",
    ]
    if any(keyword in text for keyword in stealth_keywords):
        return "STEALTH"
    return "DIRECT"


def archetype_from_fastmoss(category: str, sub_category: str, product_type: str, product_name: str) -> Archetype:
    category_n = normalize_spaces(category)
    sub_n = normalize_spaces(sub_category)
    type_n = normalize_spaces(product_type)
    name_n = normalize_spaces(product_name)
    type_text = " ".join([category_n, sub_n, type_n]).lower()
    full_text = " ".join([category_n, sub_n, type_n, name_n]).lower()
    content_type = infer_type_of_content(category_n, sub_n, type_n, name_n)

    def build(
        code: str,
        name: str,
        silo_key: str,
        default_formula: str,
        notes: str,
    ) -> Archetype:
        return Archetype(
            code=code,
            name=name,
            worksheet_name=excel_sheet_name(code),
            type_of_content=content_type,
            silo_key=silo_key,
            default_formula=default_formula,
            category_family=category_n,
            sub_category_family=sub_n,
            notes=notes,
        )

    if "massage oil" in type_text or "minyak urut" in type_text or "traditional remedy" in type_text or "minyak angin" in type_text:
        if content_type == "STEALTH":
            return build(
                "ARCH_STEALTH_MASSAGE_OIL",
                "Stealth Massage Oil",
                "male_health_stealth_generic",
                "PAS",
                "Sensitive male/female massage-oil family using euphemistic or metaphor-based copy.",
            )
        return build(
            "ARCH_TRADITIONAL_REMEDY_DIRECT",
            "Traditional Remedy Direct",
            "traditional_remedy_direct",
            "PAS",
            "Traditional remedy or minyak urut family with direct household-relief copy.",
        )

    if "men's perfume" in type_text:
        return build("ARCH_MEN_PERFUME", "Men Perfume Direct", "men_perfume_direct", "AIDA", "Men fragrance products focused on style, scent identity, and confidence.")
    if "women's perfume" in type_text:
        return build("ARCH_WOMEN_PERFUME", "Women Perfume Direct", "women_perfume_direct", "AIDA", "Women fragrance products focused on scent mood, style, and confidence.")
    if "unisex perfume" in type_text or ("perfume" in type_text and "men's perfume" not in type_text and "women's perfume" not in type_text):
        return build("ARCH_UNISEX_PERFUME", "Unisex Perfume Direct", "unisex_perfume_direct", "AIDA", "Unisex fragrance products built around freshness, confidence, and all-day scent.")

    if any(keyword in type_text for keyword in ["facial cleanser", "moisturizer", "mist", "sunscreen", "sun care", "body serum", "body care kits", "beauty supplement", "wellness supplements", "lipstick", "lip gloss", "concealer", "foundation", "makeup", "fixing spray", "haircare", "shampoo", "conditioner"]):
        return build("ARCH_BEAUTY_CONFIDENCE", "Beauty Confidence Direct", "beauty_confidence_direct", "HPAS", "Beauty, skincare, and cosmetic products driven by confidence, before-after, and benefit proof.")

    if any(keyword in type_text for keyword in ["body wash", "soap", "deodorant", "antiperspirant"]):
        return build("ARCH_BODY_CARE_FRESHNESS", "Body Care Freshness Direct", "body_care_freshness_direct", "PAS", "Body care freshness lane focused on smell, hygiene, and daily comfort.")

    if any(keyword in type_text for keyword in ["diapers", "baby care", "baby & maternity"]):
        return build("ARCH_BABY_CARE_ESSENTIALS", "Baby Care Essentials Direct", "baby_care_essentials_direct", "PAS", "Baby-care products positioned around comfort, safety, and parent pain-points.")

    if any(keyword in type_text for keyword in ["instant hijab", "square hijabs", "tracksuits", "sportswear", "shirts", "blouses", "trousers", "bras", "socks", "underwear", "womenswear", "menswear", "muslim fashion"]):
        return build("ARCH_FASHION_STYLE_FIT", "Fashion Style Fit Direct", "fashion_style_fit_direct", "AIDA", "Fashion lane centered on fit, style, comfort, and occasion-based hooks.")

    if any(keyword in type_text for keyword in ["household cleaner", "cleaners", "fabric", "freshener", "laundry", "deodorizer"]):
        return build("ARCH_HOUSEHOLD_CLEANING", "Household Cleaning Direct", "household_cleaning_direct", "HPAS", "Problem-removal household lane built around mess, smell, and visible cleaning proof.")

    if any(keyword in type_text for keyword in ["storage boxes", "bins", "organizer", "organisers", "organizers"]):
        return build("ARCH_HOME_ORGANIZATION", "Home Organization Direct", "home_organization_direct", "AIDA", "Home organization lane focused on tidy spaces, capacity, and convenience.")

    if any(keyword in type_text for keyword in ["bedding", "sheets", "pillowcases", "curtains", "carpets", "mats", "rugs", "textiles"]):
        return build("ARCH_HOME_COMFORT_TEXTILES", "Home Comfort Textiles Direct", "home_comfort_textiles_direct", "AIDA", "Home textiles lane focused on comfort, transformation, and cozy-room appeal.")

    if any(keyword in type_text for keyword in ["cookware", "container", "tray", "kitchen", "food saver"]):
        return build("ARCH_KITCHENWARE_FUNCTIONAL", "Kitchenware Functional Direct", "kitchenware_functional_direct", "HPAS", "Kitchenware lane focused on utility, convenience, and daily use proof.")

    if any(keyword in type_text for keyword in ["instant noodles", "spaghetti", "popcorn", "cooking sauces", "canned", "packaged foods", "food & beverages", "chocolate"]):
        return build("ARCH_FOOD_CONVENIENCE_TASTE", "Food Convenience Taste Direct", "food_convenience_taste_direct", "AIDA", "Food lane focused on taste, convenience, craving, and serving occasion.")

    if any(keyword in full_text for keyword in ["car fragrance", "air freshener"]):
        return build("ARCH_CAR_FRAGRANCE", "Car Fragrance Direct", "car_fragrance_direct", "HPAS", "Car fragrance lane focused on smell removal, freshness, and in-car vibe.")

    if any(keyword in type_text for keyword in ["automotive", "motorcycle", "car interior accessories"]):
        return build("ARCH_AUTOMOTIVE_ACCESSORY", "Automotive Accessory Direct", "automotive_accessory_direct", "HPAS", "Automotive accessory lane built around problem removal, convenience, and visible upgrades.")

    if any(keyword in type_text for keyword in ["cables", "chargers", "adapters", "electronics"]):
        return build("ARCH_GADGET_ACCESSORY", "Gadget Accessory Direct", "gadget_accessory_direct", "HPAS", "Gadget accessory lane focused on practicality, compatibility, and everyday convenience.")

    if any(keyword in type_text for keyword in ["cat food", "dog", "pet"]):
        return build("ARCH_PET_CARE", "Pet Care Direct", "pet_care_direct", "PAS", "Pet care lane built around animal comfort, owner worry, and daily-use proof.")

    if any(keyword in full_text for keyword in ["stationery", "office", "writing", "teacher", "gift"]):
        return build("ARCH_STATIONERY_GIFT", "Stationery Gift Direct", "stationery_gift_direct", "AIDA", "Stationery and gift lane focused on usefulness, gifting, and seasonal moments.")

    if any(keyword in type_text for keyword in ["religion", "philosophy", "book", "books"]):
        return build("ARCH_KNOWLEDGE_SPIRITUAL", "Knowledge Spiritual Direct", "knowledge_spiritual_direct", "AIDA", "Book and spiritual lane focused on meaning, guidance, and self-improvement.")

    if "health & wellness" in type_text or "wellness" in type_text or "supplements" in type_text:
        return build("ARCH_WELLNESS_SUPPLEMENTS", "Wellness Supplements Direct", "wellness_supplements_direct", "PAS", "Wellness lane centered on daily relief, routine, and benefit-led proof.")

    fallback_base = slugify(sub_n or type_n or category_n)
    return build(
        f"ARCH_MISC_{fallback_base}",
        f"Misc {title_case_key(sub_n or type_n or category_n)} Direct",
        f"misc_{fallback_base.lower()}_direct",
        "AIDA",
        "Fallback archetype for uncaptured product families. Review if product volume grows.",
    )


def build_fastmoss_reference(product_name: str, shop_name: str) -> str:
    return f"Copywriting_Product_Map | Product={normalize_spaces(product_name)} | Shop={normalize_spaces(shop_name)}"


def load_fastmoss_copy_map() -> list[dict[str, Any]]:
    wb = load_workbook(FASTMOSS_WORKBOOK, read_only=True, data_only=True)
    ws = wb["Copywriting_Product_Map"]
    results: list[dict[str, Any]] = []
    for row in ws.iter_rows(min_row=5, values_only=True):
        if not row or not row[1]:
            continue
        rank = int(row[0])
        product_name = normalize_spaces(row[1])
        shop_name = normalize_spaces(row[2])
        category = normalize_spaces(row[3]).replace("Beauty & Personal Care", "Beauty & Personal Care")
        sub_category = normalize_spaces(row[4])
        product_type = normalize_spaces(row[5])
        angle = normalize_spaces(row[14])
        hook = normalize_spaces(row[15])
        usp_1 = normalize_spaces(row[16])
        usp_2 = normalize_spaces(row[17])
        usp_3 = normalize_spaces(row[18])
        cta = normalize_spaces(row[20])
        archetype = archetype_from_fastmoss(category, sub_category, product_type, product_name)
        results.append(
            {
                "rank": rank,
                "product_name": product_name,
                "shop_name": shop_name,
                "category": category,
                "sub_category": sub_category,
                "product_type": product_type,
                "angle": angle,
                "hook": hook,
                "usp_1": usp_1,
                "usp_2": usp_2,
                "usp_3": usp_3,
                "cta": cta,
                "fastmoss_reference": build_fastmoss_reference(product_name, shop_name),
                "archetype": archetype,
            }
        )
    return results


def flagship_bosmax_rows() -> list[list[Any]]:
    product = safe_yaml_load(ROOT / "products" / "BOSMAX_SERUM.yaml")
    authority = "SCRIPT_REGISTRY_UNIFIED.md + SCRIPT_VARIANT_LIBRARY.md + products/BOSMAX_SERUM.yaml"
    common = {
        "Archetype_Code": "ARCH_STEALTH_MASSAGE_OIL",
        "Archetype_Name": "Stealth Massage Oil",
        "Product_ID_Optional": product["product_id"],
        "Product_Name_Optional": product["product_name"],
        "SKU_Optional": "",
        "Category": product["category"],
        "Sub_Category": product["sub_category"],
        "Product_Type": "Sensitive stealth massage oil flagship",
        "Type_of_Content": "STEALTH",
        "Silo_Key": product["dialogue_authority"]["silo_id"],
        "Authority_Source": authority,
        "Fastmoss_Reference": "No confirmed direct Fastmoss listing as of 2026-06-02.",
        "Status": "SEED_READY",
    }

    starter_rows = [
        {
            "variant_id": "5ML",
            "uom": "Bottle",
            "size": "5 ml",
            "scale": "EXACTLY lip balm size, fit into fingers naturally",
            "angle_id": "ANG_001",
            "angle": "Maruah recovery with discreet pocket carry",
            "hook_id": "HOOK_001",
            "hook": "Enjin panas terus mati. Kesian abang!",
            "usp_1": "Saiz lip balm, senang simpan dan bawa tanpa nampak seperti produk sensitif.",
            "usp_2": "Botol hitam premium yang discreet, maskulin, dan tak menarik perhatian.",
            "usp_3": "Lane copy ini mesti kekal STEALTH supaya maruah dan positioning produk tak bocor.",
            "cta_id": "CTA_001",
            "cta": "SERVIS ENJIN KAU.",
            "formula": "PAS",
            "notes": "5ml flagship starter row derived from male_health_vintage_car hook set.",
        },
        {
            "variant_id": "5ML",
            "uom": "Bottle",
            "size": "5 ml",
            "scale": "EXACTLY lip balm size, fit into fingers naturally",
            "angle_id": "ANG_002",
            "angle": "Performance confidence without obvious product signaling",
            "hook_id": "HOOK_005",
            "hook": "Member lain ride sampai pagi, abang tersadai awal?",
            "usp_1": "Compact travel bottle sesuai untuk emergency carry dan repeat use harian.",
            "usp_2": "Visual identity kekal premium-black dan selari dengan sensitive male wellness positioning.",
            "usp_3": "Hook boleh bermain pada ego, tetapi product framing mesti kekal selamat dan euphemistic.",
            "cta_id": "CTA_002",
            "cta": "OVERHAUL SEKARANG.",
            "formula": "SAVAGE_HPAS",
            "notes": "Aggressive flagship row for Antigravity expansion under BOSMAX control.",
        },
        {
            "variant_id": "10ML",
            "uom": "Bottle",
            "size": "10 ml",
            "scale": "EXACTLY chapstick size, fit into fingers naturally",
            "angle_id": "ANG_003",
            "angle": "Chapstick-size confidence reset with premium wellness look",
            "hook_id": "HOOK_006",
            "hook": "Bilik dah gelap. Abang pulak yang short-circuit. Malu!",
            "usp_1": "Saiz chapstick, mudah genggam dan lebih hero-ready untuk visual close-up.",
            "usp_2": "Label BOSMAX HERBS yang jelas bantu product truth tanpa nampak murah atau pelik.",
            "usp_3": "Sesuai untuk angle restore confidence sambil kekalkan premium discreet tone.",
            "cta_id": "CTA_006",
            "cta": "JANGAN BLACKOUT LAGI.",
            "formula": "HSO",
            "notes": "10ml flagship starter row with story-offer structure.",
        },
        {
            "variant_id": "10ML",
            "uom": "Bottle",
            "size": "10 ml",
            "scale": "EXACTLY chapstick size, fit into fingers naturally",
            "angle_id": "ANG_004",
            "angle": "Discreet daily carry for lelaki yang tak mahu hilang yakin",
            "hook_id": "HOOK_011",
            "hook": "Body sado. Enjin kosong. Abang ni hantu jalanan ke?",
            "usp_1": "Botol finger-length ini cukup kecil untuk bawa tanpa rasa janggal.",
            "usp_2": "Packaging hitam premium membantu stealth positioning dalam visual dan copy.",
            "usp_3": "Formula starter ini patut dikembangkan tanpa memecahkan authority registry untuk sensitive copy.",
            "cta_id": "CTA_011",
            "cta": "KUKUHKAN TIANG KAU.",
            "formula": "PAS",
            "notes": "10ml flagship row seeded for direct Antigravity expansion.",
        },
    ]

    rows: list[list[Any]] = []
    for idx, starter in enumerate(starter_rows, start=1):
        row_id = f"{FLAGSHIP_SHEET_BOSMAX}_R{idx:03d}"
        rows.append(
            [
                row_id,
                common["Archetype_Code"],
                common["Archetype_Name"],
                common["Product_ID_Optional"],
                common["Product_Name_Optional"],
                common["SKU_Optional"],
                common["Category"],
                common["Sub_Category"],
                common["Product_Type"],
                starter["uom"],
                starter["size"],
                starter["scale"],
                common["Type_of_Content"],
                common["Silo_Key"],
                starter["angle_id"],
                starter["angle"],
                starter["hook_id"],
                starter["hook"],
                starter["usp_1"],
                starter["usp_2"],
                starter["usp_3"],
                starter["cta_id"],
                starter["cta"],
                starter["formula"],
                common["Authority_Source"],
                common["Fastmoss_Reference"],
                common["Status"],
                starter["notes"],
            ]
        )
    return rows


def flagship_mwcb_rows() -> list[list[Any]]:
    product = safe_yaml_load(ROOT / "products" / "CAP_BURUNG_MINYAK.yaml")
    variant = product["variants"][0]
    authority = "products/CAP_BURUNG_MINYAK.yaml"
    starter_rows = [
        (
            "ANG_001",
            "Household standby remedy with heritage trust",
            "HOOK_001",
            "Dalam rumah memang kena ada satu botol standby bila kepala berat, badan sengal, atau angin datang tiba-tiba.",
            "Warisan keluarga sejak 1958 memberi trust dan rasa produk rumah yang orang simpan lama.",
            "Botol WG40 30ml ini kecil, senang simpan, dan terus nampak seperti minyak warisan sebenar.",
            "Boleh diposisikan sebagai peneman harian untuk urut ringan, segar, dan rasa lega cepat.",
            "CTA_001",
            "Simpan satu botol dekat rumah dan tekan beg kuning sekarang.",
            "PAS",
            "Family-utility direct row for flagship traditional remedy.",
        ),
        (
            "ANG_002",
            "Pocket-size traditional relief for travel and daily carry",
            "HOOK_002",
            "Botol kecil macam ni yang selalu orang cari sebab senang bawa, tapi masih rasa lengkap bila diperlukan.",
            "Saiz 30ml pocket-size memudahkan carry tanpa makan ruang.",
            "Red ribbed cap dan botol kaca jernih bantu product truth kekal kuat dalam visual dan demo.",
            "Aroma herbal-eucalyptus-menthol beri rasa segar dan familiar untuk lane direct household remedy.",
            "CTA_002",
            "Masukkan dalam beg sekarang supaya tak cari bila dah perlu nanti.",
            "AIDA",
            "Travel-carry flagship direct row.",
        ),
        (
            "ANG_003",
            "Petua turun-temurun for urut, sengal, and family comfort",
            "HOOK_003",
            "Ramai suka jenis minyak yang ada rasa warisan sebenar, bukan sekadar botol cantik tapi kosong fungsi.",
            "Tagline Petua Turun Temurun kuat untuk angle trust dan familiarity keluarga.",
            "Boleh dibawa ke angle urut badan, rasa lega, dan kelegaan harian yang mudah difahami.",
            "Label hijau-krim heritage dan burung bertenggek mengunci identiti produk daripada nampak generic.",
            "CTA_003",
            "Klik beg kuning dan tambah minyak warisan ni dalam stok rumah hari ini.",
            "HSO",
            "Heritage-story flagship row.",
        ),
        (
            "ANG_004",
            "Aromatherapy freshness and rumah-tenang positioning",
            "HOOK_004",
            "Kadang orang bukan cari produk pelik pun, mereka cuma nak sesuatu yang buat badan rasa ringan dan kepala rasa lapang semula.",
            "Aroma terapi herbal membantu angle segar, tenang, dan less-stressed.",
            "Tekstur ringan dan cepat sapu sesuai untuk daily routine without fuss.",
            "Produk ini boleh masuk lane urut ringan, sapuan harian, dan comfort-at-home positioning.",
            "CTA_004",
            "Try satu botol dulu dan rasa sendiri beza dia pada rutin harian.",
            "HPAS",
            "Freshness and calm direct row.",
        ),
    ]

    rows: list[list[Any]] = []
    for idx, row in enumerate(starter_rows, start=1):
        rows.append(
            [
                f"{FLAGSHIP_SHEET_MWCB}_R{idx:03d}",
                "ARCH_TRADITIONAL_REMEDY_DIRECT",
                "Traditional Remedy Direct",
                product["product_id"],
                product["product_name"],
                "",
                product["category"],
                product["sub_category"],
                product["product_type"],
                "Bottle",
                "30 ml",
                variant["scale_anchor_descriptor"],
                "DIRECT",
                "traditional_remedy_direct",
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
                authority,
                "No confirmed direct Fastmoss listing mapped yet; use product registry truth first.",
                "SEED_READY",
                row[10],
            ]
        )
    return rows


def build_taxonomy(fastmoss_rows: list[dict[str, Any]]) -> tuple[list[list[Any]], dict[str, list[dict[str, Any]]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in fastmoss_rows:
        grouped[row["archetype"].code].append(row)

    taxonomy_rows: list[list[Any]] = []
    for code in sorted(grouped):
        sample_rows = sorted(grouped[code], key=lambda item: item["rank"])
        archetype = sample_rows[0]["archetype"]
        examples = " | ".join(item["product_name"] for item in sample_rows[:3])
        flagship_link = ""
        if code == "ARCH_STEALTH_MASSAGE_OIL":
            flagship_link = FLAGSHIP_SHEET_BOSMAX
        elif code == "ARCH_TRADITIONAL_REMEDY_DIRECT":
            flagship_link = FLAGSHIP_SHEET_MWCB
        taxonomy_rows.append(
            [
                archetype.code,
                archetype.name,
                archetype.worksheet_name,
                archetype.type_of_content,
                archetype.silo_key,
                archetype.default_formula,
                archetype.category_family,
                archetype.sub_category_family,
                sample_rows[0]["product_type"],
                len(sample_rows),
                examples,
                flagship_link,
                "FASTMOSS_COMBINED_10_FILES_WORKBOOK.xlsx::Copywriting_Product_Map",
                archetype.notes,
            ]
        )

    existing_codes = {row[0] for row in taxonomy_rows}
    for code, meta in MANDATORY_ARCHETYPES.items():
        if code in existing_codes:
            continue
        taxonomy_rows.append(
            [
                code,
                meta["name"],
                excel_sheet_name(code),
                meta["type_of_content"],
                meta["silo_key"],
                meta["default_formula"],
                meta["category_family"],
                meta["sub_category_family"],
                "",
                0,
                "",
                meta["flagship_link"],
                meta["authority_source"],
                meta["notes"],
            ]
        )
        grouped.setdefault(code, [])
    taxonomy_rows.sort(key=lambda row: row[0])
    return taxonomy_rows, grouped


def style_header(ws: Worksheet, fill: PatternFill) -> None:
    for cell in ws[1]:
        cell.fill = fill
        cell.font = WHITE_FONT
        cell.alignment = WRAP_ALIGNMENT


def set_standard_layout(ws: Worksheet) -> None:
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    for column in ws.columns:
        max_length = max(len(normalize_spaces(str(cell.value))) if cell.value is not None else 0 for cell in column)
        ws.column_dimensions[column[0].column_letter].width = min(max(max_length + 2, 14), 42)
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = WRAP_ALIGNMENT


def add_validations(ws: Worksheet) -> None:
    type_validation = DataValidation(type="list", formula1='"DIRECT,STEALTH"', allow_blank=True)
    formula_validation = DataValidation(type="list", formula1='"AIDA,PAS,HSO,HPAS,SAVAGE_HPAS"', allow_blank=True)
    status_validation = DataValidation(type="list", formula1='"SEED_READY,ANTIGRAVITY_FILL_PENDING,REVIEW_REQUIRED,APPROVED,LOCKED"', allow_blank=True)
    ws.add_data_validation(type_validation)
    ws.add_data_validation(formula_validation)
    ws.add_data_validation(status_validation)
    type_validation.add("M2:M5000")
    formula_validation.add("X2:X5000")
    status_validation.add("AA2:AA5000")


def create_sheet_with_headers(wb: Workbook, title: str, headers: list[str], header_fill: PatternFill) -> Worksheet:
    ws = wb.create_sheet(title=title)
    ws.append(headers)
    style_header(ws, header_fill)
    return ws


def write_rows(ws: Worksheet, rows: list[list[Any]]) -> None:
    for row in rows:
        ws.append(row)
    set_standard_layout(ws)


def write_index_sheet(wb: Workbook, archetype_codes: list[str]) -> None:
    ws = wb.active
    ws.title = "INDEX"
    ws.append(INDEX_HEADERS)
    style_header(ws, HEADER_FILL)
    rows = [
        ["INDEX", "Governance", "System", "Navigation sheet for workbook structure and fill responsibilities."],
        ["README_OR_RULES", "Governance", "System", "Operational rules, authority boundaries, and allowed fill surfaces for Antigravity."],
        ["TAXONOMY_MASTER", "Taxonomy", "System", "Deduped Fastmoss-to-archetype routing table and worksheet map."],
        [FLAGSHIP_SHEET_BOSMAX, "Flagship Product", "Human + Antigravity", "Controlled flagship sheet for BOSMAX Serum 5ml and 10ml sensitive copy rows."],
        [FLAGSHIP_SHEET_MWCB, "Flagship Product", "Human + Antigravity", "Controlled flagship sheet for Minyak Warisan Cap Burung direct copy rows."],
    ]
    for code in archetype_codes:
        rows.append([excel_sheet_name(code), "Archetype Library", "Antigravity", f"Reusable archetype sheet for {code.replace('ARCH_', '').replace('_', ' ').title()} copy expansion."])
    write_rows(ws, rows)


def write_readme_sheet(wb: Workbook) -> None:
    ws = create_sheet_with_headers(wb, "README_OR_RULES", ["Rule", "Detail"], HEADER_FILL)
    for rule, detail in READ_ME_ROWS:
        ws.append([rule, detail])
    set_standard_layout(ws)


def seed_archetype_rows(grouped: dict[str, list[dict[str, Any]]]) -> dict[str, list[list[Any]]]:
    seeded: dict[str, list[list[Any]]] = {}
    for code, rows in grouped.items():
        sorted_rows = sorted(rows, key=lambda item: item["rank"])
        starter_rows: list[list[Any]] = []
        for idx, row in enumerate(sorted_rows[:3], start=1):
            archetype: Archetype = row["archetype"]
            starter_rows.append(
                [
                    f"{code}_R{idx:03d}",
                    code,
                    archetype.name,
                    "",
                    row["product_name"],
                    "",
                    row["category"],
                    row["sub_category"],
                    row["product_type"],
                    "VARIES",
                    "VARIES_BY_PRODUCT",
                    "SEE_PRODUCT_TRUTH",
                    archetype.type_of_content,
                    archetype.silo_key,
                    f"{code}_ANG_{idx:03d}",
                    row["angle"],
                    f"{code}_HOOK_{idx:03d}",
                    row["hook"],
                    row["usp_1"],
                    row["usp_2"],
                    row["usp_3"],
                    f"{code}_CTA_{idx:03d}",
                    row["cta"],
                    archetype.default_formula,
                    "FASTMOSS_COMBINED_10_FILES_WORKBOOK.xlsx::Copywriting_Product_Map",
                    row["fastmoss_reference"],
                    "SEED_READY",
                    "Representative Fastmoss starter row. Generalize before large-scale Antigravity fill if needed.",
                ]
            )
        seeded[code] = starter_rows
    return seeded


def build_workbook() -> None:
    if not SOURCE_WORKBOOK.exists():
        raise FileNotFoundError(f"Source skeleton workbook not found: {SOURCE_WORKBOOK}")

    fastmoss_rows = load_fastmoss_copy_map()
    taxonomy_rows, grouped = build_taxonomy(fastmoss_rows)
    seeded_archetypes = seed_archetype_rows(grouped)

    wb = Workbook()
    write_index_sheet(wb, [row[0] for row in taxonomy_rows])
    write_readme_sheet(wb)

    taxonomy_ws = create_sheet_with_headers(wb, "TAXONOMY_MASTER", TAXONOMY_HEADERS, TAXONOMY_FILL)
    write_rows(taxonomy_ws, taxonomy_rows)

    bosmax_ws = create_sheet_with_headers(wb, FLAGSHIP_SHEET_BOSMAX, WORKING_HEADERS, FLAGSHIP_FILL)
    write_rows(bosmax_ws, flagship_bosmax_rows())
    add_validations(bosmax_ws)

    mwcb_ws = create_sheet_with_headers(wb, FLAGSHIP_SHEET_MWCB, WORKING_HEADERS, FLAGSHIP_FILL)
    write_rows(mwcb_ws, flagship_mwcb_rows())
    add_validations(mwcb_ws)

    for code, rows in seeded_archetypes.items():
        ws = create_sheet_with_headers(wb, excel_sheet_name(code), WORKING_HEADERS, ARCHETYPE_FILL)
        write_rows(ws, rows)
        add_validations(ws)

    # Visual differentiation for flagship and archetype tabs on row 2 when present.
    for ws in wb.worksheets:
        if ws.title.startswith("PRODUCT_") or ws.title.startswith("ARCH_"):
            if ws.max_row >= 2:
                for cell in ws[2]:
                    cell.fill = SUB_HEADER_FILL

    if OUTPUT_WORKBOOK.exists():
        OUTPUT_WORKBOOK.unlink()
    wb.save(OUTPUT_WORKBOOK)


if __name__ == "__main__":
    build_workbook()
    print(f"Wrote workbook: {OUTPUT_WORKBOOK}")
