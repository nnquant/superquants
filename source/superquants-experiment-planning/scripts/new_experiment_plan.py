#!/usr/bin/env python3
"""Create an implementation and experiment plan from the bundled template."""

from __future__ import annotations

import argparse
from pathlib import Path

from common import render_template, slugify, title_from_slug, today_iso, write_text_file


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, help='Project root where research/superquants should be created.')
    parser.add_argument('--slug', help='ASCII slug for the strategy or research topic.')
    parser.add_argument('--title', help='Human-readable title for the topic.')
    parser.add_argument('--date', default=today_iso(), help='Date prefix in YYYY-MM-DD format.')
    parser.add_argument('--force', action='store_true', help='Overwrite existing files if they already exist.')
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not args.slug and not args.title:
        raise SystemExit('Provide at least --slug or --title.')

    slug = args.slug or slugify(args.title)
    title = args.title or title_from_slug(slug)
    root = Path(args.root).resolve()
    plans_dir = root / 'research' / 'superquants' / 'plans'
    plans_dir.mkdir(parents=True, exist_ok=True)

    replacements = {
        'date': args.date,
        'slug': slug,
        'topic_title': title,
    }

    output_path = plans_dir / f'{args.date}-{slug}-experiment-plan.md'
    write_text_file(output_path, render_template('experiment-plan-template.md', replacements), force=args.force)

    print(f'Created experiment plan: {output_path}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
