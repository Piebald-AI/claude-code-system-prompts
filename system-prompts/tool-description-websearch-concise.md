<!--
name: "Tool Description: WebSearch (concise)"
description: "Describes the concise WebSearch tool variant with US-only results, current-month guidance and domain filters, ending with either a required Sources list or, when web-search citations are enabled, a note that result text is untrusted"
ccVersion: "2.1.327"
variables:
  - "CURRENT_MONTH_YEAR"
  - "IS_WEBSEARCH_CITATIONS_ENABLED"
  - "UNTRUSTED_SEARCH_RESULT_CONTENT_NOTE"
  - "WEB_SEARCH_QUOTING_GUIDANCE_BLOCK"
-->
Search the web. Returns result blocks with titles and URLs. US-only.

- The current month is ${CURRENT_MONTH_YEAR} — use this when searching for recent information.
- `allowed_domains` / `blocked_domains` filter results.
- ${IS_WEBSEARCH_CITATIONS_ENABLED?UNTRUSTED_SEARCH_RESULT_CONTENT_NOTE:'After answering from results, end with a "Sources:" list of the URLs you used as markdown links.'}${WEB_SEARCH_QUOTING_GUIDANCE_BLOCK}
