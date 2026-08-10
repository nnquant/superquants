---
name: superquants-brainstorms
description: use before any quantitative strategy ideation, factor research, alpha thesis, or new backtest design. turns vague trading ideas into an approved research spec through one-question-at-a-time dialogue, alternative comparison, and section-by-section validation. checks the trial registry and archive for prior attempts, and commits metrics, statistical power budget, promotion criteria, and kill criteria in writing before any data prep, backtest, notebook work, or code.
---

# Superquants Brainstorms

Help turn rough quant ideas into approved research specs.

At the start of a qualifying task, say you are using the Superquants Brainstorms skill. Then inspect any existing research artifacts, notebooks, docs, logs, or plots before asking detailed questions.

Do not invoke superquants-data-prepare, superquants-experiment-planning, write code, suggest a full backtest, or take implementation action until a written research spec has been presented and approved. This rule applies even when the idea sounds simple.

## Checklist

Complete these items in order:

1. Explore context.
   - Read the current project state first: specs, notebooks, experiment logs, plots, docs, and prior code.
   - Check `research/superquants/trial-registry.md` and `research/superquants/archive/INDEX.md` for prior attempts at this idea family; a previously killed idea needs a stated reason why now is different.
   - If the user already has a strategy draft, reconstruct the research claim before asking new questions.
2. Assess scope.
   - If the request actually contains multiple unrelated ideas, decompose them before refining details.
   - Each independent strategy idea gets its own spec.
3. Ask clarifying questions one at a time.
   - Prefer multiple-choice questions when possible.
   - Only one question per message.
   - Use questions to pin down purpose, instrument set, horizon, benchmark, constraints, and success criteria.
4. Propose 2-3 research paths.
   - For each path, explain the mechanism, required data, likely failure modes, and implementation cost.
   - Lead with your recommended path and explain why.
5. Present the design in sections.
   - After each section, ask whether it looks right so far.
   - Cover the objective, research claim, economic mechanism, universe, timing rules, portfolio mapping, benchmarks, validation design, and kill criteria.
6. Write the research spec.
   - Save to `research/superquants/specs/YYYY-MM-DD-<slug>-research-spec.md` when files are available.
   - Use `scripts/new_research_spec.py` to scaffold the file when code execution is available.
7. Self-review the spec.
   - Remove placeholders.
   - Check for contradictions, hidden future information, missing cost assumptions, and fuzzy success criteria.
8. Ask the user to review the written spec.
   - Do not move to data or implementation until the user approves.
9. Transition.
   - After approval, the next default skill is superquants-data-prepare.
   - Skip directly to superquants-experiment-planning only if the user already has a trustworthy data audit.
   - Ideas arriving from superquants-triage keep their quick-look numbers quarantined: the spec's metrics, promotion criteria, and kill criteria are committed before any clean rerun.

## Questions To Resolve Before Approval

Always resolve these topics before approving a spec:

- What decision should the research inform?
- What is the exact asset universe and how is it formed over time?
- What frequency matters: intraday, daily, weekly, event-driven, or mixed?
- What is the hypothesis and why should the edge exist economically?
- What benchmark or baseline should the work beat?
- What constraints matter: liquidity, leverage, borrow, risk limits, turnover, capacity, tax, compliance, or operations?
- How many effectively independent observations will the evaluation have, and is the claimed effect detectable at that sample size?
- Who else can see this edge, why does it survive competition, and how fast is it expected to decay?
- What pre-committed evidence would justify promotion, and at what initial size?
- What would falsify the idea quickly?

## Design Guidance

Good quant specs separate four objects clearly:

1. Research claim - what should be predictable or improvable.
2. Measurement design - how the claim will be evaluated without leakage.
3. Portfolio mapping - how a signal becomes weights, positions, or orders.
4. Operational assumptions - what costs, latency, and market frictions apply.

Do not blur these together. A predictive signal can still fail as a portfolio once costs and constraints are applied.

If the user is unsure which direction to take, explore alternatives such as:

- cross-sectional ranking vs time-series timing
- simple transparent baseline vs more complex model
- slower lower-turnover expression vs faster higher-turnover expression

## Output Standard

A finished research spec should usually contain:

- objective
- research claim
- economic mechanism
- expected decay and competition
- universe and sampling rules
- data and timestamp rules
- signal or decision rule
- portfolio and execution mapping
- benchmarks and metrics
- validation design
- statistical power budget
- promotion criteria
- kill criteria
- open questions

## Resources

- `scripts/new_research_spec.py`: scaffold a research spec at the canonical location
- `scripts/new_approach_comparison.py`: scaffold an approach comparison next to the specs
- `scripts/validate_research_spec.py`: verify the required sections exist before sign-off
- `references/question-bank.md`: targeted questions by strategy type and research phase
- `references/spec-patterns.md`: examples of strong vs weak research claims and kill criteria
- `assets/templates/research-spec-template.md`: default spec structure
- `assets/templates/approach-comparison-template.md`: default structure for comparing 2-3 research directions
