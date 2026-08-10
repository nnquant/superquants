# Spec Patterns

## Strong vs Weak Research Claims

### Strong

"Among liquid US equities, stocks with improving analyst revision breadth over the prior 20 trading days should outperform peers over the next 5 trading days after sector-neutralization, but the effect may decay sharply after costs if turnover is too high."

Why this is strong:
- defines a universe
- states a mechanism candidate
- names a forecast horizon
- hints at a likely failure mode

### Weak

"Use analyst data to build a good signal for stocks."

Why this is weak:
- no universe
- no timing assumptions
- no mechanism
- no failure mode
- no measurable success criteria

## Strong Kill Criteria

Good kill criteria are explicit and cheap to evaluate.

Examples:
- archive if rank IC is near zero after a sector-neutral baseline and realistic lagging
- archive if net performance disappears after modest cost assumptions
- archive if the edge only appears in one narrow subperiod or tiny subset of names
- archive if the signal cannot be reproduced from point-in-time inputs

## Strong Promotion Criteria

Promotion criteria are written before the final results are seen - kill criteria in reverse. Pre-committing them is what prevents the goalposts from moving once a pretty backtest exists.

Example:

"promote if net Sharpe stays above 0.5 in both halves of the out-of-sample window, capacity supports the intended size at under 10 bps assumed impact, correlation to the existing book stays below 0.3, and the red-team null story has a written answer - initial size one quarter of target, scaled only after one clean live review."

Why this is strong:
- names thresholds and splits the sample
- includes capacity and portfolio fit, not just performance
- pre-commits the initial size
- makes the adversarial review a promotion condition

## Power Budget Statements

A strong spec names its sample: "roughly 1,000 names by 120 monthly cross-sections; effective observations reduced by cross-sectional correlation; a rank IC of 0.02 is detectable, a Sharpe difference of 0.1 between variants is not."

A weak spec says "we will backtest since 2010".

If the claimed effect is smaller than what the design can detect, the spec is unfalsifiable as written: extend the sample, widen the universe, or archive before any code is written.

## Approach Comparison Pattern

When comparing 2-3 research paths, use this structure:

1. mechanism and why it may exist
2. data needed and how trustworthy it is
3. expected implementation complexity
4. likely failure modes
5. fastest falsification path
6. recommendation

## Common Spec Gaps

Patch these before approval:
- benchmark missing or unrealistic
- no explicit decision time
- no cost assumptions
- no baseline
- validation design uses future information implicitly
- portfolio mapping is hand-waved away
- research goal mixes prediction, sizing, and execution into one blob
