#!/usr/bin/env python3
"""Shared helpers for Superquants result-reporting scripts."""

from __future__ import annotations

from datetime import date
from pathlib import Path
import re
from typing import Mapping


def today_iso() -> str:
    return date.today().isoformat()


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def templates_dir() -> Path:
    return skill_root() / 'assets' / 'templates'


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r'[^a-z0-9]+', '-', value)
    value = re.sub(r'-{2,}', '-', value).strip('-')
    if not value:
        raise ValueError('Could not derive a non-empty ASCII slug from the provided value. Non-ASCII titles need an explicit --slug.')
    return value


def title_from_slug(slug: str) -> str:
    return ' '.join(part.capitalize() for part in slug.split('-'))


def render_template(template_name: str, replacements: Mapping[str, str]) -> str:
    text = (templates_dir() / template_name).read_text(encoding='utf-8')
    for key, value in replacements.items():
        text = text.replace('{{' + key + '}}', value)
    return text


def write_text_file(path: Path, text: str, force: bool = False) -> None:
    if path.exists() and not force:
        raise FileExistsError(f'File already exists: {path}')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')
