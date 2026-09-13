from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "sources" / "destination-c1-c2" / "raw" / "Destination_C1-C2.txt"
OUTPUT = ROOT / "sources" / "destination-c1-c2" / "units"
APPENDIX_OUTPUT = ROOT / "sources" / "destination-c1-c2" / "appendix"
BACK_MATTER_OUTPUT = ROOT / "sources" / "destination-c1-c2" / "back-matter"

EXPECTED_UNIT_COUNT = 26
CONTENT_START_LINE = 300

UNIT_PATTERN = re.compile(r"^\s*Unit\s+(\d+)\s+(Grammar|Vocabulary)\b.*$", re.IGNORECASE)
UNIT_11_ARTIFACT_PATTERN = re.compile(r"^\s*Unit\s+1\s+1\s+Grammar\b.*$", re.IGNORECASE)

# In this PDF, the lexical reference layer is not labelled "Appendix".
# It begins with these database headings after Unit 26.
LEXICAL_DATABASE_PATTERNS = [
    ("topic-vocabulary-database", re.compile(r"^\s*Topic vocabulary database\s*$", re.IGNORECASE)),
    ("phrasal-verbs-database", re.compile(r"^\s*Phrasal verbs database\s*$", re.IGNORECASE)),
    ("phrases-patterns-collocations-database", re.compile(r"^\s*Phrases, patterns and collocations database\s*$", re.IGNORECASE)),
    ("idioms-database", re.compile(r"^\s*Idioms database\s*$", re.IGNORECASE)),
]

APPENDIX_PATTERN = re.compile(r"^\s*Appendix(?:\s+.*)?$", re.IGNORECASE)
BACK_MATTER_PATTERNS = [
    re.compile(r"^\s*Answer\s+Keys?(?:\s+.*)?$", re.IGNORECASE),
    re.compile(r"^\s*Audioscript(?:s)?(?:\s+.*)?$", re.IGNORECASE),
    re.compile(r"^\s*Audio\s+Scripts?(?:\s+.*)?$", re.IGNORECASE),
    re.compile(r"^\s*References?(?:\s+.*)?$", re.IGNORECASE),
    re.compile(r"^\s*Word\s+List(?:s)?(?:\s+.*)?$", re.IGNORECASE),
]


def classify_structural_heading(line):
    for name, pattern in LEXICAL_DATABASE_PATTERNS:
        if pattern.match(line):
            return "appendix", name
    if APPENDIX_PATTERN.match(line):
        return "appendix", "appendix"
    for pattern in BACK_MATTER_PATTERNS:
        if pattern.match(line):
            return "back_matter", line.strip().lower().replace(" ", "-")
    return None


def discover_candidates(lines):
    candidates = []
    for index, line in enumerate(lines):
        if index < CONTENT_START_LINE:
            continue
        if UNIT_11_ARTIFACT_PATTERN.match(line):
            candidates.append({"line_index": index, "unit_number": 11, "heading": line.strip(), "kind": "known_pdf_artifact"})
            continue
        match = UNIT_PATTERN.match(line)
        if match:
            candidates.append({"line_index": index, "unit_number": int(match.group(1)), "heading": line.strip(), "kind": "normal"})
    return candidates


def discover_post_unit_sections(lines, last_unit_start):
    sections = []
    for index in range(last_unit_start + 1, len(lines)):
        line = lines[index].strip()
        if not line:
            continue
        classified = classify_structural_heading(line)
        if classified:
            kind, name = classified
            sections.append({"line_index": index, "heading": line, "kind": kind, "name": name})

    # Page headers repeat. Keep the first occurrence of each structural heading.
    selected = []
    seen = set()
    for section in sections:
        key = section["name"].casefold()
        if key in seen:
            continue
        seen.add(key)
        selected.append(section)
    return selected


def build_unit_plan(candidates):
    errors = []
    warnings = []
    selected = []
    seen = set()

    for candidate in candidates:
        number = candidate["unit_number"]
        if number in seen:
            continue
        seen.add(number)
        selected.append(candidate)

    expected = list(range(1, EXPECTED_UNIT_COUNT + 1))
    detected = [item["unit_number"] for item in selected]

    if sorted(detected) != expected:
        missing = sorted(set(expected) - set(detected))
        extra = sorted(set(detected) - set(expected))
        if missing:
            errors.append(f"Missing Unit numbers: {missing}")
        if extra:
            errors.append(f"Unexpected Unit numbers: {extra}")

    if detected != expected:
        errors.append(f"Unit sequence in RAW source is not 1..26 after normalization: {detected}")

    positions = [item["line_index"] for item in selected]
    if positions != sorted(positions):
        errors.append("Extraction boundaries are not in RAW source order.")

    if errors:
        return None, errors, warnings
    return selected, errors, warnings


def build_section_plan(lines, selected_units):
    errors = []
    warnings = []
    last_unit = selected_units[-1]
    post_unit = discover_post_unit_sections(lines, last_unit["line_index"])

    if not post_unit:
        errors.append(
            f"No Appendix, lexical database, or recognized back-matter heading was found after Unit {last_unit['unit_number']}. "
            "Refusing to let the final Unit consume the rest of the document."
        )
        return None, errors, warnings

    # The first validated post-unit section terminates Unit 26.
    unit_plan = []
    for i, unit in enumerate(selected_units):
        start = unit["line_index"]
        end = selected_units[i + 1]["line_index"] if i + 1 < len(selected_units) else post_unit[0]["line_index"]
        line_count = end - start
        unit_plan.append({**unit, "start_line": start, "end_line": end, "line_count": line_count})
        if line_count <= 1:
            errors.append(f"Unit {unit['unit_number']} has no meaningful content between lines {start + 1} and {end}.")
        if line_count < 50:
            warnings.append(f"Unit {unit['unit_number']} is unusually short: {line_count} lines.")

    section_plan = []
    for i, section in enumerate(post_unit):
        start = section["line_index"]
        end = post_unit[i + 1]["line_index"] if i + 1 < len(post_unit) else len(lines)
        line_count = end - start
        section_plan.append({**section, "start_line": start, "end_line": end, "line_count": line_count})
        if line_count <= 1:
            errors.append(f"Structural section {section['heading']!r} is empty or nearly empty.")

    lexical_names = [s["name"] for s in section_plan if s["kind"] == "appendix" and s["name"] != "appendix"]
    expected_lexical = ["topic-vocabulary-database", "phrasal-verbs-database", "phrases-patterns-collocations-database", "idioms-database"]
    if lexical_names != expected_lexical:
        errors.append(f"Lexical database sequence is not the expected order: {lexical_names}")

    if unit_plan[-1]["line_count"] > 1200:
        errors.append(
            f"Unit 26 is suspiciously large: {unit_plan[-1]['line_count']} lines. "
            "Expected the lexical/reference layer to begin earlier."
        )

    return {"units": unit_plan, "sections": section_plan}, errors, warnings


def print_plan(plan, warnings):
    print("Extraction plan")
    print("=" * 40)
    for unit in plan["units"]:
        print(f"Unit {unit['unit_number']:02d}: lines {unit['start_line'] + 1}-{unit['end_line']} ({unit['line_count']} lines)")
        if unit["kind"] != "normal":
            print(f"  NOTE: {unit['kind']}: {unit['heading']}")
    print()
    print("Post-unit structural sections")
    print("=" * 40)
    for section in plan["sections"]:
        print(f"{section['kind'].upper():11s} '{section['name']}': lines {section['start_line'] + 1}-{section['end_line']} ({section['line_count']} lines)")
    if warnings:
        print()
        print("Warnings")
        print("=" * 40)
        for warning in warnings:
            print(f"WARNING: {warning}")


def fail(errors):
    print()
    print("RESULT: FAIL")
    for error in errors:
        print(f"ERROR: {error}")
    print()
    print("No files were written.")
    raise SystemExit(1)


def ensure_no_existing(paths):
    existing = [path for path in paths if path.exists()]
    if existing:
        names = ", ".join(str(path.relative_to(ROOT)) for path in existing)
        fail([
            "Refusing to overwrite existing extracted files: " + names,
            "Move/archive the previous extraction before committing a new plan.",
        ])


def commit_plan(plan, lines):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    APPENDIX_OUTPUT.mkdir(parents=True, exist_ok=True)
    BACK_MATTER_OUTPUT.mkdir(parents=True, exist_ok=True)

    unit_paths = [OUTPUT / f"unit-{u['unit_number']:02d}.txt" for u in plan["units"]]
    appendix_paths = []
    back_matter_paths = []
    a = b = 0
    for section in plan["sections"]:
        if section["kind"] == "appendix":
            a += 1
            appendix_paths.append(APPENDIX_OUTPUT / f"appendix-{a:02d}-{section['name']}.txt")
        else:
            b += 1
            back_matter_paths.append(BACK_MATTER_OUTPUT / f"section-{b:02d}-{section['name']}.txt")

    ensure_no_existing(unit_paths + appendix_paths + back_matter_paths)

    for unit in plan["units"]:
        output_file = OUTPUT / f"unit-{unit['unit_number']:02d}.txt"
        output_file.write_text("\n".join(lines[unit["start_line"]:unit["end_line"]]) + "\n", encoding="utf-8")

    a = b = 0
    for section in plan["sections"]:
        content = "\n".join(lines[section["start_line"]:section["end_line"]]) + "\n"
        if section["kind"] == "appendix":
            a += 1
            output_file = APPENDIX_OUTPUT / f"appendix-{a:02d}-{section['name']}.txt"
        else:
            b += 1
            output_file = BACK_MATTER_OUTPUT / f"section-{b:02d}-{section['name']}.txt"
        output_file.write_text(content, encoding="utf-8")


def main():
    if not INPUT.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT}")
    lines = INPUT.read_text(encoding="utf-8", errors="replace").splitlines()
    candidates = discover_candidates(lines)
    if not candidates:
        fail(["No plausible Unit content headings found."])

    selected_units, errors, warnings = build_unit_plan(candidates)
    if errors or selected_units is None:
        fail(errors)

    plan, errors, section_warnings = build_section_plan(lines, selected_units)
    warnings.extend(section_warnings)
    if errors or plan is None:
        if plan:
            print_plan(plan, warnings)
        fail(errors)

    print_plan(plan, warnings)
    print()
    print("PLAN VALIDATION: PASS")
    print()
    commit_plan(plan, lines)
    print("RESULT: SUCCESS")
    print(f"Created {len(plan['units'])} unit files in: {OUTPUT}")
    appendix_count = sum(1 for s in plan["sections"] if s["kind"] == "appendix")
    back_matter_count = len(plan["sections"]) - appendix_count
    print(f"Created {appendix_count} appendix files in: {APPENDIX_OUTPUT}")
    print(f"Created {back_matter_count} back-matter files in: {BACK_MATTER_OUTPUT}")


if __name__ == "__main__":
    main()
