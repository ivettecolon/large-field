#!/usr/bin/env python3
"""
Generate manifest.json for the word-based triadic judgment task.
Reads the "Word" column from the Greedy_Init_800 sheet of the xlsx
word list and writes stimuli/words800/manifest.json.

Usage: python generate_word_manifest.py [xlsx_path] [sheet_name]
"""

import sys
import json
import os
from pathlib import Path

import openpyxl

REPO_ROOT = Path(__file__).resolve().parent.parent


def generate_word_manifest(xlsx_path, sheet_name="Greedy_Init_800",
                            output_dir=REPO_ROOT / "stimuli" / "words800"):
    wb = openpyxl.load_workbook(xlsx_path, read_only=True, data_only=True)
    ws = wb[sheet_name]

    rows = list(ws.iter_rows(values_only=True))
    header = rows[0]
    word_idx = header.index("Word")

    words = []
    seen = set()
    for row in rows[1:]:
        value = row[word_idx]
        if value is None:
            continue
        word = str(value).strip()
        if not word or word in seen:
            continue
        seen.add(word)
        words.append(word)

    words.sort(key=str.lower)

    manifest = {
        "words": words,
        "metadata": {
            "total_words": len(words),
            "source_file": os.path.basename(str(xlsx_path)),
            "source_sheet": sheet_name,
            "generated_by": "generate_word_manifest.py",
        },
    }

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "manifest.json"
    with open(output_path, "w") as f:
        json.dump(manifest, f, indent=2)

    return words, output_path


def main():
    xlsx_path = sys.argv[1] if len(sys.argv) > 1 else REPO_ROOT / "800wordlist_313seed.xlsx"
    sheet_name = sys.argv[2] if len(sys.argv) > 2 else "Greedy_Init_800"

    if not os.path.isfile(xlsx_path):
        print(f"Error: file '{xlsx_path}' not found")
        return 1

    print(f"Reading words from '{sheet_name}' sheet of {xlsx_path}")
    words, output_path = generate_word_manifest(xlsx_path, sheet_name)

    print(f"\nGenerated manifest.json with {len(words)} words")
    print(f"  Saved to: {output_path}\n")
    print("Words included:")
    for w in words[:20]:
        print(f"  - {w}")
    if len(words) > 20:
        print(f"  ... and {len(words) - 20} more")

    return 0


if __name__ == "__main__":
    exit(main())
