# Experiment Learning Loop

Use this loop after every completed experiment, with extra depth for a non-pass result or a material surprise. `Fail` may be the honest, final conclusion for the tested experiment; the outcome label alone is not a complete research closeout.

## 1. Classify the Outcome

Choose one class against the pre-committed criterion:

- pass: the run is valid and meets the criterion
- fail (valid negative): the run is valid and misses the criterion, so it updates belief against the tested claim or configuration
- invalid experiment: a bug, broken invariant, wrong data, or execution error means the run cannot adjudicate the claim
- inconclusive: the run is valid but the sample, power, exposure, or mixed evidence cannot separate the competing explanations

Do not call an invalid or underpowered run a fail, and do not relabel a valid fail as invalid or inconclusive to soften negative evidence. Record every run, but only valid evidence should update the alpha thesis.

Record a separate follow-up decision: promote, archive, debug, iterate, or gather evidence. The result says what happened in this experiment; the decision says what, if anything, the research process should do next.

## 2. Compare Prediction With Observation

Recover the prediction written before the run and state:

- expected direction, rough magnitude, confidence, and anticipated failure mode
- observed result under the same window, costs, benchmark, and metric definition
- the important gap or surprise
- which prior, assumption, or future estimate should change because of that gap

This is calibration, not hindsight storytelling. Do not rewrite the prediction after seeing the result.

## 3. Localize the Failure

Find the earliest layer where expected and actual behavior diverge:

1. statistical design or power
2. data, universe, timestamps, or labels
3. signal calculation or economic mechanism
4. portfolio mapping, constraints, or exposures
5. execution, costs, or capacity
6. evaluation, accounting, or reporting
7. operational environment

For the leading cause, cite the evidence, give a confidence level, and name at least one plausible alternative that remains. Broken invariants or suspicious metrics route to `superquants-strategy-debugging`; weak but internally consistent results are research evidence, not a software bug.

## 4. State What Was Learned

Separate the scope carefully:

- what this experiment falsifies or weakens
- what it does not test or rule out
- whether the failure is specific to this configuration, portfolio mapping, regime, or the underlying mechanism
- which reusable assumption, test, or gate should change for the next run

Do not rescue the thesis by inventing an explanation that the evidence does not distinguish. A useful negative result may justify archive rather than iteration.

## 5. Choose the Smallest Justified Next Action

- invalid experiment: preserve the failing evidence, debug the smallest slice, fix only the demonstrated defect, and rerun the frozen configuration
- fail (valid negative) that hits a pre-committed kill criterion: archive with the cause and any observable revival condition; no further experiment is required
- fail (valid negative) that isolates one plausible, testable link: only when the expected information gain justifies it, plan one new experiment that changes one thing and counts in the selection history; otherwise archive
- inconclusive: improve power or run the cheapest discriminator between the remaining explanations; do not tune toward the observed noise
- pass: move to the next pre-planned rung or robustness review without skipping required gates

Before closing out, complete the useful safe analysis available from already authorized data, logs, plots, and small diagnostic slices. This requirement closes the feedback loop; it does not require continuing the strategy. A new configuration, new external data, wider history, parameter search, or expensive rerun is a new experiment: write its prediction and stop criterion before execution and do not treat the failure as blanket authorization to expand scope.

## Feedback Into The Research Process

- carry the reusable lesson into the next plan's `Prior Learning Incorporated` section
- update the experiment log and selection history for every observed configuration
- if an earlier gate should have caught the problem, tighten that specific gate or test rather than adding broad ceremony
- if the mechanism is killed, record the cause and revival condition in the archive so later agents do not rediscover the same dead end
