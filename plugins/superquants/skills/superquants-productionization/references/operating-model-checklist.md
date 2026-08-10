# Operating Model Checklist

## Ownership

- who owns the strategy logic?
- who owns the data pipeline?
- who receives alerts and handles incidents?

## Data And Runtime

- what feeds or datasets are required at runtime?
- what are the freshness SLAs?
- what happens on late or missing data?

## Trading Workflow

- when are signals generated?
- when are orders sent?
- what pre-trade checks are required?
- what post-trade reconciliations are required?

## Rollout

- what shadow period is needed?
- what metrics define successful rollout?
- what triggers rollback or automatic disablement?
- what live-review cadence applies after rollout, and who runs it?
