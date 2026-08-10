#!/usr/bin/env python3
"""Create a new experiment log from the bundled template."""

from __future__ import annotations

import argparse
from pathlib import Path

from common import render_template, slugify, title_from_slug, today_iso, write_text_file


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, help='Project root that contains research/superquants.')
    parser.add_argument('--strategy-slug', required=True, help='ASCII strategy slug, e.g. mean-reversion.')
    parser.add_argument('--experiment', required=True, help='Experiment name, e.g. baseline-zscore-20d.')
    parser.add_argument('--strategy-title', help='Optional human-readable strategy title.')
    parser.add_argument('--date', default=today_iso(), help='Date prefix in YYYY-MM-DD format.')
    parser.add_argument('--force', action='store_true', help='Overwrite the file if it already exists.')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    strategy_slug = slugify(args.strategy_slug)
    experiment_slug = slugify(args.experiment)
    strategy_title = args.strategy_title or title_from_slug(strategy_slug)

    root = Path(args.root).resolve()
    experiments_dir = root / 'research' / 'superquants' / 'experiments'
    experiments_dir.mkdir(parents=True, exist_ok=True)

    replacements = {
        'date': args.date,
        'topic_title': strategy_title,
        'strategy_slug': strategy_slug,
        'experiment_name': args.experiment,
        'experiment_slug': experiment_slug,
    }

    output_path = experiments_dir / f'{args.date}-{strategy_slug}-{experiment_slug}.md'
    write_text_file(output_path, render_template('experiment-log-template.md', replacements), force=args.force)

    print(f'Created experiment log: {output_path}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
