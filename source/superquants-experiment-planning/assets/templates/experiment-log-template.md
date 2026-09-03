# {{topic_title}} Experiment - {{experiment_name}}

Date: {{date}}
Strategy Slug: {{strategy_slug}}
Experiment Slug: {{experiment_slug}}

## Summary
One paragraph describing what changed and the headline result.

## Objective
What question should this run answer?

## Hypothesis
What outcome would support the thesis?

## Data Snapshot
List the dataset version, universe, and date span.

## Selection History
How many variants of this family have been tried so far - including triage looks, mined candidates, and hyperparameter settings - and what selection rule produced this configuration?

## Implementation
Describe the exact code, config, and parameter changes.

## Portfolio and Execution Mapping
How does the signal become positions or orders?

## Costs and Constraints
List fees, slippage, borrow, financing, limits, and assumptions.

## Results
Report the key metrics and use only the result modules that answer this experiment. Link the selected plots and machine-readable artifacts; do not generate every available template by default.

## Outcome Classification
Classify the experiment result as pass, fail (valid negative), invalid experiment, or inconclusive against the pre-committed criterion. State whether it can update belief about the research claim; do not relabel a valid fail to soften the evidence.

## Follow-up Decision
Separately choose promote, archive, debug, iterate, or gather evidence. A fail may be the final experiment conclusion, and archive with no further experiment is a valid decision.

## Prediction Review
Compare the prediction written before the run with the observation. What surprised us, and which assumption or estimate should change?

## Interpretation
What changed in predictive power, tradability, or risk?

## Failure Analysis and Learning
For a non-pass or material surprise, identify the earliest failing layer, evidence for the leading cause and alternatives, what was and was not falsified, and the specific process gate or test to improve. For a clean pass, record the closest remaining failure mode.

## Next Step
If the follow-up decision requires action, name the smallest concrete action, expected information gain, pre-committed stop condition, and whether it counts as a new trial. If no further experiment is justified, state that explicitly and preserve the archive or revival condition.

## Reproducibility
List commit hash, commands, seeds, and file paths.
