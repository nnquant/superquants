#!/usr/bin/env python3
"""Validate that a Live review memo contains the required sections."""

from __future__ import annotations

import argparse
from pathlib import Path
import re

REQUIRED_HEADINGS = [
    'scope and period',
    'expectation summary',
    'live vs backtest reconciliation',
    'divergence attribution',
    'decay trigger status',
    'calibration update',
    'decision',
    'next action',
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
    text = path.read_text(encoding='utf-8')
    headings = extract_headings(text)
    missing = [heading for heading in REQUIRED_HEADINGS if heading not in headings]

    if missing:
        print(f'Live review memo is missing required sections in {path}:')
        for heading in missing:
            print(f'- {heading}')
        return 1

    print(f'Live review memo looks complete: {path}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
