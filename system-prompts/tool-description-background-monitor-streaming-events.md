<!--
name: "Tool Description: Background monitor (streaming events)"
description: "Describes the background monitor tool that streams stdout events from long-running scripts as chat notifications, with guidelines on script quality, output volume, and selective filtering"
ccVersion: "2.1.323"
variables:
  - "IS_DISKLESS_SESSION_FN"
  - "DISKLESS_MONITOR_LIFETIME_NOTE"
  - "DOES_SESSION_STOP_AFTER_REPLY_FN"
  - "STOPPING_SESSION_MONITOR_LIFETIME_NOTE"
  - "CAN_BACKGROUND_AGENT_KEEP_SESSION_ALIVE_FN"
  - "BASH_TOOL_NAME"
  - "SINGLE_NOTIFICATION_GUIDANCE_BLOCK"
  - "MONITOR_TOOL_NAME"
  - "IS_MONITOR_EXPIRY_ENABLED_FN"
  - "CAN_YIELD"
  - "YIELD_TOOL_NAME"
  - "SINGLE_NOTIFICATION_COMMAND_NOTE"
  - "MONITOR_TIMEOUT_GUIDANCE_FN"
-->
Start a background monitor that streams events from a long-running script. Each stdout line is an event — you keep working and notifications arrive in the chat. Events arrive on their own schedule and are not replies from the user, even if one lands while you're waiting for the user to answer a question.${IS_DISKLESS_SESSION_FN()?` ${DISKLESS_MONITOR_LIFETIME_NOTE}`:DOES_SESSION_STOP_AFTER_REPLY_FN()?` ${STOPPING_SESSION_MONITOR_LIFETIME_NOTE} ${CAN_BACKGROUND_AGENT_KEEP_SESSION_ALIVE_FN()?`To wait past your reply, have a background agent wait with foreground ${BASH_TOOL_NAME} commands, or tell the user what to check and when.`:"For anything longer, tell the user what to check and when."}`:""}

Pick by how many notifications you need:
${SINGLE_NOTIFICATION_GUIDANCE_BLOCK}
${IS_DISKLESS_SESSION_FN()||DOES_SESSION_STOP_AFTER_REPLY_FN()?`- **One per occurrence, while you work on this turn** ("show each ERROR line in the dev server's log while you try the change") → ${MONITOR_TOOL_NAME} with an unbounded command (`tail -f`, `inotifywait -m`, `while true`).
- **One per occurrence, until a known end, while you work on this turn** ("show each test file's result as the suite you just started runs, stop when it ends") → ${MONITOR_TOOL_NAME} with a command that emits lines and then exits.`:`- **One per occurrence, ${IS_MONITOR_EXPIRY_ENABLED_FN()?"until the monitor expires (re-arm to continue)":"indefinitely"}** ("tell me every time an ERROR line appears") → Monitor with an unbounded command (`tail -f`, `inotifywait -m`, `while true`).
- **One per occurrence, until a known end** ("emit each CI step result, stop when the run completes") → Monitor with a command that emits lines and then exits.`}

Your script's stdout is the event stream. Each line becomes a notification. Exit ends the watch.${CAN_YIELD?` ${MONITOR_TOOL_NAME} tells you when something happens; ${YIELD_TOOL_NAME} is how you wait for it.`:""}

  # Each matching log line is an event
  tail -f /var/log/app.log | grep --line-buffered "ERROR"

  # Each file change is an event
  inotifywait -m --format '%e %f' /watched/dir

  # Poll GitHub for new PR comments and emit one line per new comment
  last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  while true; do
    now=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    gh api "repos/owner/repo/issues/123/comments?since=$last" --jq '.[] | "\(.user.login): \(.body)"'
    last=$now; sleep 30
  done

  # Node script that emits events as they arrive (e.g. WebSocket listener)
  node watch-for-events.js

  # Per-occurrence with a natural end: emit each CI check as it lands, exit when the run completes
  prev=""
  while true; do
    s=$(gh pr checks 123 --json name,bucket)
    cur=$(jq -r '.[] | select(.bucket!="pending") | "\(.name): \(.bucket)"' <<<"$s" | sort)
    comm -13 <(echo "$prev") <(echo "$cur")
    prev=$cur
    jq -e 'all(.bucket!="pending")' <<<"$s" >/dev/null && break
    sleep 30
  done

**Don't use an unbounded command for a single notification.** `tail -f`, `inotifywait -m`, and `while true` never exit on their own, so the monitor stays armed until timeout even after the event has fired. For "tell me when X is ready," ${SINGLE_NOTIFICATION_COMMAND_NOTE}. Note that `tail -f log | grep -m 1 ...` does *not* fix this: if the log goes quiet after the match, `tail` never receives SIGPIPE and the pipeline hangs anyway.

**Script quality:**
- Every pipe stage must flush per line or matches sit in its buffer unseen: `grep` needs `--line-buffered`, `awk` needs `fflush()`. `head` cannot flush at all — `| head -N` delivers nothing until N matches accumulate, then ends the stream.
- In poll loops, handle transient failures (`curl ... || true`) — one failed request shouldn't kill the monitor.
- Poll intervals: 30s+ for remote APIs (rate limits), 0.5-1s for local checks.
- Write a specific `description` — it appears in every notification ("errors in deploy.log" not "watching logs").
- Only stdout is the event stream. Stderr goes to the output file (readable via Read) but does not trigger notifications — for a command you run directly (e.g. `python train.py 2>&1 | grep --line-buffered ...`), merge stderr with `2>&1` so its failures reach your filter. (No effect on `tail -f` of an existing log — that file only contains what its writer redirected.)

**Coverage — silence is not success.** When watching a job or process for an outcome, your filter must match every terminal state, not just the happy path. A monitor that greps only for the success marker stays silent through a crashloop, a hung process, or an unexpected exit — and silence looks identical to "still running." Before arming, ask: *if this process crashed right now, would my filter emit anything?* If not, widen it.

  # Wrong — silent on crash, hang, or any non-success exit
  tail -f run.log | grep --line-buffered "elapsed_steps="

  # Right — one alternation covering progress + the failure signatures you'd act on
  tail -f run.log | grep -E --line-buffered "elapsed_steps=|Traceback|Error|FAILED|assert|Killed|OOM"

For poll loops checking job state, emit on every terminal status (`succeeded|failed|cancelled|timeout`), not just success. If you cannot confidently enumerate the failure signatures, broaden the grep alternation rather than narrow it — some extra noise is better than missing a crashloop.

**Output volume**: Every stdout line is a conversation message, so the filter should be selective — but selective means "the lines you'd act on," not "only good news." Never pipe raw logs; filter to exactly the success and failure signals you care about. Monitors that produce too many events are automatically stopped; restart with a tighter filter if this happens.

Stdout lines within 200ms are batched into a single notification, so multiline output from a single event groups naturally.

The script runs in the same shell environment as Bash. Exit ends the watch (exit code is reported). ${MONITOR_TIMEOUT_GUIDANCE_FN()} Use TaskStop to cancel early.
