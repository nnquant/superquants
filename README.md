# Superquants Multi-Skill Suite

This bundle splits Superquants into eight composable skills, inspired by the workflow style of obra/superpowers, forming a closed-loop quant research process: ideas are screened, specified, audited, tested, challenged, productionized, and then measured live - with live results calibrating the next round of research.

## Skill Order

0. superquants-triage (optional entry)
   - use to screen raw ideas or mined candidate batches cheaply, under quarantine rules
   - output: trial registry entries and triage notes; verdict drop or graduate
1. superquants-brainstorms
   - use before any new strategy research or factor ideation
   - output: research spec, with power budget, promotion criteria, and kill criteria pre-committed
2. superquants-data-prepare
   - use after the research spec and before trusting data
   - output: data audit
3. superquants-experiment-planning
   - use after spec and data audit exist
   - output: experiment plan (starting at experiment zero, the power check) and experiment logs with selection history
4. superquants-strategy-debugging
   - use when results look wrong or live diverges from research
   - output: diagnosis memo
5. superquants-robustness-review
   - use when the strategy looks promising and needs challenge before promotion
   - output: review memo (with null story, pre-mortem, portfolio fit) and robustness matrix; promote, iterate against a budget, or archive
6. superquants-productionization
   - use only after review recommends promotion
   - output: production handoff with pre-committed statistical decay triggers, and runbook
7. superquants-live-review
   - use on a recurring basis once a strategy runs in shadow or live
   - output: live review memos, calibration ledger updates, and post-mortems on retirement

## Shared Canonical Paths

- `research/superquants/triage/`
- `research/superquants/specs/`
- `research/superquants/data-audits/`
- `research/superquants/plans/`
- `research/superquants/experiments/`
- `research/superquants/diagnoses/`
- `research/superquants/reviews/`
- `research/superquants/production/`
- `research/superquants/live-reviews/`
- `research/superquants/archive/` (post-mortems and `INDEX.md`, the graveyard of killed ideas)
- `research/superquants/trial-registry.md` (program-wide multiplicity ledger)
- `research/superquants/calibration-ledger.md` (expected-versus-realized feedback loop)

## Design Principles

- clarify the strategy details before doing work
- ask one question per message when important assumptions are missing
- write the artifact before claiming progress
- keep predictive evidence, portfolio mapping, execution, and operations separate
- block the next phase until the current artifact is approved or passes validation
- every look counts: quick looks, mined candidates, and hyperparameter settings enter the trial registry, and reviews judge the family, not the lucky member
- quarantine: unaudited quick-look numbers are never evidence
- pre-commit the goalposts: metrics, promotion criteria, kill criteria, and decay triggers are written before results are seen
- adversarialism needs role separation: promotion requires an answered null story, not just a passed checklist
- close the loop: live results update the calibration ledger, retirements get post-mortems, and dead ideas stay findable in the archive

## Packaging Notes

Each subdirectory of `source/` is a standalone skill. `tools/build.py` syncs `source/` into `plugins/superquants/skills/`, rebuilds the `packages/<skill>/skill.zip` files, and verifies validator-template consistency plus SKILL.md resource links. Run it after any edit to `source/`.

## Installation

- Claude Code, plugin route: `/plugin marketplace add <repo-root>` (reads `.claude-plugin/marketplace.json`), then `/plugin install superquants@superquants-local`.
- Claude Code, direct route: `python tools/install.py` copies the skills into `~/.claude/skills/` (or `--project <path>` for a single project; `--remove` uninstalls).
- Codex: repo-local plugin via `.agents/plugins/marketplace.json` and `plugins/superquants/.codex-plugin/plugin.json`.
- claude.ai: upload the per-skill `packages/<skill>/skill.zip` files individually.
