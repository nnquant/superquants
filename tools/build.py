#!/usr/bin/env python3
"""Build the Superquants suite: verify consistency, sync source/ to plugins/, rebuild packages/.

Usage: python tools/build.py [--check-only]
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import sys
import zipfile

REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / 'source'
PLUGIN_SKILLS = REPO / 'plugins' / 'superquants' / 'skills'
PACKAGES = REPO / 'packages'

VALIDATOR_TEMPLATE_PAIRS = {
    'superquants-brainstorms/scripts/validate_research_spec.py': 'superquants-brainstorms/assets/templates/research-spec-template.md',
    'superquants-data-prepare/scripts/validate_data_audit.py': 'superquants-data-prepare/assets/templates/data-audit-template.md',
    'superquants-experiment-planning/scripts/validate_experiment_plan.py': 'superquants-experiment-planning/assets/templates/experiment-plan-template.md',
    'superquants-experiment-planning/scripts/validate_experiment_log.py': 'superquants-experiment-planning/assets/templates/experiment-log-template.md',
    'superquants-strategy-debugging/scripts/validate_diagnosis_memo.py': 'superquants-strategy-debugging/assets/templates/diagnosis-memo-template.md',
    'superquants-robustness-review/scripts/validate_review_memo.py': 'superquants-robustness-review/assets/templates/review-memo-template.md',
    'superquants-productionization/scripts/validate_production_handoff.py': 'superquants-productionization/assets/templates/production-handoff-template.md',
    'superquants-live-review/scripts/validate_live_review.py': 'superquants-live-review/assets/templates/live-review-template.md',
    'superquants-live-review/scripts/validate_post_mortem.py': 'superquants-live-review/assets/templates/post-mortem-template.md',
    'superquants-triage/scripts/validate_triage_note.py': 'superquants-triage/assets/templates/triage-note-template.md',
}

KNOWN_PLACEHOLDERS = {'date', 'slug', 'topic_title', 'strategy_slug', 'experiment_name', 'experiment_slug'}


def normalize_heading(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r'[^a-z0-9]+', ' ', value)
    return re.sub(r'\s+', ' ', value).strip()


def extract_headings(text: str) -> set[str]:
    return {normalize_heading(h) for h in re.findall(r'^#{1,6}\s+(.+?)\s*$', text, flags=re.MULTILINE)}


def extract_required(validator_text: str) -> list[str]:
    block = re.search(r'REQUIRED_HEADINGS\s*=\s*\[(.*?)\]', validator_text, flags=re.DOTALL)
    if not block:
        return []
    return re.findall(r"'([^']+)'", block.group(1))


def check() -> list[str]:
    errors: list[str] = []
    skills = sorted(p for p in SOURCE.iterdir() if p.is_dir())

    for skill in skills:
        skill_md = skill / 'SKILL.md'
        if not skill_md.exists():
            errors.append(f'{skill.name}: missing SKILL.md')
            continue
        text = skill_md.read_text(encoding='utf-8')

        front = re.match(r'^---\n(.*?)\n---\n', text, flags=re.DOTALL)
        if not front:
            errors.append(f'{skill.name}: SKILL.md has no frontmatter')
        else:
            name = re.search(r'^name:\s*(\S+)\s*$', front.group(1), flags=re.MULTILINE)
            desc = re.search(r'^description:\s*\S+', front.group(1), flags=re.MULTILINE)
            if not name or name.group(1) != skill.name:
                errors.append(f'{skill.name}: frontmatter name does not match directory name')
            if not desc:
                errors.append(f'{skill.name}: frontmatter missing description')

        for rel in re.findall(r'`((?:scripts|references|assets)/[^`]+)`', text):
            if not (skill / rel).exists():
                errors.append(f'{skill.name}: SKILL.md references missing file {rel}')

        for template in skill.glob('assets/templates/*.md'):
            unknown = set(re.findall(r'\{\{([^}]+)\}\}', template.read_text(encoding='utf-8'))) - KNOWN_PLACEHOLDERS
            if unknown:
                errors.append(f'{skill.name}: {template.name} has unknown placeholders {sorted(unknown)}')

    for validator_rel, template_rel in VALIDATOR_TEMPLATE_PAIRS.items():
        validator, template = SOURCE / validator_rel, SOURCE / template_rel
        if not validator.exists() or not template.exists():
            errors.append(f'pair missing on disk: {validator_rel} / {template_rel}')
            continue
        required = extract_required(validator.read_text(encoding='utf-8'))
        if not required:
            errors.append(f'{validator_rel}: could not extract REQUIRED_HEADINGS')
            continue
        headings = extract_headings(template.read_text(encoding='utf-8'))
        for item in required:
            if normalize_heading(item) not in headings:
                errors.append(f'{validator_rel}: required heading "{item}" not found in {template.name}')

    validators = {Path(k).name.replace('validate_', '').replace('.py', '') for k in VALIDATOR_TEMPLATE_PAIRS}
    for validator in SOURCE.glob('*/scripts/validate_*.py'):
        stem = validator.name.replace('validate_', '').replace('.py', '')
        if stem not in validators:
            errors.append(f'{validator}: validator not registered in VALIDATOR_TEMPLATE_PAIRS')

    return errors


def sync() -> None:
    if PLUGIN_SKILLS.exists():
        shutil.rmtree(PLUGIN_SKILLS)
    shutil.copytree(SOURCE, PLUGIN_SKILLS, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    print(f'Synced {SOURCE} -> {PLUGIN_SKILLS}')


def package() -> None:
    for skill in sorted(p for p in SOURCE.iterdir() if p.is_dir()):
        out_dir = PACKAGES / skill.name
        out_dir.mkdir(parents=True, exist_ok=True)
        zip_path = out_dir / 'skill.zip'
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for file in sorted(skill.rglob('*')):
                if file.is_file() and '__pycache__' not in file.parts and file.suffix != '.pyc':
                    zf.write(file, f'{skill.name}/{file.relative_to(skill).as_posix()}')
        print(f'Packaged {zip_path}')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only', action='store_true', help='Run consistency checks without syncing or packaging.')
    args = parser.parse_args()

    errors = check()
    if errors:
        print('Consistency check FAILED:')
        for error in errors:
            print(f'- {error}')
        return 1
    print(f'Consistency check passed for {len(list(SOURCE.iterdir()))} skills.')

    if not args.check_only:
        sync()
        package()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
