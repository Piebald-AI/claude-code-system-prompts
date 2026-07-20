<!--
name: "Tool Description: WebSearch (concise)"
description: "Describes the concise WebSearch tool variant with US-only results, current-month guidance, domain filters, and required sources"
ccVersion: "2.1.173"
variables:
  - "CURRENT_MONTH_YEAR"
-->
Search the web. Returns result blocks with titles and URLs. US-only.

- The current month is ${CURRENT_MONTH_YEAR} — use this when searching for recent information.
- `allowed_domains` / `blocked_domains` filter results.
- After answering from results, end with a "Sources:" list of the URLs you used as markdown links.
