---
name: superquants-strategy-debugging
description: use when a backtest looks wrong, a live strategy diverges from research, exposures or pnl are suspicious, metrics disagree, or a quant bug is suspected. localizes the smallest failing slice through targeted questions, layered diagnosis across data-signal-portfolio-execution-reporting, and a written diagnosis memo before broad rewrites or full reruns.
---

# Superquants Strategy Debugging

Use this skill when the problem is not "build the strategy" but "find why it is wrong". At the start of a qualifying task, say you are using the Superquants Strategy Debugging skill.

Read the latest research spec, data audit, experiment plan, experiment logs, plots, and relevant code before proposing fixes. If the failure surface is ambiguous, ask one question per message until the symptom is concrete enough to reproduce.

Do not rewrite the whole stack, rerun giant backtests, or hand-wave the bug away. Localize the smallest failing slice first.

## Checklist

1. Read the evidence.
   - spec, audit, plan, logs, code, tests, plots, alerts, and any live-vs-research comparisons
2. Restate the symptom in one sentence.
   - what happened
   - what was expected
   - where it was first observed
3. Ask clarifying questions one at a time.
   - resolve environment, data version, timing, and reproduction uncertainty
4. Freeze a minimal failing slice.
   - smallest date range, instrument set, and config that still reproduces the issue
5. Diagnose in this order.
   - data ingestion and timestamp alignment
   - signal transformation and lag rules
   - universe filters and portfolio mapping
   - execution and cost model
   - evaluation and reporting layer
6. Write the diagnosis memo.
   - Save to `research/superquants/diagnoses/YYYY-MM-DD-<slug>-diagnosis-memo.md`.
   - Use `scripts/new_diagnosis_memo.py` when files are available.
7. Propose the fix plan only after the failure is localized.
   - Prefer targeted tests and tiny reruns over broad reruns.
8. Self-review the memo.
   - Use `scripts/validate_diagnosis_memo.py` when available.
9. Transition.
   - If the bug is fixed and the research claim is intact, return to superquants-experiment-planning for the next controlled run.
   - If the issue is actually weak evidence rather than a bug, move to superquants-robustness-review.
   - If live performance fades with no broken invariant and no bug, the question is decay, not defect: route to superquants-live-review.

## Debugging Rules

- Separate symptom from theory about root cause.
- Preserve evidence before changing code.
- Verify one layer at a time.
- When accounting identities fail, do not trust any downstream metric.
- When live diverges from backtest, compare data version, latency, universe eligibility, execution assumptions, and reporting conventions before changing the alpha logic.

## Output Standard

A finished diagnosis memo should usually contain:

- symptom
- expected behavior
- failure surface
- reproduction steps
- layered checks
- most likely root causes
- fix plan
- verification plan
- decision

## Resources

- `scripts/new_diagnosis_memo.py`: scaffold a diagnosis memo at the canonical location
- `scripts/new_minimal_failing_slice.py`: scaffold a minimal failing slice document next to the diagnoses
- `scripts/validate_diagnosis_memo.py`: verify required memo sections exist
- `references/debugging-playbook.md`: layer-by-layer debugging sequence and verification ideas
- `references/symptom-map.md`: common symptoms mapped to likely layers and first checks
- `assets/templates/diagnosis-memo-template.md`: default diagnosis memo structure
- `assets/templates/minimal-failing-slice-template.md`: default template for documenting a reduced reproduction case
