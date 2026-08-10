# Symptom Map

## PnL Looks Too Good To Be True

Likely first checks:
- timestamp leakage
- current-state universe selection
- missing costs
- benchmark or compounding bug

## Live Is Worse Than Backtest

Likely first checks:
- delayed data or stale features
- execution timing mismatch
- slippage underestimation
- universe eligibility drift

## Exposure Does Not Match Signal

Likely first checks:
- filter ordering
- normalization after filtering vs before filtering
- optimizer constraints
- stale holdings cache

## Metrics Disagree Across Reports

Likely first checks:
- gross vs net confusion
- different benchmark definitions
- different date ranges or calendars
- different treatment of missing dates

## Live PnL Fades Slowly With No Broken Invariants

Likely first checks:
- crowding: correlation to peers and known factors rising
- regime: current exposures versus the researched envelope
- costs: realized slippage versus assumptions
- decay: once bugs are excluded, route to superquants-live-review

## Backtest Fails Only On Certain Days Or Names

Likely first checks:
- corporate actions
- symbol mapping
- illiquid names or zero prices
- contract rolls or delistings
