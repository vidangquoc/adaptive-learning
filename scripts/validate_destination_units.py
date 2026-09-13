from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

RAW = ROOT / "sources" / "destination-c1-c2" / "raw" / "Destination_C1-C2.txt"
UNITS = ROOT / "sources" / "destination-c1-c2" / "units"

UNIT_PATTERN = re.compile(r"^\s*Unit\s+(\d+)\s+(.*\S)\s*$", re.IGNORECASE)


def detect_first_unit_boundaries(lines):
    """Return the first occurrence of each Unit heading in source order."""
    boundaries = []
    seen = set()

    for index, line in enumerate(lines):
        match = UNIT_PATTERN.match(line)
        if not match:
            continue

        number = int(match.group(1))
        if number in seen:
            continue

        seen.add(number)
        boundaries.append((number, index, match.group(0).strip()))

    return boundaries


def fail(message):
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main():
    if not RAW.exists():
        fail(f"Raw source not found: {RAW}")

    if not UNITS.exists():
        fail(f"Units directory not found: {UNITS}")

    lines = RAW.read_text(encoding="utf-8", errors="replace").splitlines()
    boundaries = detect_first_unit_boundaries(lines)

    if not boundaries:
        fail("No Unit headings detected in raw source.")

    expected_numbers = list(range(1, boundaries[-1][0] + 1))
    detected_numbers = [number for number, _, _ in boundaries]

    print("Destination unit validation")
    print("=" * 30)
    print(f"Detected units: {len(boundaries)}")
    print(f"Unit range: {detected_numbers[0]}-{detected_numbers[-1]}")
    print()

    if detected_numbers != expected_numbers:
        fail(
            "Unit numbering is not contiguous: "
            f"expected {expected_numbers}, got {detected_numbers}"
        )

    # Validate every extracted unit against its source boundary.
    for position, (number, start, heading) in enumerate(boundaries):
        expected_file = UNITS / f"unit-{number:02d}.txt"

        if not expected_file.exists():
            fail(f"Missing output file: {expected_file.name}")

        content_lines = expected_file.read_text(
            encoding="utf-8", errors="replace"
        ).splitlines()

        if not content_lines:
            fail(f"Empty output file: {expected_file.name}")

        first_line = content_lines[0].strip()
        if not UNIT_PATTERN.match(first_line):
            fail(
                f"{expected_file.name} does not start with a Unit heading: "
                f"{first_line!r}"
            )

        extracted_number = int(UNIT_PATTERN.match(first_line).group(1))
        if extracted_number != number:
            fail(
                f"{expected_file.name} starts with Unit {extracted_number}, "
                f"expected Unit {number}"
            )

        if position + 1 < len(boundaries):
            next_number = boundaries[position + 1][0]
            next_heading_pattern = re.compile(
                rf"^\s*Unit\s+{next_number}\s+", re.IGNORECASE
            )

            leaked = [line for line in content_lines if next_heading_pattern.match(line)]
            if leaked:
                fail(
                    f"Cross-boundary leakage: {expected_file.name} contains "
                    f"a Unit {next_number} heading"
                )

        # The first line should correspond to the detected source heading.
        if first_line != heading:
            fail(
                f"Heading mismatch in {expected_file.name}: "
                f"source={heading!r}, output={first_line!r}"
            )

        print(f"PASS  Unit {number:02d}  {expected_file.name}")

    # Warn about extra unit files that are not represented in the raw source.
    expected_files = {
        f"unit-{number:02d}.txt" for number, _, _ in boundaries
    }
    actual_files = {path.name for path in UNITS.glob("unit-*.txt")}
    extras = sorted(actual_files - expected_files)

    if extras:
        print()
        print("WARNING: extra unit files not represented in raw source:")
        for name in extras:
            print(f"  - {name}")

    print()
    print("RESULT: PASS")
    print(f"Validated {len(boundaries)} unit files.")


if __name__ == "__main__":
    main()
