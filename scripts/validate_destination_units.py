from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "sources" / "destination-c1-c2" / "raw" / "Destination_C1-C2.txt"
UNITS = ROOT / "sources" / "destination-c1-c2" / "units"
APPENDIX = ROOT / "sources" / "destination-c1-c2" / "appendix"
BACK_MATTER = ROOT / "sources" / "destination-c1-c2" / "back-matter"

# Reuse the canonical boundary-discovery logic from the extraction script.
# This keeps validation aligned with the plan that actually produced the files.
scripts_dir = ROOT / "scripts"
if str(scripts_dir) not in sys.path:
    sys.path.insert(0, str(scripts_dir))

from split_destination import (  # noqa: E402
    build_section_plan,
    build_unit_plan,
    discover_candidates,
)


def fail(message):
    print(f"FAIL: {message}")
    raise SystemExit(1)


def validate_file(path, expected_lines, label):
    if not path.exists():
        fail(f"Missing output file for {label}: {path.relative_to(ROOT)}")

    actual_lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    expected = expected_lines

    if not actual_lines:
        fail(f"Empty output file for {label}: {path.relative_to(ROOT)}")

    if actual_lines != expected:
        # Give a useful boundary-level diagnostic without dumping the whole file.
        first_mismatch = next(
            (i for i, (a, b) in enumerate(zip(actual_lines, expected)) if a != b),
            min(len(actual_lines), len(expected)),
        )
        fail(
            f"Content mismatch for {label}: {path.relative_to(ROOT)}; "
            f"first differing line index={first_mismatch + 1}, "
            f"actual_lines={len(actual_lines)}, expected_lines={len(expected)}"
        )


def main():
    if not RAW.exists():
        fail(f"Raw source not found: {RAW}")

    lines = RAW.read_text(encoding="utf-8", errors="replace").splitlines()
    candidates = discover_candidates(lines)
    if not candidates:
        fail("No plausible Unit content headings found in raw source.")

    selected_units, errors, warnings = build_unit_plan(candidates)
    if errors or selected_units is None:
        fail("Canonical Unit plan is invalid: " + " | ".join(errors))

    plan, errors, section_warnings = build_section_plan(lines, selected_units)
    warnings.extend(section_warnings)
    if errors or plan is None:
        fail("Canonical structural plan is invalid: " + " | ".join(errors))

    print("Destination extraction integrity validation")
    print("=" * 42)
    print(f"Raw lines: {len(lines)}")
    print(f"Expected units: {len(plan['units'])}")
    print(
        "Expected post-unit sections: "
        f"{len(plan['sections'])}"
    )
    print()

    expected_unit_files = set()
    for unit in plan["units"]:
        filename = f"unit-{unit['unit_number']:02d}.txt"
        expected_unit_files.add(filename)
        path = UNITS / filename
        validate_file(
            path,
            lines[unit["start_line"]:unit["end_line"]],
            f"Unit {unit['unit_number']:02d}",
        )
        print(
            f"PASS  Unit {unit['unit_number']:02d}  "
            f"{filename}  ({unit['line_count']} lines)"
        )

    actual_unit_files = {p.name for p in UNITS.glob("unit-*.txt")}
    missing_units = sorted(expected_unit_files - actual_unit_files)
    extra_units = sorted(actual_unit_files - expected_unit_files)
    if missing_units:
        fail(f"Missing unit files: {missing_units}")
    if extra_units:
        fail(f"Unexpected extra unit files: {extra_units}")

    print()
    print("Appendix / back-matter integrity")
    print("=" * 42)

    expected_appendix_files = set()
    expected_back_matter_files = set()
    appendix_index = 0
    back_index = 0
    document_end_index = 0

    for section in plan["sections"]:
        if section["kind"] == "appendix":
            appendix_index += 1
            filename = f"appendix-{appendix_index:02d}-{section['name']}.txt"
            expected_appendix_files.add(filename)
            path = APPENDIX / filename
        elif section["kind"] == "back_matter":
            back_index += 1
            filename = f"section-{back_index:02d}-{section['name']}.txt"
            expected_back_matter_files.add(filename)
            path = BACK_MATTER / filename
        else:
            document_end_index += 1
            filename = f"document-end-{document_end_index:02d}-{section['name']}.txt"
            expected_back_matter_files.add(filename)
            path = BACK_MATTER / filename

        validate_file(
            path,
            lines[section["start_line"]:section["end_line"]],
            section["name"],
        )
        print(
            f"PASS  {section['kind'].upper():11s}  {filename}  "
            f"({section['line_count']} lines)"
        )

    actual_appendix_files = {p.name for p in APPENDIX.glob("*.txt")}
    actual_back_matter_files = {p.name for p in BACK_MATTER.glob("*.txt")}

    missing_appendix = sorted(expected_appendix_files - actual_appendix_files)
    extra_appendix = sorted(actual_appendix_files - expected_appendix_files)
    missing_back = sorted(expected_back_matter_files - actual_back_matter_files)
    extra_back = sorted(actual_back_matter_files - expected_back_matter_files)

    if missing_appendix:
        fail(f"Missing appendix files: {missing_appendix}")
    if extra_appendix:
        fail(f"Unexpected extra appendix files: {extra_appendix}")
    if missing_back:
        fail(f"Missing back-matter files: {missing_back}")
    if extra_back:
        fail(f"Unexpected extra back-matter files: {extra_back}")

    print()
    if warnings:
        print("Warnings")
        print("=" * 42)
        for warning in warnings:
            print(f"WARNING: {warning}")
        print()

    print("RESULT: PASS")
    print(
        f"Validated {len(plan['units'])} units and "
        f"{len(plan['sections'])} post-unit structural sections against the canonical extraction plan."
    )


if __name__ == "__main__":
    main()
