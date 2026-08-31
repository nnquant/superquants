# Oaks-Inspired Chart Style

Use this reference only when the selected result modules need newly rendered charts. It is a visual fallback, not a required chart pack and not a dependency on Project Oaks.

## Precedence

1. Follow the user's explicit format or style request.
2. Reuse the active project's existing plotting conventions when they are clear.
3. Otherwise use the Oaks-inspired defaults below.

Do not restyle valid existing artifacts merely to match this reference. Do not import Project Oaks plotting code unless Oaks is already an available project dependency; reproduce the relevant visual choices with the plotting stack already in use.

## Composition by Claim

Build only the panels needed to support the current claim:

- portfolio backtest: make NAV or cumulative return the dominant panel and pair it with drawdown context; add monthly heatmap, annual return, turnover, PnL, exposure, or market value only when they affect the decision
- factor evidence: prefer cumulative IC or RankIC, grouped or bucket returns, turnover, and distribution views; do not add a portfolio NAV until a portfolio mapping exists
- CTA or signal diagnostic: combine the factor or signal series with the relevant return, cumulative IC, distribution, Q-Q, or sorted-return evidence; omit empty panels
- robustness or live comparison: use aligned axes and directly comparable series or small multiples; emphasize the baseline-versus-variant or backtest-versus-live gap
- execution or correctness diagnostic: use the smallest expected-versus-actual, distribution, event-slice, or attribution view that localizes the issue; a one-panel chart is acceptable

The primary decision variable should receive the largest area. A useful focused chart is better than a sparse dashboard.

## Visual Defaults

- Prefer a white background, restrained colors, thin lines, and light dashed grids (`linestyle="--"`, about `alpha=0.4`).
- Render primary NAV in black. Overlay drawdown on a secondary axis as a translucent red area, around `alpha=0.15` to `0.20`, when the scales require it.
- Use the Chinese-market convention for signed PnL bars when appropriate: red for profit and green for loss. Include a zero line or explicit labels so meaning does not depend on color alone.
- Use orange for turnover, blue for market value or a secondary operating series, and `steelblue` for neutral bars or histograms.
- Use a blue-red diverging monthly-return heatmap centered at zero, with values annotated when the matrix remains readable. Use neutral or steel-blue annual-return bars with a visible zero line.
- Put the most decision-relevant metrics in the figure title or panel title. For portfolio performance this commonly includes annualized return, volatility, Sharpe, maximum drawdown, and Calmar; show only metrics actually computed under the reported window and cost convention.
- Keep legends near their data and rotate date labels only as much as needed. Avoid rainbow palettes, decorative gradients, 3-D effects, and unrelated dual axes.

## Chinese Text and Numeric Integrity

For Matplotlib charts that may contain Chinese labels, prefer this fallback order and keep minus signs visible:

```python
plt.rcParams["font.sans-serif"] = [
    "Noto Sans CJK SC",
    "SimHei",
    "Microsoft YaHei",
    "Arial Unicode MS",
    "DejaVu Sans",
]
plt.rcParams["axes.unicode_minus"] = False
```

Use the project's actual return convention: compound simple returns where appropriate and do not silently replace them with summed returns. Chart labels, headline metrics, and machine-readable artifacts must use the same date attribution, benchmark, frequency, and transaction-cost assumptions.

## Layout Patterns

Treat these as optional patterns, not mandatory templates:

- compact portfolio: one large NAV-plus-drawdown panel
- standard portfolio: large NAV-plus-drawdown panel above monthly-return heatmap and annual-return bars
- detailed portfolio: dominant NAV panel followed by PnL, turnover, exposure or market value, then calendar summaries
- cross-sectional factor: a 2 by 2 dashboard for cumulative IC or RankIC, bucket returns, turnover, and IC distribution
- signal diagnostic: two large analytical panels above two or three compact distribution or calibration panels

Choose the smallest pattern that makes the conclusion auditable. If a panel has no useful data, remove it instead of displaying an empty placeholder.
