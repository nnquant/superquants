# ML Validation Guide

Machine-learning strategies fail through the same doors as linear ones - leakage, multiplicity, weak samples - but the doors are wider. Extra capacity to fit means extra capacity to fool.

## Hyperparameter Search Is Multiplicity

- every configuration whose validation score was seen counts as a trial; log the search-space size in the selection history
- tune on train and validation only; touch the final holdout once, after all decisions are frozen
- a reused holdout is a validation set: relabel it as such in the log and treat the "out-of-sample" claim accordingly
- prefer nested cross-validation when sample size allows; report the outer-loop score, not the best inner-loop score

## Time-Series Cross-Validation

- chronological splits only; no shuffling, no random folds
- purge training samples whose labels overlap the test window; add an embargo after each test window
- group by time, not by row: same-date observations share information and must not straddle a split
- global preprocessing leaks: normalization, feature selection, and imputation must be fit inside each training fold, never on the full history

## Overfit Diagnostics

- in-sample versus out-of-sample degradation: expect meaningful decay; near-zero degradation usually means leakage, not genius
- rank stability across folds: if the best configuration ranks poorly on other folds, selection is fitting noise (the combinatorial backtest-overfitting idea in miniature)
- seed sensitivity: retrain with different seeds; the dispersion is a stability metric and belongs in the log
- feature-importance stability across folds: importance that reshuffles every fold means the model has no persistent story

## Complexity Budget

- match parameter count to effective observations from the power budget; deep models on 300 monthly points memorize, they do not learn
- the boring baseline for any ML strategy is a regularized linear model on the same features; the ML variant must beat it net of its extra turnover and fragility
- prefer models whose failure modes are inspectable when performance is comparable

## Non-Stationarity

- the refit cadence is part of the strategy: define it in the plan, replicate it in the backtest, and freeze it in the production handoff
- a model refit whenever results disappoint is an untracked parameter search over refit dates
- report performance by subperiod and regime; averaged-over-a-decade metrics hide the years the model was dead
