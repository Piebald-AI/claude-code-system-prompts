<!--
name: "Data: Self-hosted runner control-plane idle release notice"
description: "Explains a server-provided session idle limit, the clean-checkout and session-folder release checks, runner exit behavior and ineffective hold-file limits"
ccVersion: "2.1.318"
variables:
  - "SESSION_ID"
  - "FORMATTED_IDLE_SESSION_LIMIT"
  - "DRAIN_GRACE_MS"
  - "HOLD_IDLE_FILE_PATH"
  - "MAX_HOLD_MS"
  - "IDLE_SESSION_LIMIT_MS"
-->
[runner:session] ${SESSION_ID} idle limit ${FORMATTED_IDLE_SESSION_LIMIT} from Anthropic's control plane: once its user has sent nothing for ${FORMATTED_IDLE_SESSION_LIMIT} after a finished turn, the session is released only if its checkouts hold no uncommitted changes and are still at the commit that the runner checked out, and its own folder under --base-dir/_sessions holds only what the runner put there. The runner checks that folder only on Linux, and keeps the session on any other system.${DRAIN_GRACE_MS===0?" This runner exits once its last session is released (--drain-grace-sec 0), so something has to start the next one.":""} Set --release-idle-session-min to choose your own limit, or to 0 to keep idle sessions.${HOLD_IDLE_FILE_PATH!==void 0&&MAX_HOLD_MS>0&&MAX_HOLD_MS<=IDLE_SESSION_LIMIT_MS?` --hold-idle-file holds nothing at this limit, because --max-hold-min is not longer than ${FORMATTED_IDLE_SESSION_LIMIT}: raise it for the file to hold.`:""}
