---
name: superquants-brainstorms
description: use when a new quantitative strategy or material research design needs its assumptions, metrics, validation, and stop criteria frozen before implementation. routes existing-result questions and timeboxed quick checks to lighter workflows, and chooses a compact research brief or full research spec according to ambiguity and consequence.
---

# Superquants Brainstorms

Help turn material quant ideas into an appropriately sized approved research design without making simple questions pay the cost of a full specification.

At the start of a qualifying task, say you are using the Superquants Brainstorms skill. Then inspect any existing research artifacts, notebooks, docs, logs, or plots before asking questions.

Use the lightest mode that protects the decision:

- direct answer: explain or compare existing evidence without creating a new experiment; answer from the available artifacts and do not create a spec
- quick check: one frozen configuration, no tuning, and a drop-or-graduate decision; route to superquants-triage
- compact design: one bounded hypothesis using familiar data and conventions, with no parameter search or live-capital decision; write a research brief
- full design: material ambiguity, new data or model classes, multiple variants, leverage or derivatives, broad validation, or production intent; write a full research spec

For compact and full designs, do not invoke superquants-data-prepare, superquants-experiment-planning, write research code, or run the backtest until the chosen design artifact has been presented and approved. Direct answers and quick checks follow their own lighter boundaries.

## Questioning Policy

- Infer answers from the project and prior artifacts before asking.
- Ask only questions whose answers would materially change the claim, universe, timing, benchmark, cost model, validation, or decision threshold.
- A question is required when two reasonable answers would lead to materially different data, labels, portfolio construction, costs, validation, or promotion decisions and project evidence does not select between them. Do not silently choose a consequential default merely to avoid asking.
- When the environment provides a native structured-question tool, such as `request_user_input` in Codex or `AskUserQuestion` in Claude, group up to three related questions per interaction and include a recommended option when useful.
- When that tool is unavailable, ask the same small batch in an ordinary message. Tool availability changes the presentation, not whether a material decision is put to the user.
- There is no fixed limit on question rounds. After each answer, update what is known, inferred, and still open; continue only while unresolved choices can change the design. Stop when the material choices are resolved or the user explicitly accepts the remaining stated assumptions.
- Zero question rounds are appropriate for direct answers, frozen quick checks, or compact/full designs whose material choices are already explicit or evidenced. Do not ask merely to fill a template field or reconfirm established facts.

## Checklist

Complete these items in order:

1. Explore context.
   - Read the current project state first: specs, notebooks, experiment logs, plots, docs, and prior code.
   - Check `research/superquants/trial-registry.md` and `research/superquants/archive/INDEX.md` for prior attempts at this idea family; a previously killed idea needs a stated reason why now is different.
   - If the user already has a strategy draft, reconstruct the research claim before asking new questions.
2. Assess scope.
   - If the request actually contains multiple unrelated ideas, decompose them before refining details.
   - Each independent strategy idea gets its own appropriately sized design artifact.
3. Resolve material decisions in compact question rounds.
   - Follow the Questioning Policy instead of asking every question in the bank.
   - Ask up to three related questions at a time, then reassess the design from the answers before asking more.
   - Continue for as many rounds as the complexity requires; do not present the consolidated design while a consequential choice remains unresolved unless the user explicitly accepts it as an assumption.
   - Record discoverable or safely defaulted details as assumptions for the consolidated review. If no questions were needed, make the material inferred choices visible there.
4. Compare research paths only when there is a genuine design choice.
   - If one path is clearly implied by the request and current project, recommend it directly.
   - Otherwise compare 2-3 paths by mechanism, data, failure modes, implementation cost, and fastest falsification.
5. Present one consolidated design.
   - Cover only the sections needed by the chosen mode.
   - Ask for one overall review; do not require section-by-section approval unless the user requests it.
6. Write the chosen artifact.
   - Compact: save `research/superquants/specs/YYYY-MM-DD-<slug>-research-brief.md` and use `scripts/new_research_brief.py`.
   - Full: save `research/superquants/specs/YYYY-MM-DD-<slug>-research-spec.md` and use `scripts/new_research_spec.py`.
7. Self-review the artifact.
   - Remove placeholders.
   - Check for contradictions, hidden future information, missing cost assumptions, and fuzzy success criteria.
   - Use the validator for the chosen mode when code execution is available.
8. Ask the user to review the written artifact once.
   - Do not move to data or implementation until the user approves.
9. Transition.
   - After approval, the next default skill is superquants-data-prepare.
   - Skip directly to superquants-experiment-planning only if the user already has a trustworthy data audit.
   - Ideas arriving from superquants-triage keep their quick-look numbers quarantined: the approved design commits metrics and stop criteria before any clean rerun.

## Questions To Resolve Before Approval

For a full spec, resolve the material parts of these topics before approval. For a compact brief, include only what can change the immediate experiment or its interpretation. Do not ask about items already established by the project:

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

A compact research brief should usually contain:

- decision to inform
- claim and mechanism
- scope and timing
- data and leakage guard
- baseline and metrics
- costs and constraints
- fast falsification rule
- assumptions and open questions

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
- `scripts/new_research_brief.py`: scaffold a compact research brief at the canonical location
- `scripts/new_approach_comparison.py`: scaffold an approach comparison next to the specs
- `scripts/validate_research_spec.py`: verify the required sections exist before sign-off
- `scripts/validate_research_brief.py`: verify the compact brief sections exist before sign-off
- `references/question-bank.md`: targeted questions by strategy type and research phase
- `references/spec-patterns.md`: examples of strong vs weak research claims and kill criteria
- `assets/templates/research-spec-template.md`: default spec structure
- `assets/templates/research-brief-template.md`: compact design structure
- `assets/templates/approach-comparison-template.md`: default structure for comparing 2-3 research directions
