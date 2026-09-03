# Superquants Multi-Skill Suite

This bundle splits Superquants into nine composable skills, inspired by the workflow style of obra/superpowers, forming a closed-loop quant research process: ideas are screened, specified at an appropriate depth, audited, tested, reported with selected evidence, challenged, productionized, and then measured live - with live results calibrating the next round of research.

## Skill Order

0. superquants-triage (optional entry)
   - use to screen raw ideas or mined candidate batches cheaply, under quarantine rules
   - output: trial registry entries and triage notes; verdict drop or graduate
1. superquants-brainstorms
   - use for material new strategy research or factor ideation after routing direct answers and quick checks to lighter modes
   - output: a compact research brief or full research spec, sized to ambiguity and consequence
2. superquants-data-prepare
   - use after the approved research brief or spec and before trusting data
   - output: data audit
3. superquants-experiment-planning
   - use after an approved research design and data audit exist
   - output: experiment plan (starting at experiment zero, the power check) and experiment logs with selection history, outcome classification, prediction review, failure learning, and a separate justified follow-up decision
4. superquants-result-reporting
   - use when presenting experiment, factor, backtest, diagnostic, robustness, or live results
   - output: an inline closeout or reusable report assembled from only the relevant evidence modules; non-pass outcomes add failure learning, while no full chart pack is required by default
5. superquants-strategy-debugging
   - use when results look wrong or live diverges from research
   - output: diagnosis memo
6. superquants-robustness-review
   - use when the strategy looks promising and needs challenge before promotion
   - output: review memo (with null story, pre-mortem, portfolio fit) and robustness matrix; promote, iterate against a budget, or archive
7. superquants-productionization
   - use only after review recommends promotion
   - output: production handoff with pre-committed statistical decay triggers, and runbook
8. superquants-live-review
   - use on a recurring basis once a strategy runs in shadow or live
   - output: live review memos, calibration ledger updates, and post-mortems on retirement

## Shared Canonical Paths

- `research/superquants/triage/`
- `research/superquants/specs/`
- `research/superquants/data-audits/`
- `research/superquants/plans/`
- `research/superquants/experiments/`
- `research/superquants/reports/`
- `research/superquants/diagnoses/`
- `research/superquants/reviews/`
- `research/superquants/production/`
- `research/superquants/live-reviews/`
- `research/superquants/archive/` (post-mortems and `INDEX.md`, the graveyard of killed ideas)
- `research/superquants/trial-registry.md` (program-wide multiplicity ledger)
- `research/superquants/calibration-ledger.md` (expected-versus-realized feedback loop)

## Design Principles

- use the lightest research mode that protects the decision: direct answer, quick check, compact design, or full design
- infer from project evidence first; in research design, group up to three decision-changing questions per interaction, use the native structured-question tool when available and the same small batch in ordinary messages otherwise, and continue without a fixed round cap until material choices are resolved or explicitly accepted as assumptions
- write the artifact before claiming progress
- select result-report modules by the claim and decision; templates are reusable options, not a requirement to emit every chart or table
- an experiment may legitimately end in `fail`; do not end its closeout at that one word: classify validity, compare prediction with observation, localize the failure, state what was learned, and separately choose iterate, debug, gather evidence, or archive with no further experiment
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
