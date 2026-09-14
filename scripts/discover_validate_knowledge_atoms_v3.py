from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ROOT / "sources" / "destination-c1-c2" / "sections"
OUT_DIR = ROOT / "sources" / "destination-c1-c2" / "knowledge-atoms"
DISCOVERY = OUT_DIR / "discovery-v3.jsonl"
REPORT = OUT_DIR / "discovery-v3-report.json"
EXPECTED_SECTIONS = 177

POS = re.compile(r"\((?:n|v|adj|adv|prep|conj|pron|det|phr|num|nl|modal|aux|abbrev)(?:\s*,\s*(?:n|v|adj|adv|prep|conj|pron|det|phr|num|nl|modal|aux|abbrev))*\)", re.I)
BULLET_WORDS = re.compile(r"(?:^|\s)[A-Za-z][A-Za-z'/-]*(?:\s*•\s*[A-Za-z][A-Za-z'/-]*){2,}")
OPTION_PAIR = re.compile(r"\b[A-Za-z][A-Za-z'/-]*/\s*[A-Za-z][A-Za-z'/-]*\b")
FILL_BLANK = re.compile(r"\.{3,}|_{3,}")
EXERCISE_START = re.compile(r"^\s*(?:[A-Z](?:\s|$)|\d+[.)]\s+)")

ALLOWED = {"word", "multiword_expression", "idiom", "phrasal_verb", "collocation", "word_formation"}


def norm(line: str) -> str:
    return re.sub(r"\s+", " ", line.strip())


def manifest():
    path = SECTIONS / "MANIFEST.tsv"
    if not path.exists():
        raise SystemExit("FAIL: missing sections/MANIFEST.tsv")
    rows = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if raw.strip():
            rows.append(dict(p.split("=", 1) for p in raw.split("\t") if "=" in p))
    return rows


def candidate_id(row, line_no, ordinal):
    return f"ka-destination-u{int(row['unit']):02d}-s{int(row['section_index']):02d}-l{line_no:04d}-c{ordinal:02d}"


def atom_type(row, form: str) -> str:
    section = row.get("section", "").casefold()
    if "idiom" in section:
        return "idiom"
    if "phrasal-verbs" in section:
        return "phrasal_verb"
    if "phrases-patterns-collocations" in section:
        return "collocation"
    if "word-formation" in section:
        return "word_formation"
    return "word" if len(form.split()) == 1 else "multiword_expression"


def make_candidate(row, line_no, form, raw, evidence_kind, note, ordinal=1):
    form = norm(form).strip("|•- ")
    if not form:
        return None
    return {
        "knowledge_atom_id": candidate_id(row, line_no, ordinal),
        "source_id": "destination-c1-c2",
        "source_type": "textbook",
        "source_location": {"unit": int(row["unit"]), "section_file": row["file"], "section_index": int(row["section_index"]), "line_start": line_no, "line_end": line_no},
        "section_type": row.get("kind", "unknown"),
        "section_name": row.get("section", "unknown"),
        "atom_type": atom_type(row, form),
        "canonical_form": form,
        "content": raw,
        "definition": None,
        "meaning_vi": None,
        "pronunciation": None,
        "patterns": [],
        "usage_note": None,
        "examples": [],
        "cefr": None,
        "cefr_status": "pending",
        "domain": None,
        "confidence": "pending",
        "content_status": "source_candidate",
        "provenance_status": "complete",
        "evidence": [{"kind": evidence_kind, "source_id": "destination-c1-c2", "location": f"{row['file']}:{line_no}-{line_no}", "note": note}],
        "relationships": [],
        "notes": "Candidate only; no semantic enrichment or intrinsic priority assigned.",
    }


def split_pos_row(row, line_no, line):
    out = []
    chunks = [x.strip() for x in re.split(r"\s{2,}", line.strip()) if x.strip()]
    ordinal = 0
    for chunk in chunks:
        match = POS.search(chunk)
        if not match:
            continue
        form = chunk[:match.start()].strip()
        if not form:
            continue
        ordinal += 1
        item = make_candidate(row, line_no, form, chunk, "explicit_pos_row", "lexical entry explicitly marked with part-of-speech notation", ordinal)
        if item:
            out.append(item)
    return out


def split_word_box(row, line_no, line):
    if not BULLET_WORDS.search(line):
        return []
    parts = [x.strip() for x in line.split("•") if x.strip()]
    out = []
    for ordinal, form in enumerate(parts, 1):
        if not re.fullmatch(r"[A-Za-z][A-Za-z'/-]*", form):
            continue
        item = make_candidate(row, line_no, form, line, "explicit_word_box", "lexical word-box entry; no answer inference", ordinal)
        if item:
            out.append(item)
    return out


def lexical_head(row, line_no, line):
    section = row.get("section", "").casefold()
    if not any(x in section for x in ("phrasal-verbs", "phrases-patterns-collocations", "idioms", "word-formation")):
        return []
    if FILL_BLANK.search(line) or OPTION_PAIR.search(line) or EXERCISE_START.match(line):
        return []
    text = norm(line)
    if not text or len(text) > 220:
        return []
    chunks = [x.strip() for x in re.split(r"\s{2,}", text) if x.strip()]
    if not chunks:
        return []
    head = chunks[0]
    if not re.fullmatch(r"[A-Za-z][A-Za-z'/-]*(?:\s+[A-Za-z][A-Za-z'/-]*){0,6}", head):
        return []
    if head.casefold() in {"phrases", "patterns", "collocations", "idioms", "word formation", "phrasal verbs"}:
        return []
    typ = "phrasal_verb" if "phrasal-verbs" in section else "idiom" if "idioms" in section else "collocation" if "phrases-patterns" in section else "word_formation"
    item = make_candidate(row, line_no, head, line, "lexical_table_head", f"conservative headword extracted from {typ} source layout")
    if item:
        item["atom_type"] = typ
        return [item]
    return []


def discover(rows):
    items = []
    counters = Counter()
    for row in rows:
        lines = (ROOT / row["file"]).read_text(encoding="utf-8", errors="replace").splitlines()
        for line_no, line in enumerate(lines[1:], 2):
            if not line.strip():
                continue
            found = split_pos_row(row, line_no, line)
            if not found:
                found = split_word_box(row, line_no, line)
            if not found:
                found = lexical_head(row, line_no, line)
            for item in found:
                items.append(item)
                counters[item["evidence"][0]["kind"]] += 1
    return items, counters


def validate_candidates(items, rows):
    errors, warnings = [], []
    row_map = {r["file"]: r for r in rows}
    seen_ids, forms = set(), Counter()
    for item in items:
        cid = item["knowledge_atom_id"]
        if cid in seen_ids:
            errors.append(f"duplicate candidate id: {cid}")
        seen_ids.add(cid)
        if item["atom_type"] not in ALLOWED:
            errors.append(f"unsupported atom_type: {cid} -> {item['atom_type']}")
        if "priority" in item:
            errors.append(f"intrinsic priority field is forbidden: {cid}")
        loc = item["source_location"]
        if loc["section_file"] not in row_map:
            errors.append(f"unknown section file: {cid}")
            continue
        lines = (ROOT / loc["section_file"]).read_text(encoding="utf-8", errors="replace").splitlines()
        if not (1 <= loc["line_start"] <= loc["line_end"] <= len(lines)):
            errors.append(f"invalid source range: {cid}")
            continue
        if item["evidence"][0]["kind"] != "explicit_pos_row":
            expected = "\n".join(lines[loc["line_start"] - 1:loc["line_end"]])
            if item["content"] != expected:
                errors.append(f"source span mismatch: {cid}")
        forms[item["canonical_form"].casefold()] += 1
    warnings.extend({"reason": "duplicate_candidate_form", "canonical_form": f, "count": n} for f, n in forms.items() if f and n > 1)
    return errors, warnings


def write(items, report):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    DISCOVERY.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in items), encoding="utf-8", newline="\n")
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def main():
    print("Destination C1-C2 knowledge atom discovery v3")
    print("=" * 50)
    rows = manifest()
    print("Validating section inventory...")
    if len(rows) != EXPECTED_SECTIONS:
        print(f"Section inventory: FAIL ({len(rows)}/{EXPECTED_SECTIONS})")
        raise SystemExit(1)
    print(f"Sections in manifest: {len(rows)}")
    print("Extracting evidence-specific lexical candidates...")
    items, counters = discover(rows)
    errors, warnings = validate_candidates(items, rows)
    report = {
        "source": "Destination C1-C2", "version": 3,
        "expected_sections": EXPECTED_SECTIONS, "actual_sections": len(rows),
        "candidate_count": len(items), "evidence_counts": dict(sorted(counters.items())),
        "candidate_validation": {"errors": errors, "warnings": warnings},
        "excluded_as_non_atom_evidence": {
            "option_pairs": "exercise signal; not promoted to knowledge atoms",
            "fill_blanks": "exercise signal; not promoted to knowledge atoms",
            "exercise_markers": "exercise signal; not promoted to knowledge atoms",
        },
        "promotion_allowed": not errors, "result": "PASS" if not errors else "FAIL",
    }
    write(items, report)
    print(f"Candidate atoms discovered: {len(items)}")
    for key, value in sorted(counters.items()):
        print(f"  {key}: {value}")
    print(f"Candidate errors: {len(errors)}")
    print(f"Candidate warnings: {len(warnings)}")
    print("PROMOTION GATE: " + ("PASS" if not errors else "FAIL"))
    print("RESULT: " + ("PASS" if not errors else "FAIL"))


if __name__ == "__main__":
    main()
