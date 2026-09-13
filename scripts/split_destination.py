from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

INPUT = ROOT / "sources" / "destination-c1-c2" / "raw" / "Destination_C1-C2.txt"
OUTPUT = ROOT / "sources" / "destination-c1-c2" / "units"


def main():
    if not INPUT.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT}")

    text = INPUT.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    pattern = re.compile(
        r"^\s*Unit\s+(\d+)\s+(.*\S)\s*$",
        re.IGNORECASE
    )

    boundaries = []

    for index, line in enumerate(lines):
        match = pattern.match(line)

        if match:
            boundaries.append({
                "line_index": index,
                "unit_number": int(match.group(1)),
                "heading": match.group(0).strip(),
            })

    if not boundaries:
        raise RuntimeError("No Unit headings found.")

    # Keep only the first occurrence of each Unit number.
    units = []
    seen = set()

    for boundary in boundaries:
        number = boundary["unit_number"]

        if number not in seen:
            seen.add(number)
            units.append(boundary)

    units.sort(key=lambda x: x["unit_number"])

    OUTPUT.mkdir(parents=True, exist_ok=True)

    created = []

    for i, unit in enumerate(units):
        start = unit["line_index"]

        if i + 1 < len(units):
            end = units[i + 1]["line_index"]
        else:
            end = len(lines)

        output_file = OUTPUT / f"unit-{unit['unit_number']:02d}.txt"

        # Safety: refuse to overwrite an existing file.
        if output_file.exists():
            raise FileExistsError(
                f"{output_file} already exists. "
                "Refusing to overwrite it."
            )

        output_file.write_text(
            "\n".join(lines[start:end]) + "\n",
            encoding="utf-8"
        )

        created.append(output_file)

    print()
    print("SUCCESS")
    print(f"Found {len(units)} units.")
    print(f"Created files in: {OUTPUT}")
    print()

    for file in created:
        print(file.name)


if __name__ == "__main__":
    main()