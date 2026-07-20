<!--
name: "Skill: PR explainer artifact-template mode"
description: "Generates a shareable pull request walkthrough artifact using the artifact-explainer template, required-questions block, and honesty note"
ccVersion: "2.1.206"
variables:
  - "PR_NUMBER"
  - "CURRENT_BRANCH_PR_INSTRUCTIONS"
  - "FORMAT_PR_EXPLAINER_TARGET_FN"
  - "ADDITIONAL_GUIDANCE"
  - "PR_EXPLAINER_REQUIRED_QUESTIONS_BLOCK"
  - "ARTIFACT_TOOL_NAME"
  - "ARTIFACT_ITERATION_FOOTER"
  - "PR_EXPLAINER_HONESTY_NOTE"
-->
${PR_NUMBER===""?CURRENT_BRANCH_PR_INSTRUCTIONS:FORMAT_PR_EXPLAINER_TARGET_FN(PR_NUMBER)}
${ADDITIONAL_GUIDANCE?`
Additional guidance from the user: ${ADDITIONAL_GUIDANCE}
`:""}
## Goal

Produce a **shareable PR walkthrough artifact** — a self-contained HTML page a
reviewer can read before opening the diff to understand what this change does,
why it's being made, and where to focus attention. Pitch the writing at a
reviewer seeing this PR for the first time.

${PR_EXPLAINER_REQUIRED_QUESTIONS_BLOCK}

## Build it from the explainer template

Load the `artifact-explainer` skill and build the page from its template,
publishing with the ${ARTIFACT_TOOL_NAME} tool as that skill directs. Use the
template's **sections flavor** — keep the sections structure, delete the
numbered steps. Fill the slots as follows:

- **Lede** — what this PR changes and why it's needed, in two or three
  sentences. If the PR body already says this well, reuse it.
- **Sections** — lead with one architecture or flow diagram when the change
  has a structural story; otherwise skip straight to the code. Open with a
  before/after section showing the user-observable change (behavior, API
  shape, or output); skip it if the change has no observable surface. Then
  group the diff into sections cut at the material's joints — group related
  changes rather than splitting per file. In each section the code snippet is
  usually the subject matter itself: a trimmed snippet, a plain-language
  explanation, and anything a reviewer should look closely at; add a diagram
  only where structure or flow genuinely needs one (the skill's diagram-first
  default applies to concept explainers, not PR walkthroughs, which are
  mostly symbolic content). End with a section for what's *not* obvious from
  the diff — context the diff alone doesn't show (why this approach over an
  alternative, what was tried and rejected, follow-ups intentionally left
  out).
- **Recap** — restate the takeaways as where a reviewer should focus
  attention.

End the page body with this line verbatim:

> ${ARTIFACT_ITERATION_FOOTER}

${PR_EXPLAINER_HONESTY_NOTE}
