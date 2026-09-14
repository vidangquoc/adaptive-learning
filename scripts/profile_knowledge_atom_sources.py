from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ROOT / "sources" / "destination-c1-c2" / "sections"
OUT_DIR = ROOT / "sources" / "destination-c1-c2" / "knowledge-atoms"
REPORT = OUT_DIR / "source-profile.json"
EXPECTED_SECTIONS = 177

POS = re.compile(r"\((?:n|v|adj|adv|prep|conj|pron|det|phr|num|nl|modal|aux|abbrev)(?:\s*,\s*(?:n|v|adj|adv|prep|conj|pron|det|phr|num|nl|modal|aux|abbrev))*\)", re.I)
WORD_BOX = re.compile(r"(?:^|\n)\s*[A-Za-z][A-Za-z'/-]*(?:\s*•\s*[A-Za-z][A-Za-z'/-]*){2,}")
OPTION_PAIR = re.compile(r"\b[A-Za-z][A-Za-z'/-]*/\s*[A-Za-z][A-Za-z'/-]*\b")
FILL_BLANK = re.compile(r"\.{3,}|_{3,}")
LEXICAL_SECTION = re.compile(r"(?:phrasal-verbs|phrases-patterns-collocations|idioms|word-formation|topic-vocabulary)", re.I)
EXERCISE = re.compile(r"^\s*[A-Z](?:\s|$)|^\s*\d+[.)]\s+", re.I)


def manifest():
    path = SECTIONS / "MANIFEST.tsv"
    rows = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if raw.strip():
            rows.append(dict(p.split("=", 1) for p in raw.split("\t") if "=" in p))
    return rows


def norm(line: str) -> str:
    return re.sub(r"\s+", " ", line.strip())


def profile_section(row):
    path = ROOT / row["file"]
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    nonempty = [x for x in lines[1:] if x.strip()]
    pos_lines = [norm(x) for x in nonempty if POS.search(x)]
    word_box_lines = [norm(x) for x in nonempty if WORD_BOX.search(x)]
    option_lines = [norm(x) for x in nonempty if OPTION_PAIR.search(x)]
    blank_lines = [norm(x) for x in nonempty if FILL_BLANK.search(x)]
    exercise_lines = [norm(x) for x in nonempty if EXERCISE.search(x)]
    return {
        "file": row["file"],
        "unit": int(row["unit"]),
        "section_index": int(row["section_index"]),
        "section": row.get("section", ""),
        "heading": row.get("heading", ""),
        "line_count": len(lines),
        "nonempty_lines": len(nonempty),
        "has_pos_rows": bool(pos_lines),
        "pos_row_count": len(pos_lines),
        "pos_samples": pos_lines[:3],
        "has_word_box": bool(word_box_lines),
        "word_box_count": len(word_box_lines),
        "word_box_samples": word_box_lines[:3],
        "option_pair_count": len(option_lines),
        "option_pair_samples": option_lines[:5],
        "fill_blank_count": len(blank_lines),
        "fill_blank_samples": blank_lines[:3],
        "exercise_marker_count": len(exercise_lines),
        "lexical_section": bool(LEXICAL_SECTION.search(row.get("section", ""))),
    }


def main():
    rows = manifest()
    if len(rows) != EXPECTED_SECTIONS:
        raise SystemExit(f"FAIL: expected {EXPECTED_SECTIONS} sections, found {len(rows)}")

    profiles = [profile_section(row) for row in rows]
    totals = {
        "sections": len(profiles),
        "sections_with_pos_rows": sum(x["has_pos_rows"] for x in profiles),
        "sections_with_word_boxes": sum(x["has_word_box"] for x in profiles),
        "sections_with_option_pairs": sum(x["option_pair_count"] > 0 for x in profiles),
        "sections_with_fill_blanks": sum(x["fill_blank_count"] > 0 for x in profiles),
        "sections_with_exercise_markers": sum(x["exercise_marker_count"] > 0 for x in profiles),
        "lexical_sections": sum(x["lexical_section"] for x in profiles),
        "pos_rows": sum(x["pos_row_count"] for x in profiles),
        "word_box_rows": sum(x["word_box_count"] for x in profiles),
        "option_pairs": sum(x["option_pair_count"] for x in profiles),
        "fill_blank_rows": sum(x["fill_blank_count"] for x in profiles),
        "exercise_markers": sum(x["exercise_marker_count"] for x in profiles),
    }

    report = {
        "source": "Destination C1-C2",
        "expected_sections": EXPECTED_SECTIONS,
        "actual_sections": len(profiles),
        "totals": totals,
        "profiles": profiles,
        "next_step": "Use this profile to design evidence-specific candidate extractors; do not promote directly to canonical knowledge atoms.",
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")

    print("Destination C1-C2 knowledge-source profiling")
    print("=" * 46)
    print(f"Sections profiled: {len(profiles)}")
    for key, value in totals.items():
        if key != "sections":
            print(f"{key}: {value}")
    print(f"REPORT: {REPORT.relative_to(ROOT)}")
    print("RESULT: PASS")


if __name__ == "__main__":
    main()
