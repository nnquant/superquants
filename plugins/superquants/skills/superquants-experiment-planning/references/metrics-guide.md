# Metrics Guide

## Principles

- Match the metric to the claim.
- Prefer net metrics after realistic costs.
- Pair performance with turnover, exposure, and sample-span context.
- Separate predictive power from portfolio outcome.

## Cross-Sectional Alpha

Primary metrics:
- mean IC or rank IC
- IC IR
- monotonic bucket spreads
- turnover
- exposure neutrality
- capacity footprint

## Time-Series Directional Strategies

Primary metrics:
- CAGR or annualized return
- Sharpe or Sortino
- max drawdown
- hit rate and payoff asymmetry
- turnover and holding time
- subperiod splits

## Relative Value And Stat Arb

Primary metrics:
- spread diagnostics
- gross and net exposure
- borrow or financing assumptions
- turnover
- tail and gap risk

## Execution Or Microstructure

Primary metrics:
- fill rate
- slippage
- implementation shortfall
- adverse selection
- inventory risk

## Portfolio Construction Changes

Primary metrics:
- tracking error
- concentration
- marginal risk contributions
- realized vs ex-ante risk
- turnover
- cost-aware net performance

## Multiplicity Context

Any headline metric should travel with its selection history: "best of N" changes what a number means, and best-of-20 under a pure-noise null already produces a respectable-looking Sharpe. When N is known, prefer deflated or haircut versions of the metric. When N is unknown, the result is not reviewable - reconstruct the history from the trial registry and experiment logs first.
