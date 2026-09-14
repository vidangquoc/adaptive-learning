from __future__ import annotations

import json
import re
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ROOT / "sources" / "destination-c1-c2" / "sections"
OUT_DIR = ROOT / "sources" / "destination-c1-c2" / "knowledge-atoms"
DISCOVERY = OUT_DIR / "discovery.jsonl"
REPORT = OUT_DIR / "discovery-report.json"
SCHEMA = ROOT / "schemas" / "knowledge-atom.schema.json"

EXPECTED_SECTION_COUNT = 177
POS_MARKER = re.compile(r"\((?:n|v|adj|adv|prep|conj|pron|det|phr|num|nl|modal|aux|abbrev)(?:\s*,\s*(?:n|v|adj|adv|prep|conj|pron|det|phr|num|nl|modal|aux|abbrev))*\)", re.I)
INTERNAL_HEADING = re.compile(
    r"^\s*(?:Grammar|Vocabulary|Phrasal\\?s? verbs|Phrases,? patterns and collocations|Idioms|Word formation|Review|Progress test\\b|Topic vocabulary\\s*:)",
    re.I,
)
MOJIBAKE = re.compile(r"[�]|(?:Ã.|Â.|â.)")

ALLOWED_ATOM_TYPES = {
    "word",
    "multiword_expression",
    "idiom",
    "phrasal_verb",
    "collocation",
    "fixed_expression",
    "grammar_rule",
    "grammar_pattern",
    "lexical_contrast",
    "word_formation",
    "usage_restriction",
    "meaning_distinction",
    "example_or_context",
    "unknown",
}


def load_manifest():
    manifest = SECTIONS / "MANIFEST.tsv"
    if not manifest.exists():
        raise SystemExit("FAIL: missing sections/MANIFEST.tsv")
    rows = []
    for raw in manifest.read_text(encoding="utf-8", errors="replace").splitlines():
        if not raw.strip():
            continue
        fields = dict(part.split("=", 1) for part in raw.split("\t") if "=" in part)
        rows.append(fields)
    return rows


def as_int(value, label):
    try:
        return int(value)
    except (TypeError, ValueError):
        raise ValueError(f"invalid integer for {label}: {value!r}")


def validate_sections(rows):
    errors = []
    warnings = []
    seen_files = set()
    blockers = []

    if len(rows) != EXPECTED_SECTION_COUNT:
        errors.append(f"manifest row count: expected={EXPECTED_SECTION_COUNT} actual={len(rows)}")

    for row in rows:
        file_rel = row.get("file", "")
        section_file = ROOT / file_rel
        if file_rel in seen_files:
            errors.append(f"duplicate manifest file: {file_rel}")
        seen_files.add(file_rel)

        if not section_file.exists():
            errors.append(f"missing section file: {file_rel}")
            continue

        lines = section_file.read_text(encoding="utf-8", errors="replace").splitlines()
        expected_count = as_int(row.get("line_count"), f"line_count:{file_rel}")
        if len(lines) != expected_count:
            errors.append(f"line count mismatch: {file_rel} expected={expected_count} actual={len(lines)}")

        if not lines:
            errors.append(f"empty section file: {file_rel}")
            continue

        if row.get("heading") and row["heading"].strip() and row.get("section"):
            pass

        # A section may be structurally valid but semantically contaminated by a
        # second heading that the PDF extractor failed to classify. Treat that as
        # a blocker for automatic atom promotion.
        internal = []
        for line_no, line in enumerate(lines[1:], start=2):
            normalized = re.sub(r"\s+", " ", line.strip())
            if INTERNAL_HEADING.match(normalized):
                internal.append((line_no, normalized))

        if internal:
            for line_no, text in internal:
                blockers.append({
                    "file": file_rel,
                    "line": line_no,
                    "reason": "internal_heading",
                    "text": text,
                })

        mojibake_count = sum(1 for line in lines if MOJIBAKE.search(line))
        if mojibake_count:
            warnings.append({
                "file": file_rel,
                "reason": "encoding_artifact",
                "line_count": mojibake_count,
            })

    return errors, warnings, blockers


def clean_candidate(text):
    return re.sub(r"\s+", " ", text.strip(" \t|"))


def candidate_from_span(row, line_start, line_end, form, atom_type, raw_span, basis):
    unit = as_int(row.get("unit"), "unit")
    section_index = as_int(row.get("section_index"), "section_index")
    atom_id = f"ka-destination-u{unit:02d}-s{section_index:02d}-l{line_start:04d}"
    return {
        "knowledge_atom_id": atom_id,
        "source_id": "destination-c1-c2",
        "source_type": "textbook",
        "source_location": {
            "unit": unit,
            "section_file": row["file"],
            "section_index": section_index,
            "line_start": line_start,
            "line_end": line_end,
        },
        "section_type": row.get("kind", "unknown"),
        "section_name": row.get("section", "unknown"),
        "atom_type": atom_type,
        "canonical_form": clean_candidate(form),
        "content": raw_span,
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
        "evidence": [{
            "kind": "source_span",
            "source_id": "destination-c1-c2",
            "location": f"{row['file']}:{line_start}-{line_end}",
            "note": basis,
        }],
        "relationships": [],
        "notes": "Candidate only; requires curation and evidence-backed enrichment before canonical use.",
    }


def discover_lexical_row(row, line_no, line):
    candidates = []
    # Table-like vocabulary lines often contain multiple entries separated by
    # wide whitespace. Split only when the resulting chunk contains a POS marker;
    # otherwise preserve the whole row as one pending candidate.
    chunks = [clean_candidate(x) for x in re.split(r"\s{2,}", line.strip()) if clean_candidate(x)]
    if len(chunks) > 1 and any(POS_MARKER.search(chunk) for chunk in chunks):
        for chunk in chunks:
            match = POS_MARKER.search(chunk)
            if not match:
                continue
            form = chunk[: match.start()].strip()
            if not form:
                continue
            atom_type = "word"
            section = row.get("section", "")
            if "idiom" in section:
                atom_type = "idiom"
            elif "phrasal" in section:
                atom_type = "phrasal_verb"
            elif "collocation" in section or "phrases-patterns" in section:
                atom_type = "collocation"
            elif "word-formation" in section:
                atom_type = "word_formation"
            candidates.append(candidate_from_span(
                row, line_no, line_no, form, atom_type, chunk,
                "table-like lexical row with explicit POS marker",
            ))
        return candidates

    # Phrasal verbs, collocations, idioms and word-formation entries frequently
    # have a head followed by a definition/pattern after wide whitespace.
    section = row.get("section", "")
    if any(key in section for key in ("phrasal-verbs", "phrases-patterns", "idioms", "word-formation")):
        parts = re.split(r"\s{2,}", line.strip(), maxsplit=1)
        if parts and parts[0].strip():
            atom_type = (
                "phrasal_verb" if "phrasal-verbs" in section else
                "idiom" if "idioms" in section else
                "collocation" if "phrases-patterns" in section else
                "word_formation"
            )
            candidates.append(candidate_from_span(
                row, line_no, line_no, parts[0], atom_type, line.strip(),
                "lexical row head detected from source layout",
            ))
    return candidates


def discover_rows(rows, blockers_by_file):
    candidates = []
    blocked_files = set(blockers_by_file)

    for row in rows:
        file_rel = row["file"]
        if file_rel in blocked_files:
            continue
        path = ROOT / file_rel
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        section = row.get("section", "")

        for line_no, line in enumerate(lines[1:], start=2):
            if not line.strip():
                continue
            if INTERNAL_HEADING.match(re.sub(r"\s+", " ", line.strip())):
                continue

            if row.get("kind") == "lexical":
                candidates.extend(discover_lexical_row(row, line_no, line))
            elif row.get("kind") == "main" and "grammar" in section.casefold():
                # Grammar discovery stays conservative: one non-empty source row
                # becomes a pending rule/pattern candidate rather than inventing
                # semantic boundaries.
                text = clean_candidate(line)
                if len(text) >= 20:
                    candidates.append(candidate_from_span(
                        row, line_no, line_no, text[:120], "unknown", line,
                        "conservative grammar source-row candidate",
                    ))

    return candidates


def validate_candidates(candidates, rows):
    errors = []
    warnings = []
    row_by_file = {row["file"]: row for row in rows}
    seen_ids = set()
    duplicate_forms = Counter()

    for candidate in candidates:
        cid = candidate["knowledge_atom_id"]
        if cid in seen_ids:
            errors.append(f"duplicate candidate id: {cid}")
        seen_ids.add(cid)

        if candidate["atom_type"] not in ALLOWED_ATOM_TYPES:
            errors.append(f"unsupported atom_type: {cid} -> {candidate['atom_type']}")

        if "priority" in candidate:
            errors.append(f"intrinsic priority field is forbidden: {cid}")

        loc = candidate["source_location"]
        row = row_by_file.get(loc["section_file"])
        if row is None:
            errors.append(f"unknown section file: {cid} -> {loc['section_file']}")
            continue

        path = ROOT / loc["section_file"]
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        if loc["line_start"] < 1 or loc["line_end"] > len(lines) or loc["line_start"] > loc["line_end"]:
            errors.append(f"invalid source range: {cid}")
            continue

        expected = "\n".join(lines[loc["line_start"] - 1:loc["line_end"]])
        if candidate["content"] != expected:
            errors.append(f"source span mismatch: {cid}")

        duplicate_forms[candidate["canonical_form"].casefold()] += 1

    for form, count in duplicate_forms.items():
        if count > 1 and form:
            warnings.append({"reason": "duplicate_candidate_form", "canonical_form": form, "count": count})

    return errors, warnings


def write_outputs(candidates, report):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with DISCOVERY.open("w", encoding="utf-8", newline="\n") as handle:
        for candidate in candidates:
            handle.write(json.dumps(candidate, ensure_ascii=False, sort_keys=True) + "\n")
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def main():
    print("Destination C1-C2 knowledge atom discovery")
    print("=" * 46)
    print("Loading validated section manifest...")
    rows = load_manifest()

    print("Validating source sections and scanning for internal-boundary anomalies...")
    section_errors, section_warnings, blockers = validate_sections(rows)
    blockers_by_file = {item["file"] for item in blockers}

    print(f"Sections in manifest: {len(rows)}")
    print(f"Blocked section files: {len(blockers_by_file)}")

    candidates = discover_rows(rows, blockers_by_file)
    candidate_errors, candidate_warnings = validate_candidates(candidates, rows)

    report = {
        "source": "Destination C1-C2",
        "expected_sections": EXPECTED_SECTION_COUNT,
        "actual_sections": len(rows),
        "section_validation": {
            "errors": section_errors,
            "warnings": section_warnings,
            "blockers": blockers,
        },
        "candidate_validation": {
            "errors": candidate_errors,
            "warnings": candidate_warnings,
        },
        "candidate_count": len(candidates),
        "promotion_allowed": not section_errors and not blockers and not candidate_errors,
        "result": "PASS" if not section_errors and not blockers and not candidate_errors else "FAIL",
    }

    write_outputs(candidates, report)

    print(f"Candidate atoms discovered: {len(candidates)}")
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
