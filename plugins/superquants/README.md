# Superquants Plugin

This plugin packages the Superquants workflow as a repo-local Codex plugin.

Included skills:

1. `superquants-triage`
2. `superquants-brainstorms`
3. `superquants-data-prepare`
4. `superquants-experiment-planning`
5. `superquants-result-reporting`
6. `superquants-strategy-debugging`
7. `superquants-robustness-review`
8. `superquants-productionization`
9. `superquants-live-review`

Plugin root:

- `plugins/superquants/.codex-plugin/plugin.json`
- `plugins/superquants/skills/`

Marketplace entry:

- `.agents/plugins/marketplace.json`

Notes:

- The plugin is wired for repo-local installation through the marketplace entry.
- Author, repository, homepage, and policy URLs remain TODO placeholders for you to fill.
- Asset paths are present in the manifest but no branded images are included yet.
- `plugins/superquants/skills/` is generated from `source/` by `tools/build.py`; edit `source/` and rebuild rather than editing here.
