#!/usr/bin/env python3
"""
Notebook Testing Script

Automatically test that all Jupyter notebooks execute without errors.
"""

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from pathlib import Path
import sys
import argparse
from typing import List, Dict


def test_notebook(notebook_path: Path, timeout: int = 600) -> Dict:
    """
    Test a single notebook by executing all cells.

    Args:
        notebook_path: Path to the notebook
        timeout: Execution timeout in seconds

    Returns:
        Dict with test results
    """
    result = {
        "notebook": notebook_path.name,
        "path": str(notebook_path),
        "success": False,
        "error": None,
        "cells_executed": 0,
    }

    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)

        ep = ExecutePreprocessor(timeout=timeout, kernel_name="python3")

        # Execute the notebook
        ep.preprocess(nb, {"metadata": {"path": str(notebook_path.parent)}})

        result["success"] = True
        result["cells_executed"] = len(nb.cells)

    except Exception as e:
        result["error"] = str(e)

    return result


def test_all_notebooks(
    notebooks_dir: Path, pattern: str = "*.ipynb", exclude: List[str] = None
) -> List[Dict]:
    """
    Test all notebooks in a directory.

    Args:
        notebooks_dir: Directory containing notebooks
        pattern: Glob pattern for notebook files
        exclude: List of notebook names to exclude

    Returns:
        List of test results
    """
    if exclude is None:
        exclude = []

    notebooks = list(notebooks_dir.glob(pattern))
    notebooks = [nb for nb in notebooks if nb.name not in exclude]

    results = []
    total = len(notebooks)

    print(f"Found {total} notebooks to test\n")

    for i, notebook_path in enumerate(notebooks, 1):
        print(f"[{i}/{total}] Testing {notebook_path.name}...", end=" ")

        result = test_notebook(notebook_path)

        if result["success"]:
            print("✓ PASSED")
        else:
            print("✗ FAILED")
            print(f"  Error: {result['error']}")

        results.append(result)

    return results


def print_summary(results: List[Dict]):
    """Print test summary."""
    total = len(results)
    passed = sum(1 for r in results if r["success"])
    failed = total - passed

    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Total notebooks: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Success rate: {(passed/total*100):.1f}%")

    if failed > 0:
        print("\nFailed notebooks:")
        for r in results:
            if not r["success"]:
                print(f"  - {r['notebook']}")
                print(f"    Error: {r['error'][:100]}...")

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Test Jupyter notebooks")
    parser.add_argument(
        "--dir", type=str, default="notebooks", help="Directory containing notebooks"
    )
    parser.add_argument(
        "--pattern", type=str, default="*.ipynb", help="Glob pattern for notebook files"
    )
    parser.add_argument(
        "--timeout", type=int, default=600, help="Execution timeout in seconds"
    )
    parser.add_argument(
        "--exclude", type=str, nargs="+", help="Notebook names to exclude"
    )

    args = parser.parse_args()

    # Resolve paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    notebooks_dir = repo_root / args.dir

    if not notebooks_dir.exists():
        print(f"Error: Directory {notebooks_dir} does not exist")
        sys.exit(1)

    # Run tests
    results = test_all_notebooks(
        notebooks_dir, pattern=args.pattern, exclude=args.exclude or []
    )

    # Print summary
    print_summary(results)

    # Exit with error code if any tests failed
    if any(not r["success"] for r in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
