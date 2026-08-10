# Decay and Calibration

## Why Triggers Are Pre-Committed

Post-hoc thresholds always rationalize continuing: after a drawdown there is always a story, and the story always says hold on. Decay triggers are therefore defined at handoff time, from the backtest distribution, before any live result exists. The live review's job is to check them honestly, not to renegotiate them.

## Constructing Decay Triggers

- Use a blocked bootstrap of backtest net returns to build the distribution of rolling 6 and 12 month Sharpe (or the headline metric of the spec).
- Set the alarm at a chosen percentile of that distribution, for example the 5th: "live rolling 12m Sharpe below the backtest 5th percentile triggers review".
- A fired trigger forces a decision at the next live review; it does not force retirement.
- For signal-level decay, track rolling IC with a CUSUM-style drift check; signal decay usually precedes pnl decay.
- Track risk-profile change separately from performance: exposure drift outside the researched envelope is a trigger of its own, even when pnl still looks fine.

## Decay Priors

- Published anomalies lose roughly a third to a half of their in-sample edge after publication; treat paper-sourced ideas accordingly from day one.
- Execution and microstructure edges decay fastest; structural and risk-premium edges decay slowest.
- Crowding decay often shows up first as rising correlation to peers and worse behavior in stress unwinds, before average performance visibly fades.
- Capacity-consumed decay is permanent; regime-driven underperformance may mean-revert. This distinction is what separates resize from retire.

## Attribution Order

Before concluding alpha decay, exclude in order:

1. bug or broken invariant - route to superquants-strategy-debugging
2. data drift - revisions, delays, universe eligibility changes
3. execution and cost degradation - realized slippage and fills versus assumptions
4. regime or exposure shift - is the environment inside the researched envelope?
5. crowding - peer correlation and unwind behavior

Residual decay is the diagnosis of last resort - and the most common true one.

## Calibration Ledger Mechanics

- For each promoted strategy, record expected versus realized headline metrics at 6 and 12 months.
- The program-level median ratio is the haircut. Apply it in robustness review: an expected net Sharpe of 1.0 under a program haircut of 0.6 plans for 0.6.
- With fewer than five promoted strategies the haircut is directional; do not over-tune gates from two observations.
- In every post-mortem, name the specific gate that should have caught the failure. Tighten that gate, not all gates: blanket tightening taxes throughput without fixing the miss.
- A ledger that only contains successes is a warning sign in itself: it means retirements are not being recorded.
