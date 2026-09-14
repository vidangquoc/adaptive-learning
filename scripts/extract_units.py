from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "sources" / "destination-c1-c2" / "raw" / "Destination_C1-C2.txt"
OUTPUT = ROOT / "sources" / "destination-c1-c2" / "units"

EXPECTED_UNIT_COUNT = 26
CONTENT_START_LINE = 300

# The source contains the real Unit headings as "Unit N Grammar" or
# "Unit N Vocabulary". One known PDF extraction artifact for Unit 11 is
# normalized to Unit 11.
UNIT_PATTERN = re.compile(
    r"^\s*Unit\s+(\d+)\s+(Grammar|Vocabulary)\b.*$",
    re.IGNORECASE,
)
UNIT_11_ARTIFACT_PATTERN = re.compile(
    r"^\s*Unit\s+1\s+1\s+Grammar\b.*$",
    re.IGNORECASE,
)

# These markers are used only to prevent Unit 26 from consuming material
# that starts after the Unit sequence. They are NOT extracted as sections.
POST_UNIT_MARKERS = [
    re.compile(r"^\s*Topic vocabulary database\s*$", re.IGNORECASE),
    re.compile(r"^\s*Phrasal verbs database\s*$", re.IGNORECASE),
    re.compile(
        r"^\s*Phrases, patterns and collocations database\s*$",
        re.IGNORECASE,
    ),
    re.compile(r"^\s*Idioms database\s*$", re.IGNORECASE),
    re.compile(r"^\s*Appendix(?:\s+.*)?$", re.IGNORECASE),
    re.compile(r"^\s*Answer\s+Keys?(?:\s+.*)?$", re.IGNORECASE),
    re.compile(r"^\s*Audioscript(?:s)?(?:\s+.*)?$", re.IGNORECASE),
    re.compile(r"^\s*Audio\s+Scripts?(?:\s+.*)?$", re.IGNORECASE),
    re.compile(r"^\s*Word\s+List(?:s)?(?:\s+.*)?$", re.IGNORECASE),
]


def is_post_unit_marker(line):
    return any(pattern.match(line) for pattern in POST_UNIT_MARKERS)


def discover_units(lines):
    candidates = []
    for index, line in enumerate(lines):
        if index < CONTENT_START_LINE:
            continue

        if UNIT_11_ARTIFACT_PATTERN.match(line):
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
        if match:
            candidates.append(
                {
                    "line_index": index,
                    "unit_number": int(match.group(1)),
                    "heading": line.strip(),
                    "kind": "normal",
                }
            )

    selected = []
    seen = set()
    for candidate in candidates:
        number = candidate["unit_number"]
        if number in seen:
            continue
        seen.add(number)
        selected.append(candidate)

    return selected


def build_unit_plan(lines):
    candidates = discover_units(lines)
    errors = []
    warnings = []

    expected = list(range(1, EXPECTED_UNIT_COUNT + 1))
    detected = [item["unit_number"] for item in candidates]

    if sorted(detected) != expected:
        missing = sorted(set(expected) - set(detected))
        extra = sorted(set(detected) - set(expected))
        if missing:
            errors.append(f"Missing Unit numbers: {missing}")
        if extra:
            errors.append(f"Unexpected Unit numbers: {extra}")

    if detected != expected:
        errors.append(f"Unit sequence is not 1..26: {detected}")

    positions = [item["line_index"] for item in candidates]
    if positions != sorted(positions):
        errors.append("Unit boundaries are not in source order.")

    if errors:
        return None, errors, warnings

    units = []
    for index, unit in enumerate(candidates):
        start = unit["line_index"]

        if index + 1 < len(candidates):
            end = candidates[index + 1]["line_index"]
        else:
            end = len(lines)
            # Unit 26 must stop before post-unit material, if such a marker
            # exists. The marker itself is not emitted into any Unit file.
            for marker_index in range(start + 1, len(lines)):
                if is_post_unit_marker(lines[marker_index].strip()):
                    end = marker_index
                    break

        line_count = end - start
        if line_count <= 1:
            errors.append(
                f"Unit {unit['unit_number']} has no meaningful content "
                f"between lines {start + 1} and {end}."
            )
        if line_count < 50:
            warnings.append(
                f"Unit {unit['unit_number']} is unusually short: {line_count} lines."
            )

        units.append(
            {
                **unit,
                "start_line": start,
                "end_line": end,
                "line_count": line_count,
            }
        )

    raw_line_count = len(lines)
    for unit in units:
        if not (0 <= unit["start_line"] < unit["end_line"] <= raw_line_count):
            errors.append(
                f"Invalid boundary for Unit {unit['unit_number']}: "
                f"lines {unit['start_line'] + 1}-{unit['end_line']} "
                f"exceed raw line count {raw_line_count}."
            )

    return units, errors, warnings


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
        fail(
            [
                "Refusing to overwrite existing Unit files: " + names,
                "Remove/archive the previous extraction before running a new extraction.",
            ]
        )


def main():
    if not INPUT.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT}")

    lines = INPUT.read_text(encoding="utf-8", errors="replace").splitlines()
    units, errors, warnings = build_unit_plan(lines)

    if errors or units is None:
        fail(errors)

    print("Unit extraction plan")
    print("=" * 40)
    for unit in units:
        print(
            f"Unit {unit['unit_number']:02d}: "
            f"lines {unit['start_line'] + 1}-{unit['end_line']} "
            f"({unit['line_count']} lines)"
        )

    if warnings:
        print()
        print("Warnings")
        print("=" * 40)
        for warning in warnings:
            print(f"WARNING: {warning}")

    print()
    print("PLAN VALIDATION: PASS")

    output_paths = [
        OUTPUT / f"unit-{unit['unit_number']:02d}.txt" for unit in units
    ]
    ensure_no_existing(output_paths)

    OUTPUT.mkdir(parents=True, exist_ok=True)
    for unit in units:
        output_file = OUTPUT / f"unit-{unit['unit_number']:02d}.txt"
        content = "\n".join(lines[unit["start_line"] : unit["end_line"]]) + "\n"
        output_file.write_text(content, encoding="utf-8")

    print()
    print("RESULT: SUCCESS")
    print(f"Created {len(units)} Unit files in: {OUTPUT}")


if __name__ == "__main__":
    main()
