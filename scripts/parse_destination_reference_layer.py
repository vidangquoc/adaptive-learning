#!/usr/bin/env python3
"""Build a searchable reference layer from Destination C1-C2 reference sources.

This script intentionally does NOT create knowledge atoms. It preserves source evidence
and creates lookup-oriented derived records that later context-aware processing can use.

Fail-closed rules:
- missing source files are errors;
- existing outputs are never overwritten unless --force is supplied;
- records retain source path and source line numbers;
- uncertain lexical parsing is retained as raw evidence rather than guessed.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable

PARSER_VERSION = "reference-layer-v1"
ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "sources" / "destination-c1-c2"
OUT_ROOT = SOURCE_ROOT / "reference-layer"

SOURCES = [
    ("topic_vocabulary_database", SOURCE_ROOT / "appendix" / "appendix-01-topic-vocabulary-database.txt"),
    ("phrasal_verbs_database", SOURCE_ROOT / "appendix" / "appendix-02-phrasal-verbs-database.txt"),
    ("phrases_patterns_collocations_database", SOURCE_ROOT / "appendix" / "appendix-03-phrases-patterns-collocations-database.txt"),
    ("idioms_database", SOURCE_ROOT / "appendix" / "appendix-04-idioms-database.txt"),
    ("answer_key", SOURCE_ROOT / "back-matter" / "section-01-answer-key.txt"),
]

POS_RE = re.compile(r"\((?:n|v|adj|adv|prep|conj|pron|det|phr|modal|aux|n phr|adj phr|adv phr)(?:,\s*(?:n|v|adj|adv|prep|conj|pron|det|phr))*\)", re.I)
HEAD_RE = re.compile(r"^\s*([A-Za-z][A-Za-z'’./-]*(?:\s+[A-Za-z][A-Za-z'’./-]*){0,8})\s+(\([^)]{1,40}\))\s+(.*)$")


def norm(text: str) -> str:
    text = text.lower().replace("’", "'")
    return re.sub(r"\s+", " ", text).strip()


def fail_if_outputs_exist(paths: Iterable[Path], force: bool) -> None:
    if force:
        return
    existing = [str(p) for p in paths if p.exists()]
    if existing:
        raise SystemExit("Refusing to overwrite existing outputs:\n" + "\n".join(existing) + "\nUse --force only after inspecting them.")


def read_source(source_type: str, path: Path) -> list[str]:
    if not path.exists():
        raise SystemExit(f"Missing required reference source: {path}")
    return path.read_text(encoding="utf-8").splitlines()


def lexical_records(source_type: str, path: Path, lines: list[str]) -> tuple[list[dict], int]:
    records: list[dict] = []
    uncertain = 0
    for line_no, raw in enumerate(lines, 1):
        if not raw.strip():
            continue
        # Keep the entire source line as immutable evidence. Also inspect each side of
        # the common two-column layout separately so both glossary columns are searchable.
        fragments = [raw]
        if len(raw) >= 70:
            fragments.extend([raw[:78], raw[78:]])
        for fragment in fragments:
            m = HEAD_RE.match(fragment)
            if not m or not POS_RE.search(m.group(2)):
                continue
            headword = m.group(1).strip()
            definition = m.group(3).strip()
            if not definition:
                uncertain += 1
            records.append({
                "reference_id": f"{source_type}:{line_no}:{len(records)+1}",
                "source_id": "destination-c1-c2",
                "source_path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "source_type": source_type,
                "source_location": f"line {line_no}",
                "source_text": fragment.strip(),
                "parsed_fields": {
                    "headword": headword,
                    "headword_normalized": norm(headword),
                    "part_of_speech": m.group(2).strip("()"),
                    "definition_raw": definition or None,
                },
                "parser_version": PARSER_VERSION,
            })
    return records, uncertain


def line_records(source_type: str, path: Path, lines: list[str]) -> list[dict]:
    records = []
    for line_no, raw in enumerate(lines, 1):
        if not raw.strip():
            continue
        records.append({
            "reference_id": f"{source_type}:line:{line_no}",
            "source_id": "destination-c1-c2",
            "source_path": str(path.relative_to(ROOT)).replace("\\", "/"),
            "source_type": source_type,
            "source_location": f"line {line_no}",
            "source_text": raw,
            "parsed_fields": {},
            "parser_version": PARSER_VERSION,
        })
    return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    records_path = OUT_ROOT / "reference-records.jsonl"
    lookup_path = OUT_ROOT / "reference-lookup.json"
    report_path = OUT_ROOT / "reference-layer-report.json"
    fail_if_outputs_exist([records_path, lookup_path, report_path], args.force)

    all_records: list[dict] = []
    lookup: dict[str, list[str]] = {}
    source_report = []

    for source_type, path in SOURCES:
        lines = read_source(source_type, path)
        if source_type == "answer_key":
            records = line_records(source_type, path, lines)
            uncertain = 0
        else:
            records, uncertain = lexical_records(source_type, path, lines)
        all_records.extend(records)
        for record in records:
            fields = record["parsed_fields"]
            key = fields.get("headword_normalized")
            if key:
                lookup.setdefault(key, []).append(record["reference_id"])
        source_report.append({
            "source_type": source_type,
            "source_path": str(path.relative_to(ROOT)).replace("\\", "/"),
            "line_count": len(lines),
            "record_count": len(records),
            "uncertain_records": uncertain,
        })

    with records_path.open("w", encoding="utf-8", newline="\n") as f:
        for record in all_records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    lookup_path.write_text(json.dumps(lookup, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report = {
        "parser_version": PARSER_VERSION,
        "source_count": len(SOURCES),
        "record_count": len(all_records),
        "lookup_key_count": len(lookup),
        "sources": source_report,
        "result": "PASS",
        "note": "Reference records are evidence/lookup data, not verified knowledge atoms.",
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Destination C1-C2 reference layer ({PARSER_VERSION})")
    print("=" * 52)
    print(f"Sources: {len(SOURCES)}")
    print(f"Reference records: {len(all_records)}")
    print(f"Lookup keys: {len(lookup)}")
    for item in source_report:
        print(f"  {item['source_type']}: {item['record_count']} records")
    print(f"REPORT: {report_path.relative_to(ROOT)}")
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
