# Planning Patterns

## Experiment Zero: Power Check

Before any backtest, count what the design can actually detect:

- effective independent observations: cross-sectional width times time span, discounted for cross-sectional correlation and label overlap
- smallest detectable effect: at 300 monthly observations, Sharpe differences below roughly 0.4 are indistinguishable from noise; daily cross-sectional designs can detect far smaller edges
- if the claimed effect is below the detectable threshold, the experiment cannot falsify anything: renegotiate the spec, extend the sample, or archive
- a design that could not detect its own death within five live years deserves extra skepticism at review time

## Metric Freeze

The spec's benchmarks-and-metrics section is the complete list of headline metrics, frozen before the first run. Metrics added after seeing results are exploratory: report them in a separate section, amend the spec, and count the addition in the selection history. Metric shopping is multiplicity wearing a suit.

## Predict Then Run

Before each experiment, write the predicted result and a rough confidence: direction, magnitude, and the most likely failure mode. Comparing predictions to outcomes calibrates the researcher over time and makes hindsight bias visible in the log.

## Smallest Vertical Slice

The first implementable slice should usually be:
1. load a tiny sample
2. compute the signal or decision variable
3. map it to positions or orders
4. compute pnl or quality metrics with explicit costs
5. reconcile at least one or two rows manually

## Baseline First

Every plan should define at least one boring baseline, such as:
- equal-weight or benchmark exposure
- simple ranking without neutralization
- previous production logic
- shuffled or null signal where appropriate

## Experiment Ladder

A good ladder often looks like:
- Experiment 1: data and alignment sanity check
- Experiment 2: predictive or mechanical baseline
- Experiment 3: first cost-aware portfolio expression
- Experiment 4: broader history or larger universe
- Experiment 5: parameter or robustness sweep only after earlier wins

## Stop Conditions

Write stop conditions in advance.
Examples:
- archive if the baseline cannot be reproduced cleanly
- archive if predictive power vanishes after proper lagging
- archive if turnover makes net results unattractive
- escalate to debugging if accounting invariants fail
