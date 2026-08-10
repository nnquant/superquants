# Red Team Protocol

A checklist self-review is necessary but not sufficient: the author of a result is structurally the wrong person to attack it. The red-team pass separates the roles.

## Setup

- reviewer: an independent subagent when the environment supports one; otherwise the same agent in a separate pass, after an explicit role switch, writing its attack before rereading the author's interpretation
- inputs: the evidence packet only - spec, data audit, plan, experiment logs' data and results sections, the robustness matrix evidence
- withheld: the author's interpretation, narrative, and recommendation sections; the red team must form its account from the evidence, not rebut a story

## Deliverables

1. Strongest null story.
   The most plausible account in which the result is luck or artifact, built from the usual suspects: selection residue and multiplicity, leakage remnants, cost optimism, a single carrying regime, known-factor exposure in disguise, a benchmark or accounting convention flattering the numbers. The null story must name the checkable implication of each element - what would be true in the data if the null story were right.

2. Pre-mortem.
   Assume the strategy is dead within two years of going live. Rank the most likely causes of death, drawing on the decay priors: crowding, cost realization, regime exit, capacity, operational drift.

3. Falsification list.
   The cheapest checks that would separate the null story from the alpha story, in cost order. These become review tasks, not suggestions.

## Author Response

- answer each named implication of the null story with evidence, or concede it and downgrade the recommendation
- an unanswered null story blocks promotion; "we ran out of time to check" means iterate, and consumes iteration budget
- the pre-mortem's top causes become monitoring requirements in the production handoff and check items for future live reviews

## Spirit

The red team wins by being right, not by being harsh: a null story that survives scrutiny saved the book real money, and a null story demolished by evidence makes the promotion case genuinely stronger. The goal is not to pass the review; it is to fail before capital does.
