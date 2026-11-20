<!--
name: "Tool Description: CronCreate"
description: "Describes the CronCreate tool for enqueuing one-shot or recurring cron-based jobs, with durable or session-only persistence, jitter and off-minute scheduling guidance"
ccVersion: "2.1.329"
variables:
  - "CRON_DURABLE_FLAG"
  - "CRON_CREATE_TOOL_NAME"
  - "MONITOR_TOOL_NAME"
  - "MATH_OBJECT"
  - "RECURRING_JITTER_FRACTION"
  - "RECURRING_JITTER_CAP_MS"
  - "ONE_SHOT_JITTER_MAX_MS"
  - "CRON_LIST_TOOL_NAME"
  - "CANCEL_TIMEFRAME_DAYS"
  - "CRON_DELETE_TOOL_NAME"
-->
Schedule a prompt to be enqueued at a future time. Use for both recurring schedules and one-shot reminders.

Uses standard 5-field cron in the user's local timezone: minute hour day-of-month month day-of-week. "0 9 * * *" means 9am local — no timezone conversion needed.

## One-shot tasks (recurring: false)

For "remind me at X" or "at <time>, do Y" requests — fire once then auto-delete.
Pin minute/hour/day-of-month/month to specific values:
  "remind me at 2:30pm today to check the deploy" → cron: "30 14 <today_dom> <today_month> *", recurring: false
  "tomorrow morning, run the smoke test" → cron: "57 8 <tomorrow_dom> <tomorrow_month> *", recurring: false

## Recurring jobs (recurring: true, the default)

For "every N minutes" / "every hour" / "weekdays at 9am" requests:
  "*/5 * * * *" (every 5 min), "0 * * * *" (hourly), "0 9 * * 1-5" (weekdays at 9am local)

## Avoid the :00 and :30 minute marks when the task allows it

Every user who asks for "9am" gets `0 9`, and every user who asks for "hourly" gets `0 *` — which means requests from across the planet land on the API at the same instant. When the user's request is approximate, pick a minute that is NOT 0 or 30:
  "every morning around 9" → "57 8 * * *" or "3 9 * * *" (not "0 9 * * *")
  "hourly" → "7 * * * *" (not "0 * * * *")
  "in an hour or so, remind me to..." → pick whatever minute you land on, don't round

Only use minute 0 or 30 when the user names that exact time and clearly means it ("at 9:00 sharp", "at half past", coordinating with a meeting). When in doubt, nudge a few minutes early or late — the user will not notice, and the fleet will.

${CRON_DURABLE_FLAG?`## Durability

By default (durable: false) the job lives only in this Claude session — nothing is written to disk, and the job is gone when Claude exits. Pass durable: true to write to .claude/scheduled_tasks.json so the job survives restarts. Only use durable: true when the user explicitly asks for the task to persist ("keep doing this every day", "set this up permanently"). Most "remind me in 5 minutes" / "check back in an hour" requests should stay session-only.`:`## Session-only

Jobs live only in this Claude session — nothing is written to disk, and the job is gone when Claude exits.`}

## Not for live watching

${CRON_CREATE_TOOL_NAME} re-runs a prompt at fixed wall-clock intervals. To watch a log file, process, or command output and be notified the moment something changes, use the ${MONITOR_TOOL_NAME} tool instead — ${MONITOR_TOOL_NAME} streams events as they happen; cron polls on a schedule.

## Runtime behavior

Jobs only fire while the REPL is idle (not mid-query). ${CRON_DURABLE_FLAG?"Durable jobs persist to .claude/scheduled_tasks.json and survive session restarts — on the next launch signed in to the same organization they resume automatically. One-shot durable tasks that were missed while the REPL was closed are surfaced for catch-up. Session-only jobs die with the process. ":""}The scheduler shifts each job by a fixed per-job offset on top of whatever you pick: by default a recurring job runs up to ${MATH_OBJECT.round(RECURRING_JITTER_FRACTION*100)}% of its period late (max ${RECURRING_JITTER_CAP_MS/60000} min), and a one-shot job landing on :00 or :30 runs up to ${ONE_SHOT_JITTER_MAX_MS/1000} s early. The result of this tool and of ${CRON_LIST_TOOL_NAME} gives each job's actual next run time: when you tell the user when a job will run, give that time, not the minute in the cron expression. Picking an off-minute is still the bigger lever.

Recurring tasks auto-expire after ${CANCEL_TIMEFRAME_DAYS} days — they fire one final time, then are deleted. This bounds session lifetime. Tell the user about the ${CANCEL_TIMEFRAME_DAYS}-day limit when scheduling recurring jobs.

Returns a job ID you can pass to ${CRON_DELETE_TOOL_NAME}.
