<!--
name: "Tool Description: WebFetch (concise)"
description: "Concise tool description for WebFetch covering URL fetching, private URL limitations, redirects, and caching"
ccVersion: "2.1.329"
variables:
  - "WEBFETCH_OBSERVABLE_ACTION_NOTE"
  - "FORMAT_CONCISE_ARTIFACT_LINK_NOTE_FN"
  - "ARTIFACT_LINK_HANDLING_MODE"
  - "GET_WEBFETCH_MCP_TOOL_CONFIG_FN"
  - "WEBFETCH_CACHE_TTL_FN"
-->
${WEBFETCH_OBSERVABLE_ACTION_NOTE}Fetches a URL, converts the page to markdown, and answers `prompt` against it using a small fast model.

- Fails on authenticated/private URLs — use an authenticated MCP tool or `gh` for those instead.${FORMAT_CONCISE_ARTIFACT_LINK_NOTE_FN(ARTIFACT_LINK_HANDLING_MODE)}
- Fails on localhost and other hostnames without a dot${GET_WEBFETCH_MCP_TOOL_CONFIG_FN()?"":"; for a local server, use curl via Bash"}.
- HTTP is upgraded to HTTPS. Cross-host redirects are returned to you rather than followed; call again with the redirect URL.
- Responses are cached for ${WEBFETCH_CACHE_TTL_FN()} per URL.
