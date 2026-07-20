<!--
name: "Skill: Code walkthrough"
description: "Generates an interactive explainer artifact for a file, directory, PR, or reference so newcomers can understand the code"
ccVersion: "2.1.198"
variables:
  - "WALKTHROUGH_TARGET"
  - "ARTIFACT_TOOL_NAME"
  - "ARTIFACT_DESIGN_SKILL_NAME"
  - "ARTIFACT_ITERATION_FOOTER"
-->
${WALKTHROUGH_TARGET===""?"No target was given. Ask the user which file, directory, or PR they want explained — one short question — and stop until they answer.":`Walkthrough target: `${WALKTHROUGH_TARGET}``}

## Goal

Produce an **interactive explainer artifact** for the target above — a
self-contained HTML page a newcomer can read top-to-bottom to understand what
this code does, how it fits together, and why it's built the way it is. Pitch
the writing at explain-like-I'm-new-here: assume the reader is a capable
engineer who has never seen this codebase.

## Explore first

Read the target and whatever it immediately depends on (callers, callees,
types it mentions, tests that exercise it). Build a mental model before
writing a word of the artifact. The artifact is only as good as your
understanding.

## Structure of the artifact

Write an HTML file and publish it with the ${ARTIFACT_TOOL_NAME} tool. Load
the `${ARTIFACT_DESIGN_SKILL_NAME}` skill first and give the page a
utilitarian treatment — this is a document, not a landing page.

The page should contain, in this order:

1. **One-paragraph summary** — what the target is for, in plain language.
2. **Map** — a short list or simple diagram of the main pieces and how they
   connect. For a single file this is the key functions/types; for a
   directory it's the files; for a PR it's the before→after.
3. **Walkthrough sections** — one `<details>` block per piece from the map.
   Inside each:
   - A plain-language explanation of what this piece does.
   - An **annotated code snippet**: the real code (trimmed to the relevant
     lines) with inline explanations of the non-obvious parts.
   - A **"why this matters"** callout — what would break or be worse if this
     piece didn't exist or worked differently.
4. **Open questions** — anything you couldn't determine from the code that a
   maintainer would know. Honest "I don't know" beats a guess.

End the page body with this line verbatim so the reader can bring the
artifact back into Claude Code to keep iterating:

> ${ARTIFACT_ITERATION_FOOTER}

## Keep it honest

Explain what the code *actually does* (trace it), not what its names suggest
it does. When a section is genuinely simple, say so briefly and move on —
don't pad.
