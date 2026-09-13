from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
UNITS = ROOT / "sources" / "destination-c1-c2" / "units"

EXPECTED_UNITS = 26

# Conservative structural headings observed in the extracted Destination C1-C2
# units. This script discovers/validates boundaries only; it never writes section
# files. Ambiguity must fail closed rather than being silently repaired.
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

# Only strip decorative extraction characters when they are immediately before a
# known heading. Do NOT strip arbitrary leading non-letters: doing so turns text
# such as "§ Grammar" inside a comparison note into a false section heading.
HEADING_PREFIX_PATTERN = re.compile(
    r"^[^A-Za-z]*(?=(?:Grammar|Vocabulary|Phrasal\s+verbs|Phrases,\s*patterns\s+and\s+collocations|Idioms|Word\s+formation|Review|Topic\s+vocabulary\s*:|Progress\s+test\b))",
    re.IGNORECASE,
)


def normalize_heading(line):
    text = line.strip()
    text = HEADING_PREFIX_PATTERN.sub("", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_page_header(text):
    return any(pattern.fullmatch(text) for pattern in PAGE_HEADER_PATTERNS)


def classify(line):
    text = normalize_heading(line)
    if not text or is_page_header(text):
        return None

    topic = TOPIC_PATTERN.fullmatch(text)
    if topic:
        topic_name = topic.group(1).strip()
        return "lexical", f"topic-vocabulary:{topic_name}"

    if PROGRESS_TEST_PATTERN.fullmatch(text):
        return "assessment", "progress-test"

    exact = EXACT_HEADINGS.get(text.casefold())
    if exact:
        return exact

    return None


def discover_unit_sections(unit_path):
    lines = unit_path.read_text(encoding="utf-8", errors="replace").splitlines()
    candidates = []
    ignored_repeats = []

    for index, raw_line in enumerate(lines):
        classified = classify(raw_line)
        if classified is None:
            continue

        kind, name = classified
        candidate = {
            "line_index": index,
            "line_number": index + 1,
            "raw_heading": raw_line.strip(),
            "heading": normalize_heading(raw_line),
            "kind": kind,
            "name": name,
        }

        # Destination repeats the same section heading at page breaks. The second
        # occurrence is a continuation marker, not a new section boundary. Keep
        # the evidence so validation/reporting remains auditable, but do not let it
        # split the section.
        if candidates and candidate["name"] == candidates[-1]["name"]:
            ignored_repeats.append(candidate)
            continue

        candidates.append(candidate)

    return lines, candidates, ignored_repeats


def validate_unit_plan(unit_number, lines, candidates, ignored_repeats):
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

    # Repeated exact headings are expected page-break continuations in this source,
    # but report them explicitly so the discovery plan remains auditable.
    for repeat in ignored_repeats:
        warnings.append(
            f"repeated heading treated as continuation: {repeat['heading']!r} "
            f"at line {repeat['line_number']}"
        )

    # Unit files are physical extraction slices, not guaranteed to start at the
    # semantic beginning of a unit. Therefore a lexical/assessment first section
    # is not itself an error; it can be evidence that the preceding page belongs to
    # the same unit. Do not guess or rewrite the unit boundary here.
    first = candidates[0]
    if first["name"] not in {"grammar", "vocabulary"}:
        warnings.append(
            f"first detected section is {first['heading']!r}, not Grammar/Vocabulary; "
            "preserved for structural review"
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

        lines, candidates, ignored_repeats = discover_unit_sections(unit_path)
        errors, warnings = validate_unit_plan(
            unit_number, lines, candidates, ignored_repeats
        )

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
            "ignored_repeats": ignored_repeats,
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
    print("Repeated headings were excluded only as exact continuation markers; no files were written.")


if __name__ == "__main__":
    main()
