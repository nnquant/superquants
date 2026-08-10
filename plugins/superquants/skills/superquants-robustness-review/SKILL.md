---
name: superquants-robustness-review
description: use when a quantitative strategy or experiment looks promising and needs to be challenged before promotion. establishes the selection history and applies multiplicity discipline, tests out-of-sample behavior, cost sensitivity, parameter stability, regime dependence, concentration, capacity, exposures, crowding, and reproducibility, runs an adversarial red-team pass producing a null story and pre-mortem, weighs marginal portfolio contribution, and ends in promote with sizing, iterate against a budget, or archive with cause of death.
---

# Superquants Robustness Review

Use this skill once a strategy has some positive evidence and the question becomes whether it deserves more trust. At the start of a qualifying task, say you are using the Superquants Robustness Review skill.

Read the research spec, data audit, experiment plan, experiment logs, plots, and current implementation before judging robustness. If the evidence packet is incomplete or ambiguous, ask one question per message until the key assumptions are explicit.

Do not recommend productionization from a single pretty backtest or a loosely documented notebook. And do not score any evidence whose selection history is unknown: a result's meaning depends on how many siblings died for it.

## Checklist

1. Read the evidence packet.
   - spec, audit, plan, logs, code, tests, plots, and any previous review memos
   - the trial registry entries and selection history for this strategy family
   - the current program haircut from `research/superquants/calibration-ledger.md` when it exists
2. Restate the claim under review in one sentence.
   - what exactly is supposed to work?
3. Ask clarifying questions one at a time.
   - resolve cost assumptions, parameter-selection logic, selection history, benchmark choice, capacity assumptions, and reproducibility gaps
4. Establish the selection history before judging any evidence.
   - how many candidates, variants, quick looks, and hyperparameter settings preceded this result
   - for mined families, demand the family metadata: family id, counts, selection rule, holdout status
   - apply multiplicity discipline per `references/multiplicity-and-batch-review.md`; a result with an unreconstructable selection history is not reviewable
5. Challenge the claim across the review matrix.
   - selection history and multiplicity
   - out-of-sample behavior
   - cost sensitivity
   - parameter sensitivity
   - regime or subperiod behavior
   - crowding and competition
   - concentration and capacity
   - exposure decomposition
   - mechanism discrimination
   - marginal portfolio contribution
   - operational realism and reproducibility
6. Run the red-team pass.
   - an independent reviewer - a subagent when available, otherwise a separate pass after an explicit role switch - receives the evidence packet without the researcher's interpretation sections
   - deliverables per `references/red-team-protocol.md`: the strongest null story, a pre-mortem, and the cheapest checks that would separate them from the alpha story
   - the memo must answer the null story with evidence; an unanswered null story blocks promotion
7. Write the review memo.
   - Save to `research/superquants/reviews/YYYY-MM-DD-<slug>-review-memo.md`.
   - Use `scripts/new_review_memo.py` when files are available.
8. Record the review matrix.
   - Use `scripts/new_robustness_matrix.py` to scaffold the table when a written record of checks helps.
9. Self-review the memo.
   - Use `scripts/validate_review_memo.py` when available.
10. Make a decision.
    - promote: evidence is strong enough to plan rollout; state the initial size and the marginal contribution to the existing book, with the program haircut applied to expected performance
    - iterate: promising but missing crucial validation; name the missing evidence and consume one unit of the family's iteration budget - default three per family; when the budget is exhausted, the default becomes archive
    - archive: evidence is too weak or fragile; record the idea and its cause of death in `research/superquants/archive/INDEX.md`
11. Transition.
    - Only after a promote decision should the next default skill be superquants-productionization; once deployed, recurring superquants-live-review sessions take over.
    - If the issue is a bug or accounting mismatch, switch to superquants-strategy-debugging.

## Review Rules

- Distinguish predictive evidence from portfolio construction evidence.
- Distinguish in-sample success from out-of-sample stability.
- Distinguish statistical significance from economic significance after costs and constraints.
- Judge the family, not the lucky member: best-of-N changes what every number means.
- Genuine adversarialism needs role separation; a checklist self-review is necessary but not sufficient.
- Treat reproducibility as part of robustness, not a separate convenience issue.
- The iteration budget exists because sunk cost compounds: iterating forever is archiving in denial.
- When the evidence is mixed, say so explicitly.

## Output Standard

A finished review memo should usually contain:

- scope reviewed
- claim under review
- evidence for
- evidence against
- strongest null story
- pre-mortem
- robustness checks
- reproducibility
- portfolio fit and sizing
- remaining risks
- recommendation
- next action

## Resources

- `scripts/new_review_memo.py`: scaffold the review memo at the canonical location
- `scripts/new_robustness_matrix.py`: scaffold the robustness matrix next to the reviews
- `scripts/validate_review_memo.py`: verify required memo sections exist
- `references/robustness-matrix.md`: the default checklist of robustness dimensions and questions
- `references/multiplicity-and-batch-review.md`: selection history, trial counting, haircuts, and reviewing mined candidate families
- `references/red-team-protocol.md`: role-separated adversarial pass - null story, pre-mortem, and falsification checks
- `references/red-flags.md`: common failure patterns that should block promotion
- `assets/templates/review-memo-template.md`: default review memo structure
- `assets/templates/robustness-matrix-template.md`: table structure for recording robustness checks
