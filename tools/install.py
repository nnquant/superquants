#!/usr/bin/env python3
"""Install the Superquants skills for Claude Code without the plugin mechanism.

Copies each skill from source/ into a skills directory that Claude Code
auto-discovers:

  user scope (default): ~/.claude/skills/<skill-name>/
  project scope:        <project>/.claude/skills/<skill-name>/  (--project PATH)

Use --remove to uninstall the same set. Alternatively, skip this script and use
the plugin route: /plugin marketplace add <repo-root>, then
/plugin install superquants@superquants-local.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil

REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / 'source'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--project', help='Install into this project directory (.claude/skills/) instead of the user scope.')
    parser.add_argument('--target-dir', help='Explicit skills directory (overrides scope selection).')
    parser.add_argument('--remove', action='store_true', help='Remove the Superquants skills from the target instead of installing.')
    return parser.parse_args()


def target_skills_dir(args: argparse.Namespace) -> Path:
    if args.target_dir:
        return Path(args.target_dir).resolve()
    if args.project:
        return Path(args.project).resolve() / '.claude' / 'skills'
    return Path.home() / '.claude' / 'skills'


def main() -> int:
    args = parse_args()
    target = target_skills_dir(args)
    skills = sorted(p for p in SOURCE.iterdir() if p.is_dir())

    for skill in skills:
        dest = target / skill.name
        if args.remove:
            if dest.exists():
                shutil.rmtree(dest)
                print(f'Removed {dest}')
            continue
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(skill, dest, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        print(f'Installed {skill.name} -> {dest}')

    if not args.remove:
        print(f'\n{len(skills)} skills installed under {target}. Restart Claude Code sessions to pick them up.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
