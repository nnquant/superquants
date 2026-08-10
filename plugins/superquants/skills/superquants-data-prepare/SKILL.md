---
name: superquants-data-prepare
description: use after a quantitative research spec exists and before trusting datasets, feature tables, labels, or backtests. audits point-in-time correctness, universe formation, timestamps, joins, transforms, leakage, and operational assumptions through targeted dialogue and a written data audit; blocks experimentation until the audit passes or risks are explicitly accepted.
---

# Superquants Data Prepare

Use this skill after a research spec exists and before serious experimentation. At the start of a qualifying task, say you are using the Superquants Data Prepare skill.

Read the current research spec, existing data docs, sample rows, and any prior data audit before proposing feature engineering or backtests. If critical assumptions are missing, ask one question per message until the missing pieces are pinned down.

Do not engineer features, fit models, run a full backtest, or interpret strategy metrics until the data audit is marked pass or conditionally pass with the risks made explicit.

Quick looks run under superquants-triage may precede a full audit, but their outputs are quarantined: nothing computed from unaudited data may be cited as evidence in any downstream artifact.

## Checklist

1. Read the approved research spec first.
   - Reconstruct the decision time, forecast horizon, benchmark, and operational constraints.
2. Inspect the current data state.
   - Raw sources, vendor snapshots, data contracts, sample rows, joins, and transforms.
3. Ask clarifying questions one at a time.
   - Resolve missing details around timestamps, universe membership, splits, rolls, borrow, latency, and imputation.
4. Build a dataset inventory.
   - Separate raw inputs, derived features, labels, and execution or market data.
5. Audit point-in-time correctness.
   - Universe membership
   - corporate actions and rolls
   - delayed availability of fundamentals or alternative data
   - joins and forward fills
   - timezone and session boundary handling
6. Write the data audit.
   - Save to `research/superquants/data-audits/YYYY-MM-DD-<slug>-data-audit.md`.
   - Use `scripts/new_data_audit.py` when files are available.
7. Determine status.
   - pass: safe enough to start experiments
   - conditionally pass: can proceed only if named limitations are kept in scope
   - fail: block experimentation
8. Self-review the audit.
   - Use `scripts/validate_data_audit.py` if code execution is available.
9. Transition.
   - If the audit passes, the next default skill is superquants-experiment-planning.
   - If the audit fails, stay here and repair assumptions before moving on.

## Minimum Questions To Resolve

Before a data audit can pass, the skill should be able to answer:

- What is the exact decision timestamp?
- Which assets are eligible at each point in time?
- How are delistings, symbol changes, splits, dividends, futures rolls, or contract changes handled?
- Which fields arrive late relative to the decision timestamp?
- Which transforms could leak future information through normalization, winsorization, imputation, or lookups?
- What chronological validation scheme avoids overlap leakage?

## Audit Guidance

Separate these layers explicitly:

1. raw source trustworthiness
2. timestamp alignment
3. universe formation
4. transforms and feature engineering
5. label construction
6. validation split design

Do not compress them into one vague statement like "data looks fine".

When uncertainty remains, bias toward documenting the limitation rather than hand-waving it away.

## Output Standard

A finished data audit should usually contain:

- sources and snapshots
- decision time
- universe formation
- timestamp alignment
- corporate actions and rolls
- missing data and imputation
- feature engineering risks
- leakage risks
- validation split design
- status
- blocking questions

## Resources

- `scripts/new_data_audit.py`: scaffold a data audit at the canonical location
- `scripts/new_dataset_inventory.py`: scaffold a dataset inventory alongside the audit
- `scripts/validate_data_audit.py`: verify the required sections exist before sign-off
- `references/leakage-checklist.md`: point-in-time, leakage, and validation checks
- `references/data-shaping-guide.md`: how to discuss joins, transforms, and missingness clearly
- `assets/templates/data-audit-template.md`: default audit structure
- `assets/templates/dataset-inventory-template.md`: default structure for enumerating raw and derived datasets
