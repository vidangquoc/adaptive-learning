from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "sources" / "destination-c1-c2" / "source-segments.yaml"
PDF = ROOT / "sources" / "Destination_C1-C2.pdf"
OUTPUT = ROOT / "sources" / "destination-c1-c2" / "segments"


def parse_manifest(path):
    """Parse the small, constrained YAML manifest without a YAML dependency."""
    segments = []
    current = None
    in_segments = False

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line == "source_segments:":
            in_segments = True
            continue
        if not in_segments:
            continue
        if line.startswith("- id:"):
            if current is not None:
                segments.append(current)
            current = {"id": line.split(":", 1)[1].strip()}
            continue
        if current is None or ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key == "type":
            current["type"] = value
        elif key == "number":
            current["number"] = int(value)
        elif key == "start_page":
            current["start_page"] = int(value)
        elif key == "name":
            current["name"] = value
        elif key == "covers":
            value = value.strip("[] ")
            current["covers"] = [item.strip() for item in value.split(",") if item.strip()]

    if current is not None:
        segments.append(current)
    return segments


def validate_segments(segments):
    errors = []
    if not segments:
        return ["Manifest contains no source segments."]

    starts = [segment.get("start_page") for segment in segments]
    if any(page is None for page in starts):
        errors.append("Every source segment must define start_page.")
    if starts != sorted(starts):
        errors.append("Source segments are not ordered by start_page.")
    if len(starts) != len(set(starts)):
        errors.append("Two or more source segments share the same start_page.")

    ids = [segment.get("id") for segment in segments]
    if len(ids) != len(set(ids)):
        errors.append("Source segment IDs must be unique.")

    for segment in segments:
        if "type" not in segment:
            errors.append(f"Missing type for segment {segment.get('id')}.")

    units = [s for s in segments if s.get("type") == "unit"]
    unit_numbers = [s.get("number") for s in units]
    if unit_numbers != list(range(1, 27)):
        errors.append(f"Unit sequence must be 1..26; found {unit_numbers}.")

    segment_ids = set(ids)
    for segment in segments:
        for covered in segment.get("covers", []):
            if covered not in segment_ids:
                errors.append(
                    f"Segment {segment['id']} references unknown covered segment {covered}."
                )
    return errors


def derive_ranges(segments, pdf_page_count):
    derived = []
    for index, segment in enumerate(segments):
        start = segment["start_page"]
        end = segments[index + 1]["start_page"] - 1 if index + 1 < len(segments) else pdf_page_count
        if start < 1 or end < start or end > pdf_page_count:
            raise ValueError(
                f"Invalid page range for {segment['id']}: {start}-{end}; PDF has {pdf_page_count} pages."
            )
        derived.append({**segment, "end_page": end})
    return derived


def fail(errors):
    print("RESULT: FAIL")
    for error in errors:
        print(f"ERROR: {error}")
    print("No files were written.")
    raise SystemExit(1)


def get_pdf_page_count():
    try:
        import fitz
    except ImportError as exc:
        raise SystemExit("PyMuPDF is required. Install with: pip install pymupdf") from exc
    if not PDF.exists():
        raise FileNotFoundError(f"PDF source not found: {PDF}")
    with fitz.open(PDF) as document:
        return len(document)


def extract_pdf_segments(segments):
    try:
        import fitz
    except ImportError as exc:
        raise SystemExit("PyMuPDF is required. Install with: pip install pymupdf") from exc

    output_paths = [OUTPUT / f"{segment['id']}.pdf" for segment in segments]
    existing = [path for path in output_paths if path.exists()]
    if existing:
        names = ", ".join(str(path.relative_to(ROOT)) for path in existing)
        fail([
            "Refusing to overwrite existing extracted segments: " + names,
            "Remove/archive the previous extraction before running a new extraction.",
        ])

    OUTPUT.mkdir(parents=True, exist_ok=True)
    with fitz.open(PDF) as source:
        for segment in segments:
            # Manifest pages are 1-based PDF viewer pages; PyMuPDF is 0-based.
            start_index = segment["start_page"] - 1
            end_index = segment["end_page"] - 1
            output = fitz.open()
            output.insert_pdf(source, from_page=start_index, to_page=end_index)
            output.save(OUTPUT / f"{segment['id']}.pdf")
            output.close()


def main():
    if not MANIFEST.exists():
        raise FileNotFoundError(f"Manifest not found: {MANIFEST}")

    segments = parse_manifest(MANIFEST)
    errors = validate_segments(segments)
    if errors:
        fail(errors)

    pdf_page_count = get_pdf_page_count()
    derived = derive_ranges(segments, pdf_page_count)

    print("Source segment extraction plan")
    print("=" * 60)
    print(f"PDF pages: {pdf_page_count}")
    print(f"Segments: {len(derived)}")
    for segment in derived:
        print(
            f"{segment['id']:<42} "
            f"pages {segment['start_page']}-{segment['end_page']} "
            f"({segment['type']})"
        )
    print("PLAN VALIDATION: PASS")
    print("Page numbering: 1-based PDF viewer pages")
    print("Extraction source: original PDF only")

    extract_pdf_segments(derived)

    print("RESULT: SUCCESS")
    print(f"Created {len(derived)} PDF source-segment files in: {OUTPUT}")


if __name__ == "__main__":
    main()
