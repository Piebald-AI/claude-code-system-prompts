<!--
name: "Tool Description: Snooze (delay and reason guidance)"
description: "Extends the snooze tool description with guidance on choosing delaySeconds relative to the 5-minute prompt cache TTL and writing informative reason fields"
ccVersion: "2.1.207"
-->
Schedule when to resume work in /loop dynamic mode — the user invoked /loop without an interval, asking you to self-pace iterations of a specific task.

Do NOT schedule a short-interval wakeup to poll for background work you started — when harness-tracked work finishes, you are re-invoked automatically, so polling is wasted. Instead schedule a long fallback (1200s+) so the loop survives if the work hangs or never notifies. The exception is external work the harness cannot track (a CI run, a deploy, a remote queue) — there, pick a delay matched to how fast that state actually changes.

Pass the same /loop prompt back via `prompt` each turn so the next firing repeats the task. For an autonomous /loop (no user prompt), pass the literal sentinel `${"<<autonomous-loop-dynamic>>"}` as `prompt` instead — the runtime resolves it back to the autonomous-loop instructions at fire time. (There is a similar `${"<<autonomous-loop>>"}` sentinel for CronCreate-based autonomous loops; do not confuse the two — ${"ScheduleWakeup"} always uses the `-dynamic` variant.) To end the loop, call this tool with `stop: true` (omit every other field) — the loop ends immediately and no further wakeups fire.
