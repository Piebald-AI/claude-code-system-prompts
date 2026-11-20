<!--
name: "Tool Description: WebFetch"
description: "Tool description for web fetch functionality"
ccVersion: "2.1.329"
variables:
  - "GET_WEBFETCH_MCP_TOOL_CONFIG_FN"
  - "WEBFETCH_CACHE_TTL_FN"
-->

- Fetches content from a specified URL and processes it using an AI model
- Takes a URL and a prompt as input
- Fetches the URL content, converts HTML to markdown
- Processes the content with the prompt using a small, fast model
- Returns the model's response about the content
- Use this tool when you need to retrieve and analyze web content

Usage notes:
${GET_WEBFETCH_MCP_TOOL_CONFIG_FN()?"":`  - IMPORTANT: If an MCP-provided web fetch tool is available, prefer using that tool instead of this one, as it may have fewer restrictions.
`}  - The URL must be a fully-formed valid URL
  - HTTP URLs will be automatically upgraded to HTTPS
  - localhost and other hostnames without a dot are not supported${GET_WEBFETCH_MCP_TOOL_CONFIG_FN()?"":"; for a local server, use curl via Bash"}
  - The prompt should describe what information you want to extract from the page
  - This tool is read-only and does not modify any files
  - Results may be summarized if the content is very large
  - Includes a self-cleaning cache (entries expire after ${WEBFETCH_CACHE_TTL_FN()}) for faster responses when repeatedly accessing the same URL
  - When a URL redirects to a different host, the tool will inform you and provide the redirect URL in a special format. You should then make a new WebFetch request with the redirect URL to fetch the content.
  - For GitHub URLs, prefer using the gh CLI via Bash instead (e.g., gh pr view, gh issue view, gh api).
