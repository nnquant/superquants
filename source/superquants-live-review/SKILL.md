---
name: superquants-live-review
description: use when a promoted quantitative strategy is running in shadow or live and needs research-level review rather than ops monitoring. reconciles live results against backtest expectations, checks pre-committed decay triggers, attributes divergence across bug, data, costs, regime, crowding, and residual decay, updates the calibration ledger that scores the research process itself, and decides continue, resize, re-fit, or retire with a post-mortem on retirement.
---

# Superquants Live Review

Use this skill once a strategy is deployed in shadow or live and the question becomes whether reality matches the research. At the start of a qualifying task, say you are using the Superquants Live Review skill.

Read the research spec, review memo, production handoff, prior live reviews, calibration ledger, and live performance records before judging anything. If live records are incomplete, ask one question per message until the reconciliation inputs are pinned down.

Do not conclude alpha decay, resize, or retire from a raw pnl chart. Reconcile first, attribute second, decide third. And do not let a strategy run indefinitely without a scheduled review: unmeasured live performance is unfinished research.

## Checklist

1. Read the strategy packet.
   - research spec: expected economics, decay expectations, promotion criteria
   - review memo: promotion rationale and initial sizing
   - production handoff: frozen assumptions and pre-committed statistical decay triggers
   - prior live reviews and `research/superquants/calibration-ledger.md`
   - live records: returns, positions, fills, costs, exposures, incidents
2. Restate the expectation in one sentence.
   - What did the research promise, net of costs, at what sizing?
3. Ask clarifying questions one at a time.
   - resolve live data completeness, config drift, cost and fill records, and the review window
4. Reconcile live against research.
   - run or request a same-period simulation under the frozen research assumptions
   - compare net returns, turnover, exposures, costs, and hit patterns on the same calendar and the same conventions
5. Attribute the divergence in this order.
   - suspected bug or broken invariant: switch to superquants-strategy-debugging before any other conclusion
   - data differences: revisions, delays, universe drift
   - execution and costs: slippage, fills, borrow versus assumptions
   - regime or exposure shift: is the environment outside the researched envelope?
   - crowding: rising correlation to peers, unwind behavior
   - residual alpha decay: only after everything above is excluded
6. Check the pre-committed decay triggers.
   - evaluate each trigger from the handoff against live statistics
   - a fired trigger forces a decision; it does not force retirement
7. Update the calibration ledger.
   - record expected-versus-realized ratios for this strategy
   - re-read the program-level ratios: is the research process systematically overpromising? carry the current haircut into future promotion reviews
8. Write the live review memo.
   - Save to `research/superquants/live-reviews/YYYY-MM-DD-<slug>-live-review.md`.
   - Use `scripts/new_live_review.py` when files are available.
9. Self-review the memo.
   - Use `scripts/validate_live_review.py` when available.
10. Decide and transition.
    - continue: schedule the next review date in the memo
    - resize: record the new size and its rationale
    - re-fit or modify: any change to expected economics is new research; route through superquants-experiment-planning and re-review before redeploying
    - retire: write a post-mortem with `scripts/new_post_mortem.py`, record the cause of death and revival conditions in `research/superquants/archive/INDEX.md`, and feed the lessons into future triage and brainstorm priors

## Live Review Rules

- Compare like with like: net against net, same calendar, same benchmark, same conventions.
- Route suspected bugs to superquants-strategy-debugging before concluding decay.
- Pre-committed triggers outrank post-hoc stories; post-hoc thresholds always rationalize continuing.
- A re-fit that changes expected economics is a new promotion decision, not an operations tweak.
- Retirement is a normal outcome of a healthy process; an unrecorded death is the only process failure.
- Every live review must leave the calibration ledger more informative than before.

## Output Standard

A finished live review memo should usually contain:

- scope and period
- expectation summary
- live vs backtest reconciliation
- divergence attribution
- decay trigger status
- calibration update
- decision
- next action

A finished post-mortem should usually contain:

- strategy summary
- lifespan and realized economics
- cause of death
- what the process missed
- priors for future research
- revival conditions

## Resources

- `scripts/new_live_review.py`: scaffold a live review memo at the canonical location (seeds `research/superquants/calibration-ledger.md` on first use)
- `scripts/validate_live_review.py`: verify required memo sections exist
- `scripts/new_post_mortem.py`: scaffold a retirement post-mortem in the archive (seeds `research/superquants/archive/INDEX.md` on first use)
- `scripts/validate_post_mortem.py`: verify required post-mortem sections exist
- `references/decay-and-calibration.md`: pre-committed decay triggers, decay priors, attribution order, and calibration ledger mechanics
- `assets/templates/live-review-template.md`: default memo structure
- `assets/templates/post-mortem-template.md`: default post-mortem structure
- `assets/templates/calibration-ledger-template.md`: seed structure for the program-level calibration ledger
- `assets/templates/archive-index-template.md`: seed structure for the archive index of retired and killed ideas
