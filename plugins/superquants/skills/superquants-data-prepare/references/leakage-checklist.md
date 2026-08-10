# Leakage Checklist

## Point-In-Time Basics

- Confirm that the historical universe is formed using information available at that historical timestamp.
- Include delistings or dead names when relevant.
- Confirm whether index membership is current-state or point-in-time.
- Check whether corporate actions are applied consistently to both features and returns.

## Timestamp Alignment

- Write down the decision timestamp explicitly.
- Write down the label horizon explicitly.
- For every source, note when the data becomes known, not just the event date.
- Check timezone conversions and session boundaries.
- For intraday work, check quote, trade, bar, and event clock alignment.

## Transform Leakage

- Cross-sectional normalization should only use names in the tradable universe at that timestamp.
- Rolling statistics should only look backward.
- Imputation should not peek at future values.
- Winsorization and clipping should use historical or same-timestamp information only.
- Joins on entity identifiers should be audited for revisions and backfills.

## Validation Leakage

- Use chronological splits.
- When labels overlap, consider purging and embargo.
- Do not tune on the final test set.
- Do not let repeated notebook iteration leak information from future periods into early design choices without documenting it.

## Common Red Flags

- current constituents used for historical backtests
- fundamentals aligned to fiscal period end instead of actual release time
- cross-sectional z-scores built on future membership
- forward-filled fields with no freshness limit
- event timestamps rounded into the wrong session
