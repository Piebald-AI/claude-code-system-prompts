<!--
name: "Tool Parameter: Workflow resume run ID"
description: "Workflow parameter for resuming a prior run, explaining that cached agent() calls replay up to the first changed or failed call and that the prior run must be stopped first"
ccVersion: "2.1.326"
variables:
  - "TASK_STOP_TOOL_NAME"
-->
Run ID of a prior Workflow invocation to resume from. The cache is positional: agent() calls replay from cache up to the first call that failed, no longer matches the earlier run (edited, added, removed or reordered) or never started in it; that call and every call after it run again, even when their own (prompt, opts) are unchanged. A call a usage limit refused, or one still running when the run stopped, usually runs again without ending reuse: finished calls after it still come from cache. Same-session only. Stop the prior run first (${TASK_STOP_TOOL_NAME}) before resuming.
