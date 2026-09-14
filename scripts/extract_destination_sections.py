from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
UNITS = ROOT / "sources" / "destination-c1-c2" / "units"
SECTIONS = ROOT / "sources" / "destination-c1-c2" / "sections"
EXPECTED_UNITS = 26

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
PAGE_HEADER_PATTERNS = [
    re.compile(r"^\s*\d+\s+vocabulary\s*$", re.IGNORECASE),
    re.compile(r"^\s*\d+\s+grammar\s*$", re.IGNORECASE),
    re.compile(r"^\s*U\s*N\s*I\s*T\s*$", re.IGNORECASE),
    re.compile(r"^\s*\d+\s*$"),
]
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
        return "lexical", f"topic-vocabulary:{topic.group(1).strip()}"
    if PROGRESS_TEST_PATTERN.fullmatch(text):
        return "assessment", "progress-test"
    return EXACT_HEADINGS.get(text.casefold())


def discover(lines):
    candidates = []
    for index, raw in enumerate(lines):
        classified = classify(raw)
        if classified is None:
            continue
        kind, name = classified
        candidate = {
            "line_index": index,
            "line_number": index + 1,
            "raw_heading": raw.strip(),
            "heading": normalize_heading(raw),
            "kind": kind,
            "name": name,
        }
        if candidates and candidate["name"] == candidates[-1]["name"]:
            continue
        candidates.append(candidate)
    return candidates


def build_plan():
    unit_paths = sorted(UNITS.glob("unit-*.txt"))
    if len(unit_paths) != EXPECTED_UNITS:
        raise SystemExit(f"FAIL: expected {EXPECTED_UNITS} unit files, found {len(unit_paths)}")

    plan = []
    errors = []
    for expected, path in enumerate(unit_paths, 1):
        match = re.fullmatch(r"unit-(\d+)\.txt", path.name)
        number = int(match.group(1))
        if number != expected:
            errors.append(f"unit sequence mismatch: expected {expected}, got {number}")
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        candidates = discover(lines)
        if not candidates:
            errors.append(f"Unit {number:02d}: no structural candidates")
            continue
        for i, c in enumerate(candidates):
            end = candidates[i + 1]["line_index"] if i + 1 < len(candidates) else len(lines)
            c["end_line"] = end
            c["line_count"] = end - c["line_index"]
            if c["line_count"] <= 1:
                errors.append(f"Unit {number:02d}: empty section at line {c['line_number']}")
        plan.append((number, path, lines, candidates))
    if errors:
        print("PLAN VALIDATION: FAIL")
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    return plan


def safe_name(number, candidate):
    slug = candidate["name"].replace(":", "-")
    slug = re.sub(r"[^a-z0-9-]+", "-", slug.casefold()).strip("-")
    return f"unit-{number:02d}-{slug}.txt"


def extract(plan):
    if SECTIONS.exists() and any(SECTIONS.iterdir()):
        raise SystemExit("FAIL: sections directory is non-empty; refusing to overwrite")
    SECTIONS.mkdir(parents=True, exist_ok=True)
    manifest = []
    for number, path, lines, candidates in plan:
        for candidate in candidates:
            start = candidate["line_index"]
            end = candidate["end_line"]
            content = "\n".join(lines[start:end]) + "\n"
            output = SECTIONS / safe_name(number, candidate)
            output.write_text(content, encoding="utf-8", newline="\n")
            manifest.append(
                f"unit={number:02d}\tsection={candidate['name']}\theading={candidate['heading']}"
                f"\tstart_line={candidate['line_number']}\tend_line={end}"
                f"\tline_count={candidate['line_count']}\tsource={path.relative_to(ROOT)}"
                f"\tfile={output.relative_to(ROOT)}"
            )
    (SECTIONS / "MANIFEST.tsv").write_text("\n".join(manifest) + "\n", encoding="utf-8", newline="\n")


def validate(plan):
    errors = []
    expected_files = []
    for number, path, lines, candidates in plan:
        unit_dir = SECTIONS
        for candidate in candidates:
            output = unit_dir / safe_name(number, candidate)
            expected_files.append(output)
            if not output.exists():
                errors.append(f"missing output: {output}")
                continue
            actual = output.read_text(encoding="utf-8", errors="replace")
            expected = "\n".join(lines[candidate["line_index"]:candidate["end_line"]]) + "\n"
            if actual != expected:
                errors.append(f"content mismatch: {output}")
            first = actual.splitlines()[0] if actual.splitlines() else ""
            if first != candidate["heading"] and first != candidate["raw_heading"]:
                errors.append(f"heading mismatch: {output}")
    actual_files = sorted(p for p in SECTIONS.glob("*.txt") if p.name != "MANIFEST.tsv")
    if sorted(actual_files) != sorted(expected_files):
        errors.append("output file set does not match validated plan")
    manifest = SECTIONS / "MANIFEST.tsv"
    if not manifest.exists():
        errors.append("missing MANIFEST.tsv")
    if errors:
        print("POST-EXTRACTION VALIDATION: FAIL")
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print("POST-EXTRACTION VALIDATION: PASS")
    print(f"Validated {len(expected_files)} section files across {EXPECTED_UNITS} units.")


def main():
    print("Destination C1-C2 section extraction")
    print("=" * 42)
    print("Building and validating global plan...")
    plan = build_plan()
    total = sum(len(candidates) for _, _, _, candidates in plan)
    print(f"PLAN VALIDATION: PASS ({total} sections)")
    print("Writing section files...")
    extract(plan)
    validate(plan)
    print("RESULT: PASS")


if __name__ == "__main__":
    main()
