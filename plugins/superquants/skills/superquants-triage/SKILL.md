---
name: superquants-triage
description: use for a timeboxed quick check of one raw quantitative idea or a batch of mined candidates before committing to the full superquants pipeline. runs a desk check or one frozen crude configuration with no tuning, keeps observed numbers quarantined, records actual trials for multiplicity accounting, and ends in drop or graduate-to-design.
---

# Superquants Triage

Use this skill when the task is cheaply deciding whether one idea or a candidate batch deserves a proper research design, not validating it for promotion. At the start of a qualifying task, say you are using the Superquants Triage skill.

Before looking at anything, read `research/superquants/trial-registry.md` and `research/superquants/archive/INDEX.md`: most "new" ideas have been tried before, and a previously killed idea needs a stated reason why now is different, not a rerun.

Infer the configuration from the user's request and current project when possible. If a material choice remains, use the environment's native structured-question tool when available and ask up to three related questions in one round. Otherwise state a reasonable default and ask only the blocker that cannot be safely inferred; do not run a serial survey.

Do not tune parameters, do not iterate on a quick look, and never cite a triage result as evidence anywhere downstream. Triage exists to protect the pipeline's statistics, not to shortcut them.

## Checklist

1. Check priors.
   - search the trial registry and the archive index for this idea family
   - if it was killed before and the current context does not establish what changed, ask that as the only blocker; no answer means drop
2. Declare the timebox and configuration before looking.
   - T0: desk check, up to an hour - does the data exist, is there a structural reason it cannot work
   - T1: single crude cut, up to half a day - one default configuration, one pre-named metric
   - anything larger is not triage; route to superquants-brainstorms for a compact brief or full spec
3. Run the quick look.
   - simplest usable data, no tuning, no second configuration
   - if a second configuration is genuinely needed, that is a second trial: log both
4. Log the attempt in the trial registry before deciding.
   - Use `scripts/new_triage_note.py` to scaffold the note; it seeds the registry on first use.
   - for mined batches, log the family: family id, count generated, count evaluated, selection rule
5. Decide per idea: drop or graduate.
   - drop: one-line reason in the registry; write a triage note only when the reason is instructive
   - graduate: write the triage note and open superquants-brainstorms
6. Guard the quarantine on graduation.
   - the approved design commits metrics and stop criteria before the clean rerun
   - the triage note is linked for context and marked quarantined; its numbers are not evidence

## Triage Rules

- Every look counts: a quick look you do not log is untracked multiple testing.
- One configuration, chosen before looking. Tuning is the pipeline's job, under multiplicity accounting.
- A triage verdict may say "worth a research design" or "dead because X". It may never say "works" or quote a Sharpe as evidence.
- Batches are families: mined candidates are logged and later reviewed as a family, not as N independent discoveries.
- Throughput is the point: when an idea overruns its timebox, graduate it or drop it - do not linger.
- When presenting the quick-look result, use superquants-result-reporting to select only the evidence modules that clarify the verdict; mark every observed number and chart as quarantined and do not generate a full chart pack by default.

## Output Standard

A finished triage note should usually contain:

- idea
- prior attempts
- timebox and config
- what was examined
- quarantined result
- multiplicity context
- verdict

## Resources

- `scripts/new_triage_note.py`: scaffold a triage note (seeds `research/superquants/trial-registry.md` on first use)
- `scripts/validate_triage_note.py`: verify required note sections exist
- `references/triage-discipline.md`: quarantine rationale, timebox tiers, batch and mining-family interface, graduation rules
- `assets/templates/triage-note-template.md`: default note structure
- `assets/templates/trial-registry-template.md`: seed structure for the program-wide trial registry
