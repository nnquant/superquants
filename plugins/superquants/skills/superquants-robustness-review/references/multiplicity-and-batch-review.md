# Multiplicity and Batch Review

## What Counts as a Trial

Any configuration whose result was seen by anyone: triage quick looks, mined candidates, hyperparameter settings, discarded label or universe variants, reruns after "small fixes" that changed results. If seeing it could have changed what gets reported, it counts.

Sources to reconstruct the count:
- `research/superquants/trial-registry.md`
- the selection-history sections of the experiment logs
- mining-run family metadata
- hyperparameter search-space sizes from the plan

## Why Best-of-N Ruins Naive Reading

Selecting the best of N noise-only backtests produces steadily more impressive statistics as N grows: best-of-20 already yields a respectable-looking Sharpe over typical sample lengths with no true edge at all. A reported metric therefore means nothing without its N. This is not pedantry; it is the main way quant research programs fool themselves.

## Effective Number of Trials

Correlated trials count less than independent ones. Twenty variants of the same 20-day momentum signal are nowhere near twenty independent tries. Estimate the effective count from the average pairwise correlation of the candidates' return streams or signal values; high average correlation collapses N toward 1, low correlation keeps N near nominal. Precision is not required - the difference between "about 3 effective trials" and "about 300" is what changes the verdict.

## Haircuts in Practice

- when N is known, prefer a deflated metric: adjust the observed Sharpe for the effective number of trials, sample length, and non-normality before comparing it to the promotion bar
- when exact adjustment is impractical, at minimum report every headline number as "best of N" and raise the bar accordingly
- the cleanest cure is a truly untouched holdout evaluated once, after all selection is finished; a surviving result on virgin data needs no N-correction for that data

## Reviewing a Mined Family

A factor-mining run is reviewed as a family, not as one lucky member:

1. demand the family metadata with any survivor: family id, N generated, N evaluated, selection rule, evaluation metric, holdout status - refuse review without it
2. judge the family's selection process: was the holdout untouched during mining? was the selection rule fixed in advance?
3. apply a false-discovery discipline across the family: a Benjamini-Hochberg-style pass over the candidates' statistics, or admit only the top slice into a one-shot clean holdout re-validation and judge on the holdout alone
4. expect most admitted candidates to die; a family where everything passes is evidence of leakage or a reused holdout, not of genius
5. record family outcomes in the trial registry so the next mining run inherits the prior

## Holdout Hygiene

- one look per holdout; a holdout consulted twice is a validation set - relabel it and find fresh data for the final judgment
- log every holdout touch in the experiment log; "we only peeked once" must be verifiable, not remembered
