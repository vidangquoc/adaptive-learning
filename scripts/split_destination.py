from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

INPUT = ROOT / "sources" / "destination-c1-c2" / "raw" / "Destination_C1-C2.txt"
OUTPUT = ROOT / "sources" / "destination-c1-c2" / "units"

EXPECTED_UNIT_COUNT = 26
CONTENT_START_LINE = 300

# Normal PDF-extracted headings.
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


def discover_candidates(lines):
    """Discover plausible content-unit headings without mutating the source."""
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


def build_plan(candidates, lines):
    """Build a physical extraction plan, preserving RAW order."""
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

    # Boundaries must be physically ordered in the RAW source.
    positions = [item["line_index"] for item in selected]
    if positions != sorted(positions):
        errors.append("Extraction boundaries are not in RAW source order.")

    # The expected logical sequence must also be preserved by physical order.
    physical_numbers = [item["unit_number"] for item in selected]
    if physical_numbers != expected:
        errors.append(
            "Unit sequence in RAW source is not 1..26 after normalization: "
            f"{physical_numbers}"
        )

    if errors:
        return None, errors, warnings

    plan = []
    for i, unit in enumerate(selected):
        start = unit["line_index"]
        end = selected[i + 1]["line_index"] if i + 1 < len(selected) else len(lines)
        content_line_count = end - start

        if content_line_count <= 1:
            errors.append(
                f"Unit {unit['unit_number']} has no meaningful content "
                f"between lines {start + 1} and {end}."
            )

        plan.append(
            {
                **unit,
                "start_line": start,
                "end_line": end,
                "line_count": content_line_count,
            }
        )

    # Detect suspiciously short units before any files are written.
    for unit in plan:
        if unit["line_count"] < 50:
            warnings.append(
                f"Unit {unit['unit_number']} is unusually short: "
                f"{unit['line_count']} lines."
            )

    return plan, errors, warnings


def print_plan(plan, warnings):
    print("Extraction plan")
    print("=" * 40)
    for unit in plan:
        print(
            f"Unit {unit['unit_number']:02d}: "
            f"lines {unit['start_line'] + 1}-{unit['end_line']} "
            f"({unit['line_count']} lines)"
        )
        if unit["kind"] != "normal":
            print(f"  NOTE: {unit['kind']}: {unit['heading']}")

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


def commit_plan(plan, lines):
    """Write files only after the complete plan has passed validation."""
    OUTPUT.mkdir(parents=True, exist_ok=True)

    existing = [
        OUTPUT / f"unit-{unit['unit_number']:02d}.txt"
        for unit in plan
        if (OUTPUT / f"unit-{unit['unit_number']:02d}.txt").exists()
    ]

    if existing:
        names = ", ".join(path.name for path in existing)
        fail([
            "Refusing to overwrite existing unit files: " + names,
            "Move/archive the previous extraction before committing a new plan.",
        ])

    for unit in plan:
        output_file = OUTPUT / f"unit-{unit['unit_number']:02d}.txt"
        content = "\n".join(lines[unit["start_line"]:unit["end_line"]]) + "\n"
        output_file.write_text(content, encoding="utf-8")


def main():
    if not INPUT.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT}")

    text = INPUT.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    candidates = discover_candidates(lines)
    if not candidates:
        fail(["No plausible Unit content headings found."])

    plan, errors, warnings = build_plan(candidates, lines)

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
    print(f"Created {len(plan)} unit files in: {OUTPUT}")


if __name__ == "__main__":
    main()
