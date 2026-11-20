<!--
name: "Skill: Code Review named target diff instructions"
description: "Supplies a review target's diff command and limits local context and fixes to files that already contain the target's added lines"
ccVersion: "2.1.329"
variables:
  - "REVIEW_TARGET_NAME"
  - "REVIEW_DIFF_COMMAND"
  - "IS_REVIEW_TARGET_URL"
  - "SHOULD_APPLY_REVIEW_FIXES"
  - "FALLBACK_REVIEW_DIFF_COMMAND"
  - "REVIEW_DIFF_FAILURE_GUIDANCE_BLOCK"
-->
That target is ${REVIEW_TARGET_NAME}, and its own diff is this review's scope. Get the diff with this command, run alone, with nothing chained, piped or redirected:

```
${REVIEW_DIFF_COMMAND}
```

It replaces every `git diff` command that the instructions below give for gathering the diff. This checkout may be on another branch${IS_REVIEW_TARGET_URL?", or of another repository":""}, and must stay as it is: before you lean on a file here for context, check that it already has the diff's added lines, and where it does not, judge from the diff alone and report nothing from that file. If you start subagents, give each one the diff itself and this warning: they see none of this.${SHOULD_APPLY_REVIEW_FIXES?" Apply a fix only to a file that already has the diff's added lines, and list every other finding as skipped.":""}
${FALLBACK_REVIEW_DIFF_COMMAND?`
Some sessions have a gh with no `pr diff` command. Only if gh itself says so, run this in its place, alone too:

```
${FALLBACK_REVIEW_DIFF_COMMAND}
```
`:""}
${REVIEW_DIFF_FAILURE_GUIDANCE_BLOCK}

Use the quoted words only where you could not read the diff. Where you did read it, leave them out altogether.

