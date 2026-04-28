<div>
<div align="right">
<a href="https://piebald.ai"><img width="200" top="20" align="right" src="https://github.com/Piebald-AI/.github/raw/main/Wordmark.svg"></a>
</div>

<div align="left">

### Check out Piebald
We've released **Piebald**, the ultimate agentic AI developer experience. \
Download it and try it out for free!  **https://piebald.ai/**

<a href="https://piebald.ai/discord"><img src="https://img.shields.io/badge/Join%20our%20Discord-5865F2?style=flat&logo=discord&logoColor=white" alt="Join our Discord"></a>
<a href="https://x.com/PiebaldAI"><img src="https://img.shields.io/badge/Follow%20%40PiebaldAI-000000?style=flat&logo=x&logoColor=white" alt="X"></a>

<sub>[**Scroll down for Claude Code's system prompts.**](#claude-code-system-prompts) :point_down:</sub>

</div>
</div>

<div align="left">
<a href="https://piebald.ai">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://piebald.ai/screenshot-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="https://piebald.ai/screenshot-light.png">
  <img alt="hero" width="800" src="https://piebald.ai/screenshot-light.png">
</picture>
</a>
</div>

# Claude Code System Prompts

[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)

> [!important]
> **NEW (January 23, 2026): We've added all of Claude Code's ~40 system reminders to this list&mdash;see [System Reminders](#system-reminders).**

This repository contains an up-to-date list of all Claude Code's various system prompts and their associated token counts as of **[Claude Code v2.1.122](https://www.npmjs.com/package/@anthropic-ai/claude-code/v/2.1.122) (April 28th, 2026).**  It also contains a [**CHANGELOG.md**](./CHANGELOG.md) for the system prompts across 164 versions since v2.0.14.  From the team behind [<img src="https://github.com/Piebald-AI/piebald/raw/main/assets/logo.svg" width="15"> **Piebald.**](https://piebald.ai/)

**This repository is updated within minutes of each Claude Code release.  See the [changelog](./CHANGELOG.md), and follow [@PiebaldAI](https://x.com/PiebaldAI) on X for a summary of the system prompt changes in each release.**

> [!note]
> ⭐ **Star** this repository to get notified about new Claude Code versions.  For each new Claude Code version, we create a release on GitHub, which will notify all users who've starred the repository.

---

Why multiple "system prompts?"

**Claude Code doesn't just have one single string for its system prompt.**

Instead, there are:
- Large portions conditionally added depending on the environment and various configs.
- Descriptions for builtin tools like `Write`, `Bash`, and `TodoWrite`, and some are fairly large.
- Separate system prompts for builtin agents like Explore and Plan.
- Numerous AI-powered utility functions, such as conversation compaction, `CLAUDE.md` generation, session title generation, etc. featuring their own systems prompts.

The result&mdash;110+ strings that are constantly changing and moving within a very large minified JS file.

> [!TIP]
> Want to **modify a particular piece of the system prompt** in your own Claude Code installation?  **Use [tweakcc](https://github.com/Piebald-AI/tweakcc).**  It&mdash;
> - lets you customize the the individual pieces of the system prompt as markdown files, and then
> - patches your npm-based or native (binary) Claude Code installation with them, and also
> - provides diffing and conflict management for when both you and Anthropic have conflicting modifications to the same prompt file.

## Extraction

This repository contains the system prompts extracted using a script from the latest npm version of Claude Code.  As they're extracted directly from Claude Code's compiled source code, they're guaranteed to be exactly what Claude Code uses.  If you use [tweakcc](https://github.com/Piebald-AI/tweakcc) to customize the system prompts, it works in a similar way&mdash;it patches the exact same strings in your local installation as are extracted into this repository.

## Prompts

Note that some prompts contain interpolated bits such as builtin tool name references, lists of available sub agents, and various other context-specific variables, so the actual counts in a particular Claude Code session will differ slightly&mdash;likely not beyond ±20 tokens, however.

### Agent Prompts

Sub-agents and utilities.

#### Sub-agents

- [Agent Prompt: Explore](./system-prompts/agent-prompt-explore.md) (**575** tks) - System prompt for the Explore subagent.
- [Agent Prompt: Plan mode (enhanced)](./system-prompts/agent-prompt-plan-mode-enhanced.md) (**715** tks) - Enhanced prompt for the Plan subagent.

#### Creation Assistants

- [Agent Prompt: Agent creation architect](./system-prompts/agent-prompt-agent-creation-architect.md) (**1110** tks) - System prompt for creating custom AI agents with detailed specifications.
- [Agent Prompt: CLAUDE.md creation](./system-prompts/agent-prompt-claudemd-creation.md) (**384** tks) - System prompt for analyzing codebases and creating CLAUDE.md documentation files.
- [Agent Prompt: Status line setup](./system-prompts/agent-prompt-status-line-setup.md) (**2120** tks) - System prompt for the statusline-setup agent that configures status line display.

#### Slash Commands

- [Agent Prompt: /batch slash command](./system-prompts/agent-prompt-batch-slash-command.md) (**1106** tks) - Instructions for orchestrating a large, parallelizable change across a codebase.
- [Agent Prompt: /rename auto-generate session name](./system-prompts/agent-prompt-rename-auto-generate-session-name.md) (**80** tks) - Prompt used by /rename (no args) to auto-generate a kebab-case session name from conversation context.
- [Agent Prompt: /review-pr slash command](./system-prompts/agent-prompt-review-pr-slash-command.md) (**211** tks) - System prompt for reviewing GitHub pull requests with code analysis.
- [Agent Prompt: /schedule slash command](./system-prompts/agent-prompt-schedule-slash-command.md) (**3130** tks) - Guides the user through scheduling, updating, listing, or running remote Claude Code agents on cron triggers via the Anthropic cloud API.
- [Agent Prompt: /security-review slash command](./system-prompts/agent-prompt-security-review-slash-command.md) (**2521** tks) - Comprehensive security review prompt for analyzing code changes with focus on exploitable vulnerabilities.

#### Utilities

- [Agent Prompt: Auto mode rule reviewer](./system-prompts/agent-prompt-auto-mode-rule-reviewer.md) (**257** tks) - Reviews and critiques user-defined auto mode classifier rules for clarity, completeness, conflicts, and actionability.
- [Agent Prompt: Background agent state classifier](./system-prompts/agent-prompt-background-agent-state-classifier.md) (**848** tks) - Classifies the tail of a background agent transcript as working, blocked, done, or failed and returns concise state JSON.
- [Agent Prompt: Bash command description writer](./system-prompts/agent-prompt-bash-command-description-writer.md) (**207** tks) - Instructions for generating clear, concise command descriptions in active voice for bash commands.
- [Agent Prompt: Bash command prefix detection](./system-prompts/agent-prompt-bash-command-prefix-detection.md) (**823** tks) - System prompt for detecting command prefixes and command injection.
- [Agent Prompt: Claude guide agent](./system-prompts/agent-prompt-claude-guide-agent.md) (**734** tks) - System prompt for the claude-guide agent that helps users understand and use Claude Code, the Claude Agent SDK and the Claude API effectively.
- [Agent Prompt: Coding session title generator](./system-prompts/agent-prompt-coding-session-title-generator.md) (**181** tks) - Generates a title for the coding session.
- [Agent Prompt: Conversation summarization](./system-prompts/agent-prompt-conversation-summarization.md) (**1121** tks) - System prompt for creating detailed conversation summaries.
- [Agent Prompt: Determine which memory files to attach](./system-prompts/agent-prompt-determine-which-memory-files-to-attach.md) (**265** tks) - Agent for determining which memory files to attach for the main agent.
- [Agent Prompt: Dream memory consolidation](./system-prompts/agent-prompt-dream-memory-consolidation.md) (**859** tks) - Instructs an agent to perform a multi-phase memory consolidation pass — orienting on existing memories, gathering recent signal from logs and transcripts, merging updates into topic files, and pruning the index.
- [Agent Prompt: Dream memory pruning](./system-prompts/agent-prompt-dream-memory-pruning.md) (**456** tks) - Instructs an agent to perform a memory pruning pass by deleting stale or invalidated memory files and collapsing duplicates in the memory directory.
- [Agent Prompt: General purpose](./system-prompts/agent-prompt-general-purpose.md) (**285** tks) - System prompt for the general-purpose subagent that searches, analyzes, and edits code across a codebase while reporting findings concisely to the caller.
- [Agent Prompt: Hook condition evaluator (stop)](./system-prompts/agent-prompt-hook-condition-evaluator-stop.md) (**145** tks) - System prompt for evaluating hook conditions, specifically stop conditions, in Claude Code.
- [Agent Prompt: Managed Agents onboarding flow](./system-prompts/agent-prompt-managed-agents-onboarding-flow.md) (**2525** tks) - Interactive interview script that walks users through configuring a Managed Agent from scratch — selecting tools, skills, files, environment settings — and emits setup and runtime code.
- [Agent Prompt: Memory synthesis](./system-prompts/agent-prompt-memory-synthesis.md) (**443** tks) - Subagent that reads persistent memory files and returns a JSON synthesis of only the information relevant to each query, with cited filenames.
- [Agent Prompt: Onboarding guide generator](./system-prompts/agent-prompt-onboarding-guide-generator.md) (**1135** tks) - Co-authors a team onboarding guide (ONBOARDING.md) for new Claude Code users by analyzing the creator's usage data, classifying session types, and iterating on the draft collaboratively.
- [Agent Prompt: Prompt Suggestion Generator v2](./system-prompts/agent-prompt-prompt-suggestion-generator-v2.md) (**296** tks) - V2 instructions for generating prompt suggestions for Claude Code.
- [Agent Prompt: Quick PR creation](./system-prompts/agent-prompt-quick-pr-creation.md) (**986** tks) - Streamlined prompt for creating a commit and pull request with pre-populated context.
- [Agent Prompt: Quick git commit](./system-prompts/agent-prompt-quick-git-commit.md) (**574** tks) - Streamlined prompt for creating a single git commit with pre-populated context.
- [Agent Prompt: Recent Message Summarization](./system-prompts/agent-prompt-recent-message-summarization.md) (**724** tks) - Agent prompt used for summarizing recent messages.
- [Agent Prompt: Security monitor for autonomous agent actions (first part)](./system-prompts/agent-prompt-security-monitor-for-autonomous-agent-actions-first-part.md) (**3196** tks) - Instructs Claude to act as a security monitor that evaluates autonomous coding agent actions against block/allow rules to prevent prompt injection, scope creep, and accidental damage.
- [Agent Prompt: Security monitor for autonomous agent actions (second part)](./system-prompts/agent-prompt-security-monitor-for-autonomous-agent-actions-second-part.md) (**3679** tks) - Defines the environment context, block rules, and allow exceptions that govern which tool actions the agent may or may not perform.
- [Agent Prompt: Session memory update instructions](./system-prompts/agent-prompt-session-memory-update-instructions.md) (**756** tks) - Instructions for updating session memory files during conversations.
- [Agent Prompt: Session search](./system-prompts/agent-prompt-session-search.md) (**158** tks) - Subagent prompt for searching past Claude Code conversation sessions by scanning .jsonl transcript files and returning matching session IDs.
- [Agent Prompt: Session title and branch generation](./system-prompts/agent-prompt-session-title-and-branch-generation.md) (**307** tks) - Agent for generating succinct session titles and git branch names.
- [Agent Prompt: Verification specialist](./system-prompts/agent-prompt-verification-specialist.md) (**2885** tks) - System prompt for a verification subagent that adversarially tests implementations by running builds, test suites, linters, and adversarial probes, then issuing a PASS/FAIL/PARTIAL verdict.
- [Agent Prompt: WebFetch summarizer](./system-prompts/agent-prompt-webfetch-summarizer.md) (**189** tks) - Prompt for agent that summarizes verbose output from WebFetch for the main model.
- [Agent Prompt: Worker fork](./system-prompts/agent-prompt-worker-fork.md) (**258** tks) - System prompt for a forked worker sub-agent that executes a single directive from the parent agent and reports back concisely.

### Data

The content of various template files embedded in Claude Code.

- [Data: Anthropic CLI](./system-prompts/data-anthropic-cli.md) (**2878** tks) - Reference documentation for the ant CLI covering installation, authentication, command structure, input and output shaping, managed agents workflows, and scripting patterns.
- [Data: Assistant voice and values template](./system-prompts/data-assistant-voice-and-values-template.md) (**454** tks) - Template content for an assistant.md file describing Claude's voice, values, and communication style.
- [Data: Background agent state classification examples](./system-prompts/data-background-agent-state-classification-examples.md) (**510** tks) - Example assistant-message tails and JSON outputs for classifying background agent state, tempo, needs, and result.
- [Data: Claude API reference — C#](./system-prompts/data-claude-api-reference-c.md) (**4341** tks) - C# SDK reference including installation, client initialization, basic requests, streaming, and tool use.
- [Data: Claude API reference — Go](./system-prompts/data-claude-api-reference-go.md) (**4294** tks) - Go SDK reference.
- [Data: Claude API reference — Java](./system-prompts/data-claude-api-reference-java.md) (**4506** tks) - Java SDK reference including installation, client initialization, basic requests, streaming, and beta tool use.
- [Data: Claude API reference — PHP](./system-prompts/data-claude-api-reference-php.md) (**3486** tks) - PHP SDK reference.
- [Data: Claude API reference — Python](./system-prompts/data-claude-api-reference-python.md) (**4391** tks) - Python SDK reference including installation, client initialization, basic requests, thinking, and multi-turn conversation.
- [Data: Claude API reference — Ruby](./system-prompts/data-claude-api-reference-ruby.md) (**923** tks) - Ruby SDK reference including installation, client initialization, basic requests, streaming, and beta tool runner.
- [Data: Claude API reference — TypeScript](./system-prompts/data-claude-api-reference-typescript.md) (**2915** tks) - TypeScript SDK reference including installation, client initialization, basic requests, thinking, and multi-turn conversation.
- [Data: Claude API reference — cURL](./system-prompts/data-claude-api-reference-curl.md) (**2201** tks) - Raw API reference for Claude API for use with cURL or else Raw HTTP.
- [Data: Claude model catalog](./system-prompts/data-claude-model-catalog.md) (**2278** tks) - Catalog of current and legacy Claude models with exact model IDs, aliases, context windows, and pricing.
- [Data: Files API reference — Python](./system-prompts/data-files-api-reference-python.md) (**1360** tks) - Python Files API reference including file upload, listing, deletion, and usage in messages.
- [Data: Files API reference — TypeScript](./system-prompts/data-files-api-reference-typescript.md) (**797** tks) - TypeScript Files API reference including file upload, listing, deletion, and usage in messages.
- [Data: GitHub Actions workflow for @claude mentions](./system-prompts/data-github-actions-workflow-for-claude-mentions.md) (**525** tks) - GitHub Actions workflow template for triggering Claude Code via @claude mentions.
- [Data: GitHub App installation PR description](./system-prompts/data-github-app-installation-pr-description.md) (**409** tks) - Template for PR description when installing Claude Code GitHub App integration.
- [Data: HTTP error codes reference](./system-prompts/data-http-error-codes-reference.md) (**2124** tks) - Reference for HTTP error codes returned by the Claude API with common causes and handling strategies.
- [Data: Live documentation sources](./system-prompts/data-live-documentation-sources.md) (**3639** tks) - WebFetch URLs for fetching current Claude API and Agent SDK documentation from official sources.
- [Data: Managed Agents client patterns](./system-prompts/data-managed-agents-client-patterns.md) (**2685** tks) - Reference guide of common client-side patterns for driving Managed Agent sessions, including stream reconnection, idle-break gating, tool confirmations, interrupts, and custom tools.
- [Data: Managed Agents core concepts](./system-prompts/data-managed-agents-core-concepts.md) (**3531** tks) - Reference documentation for the Managed Agents API covering core concepts (Agents, Sessions, Environments, Containers), lifecycle, versioning, endpoints, and usage patterns.
- [Data: Managed Agents endpoint reference](./system-prompts/data-managed-agents-endpoint-reference.md) (**5868** tks) - Comprehensive reference for Managed Agents API endpoints, SDK methods, request/response schemas, error handling, and rate limits.
- [Data: Managed Agents environments and resources](./system-prompts/data-managed-agents-environments-and-resources.md) (**2950** tks) - Reference documentation covering Managed Agents environments, file resources, GitHub repository mounting, and the Files API with SDK examples.
- [Data: Managed Agents events and steering](./system-prompts/data-managed-agents-events-and-steering.md) (**2428** tks) - Reference guide for sending and receiving events on managed agent sessions, including streaming, polling, reconnection, message queuing, interrupts, and event payload details.
- [Data: Managed Agents memory stores reference](./system-prompts/data-managed-agents-memory-stores-reference.md) (**2780** tks) - Reference documentation for Managed Agents memory stores, including store creation, session attachment, FUSE mounts, memory CRUD, concurrency, versions, redaction, and endpoint paths.
- [Data: Managed Agents overview](./system-prompts/data-managed-agents-overview.md) (**2316** tks) - Provides the agent with a comprehensive overview of the Managed Agents API architecture, mandatory agent-then-session flow, beta headers, documentation reading guide, and common pitfalls.
- [Data: Managed Agents reference — Python](./system-prompts/data-managed-agents-reference-python.md) (**2841** tks) - Reference guide for using the Anthropic Python SDK to create and manage agents, sessions, environments, streaming, custom tools, files, and MCP servers.
- [Data: Managed Agents reference — TypeScript](./system-prompts/data-managed-agents-reference-typescript.md) (**2855** tks) - Reference guide for using the Anthropic TypeScript SDK to create and manage agents, sessions, environments, streaming, custom tools, file uploads, and MCP server integration.
- [Data: Managed Agents reference — cURL](./system-prompts/data-managed-agents-reference-curl.md) (**2641** tks) - Provides cURL and raw HTTP request examples for the Managed Agents API including environment, agent, and session lifecycle operations.
- [Data: Managed Agents tools and skills](./system-prompts/data-managed-agents-tools-and-skills.md) (**3844** tks) - Reference documentation covering the Managed Agents SDK's tool types (agent toolset, MCP, custom), permission policies, vault credential management, and skills API for building specialized agents.
- [Data: Message Batches API reference — Python](./system-prompts/data-message-batches-api-reference-python.md) (**1635** tks) - Python Batches API reference including batch creation, status polling, and result retrieval at 50% cost.
- [Data: Prompt Caching — Design & Optimization](./system-prompts/data-prompt-caching-design-optimization.md) (**2664** tks) - Document on how to design prompt-building code for effective caching, including placement patterns and anti-patterns.
- [Data: Session memory template](./system-prompts/data-session-memory-template.md) (**292** tks) - Template structure for session memory `summary.md` files.
- [Data: Streaming reference — Python](./system-prompts/data-streaming-reference-python.md) (**1660** tks) - Python streaming reference including sync/async streaming and handling different content types.
- [Data: Streaming reference — TypeScript](./system-prompts/data-streaming-reference-typescript.md) (**1612** tks) - TypeScript streaming reference including basic streaming and handling different content types.
- [Data: Tool use concepts](./system-prompts/data-tool-use-concepts.md) (**4147** tks) - Conceptual foundations of tool use with the Claude API including tool definitions, tool choice, and best practices.
- [Data: Tool use reference — Python](./system-prompts/data-tool-use-reference-python.md) (**5106** tks) - Python tool use reference including tool runner, manual agentic loop, code execution, and structured outputs.
- [Data: Tool use reference — TypeScript](./system-prompts/data-tool-use-reference-typescript.md) (**5033** tks) - TypeScript tool use reference including tool runner, manual agentic loop, code execution, and structured outputs.
- [Data: User profile memory template](./system-prompts/data-user-profile-memory-template.md) (**232** tks) - Template content for the user profile memory file, covering personal details, work context, schedule, and communication preferences.

### System Prompt

Parts of the main system prompt.

- [System Prompt: Advisor tool instructions](./system-prompts/system-prompt-advisor-tool-instructions.md) (**443** tks) - Instructions for using the Advisor tool.
- [System Prompt: Agent Summary Generation](./system-prompts/system-prompt-agent-summary-generation.md) (**178** tks) - System prompt used for "Agent Summary" generation.
- [System Prompt: Agent memory instructions](./system-prompts/system-prompt-agent-memory-instructions.md) (**337** tks) - Instructions for including memory update guidance in agent system prompts.
- [System Prompt: Agent thread notes](./system-prompts/system-prompt-agent-thread-notes.md) (**159** tks) - Behavioral guidelines for agent threads covering absolute paths, response formatting, emoji avoidance, and tool call punctuation.
- [System Prompt: Auto mode](./system-prompts/system-prompt-auto-mode.md) (**255** tks) - Continuous task execution, akin to a background agent.
- [System Prompt: Autonomous loop check](./system-prompts/system-prompt-autonomous-loop-check.md) (**1071** tks) - Defines behavior for autonomous timer-based invocations, guiding Claude to continue established work, maintain PRs, and handle repeated idle checks while the user is away.
- [System Prompt: Avoiding Unnecessary Sleep Commands (part of PowerShell tool description)](./system-prompts/system-prompt-avoiding-unnecessary-sleep-commands-part-of-powershell-tool-description.md) (**175** tks) - Guidelines for avoiding unnecessary sleep commands in PowerShell scripts, including alternatives for waiting and notification.
- [System Prompt: Background job behavior](./system-prompts/system-prompt-background-job-behavior.md) (**349** tks) - Instructs background job agents to narrate progress, restate results in message text for classifier extraction, and signal done/blocked/failed status.
- [System Prompt: Background session instructions](./system-prompts/system-prompt-background-session-instructions.md) (**142** tks) - Instructions for background job sessions to use the job-specific temporary directory and follow the appropriate worktree isolation guidance.
- [System Prompt: Censoring assistance with malicious activities](./system-prompts/system-prompt-censoring-assistance-with-malicious-activities.md) (**98** tks) - Guidelines for assisting with authorized security testing, defensive security, CTF challenges, and educational contexts while censoring requests for malicious activities.
- [System Prompt: Chrome browser MCP tools](./system-prompts/system-prompt-chrome-browser-mcp-tools.md) (**156** tks) - Instructions for loading Chrome browser MCP tools via MCPSearch before use.
- [System Prompt: Claude in Chrome browser automation](./system-prompts/system-prompt-claude-in-chrome-browser-automation.md) (**759** tks) - Instructions for using Claude in Chrome browser automation tools effectively.
- [System Prompt: Communication style](./system-prompts/system-prompt-communication-style.md) (**297** tks) - Instructs Claude to give brief, user-facing updates at key moments during tool use, write concise end-of-turn summaries, match response format to task complexity, and avoid comments and planning documents in code.
- [System Prompt: Context compaction summary](./system-prompts/system-prompt-context-compaction-summary.md) (**278** tks) - Prompt used for context compaction summary (for the SDK).
- [System Prompt: Description part of memory instructions](./system-prompts/system-prompt-description-part-of-memory-instructions.md) (**148** tks) - Field for describing _what_ the memory is.  Part of a bigger effort to instruct Claude how to create memories.
- [System Prompt: Doing tasks (ambitious tasks)](./system-prompts/system-prompt-doing-tasks-ambitious-tasks.md) (**47** tks) - Allow users to complete ambitious tasks; defer to user judgement on scope.
- [System Prompt: Doing tasks (help and feedback)](./system-prompts/system-prompt-doing-tasks-help-and-feedback.md) (**24** tks) - How to inform users about help and feedback channels.
- [System Prompt: Doing tasks (no compatibility hacks)](./system-prompts/system-prompt-doing-tasks-no-compatibility-hacks.md) (**52** tks) - Delete unused code completely rather than adding compatibility shims.
- [System Prompt: Doing tasks (no unnecessary error handling)](./system-prompts/system-prompt-doing-tasks-no-unnecessary-error-handling.md) (**64** tks) - Do not add error handling for impossible scenarios; only validate at boundaries.
- [System Prompt: Doing tasks (security)](./system-prompts/system-prompt-doing-tasks-security.md) (**67** tks) - Avoid introducing security vulnerabilities like injection, XSS, etc.
- [System Prompt: Doing tasks (software engineering focus)](./system-prompts/system-prompt-doing-tasks-software-engineering-focus.md) (**104** tks) - Users primarily request software engineering tasks; interpret instructions in that context.
- [System Prompt: Dream CLAUDE.md memory reconciliation](./system-prompts/system-prompt-dream-claudemd-memory-reconciliation.md) (**279** tks) - Instructs dream memory consolidation to reconcile feedback and project memories against CLAUDE.md, deleting stale memories or flagging possible CLAUDE.md drift.
- [System Prompt: Dream team memory handling](./system-prompts/system-prompt-dream-team-memory-handling.md) (**279** tks) - Instructions for handling shared team memories during dream consolidation, including deduplication, conservative pruning rules, and avoiding accidental promotion of personal memories.
- [System Prompt: Executing actions with care](./system-prompts/system-prompt-executing-actions-with-care.md) (**590** tks) - Instructions for executing actions carefully.
- [System Prompt: Fork usage guidelines](./system-prompts/system-prompt-fork-usage-guidelines.md) (**323** tks) - Instructions for when to fork subagents and rules against reading fork output mid-flight or fabricating fork results.
- [System Prompt: Git status](./system-prompts/system-prompt-git-status.md) (**37** tks) - System prompt for displaying the current git status at the start of the conversation.
- [System Prompt: Harness instructions](./system-prompts/system-prompt-harness-instructions.md) (**193** tks) - Core interactive-agent identity and harness instructions for terminal markdown output, permissions, system reminders, compaction, tool use, and code references.
- [System Prompt: Hooks Configuration](./system-prompts/system-prompt-hooks-configuration.md) (**1493** tks) - System prompt for hooks configuration.  Used for above Claude Code config skill.
- [System Prompt: How to use the SendUserMessage tool](./system-prompts/system-prompt-how-to-use-the-sendusermessage-tool.md) (**283** tks) - Instructions for using the SendUserMessage tool.
- [System Prompt: Insights at a glance summary](./system-prompts/system-prompt-insights-at-a-glance-summary.md) (**569** tks) - Generates a concise 4-part summary (what's working, hindrances, quick wins, ambitious workflows) for the insights report.
- [System Prompt: Insights friction analysis](./system-prompts/system-prompt-insights-friction-analysis.md) (**139** tks) - Analyzes aggregated usage data to identify friction patterns and categorize recurring issues.
- [System Prompt: Insights on the horizon](./system-prompts/system-prompt-insights-on-the-horizon.md) (**148** tks) - Identifies ambitious future workflows and opportunities for autonomous AI-assisted development.
- [System Prompt: Insights session facets extraction](./system-prompts/system-prompt-insights-session-facets-extraction.md) (**310** tks) - Extracts structured facets (goal categories, satisfaction, friction) from a single Claude Code session transcript.
- [System Prompt: Insights suggestions](./system-prompts/system-prompt-insights-suggestions.md) (**748** tks) - Generates actionable suggestions including CLAUDE.md additions, features to try, and usage patterns.
- [System Prompt: Learning mode (insights)](./system-prompts/system-prompt-learning-mode-insights.md) (**142** tks) - Instructions for providing educational insights when learning mode is active.
- [System Prompt: Learning mode](./system-prompts/system-prompt-learning-mode.md) (**1042** tks) - Main system prompt for learning mode with human collaboration instructions.
- [System Prompt: Memory description of user details](./system-prompts/system-prompt-memory-description-of-user-details.md) (**122** tks) - Describes the purpose and guidelines for per-user memory files that accumulate details about the user's role, goals, knowledge, and preferences across sessions.
- [System Prompt: Memory description of user feedback (with explicit save)](./system-prompts/system-prompt-memory-description-of-user-feedback-with-explicit-save.md) (**146** tks) - Describes the feedback memory type that captures user guidance on work approaches, emphasizing recording both successes and failures and explicitly instructing to save a new memory noting contradictions with team feedback.
- [System Prompt: Memory description of user feedback](./system-prompts/system-prompt-memory-description-of-user-feedback.md) (**139** tks) - Describes the user feedback memory type that stores guidance about work approaches, emphasizing recording both successes and failures and checking for contradictions with team memories.
- [System Prompt: Memory instructions](./system-prompts/system-prompt-memory-instructions.md) (**355** tks) - Instructions for using persistent file-based memory, including memory file format, scope, indexing, and stale-memory handling.
- [System Prompt: Memory staleness verification](./system-prompts/system-prompt-memory-staleness-verification.md) (**112** tks) - Instructs the agent to verify memory records against current file/resource state and delete stale memories that conflict with observed reality.
- [System Prompt: Minimal mode](./system-prompts/system-prompt-minimal-mode.md) (**164** tks) - Describes the behavior and constraints of minimal mode, which skips hooks, LSP, plugins, auto-memory, and other features while requiring explicit context via CLI flags.
- [System Prompt: One of six rules for using sleep command](./system-prompts/system-prompt-one-of-six-rules-for-using-sleep-command.md) (**23** tks) - One of the six rules for using the sleep command.
- [System Prompt: Option previewer](./system-prompts/system-prompt-option-previewer.md) (**151** tks) - System prompt for previewing UI options in a side-by-side layout.
- [System Prompt: Parallel tool call note (part of "Tool usage policy")](./system-prompts/system-prompt-parallel-tool-call-note-part-of-tool-usage-policy.md) (**102** tks) - System prompt for telling Claude to using parallel tool calls.
- [System Prompt: Partial compaction instructions](./system-prompts/system-prompt-partial-compaction-instructions.md) (**725** tks) - Instructions on how to compact when the user decided to compact only a portion of the conversation, with a structured summary format and analysis process.
- [System Prompt: PowerShell edition for 5.1](./system-prompts/system-prompt-powershell-edition-for-51.md) (**285** tks) - System prompt for providing information about Windows PowerShell 5.1.
- [System Prompt: Proactive schedule offer after follow-up work](./system-prompts/system-prompt-proactive-schedule-offer-after-follow-up-work.md) (**272** tks) - Instructs the agent to offer a one-line /schedule follow-up only when completed work has a strong natural future action and the user is likely to want it.
- [System Prompt: REPL tool usage and scripting conventions](./system-prompts/system-prompt-repl-tool-usage-and-scripting-conventions.md) (**989** tks) - Instructs Claude on how to use the REPL tool effectively with dense JavaScript scripts, shorthands, batching rules, and API reference for investigation tasks.
- [System Prompt: Remote plan mode (ultraplan)](./system-prompts/system-prompt-remote-plan-mode-ultraplan.md) (**617** tks) - System reminder injected during remote planning sessions that instructs Claude to explore the codebase, produce a diagram-rich plan via ExitPlanMode, and implement it with a pull request upon approval.
- [System Prompt: Remote planning session](./system-prompts/system-prompt-remote-planning-session.md) (**432** tks) - System reminder that configures a remote planning session to explore the codebase, produce an implementation plan via ExitPlanMode, and handle plan approval, rejection, or teleportation back to the user's local terminal.
- [System Prompt: Scratchpad directory](./system-prompts/system-prompt-scratchpad-directory.md) (**170** tks) - Instructions for using a dedicated scratchpad directory for temporary files.
- [System Prompt: Skillify Current Session](./system-prompts/system-prompt-skillify-current-session.md) (**1798** tks) - System prompt for converting the current session in to a skill.
- [System Prompt: Subagent delegation examples](./system-prompts/system-prompt-subagent-delegation-examples.md) (**606** tks) - Provides example interactions showing how a coordinator agent should delegate tasks to subagents, handle waiting states, and report results.
- [System Prompt: Subagent prompt-writing examples](./system-prompts/system-prompt-subagent-prompt-writing-examples.md) (**439** tks) - Provides example usage patterns demonstrating how to write self-contained, well-structured prompts when delegating tasks to subagents.
- [System Prompt: Tone and style (code references)](./system-prompts/system-prompt-tone-and-style-code-references.md) (**39** tks) - Instruction to include file_path:line_number when referencing code.
- [System Prompt: Tone and style (concise output — short)](./system-prompts/system-prompt-tone-and-style-concise-output-short.md) (**16** tks) - Instruction for short and concise responses.
- [System Prompt: Tool execution denied](./system-prompts/system-prompt-tool-execution-denied.md) (**144** tks) - System prompt for when tool execution is denied.
- [System Prompt: Tool usage (subagent guidance)](./system-prompts/system-prompt-tool-usage-subagent-guidance.md) (**103** tks) - Guidance on when and how to use subagents effectively.
- [System Prompt: Tool usage (task management)](./system-prompts/system-prompt-tool-usage-task-management.md) (**70** tks) - Use TodoWrite to break down and track work progress.
- [System Prompt: WSL managed settings double opt-in](./system-prompts/system-prompt-wsl-managed-settings-double-opt-in.md) (**152** tks) - Explains that WSL can read the Windows managed settings policy chain only when the admin-enabled flag is set, with HKCU requiring an additional user opt-in.
- [System Prompt: Worker instructions](./system-prompts/system-prompt-worker-instructions.md) (**272** tks) - Instructions for workers to follow when implementing a change.
- [System Prompt: Writing subagent prompts](./system-prompts/system-prompt-writing-subagent-prompts.md) (**287** tks) - Guidelines for writing effective prompts when delegating tasks to subagents, covering context-inheriting vs fresh subagent scenarios.

### System Reminders

Text for large system reminders.

- [System Reminder: /btw side question](./system-prompts/system-reminder-btw-side-question.md) (**244** tks) - System reminder for /btw slash command side questions without tools.
- [System Reminder: Agent mention](./system-prompts/system-reminder-agent-mention.md) (**45** tks) - Notification that user wants to invoke an agent.
- [System Reminder: Compact file reference](./system-prompts/system-reminder-compact-file-reference.md) (**57** tks) - Reference to file read before conversation summarization.
- [System Reminder: Exited plan mode](./system-prompts/system-reminder-exited-plan-mode.md) (**41** tks) - Notification when exiting plan mode.
- [System Reminder: File exists but empty](./system-prompts/system-reminder-file-exists-but-empty.md) (**27** tks) - Warning when reading an empty file.
- [System Reminder: File modified by user or linter](./system-prompts/system-reminder-file-modified-by-user-or-linter.md) (**97** tks) - Notification that a file was modified externally.
- [System Reminder: File opened in IDE](./system-prompts/system-reminder-file-opened-in-ide.md) (**37** tks) - Notification that user opened a file in IDE.
- [System Reminder: File shorter than offset](./system-prompts/system-reminder-file-shorter-than-offset.md) (**59** tks) - Warning when file read offset exceeds file length.
- [System Reminder: File truncated](./system-prompts/system-reminder-file-truncated.md) (**74** tks) - Notification that file was truncated due to size.
- [System Reminder: Hook additional context](./system-prompts/system-reminder-hook-additional-context.md) (**35** tks) - Additional context from a hook.
- [System Reminder: Hook blocking error](./system-prompts/system-reminder-hook-blocking-error.md) (**52** tks) - Error from a blocking hook command.
- [System Reminder: Hook stopped continuation prefix](./system-prompts/system-reminder-hook-stopped-continuation-prefix.md) (**12** tks) - Prefix for hook stopped continuation messages.
- [System Reminder: Hook stopped continuation](./system-prompts/system-reminder-hook-stopped-continuation.md) (**30** tks) - Message when a hook stops continuation.
- [System Reminder: Hook success](./system-prompts/system-reminder-hook-success.md) (**29** tks) - Success message from a hook.
- [System Reminder: Lines selected in IDE](./system-prompts/system-reminder-lines-selected-in-ide.md) (**66** tks) - Notification about lines selected by user in IDE.
- [System Reminder: MCP resource no content](./system-prompts/system-reminder-mcp-resource-no-content.md) (**41** tks) - Shown when MCP resource has no content.
- [System Reminder: MCP resource no displayable content](./system-prompts/system-reminder-mcp-resource-no-displayable-content.md) (**43** tks) - Shown when MCP resource has no displayable content.
- [System Reminder: Malware analysis after Read tool call](./system-prompts/system-reminder-malware-analysis-after-read-tool-call.md) (**87** tks) - Instructions for analyzing malware without improving or augmenting it.
- [System Reminder: Memory file contents](./system-prompts/system-reminder-memory-file-contents.md) (**36** tks) - Contents of a memory file by path.
- [System Reminder: Nested memory contents](./system-prompts/system-reminder-nested-memory-contents.md) (**33** tks) - Contents of a nested memory file.
- [System Reminder: New diagnostics detected](./system-prompts/system-reminder-new-diagnostics-detected.md) (**52** tks) - Notification about new diagnostic issues.
- [System Reminder: Output style active](./system-prompts/system-reminder-output-style-active.md) (**32** tks) - Notification that an output style is active.
- [System Reminder: Plan file reference](./system-prompts/system-reminder-plan-file-reference.md) (**62** tks) - Reference to an existing plan file.
- [System Reminder: Plan mode approval tool enforcement](./system-prompts/system-reminder-plan-mode-approval-tool-enforcement.md) (**236** tks) - Requires plan mode turns to end with either AskUserQuestion for clarification or ExitPlanMode for plan approval, and forbids asking for approval any other way.
- [System Reminder: Plan mode is active (5-phase)](./system-prompts/system-reminder-plan-mode-is-active-5-phase.md) (**927** tks) - Enhanced plan mode system reminder with parallel exploration and multi-agent planning.
- [System Reminder: Plan mode is active (iterative)](./system-prompts/system-reminder-plan-mode-is-active-iterative.md) (**936** tks) - Iterative plan mode system reminder for main agent with user interviewing workflow.
- [System Reminder: Plan mode is active (subagent)](./system-prompts/system-reminder-plan-mode-is-active-subagent.md) (**307** tks) - Simplified plan mode system reminder for sub agents.
- [System Reminder: Plan mode re-entry](./system-prompts/system-reminder-plan-mode-re-entry.md) (**236** tks) - System reminder sent when the user enters Plan mode after having previously exited it either via shift+tab or by approving Claude's plan.
- [System Reminder: Previously invoked skills](./system-prompts/system-reminder-previously-invoked-skills.md) (**131** tks) - Restores skills invoked before conversation compaction as context only, warning not to re-execute their setup actions or treat prior inputs as current instructions.
- [System Reminder: Session continuation](./system-prompts/system-reminder-session-continuation.md) (**37** tks) - Notification that session continues from another machine.
- [System Reminder: Stop hook blocking error](./system-prompts/system-reminder-stop-hook-blocking-error.md) (**20** tks) - Error from a blocking hook command.
- [System Reminder: Task tools reminder](./system-prompts/system-reminder-task-tools-reminder.md) (**123** tks) - Reminder to use task tracking tools.
- [System Reminder: Team Coordination](./system-prompts/system-reminder-team-coordination.md) (**250** tks) - System reminder for team coordination.
- [System Reminder: Team Shutdown](./system-prompts/system-reminder-team-shutdown.md) (**136** tks) - System reminder for team shutdown.
- [System Reminder: Thinking frequency tuning](./system-prompts/system-reminder-thinking-frequency-tuning.md) (**119** tks) - Instructs Claude to treat system-reminder tags as harness instructions and calibrate thinking frequency based on task complexity.
- [System Reminder: TodoWrite reminder](./system-prompts/system-reminder-todowrite-reminder.md) (**98** tks) - Reminder to use TodoWrite tool for task tracking.
- [System Reminder: Token usage](./system-prompts/system-reminder-token-usage.md) (**39** tks) - Current token usage statistics.
- [System Reminder: USD budget](./system-prompts/system-reminder-usd-budget.md) (**42** tks) - Current USD budget statistics.
- [System Reminder: Ultraplan mode](./system-prompts/system-reminder-ultraplan-mode.md) (**437** tks) - System reminder for using Ultraplan mode to create a detailed implementation plan with multi-agent exploration and critique.
- [System Reminder: Verify plan reminder](./system-prompts/system-reminder-verify-plan-reminder.md) (**47** tks) - Reminder to verify completed plan.

### Builtin Tool Descriptions

- [Tool Description: AskUserQuestion](./system-prompts/tool-description-askuserquestion.md) (**287** tks) - Tool description for asking user questions.
- [Tool Description: BrowserBatch](./system-prompts/tool-description-browserbatch.md) (**159** tks) - Tool description for BrowserBatch, which executes multiple browser tool calls sequentially in one round trip.
- [Tool Description: Computer](./system-prompts/tool-description-computer.md) (**161** tks) - Main description for the Chrome browser computer automation tool.
- [Tool Description: CronCreate](./system-prompts/tool-description-croncreate.md) (**948** tks) - Describes the CronCreate tool for enqueuing one-shot or recurring cron-based jobs with jitter and off-minute scheduling guidance.
- [Tool Description: Edit](./system-prompts/tool-description-edit.md) (**202** tks) - Tool for performing exact string replacements in files.
- [Tool Description: EnterPlanMode](./system-prompts/tool-description-enterplanmode.md) (**878** tks) - Tool description for entering plan mode to explore and design implementation approaches.
- [Tool Description: EnterWorktree](./system-prompts/tool-description-enterworktree.md) (**565** tks) - Tool description for the EnterWorktree tool.
- [Tool Description: ExitPlanMode](./system-prompts/tool-description-exitplanmode.md) (**417** tks) - Description for the ExitPlanMode tool, which presents a plan dialog for the user to approve.
- [Tool Description: ExitWorktree](./system-prompts/tool-description-exitworktree.md) (**527** tks) - Roughly, the reverse of the ExitWorktree.
- [Tool Description: Grep](./system-prompts/tool-description-grep.md) (**300** tks) - Tool description for content search using ripgrep.
- [Tool Description: LSP](./system-prompts/tool-description-lsp.md) (**255** tks) - Description for the LSP tool.
- [Tool Description: NotebookEdit](./system-prompts/tool-description-notebookedit.md) (**121** tks) - Tool description for editing Jupyter notebook cells.
- [Tool Description: PowerShell](./system-prompts/tool-description-powershell.md) (**1455** tks) - Describes the PowerShell command execution tool with syntax guidance, timeout settings, and instructions to prefer specialized tools over PowerShell for file operations.
- [Tool Description: PushNotification](./system-prompts/tool-description-pushnotification.md) (**261** tks) - Tool description for PushNotification. This is a tool that sends a desktop notification in the user's terminal and pushes to their phone if Remote Control is connected.
- [Tool Description: REPL](./system-prompts/tool-description-repl.md) (**715** tks) - Describes the REPL tool, a JavaScript programming interface for looping, branching, and composing Claude Code tool calls as async functions.
- [Tool Description: ReadFile](./system-prompts/tool-description-readfile.md) (**427** tks) - Tool description for reading files.
- [Tool Description: Schedule proactive offer guidance](./system-prompts/tool-description-schedule-proactive-offer-guidance.md) (**229** tks) - Explains when to use the scheduling tool for recurring or one-time remote agents and when to proactively offer scheduling after successful work.
- [Tool Description: SendMessageTool](./system-prompts/tool-description-sendmessagetool.md) (**332** tks) - Agent teams version of SendMessageTool.
- [Tool Description: Skill](./system-prompts/tool-description-skill.md) (**306** tks) - Tool description for executing skills in the main conversation.
- [Tool Description: TaskCreate](./system-prompts/tool-description-taskcreate.md) (**499** tks) - Tool description for TaskCreate tool.
- [Tool Description: TeamDelete](./system-prompts/tool-description-teamdelete.md) (**154** tks) - Tool description for the TeamDelete tool.
- [Tool Description: TeammateTool](./system-prompts/tool-description-teammatetool.md) (**1585** tks) - Tool for managing teams and coordinating teammates in a swarm.
- [Tool Description: TodoWrite](./system-prompts/tool-description-todowrite.md) (**2037** tks) - Tool description for creating and managing task lists.
- [Tool Description: WebFetch](./system-prompts/tool-description-webfetch.md) (**297** tks) - Tool description for web fetch functionality.
- [Tool Description: WebSearch](./system-prompts/tool-description-websearch.md) (**319** tks) - Tool description for web search functionality.
- [Tool Description: Write](./system-prompts/tool-description-write.md) (**129** tks) - Tool for writing files to the local filesystem.

**Additional notes for some Tool Descriptions**

- [Tool Description: Agent (usage notes)](./system-prompts/tool-description-agent-usage-notes.md) (**791** tks) - Usage notes and instructions for the Task/Agent tool, including guidance on launching subagents, background execution, resumption, and worktree isolation.
- [Tool Description: AskUserQuestion (preview field)](./system-prompts/tool-description-askuserquestion-preview-field.md) (**134** tks) - Instructions for using the HTML preview field on single-select question options to display visual artifacts like UI mockups, code snippets, and diagrams.
- [Tool Description: Background monitor (streaming events)](./system-prompts/tool-description-background-monitor-streaming-events.md) (**1401** tks) - Describes the background monitor tool that streams stdout events from long-running scripts as chat notifications, with guidelines on script quality, output volume, and selective filtering.
- [Tool Description: Bash (Git commit and PR creation instructions)](./system-prompts/tool-description-bash-git-commit-and-pr-creation-instructions.md) (**1611** tks) - Instructions for creating git commits and GitHub pull requests.
- [Tool Description: Bash (alternative — communication)](./system-prompts/tool-description-bash-alternative-communication.md) (**18** tks) - Bash tool alternative: output text directly instead of echo/printf.
- [Tool Description: Bash (alternative — content search)](./system-prompts/tool-description-bash-alternative-content-search.md) (**27** tks) - Bash tool alternative: use Grep for content search instead of grep/rg.
- [Tool Description: Bash (alternative — edit files)](./system-prompts/tool-description-bash-alternative-edit-files.md) (**27** tks) - Bash tool alternative: use Edit for file editing instead of sed/awk.
- [Tool Description: Bash (alternative — file search)](./system-prompts/tool-description-bash-alternative-file-search.md) (**26** tks) - Bash tool alternative: use Glob for file search instead of find/ls.
- [Tool Description: Bash (alternative — read files)](./system-prompts/tool-description-bash-alternative-read-files.md) (**27** tks) - Bash tool alternative: use Read for file reading instead of cat/head/tail.
- [Tool Description: Bash (alternative — write files)](./system-prompts/tool-description-bash-alternative-write-files.md) (**29** tks) - Bash tool alternative: use Write for file writing instead of echo/cat.
- [Tool Description: Bash (built-in tools note)](./system-prompts/tool-description-bash-built-in-tools-note.md) (**53** tks) - Note that built-in tools provide better UX than Bash equivalents.
- [Tool Description: Bash (git — avoid destructive ops)](./system-prompts/tool-description-bash-git-avoid-destructive-ops.md) (**58** tks) - Bash tool git instruction: consider safer alternatives to destructive operations.
- [Tool Description: Bash (git — never skip hooks)](./system-prompts/tool-description-bash-git-never-skip-hooks.md) (**59** tks) - Bash tool git instruction: never skip hooks or bypass signing unless user requests it.
- [Tool Description: Bash (git — prefer new commits)](./system-prompts/tool-description-bash-git-prefer-new-commits.md) (**22** tks) - Bash tool git instruction: prefer new commits over amending.
- [Tool Description: Bash (maintain cwd)](./system-prompts/tool-description-bash-maintain-cwd.md) (**81** tks) - Bash tool instruction: use absolute paths and avoid cd.
- [Tool Description: Bash (no newlines)](./system-prompts/tool-description-bash-no-newlines.md) (**24** tks) - Bash tool instruction: do not use newlines to separate commands.
- [Tool Description: Bash (overview)](./system-prompts/tool-description-bash-overview.md) (**19** tks) - Opening line of the Bash tool description.
- [Tool Description: Bash (parallel commands)](./system-prompts/tool-description-bash-parallel-commands.md) (**72** tks) - Bash tool instruction: run independent commands as parallel tool calls.
- [Tool Description: Bash (prefer dedicated tools)](./system-prompts/tool-description-bash-prefer-dedicated-tools.md) (**71** tks) - Warning to prefer dedicated tools over Bash for find, grep, cat, etc.
- [Tool Description: Bash (quote file paths)](./system-prompts/tool-description-bash-quote-file-paths.md) (**35** tks) - Bash tool instruction: quote file paths containing spaces.
- [Tool Description: Bash (sandbox — adjust settings)](./system-prompts/tool-description-bash-sandbox-adjust-settings.md) (**26** tks) - Work with user to adjust sandbox settings on failure.
- [Tool Description: Bash (sandbox — default to sandbox)](./system-prompts/tool-description-bash-sandbox-default-to-sandbox.md) (**38** tks) - Default to sandbox; only bypass when user asks or evidence of sandbox restriction.
- [Tool Description: Bash (sandbox — evidence list header)](./system-prompts/tool-description-bash-sandbox-evidence-list-header.md) (**15** tks) - Header for list of sandbox-caused failure evidence.
- [Tool Description: Bash (sandbox — evidence: access denied)](./system-prompts/tool-description-bash-sandbox-evidence-access-denied.md) (**15** tks) - Sandbox evidence: access denied to paths outside allowed directories.
- [Tool Description: Bash (sandbox — evidence: network failures)](./system-prompts/tool-description-bash-sandbox-evidence-network-failures.md) (**17** tks) - Sandbox evidence: network connection failures to non-whitelisted hosts.
- [Tool Description: Bash (sandbox — evidence: operation not permitted)](./system-prompts/tool-description-bash-sandbox-evidence-operation-not-permitted.md) (**18** tks) - Sandbox evidence: operation not permitted errors.
- [Tool Description: Bash (sandbox — evidence: unix socket errors)](./system-prompts/tool-description-bash-sandbox-evidence-unix-socket-errors.md) (**11** tks) - Sandbox evidence: unix socket connection errors.
- [Tool Description: Bash (sandbox — explain restriction)](./system-prompts/tool-description-bash-sandbox-explain-restriction.md) (**36** tks) - Explain which sandbox restriction caused the failure.
- [Tool Description: Bash (sandbox — failure evidence condition)](./system-prompts/tool-description-bash-sandbox-failure-evidence-condition.md) (**48** tks) - Condition: command failed with evidence of sandbox restrictions.
- [Tool Description: Bash (sandbox — mandatory mode)](./system-prompts/tool-description-bash-sandbox-mandatory-mode.md) (**34** tks) - Policy: all commands must run in sandbox mode.
- [Tool Description: Bash (sandbox — no exceptions)](./system-prompts/tool-description-bash-sandbox-no-exceptions.md) (**17** tks) - Commands cannot run outside sandbox under any circumstances.
- [Tool Description: Bash (sandbox — no sensitive paths)](./system-prompts/tool-description-bash-sandbox-no-sensitive-paths.md) (**36** tks) - Do not suggest adding sensitive paths to sandbox allowlist.
- [Tool Description: Bash (sandbox — per-command)](./system-prompts/tool-description-bash-sandbox-per-command.md) (**52** tks) - Treat each command individually; default to sandbox for future commands.
- [Tool Description: Bash (sandbox — response header)](./system-prompts/tool-description-bash-sandbox-response-header.md) (**17** tks) - Header for how to respond when seeing sandbox-caused failures.
- [Tool Description: Bash (sandbox — retry without sandbox)](./system-prompts/tool-description-bash-sandbox-retry-without-sandbox.md) (**33** tks) - Immediately retry with dangerouslyDisableSandbox on sandbox failure.
- [Tool Description: Bash (sandbox — tmpdir)](./system-prompts/tool-description-bash-sandbox-tmpdir.md) (**58** tks) - Use $TMPDIR for temporary files in sandbox mode.
- [Tool Description: Bash (sandbox — user permission prompt)](./system-prompts/tool-description-bash-sandbox-user-permission-prompt.md) (**14** tks) - Note that disabling sandbox will prompt user for permission.
- [Tool Description: Bash (semicolon usage)](./system-prompts/tool-description-bash-semicolon-usage.md) (**29** tks) - Bash tool instruction: use semicolons when sequential order matters but failure does not.
- [Tool Description: Bash (sequential commands)](./system-prompts/tool-description-bash-sequential-commands.md) (**42** tks) - Bash tool instruction: chain dependent commands with &&.
- [Tool Description: Bash (sleep — keep short)](./system-prompts/tool-description-bash-sleep-keep-short.md) (**22** tks) - Bash tool instruction: keep sleep duration to 1-5 seconds.
- [Tool Description: Bash (sleep — no polling background tasks)](./system-prompts/tool-description-bash-sleep-no-polling-background-tasks.md) (**37** tks) - Bash tool instruction: do not poll background tasks, wait for notification.
- [Tool Description: Bash (sleep — run immediately)](./system-prompts/tool-description-bash-sleep-run-immediately.md) (**21** tks) - Bash tool instruction: do not sleep between commands that can run immediately.
- [Tool Description: Bash (sleep — use check commands)](./system-prompts/tool-description-bash-sleep-use-check-commands.md) (**34** tks) - Bash tool instruction: use check commands rather than sleeping when polling.
- [Tool Description: Bash (timeout)](./system-prompts/tool-description-bash-timeout.md) (**83** tks) - Bash tool instruction: optional timeout configuration.
- [Tool Description: Bash (verify parent directory)](./system-prompts/tool-description-bash-verify-parent-directory.md) (**38** tks) - Bash tool instruction: verify parent directory before creating files.
- [Tool Description: Bash (working directory)](./system-prompts/tool-description-bash-working-directory.md) (**37** tks) - Bash tool note about working directory persistence and shell state.
- [Tool Description: SendMessageTool (non-agent-teams)](./system-prompts/tool-description-sendmessagetool-non-agent-teams.md) (**226** tks) - Send a message the user will read, describes this tool well.
- [Tool Description: Snooze (delay and reason guidance)](./system-prompts/tool-description-snooze-delay-and-reason-guidance.md) (**608** tks) - Extends the snooze tool description with guidance on choosing delaySeconds relative to the 5-minute prompt cache TTL and writing informative reason fields.
- [Tool Description: TaskList (teammate workflow)](./system-prompts/tool-description-tasklist-teammate-workflow.md) (**133** tks) - Conditional section appended to TaskList tool description.
- [Tool Description: ToolSearch (second part)](./system-prompts/tool-description-toolsearch-second-part.md) (**202** tks) - The bulk of the tool description.
- [Tool Description: Write (read existing file first)](./system-prompts/tool-description-write-read-existing-file-first.md) (**70** tks) - Tool description for Write in environments where existing files must be read before overwrite.
- [Tool Description: request_teach_access (part of teach mode)](./system-prompts/tool-description-request_teach_access-part-of-teach-mode.md) (**139** tks) - Describes a tool that requests permission to guide the user through a task step-by-step using fullscreen tooltip overlays instead of direct access.
- [Tool Parameter: Computer action](./system-prompts/tool-parameter-computer-action.md) (**251** tks) - Action parameter options for the Chrome browser computer tool.

### Skills

Built-in skill prompts for specialized tasks.

- [Skill: /catch-up periodic heartbeat](./system-prompts/skill-catch-up-periodic-heartbeat.md) (**1591** tks) - Skill definition for the /catch-up periodic heartbeat that scans current priorities, triages actionable changes, reports a short digest, and updates catch-up state.
- [Skill: /dream memory consolidation](./system-prompts/skill-dream-memory-consolidation.md) (**512** tks) - Skill definition for the /dream nightly housekeeping job that consolidates recent logs and transcripts into persistent memory topics, learnings, and a pruned MEMORY.md index.
- [Skill: /dream nightly schedule](./system-prompts/skill-dream-nightly-schedule.md) (**441** tks) - Sets up a recurring nightly memory consolidation job by deduplicating existing schedules, creating a new cron task, confirming details to the user, and running an immediate consolidation.
- [Skill: /init CLAUDE.md and skill setup (new version)](./system-prompts/skill-init-claudemd-and-skill-setup-new-version.md) (**5384** tks) - A comprehensive onboarding flow for setting up CLAUDE.md and related skills/hooks in the current repository, including codebase exploration, user interviews, and iterative proposal refinement.
- [Skill: /insights report output](./system-prompts/skill-insights-report-output.md) (**191** tks) - Formats and displays the insights usage report results after the user runs the /insights slash command.
- [Skill: /loop cloud-first scheduling offer](./system-prompts/skill-loop-cloud-first-scheduling-offer.md) (**510** tks) - Decision tree for offering cloud-based scheduling before falling back to local session loops in the /loop command.
- [Skill: /loop self-pacing mode](./system-prompts/skill-loop-self-pacing-mode.md) (**638** tks) - Instructs Claude how to self-pace a recurring loop by arming event monitors as primary wake signals and scheduling fallback heartbeat delays between iterations.
- [Skill: /loop slash command (dynamic mode)](./system-prompts/skill-loop-slash-command-dynamic-mode.md) (**514** tks) - Parses user input into an interval and prompt for scheduling recurring or dynamically self-paced loop executions.
- [Skill: /loop slash command](./system-prompts/skill-loop-slash-command.md) (**969** tks) - Parses user input into an interval and prompt, converts the interval to a cron expression, and schedules a recurring task.
- [Skill: /morning-checkin daily brief](./system-prompts/skill-morning-checkin-daily-brief.md) (**1576** tks) - Skill definition for the /morning-checkin scheduled task that prepares a daily calendar and inbox digest, schedules pre-meeting check-ins, and records the day’s top priority.
- [Skill: /pre-meeting-checkin event brief](./system-prompts/skill-pre-meeting-checkin-event-brief.md) (**491** tks) - Skill definition for the /pre-meeting-checkin task that gathers event materials, recent thread context, open questions, and a concise meeting brief.
- [Skill: /stuck slash command](./system-prompts/skill-stuck-slash-command.md) (**964** tks) - Diagnozse frozen or slow Claude Code sessions.
- [Skill: Agent Design Patterns](./system-prompts/skill-agent-design-patterns.md) (**1974** tks) - Reference guide covering decision heuristics for building agents on the Claude API, including tool surface design, context management, caching strategies, and composing tool calls.
- [Skill: Build with Claude API (reference guide)](./system-prompts/skill-build-with-claude-api-reference-guide.md) (**655** tks) - Template for presenting language-specific reference documentation with quick task navigation.
- [Skill: Building LLM-powered applications with Claude](./system-prompts/skill-building-llm-powered-applications-with-claude.md) (**8769** tks) - Guides Claude in building LLM-powered applications using the Anthropic SDK, covering language detection, API surface selection (Claude API vs Managed Agents), model defaults, thinking/effort configuration, and language-specific documentation reading.
- [Skill: Computer Use MCP](./system-prompts/skill-computer-use-mcp.md) (**1206** tks) - Instructions for using computer-use MCP tools including tool selection tiers, app access tiers, link safety, and financial action restrictions.
- [Skill: Create verifier skills](./system-prompts/skill-create-verifier-skills.md) (**2551** tks) - Prompt for creating verifier skills for the Verify agent to automatically verify code changes.
- [Skill: Debugging](./system-prompts/skill-debugging.md) (**417** tks) - Instructions for debugging an issue that the user is encountering in the Claude Code session.
- [Skill: Dynamic pacing loop execution](./system-prompts/skill-dynamic-pacing-loop-execution.md) (**558** tks) - Step-by-step instructions for executing a dynamic pacing loop that runs tasks, arms persistent monitors for event-gated waits, schedules fallback heartbeat ticks, and handles task notifications.
- [Skill: Generate permission allowlist from transcripts](./system-prompts/skill-generate-permission-allowlist-from-transcripts.md) (**2338** tks) - Analyzes session transcripts to extract frequently used read-only tool-call patterns and adds them to the project's .claude/settings.json permission allowlist to reduce permission prompts.
- [Skill: Model migration guide](./system-prompts/skill-model-migration-guide.md) (**18104** tks) - Step-by-step instructions for migrating existing code to newer Claude models, covering breaking changes, deprecated parameters, per-SDK syntax, prompt-behavior shifts, and migration checklists.
- [Skill: Schedule recurring cron and execute immediately (compact)](./system-prompts/skill-schedule-recurring-cron-and-execute-immediately-compact.md) (**173** tks) - Instructions for creating a recurring cron job, confirming the schedule with the user, and immediately executing the parsed prompt without waiting for the first cron fire.
- [Skill: Schedule recurring cron and run immediately](./system-prompts/skill-schedule-recurring-cron-and-run-immediately.md) (**271** tks) - Converts an interval to a cron expression, schedules a recurring task via the cron creation tool, confirms to the user, and immediately executes the task without waiting for the first cron fire.
- [Skill: Simplify](./system-prompts/skill-simplify.md) (**937** tks) - Instructions for simplifying code.
- [Skill: Team onboarding guide](./system-prompts/skill-team-onboarding-guide.md) (**521** tks) - Template for onboarding a new teammate to a team's Claude Code setup, walking them through usage stats, setup checklists, MCP servers, skills, and team tips in a warm conversational style.
- [Skill: Update Claude Code Config](./system-prompts/skill-update-claude-code-config.md) (**1195** tks) - Skill for modifying Claude Code configuration file (settings.json).
- [Skill: Verify CLI changes (example for Verify skill)](./system-prompts/skill-verify-cli-changes-example-for-verify-skill.md) (**565** tks) - Example workflow for verifying a CLI change, as part of the Verify skill.
- [Skill: Verify server/API changes (example for Verify skill)](./system-prompts/skill-verify-serverapi-changes-example-for-verify-skill.md) (**612** tks) - Example workflow for verifying a server/API change, as part of the Verify skill.
- [Skill: Verify skill](./system-prompts/skill-verify-skill.md) (**2694** tks) - Skill for opinionated verification workflow for validating code changes.
- [Skill: update-config (7-step verification flow)](./system-prompts/skill-update-config-7-step-verification-flow.md) (**1160** tks) - A skill that guides Claude through a 7-step process to construct and verify hooks for Claude Code, ensuring they work correctly in the user's specific project environment.
