# Data Shaping Guide

## Dataset Inventory Pattern

Document each dataset with:
- source and vendor
- entity keys and symbol history assumptions
- timestamp granularity
- update latency
- missingness behavior
- intended use: feature, label, filter, benchmark, or execution input

## Join Questions

When combining datasets, answer:
- what is the primary entity key?
- how are symbol changes or contract rolls handled?
- what timestamp is the join anchored to?
- how are duplicates, revisions, and late arrivals handled?

## Missing Data

Do not just say "filled missing values". Specify:
- what was dropped
- what was forward-filled and for how long
- what was backfilled and why
- what value was imputed and whether that creates bias

## Transform Notes

Every feature transform should state:
- raw field used
- lookback window
- whether normalization is time-series or cross-sectional
- whether the transform is applied before or after filtering
- whether the transform changes turnover or capacity materially
