<!--
name: "Agent Prompt: Artifact type creation slash command (first-party type)"
description: "Directs an Artifact creation slash command for a type with no quickstart intent to list types with the Artifact tool's type query, take the first-party type with the matching title, create the new Artifact from its type URL with no files at first, and fill it by following the type's instructions"
ccVersion: "2.1.323"
variables:
  - "ARTIFACT_COMMAND_NAME"
  - "ARTIFACT_NOUN_PHRASE"
  - "ARTIFACT_TYPE_TITLE"
  - "IS_ARTIFACT_QUICKSTART_ENABLED_FN"
  - "ARTIFACT_TOOL_NAME"
  - "SAY_PLAINLY_INSTRUCTION"
-->
`/${ARTIFACT_COMMAND_NAME}` was invoked: a request for ${ARTIFACT_NOUN_PHRASE} made as a NEW Artifact from the published Artifact type titled "${ARTIFACT_TYPE_TITLE}". ${IS_ARTIFACT_QUICKSTART_ENABLED_FN()?"No quickstart call is needed: use":"Use"} the `${ARTIFACT_TOOL_NAME}` tool to list the Artifact types available to this user (`type_query: "${ARTIFACT_TYPE_TITLE}"`), take the first-party type titled "${ARTIFACT_TYPE_TITLE}" (a first-party row opens with its tier in brackets, such as `[core]`; if more than one has that title, ask the user which before creating), create the new Artifact from its `type_url` — a `title` drawn from the brief, and no files at first so the type's instructions arrive — then fill it by following those instructions. If no first-party type titled "${ARTIFACT_TYPE_TITLE}" is listed for this user, ${SAY_PLAINLY_INSTRUCTION} and offer to make ${ARTIFACT_NOUN_PHRASE} another way.
