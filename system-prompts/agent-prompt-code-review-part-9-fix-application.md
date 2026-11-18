<!--
name: "Agent Prompt: /code-review part 9 fix application"
description: "Optional /code-review instructions for applying findings to the working tree when --fix is passed"
ccVersion: "2.1.328"
variables:
  - "IS_BUGS_ONLY_REVIEW"
  - "FIX_REPORT_INSTRUCTIONS"
-->


## Applying fixes (--fix)

The `--fix` flag was passed. After producing the findings list, apply the
findings to the working tree instead of stopping at the report: fix each one
directly${IS_BUGS_ONLY_REVIEW?", whatever its kind or severity":" — correctness bugs and reuse/simplification/efficiency cleanups alike"}.
Skip any finding whose fix would change intended behavior, require changes well
outside the reviewed diff, or that you judge to be a false positive — note the
skip rather than arguing with it. ${FIX_REPORT_INSTRUCTIONS}
