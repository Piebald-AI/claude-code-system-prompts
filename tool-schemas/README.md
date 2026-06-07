# Tool Schemas

JSON `input_schema` for Claude Code's builtin tools, captured verbatim from
the API request body Claude Code sends to Anthropic.

Seeded from issue
[#22](https://github.com/Piebald-AI/system-prompts/issues/22). All 29 tools
shipped in Claude Code v2.1.168 are covered.

## What's in each file

Each `<tool>.json` is a standalone JSON Schema document — the exact value of
`tools[i].input_schema` from a real `POST /v1/messages` request. No wrapping,
no transformation, no re-formatting beyond `JSON.stringify(value, null, 2)`
so diffs across versions stay readable.

The tool's prose description is **not** duplicated here — it lives in
[`system-prompts/tool-description-<tool>.md`](../system-prompts/) and stays
the single source of truth for that content.

## Source

Captured at the wire level via a local reverse proxy
([flare](https://github.com/YiRaaaan/flare)) that sits between Claude Code
and `api.anthropic.com` and records each request body. Because the schema
comes from the API payload — not from parsing the minified `cli.js` — it is
not affected by bundler or minifier changes between Claude Code releases.

## Version and stability

Files in this directory were captured from **v2.1.168**
(`x-anthropic-billing-header: cc_version=2.1.168.fc4`).

As a small data point on the maintenance argument from issue #22: comparing
captures from **v2.1.161 → v2.1.168** (seven patch releases), **28 of 29
schemas are byte-identical**. The only change was `LSP`, which gained a new
`query` property used by the `workspaceSymbol` operation:

```diff
+ "query": {
+   "description": "The symbol name or partial name to search for (workspaceSymbol only). ...",
+   "type": "string"
+ }
```

That is exactly the kind of change a runtime-contract reader would want to
know about — and exactly the kind of change that is invisible if only the
prose description is tracked.

Over the same seven versions, prose descriptions for `AskUserQuestion`,
`LSP`, `NotebookEdit`, and `Workflow` were edited — confirming that schemas
and descriptions vary on independent axes.

## Naming convention

- File: `<kebab-case-tool-name>.json`, e.g. `bash.json`, `web-fetch.json`,
  `ask-user-question.json`, mirroring the `tool-description-<kebab>.md`
  convention already used in `system-prompts/`.
- The tool name appears in the filename only; the file body is the schema
  itself.

## Relationship to the existing extractor

This directory is intentionally decoupled from
[`tools/updatePrompts.js`](../tools/updatePrompts.js) and the upstream
[`tweakcc` extractor](https://github.com/Piebald-AI/tweakcc/blob/main/tools/promptExtractor.js).
Those tools walk the Claude Code AST looking for `StringLiteral` /
`TemplateLiteral` nodes that pass a "looks like a prompt" heuristic — that
heuristic cannot match an `ObjectExpression` JSON schema and would need a
separate identifier+correlation step to associate each schema with its
tool. The proxy-capture path avoids that entirely; nothing in this
directory needs the existing extractor to keep working, and nothing in the
existing extractor needs to know about this directory.
