---
name: superquants-productionization
description: use only after a quantitative strategy has passed robustness review and is being prepared for real operation. turns an approved research result into modules, configs, jobs, monitoring, shadow rollout, rollback criteria, pre-committed statistical decay triggers, and operating runbooks through targeted questions and a written production handoff before implementation.
---

# Superquants Productionization

Use this skill when the strategy is approved in principle and the work becomes operationalization. At the start of a qualifying task, say you are using the Superquants Productionization skill.

Read the latest research design, data audit, experiment plan, review memo, current codebase, and operating context before proposing architecture changes. If operational assumptions are incomplete, ask only decision-changing questions. Use the environment's native structured-question tool when available and group up to three related questions in one round; otherwise state reasonable defaults and ask only the blocker that cannot be safely inferred. Do not conduct a serial survey.

Do not move a strategy toward live use based only on research notebooks. Freeze assumptions and define operating controls first.

## Checklist

1. Read the approval packet.
   - research brief or spec
   - data audit
   - latest experiment or validation logs
   - review memo with promote decision
   - codebase and existing ops tooling
2. Resolve material operational blockers in a compact question round.
   - group only unresolved trading-window, data-SLA, latency, risk-control, ownership, incident, or rollback details that change the production contract
3. Freeze the research contract.
   - formulae
   - config
   - benchmark
   - cost assumptions
   - data dependencies
4. Define the production shape.
   - reusable modules instead of notebook state
   - externalized config
   - deterministic jobs and scheduling
   - monitoring and alerts
   - statistical decay triggers derived from the backtest distribution, pre-committed for superquants-live-review
   - shadow mode and rollout criteria
   - rollback triggers and incident workflow
5. Write the production handoff.
   - Save to `research/superquants/production/YYYY-MM-DD-<slug>-production-handoff.md`.
   - Use `scripts/new_production_handoff.py` when files are available.
6. Create the runbook.
   - Use `scripts/new_runbook.py` to scaffold it at the canonical location.
7. Self-review the handoff.
   - Use `scripts/validate_production_handoff.py` when available.
8. Transition.
   - Only after the handoff is complete should implementation begin.
   - After rollout, schedule recurring superquants-live-review sessions; the first is due at the end of the shadow period.
   - If rollout confidence weakens because the evidence is not robust enough, return to superquants-robustness-review.

## Production Rules

- Preserve a clear boundary between research logic and runtime infrastructure.
- Freeze anything that changes expected economics before rollout.
- Instrument missing-data, drift, turnover, exposure, slippage, and order-failure monitoring before trusting live operation.
- Pre-commit statistical decay triggers before launch; post-hoc thresholds always rationalize continuing.
- Require shadow mode or staged rollout unless the user explicitly chooses otherwise.
- Make rollback triggers explicit before launch.

## Output Standard

A finished production handoff should usually contain:

- strategy summary
- frozen assumptions
- system boundaries
- runtime dependencies
- monitoring and alerts
- statistical decay triggers
- shadow mode
- rollout criteria
- rollback triggers
- runbook
- open risks

## Resources

- `scripts/new_production_handoff.py`: scaffold the production handoff at the canonical location
- `scripts/new_runbook.py`: scaffold the operator runbook next to the handoffs
- `scripts/validate_production_handoff.py`: verify required handoff sections exist
- `references/operating-model-checklist.md`: default questions about ownership, controls, and rollout
- `references/monitoring-metrics.md`: common live metrics and alert ideas for quant systems
- `assets/templates/production-handoff-template.md`: default handoff structure
- `assets/templates/runbook-template.md`: default operator runbook structure
