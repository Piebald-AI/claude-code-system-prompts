<!--
name: "Skill: Code Review (Output — findings JSON array)"
description: "Defines the code-review skill's result shape: a JSON array of findings carrying file, line, summary, and failure_scenario"
ccVersion: "2.1.328"
variables:
  - "MAX_FINDINGS"
  - "PLURALIZE_FN"
  - "SHOULD_INCLUDE_FINDING_SEVERITY"
  - "FINDING_SEVERITY_GUIDANCE"
  - "REPORT_FINDINGS_TOOL_NAME"
-->
## Output

Return findings as a JSON array ${MAX_FINDINGS==="all"?"with one object for every finding that survives, no maximum":`of at most ${MAX_FINDINGS} ${PLURALIZE_FN(MAX_FINDINGS,"object")}`}:

```json
[
  {
    "file": "path/to/file.ext",
    "line": 123,
    "summary": "${SHOULD_INCLUDE_FINDING_SEVERITY?"the problem, where it happens and what sets it off. Fix: the change to make":"one-sentence statement of the bug"}",
    "failure_scenario": "concrete inputs/state → wrong output/crash"${SHOULD_INCLUDE_FINDING_SEVERITY?`,
    "severity": "one of: important, nit, pre_existing"`:""}
  }
]
```

${SHOULD_INCLUDE_FINDING_SEVERITY?`${FINDING_SEVERITY_GUIDANCE}
`:""}Ranked most-severe first. ${MAX_FINDINGS==="all"?"Keep every finding that survives. There is no maximum.":`If more than ${MAX_FINDINGS} survive, keep the ${MAX_FINDINGS} most
severe.`} If nothing survives verification, return `[]`. Do not call the
${REPORT_FINDINGS_TOOL_NAME} tool even if it is available - this review's
output contract is the JSON block above.
