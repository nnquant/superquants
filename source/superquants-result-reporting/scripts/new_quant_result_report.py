#!/usr/bin/env python3
"""Create a quant result report with only the selected evidence modules."""

from __future__ import annotations

import argparse
from pathlib import Path

from common import render_template, slugify, title_from_slug, today_iso, write_text_file


MODULE_TEMPLATES = {
    'backtest': 'module-backtest-template.md',
    'factor': 'module-factor-template.md',
    'execution': 'module-execution-template.md',
    'robustness': 'module-robustness-template.md',
    'live': 'module-live-template.md',
    'diagnostic': 'module-diagnostic-template.md',
    'learning': 'module-learning-template.md',
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, help='Project root where research/superquants should be created.')
    parser.add_argument('--slug', help='ASCII slug for the strategy or research topic.')
    parser.add_argument('--title', help='Human-readable title for the topic.')
    parser.add_argument('--date', default=today_iso(), help='Date prefix in YYYY-MM-DD format.')
    parser.add_argument('--modules', nargs='*', choices=sorted(MODULE_TEMPLATES), default=[], help='Evidence modules to include. Omit for a core-only report.')
    parser.add_argument('--force', action='store_true', help='Overwrite an existing report.')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.slug and not args.title:
        raise SystemExit('Provide at least --slug or --title.')

    slug = args.slug or slugify(args.title)
    title = args.title or title_from_slug(slug)
    replacements = {'date': args.date, 'slug': slug, 'topic_title': title}
    core = render_template('quant-result-report-template.md', replacements)

    module_names = list(dict.fromkeys(args.modules))
    if module_names:
        selected = '\n\n'.join(render_template(MODULE_TEMPLATES[name], replacements).strip() for name in module_names)
    else:
        selected = 'No optional evidence module selected yet. Add only the evidence needed for this result.'
    report = core.replace('<!-- SELECTED_MODULES -->', selected)

    root = Path(args.root).resolve()
    output_path = root / 'research' / 'superquants' / 'reports' / f'{args.date}-{slug}-result-report.md'
    write_text_file(output_path, report, force=args.force)
    print(f'Created quant result report: {output_path}')
    print(f'Selected modules: {", ".join(module_names) if module_names else "core only"}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
