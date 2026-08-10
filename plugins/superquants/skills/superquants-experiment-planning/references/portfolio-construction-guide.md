# Portfolio Construction Guide

Portfolio mapping is where predictive evidence goes to die. The mapping from signal to positions is a modeling decision with its own failure modes; keep it explicit and keep it simple until evidence demands otherwise.

## Signal-to-Position Paths

In order of increasing complexity:

1. quantile buckets: long top, short bottom, equal weight - transparent, robust, hard to overfit
2. rank or z-score proportional weights with position caps
3. optimizer-based construction with risk model, turnover penalty, and constraints

Escalate only when the simpler mapping demonstrably leaves money or risk control on the table, and always keep the naive mapping as the baseline: if the optimizer does not beat quantile buckets net of its extra turnover, keep the buckets.

## Neutralization

- decide what the strategy should not bet on: market, sector, size, beta - then remove it deliberately
- where neutralization happens changes the strategy: demeaning before ranking is not the same as constraining the optimizer afterward
- after neutralizing, re-check that the claimed edge still exists; many published effects are exposure in disguise
- neutralization consumes breadth and adds turnover; account for both

## Volatility Targeting and Leverage

- portfolio-level vol targeting stabilizes risk but adds turnover and leverage variation; the estimation window is a parameter - count it
- name-level inverse-vol weighting changes the effective universe tilt toward quiet names; verify the signal survives the tilt

## Turnover Control

- smooth signals (EWMA) or trade only when ranks move beyond a band; both trade alpha timeliness against costs
- verify smoothing does not lag away the edge: the smoothing half-life must be short relative to the signal's decay horizon
- no-trade bands create path dependence; test sensitivity to the band width

## Constraint Interactions

- position caps, neutrality constraints, and turnover limits interact; binding combinations produce corner solutions that look nothing like the signal
- inspect the final weights against the raw signal regularly: if the correlation is low, the constraints own the portfolio, not the alpha
- infeasible constraint sets fail silently in some optimizers; assert feasibility explicitly

## Conservation Checks

- weights sum to the intended gross and net; cash reconciles; position changes match orders
- these are the accounting invariants that superquants-strategy-debugging expects to hold; wire them as tests, not eyeball checks

## Book-Level Sizing

- a new strategy's size is set by its marginal contribution to the existing book: correlation, incremental net Sharpe, and drawdown budget - not by its standalone Sharpe
- this question belongs to robustness review's portfolio-fit dimension; the plan should produce the numbers that review will need
