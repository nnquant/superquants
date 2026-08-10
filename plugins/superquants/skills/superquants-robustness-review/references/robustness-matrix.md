# Robustness Matrix

## Selection History

Ask:
- how many candidates, variants, quick looks, and hyperparameter settings preceded this result?
- is this the best of N, and does the edge survive a best-of-N haircut or a deflated metric?
- was any holdout touched more than once?
- for mined families: what are the family id, counts, and selection rule?

## Out-Of-Sample

Ask:
- does the effect survive holdout periods or walk-forward windows?
- is the edge broad or concentrated in one period?

## Costs

Ask:
- what happens after realistic fees, slippage, borrow, financing, and impact assumptions?
- does the strategy still look attractive after modest cost stress?

## Parameter Sensitivity

Ask:
- is the chosen parameter a sharp local optimum?
- do nearby settings behave similarly enough to trust the idea?

## Regimes And Subperiods

Ask:
- does the strategy only work in one volatility or trend regime?
- what happens in crisis periods, low-volatility periods, and high-turnover periods?

## Crowding And Competition

Ask:
- how correlated are the returns to published factors and observable peers?
- how did the strategy behave in known unwind or stress episodes for its style?
- who else can see this signal, and what is the expected half-life of the edge?

## Concentration And Capacity

Ask:
- is pnl dominated by a few names or dates?
- what liquidity footprint and turnover does the strategy require?

## Exposure Decomposition

Ask:
- are returns mostly beta, sector, carry, or some other known exposure?
- does the edge survive neutralization or basic risk controls?

## Mechanism Discrimination

Ask:
- what alternative explanations produce the same headline result: known factor exposure, selection residue, cost optimism, a single lucky regime?
- what additional predictions does the claimed mechanism make, and were any of them tested?
- is the edge strongest exactly where the mechanism says it should be strongest?

## Marginal Portfolio Contribution

Ask:
- what is the correlation to the existing book, and the incremental net Sharpe at the intended size?
- does it lose money at the same time as the rest of the book?
- would the same capital do better scaling an existing strategy?

## Reproducibility And Operations

Ask:
- can the result be rerun from raw inputs and frozen config?
- does the implementation rely on notebook state or manual steps?
