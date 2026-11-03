<!--
name: "Data: attributionProject setting"
description: "Documents project attribution through claude_proj_ or chan_ IDs and claude_proj_ UUIDs, including empty values, login and connection requirements, environment precedence, managed overrides and trusted-folder settings"
ccVersion: "2.1.318"
-->
The claude.ai Project this session names for your organization's usage reports: the Project's ID, starting with "claude_proj_" or "chan_", or the UUID of a "claude_proj_" Project. An empty string names none and stops lower-precedence files from naming one; the organization default still applies. Sent only when Claude Code uses your claude.ai login, connects directly to the Anthropic API, is not in a cloud session, and CLAUDE_CODE_ATTRIBUTION_HEADER is not 0. CLAUDE_CODE_ATTRIBUTION_PROJECT takes precedence over it. Set in managed settings, it overrides people's own settings files. A project's .claude/settings.json and settings.local.json count only once the folder is trusted; for runs in a folder nobody has trusted, such as CI, use CLAUDE_CODE_ATTRIBUTION_PROJECT.
