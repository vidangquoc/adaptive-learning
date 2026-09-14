from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ROOT / "sources" / "destination-c1-c2" / "sections"
OUT_DIR = ROOT / "sources" / "destination-c1-c2" / "knowledge-atoms"
DISCOVERY = OUT_DIR / "discovery.jsonl"
REPORT = OUT_DIR / "discovery-report.json"
EXPECTED_SECTIONS = 177

POS = re.compile(r"\((?:n|v|adj|adv|prep|conj|pron|det|phr|num|nl|modal|aux|abbrev)(?:\s*,\s*(?:n|v|adj|adv|prep|conj|pron|det|phr|num|nl|modal|aux|abbrev))*\)", re.I)
EXACT_HEADINGS = {"grammar", "vocabulary", "phrasal verbs", "phrases, patterns and collocations", "idioms", "word formation", "review"}
TOPIC = re.compile(r"^topic\s+vocabulary\s*:\s*\S.+$", re.I)
PROGRESS = re.compile(r"^progress\s+test\b.*$", re.I)
MOJIBAKE = re.compile(r"[�]|(?:Ã.|Â.|â.)")
ALLOWED = {"word", "multiword_expression", "idiom", "phrasal_verb", "collocation", "fixed_expression", "grammar_rule", "grammar_pattern", "lexical_contrast", "word_formation", "usage_restriction", "meaning_distinction", "example_or_context", "unknown"}


def norm(line):
    return re.sub(r"\s+", " ", line.strip())


def structural_heading(line):
    text = norm(line)
    if text.casefold() in EXACT_HEADINGS or TOPIC.fullmatch(text) or PROGRESS.fullmatch(text):
        return text
    return None


def manifest():
    path = SECTIONS / "MANIFEST.tsv"
    if not path.exists():
        raise SystemExit("FAIL: missing sections/MANIFEST.tsv")
    rows = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if raw.strip():
            rows.append(dict(p.split("=", 1) for p in raw.split("\t") if "=" in p))
    return rows


def integer(value, name):
    try:
        return int(value)
    except (TypeError, ValueError):
        raise ValueError(f"invalid integer for {name}: {value!r}")


def validate_sections(rows):
    errors, warnings, blockers = [], [], []
    if len(rows) != EXPECTED_SECTIONS:
        errors.append(f"manifest row count: expected={EXPECTED_SECTIONS} actual={len(rows)}")
    seen = set()
    for row in rows:
        rel = row.get("file", "")
        path = ROOT / rel
        if rel in seen:
            errors.append(f"duplicate manifest file: {rel}")
        seen.add(rel)
        if not path.exists():
            errors.append(f"missing section file: {rel}")
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        expected = integer(row.get("line_count"), f"line_count:{rel}")
        if len(lines) != expected:
            errors.append(f"line count mismatch: {rel} expected={expected} actual={len(lines)}")
        if not lines:
            errors.append(f"empty section file: {rel}")
            continue
        own = row.get("heading", "").strip().casefold()
        for n, line in enumerate(lines[1:], 2):
            heading = structural_heading(line)
            if heading and heading.casefold() != own:
                blockers.append({"file": rel, "line": n, "reason": "internal_structural_heading", "text": heading})
        bad = sum(bool(MOJIBAKE.search(x)) for x in lines)
        if bad:
            warnings.append({"file": rel, "reason": "encoding_artifact", "line_count": bad})
    return errors, warnings, blockers


def candidate(row, start, form, atom_type, raw, basis):
    unit = integer(row["unit"], "unit")
    section = integer(row["section_index"], "section_index")
    return {
        "knowledge_atom_id": f"ka-destination-u{unit:02d}-s{section:02d}-l{start:04d}",
        "source_id": "destination-c1-c2",
        "source_type": "textbook",
        "source_location": {"unit": unit, "section_file": row["file"], "section_index": section, "line_start": start, "line_end": start},
        "section_type": row.get("kind", "unknown"),
        "section_name": row.get("section", "unknown"),
        "atom_type": atom_type,
        "canonical_form": re.sub(r"\s+", " ", form.strip(" \t|")),
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
        "evidence": [{"kind": "source_span", "source_id": "destination-c1-c2", "location": f"{row['file']}:{start}-{start}", "note": basis}],
        "relationships": [],
        "notes": "Candidate only; requires curation and evidence-backed enrichment before canonical use.",
    }


def discover_lexical(row, line_no, line):
    out = []
    chunks = [x.strip() for x in re.split(r"\s{2,}", line.strip()) if x.strip()]
    section = row.get("section", "")
    if len(chunks) > 1 and any(POS.search(x) for x in chunks):
        for chunk in chunks:
            match = POS.search(chunk)
            if not match:
                continue
            form = chunk[:match.start()].strip()
            if not form:
                continue
            typ = "word"
            if "idiom" in section:
                typ = "idiom"
            elif "phrasal" in section:
                typ = "phrasal_verb"
            elif "collocation" in section or "phrases-patterns" in section:
                typ = "collocation"
            elif "word-formation" in section:
                typ = "word_formation"
            out.append(candidate(row, line_no, form, typ, chunk, "lexical row with explicit POS marker"))
        return out
    if any(k in section for k in ("phrasal-verbs", "phrases-patterns", "idioms", "word-formation")):
        head = re.split(r"\s{2,}", line.strip(), maxsplit=1)[0].strip()
        if head:
            typ = "phrasal_verb" if "phrasal-verbs" in section else "idiom" if "idioms" in section else "collocation" if "phrases-patterns" in section else "word_formation"
            out.append(candidate(row, line_no, head, typ, line.strip(), "lexical row head from source layout"))
    return out


def discover(rows, blocked):
    out = []
    for row in rows:
        if row["file"] in blocked:
            continue
        lines = (ROOT / row["file"]).read_text(encoding="utf-8", errors="replace").splitlines()
        for n, line in enumerate(lines[1:], 2):
            if not line.strip() or structural_heading(line):
                continue
            if row.get("kind") == "lexical":
                out.extend(discover_lexical(row, n, line))
            elif row.get("kind") == "main" and "grammar" in row.get("section", "").casefold() and len(line.strip()) >= 20:
                text = re.sub(r"\s+", " ", line.strip())
                out.append(candidate(row, n, text[:120], "unknown", line, "conservative grammar source-row candidate"))
    return out


def validate_candidates(items, rows):
    errors, warnings, seen, forms = [], [], set(), Counter()
    row_map = {r["file"]: r for r in rows}
    for item in items:
        cid = item["knowledge_atom_id"]
        if cid in seen:
            errors.append(f"duplicate candidate id: {cid}")
        seen.add(cid)
        if item["atom_type"] not in ALLOWED:
            errors.append(f"unsupported atom_type: {cid} -> {item['atom_type']}")
        if "priority" in item:
            errors.append(f"intrinsic priority field is forbidden: {cid}")
        loc = item["source_location"]
        row = row_map.get(loc["section_file"])
        if not row:
            errors.append(f"unknown section file: {cid}")
            continue
        lines = (ROOT / loc["section_file"]).read_text(encoding="utf-8", errors="replace").splitlines()
        if not (1 <= loc["line_start"] <= loc["line_end"] <= len(lines)):
            errors.append(f"invalid source range: {cid}")
            continue
        expected = "\n".join(lines[loc["line_start"]-1:loc["line_end"]])
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
    print("Destination C1-C2 knowledge atom discovery")
    print("=" * 46)
    print("Loading validated section manifest...")
    rows = manifest()
    print("Validating source sections and scanning for internal-boundary anomalies...")
    section_errors, section_warnings, blockers = validate_sections(rows)
    blocked = {x["file"] for x in blockers}
    print(f"Sections in manifest: {len(rows)}")
    print(f"Blocked section files: {len(blocked)}")
    if blockers:
        print("Boundary blockers:")
        for b in blockers:
            print(f"  {b['file']}:{b['line']} [{b['reason']}] {b['text']}")
    items = discover(rows, blocked)
    candidate_errors, candidate_warnings = validate_candidates(items, rows)
    report = {"source": "Destination C1-C2", "expected_sections": EXPECTED_SECTIONS, "actual_sections": len(rows), "section_validation": {"errors": section_errors, "warnings": section_warnings, "blockers": blockers}, "candidate_validation": {"errors": candidate_errors, "warnings": candidate_warnings}, "candidate_count": len(items), "promotion_allowed": not section_errors and not blockers and not candidate_errors, "result": "PASS" if not section_errors and not blockers and not candidate_errors else "FAIL"}
    write(items, report)
    print(f"Candidate atoms discovered: {len(items)}")
    print(f"Section errors: {len(section_errors)}")
    print(f"Boundary blockers: {len(blockers)}")
    print(f"Candidate errors: {len(candidate_errors)}")
    print(f"Candidate warnings: {len(section_warnings) + len(candidate_warnings)}")
    if report["result"] == "PASS":
        print("PROMOTION GATE: PASS")
        print("RESULT: PASS")
    else:
        print("PROMOTION GATE: FAIL")
        print("No canonical knowledge-atom dataset is produced by this step.")
        print("RESULT: FAIL")


if __name__ == "__main__":
    main()
