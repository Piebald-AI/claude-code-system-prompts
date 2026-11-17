<!--
name: "Tool Description: WebSearch"
description: "Full WebSearch tool description: searching beyond the knowledge cutoff, US-only with domain filters, current-month year guidance, and either a mandatory Sources list or, when web-search citations are enabled, a note that result text is untrusted"
ccVersion: "2.1.327"
variables:
  - "IS_WEBSEARCH_CITATIONS_ENABLED"
  - "WEB_SEARCH_QUOTING_GUIDANCE_BLOCK"
  - "UNTRUSTED_SEARCH_RESULT_CONTENT_NOTE"
  - "CURRENT_MONTH_YEAR"
-->

- Allows Claude to search the web and use the results to inform responses
- Provides up-to-date information for current events and recent data
- Returns search result information formatted as search result blocks${IS_WEBSEARCH_CITATIONS_ENABLED?"":", including links as markdown hyperlinks"}
- Use this tool for accessing information beyond Claude's knowledge cutoff
- Searches are performed automatically within a single API call${WEB_SEARCH_QUOTING_GUIDANCE_BLOCK}
${IS_WEBSEARCH_CITATIONS_ENABLED?`- ${UNTRUSTED_SEARCH_RESULT_CONTENT_NOTE}
`:`
CRITICAL REQUIREMENT - You MUST follow this:
  - After answering the user's question, you MUST include a "Sources:" section at the end of your response
  - In the Sources section, list all relevant URLs from the search results as markdown hyperlinks: [Title](URL)
  - This is MANDATORY - never skip including sources in your response
  - Example format:

    [Your answer here]

    Sources:
    - [Source Title 1](https://example.com/1)
    - [Source Title 2](https://example.com/2)
`}
Usage notes:
  - Domain filtering is supported to include or block specific websites
  - Web search is only available in the US

IMPORTANT - Use the correct year in search queries:
  - The current month is ${CURRENT_MONTH_YEAR}. You MUST use this year when searching for recent information, documentation, or current events.
  - Example: If the user asks for "latest React docs", search for "React documentation" with the current year, NOT last year
