# Tool Schemas

JSON `input_schema` for Claude Code's builtin tools, captured verbatim from
the API request body Claude Code sends to Anthropic.

Seeded from issue
[#22](https://github.com/Piebald-AI/claude-code-system-prompts/issues/22).

35 schemas total, grouped by how they surface in the `tools[]` payload:

| Group | Tools | How to surface |
|---|---|---|
| **Default main loop** (29) | `agent`, `ask-user-question`, `bash`, `cron-*`, `edit`, `enter-/exit-plan-mode`, `enter-/exit-worktree`, `lsp`, `monitor`, `notebook-edit`, `push-notification`, `read`, `remote-trigger`, `schedule-wakeup`, `skill`, `task-*`, `web-fetch`, `web-search`, `workflow`, `write` | Standard Claude Code session, no flags |
| **Agent Teams** (3) | `send-message`, `team-create`, `team-delete` | `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` or `--agent-teams` (`utils/agentSwarmsEnabled.ts`) |
| **`local-agent` entrypoint** (2) | `glob`, `grep` | `CLAUDE_CODE_ENTRYPOINT=local-agent` (sub-agent context that exposes the dedicated search tools instead of having the model shell out via `Bash`) |
| **Brief / assistant mode** (1) | `send-user-message` | `CLAUDE_CODE_BRIEF=1` (KAIROS-style assistant entrypoint) |

Build-time-gated tools (`SendUserFile`, `Snip`, `WebBrowser`, …) live
behind `bun:bundle` `feature('KAIROS')` / `feature('WEB_BROWSER_TOOL')`
macros. Their code is present in the public native binary but they
require additional runtime gates not exposed by the env flags above;
left for a follow-up PR. `PowerShell` is Windows-only.

## File contents

Each `<tool>.json` is a standalone JSON Schema document — the exact value of
`tools[i].input_schema` from a real `POST /v1/messages` request, written with
`JSON.stringify(value, null, 2)` so diffs stay readable. No wrapping, no key
reordering, no other transformation.

The tool's prose description is not duplicated here — it lives in
[`system-prompts/tool-description-<tool>.md`](../system-prompts/).

## Source

Captured at the wire level via a local reverse proxy sitting between
Claude Code and `api.anthropic.com`. Because the schemas come from the API
payload rather than from parsing `cli.js`, they are independent of
bundler/minifier changes across Claude Code releases.

## Naming

`<kebab-case-tool-name>.json` — e.g. `bash.json`, `web-fetch.json`,
`ask-user-question.json`. The tool name is in the filename only; the file
body is the schema itself.

If a layout closer to `system-prompts/tool-description-<tool>.md` is
preferred (co-located, single dir, `tool-schema-<tool>.json` prefix), the
files rename cleanly — happy to follow whatever convention the maintainers
want.

## Not covered

`StructuredOutput`, a sub-agent tool whose `input_schema` is supplied at
spawn time by the caller rather than defined by Claude Code, has no fixed
shape to record.
