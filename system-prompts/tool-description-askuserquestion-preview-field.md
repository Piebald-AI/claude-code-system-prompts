<!--
name: "Tool Description: AskUserQuestion (preview field)"
description: "Instructions for using the HTML preview field on single-select question options to display visual artifacts like UI mockups, code snippets, and diagrams"
ccVersion: "2.1.69"
-->

Preview feature:
Use the optional `preview` field on options when presenting concrete artifacts that users need to visually compare:
- HTML mockups of UI layouts or components
- Formatted code snippets showing different implementations
- Visual comparisons or diagrams

Preview content must be a self-contained HTML fragment (no <html>/<body> wrapper, no <script> or <style> tags — use inline style attributes instead). Do not use previews for simple preference questions where labels and descriptions suffice. Note: previews are only supported for single-select questions (not multiSelect).
