from __future__ import annotations

import argparse
from pathlib import Path

import fitz  # PyMuPDF


REPO_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_INPUT_DIR = REPO_ROOT / "sources" / "destination-c1-c2" / "segments"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "sources" / "destination-c1-c2" / "segment-text"


def pdf_to_text(pdf_path: Path) -> str:
    """Extract text from a PDF while preserving page order."""
    document = fitz.open(pdf_path)
    pages = []

    try:
        for page_number, page in enumerate(document, start=1):
            text = page.get_text("text")
            pages.append(f"\n===== PDF PAGE {page_number} =====\n\n{text.rstrip()}\n")
    finally:
        document.close()

    return "".join(pages).lstrip()


def convert_segment(pdf_path: Path, output_dir: Path, overwrite: bool) -> Path:
    output_path = output_dir / f"{pdf_path.stem}.txt"

    if output_path.exists() and not overwrite:
        raise FileExistsError(
            f"Output already exists: {output_path}\n"
            "Use --overwrite if you want to replace it."
        )

    text = pdf_to_text(pdf_path)
    output_path.write_text(text, encoding="utf-8")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Destination C1-C2 PDF source segments to TXT."
    )
    parser.add_argument(
        "segment",
        nargs="?",
        help="Segment filename, e.g. unit-01.pdf. If omitted, all PDF segments are converted.",
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=DEFAULT_INPUT_DIR,
        help="Directory containing PDF source segments.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory where TXT files will be written.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing TXT files.",
    )
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)

    if args.segment:
        pdf_path = input_dir / args.segment
        if not pdf_path.exists():
            raise FileNotFoundError(f"Segment not found: {pdf_path}")
        if pdf_path.suffix.lower() != ".pdf":
            raise ValueError(f"Expected a PDF file, got: {pdf_path.name}")
        pdf_files = [pdf_path]
    else:
        pdf_files = sorted(input_dir.glob("*.pdf"))

    if not pdf_files:
        raise RuntimeError(f"No PDF segments found in: {input_dir}")

    print(f"Input : {input_dir}")
    print(f"Output: {output_dir}")
    print(f"Segments: {len(pdf_files)}")
    print()

    converted = 0

    for pdf_path in pdf_files:
        print(f"[{converted + 1}/{len(pdf_files)}] {pdf_path.name}")
        try:
            output_path = convert_segment(pdf_path, output_dir, args.overwrite)
            print(f"  -> {output_path.name}")
            converted += 1
        except FileExistsError as exc:
            print(f"  SKIP: {exc}")

    print()
    print(f"Converted: {converted}/{len(pdf_files)}")
    print("RESULT: SUCCESS")


if __name__ == "__main__":
    main()
