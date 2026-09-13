from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
UNITS = ROOT / "sources" / "destination-c1-c2" / "units"

EXPECTED_UNITS = 26

# These are deliberately conservative structural headings observed in the
# extracted Destination C1-C2 units. This script discovers boundaries only;
# it does not create section files yet.
EXACT_HEADINGS = {
    "grammar": ("main", "grammar"),
    "vocabulary": ("main", "vocabulary"),
    "phrasal verbs": ("lexical", "phrasal-verbs"),
    "phrases, patterns and collocations": ("lexical", "phrases-patterns-collocations"),
    "idioms": ("lexical", "idioms"),
    "word formation": ("lexical", "word-formation"),
    "review": ("assessment", "review"),
}

TOPIC_PATTERN = re.compile(r"^topic\s+vocabulary\s*:\s*(.+?)\s*$", re.IGNORECASE)
PROGRESS_TEST_PATTERN = re.compile(r"^progress\s+test\b.*$", re.IGNORECASE)

# Page headers produced by PDF extraction. They must not become section starts.
PAGE_HEADER_PATTERNS = [
    re.compile(r"^\s*\d+\s+vocabulary\s*$", re.IGNORECASE),
    re.compile(r"^\s*\d+\s+grammar\s*$", re.IGNORECASE),
    re.compile(r"^\s*U\s*N\s*I\s*T\s*$", re.IGNORECASE),
    re.compile(r"^\s*\d+\s*$"),
]


def normalize_heading(line):
    text = line.strip()
    # Remove extraction artefacts around otherwise clean headings, e.g.
    # ". Idioms" -> "Idioms".
    text = re.sub(r"^[^A-Za-z]+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_page_header(text):
    return any(pattern.match(text) for pattern in PAGE_HEADER_PATTERNS)


def classify(line):
    text = normalize_heading(line)
    if not text or is_page_header(text):
        return None

    topic = TOPIC_PATTERN.match(text)
    if topic:
        topic_name = topic.group(1).strip()
        return "lexical", f"topic-vocabulary:{topic_name}"

    if PROGRESS_TEST_PATTERN.match(text):
        return "assessment", "progress-test"

    exact = EXACT_HEADINGS.get(text.casefold())
    if exact:
        return exact

    return None


def discover_unit_sections(unit_path):
    lines = unit_path.read_text(encoding="utf-8", errors="replace").splitlines()
    candidates = []

    for index, raw_line in enumerate(lines):
        classified = classify(raw_line)
        if classified is None:
            continue

        kind, name = classified
        candidates.append({
            "line_index": index,
            "line_number": index + 1,
            "raw_heading": raw_line.strip(),
            "heading": normalize_heading(raw_line),
            "kind": kind,
            "name": name,
        })

    return lines, candidates


def validate_unit_plan(unit_number, lines, candidates):
    errors = []
    warnings = []

    if not candidates:
        errors.append("no structural section candidates found")
        return errors, warnings

    positions = [c["line_index"] for c in candidates]
    if positions != sorted(positions):
        errors.append("section boundaries are not in source order")

    for previous, current in zip(candidates, candidates[1:]):
        if current["line_index"] <= previous["line_index"]:
            errors.append(
                f"non-increasing boundary: {previous['heading']!r} -> {current['heading']!r}"
            )

    # A candidate must have actual content before the next candidate.
    for i, candidate in enumerate(candidates):
        end = candidates[i + 1]["line_index"] if i + 1 < len(candidates) else len(lines)
        line_count = end - candidate["line_index"]
        candidate["end_line"] = end
        candidate["line_count"] = line_count
        if line_count <= 1:
            errors.append(
                f"section {candidate['heading']!r} is empty or nearly empty "
                f"(lines {candidate['line_number']}-{end})"
            )
        elif line_count < 8:
            warnings.append(
                f"section {candidate['heading']!r} is unusually short ({line_count} lines)"
            )

    # A unit should normally begin with Grammar or Vocabulary. If not, keep the
    # candidate but flag it for manual inspection rather than guessing.
    first = candidates[0]
    if first["name"] not in {"grammar", "vocabulary"}:
        warnings.append(
            f"first detected section is {first['heading']!r}, not Grammar/Vocabulary"
        )

    return errors, warnings


def main():
    unit_paths = sorted(UNITS.glob("unit-*.txt"))
    if len(unit_paths) != EXPECTED_UNITS:
        raise SystemExit(
            f"FAIL: expected {EXPECTED_UNITS} unit files, found {len(unit_paths)}"
        )

    all_errors = []
    all_warnings = []
    global_plan = []

    print("Destination C1-C2 section discovery")
    print("=" * 42)
    print(f"Units discovered: {len(unit_paths)}")
    print("No section files will be written by this script.")
    print()

    for expected_number, unit_path in enumerate(unit_paths, start=1):
        match = re.fullmatch(r"unit-(\d+)\.txt", unit_path.name)
        unit_number = int(match.group(1)) if match else expected_number
        if unit_number != expected_number:
            all_errors.append(
                f"unit sequence mismatch: expected {expected_number:02d}, got {unit_number:02d}"
            )

        lines, candidates = discover_unit_sections(unit_path)
        errors, warnings = validate_unit_plan(unit_number, lines, candidates)

        for error in errors:
            all_errors.append(f"Unit {unit_number:02d}: {error}")
        for warning in warnings:
            all_warnings.append(f"Unit {unit_number:02d}: {warning}")

        print(f"Unit {unit_number:02d}: {len(candidates)} candidates")
        for i, candidate in enumerate(candidates):
            end = candidates[i + 1]["line_index"] if i + 1 < len(candidates) else len(lines)
            print(
                f"  {candidate['line_number']:4d}-{end:4d}  "
                f"{candidate['kind']:10s}  {candidate['heading']}"
            )

        global_plan.append({
            "unit": unit_number,
            "path": str(unit_path.relative_to(ROOT)),
            "line_count": len(lines),
            "sections": candidates,
        })
        print()

    print("Validation")
    print("=" * 42)
    if all_warnings:
        for warning in all_warnings:
            print(f"WARNING: {warning}")
    if all_errors:
        print("RESULT: FAIL")
        for error in all_errors:
            print(f"ERROR: {error}")
        print("No files were written.")
        raise SystemExit(1)

    total = sum(len(item["sections"]) for item in global_plan)
    print("RESULT: PASS")
    print(f"Discovered {total} structural section candidates across {EXPECTED_UNITS} units.")
    print("This is a discovery/validation pass only; no section files were created.")


if __name__ == "__main__":
    main()
