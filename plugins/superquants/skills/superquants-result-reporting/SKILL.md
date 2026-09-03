---
name: superquants-result-reporting
description: use when presenting quantitative research, factor, backtest, robustness, diagnostic, or live-review results. selects only relevant metrics, charts, tables, and links, and pairs non-pass outcomes with causal evidence, learning, and a justified follow-up decision instead of treating the outcome label as the whole closeout.
---

# Superquants Result Reporting

Present quant results in the smallest form that makes the decision inspectable. This skill is a reporting step, not a new approval gate, and it does not authorize new experiments or parameter tuning.

At the start of a qualifying task, say you are using the Superquants Result Reporting skill. Read the result data, logs, plots, experiment or review record, and the user's requested decision before choosing report modules.

## Reporting Depth

Choose the lightest useful depth:

- inline: a status, narrow diagnostic, or small result that is clear from a few verified numbers and paths
- focused report: a completed experiment or backtest that benefits from a reusable report artifact and selected visuals
- decision closeout: a robustness, promotion, archive, or live decision that needs comparison evidence and reproducibility details

Do not create a report file or chart merely because a template exists. Do not omit evidence that is central to the claim merely to keep the report short.

## Module Selection

Read `references/result-modules.md` and choose only the modules that answer the current question:

- portfolio backtest
- factor evidence
- execution quality
- robustness
- live versus backtest
- diagnostic
- failure learning

A portfolio-return claim normally needs a NAV or cumulative-return view and drawdown context. A factor-predictiveness claim may be better served by IC and bucket evidence without a strategy NAV. A one-day diagnostic may need no performance chart. The user's explicit requested format takes priority.

Any non-pass result or material surprise requires the failure-learning module in addition to whatever evidence module supports the underlying claim. Inline reporting may present the same content compactly without creating a report file.

## Failure Learning

`Fail` may be the honest, final conclusion for the experiment. Before closeout, complete the feedback process:

- classify the experiment result as pass, fail (valid negative), invalid experiment, or inconclusive against the frozen criterion
- record the follow-up decision separately as promote, archive, debug, iterate, or gather evidence
- compare the pre-run prediction with the observed result
- localize the earliest divergence across statistical design, data, signal, portfolio, execution, evaluation, or operations
- distinguish what was falsified from what remains untested, and give evidence and confidence for the leading cause
- identify the specific assumption, test, or gate that should improve
- state the justified follow-up: either the smallest next action with expected information gain and a stop condition, or archive with no further experiment

Use already available logs, artifacts, and safe diagnostic slices proactively. This reporting skill does not authorize a new configuration, parameter search, wider dataset, or expensive rerun; those are new experiments and must be planned and counted. Route broken invariants or suspicious metrics to superquants-strategy-debugging. Do not relabel a valid fail as invalid or inconclusive. A fail that hits the pre-committed kill criterion should be archived rather than tuned, and no continuation is required.

## Chart Style

When newly rendering selected charts, preserve the active project's established visual conventions. If none are clear, read `references/oaks-chart-style.md` and use its Project Oaks-inspired hierarchy, palette, Chinese-font handling, and claim-specific layouts. It is a fallback theme, not a requirement to generate every listed chart or to add Project Oaks as a dependency.

## Checklist

1. Verify scope.
   - exact strategy or factor, configuration, benchmark, date range, data cutoff, sample count, and cost convention
2. Identify the decision.
   - what should the reader continue, reject, compare, debug, resize, or archive?
3. Select the smallest sufficient module set.
   - use available evidence; do not manufacture unused tables, empty CSVs, or irrelevant charts
4. Build the report.
   - for a focused report or closeout, use `scripts/new_quant_result_report.py` with only the selected modules
   - delete unused optional prompts and keep Chinese or domain-specific naming when it matches the project
5. Reconcile the evidence.
   - headline numbers must match machine-readable outputs and use the same window, benchmark, and cost convention
6. Close the learning loop for non-pass or surprising outcomes.
   - add the failure-learning module, identify why the result missed, what was learned, and the smallest justified next decision
   - never substitute generic suggestions for evidence about the actual failing layer
7. Present the result.
   - lead with the plain-language decision
   - show or link the selected charts and exact artifact paths
   - state material missing evidence instead of filling the gap with prose
8. Validate substantial report artifacts with `scripts/validate_quant_result_report.py`.

## Questioning Policy

Reporting should rarely require a question. Infer the requested format and conventions from existing outputs. If one missing choice would materially change interpretation, use the environment's native structured-question tool when available; otherwise ask only that blocker. Do not reopen the research design during reporting.

## Output Standard

For a focused report or decision closeout, retain these core sections:

- decision
- scope and data cutoff
- key metrics
- selected evidence
- interpretation and risks
- artifact index
- reproducibility

The contents inside selected evidence are modular. There is no requirement to return every template, chart, or table on every run.

## Resources

- `scripts/new_quant_result_report.py`: scaffold a report from the core template plus selected modules
- `scripts/validate_quant_result_report.py`: verify the core report sections exist
- `references/result-modules.md`: routing guidance for selecting evidence modules
- `references/oaks-chart-style.md`: optional Project Oaks-inspired visual fallback for newly rendered charts
- `assets/templates/quant-result-report-template.md`: reusable report core
- `assets/templates/module-backtest-template.md`: portfolio return, benchmark, excess return, drawdown, cost, and turnover options
- `assets/templates/module-factor-template.md`: IC, coverage, bucket, monotonicity, and turnover options
- `assets/templates/module-execution-template.md`: fill, slippage, shortfall, and adverse-selection options
- `assets/templates/module-robustness-template.md`: OOS, cost, parameter, regime, concentration, and reproducibility options
- `assets/templates/module-live-template.md`: same-period live-versus-backtest and decay-trigger options
- `assets/templates/module-diagnostic-template.md`: expected-versus-actual and minimal-failing-slice options
- `assets/templates/module-learning-template.md`: non-pass classification, failure analysis, process learning, and smallest next-action options
