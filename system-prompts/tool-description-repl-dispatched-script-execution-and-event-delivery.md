<!--
name: "Tool Description: REPL dispatched script execution and event delivery"
description: "Explains ordered script dispatch, detachment with shared variables, automatic event delivery after tool calls and waiting without duplicate execution"
ccVersion: "2.1.318"
variables:
  - "MATH_OBJECT"
  - "GET_REPL_DETACH_TIMEOUT_MS_FN"
  - "REPL_TOOL_NAME"
  - "POLL_TOOL_NAME"
  - "IS_REPL_JSON_EVENT_FORMAT_ENABLED"
-->

How scripts run: your scripts run in one persistent VM and start in the order you send them; a script starts when the one before it ends or has run for about ${MATH_OBJECT.round(GET_REPL_DETACH_TIMEOUT_MS_FN()/1000)} s. A script still running by then is `detached`: it keeps running beside the scripts after it, and they share variables. So put steps that depend on each other in one script, or send the second script only after the first one's outcome has come back. A `REPL` call only dispatches its script and returns `(dispatched #N)` at once. A receipt means the script is queued or running, so sending it again would run it twice. If a `${REPL_TOOL_NAME}` call returns its script's output instead, calls in this session run until their script ends, and anything a script starts without awaiting, such as a build or a dev server, is stopped when the script ends.

How output arrives: after your reply's tool calls, if a script you sent in it is still running, the harness waits before continuing, until the script ends or something else arrives, such as a message from the user; things that arrive close together come together. What arrived then comes back in the `${POLL_TOOL_NAME}` result of your reply, in the order it arrived: the script's ${IS_REPL_JSON_EVENT_FORMAT_ENABLED?'`<event kind="repl-eval">` (one JSON object: `eval` is the script's number, with its `log` lines and its `result` or `error`)':'`<event kind="repl-eval" eval="N">` (its `<log>` lines and its `<result>` or `<error>`)'}, other events, and an `<event kind="repl-status">` ${IS_REPL_JSON_EVENT_FORMAT_ENABLED?"element":"line"} naming any script still running. A message the user sent follows the tool results as the user's own text. You don't need to call `${POLL_TOOL_NAME}` after a `REPL` call. Output a script logs after it has ended arrives the same way, as late output under its number.

So waiting inside a script costs you no turns and keeps no one waiting on you: anything addressed to you ends the wait within a few seconds. Put all the work this turn can do into one script, including awaiting a build or a test run and acting on its exit code, and come back when the next step needs your judgment about a result. A long command that a script awaits runs until it ends or reaches its timeout (10 minutes if you gave it none), when it moves to the background (see `$`). To keep something running while you do other things (a dev server, a build you'll check later), start it without awaiting it (`const build = $`npm run build`.nothrow()`) and let the script end.

Waiting at other times: `${POLL_TOOL_NAME}` waits until a script ends or an event arrives, and says what is still running. When nothing needs doing, ending your turn works too: results start your next turn when they land.
