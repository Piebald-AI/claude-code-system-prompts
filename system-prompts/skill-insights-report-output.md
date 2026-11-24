<!--
name: "Skill: /insights report output"
description: "Formats and displays the insights usage report results after the user runs the /insights slash command"
ccVersion: "2.1.331"
variables:
  - "NEUTRALIZE_INSIGHTS_AT_REFERENCES_FN"
  - "INSIGHTS_DATA"
  - "REPORT_URL"
  - "HTML_FILE_PATH"
  - "FACETS_DIRECTORY"
  - "REPORT_HEADER"
  - "AT_A_GLANCE_SUMMARY"
  - "LEFT_OUT_LINE"
  - "RECOMMENDATION_TIP_LINE"
-->
The user just ran /insights to generate a usage report analyzing their Claude Code sessions.

Here is the full insights data:
${NEUTRALIZE_INSIGHTS_AT_REFERENCES_FN(INSIGHTS_DATA)}

Report URL: ${REPORT_URL}
HTML file: ${HTML_FILE_PATH}${FACETS_DIRECTORY===void 0?"":`
Facets directory: ${FACETS_DIRECTORY}`}

At-a-glance summary (for your context only — the user has not seen any output yet):
${NEUTRALIZE_INSIGHTS_AT_REFERENCES_FN(REPORT_HEADER+AT_A_GLANCE_SUMMARY)}

Respond with exactly the following, and nothing else. Do not add, omit, or reword any line:

Your shareable insights report is ready:
${REPORT_URL}
${LEFT_OUT_LINE?`
${LEFT_OUT_LINE}
`:""}${RECOMMENDATION_TIP_LINE?`
${RECOMMENDATION_TIP_LINE}
`:""}
Want to dig into any section or try one of the suggestions?
