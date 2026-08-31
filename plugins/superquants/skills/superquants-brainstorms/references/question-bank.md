# Question Bank

Use these questions selectively after inspecting the project. Ask only what would materially change the research design. When a native structured-question tool is available, group up to three related questions in one round; otherwise state reasonable defaults and ask only the blocker that cannot be safely inferred. Never turn this bank into a serial survey.

## Intent And Decision

- What decision should this research change if it succeeds?
- Is the user trying to discover new alpha, improve an existing strategy, or explain recent underperformance?
- What does success look like in practice: better IC, better net Sharpe, lower drawdown, better execution, or lower turnover?

## Universe And Horizon

- Which instruments are in scope: equities, futures, options, FX, crypto, credit, or something else?
- Is the strategy cross-sectional, time-series, market-neutral, long-only, or event-driven?
- What holding period is realistic once trading and operations are considered?
- Are there liquidity, borrow, leverage, or concentration limits?

## Data And Timing

- What raw data is available today, and what timestamps come with it?
- Are there fundamentals, alternative data, or execution data that arrive with delay?
- What decision time matters: prior close, open, close, intraday bar, or event timestamp?
- Is the historical universe point-in-time or based on current constituents?

## Economic Mechanism

- Why should the edge exist rather than being a random pattern?
- Who is the natural counterparty and why might they persist?
- Is the strategy harvesting risk, information, microstructure, behavioral bias, or implementation inefficiency?

## Benchmarks And Validation

- What boring baseline should the strategy beat?
- How will results be validated: holdout, walk-forward, rolling windows, or regime splits?
- What would cause the idea to be archived quickly?

## Statistical Power

- How many effectively independent bets does the strategy make per year, after overlap and cross-sectional correlation?
- At that sample size, what is the smallest edge that could be distinguished from noise?
- Could five years of live data even detect that the edge had stopped working?

## Competition And Crowding

- Who else can compute this signal, and what stops them from arbing it away?
- What is the expected half-life of the edge, and what does that imply for how much to invest in building it?
- Which crowding proxies can be watched: correlation to published factors, peer performance, positioning data?
- If the idea comes from a paper, what does the post-publication decay record suggest?

## Strategy-Type Specific Prompts

### Cross-Sectional Alpha
- What future return horizon should the factor predict?
- Should the signal be sector-neutral, beta-neutral, or region-neutral?
- What turnover is acceptable?

### Time-Series Timing
- What is the timing horizon and regime assumption?
- Is the goal absolute return, drawdown reduction, or exposure timing?
- How sensitive is the strategy likely to costs and whipsaw?

### Relative Value And Stat Arb
- What anchors the spread economically?
- How stable is the relationship through time?
- What borrow or financing assumptions matter?

### Execution And Microstructure
- Is the objective better fills, lower shortfall, or lower adverse selection?
- What venues, order types, and latency assumptions apply?
- What inventory and participation constraints exist?
