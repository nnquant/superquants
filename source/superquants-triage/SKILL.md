---
name: superquants-triage
description: use when screening raw quantitative strategy ideas or batches of mined factor candidates quickly, before committing to the full superquants pipeline. runs timeboxed quick looks under quarantine rules with a single default configuration and no tuning, logs every attempt and candidate family to the trial registry for multiplicity accounting, and ends each idea in drop or graduate-to-spec.
---

# Superquants Triage

Use this skill when the task is screening many ideas cheaply, not validating one idea properly. At the start of a qualifying task, say you are using the Superquants Triage skill.

Before looking at anything, read `research/superquants/trial-registry.md` and `research/superquants/archive/INDEX.md`: most "new" ideas have been tried before, and a previously killed idea needs a stated reason why now is different, not a rerun.

Do not tune parameters, do not iterate on a quick look, and never cite a triage result as evidence anywhere downstream. Triage exists to protect the pipeline's statistics, not to shortcut them.

## Checklist

1. Check priors.
   - search the trial registry and the archive index for this idea family
   - if it was killed before, ask what is different now; no answer means drop
2. Declare the timebox and configuration before looking.
   - T0: desk check, up to an hour - does the data exist, is there a structural reason it cannot work
   - T1: single crude cut, up to half a day - one default configuration, one pre-named metric
   - anything larger is not triage; write a spec instead
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
   - the spec commits metrics, kill criteria, and promotion criteria before the clean rerun
   - the triage note is linked for context and marked quarantined; its numbers are not evidence

## Triage Rules

- Every look counts: a quick look you do not log is untracked multiple testing.
- One configuration, chosen before looking. Tuning is the pipeline's job, under multiplicity accounting.
- A triage verdict may say "worth a spec" or "dead because X". It may never say "works" or quote a Sharpe as evidence.
- Batches are families: mined candidates are logged and later reviewed as a family, not as N independent discoveries.
- Throughput is the point: when an idea overruns its timebox, graduate it or drop it - do not linger.

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
