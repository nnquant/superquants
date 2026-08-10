# Cost Model Guide

Cost assumptions are part of the experiment definition. A strategy is not "profitable before costs" - it is untested.

## Components

- fees and commissions: exchange, clearing, regulatory; usually small and knowable
- spread: half the quoted spread per crossing, wider for illiquid names and stressed sessions
- market impact: grows with participation; a square-root form (impact proportional to volatility times the square root of order size over daily volume) is a serviceable default
- borrow and financing: shorts and leverage carry ongoing costs that vary by name and time; hard-to-borrow names can dominate the cost stack
- slippage versus decision price: the implementation-shortfall view - the difference between the price at decision time and the achieved fill, which includes delay cost

## Turnover Arithmetic

- annual cost drag equals two-sided turnover times per-side cost; do this multiplication in every plan
- a 200 percent two-sided annual turnover at 10 bps per side costs roughly 40 bps per year; at daily rebalancing the same per-side cost can consume multiple percent
- report gross and net side by side; the gap is the cost bet embedded in the strategy

## Calibration and Validation

- calibrate against your own realized fills whenever any exist; vendor or literature values are priors, not facts
- re-validate quarterly in production: realized versus assumed slippage is a standing monitoring metric
- costs are regime-dependent: spreads widen exactly when signals fire hardest; a flat per-share assumption flatters volatility-timed strategies

## The Stress Rule

Report every net result at 1x and 2x assumed costs. A strategy that dies at 2x costs is a bet on the cost model, not on the alpha - say so in the review memo.

## Capacity

- capacity is the size at which impact-adjusted net performance falls below the promotion bar
- estimate it from the cost curve, not from wishful participation caps
- state capacity in the spec's constraints and revisit it in robustness review

## Pitfalls

- assuming execution at the close while computing signals from the same close: the fill and the signal cannot share a timestamp
- ignoring spread widening on rebalance days driven by the same event as the signal
- zero-cost assumptions on futures rolls or FX conversion legs
- averaging costs across liquidity tiers when the strategy concentrates in the illiquid tail
