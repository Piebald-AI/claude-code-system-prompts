<!--
name: "System Reminder: Session stop hook active"
description: "Tells Claude a session-scoped Stop hook condition is active and must be treated as the directive until met"
ccVersion: "2.1.173"
variables:
  - "STOP_HOOK_CONDITION"
-->
A session-scoped Stop hook is now active with condition: "${STOP_HOOK_CONDITION}". Briefly acknowledge the goal, then immediately start (or continue) working toward it — treat the condition itself as your directive and do not pause to ask the user what to do. The hook will block stopping until the condition holds. It auto-clears once the condition is met — do not tell the user to run `/goal clear` after success; that's only for clearing a goal early.
