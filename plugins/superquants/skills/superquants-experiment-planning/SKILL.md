---
name: superquants-experiment-planning
description: use after an approved quantitative research brief or spec and trustworthy data audit exist. breaks strategy implementation into bite-sized experiments with exact files, tests, baselines, predictions, and experiment logs; asks only decision-changing questions before execution and blocks large backtests or broad parameter sweeps until the design passes a statistical power check and the smallest verifiable slice is planned.
---

# Superquants Experiment Planning

Use this skill once the research question and data assumptions are stable enough to plan implementation. At the start of a qualifying task, say you are using the Superquants Experiment Planning skill.

Read the approved research brief or spec and data audit before proposing code, notebooks, experiments, or backtests. If the research packet is incomplete, ask only decision-changing questions. Use the environment's native structured-question tool when available and group up to three related questions in one round; otherwise state reasonable defaults and ask only the blocker that cannot be safely inferred. Do not conduct a serial survey.

Do not jump to a full-history backtest, giant parameter sweep, or production build. Start with the smallest vertical slice that can falsify the idea.

## Checklist

1. Read the current research packet.
   - research brief or spec
   - data audit
   - existing code or notebooks
   - prior experiment logs and plots
2. Restate the current objective in one sentence.
   - What decision should the next experiment change?
3. Resolve material blockers in a compact question round.
   - Group only the missing details that can change baselines, benchmarks, costs, lagging, or operational constraints.
4. Design the experiment ladder.
   - experiment zero: power and falsifiability check - can this design distinguish the claimed effect from noise at all?
   - baseline or null comparison
   - smallest vertical slice
   - medium-confidence sanity run
   - full-history or broader-scale run
5. Write the implementation and experiment plan.
   - Save to `research/superquants/plans/YYYY-MM-DD-<slug>-experiment-plan.md`.
   - Use `scripts/new_experiment_plan.py` to scaffold it.
6. Plan the first experiment log before execution.
   - Use `scripts/new_experiment_log.py`.
   - Log the exact change, config, costs, date span, and interpretation.
   - Record the running selection history: how many variants of this family have been tried, including triage looks, mined candidates, and hyperparameter settings.
   - Write the predicted result before running; predictions calibrate the researcher and expose hindsight bias.
7. Require targeted verification before scale.
   - feature alignment tests
   - lag correctness tests
   - position or order conservation checks
   - cost arithmetic checks
   - benchmark math checks
8. Self-review the plan.
   - Use `scripts/validate_experiment_plan.py` and `scripts/validate_experiment_log.py` when available.
9. Transition.
   - Execute the plan only after it is concrete enough that another agent could follow it without guessing.
   - When presenting completed results, use superquants-result-reporting to select the smallest useful set of report modules; do not generate every available chart by default.
   - If results later look suspicious or inconsistent, move to superquants-strategy-debugging.

## Planning Rules

- Every planned experiment should answer one question.
- Prefer a minimal falsification path over maximal complexity.
- Keep predictive validation separate from portfolio or execution validation.
- Document the baseline that each experiment must beat.
- Treat cost assumptions as part of the experiment definition, not an afterthought.
- State stop conditions up front so the user knows when to promote, iterate, or archive.
- Metrics are frozen in the approved research design before the first backtest; a metric added after seeing results is exploratory - label it and amend the design.
- Every variant counts toward the selection history, including the ones that will not be reported.

## Output Standard

A finished experiment plan should usually contain:

- goal
- current context
- experiment ladder
- files to create or modify
- targeted verification strategy
- stop conditions
- open questions

A finished experiment log should usually contain:

- summary
- objective
- hypothesis
- data snapshot
- implementation
- portfolio and execution mapping
- costs and constraints
- results
- selected result evidence and artifact paths appropriate to the experiment
- interpretation
- next step
- reproducibility

## Resources

- `scripts/new_experiment_plan.py`: scaffold the implementation and experiment plan
- `scripts/validate_experiment_plan.py`: verify required plan sections exist
- `scripts/new_experiment_log.py`: scaffold a new experiment log
- `scripts/validate_experiment_log.py`: verify required log sections exist
- `references/planning-patterns.md`: patterns for smallest-slice planning, power checks, metric freeze, and baseline-first design
- `references/metrics-guide.md`: choose metrics by strategy type, with multiplicity context
- `references/label-engineering.md`: designing the prediction target - horizons, residualization, and label pitfalls
- `references/cost-model-guide.md`: building and validating transaction cost assumptions
- `references/portfolio-construction-guide.md`: mapping signals to positions without destroying the edge
- `references/ml-validation-guide.md`: validation discipline for machine-learning strategies
- `assets/templates/experiment-plan-template.md`: default experiment plan structure
- `assets/templates/experiment-log-template.md`: default experiment log structure
