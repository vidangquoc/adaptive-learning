from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

INPUT = ROOT / "sources" / "destination-c1-c2" / "raw" / "Destination_C1-C2.txt"
OUTPUT = ROOT / "sources" / "destination-c1-c2" / "units"
APPENDIX_OUTPUT = ROOT / "sources" / "destination-c1-c2" / "appendix"
BACK_MATTER_OUTPUT = ROOT / "sources" / "destination-c1-c2" / "back-matter"

EXPECTED_UNIT_COUNT = 26
CONTENT_START_LINE = 300

# Normal PDF-extracted unit headings.
UNIT_PATTERN = re.compile(
    r"^\s*Unit\s+(\d+)\s+(Grammar|Vocabulary)\b.*$",
    re.IGNORECASE,
)

# Known PDF extraction artifact in this source:
# "Unit 1 1 Grammar" is the Unit 11 heading.
UNIT_11_ARTIFACT_PATTERN = re.compile(
    r"^\s*Unit\s+1\s+1\s+Grammar\b.*$",
    re.IGNORECASE,
)

# Structural headings that may terminate the final teaching unit.
# These are intentionally broad: the parser should preserve the section
# rather than guess its semantic role.
APPENDIX_PATTERN = re.compile(
    r"^\s*Appendix(?:\s+.*)?$",
    re.IGNORECASE,
)

BACK_MATTER_PATTERNS = [
    re.compile(r"^\s*Answer\s+Key(?:\s+.*)?$", re.IGNORECASE),
    re.compile(r"^\s*Answer\s+Keys?(?:\s+.*)?$", re.IGNORECASE),
    re.compile(r"^\s*Audioscript(?:s)?(?:\s+.*)?$", re.IGNORECASE),
    re.compile(r"^\s*Audio\s+Scripts?(?:\s+.*)?$", re.IGNORECASE),
    re.compile(r"^\s*References?(?:\s+.*)?$", re.IGNORECASE),
    re.compile(r"^\s*Word\s+List(?:s)?(?:\s+.*)?$", re.IGNORECASE),
]


def classify_structural_heading(line):
    """Return the structural section type for a plausible back-matter heading."""
    if APPENDIX_PATTERN.match(line):
        return "appendix"

    for pattern in BACK_MATTER_PATTERNS:
        if pattern.match(line):
            return "back_matter"

    return None


def discover_candidates(lines):
    """Discover plausible content-unit headings without mutating RAW."""
    candidates = []

    for index, line in enumerate(lines):
        if index < CONTENT_START_LINE:
            continue

        artifact = UNIT_11_ARTIFACT_PATTERN.match(line)
        if artifact:
            candidates.append(
                {
                    "line_index": index,
                    "unit_number": 11,
                    "heading": line.strip(),
                    "kind": "known_pdf_artifact",
                }
            )
            continue

        match = UNIT_PATTERN.match(line)
        if not match:
            continue

        candidates.append(
            {
                "line_index": index,
                "unit_number": int(match.group(1)),
                "heading": line.strip(),
                "kind": "normal",
            }
        )

    return candidates


def discover_post_unit_sections(lines, last_unit_start):
    """Discover structural sections after the final Unit heading."""
    sections = []

    for index in range(last_unit_start + 1, len(lines)):
        line = lines[index].strip()
        if not line:
            continue

        kind = classify_structural_heading(line)
        if kind:
            sections.append(
                {
                    "line_index": index,
                    "heading": line,
                    "kind": kind,
                }
            )

    # Repeated page headers can duplicate a structural heading. Keep only the
    # first occurrence of an identical heading.
    selected = []
    seen_headings = set()

    for section in sections:
        key = section["heading"].casefold()
        if key in seen_headings:
            continue
        seen_headings.add(key)
        selected.append(section)

    return selected


def build_unit_plan(candidates, lines):
    """Build a physical Unit extraction plan, preserving RAW order."""
    errors = []
    warnings = []

    # Keep the first plausible content heading for each unit number.
    # Do NOT sort by unit number: physical RAW order defines boundaries.
    selected = []
    seen = set()

    for candidate in candidates:
        number = candidate["unit_number"]

        if number in seen:
            continue

        seen.add(number)
        selected.append(candidate)

    expected = list(range(1, EXPECTED_UNIT_COUNT + 1))
    detected = sorted(seen)

    if detected != expected:
        missing = sorted(set(expected) - set(detected))
        extra = sorted(set(detected) - set(expected))
        if missing:
            errors.append(f"Missing Unit numbers: {missing}")
        if extra:
            errors.append(f"Unexpected Unit numbers: {extra}")

    positions = [item["line_index"] for item in selected]
    if positions != sorted(positions):
        errors.append("Extraction boundaries are not in RAW source order.")

    physical_numbers = [item["unit_number"] for item in selected]
    if physical_numbers != expected:
        errors.append(
            "Unit sequence in RAW source is not 1..26 after normalization: "
            f"{physical_numbers}"
        )

    if errors:
        return None, errors, warnings

    return selected, errors, warnings


def build_section_plan(lines, selected_units):
    """Build Unit + post-Unit structural boundaries without guessing."""
    errors = []
    warnings = []

    last_unit = selected_units[-1]
    post_unit = discover_post_unit_sections(lines, last_unit["line_index"])

    if not post_unit:
        errors.append(
            "No Appendix or recognized back-matter heading was found after "
            f"Unit {last_unit['unit_number']}. Refusing to let the final Unit "
            "consume the rest of the document."
        )
        return None, errors, warnings

    # The first post-unit structural heading terminates the final Unit.
    unit_plan = []
    for i, unit in enumerate(selected_units):
        start = unit["line_index"]

        if i + 1 < len(selected_units):
            end = selected_units[i + 1]["line_index"]
        else:
            end = post_unit[0]["line_index"]

        line_count = end - start
        unit_plan.append(
            {
                **unit,
                "start_line": start,
                "end_line": end,
                "line_count": line_count,
            }
        )

        if line_count <= 1:
            errors.append(
                f"Unit {unit['unit_number']} has no meaningful content "
                f"between lines {start + 1} and {end}."
            )

        if line_count < 50:
            warnings.append(
                f"Unit {unit['unit_number']} is unusually short: "
                f"{line_count} lines."
            )

    # Build post-unit sections in physical order. The final section is allowed
    # to extend to EOF because it is explicitly classified as back matter.
    section_plan = []
    for i, section in enumerate(post_unit):
        start = section["line_index"]
        end = post_unit[i + 1]["line_index"] if i + 1 < len(post_unit) else len(lines)
        line_count = end - start

        section_plan.append(
            {
                **section,
                "start_line": start,
                "end_line": end,
                "line_count": line_count,
            }
        )

        if line_count <= 1:
            errors.append(
                f"Structural section {section['heading']!r} is empty or nearly empty."
            )

    return {
        "units": unit_plan,
        "sections": section_plan,
    }, errors, warnings


def print_plan(plan, warnings):
    print("Extraction plan")
    print("=" * 40)

    for unit in plan["units"]:
        print(
            f"Unit {unit['unit_number']:02d}: "
            f"lines {unit['start_line'] + 1}-{unit['end_line']} "
            f"({unit['line_count']} lines)"
        )
        if unit["kind"] != "normal":
            print(f"  NOTE: {unit['kind']}: {unit['heading']}")

    print()
    print("Post-unit structural sections")
    print("=" * 40)
    for section in plan["sections"]:
        print(
            f"{section['kind'].upper():11s} {section['heading']!r}: "
            f"lines {section['start_line'] + 1}-{section['end_line']} "
            f"({section['line_count']} lines)"
        )

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
        names = ", ".join(path.name for path in existing)
        fail([
            "Refusing to overwrite existing extracted files: " + names,
            "Move/archive the previous extraction before committing a new plan.",
        ])


def commit_plan(plan, lines):
    """Write files only after the complete document plan has passed validation."""
    OUTPUT.mkdir(parents=True, exist_ok=True)
    APPENDIX_OUTPUT.mkdir(parents=True, exist_ok=True)
    BACK_MATTER_OUTPUT.mkdir(parents=True, exist_ok=True)

    unit_paths = [
        OUTPUT / f"unit-{unit['unit_number']:02d}.txt"
        for unit in plan["units"]
    ]

    appendix_paths = []
    back_matter_paths = []
    appendix_index = 0
    back_matter_index = 0

    for section in plan["sections"]:
        if section["kind"] == "appendix":
            appendix_index += 1
            appendix_paths.append(APPENDIX_OUTPUT / f"appendix-{appendix_index:02d}.txt")
        else:
            back_matter_index += 1
            back_matter_paths.append(
                BACK_MATTER_OUTPUT / f"section-{back_matter_index:02d}.txt"
            )

    ensure_no_existing(unit_paths + appendix_paths + back_matter_paths)

    # Commit only after every target path has passed the overwrite check.
    for unit in plan["units"]:
        output_file = OUTPUT / f"unit-{unit['unit_number']:02d}.txt"
        content = "\n".join(lines[unit["start_line"]:unit["end_line"]]) + "\n"
        output_file.write_text(content, encoding="utf-8")

    appendix_index = 0
    back_matter_index = 0

    for section in plan["sections"]:
        content = "\n".join(lines[section["start_line"]:section["end_line"]]) + "\n"

        if section["kind"] == "appendix":
            appendix_index += 1
            output_file = APPENDIX_OUTPUT / f"appendix-{appendix_index:02d}.txt"
        else:
            back_matter_index += 1
            output_file = BACK_MATTER_OUTPUT / f"section-{back_matter_index:02d}.txt"

        output_file.write_text(content, encoding="utf-8")


def main():
    if not INPUT.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT}")

    text = INPUT.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    candidates = discover_candidates(lines)
    if not candidates:
        fail(["No plausible Unit content headings found."])

    selected_units, errors, warnings = build_unit_plan(candidates, lines)
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
    print("No files have been written yet.")
    print()

    commit_plan(plan, lines)

    print("RESULT: SUCCESS")
    print(f"Created {len(plan['units'])} unit files in: {OUTPUT}")

    appendix_count = sum(1 for section in plan["sections"] if section["kind"] == "appendix")
    back_matter_count = len(plan["sections"]) - appendix_count

    print(f"Created {appendix_count} appendix files in: {APPENDIX_OUTPUT}")
    print(f"Created {back_matter_count} back-matter files in: {BACK_MATTER_OUTPUT}")


if __name__ == "__main__":
    main()
