<!--
name: "Tool Description: REPL asynchronous output and polling instructions"
description: "Explains inline versus dispatched REPL results, asynchronous event formats, Poll waiting and how to avoid launching a running script twice"
ccVersion: "2.1.318"
variables:
  - "MATH_OBJECT"
  - "GET_REPL_INLINE_WAIT_TIMEOUT_MS_FN"
  - "IS_REPL_JSON_EVENT_FORMAT_ENABLED"
  - "POLL_TOOL_NAME"
-->

How output arrives: a script that finishes within about ${MATH_OBJECT.round(GET_REPL_INLINE_WAIT_TIMEOUT_MS_FN()/1000)} s comes back as the `REPL` call's own result, a `<repl-output eval="N">` element holding `<log>` lines and the `<result>` (or `<error>`). One still running by then returns `(dispatched #N)` instead, runs on, and no longer holds up the scripts after it: its output arrives as an ${IS_REPL_JSON_EVENT_FORMAT_ENABLED?'`<event kind="repl-eval">` element whose body is one JSON object (`eval` is the script's number, with its `log` lines and its `result` or `error`)':'`<event kind="repl-eval" eval="N">` element with the same children'}, in a `${POLL_TOOL_NAME}` result or before your next turn, with an `<event kind="repl-status">` ${IS_REPL_JSON_EVENT_FORMAT_ENABLED?"element":"line"} meanwhile saying what is still pending. A receipt means the script is running, so issuing it again would run it twice. Scripts start in call order.

Waiting: `${POLL_TOOL_NAME}` returns as soon as something arrives; while a script or a background task (a context, say) is still running, a wait with nothing to deliver ends just before the prompt cache would expire (about 5 minutes, or about an hour on a 1-hour cache) in a status line saying what is still pending, so you can poll again. Sent in the same turn as a `REPL` call it waits for that call's script: a long one (a test suite, a build) then costs no extra round trip, and one that has already come back ends the wait at once. When nothing else needs doing while a long script or a context runs, ending your turn works too: its result or notification starts your next turn when it lands, and waiting that way costs nothing. A shell command with no timeout of its own moves to the background after 10 minutes, so give a long build a longer timeout (up to 2 hours) to await it.
