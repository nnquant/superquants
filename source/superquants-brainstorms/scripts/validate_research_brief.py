#!/usr/bin/env python3
"""Validate that a compact research brief contains the required sections."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


REQUIRED_HEADINGS = [
    'decision to inform',
    'claim and mechanism',
    'scope and timing',
    'data and leakage guard',
    'baseline and metrics',
    'costs and constraints',
    'fast falsification',
    'assumptions and open questions',
]


def normalize_heading(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r'[^a-z0-9]+', ' ', value)
    return re.sub(r'\s+', ' ', value).strip()


def extract_headings(text: str) -> set[str]:
    headings = re.findall(r'^#{1,6}\s+(.+?)\s*$', text, flags=re.MULTILINE)
    return {normalize_heading(item) for item in headings}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', help='Path to the markdown document.')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.path).resolve()
    headings = extract_headings(path.read_text(encoding='utf-8'))
    missing = [heading for heading in REQUIRED_HEADINGS if heading not in headings]
    if missing:
        print(f'Research brief is missing required sections in {path}:')
        for heading in missing:
            print(f'- {heading}')
        return 1
    print(f'Research brief looks complete: {path}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
