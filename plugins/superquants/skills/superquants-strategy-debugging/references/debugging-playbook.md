# Debugging Playbook

## Layer 1: Data And Timestamps

Check:
- raw rows and timestamps for the failing sample
- timezone or session boundary conversions
- delayed fields or stale prices
- point-in-time universe membership

## Layer 2: Signal Logic

Check:
- lookback windows
- shifts and lag rules
- normalization and neutralization steps
- missing-value handling

## Layer 3: Portfolio Mapping

Check:
- eligibility filters
- ranking to weights logic
- turnover caps and constraints
- cash, leverage, and position conservation

## Layer 4: Execution And Costs

Check:
- order timing assumptions
- slippage or fee model
- borrow and financing assumptions
- fill logic and partial execution behavior

## Layer 5: Evaluation And Reporting

Check:
- benchmark construction
- return aggregation conventions
- gross vs net calculation
- charting and metric window definitions

## Verification Pattern

For each suspected layer:
1. write a tiny test or manual reconciliation
2. prove the failure exists there
3. change one thing
4. rerun the tiny check
5. only then rerun a wider slice
