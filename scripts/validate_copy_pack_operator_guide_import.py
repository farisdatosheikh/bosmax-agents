#!/usr/bin/env python3
"""
Validator: Static CopyPack Operator Guide (Notion import CSV)

Validates outputs/notion_import/COPY_PACK_OPERATOR_GUIDE_IMPORT_v1.csv against
the BOSMAX operator-safe metadata contract:

  1. CSV exists
  2. exactly 96 rows
  3. 30 BOSMAX_SERUM rows
  4. 66 CAP_BURUNG_MINYAK rows
  5. all required columns exist (17, in order)
  6. no Hook / USP / CTA columns exist
  7. no forbidden words in label / positioning fields
  8. every row has non-empty Guide Angle Label
  9. every row has non-empty Guide Operator Note
  10. Status populated for every row

Exit code 0 = PASS, 1 = FAIL. Prints a PASS/FAIL line per check plus a summary.
"""

import csv
import os
import re
import sys

CSV_PATH = os.path.join("outputs", "notion_import", "COPY_PACK_OPERATOR_GUIDE_IMPORT_v1.csv")

REQUIRED_COLUMNS = [
    "CopyPack ID", "Product Name", "Product ID", "Lane", "Formula", "Formula Meaning",
    "Guide Angle Label", "Guide Use Case", "Guide Best For", "Guide Tone", "Guide Claim Risk",
    "Guide Do", "Guide Do Not", "Guide Production Readiness", "Guide Operator Note",
    "Guide Compliance Note", "Status",
]

FORBIDDEN_COLUMN_PATTERNS = [
    r"\bhook\b", r"\busp\b", r"\bcta\b", r"\bsource[_ ]?node\b",
    r"\bsource[_ ]?script\b", r"\bauthority[_ ]?source\b", r"\bdisplay[_ ]?name\b",
    r"\bprompt[_ ]?fragment\b",
]

FORBIDDEN_WORDS = [
    "cure", "treat", "heal",
    "sex", "sexual", "penis", "erection", "orgasm", "intercourse",
    "piston", "aban", "penggera", "ego", "alpha",
]

# Scope of the forbidden-word scan (check 7): labels and positioning copy an
# operator reads as "the angle". Deliberately EXCLUDED: Guide Do, Guide Do Not,
# Guide Compliance Note — those fields exist to instruct operators what to
# avoid (e.g. "Do not say the product cures, treats, or heals ..."), so naming
# the forbidden concept there is the guardrail working as intended, not a leak.
LABEL_SCAN_COLUMNS = [
    "CopyPack ID", "Product Name", "Guide Angle Label", "Guide Use Case",
    "Guide Best For", "Guide Tone", "Guide Operator Note",
]


def load_csv():
    if not os.path.isfile(CSV_PATH):
        return None, None
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if not rows:
        return [], []
    return rows[0], rows[1:]


def print_results(results):
    for name, ok, detail in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name} -- {detail}")


def main():
    header, data = load_csv()
    results = []

    exists = header is not None
    results.append(("1. CSV exists", exists, CSV_PATH))
    if not exists:
        results.append(("2-10. (skipped)", False, "CSV file not found"))
        print_results(results)
        sys.exit(1)

    dict_rows = [dict(zip(header, row)) for row in data]

    n = len(data)
    results.append(("2. Exactly 96 data rows", n == 96, f"found {n}"))

    bos_n = sum(1 for r in dict_rows if r.get("CopyPack ID", "").startswith("BOSMAX_SERUM_CP_"))
    results.append(("3. 30 BOSMAX_SERUM_CP_* rows", bos_n == 30, f"found {bos_n}"))

    mwcb_n = sum(1 for r in dict_rows if r.get("CopyPack ID", "").startswith("CAP_BURUNG_MINYAK_CP_"))
    results.append(("4. 66 CAP_BURUNG_MINYAK_CP_* rows", mwcb_n == 66, f"found {mwcb_n}"))

    header_ok = (header == REQUIRED_COLUMNS)
    results.append(("5. Required 17 columns present & in order", header_ok,
                    "header matches contract" if header_ok else f"header={header}"))

    bad_cols = [c for c in header if any(re.search(p, c, re.IGNORECASE) for p in FORBIDDEN_COLUMN_PATTERNS)]
    results.append(("6. No Hook/USP/CTA/source columns", len(bad_cols) == 0,
                    "none found" if not bad_cols else f"forbidden columns found: {bad_cols}"))

    forbidden_hits = []
    word_res = [re.compile(r"\b" + re.escape(w) + r"\b", re.IGNORECASE) for w in FORBIDDEN_WORDS]
    for i, row in enumerate(dict_rows, start=2):
        for col in LABEL_SCAN_COLUMNS:
            val = row.get(col, "")
            if not val:
                continue
            for w, rx in zip(FORBIDDEN_WORDS, word_res):
                if rx.search(val):
                    forbidden_hits.append((i, col, w))
    results.append(("7. No forbidden words in label/positioning fields", len(forbidden_hits) == 0,
                    "clean" if not forbidden_hits else f"hits: {forbidden_hits[:10]}"))

    missing_label = [r["CopyPack ID"] for r in dict_rows if not r.get("Guide Angle Label", "").strip()]
    results.append(("8. Guide Angle Label non-empty for every row", len(missing_label) == 0,
                    "all populated" if not missing_label else f"missing: {missing_label}"))

    missing_note = [r["CopyPack ID"] for r in dict_rows if not r.get("Guide Operator Note", "").strip()]
    results.append(("9. Guide Operator Note non-empty for every row", len(missing_note) == 0,
                    "all populated" if not missing_note else f"missing: {missing_note}"))

    missing_status = [r["CopyPack ID"] for r in dict_rows if not r.get("Status", "").strip()]
    results.append(("10. Status populated for every row", len(missing_status) == 0,
                    "all populated" if not missing_status else f"missing: {missing_status}"))

    overall_pass = all(ok for _, ok, _ in results)
    print_results(results)
    print()
    print("OVERALL:", "PASS" if overall_pass else "FAIL")
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
