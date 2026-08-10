# Triage Discipline

## Why Quarantine Exists

Quick looks are the primary source of silent multiple testing in a research program: twenty crude backtests before lunch, the best one remembered, the rest forgotten. By the time the survivor reaches a formal review, its selection history has evaporated and the review overrates it. Triage legalizes the quick look by converting it into accounting: every look is logged, and no look is evidence.

## Timebox Tiers

- T0, up to an hour: desk check only. Does the data exist at usable quality? Is there a structural reason the idea cannot work - capacity, borrow, latency, licensing? No backtest.
- T1, up to half a day: one crude cut. One default configuration chosen before looking, one pre-named metric, simplest usable data.
- Longer than T1 means the idea deserves a spec. Stop and write one.

## The No-Tuning Rule

Tuning inside triage is untracked multiplicity in its purest form. One configuration, chosen before looking. If a second configuration is genuinely necessary, it is a second trial: log it. A third configuration means research is happening without a spec - stop.

## What a Triage Verdict May Conclude

- allowed: "worth a spec", "dead: no usable data before 2019", "dead: capacity below minimum size", "dead: killed in 2025 for cost reasons and nothing has changed"
- never: "works", "Sharpe 1.4", or any quarantined number quoted as evidence downstream

The clean pipeline recomputes everything under pre-committed metrics. If an idea is only attractive because of its quarantined number, it has no spec-worthy mechanism - that is itself a drop signal.

## Batch and Mining Interface

A factor-mining run enters triage as a family, not as N independent discoveries:

- log one registry line per family: family id, N generated, N evaluated, selection rule, evaluation metric, holdout status
- graduate at most a handful of candidates per family into specs; log the rest as dropped members of the family
- the family metadata travels with every survivor into superquants-robustness-review, which judges the family's selection history, not the lucky member alone
- if the mining tool keeps its own logs, link them from the registry line; the registry stores the summary

## Graduation Rules

- open superquants-brainstorms; the spec commits metrics, kill criteria, and promotion criteria before any clean rerun
- link the triage note from the spec's open questions or context, marked quarantined
- the clean pipeline must remain able to falsify the idea even though triage liked it; if the spec cannot name a kill criterion, the graduation was premature
