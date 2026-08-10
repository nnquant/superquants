# Monitoring Metrics

Track at least these categories:

## Data Health
- feed freshness
- missing values
- stale prices
- universe size drift

## Signal Health
- signal distribution drift
- unexpected sparsity or clipping
- factor exposure drift

## Portfolio Health
- gross and net exposure
- turnover
- concentration
- risk limit breaches

## Execution Health
- rejects and failures
- slippage
- fill rate
- implementation shortfall

## Outcome Monitoring
- realized vs expected pnl decomposition
- benchmark-relative behavior
- regime-specific underperformance

## Decay Detection
- rolling net Sharpe or headline metric versus its backtest bootstrap percentile
- CUSUM-style drift on rolling IC
- correlation to peers and published factors as a crowding onset signal
- realized versus assumed cost trend

These feed the pre-committed triggers checked in superquants-live-review.
