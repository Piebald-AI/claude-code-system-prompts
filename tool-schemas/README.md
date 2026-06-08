# Tool Schemas

JSON `input_schema` for Claude Code's builtin tools, captured verbatim from
the API request body Claude Code sends to Anthropic.

Seeded from issue
[#22](https://github.com/Piebald-AI/claude-code-system-prompts/issues/22).
Covers the 29 tools shipped to the main agent loop.

## File contents

Each `<tool>.json` is a standalone JSON Schema document — the exact value of
`tools[i].input_schema` from a real `POST /v1/messages` request, written with
`JSON.stringify(value, null, 2)` so diffs stay readable. No wrapping, no key
reordering, no other transformation.

The tool's prose description is not duplicated here — it lives in
[`system-prompts/tool-description-<tool>.md`](../system-prompts/).

## Source

Captured at the wire level via a local reverse proxy
([flare](https://github.com/YiRaaaan/flare)) sitting between Claude Code and
`api.anthropic.com`. Because the schemas come from the API payload rather
than from parsing `cli.js`, they are independent of bundler/minifier changes
across Claude Code releases.

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
