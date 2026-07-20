<!--
name: "Skill: /stuck (background-daemon diagnostics)"
description: "The background-daemon troubleshooting section of the /stuck skill"
ccVersion: "2.1.173"
variables:
  - "DAEMON_LOCK_CONTENT"
  - "DAEMON_STATUS_CONTENT"
  - "DAEMON_LOG_PATH"
  - "DAEMON_LOG_SNIPPET"
  - "WORKER_ROSTER_PATH_FN"
  - "DAEMON_STATE_DIR_FN"
-->
## Daemon

The background daemon manages `& <prompt>` jobs and `claude agents`. If the issue involves background sessions, look here.

### daemon.lock
```json
${DAEMON_LOCK_CONTENT??"(missing)"}
```

### daemon.status.json
```json
${DAEMON_STATUS_CONTENT??"(missing)"}
```

### Daemon log (`${DAEMON_LOG_PATH}`)
${DAEMON_LOG_SNIPPET}

Other daemon state on disk (Read if relevant — roster contains user prompts and env vars):
- `${WORKER_ROSTER_PATH_FN()}` — live worker roster
- `${DAEMON_STATE_DIR_FN()}/<short>/state.json` — per-job state
