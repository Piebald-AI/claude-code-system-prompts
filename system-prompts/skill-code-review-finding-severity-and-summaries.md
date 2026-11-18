<!--
name: "Skill: Code Review finding severity and summaries"
description: "Defines finding severities, ranking, the summary format, and how to report repeated mistakes"
ccVersion: "2.1.328"
-->
Every object carries every key shown above. Its `severity` is one of:

- `important`: a bug that should be fixed before merging because this change
  adds it or makes it worse. If someone can hit it, a rare trigger does not
  lower the severity.
- `nit`: a minor issue, worth fixing but not blocking: a broken CLAUDE.md rule,
  or a bug that harms nobody, such as a misleading log line.
- `pre_existing`: a bug that exists in the codebase but that this change did
  not introduce. A bug in unchanged lines is `pre_existing` if the change only
  fails to fix it, and `important` if the change re-exposes it.

A severity only labels and orders a finding: never drop one for its severity.
When the limit forces a cut, cut the lowest-ranked first. Most severe means
`important`, then `pre_existing`, then `nit`.

Write each `summary` in two or three short sentences. Start with the problem as
a user of the code would see it. Next say where it happens and what sets it
off. End with "Fix:" and the change to make, or what to check if you are not
sure.

Beyond Phase 2's dedup, if the same mistake is repeated in several places,
report it once and name the other places in its `summary`. Different mistakes
stay separate findings, even when one change would fix them all.
