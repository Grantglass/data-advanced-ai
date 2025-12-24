#!/usr/bin/env python3
"""
Notebook Enhancement Script

Applies educational enhancements to Jupyter notebooks based on documented patterns.
"""

import nbformat
from pathlib import Path
import re
import sys


def enhance_markdown_cell(cell_source):
    """
    Enhance markdown cells with better formatting and visual elements.
    """
    # Add visual hierarchy to headers
    if cell_source.startswith('# ') and not any(emoji in cell_source for emoji in ['📘', '🎯', '💡', '📊', '🔧']):
        # Add topic emoji to main headers
        if 'Week' in cell_source[:50]:
            cell_source = cell_source.replace('# ', '# 📘 ', 1)

    # Enhance learning objectives
    if 'Learning Objectives' in cell_source:
        if '- [ ]' not in cell_source:
            # Convert bullet points to checkboxes
            cell_source = cell_source.replace('\n- ', '\n- [ ] ')
            cell_source = cell_source.replace('## Learning Objectives', '## 🎯 Learning Objectives')

    # Add callout boxes where appropriate
    if 'important' in cell_source.lower() or 'key' in cell_source.lower():
        if not cell_source.startswith('>'):
            # Look for sentences with "important" or "key" and make them callouts
            lines = cell_source.split('\n')
            enhanced_lines = []
            for line in lines:
                if ('important' in line.lower() or 'key concept' in line.lower()) and not line.startswith('>'):
                    enhanced_lines.append(f"> 💡 **Key Insight**: {line.strip('- ').strip()}")
                else:
                    enhanced_lines.append(line)
            cell_source = '\n'.join(enhanced_lines)

    # Enhance discussion questions
    if 'Discussion Question' in cell_source or 'Consider the following' in cell_source:
        cell_source = cell_source.replace('## Discussion Question', '## 🤔 Discussion Question')
        cell_source = cell_source.replace('## Discussion', '## 🤔 Discussion')

    # Enhance key takeaways
    if 'Key Takeaway' in cell_source or 'Summary' in cell_source:
        cell_source = cell_source.replace('## Key Takeaway', '## 📌 Key Takeaways')
        cell_source = cell_source.replace('## Summary', '## 📌 Summary')

    # Add checkboxes to hands-on sections
    if 'YOUR TURN' in cell_source or 'Exercise' in cell_source:
        cell_source = cell_source.replace('## Exercise', '## 🔧 Hands-On Exercise')
        cell_source = cell_source.replace('YOUR TURN', '🎯 YOUR TURN')

    return cell_source


def enhance_code_cell(cell_source):
    """
    Enhance code cells with better documentation.
    """
    # If code doesn't have a goal comment, don't modify
    # (we'd need AI to understand what the code does)
    # Just ensure good formatting

    lines = cell_source.split('\n')
    if lines and not lines[0].startswith('#'):
        # Add a placeholder for manual enhancement
        enhanced = f"# 🎯 GOAL: [Describe what this code does]\n# Example input: [Show example]\n# Expected output: [Show expected result]\n\n{cell_source}"
        return enhanced

    return cell_source


def add_visual_summary(notebook_cells):
    """
    Add a visual summary cell at the end if not present.
    """
    # Check if last few cells have a summary
    has_summary = any('Key Takeaway' in str(cell.get('source', '')) or 'Summary' in str(cell.get('source', ''))
                     for cell in notebook_cells[-5:] if cell['cell_type'] == 'markdown')

    if not has_summary:
        summary_cell = {
            'cell_type': 'markdown',
            'metadata': {},
            'source': """## 📌 Key Takeaways

### Main Concepts

> 💡 **Remember**: [List 3-5 key concepts from this notebook]

### Quick Reference

| Concept | When to Use | Key Benefit |
|---------|-------------|-------------|
| [Concept 1] | [Scenario] | [Benefit] |
| [Concept 2] | [Scenario] | [Benefit] |

### ✅ Self-Assessment

Before moving on, can you:
- [ ] Explain [concept 1]?
- [ ] Implement [technique 2]?
- [ ] Identify when to use [approach 3]?

If you checked all boxes: Great! You're ready for the next week.
If not: Review the sections you're unsure about."""
        }
        return summary_cell

    return None


def enhance_notebook(notebook_path):
    """
    Apply all enhancements to a notebook.
    """
    print(f"Enhancing: {notebook_path.name}")

    # Read notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Track changes
    changes = 0

    # Enhance each cell
    for cell in nb.cells:
        original_source = cell['source']

        if cell['cell_type'] == 'markdown':
            cell['source'] = enhance_markdown_cell(cell['source'])
            if cell['source'] != original_source:
                changes += 1

        # Note: We're being conservative with code cells
        # Only add comments if they're completely missing
        # elif cell['cell_type'] == 'code' and cell['source'].strip():
        #     enhanced = enhance_code_cell(cell['source'])
        #     if enhanced != cell['source']:
        #         cell['source'] = enhanced
        #         changes += 1

    # Add summary if missing
    summary = add_visual_summary(nb.cells)
    if summary:
        nb.cells.append(nbformat.v4.new_markdown_cell(summary['source']))
        changes += 1

    # Write enhanced notebook
    if changes > 0:
        output_path = notebook_path.parent / f"{notebook_path.stem}_enhanced{notebook_path.suffix}"
        with open(output_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"  ✅ Made {changes} enhancements → {output_path.name}")
        return True
    else:
        print(f"  ℹ️  No automatic enhancements needed")
        return False


def main():
    # Get notebooks directory
    script_dir = Path(__file__).parent
    notebooks_dir = script_dir.parent / 'notebooks'

    if not notebooks_dir.exists():
        print(f"Error: {notebooks_dir} not found")
        sys.exit(1)

    # Find all notebooks
    notebooks = sorted(notebooks_dir.glob('week*.ipynb'))

    if not notebooks:
        print(f"No notebooks found in {notebooks_dir}")
        sys.exit(1)

    print(f"Found {len(notebooks)} notebooks to enhance\n")

    enhanced_count = 0
    for notebook_path in notebooks:
        if enhance_notebook(notebook_path):
            enhanced_count += 1
        print()

    print("="*60)
    print(f"Enhancement complete!")
    print(f"Enhanced {enhanced_count}/{len(notebooks)} notebooks")
    print("\nNote: This script applies automatic enhancements.")
    print("For full enhancement, manually add:")
    print("  - ASCII diagrams")
    print("  - Real-world case studies")
    print("  - Detailed code comments (GOAL, EXAMPLE, WHY)")
    print("  - Interactive elements")
    print("\nSee docs/notebook_enhancements_example.md for patterns.")


if __name__ == '__main__':
    main()
