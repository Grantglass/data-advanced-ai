#!/usr/bin/env python3
"""
Export Notebooks to Various Formats

Convert Jupyter notebooks to PDF, HTML, and slides.
"""

import subprocess
from pathlib import Path
import argparse
import sys


def export_notebook(notebook_path: Path, format: str, output_dir: Path) -> bool:
    """
    Export a notebook to specified format.

    Args:
        notebook_path: Path to notebook
        format: Output format ('pdf', 'html', 'slides')
        output_dir: Output directory

    Returns:
        bool: Success status
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    # Determine output file
    output_file = output_dir / f"{notebook_path.stem}.{format}"

    try:
        if format == "html":
            cmd = [
                "jupyter",
                "nbconvert",
                "--to",
                "html",
                "--output",
                str(output_file),
                str(notebook_path),
            ]
        elif format == "pdf":
            cmd = [
                "jupyter",
                "nbconvert",
                "--to",
                "pdf",
                "--output",
                str(output_file),
                str(notebook_path),
            ]
        elif format == "slides":
            cmd = [
                "jupyter",
                "nbconvert",
                "--to",
                "slides",
                "--output",
                str(output_file),
                str(notebook_path),
            ]
        else:
            print(f"Unsupported format: {format}")
            return False

        subprocess.run(cmd, check=True, capture_output=True)
        print(f"✓ Exported {notebook_path.name} to {format}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to export {notebook_path.name}: {e.stderr.decode()}")
        return False
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False


def export_all_notebooks(notebooks_dir: Path, formats: list, output_base_dir: Path):
    """Export all notebooks to specified formats."""
    notebooks = list(notebooks_dir.glob("*.ipynb"))

    if not notebooks:
        print(f"No notebooks found in {notebooks_dir}")
        return

    print(f"Found {len(notebooks)} notebooks\n")

    for fmt in formats:
        print(f"Exporting to {fmt.upper()}...")
        output_dir = output_base_dir / fmt
        output_dir.mkdir(parents=True, exist_ok=True)

        success_count = 0
        for notebook in notebooks:
            if export_notebook(notebook, fmt, output_dir):
                success_count += 1

        print(f"Exported {success_count}/{len(notebooks)} notebooks to {fmt}\n")


def main():
    parser = argparse.ArgumentParser(description="Export Jupyter notebooks")
    parser.add_argument(
        "--dir", type=str, default="notebooks", help="Directory containing notebooks"
    )
    parser.add_argument(
        "--formats",
        type=str,
        nargs="+",
        default=["html"],
        choices=["html", "pdf", "slides"],
        help="Output formats",
    )
    parser.add_argument(
        "--output", type=str, default="exports", help="Output directory"
    )

    args = parser.parse_args()

    # Resolve paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    notebooks_dir = repo_root / args.dir
    output_dir = repo_root / args.output

    if not notebooks_dir.exists():
        print(f"Error: Directory {notebooks_dir} does not exist")
        sys.exit(1)

    export_all_notebooks(notebooks_dir, args.formats, output_dir)


if __name__ == "__main__":
    main()
