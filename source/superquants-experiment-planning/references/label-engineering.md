# Label Engineering

The prediction target is a design choice, not a given. The same features against different labels produce different strategies, and label choice usually matters more than feature choice.

## Match the Label to the Claim

- raw forward return: tests total-return predictability, including beta and style
- benchmark-excess return: tests whether the signal beats the boring alternative
- residualized return (beta, sector, or factor neutral): tests alpha in the narrow sense
- volatility-scaled return: tests risk-adjusted selection and stabilizes cross-sectional comparisons

If the spec claims alpha but the label is raw return, the experiment tests the wrong claim. State which object the label measures and keep it aligned with the research claim.

## Horizon

- match the label horizon to the signal's expected decay and to realistic trading latency
- overlapping labels inflate the apparent sample: 5-day returns sampled daily are not independent observations - discount the power budget and use purging and embargo in splits
- a horizon much longer than the rebalance cadence mixes signal effects with portfolio path effects; keep them separable

## Classification vs Regression vs Path Labels

- sign labels discard magnitude; acceptable when only direction is tradable, wasteful otherwise
- threshold and barrier-style labels (profit-take, stop, timeout) embed an exit policy inside the label - use them only when that exit policy is actually the intended trading rule
- quantile labels are robust to outliers but blur the tails, where much of the pnl usually lives

## Label Pitfalls

- label computed from prices the strategy could not trade: delisted names, halted sessions, limit days
- label denominators using future information: volatility scaling with a window that extends past the decision time
- corporate actions applied to features but not labels, or vice versa
- label conventions differing between research and evaluation code: total-return versus price-return, close-to-close versus open-to-open

## Rules

- state the exact label formula, horizon, and overlap handling in the spec
- changing the label mid-project is a new trial: log it in the selection history
- when in doubt, evaluate against two label variants and report both - as two counted trials, not one result and one confirmation
