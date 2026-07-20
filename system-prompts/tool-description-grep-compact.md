<!--
name: "Tool Description: Grep compact"
description: "Compact Grep tool description served to newer models — ripgrep-backed content search preferred over raw grep/rg, with permission-UI integration"
ccVersion: "2.1.178"
variables:
  - "BASH_TOOL_NAME"
-->
Content search built on ripgrep. Prefer this over `grep`/`rg` via ${BASH_TOOL_NAME} — results integrate with the permission UI and file links.

- Full regex syntax (e.g. "log.*Error", "function\s+\w+"). Ripgrep, not grep — escape literal braces (`interface\{\}`).
- Filter with `glob` (e.g. "**/*.tsx") or `type` (e.g. "js", "py", "rust").
- `output_mode`: "content" (matching lines), "files_with_matches" (paths only, default), or "count".
- `multiline: true` for patterns that span lines.
