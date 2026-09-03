# Result Modules

Choose modules by the claim and decision, not by template availability. A report can use one module, several modules, or only the core sections.

## Portfolio Backtest

Use when the claim is about portfolio performance or tradability. Select from:

- strategy NAV or cumulative return versus the named benchmark
- excess NAV and drawdown
- gross versus net performance and cost drag
- turnover, exposure, concentration, or holding-period evidence
- subperiod or regime comparison when it changes the decision

NAV and drawdown are normally useful for a completed multi-period backtest, but not mandatory for a one-day check, a power calculation, or a non-portfolio factor test.

## Factor Evidence

Use when the claim is predictive rather than a finished portfolio. Select from:

- coverage and missingness
- IC or rank IC series, mean, IR, and cumulative IC
- bucket or quantile returns and monotonicity
- long-short spread
- turnover, exposure neutrality, and capacity footprint

Do not force a strategy NAV before portfolio mapping exists.

## Execution Quality

Use for order and microstructure research. Select from:

- fill rate and unfilled reasons
- slippage or implementation shortfall distribution
- adverse selection
- time-of-day, venue, liquidity-tier, or participation breakdown
- assumed versus realized cost reconciliation

## Robustness

Use only checks that bear on the decision. Select from:

- in-sample versus out-of-sample
- 1x versus 2x costs
- parameter neighborhood
- regime or subperiod stability
- exposure, concentration, capacity, and portfolio fit
- reproducibility and selection-history context

## Live Versus Backtest

Use for shadow or live review. Align conventions first, then select from:

- same-period live and backtest NAV or returns
- expected versus realized turnover, costs, exposures, and fills
- rolling or cumulative divergence
- decay-trigger status
- incident-adjusted comparison

## Diagnostic

Use when the decision is about correctness rather than performance. Select from:

- expected versus actual values
- smallest failing date and instrument slice
- accounting or conservation identity
- layer-by-layer evidence across data, signal, portfolio, execution, and reporting
- before-and-after verification when a fix is in scope

## Failure Learning

Use for every non-pass result or material surprise, alongside the relevant domain module. Select from:

- experiment result: pass, fail (valid negative), invalid experiment, or inconclusive against the pre-committed criterion
- separate follow-up decision: promote, archive, debug, iterate, or gather evidence
- pre-run prediction versus observed result
- earliest failing layer and evidence for the leading cause versus alternatives
- scope of falsification: mechanism, configuration, mapping, regime, or implementation
- reusable lesson and the specific research-process gate or test to update
- justified follow-up: the smallest next action with expected information gain, stop condition, and selection-history consequence, or archive with no further experiment

`Fail` may be a legitimate final experiment conclusion, but the label alone is not a complete closeout. Do not treat an invalid experiment as negative alpha evidence, relabel a valid fail to soften it, or use failure analysis as permission for unplanned tuning.

## Artifact Rules

- Prefer existing project formats and paths over inventing a parallel output tree.
- When a selected module needs a new chart and the project has no established style, apply `oaks-chart-style.md`; this does not expand the selected module set.
- Create machine-readable CSV or parquet outputs only for data actually computed and useful for verification.
- Use stable, numbered chart names when the project has no established naming convention.
- Every reported artifact path must exist and every headline number must reconcile to the same date window and cost convention.
- When a useful module cannot be produced from the available evidence, state the gap; do not generate an empty placeholder.
