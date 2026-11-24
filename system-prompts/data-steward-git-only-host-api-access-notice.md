<!--
name: "Data: Steward git-only host API access notice"
description: "Explains the host API information Claude Code can read with git's sign-in, what the watch can act on, what the user must monitor and when the watch stops"
ccVersion: "2.1.331"
variables:
  - "REMOTE_HOST_NAME"
  - "READABLE_HOST_PARTS"
  - "HOST_PART_ACTIONS_FIELD"
  - "HOST_PART_VALUE_BINDING"
  - "INACCESSIBLE_HOST_PARTS"
  - "HOST_PART_NAME_FIELD"
  - "HOST_API_CONTEXT"
  - "PENDING_HOST_PARTS"
  - "HOST_PART_STATE_FIELD"
  - "HOST_PART_NAME_BINDING"
  - "FORMAT_HOST_READ_FAILURE_FN"
  - "WATCH_STOP_CONDITION_TEXT"
-->
Claude Code also reads ${REMOTE_HOST_NAME}'s web API every two minutes, and only reads. That is new in Claude Code: code reuses git's saved sign-in for web calls. I act on ${READABLE_HOST_PARTS.map(({HOST_PART_ACTIONS_FIELD:HOST_PART_VALUE_BINDING})=>HOST_PART_VALUE_BINDING).join(", and on ")||"nothing there for now"}.${INACCESSIBLE_HOST_PARTS.length===0?"":` That sign-in doesn't open ${INACCESSIBLE_HOST_PARTS.map(({HOST_PART_NAME_FIELD:HOST_PART_VALUE_BINDING})=>HOST_PART_VALUE_BINDING).join(" or ")}, so those are yours to watch.${HOST_API_CONTEXT.place.kind==="bitbucket"&&INACCESSIBLE_HOST_PARTS.some(({HOST_PART_NAME_FIELD:HOST_PART_VALUE_BINDING})=>HOST_PART_VALUE_BINDING==="review comments")?" Reading them takes a token with read:user:bitbucket and read:pullrequest:bitbucket.":""}`}${PENDING_HOST_PARTS.map(({HOST_PART_STATE_FIELD:HOST_PART_VALUE_BINDING,HOST_PART_NAME_FIELD:HOST_PART_NAME_BINDING})=>` Its ${HOST_PART_NAME_BINDING} couldn't be read just now (${FORMAT_HOST_READ_FAILURE_FN(HOST_PART_VALUE_BINDING.why??"no_answer")}): Claude Code goes on trying.`).join("")} I can't reply there, re-run a check or read CI logs: I tell you here. I stop when ${HOST_API_CONTEXT.requestId===void 0?"":"the request is merged or closed, when "}${WATCH_STOP_CONDITION_TEXT}.
