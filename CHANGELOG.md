<!--
Note: Only use **NEW:** for entirely new prompt files, NOT for new additions/sections within existing prompts.
-->

### Claude Code System Prompts Changelog

# [2.1.83](https://github.com/Piebald-AI/claude-code-system-prompts/commit/a9eee87)

_+5,960 tokens_

- **NEW:** Data: Prompt Caching — Design & Optimization — New document covering how to design prompt-building code for effective caching, including placement patterns and anti-patterns.
- **NEW:** System Prompt: Advisor tool instructions — Instructions for using the Advisor tool.
- **NEW:** System Reminder: Ultraplan mode — System reminder for using Ultraplan mode to create a detailed implementation plan with multi-agent exploration and critique.
- **NEW:** Skill: Verify CLI changes (example for Verify skill) — Example workflow for verifying a CLI change, as part of the Verify skill.
- **NEW:** Skill: Verify server/API changes (example for Verify skill) — Example workflow for verifying a server/API change, as part of the Verify skill.
- **NEW:** Skill: Verify skill — Opinionated verification workflow for validating code changes, replacing the previous verification specialist skill.
- **REMOVED:** Skill: Verification specialist — Removed in favor of the new Verify skill and its example workflows.
- **REMOVED:** System Reminder: Task status — Removed TaskOutput tool reference reminder.
- Agent Prompt: Dream memory consolidation — Added a ~25KB size cap to the index file; tightened index entry format to one line under ~150 characters; changed verbose-entry demotion guidance to trigger on lines over ~200 chars.
- Data: Agent SDK reference — Python — Added documentation for per-turn `usage` data on `AssistantMessage` for tracking costs.
- Data: Agent SDK reference — TypeScript — Added comment noting optional `skills` and `mcpServers` for subagent customization in team definitions.
- Data: Claude API reference — C# — Updated source-verified SDK version from 12.8.0 to 12.9.0; added prompt caching cross-reference to the shared design document; added cache-hit verification via usage fields.
- Data: Claude API reference — cURL — Added Prompt Caching section with example, TTL options, top-level auto-placement, and cache-hit verification guidance.
- Data: Claude API reference — Go — Added Prompt Caching section with system block caching example, TTL options, top-level auto-placement, and cache-hit verification.
- Data: Claude API reference — Java — Bumped SDK version from 2.16.1 to 2.17.0; added prompt caching cross-reference to the shared design document; added cache-hit verification via usage fields.
- Data: Claude API reference — PHP — Added beta tool runner documentation with `BetaRunnableTool` and `toolRunner()` examples; added structured outputs section with `StructuredOutputModel` and raw schema approaches; added Prompt Caching section; bumped recommended SDK version from ^0.6 to ^0.7; updated intro note to reflect new beta tool runner and structured output support.
- Data: Claude API reference — Python — Expanded prompt caching intro with prefix-match explanation, architectural guidance, and silent-invalidator audit reference; added "Verifying Cache Hits" subsection with usage field examples and debugging tips.
- Data: Claude API reference — Ruby — Added Prompt Caching section with system block caching example, TTL options, top-level auto-placement, and cache-hit verification.
- Data: Claude API reference — TypeScript — Added prefix-match explanation and cross-reference to the shared caching design document; added "Verifying Cache Hits" subsection with usage field examples and silent-invalidator debugging tips.
- Data: Tool use concepts — Updated tool runner language list to include PHP; noted PHP's `BetaRunnableTool` wraps a run closure around a hand-written schema.
- Skill: Build with Claude API — Added PHP beta tool runner to the SDK feature table; added "Prompt Caching (Quick Reference)" section with prefix-match explanation, top-level auto-caching guidance, and silent-invalidator troubleshooting; added prompt caching routing entries to the reading guide.
- Skill: Build with Claude API (reference guide) — Added prompt caching routing entry for quick task navigation.
- Tool Description: CronCreate — Added durable mode documentation: jobs can now optionally persist to disk and survive session restarts, with guidance on when to use durable vs. session-only; expanded runtime behavior section for durable job catch-up semantics.
- Tool Description: SendMessageTool — Significantly condensed from a detailed protocol reference to a compact quick-reference format; inlined addressing table, simplified protocol response examples, and removed verbose per-message-type sections.

# [2.1.81](https://github.com/Piebald-AI/claude-code-system-prompts/commit/a82ade6)

_+294 tokens_

- **NEW:** Agent Prompt: /review slash command (remote) — Remote version of the /review slash command.
- **NEW:** Agent Prompt: Auto mode rule reviewer — Reviews and critiques user-defined auto mode classifier rules for clarity, completeness, conflicts, and actionability.
- **NEW:** System Prompt: Minimal mode — Describes the behavior and constraints of minimal mode, which skips hooks, LSP, plugins, auto-memory, and other features while requiring explicit context via CLI flags.
- Agent Prompt: /batch slash command — Changed terminology from "Explore agents" to "subagents" in the scope-understanding step.
- Agent Prompt: /schedule slash command — Replaced raw curl-based API calls with a dedicated tool for managing remote triggers; simplified the create body shape documentation; removed direct references to auth environment variables.
- Agent Prompt: Security monitor for autonomous agent actions (first part) — Clarified transcript evaluation target from "final tool_use block" to "agent's most recent action"; strengthened the "Evaluate on Own Merits" rule with an explicit "silence is not consent" principle — the user not intervening between consecutive actions is not evidence of approval.
- Agent Prompt: Security monitor for autonomous agent actions (second part) — Expanded sensitive data definition to default-classify internal files (repo scripts, diagrams, slides) as sensitive when uploading to public storage such as gists, pastebins, or diagram renderers.
- Skill: /init CLAUDE.md and skill setup (new version) — Changed terminology from "Explore subagent" to generic "subagent" in the codebase exploration phase.
- Skill: Simplify — Added "unnecessary comments" check to the hacky-patterns review: delete comments that explain what code does, narrate the change, or reference the task/caller; keep only non-obvious "why" comments.
- System Prompt: Fork usage guidelines — Changed terminology from referencing a specific subagent type to "a fresh subagent" when explaining cache-sharing advantages of forks.
- System Prompt: Tool usage (task management) — Simplified tool name reference.
- System Reminder: Plan mode is active (iterative) — Minor rewording of the explore step's subagent guidance.

# [2.1.80](https://github.com/Piebald-AI/claude-code-system-prompts/commit/abbb61f)

_+3,065 tokens_

- **NEW:** Agent Prompt: /schedule slash command — Guides the user through scheduling, updating, listing, or running remote Claude Code agents on cron triggers via the Anthropic cloud API.
- Agent Prompt: Status line setup — Added `rate_limits` object to the status line JSON schema, exposing Claude.ai subscription usage limits with 5-hour session and 7-day weekly windows (each with used percentage and reset timestamp); added example shell commands for displaying rate limit usage in the status line.
- Data: HTTP error codes reference — Minor update to HTTP error codes documentation.


# [2.1.79](https://github.com/Piebald-AI/claude-code-system-prompts/commit/7f0098b)

_+714 tokens_

- **REMOVED:** System Prompt: Tool Use Summary Generation — Removed prompt for generating brief past-tense summaries of tool usage.
- Data: Claude model catalog — Added Programmatic Model Discovery section with Python SDK and raw HTTP examples for querying the Models API to retrieve live capability data (context window, max output tokens, vision, thinking, effort, structured outputs); includes guidance on iterating and filtering models by capability.
- Skill: Build with Claude API — Added Models API endpoints (`GET /v1/models`, `GET /v1/models/{id}`) to the list of supporting endpoints; added live capability lookup note directing users to query the Models API instead of relying on cached model tables.
- Skill: /loop slash command — Changed recurring task auto-expiry from a hardcoded 3-day limit to a configurable timeframe.
- Tool Description: CronCreate — Changed recurring task auto-expiry from a hardcoded 3-day limit to a configurable timeframe.
- System Prompt: Team memory content display — Updated memory content rendering to use a separate content reference.
- System Reminder: Memory file contents — Updated memory content rendering to use a separate content reference.


# [2.1.78](https://github.com/Piebald-AI/claude-code-system-prompts/commit/9f2320d)

_+1,956 tokens_

- **NEW:** Agent Prompt: Dream memory consolidation — Instructs an agent to perform a multi-phase memory consolidation pass — orienting on existing memories, gathering recent signal from logs and transcripts, merging updates into topic files, and pruning the index.
- **REMOVED:** System Prompt: Memory system (private feedback) — Removed description of the private feedback memory type for storing user guidance and corrections.
- **REMOVED:** System Prompt: Tone and style (concise output — detailed) — Removed instruction for concise, polished output without filler or inner monologue.
- **NEW:** System Prompt: Memory description of user feedback — Describes the user feedback memory type that stores guidance about work approaches, emphasizing recording both successes and failures and checking for contradictions with team memories.
- Data: Agent SDK patterns — Python — Added Session Mutations section with `rename_session`, `tag_session` examples including tag clearing and project-directory scoping.
- Data: Agent SDK patterns — TypeScript — Added `getSessionInfo` to Session History; added `tag` field to session listing output; added Session Mutations section with `renameSession`, `tagSession`, and `forkSession` examples; noted pagination support via `limit`/`offset` on `listSessions`.
- Data: Agent SDK reference — Python — Added `RateLimitEvent` documentation with example showing how to handle rate-limit status transitions; added Session Mutations section with `rename_session` and `tag_session` (sync functions, optional directory scoping).
- Data: Agent SDK reference — TypeScript — Added `agentProgressSummaries` option to the options table for enabling periodic AI-generated progress summaries on `task_progress` events; updated `task_progress` description to mention the `summary` field; added `getSessionInfo` for single-session metadata retrieval; added `tag` field to session listing; noted pagination support on `listSessions`; added Session Mutations section with `renameSession`, `tagSession`, and `forkSession`.
- Data: Claude API reference — Java — Bumped SDK version from 2.16.0 to 2.16.1.
Data: Claude API references (all languages) and tool use / streaming / batches / files references — Updated `max_tokens` values across code examples, increasing to `16000` for non-streaming and `64000` for streaming to avoid mid-thought truncation.
- Skill: Build with Claude API — Added `max_tokens` defaults guidance: use ~16000 for non-streaming and ~64000 for streaming; clarified that lowballing `max_tokens` truncates output and requires retries; noted exceptions for classification (~256), cost caps, or deliberately short outputs.
- System Prompt: Auto mode — Added rule 6: never post to public services (GitHub gists, Mermaid Live, Pastebin, etc.) without explicit written user approval, requiring the user to review content for sensitivity first.
- System Prompt: Executing actions with care — Added guidance that uploading content to third-party web tools (diagram renderers, pastebins, gists) publishes it and may be cached or indexed, so sensitivity should be considered before sending.


# [2.1.77](https://github.com/Piebald-AI/claude-code-system-prompts/commit/87fae2a)

_+6,494 tokens_

- **NEW:** Skill: /init CLAUDE.md and skill setup (new version) — A comprehensive onboarding flow for setting up CLAUDE.md and related skills/hooks in the current repository, including codebase exploration, user interviews, and iterative proposal refinement.
- **NEW:** Skill: update-config (7-step verification flow) — A skill that guides Claude through a 7-step process to construct and verify hooks for Claude Code, ensuring they work correctly in the user's specific project environment.
- Data: Claude API reference — Java — Bumped SDK version from 2.15.0 to 2.16.0; added Memory Tool section with `BetaMemoryToolHandler` example showing how to implement a file-system-backed memory backend with `BetaToolRunner`.
- Data: Tool use concepts — Added Java to the list of SDKs that provide helper classes/functions for implementing the memory tool backend.
- Skill: /loop slash command — Reformatted action steps as a numbered list; added step 3 instructing Claude to immediately execute the parsed prompt instead of waiting for the first cron fire (invoking slash commands via the Skill tool or acting directly).
- Skill: /stuck slash command — Changed Slack reporting to only post when a stuck session is actually found (no more all-clear messages); introduced a two-message structure with a short top-level message and a threaded detail reply for channel scannability; added relevant debug log tail or `sample` output to the thread reply.
- Skill: Update Claude Code Config — Added reference to the new constructing-hook prompt; updated the prettier hook example command from `xargs prettier --write` to a safer `read -r f; prettier --write "$f"` pattern.
- System Prompt: Hooks Configuration — Updated the prettier PostToolUse hook example command from `xargs prettier --write` to `read -r f; prettier --write "$f"` for safer filename handling.
- Tool Description: Agent (usage notes) — Replaced agent resume-by-ID mechanism with instructions to use SendMessage with the agent's ID or name as the `to` field to continue a previously spawned agent; removed the separate bullet about agent ID return values; consolidated fresh-invocation guidance into a single bullet.

# [2.1.76](https://github.com/Piebald-AI/claude-code-system-prompts/commit/6cc7a81)

_+43 tokens_

- Agent Prompt: Security monitor for autonomous agent actions (second part) — Clarified "base64-encoded" to "encoded (e.g. base64)" for sensitive data detection; broadened code-from-external deserialization examples to "formats that can execute code (eval, exec, yaml.unsafe_load, pickle, etc)"; refined "Modify Shared Resources" examples by removing "model registrations"; improved "Irreversible Local Destruction" formatting and clarified package-manager-controlled directory guidance (explaining files get regenerated on install and suggesting copying into source tree); changed "GitHub issues/PRs" capitalization to "GitHub Issues/PRs" in External System Writes; updated Data Exfiltration to replace "creating gists" with "public plaintext sharing applications (e.g. public GitHub gists)"; quoted rule names in cross-references (e.g. "Local Operations" ALLOW exception, "Irreversible Local Destruction" in BLOCK).
- Skill: Update Claude Code Config — Added `PostCompact` to the list of available hook events.
- System Prompt: Hooks Configuration — Added `PostCompact` hook event (fires after compaction, receives summary) to the hooks event table.
- Tool Description: ReadFile — Condensed and reordered usage notes; added a note about reading full files.


# [2.1.75](https://github.com/Piebald-AI/claude-code-system-prompts/commit/97ce0c2)

_+156 tokens_

- **NEW:** Agent Prompt: Determine which memory files to attach — Agent for determining which memory files to attach for the main agent.
- **NEW:** System Prompt: One of six rules for using sleep command — One of the six rules for using the sleep command.
- **NEW:** System Prompt: System section — System section of the main system prompt.
- **REMOVED:** Agent Prompt: Memory selection — Removed instructions for selecting relevant memories for a user query (replaced by "Determine which memory files to attach").
- **REMOVED:** Tool Description: Bash (sleep — no retry loops) — Removed instruction to diagnose failures instead of retrying in sleep loops.
- **REMOVED:** Tool Description: Bash (sleep — use run_in_background) — Removed instruction to use run_in_background for long-running commands.
- Agent Prompt: Security monitor for autonomous agent actions (first part) — Added "Unseen Tool Results" evaluation rule: when an action's parameters depend on a tool result not visible in the transcript, treat those parameters as unverifiable and block if the action is high-severity.
- System Prompt: Teammate Communication — Updated SendMessage usage instructions from `type: "message"` / `type: "broadcast"` to `to: "<name>"` / `to: "*"` addressing pattern.
- System Reminder: Team Coordination — Updated SendMessage example from `operation`/`target_agent_id`/`value` fields to `to`/`message`/`summary` fields.
- Tool Description: ReadFile — Simplified usage notes around line length truncation and conditional read lines.
- Tool Description: SendMessageTool — Restructured around a unified three-field schema (`to`, `message`, `summary`) replacing the previous `type`/`recipient`/`content` pattern; protocol messages (shutdown, plan approval) are now nested inside the `message` field as structured objects; added addressing table; clarified that structured protocol messages cannot be broadcast.
- Tool Description: TeammateTool — Updated SendMessage references from `type: "shutdown_request"` to `message: {type: "shutdown_request"}`; changed field name from `target_agent_id` to `to` for sending messages.


# [2.1.74](https://github.com/Piebald-AI/claude-code-system-prompts/commit/93acf03)

_+1,750 tokens_

- **NEW:** Agent Prompt: Coding session title generator — Generates a title for the coding session.
- **NEW:** Skill: /stuck — Diagnose frozen or slow Claude Code sessions.
- Agent Prompt: Memory selection — Added rule to skip API/usage reference memories for tools already in active use, while still selecting warnings, gotchas, and known-issue memories for those tools.
- Agent Prompt: Security monitor for autonomous agent actions (first part) — Added block rule for agents posting or commenting to shared/external systems when the user only asked a question or requested analysis; added "posting or writing to shared/external systems" to the list of high-severity actions requiring precise user intent; refined messaging context rule to evaluate content sensitivity, accuracy, and audience scope rather than blanket-allowing internal messaging; simplified evaluation procedure wording; added scope-creep example for read-vs-publish distinction.
- Agent Prompt: Security monitor for autonomous agent actions (second part) — Added "Remote Shell Writes" block rule for writes to production/shared hosts via `kubectl exec`, `docker exec`, or `ssh`; renamed "Preview/Apply Collapse" to "Blind Apply" with clearer description of bypassed confirmation flags; added "External System Writes" block rule covering deletions, modifications, and publishing in external collaboration tools the agent didn't create; added "Content Integrity / Impersonation" block rule for false, fabricated, or misattributed content; added "Real-World Transactions" block rule for purchases, payments, and communications to people outside the user's organization; expanded "Irreversible Local Destruction" to cover untested glob/regex patterns and edits to package-manager-installed files; clarified "Local Operations" allow exception to scope "project scope" as the starting repository only; expanded "Production Deploy" definition to include production services.
- System Reminder: /btw side question — Rewrote constraint framing from 'CRITICAL CONSTRAINTS' with 'no tools available' messaging to 'IMPORTANT CONTEXT' explaining the responder is a separate lightweight agent; clarified that the main agent continues working independently and that the responder should not reference being interrupted.


# [2.1.73](https://github.com/Piebald-AI/claude-code-system-prompts/commit/c02a840)

_+13,443 tokens_

- **NEW:** Data: Claude API reference — cURL — Raw API reference for Claude API for use with cURL or raw HTTP.
- **NEW:** System Prompt: How to use the SendUserMessage tool — Instructions for using the SendUserMessage tool.
- **NEW:** System Prompt: Phase four of plan mode — Phase four of plan mode, extracted as a standalone prompt.
- **NEW:** Tool Description: SendMessageTool (non-agent-teams) — Description of the SendMessageTool for non-agent-teams contexts.
- **REMOVED:** System Prompt: Brief mode — Removed Codex-like execution mode with short status updates before launching into work.
- **REMOVED:** System Prompt: Post checkpoints — Removed instructions for how to post checkpoints during task execution.
- Data: Agent SDK patterns — Python — Clarified that custom SDK MCP tools require `ClaudeSDKClient` (not `query()`); removed `allow_dangerously_skip_permissions` from bypass permissions example; fixed session ID extraction to use `message.data.get("session_id")`; changed `list_sessions` and `get_session_messages` from async to sync functions.
- Data: Agent SDK reference — Python — Removed `"dontAsk"` permission mode; removed `allow_dangerously_skip_permissions` option and requirement for bypass permissions; reduced available hook events list to a smaller set; fixed session ID extraction to use `message.data.get("session_id")`; renamed task message subclasses to `TaskStartedMessage`, `TaskProgressMessage`, `TaskNotificationMessage`; changed `list_sessions` and `get_session_messages` from async to sync functions; changed MCP server management methods from add/remove to reconnect/toggle/status pattern.
- Data: Agent SDK reference — TypeScript — Clarified `"dontAsk"` permission mode as denying anything not pre-approved rather than auto-approving; expanded available hook events list with `Elicitation`, `ElicitationResult`, `WorktreeCreate`, `WorktreeRemove`, `InstructionsLoaded`; changed `tools` option to accept a preset object in addition to string arrays; changed `systemPrompt` option to accept a preset object with optional append; corrected stop reason example values; clarified `toggleMcpServer` requires both name and enabled parameters; clarified `mcpServerStatus` returns an array of all configured servers.
- Data: Claude API reference — C# — Substantially expanded: added content block iteration with `TryPick*` pattern for type-safe narrowing; added adaptive thinking section; added full tool definition and manual tool loop with round-trip conversion guidance; added context editing/compaction beta section with `BetaContentBlock` handling; added effort parameter, prompt caching, token counting, structured output, PDF/document input, server-side tools, and Files API beta sections.
- Data: Claude API reference — Go — Added stream message accumulation pattern; added `BetaTextBlock` type narrowing for `RunToCompletion` results; replaced fixed-budget extended thinking with adaptive thinking as recommended mode; added server-side tools, PDF/document input, Files API beta, and context editing/compaction beta sections.
- Data: Claude API reference — Java — Substantially expanded: added adaptive thinking section with `ThinkingConfigAdaptive`; added non-beta tool declaration with manual JSON schema; added `MessageParam` content block building for tool result round-trips; added effort parameter, prompt caching, token counting, structured output with typed parsing, PDF/document input, server-side tools with beta namespace guidance, server tool response reading, and Files API beta sections.
- Data: Claude API reference — PHP — Substantially expanded: updated Bedrock, Vertex AI, and Foundry client initialization to use new namespaced static factories; added content block type checking for safe text extraction; added SDK version requirement note for streaming; added typed streaming event handling; added full manual tool use loop with camelCase key guidance; added adaptive thinking section; added beta features section with MCP server and server-side tools guidance.
- Data: Claude API reference — Python — Updated compaction availability from "Opus 4.6 only" to "Opus 4.6 and Sonnet 4.6."
- Data: Claude API reference — TypeScript — Corrected multi-turn rule from "messages must alternate" to "consecutive same-role messages are allowed"; updated compaction availability from "Opus 4.6 only" to "Opus 4.6 and Sonnet 4.6"; added type guard narrowing for `BetaTextBlock` in compaction example.
- Data: Claude model catalog — Added retirement date (Apr 19, 2026) for Claude Haiku 3.
- Data: Files API reference — Python — Updated code examples to iterate content blocks by type instead of indexing `content[0].text`.
- Data: HTTP error codes reference — Added `request_id` field to error response example.
- Data: Message Batches API reference — Python — Updated code examples to find text blocks by type instead of indexing `content[0].text`.
- Data: Tool use reference — Python — Fixed `tool_runner` call from async to sync; updated structured output example to find text blocks by type instead of indexing `content[0].text`.
- Data: Tool use reference — TypeScript — Added server-side tools section with interface/name/type mapping table and beta mixing warning; fixed `pause_turn` handling to append assistant turn instead of resetting messages; added ESM `__dirname` workaround note; fixed variable shadowing in file download example; added nullability annotations for `container.id` and `parsed_output`; added "Reading Local Files" ESM section.
- Skill: Build with Claude API — Updated compaction availability from "Opus 4.6 only" to "Opus 4.6 and Sonnet 4.6."
- System Reminder: Plan mode is active (5-phase) — Extracted Phase 4 (Final Plan) instructions into a separate reusable prompt reference.

# [2.1.72](https://github.com/Piebald-AI/claude-code-system-prompts/commit/7a45418)

_+1,643 tokens_

- **NEW:** System Prompt: Auto mode — Continuous task execution mode, akin to a background agent.
- **NEW:** System Prompt: Brief mode — Codex-like execution mode with short status updates before launching into work.
- **NEW:** System Prompt: Post checkpoints — Instructions for how to post checkpoints during task execution.
- **NEW:** Tool Description: ExitWorktree — Tool for leaving a git worktree mid-session, with option to keep or remove it.
- **NEW:** Tool Description: ToolSearch (second part) — Second part of the ToolSearch tool description with query modes and usage examples.
- **REMOVED:** System Prompt: Tool permission mode — Removed guidance on tool permission modes and handling denied tool calls.
- **REMOVED:** System Prompt: Using your tools (how to use searching tools) — Removed standalone searching tools guidance (consolidated into existing direct search and delegate exploration prompts).
- **REMOVED:** System Prompt: Using your tools (whether to use Explore subagent) — Removed standalone Explore subagent guidance (consolidated into existing delegate exploration prompt).
- **REMOVED:** Tool Description: ToolSearch extended — Removed extended ToolSearch usage instructions (replaced by ToolSearch second part).
- Agent Prompt: Claude guide agent — Removed inline agent metadata block (agent type, model, permission mode, tool list, and when-to-use guidance).
- Agent Prompt: Explore strengths and guidelines — Added agent metadata block with agent type, model, disallowed tools, when-to-use guidance, and critical read-only system reminder (moved from Explore prompt).
- Agent Prompt: Explore — Removed inline agent metadata block (moved to Explore strengths and guidelines).
- Agent Prompt: Verification specialist — Significantly expanded with two documented failure patterns (verification avoidance and "first 80%" bias); added structured per-check output format requiring command run, output observed, and result; added self-rationalization recognition section with common excuses to override; added guidance to match rigor to stakes; added pre-FAIL checklist to avoid flagging intentional behavior or already-handled cases; defined PARTIAL as environmental limitations only; updated mobile verification strategy to use accessibility/UI tree dumps instead of screenshots; clarified that test suite results are context, not evidence.
- Skill: Simplify — Added "Recurring no-op updates" as a new efficiency check for state/store updates in polling loops or event handlers that fire unconditionally without change detection.
- System Prompt: Fork usage guidelines — Refined forking criteria from a list of use cases to a qualitative "will I need this output again" heuristic; added guidance that forks beat Explore subagent for research because they inherit context and share cache; added warning not to set a different model on forks to preserve cache reuse.
- System Prompt: Tool usage (delegate exploration) — Generalized individual tool name references to a unified search tools reference.
- System Prompt: Tool usage (direct search) — Generalized individual tool name references to a unified search tools reference.
- Tool Description: Agent (usage notes) — Internal variable renames only; no user-facing changes.
- Tool Description: EnterWorktree — Added mention of ExitWorktree for leaving the worktree mid-session; clarified that the keep/remove prompt on session exit only applies if still in the worktree.
- Tool Description: WebSearch — Internal variable rename only; no user-facing changes.

# [2.1.71](https://github.com/Piebald-AI/claude-code-system-prompts/commit/10a9b4f)

_+10,211 tokens_

- **NEW:** Agent Prompt: Security monitor for autonomous agent actions (first part) — Instructs Claude to act as a security monitor that evaluates autonomous coding agent actions against block/allow rules to prevent prompt injection, scope creep, and accidental damage.
- **NEW:** Agent Prompt: Security monitor for autonomous agent actions (second part) — Defines the environment context, block rules, and allow exceptions that govern which tool actions the agent may or may not perform.
- **NEW:** Skill: /loop slash command — Parses user input into an interval and prompt, converts the interval to a cron expression, and schedules a recurring task.
- **NEW:** System Prompt: Memory system (private feedback) — Describes the private feedback memory type for storing user guidance and corrections, with instructions to check for contradictions against team feedback before saving.
- **NEW:** System Prompt: Team memory content display — Renders shared team memory file contents with path and content for injection into the conversation context.
- **NEW:** System Prompt: Using your tools (how to use searching tools) — Guidance to use `find` or `grep` via Bash for simple, directed codebase searches like finding a specific file, class, or function.
- **NEW:** System Prompt: Using your tools (whether to use Explore subagent) — Guidance to use the Explore subagent for broader codebase exploration and deep research, noting it's slower than direct find/grep and should only be used when simple searches are insufficient.
- **NEW:** Tool Description: CronCreate — Describes the CronCreate tool for enqueuing one-shot or recurring cron-based jobs with jitter and off-minute scheduling guidance.
- Agent Prompt: Claude guide agent — Consolidated individual tool name references (Read, Glob, Grep) into a single grouped reference for local project file searching.
- Agent Prompt: Explore strengths and guidelines — Generalized file search guidance from "Use Grep or Glob" to "search broadly when you don't know where something lives."
- Agent Prompt: Explore — Tool usage guidelines now adapt based on whether embedded tools are active, conditionally including `grep` in allowed Bash operations.
- Agent Prompt: Plan mode (enhanced) — Exploration instructions now adapt between `find`/`grep` and Glob/Grep tool references depending on embedded tools mode; conditionally includes `grep` in allowed Bash operations.
- Agent Prompt: Worker fork execution — Removed Grep and Glob from the explicit tool list; added agent metadata block (fork type, inherited model, permission bubbling, max turns).
- Data: Agent SDK patterns — Python — Added Session History section with examples for listing past sessions and retrieving messages.
- Data: Agent SDK patterns — TypeScript — Added Session History section with examples for listing past sessions and retrieving messages with pagination.
- Data: Agent SDK reference — Python — Added `agent_id`/`agent_type` fields on tool-lifecycle hook inputs; added `stop_reason` to result messages; added typed task message subclasses (TaskStarted, TaskProgress, TaskNotification); added Session History section; added MCP Server Management section with runtime add/remove/status operations.
- Data: Agent SDK reference — TypeScript — Added `agent_id`/`agent_type` fields on tool-lifecycle hook inputs; added `stop_reason` to result messages; added task-related system message subtypes (task_started, task_progress, task_notification); added Session History section with pagination support; added MCP Server Management section with reconnect/toggle/status operations.
- Data: Claude API reference — Go — Substantially expanded: updated basic example to use `context.Background()` and proper content block type-switching; added full manual agentic tool loop example with key API surface table; added Extended Thinking section with enable/disable/adaptive helpers.
- Data: Claude API reference — Python — Updated basic message example to iterate content blocks by type instead of indexing `content[0].text`; updated ConversationManager to use `next()` with type filter.
- Data: Claude API reference — Ruby — Updated basic message example to iterate content blocks by type symbol instead of calling `.first.text`.
- Data: Claude API reference — TypeScript — Updated basic message example to iterate content blocks with type narrowing instead of indexing `content[0].text`.
- Skill: Debugging — Added conditional section informing users when debug logging was just enabled (vs. already active), with instructions to reproduce the issue; fixed typo "relevate" → "relevant."
- Skill: Simplify — Added "Unnecessary JSX nesting" as a new hacky-pattern check for wrapper elements that add no layout value; generalized duplicate-search guidance from tool-specific to broad search language.
- Tool Description: Bash (prefer dedicated tools) — The list of commands to avoid running via Bash (previously hardcoded as find, grep, cat, head, tail, sed, awk, echo) is now dynamically determined based on context.


# [2.1.70](https://github.com/Piebald-AI/claude-code-system-prompts/commit/186e12a)

_+1,212 tokens_

- **NEW:** Agent Prompt: Worker fork execution — System prompt for a forked worker sub-agent that executes a directive directly without spawning further sub-agents, then reports structured results.
- **NEW:** System Prompt: Fork usage guidelines — Instructions for when to fork subagents and rules against reading fork output mid-flight or fabricating fork results.
- **NEW:** System Prompt: Subagent delegation examples — Provides example interactions showing how a coordinator agent should delegate tasks to subagents, handle waiting states, and report results.
- **NEW:** System Prompt: Writing subagent prompts — Guidelines for writing effective prompts when delegating tasks to subagents, covering context-inheriting vs fresh subagent scenarios.
- **NEW:** Tool Description: Agent (usage notes) — Usage notes and instructions for the Task/Agent tool, including guidance on launching subagents, background execution, resumption, and worktree isolation.
- **NEW:** Tool Description: Agent (when to launch subagents) — Describes when to use the Agent tool for launching specialized subagent subprocesses to autonomously handle complex multi-step tasks.
- **REMOVED:** Agent Prompt: User sentiment analysis — Deleted the agent prompt for analyzing user frustration and PR creation requests.
- **REMOVED:** Tool Description: Task — Deleted the Task tool description (replaced by the new Agent usage notes and Agent when-to-launch prompts).
- Agent Prompt: /security-review slash command — Changed git diff command from `--merge-base origin/HEAD` to `origin/HEAD...`; fixed version tag.


# [2.1.69](https://github.com/Piebald-AI/claude-code-system-prompts/commit/2fde688)

_+3,310 tokens_

- **NEW:** Agent Prompt: Common suffix (response format) — Appends response format instructions to agent prompts, switching between concise sub-agent reporting and detailed standalone writeups based on a caller flag.
- **NEW:** Agent Prompt: Explore strengths and guidelines — Defines the strengths and behavioral guidelines for the codebase exploration subagent, emphasizing search strategies, thoroughness, and avoiding unnecessary file creation.
- **NEW:** Agent Prompt: Verification specialist — Re-added system prompt for a verification subagent that adversarially tests implementations and issues PASS/FAIL/PARTIAL verdicts (removed in v2.1.66).
- **NEW:** System Prompt: Agent thread notes — Behavioral guidelines for agent threads covering absolute paths, response formatting, emoji avoidance, and tool call punctuation.
- **NEW:** System Prompt: Analysis instructions for full compact prompt (full conversation) — Compaction analysis instructions for full conversation context.
- **NEW:** System Prompt: Analysis instructions for full compact prompt (minimal and via feature flag) — Lean/experimental compaction analysis instructions.
- **NEW:** System Prompt: Analysis instructions for full compact prompt (recent messages) — Compaction analysis instructions for recent messages only.
- **NEW:** System Prompt: Description part of memory instructions — Field for describing what a memory is, part of memory creation instructions.
- **NEW:** System Prompt: Output efficiency — Re-added instructions for concise, direct output (removed in v2.1.66).
**NEW:** Tool Description: AskUserQuestion (preview field) — Instructions for using the optional `preview` field on single-select question options to display visual artifacts like HTML mockups, code snippets, and diagrams.
- **REMOVED:** Agent Prompt: Task tool — Deleted the general-purpose subagent system prompt (content split into Explore strengths and guidelines and Agent thread notes).
- **REMOVED:** Agent Prompt: Task tool (extra notes) — Deleted additional notes for Task tool usage (content moved to Agent thread notes).
- **REMOVED:** System Reminder: Output token limit exceeded — Deleted the warning shown when a response exceeds the output token limit.
- **REMOVED:** Tool Description: ToolSearch — Deleted the base ToolSearch tool description (content consolidated into ToolSearch extended).
- Agent Prompt: Conversation summarization — Replaced inline analysis instructions with `${ANALYSIS_INSTRUCTION_TAGS}` variable.
- Agent Prompt: /pr-comments slash command — Minor wording changes.
- Agent Prompt: Quick PR creation — Removed hardcoded Changelog section and Slack posting step; made PR creation/edit options and body sections configurable; fixed typo in SAFEUSER variable name.
- Agent Prompt: Recent Message Summarization — Refactored analysis instructions into a shared component.
- Agent Prompt: Status line setup — Re-added `worktree` object to the status line JSON schema (name, path, branch, original cwd, and original branch fields).
- Data: Tool use concepts — Added mention of Python SDK MCP conversion helpers (`anthropic.lib.tools.mcp`).
- Data: Tool use reference — Python — Added full MCP Tool Conversion Helpers section with examples for tool runner integration, prompts, resources as content, and file uploads.
- Skill: Create verifier skills — Re-added self-update guidance: verifiers now offer to edit their own SKILL.md when instructions are outdated; added user-facing note about self-update behavior.
- Skill: Verification specialist — Re-added verifier skill maintenance section for distinguishing outdated verifier instructions from actual feature failures.
- System Prompt: Option previewer — Renamed `markdown` field to `preview`; added description of rendering as markdown in a monospace box with multi-line support.
- Tool Description: Task — Removed 'access to current context' guidance; added note that teammates cannot spawn other teammates when background tasks are disabled.
- Tool Description: TaskCreate — Made `activeForm` parameter optional (spinner falls back to subject when omitted); simplified task creation instructions.
- Tool Description: ToolSearch extended — Re-added comma-separated multi-tool direct selection (e.g., `select:Read,Edit,Grep`).


#### [2.1.68](https://github.com/Piebald-AI/claude-code-system-prompts/commit/a4d3cca)

<sub>_No changes to the system prompts in v2.1.68._</sub>

# [2.1.66](https://github.com/Piebald-AI/claude-code-system-prompts/commit/c55bb75)

_-1,507 tokens_

- **REMOVED:** Agent Prompt: Verification specialist — Deleted the adversarial verification agent prompt that returned PASS/FAIL/PARTIAL verdicts.
- **REMOVED:** System Prompt: Output efficiency instructions — Deleted instructions for concise, direct output.
- **REMOVED:** System Reminder: Ultraplan complete — Deleted the reminder instructing Claude to present a pre-generated plan from a remote session.
- Agent Prompt: Explore — Removed inline `whenToUse` description and `whenToUseDynamic` flag from agent metadata; renamed `Agent` to `tq` in disallowed tools.
- Agent Prompt: Plan mode enhanced — Renamed `Agent` to `tq` in disallowed tools.
- Agent Prompt: Status line setup — Removed `worktree` object from the status line JSON schema (name, path, branch, original cwd, and original branch fields).
- Skill: Create verifier skills — Removed self-update guidance: verifiers no longer offer to edit their own SKILL.md when instructions are outdated.
- Skill: Verification specialist — Removed verifier skill maintenance section for distinguishing outdated verifier instructions from actual feature failures.
- Tool Description: Task — Re-added guidance about agents with "access to current context" seeing full conversation history (had been removed in v2.1.64).
- Tool Description: ToolSearch extended — Removed comma-separated multi-tool direct selection; `select:` now loads only a single named tool.
- Tool Description: ToolSearch — Added `ADDITIONAL_PROMPT_SECTION` variable.

# [2.1.64](https://github.com/Piebald-AI/claude-code-system-prompts/commit/ac581b8)

_+1,291 tokens_

- **NEW:** Agent Prompt: Verification specialist — System prompt for adversarially verifying implementation correctness through builds, tests, and runtime checks, returning PASS/FAIL/PARTIAL verdicts.
- **NEW:** System Prompt: Output efficiency instructions — Instructions for being concise and to the point.
- **NEW:** System Reminder: Ultraplan complete — Instructs Claude to present a pre-generated plan from a remote session without further exploration.
- Agent Prompt: Status line setup — Added `worktree` object to the status line JSON schema with name, path, branch, original cwd, and original branch fields.
- Skill: Create verifier skills — Added self-update guidance: verifiers now offer to edit their own SKILL.md when instructions are outdated rather than reporting a false FAIL.
- Skill: Verification specialist — Added verifier skill maintenance section for distinguishing outdated verifier instructions from actual feature failures, with self-repair workflow.
- Tool Description: Task — Removed guidance about agents with "access to current context" seeing full conversation history.
- Tool Description: ToolSearch extended — Added comma-separated multi-tool direct selection (e.g., `select:Read,Edit,Grep`).
- Tool Description: ToolSearch — Removed `EXTENDED_TOOL_SEARCH_PROMPT` variable; inlined the tool description.


# [2.1.63](https://github.com/Piebald-AI/claude-code-system-prompts/commit/7e37a33)

_+4,200 tokens_

- **NEW:** Agent Prompt: /batch slash command — Instructions for orchestrating a large, parallelizable change across a codebase.
- **NEW:** System Prompt: Worker instructions — Instructions for workers to follow when implementing a change.
- **REMOVED:** Agent Prompt: Bash command file path extraction — System prompt for extracting file paths from bash command output.
- **REMOVED:** Skill: Build with Claude API (trigger) — Activation criteria for the Build with Claude API skill.
- **REMOVED:** System Reminder: Todo list changed — Notification that todo list has changed.
- **REMOVED:** System Reminder: Todo list empty — Reminder that todo list is empty.
- Data: Claude API reference — Go — Added `BetaToolRunner` documentation with the `toolrunner` package; restructured tool use into "Tool Runner (Beta)" and "Manual Loop" sections.
- Data: Claude API reference — PHP — Added Bedrock, Vertex AI, and Foundry client initialization examples; removed version pinning from install command.
- Data: Claude API reference — Java — Updated SDK version from 2.14.0 to 2.15.0.
- Data: Claude API reference — Python — Added automatic caching section for simplified prompt caching alongside existing manual cache control.
- Data: Claude API reference — TypeScript — Added automatic caching section, typed error handling guidance, SDK types guidance (`Anthropic.MessageParam`, etc.), and multi-turn typing improvements.
- Data: HTTP error codes reference — Added typed exceptions table mapping HTTP codes to TypeScript and Python exception classes, with correct/incorrect usage examples.
- Data: Tool use concepts — Expanded tool runner availability to include Java, Go, and Ruby; improved `pause_turn` handling with code example and `max_continuations` guidance; simplified dynamic filtering (no longer requires separate `code_execution` tool or beta header).
- Data: Tool use reference — TypeScript — Added streaming manual loop section combining `stream()` + `finalMessage()` with tool-use loop; added `pause_turn` handling; added SDK type annotations and error handling guidance throughout.
- Data: Tool use reference — Python — Added `pause_turn` handling in manual agentic loop.
- Data: Streaming reference — TypeScript — Enhanced best practices: expanded `finalMessage()` guidance, added `stream.on("text")` tip, added agentic loop streaming cross-reference.
- Data: Claude model catalog — Moved Claude Haiku 3 from current models to deprecated.
- Skill: Build with Claude API — Updated Go SDK to show beta tool runner support; added guidance against reimplementing SDK functionality, redefining SDK types, and guidance on report/document output via code execution sandbox.
- Agent SDK references and patterns (Python, TypeScript) — Renamed `Task` tool to `Agent` in allowed tools, tool tables, and code examples.
- Agent Prompt: Conversation summarization — Fixed list indentation and corrected duplicate section numbering (two section 6s → 6, 7).
- System Reminder: Plan mode is active (5-phase) — Simplified template variables and removed several variable declarations.
- System Reminder: Plan mode is active (iterative) — Restructured plan file info rendering and simplified variable references.
- Tool descriptions (EnterPlanMode, TeammateTool) — Renamed `Task` tool references to `Agent`.
- Hardcoded model IDs (e.g., `claude-opus-4-6`) replaced with template variables (e.g., `{{OPUS_ID}}`) across all SDK reference, data, and skill files.

#### [2.1.62](https://github.com/Piebald-AI/claude-code-system-prompts/commit/5e65215)

<sub>_No changes to the system prompts in v2.1.62._</sub>

#### [2.1.61](https://github.com/Piebald-AI/claude-code-system-prompts/commit/c197152)

<sub>_No changes to the system prompts in v2.1.61._</sub>

# [2.1.59](https://github.com/Piebald-AI/claude-code-system-prompts/commit/6147099)

_-493 tokens_

- **REMOVED:** Data: Claude Code version mismatch warning — Warning shown when Claude Code version is outdated, including update instructions.
- **REMOVED:** System Reminder: Hook JSON validation failed — Error message shown when hook JSON output fails schema validation.

#### [2.1.58](https://github.com/Piebald-AI/claude-code-system-prompts/commit/e92625f)

<sub>_No changes to the system prompts in v2.1.58._</sub>

#### [2.1.56](https://github.com/Piebald-AI/claude-code-system-prompts/commit/3d084a9)

<sub>_No changes to the system prompts in v2.1.56._</sub>

#### [2.1.55](https://github.com/Piebald-AI/claude-code-system-prompts/commit/97cca68)

<sub>_No changes to the system prompts in v2.1.55._</sub>

#### [2.1.54](https://github.com/Piebald-AI/claude-code-system-prompts/commit/ca8e3dd)

<sub>_No changes to the system prompts in v2.1.54._</sub>

# [2.1.53](https://github.com/Piebald-AI/claude-code-system-prompts/commit/f7330d2)

_-617 tokens_

- **NEW:** Agent Prompt: Memory selection - Instructions for selecting relevant memories for a user query (156 tks).
- **REMOVED:** Agent Prompt: Command execution specialist - Removed command execution specialist agent for running bash commands (109 tks).
- **REMOVED:** System Prompt: Main system prompt - Removed standalone core identity prompt; content absorbed into other prompt sections (269 tks).
- Tool Description: Task - Background agents now auto-notify on completion instead of providing an output file path; explicitly discourages sleeping, polling, or proactive checking (1317 → 1331 tks).
- Tool Description: Write - Clarified Write vs Edit guidance: prefer Edit for modifications (sends only the diff), reserve Write for new files or complete rewrites (127 → 129 tks).
- Widespread decomposition of 6 monolithic system prompts and 2 tool descriptions into ~70 smaller atomic files. Content is largely preserved but reorganized into independently addressable units, with some new sub-prompts (e.g., "ambitious tasks", "blocked approach", "code references") and redistributed content (e.g., "no time estimates" moved from Tone and style to Doing tasks):
  - System Prompt: Doing tasks (437 tks) → 13 files covering software engineering focus, read-before-modifying, security, over-engineering, unnecessary additions, error handling, premature abstractions, compatibility hacks, file creation, time estimates, help/feedback, ambitious tasks, and blocked approach.
  - System Prompt: Tone and style (500 tks) → 3 files covering code references, concise output (detailed), and concise output (short).
  - System Prompt: Tool usage policy (352 tks) → 11 files covering create/edit/read/search files, Bash reservation, content search, delegate exploration, direct search, skill invocation, subagent guidance, and task management.
  - System Prompt: Task management (565 tks) → merged into Tool usage (task management) sub-prompt (73 tks).
  - System Prompt: Conditional delegate codebase exploration (249 tks) → merged into Tool usage (delegate exploration) sub-prompt (114 tks).
  - Tool Description: Bash (1067 tks) + Bash (sandbox note) (438 tks) → 45 files covering overview, working directory, timeout, command description, quoting, sequential/parallel commands, newlines, semicolons, cwd maintenance, dedicated-tool preferences, 6 alternative-tool notes, git safety (3 files), sleep guidance (6 files), sandbox policy (17 files), and verify-parent-directory.

#### [2.1.52](https://github.com/Piebald-AI/claude-code-system-prompts/commit/94cd8e5)

<sub>_No changes to the system prompts in v2.1.52._</sub>

# [2.1.51](https://github.com/Piebald-AI/claude-code-system-prompts/commit/1988a63)

_+6,918 tokens_

- **NEW:** Agent Prompt: Quick PR creation - Streamlined prompt for creating a commit and pull request with pre-populated context (945 tks).
- **NEW:** Agent Prompt: Quick git commit - Streamlined prompt for creating a single git commit with pre-populated context (507 tks).
- **NEW:** Data: Agent SDK reference — TypeScript - TypeScript Agent SDK reference including installation, quick start, custom tools, and hooks (2287 tks).
- **NEW:** Data: Claude Code version mismatch warning - Warning shown when Claude Code version is outdated (173 tks).
- **NEW:** Skill: Create verifier skills - Prompt for creating verifier skills for the Verify agent to automatically verify code changes (2586 tks).
- **NEW:** System Reminder: Hook JSON validation failed - Error when hook JSON output fails validation (320 tks).
- **REMOVED:** Agent Prompt: Single-word search term extractor - Removed prompt for extracting single-word search terms from a user's query (361 tks).
- Data: Agent SDK patterns — Python - Replaced `asyncio` with `anyio`; switched message type checks from `message.type == "result"` to `isinstance(message, ResultMessage)`; custom tools now require MCP server via `create_sdk_mcp_server` + `ClaudeSDKClient`; added `permission_mode="plan"` and `allow_dangerously_skip_permissions` for bypass mode (2080 → 2350 tks).
- Data: Agent SDK reference — Python - Added `ClaudeSDKClient` interface with full lifecycle control; expanded built-in tools table (`AskUserQuestion`, `Task`); added `plan` and `dontAsk` permission modes; greatly expanded Common Options table with `max_budget_usd`, `output_format`, `thinking`, `betas`, `setting_sources`, `env`, and more; updated hook events list with 15+ event types (1718 → 2750 tks).
- Data: Tool use concepts - Code execution promoted from beta to GA (`code_execution_20260120`); added new server-side tools sections for Web Search/Fetch (`web_search_20260209`, `web_fetch_20260209`) with dynamic filtering, Programmatic Tool Calling, Tool Search, and Tool Use Examples; removed beta requirement for memory tool; updated structured outputs guidance for `output_config.format` (2820 → 3640 tks).
- Data: Tool use reference — Python - Migrated code execution and memory from `client.beta.messages.create` to `client.messages.create`; removed `betas` arrays; Files API beta now passed via `extra_headers` (4261 → 4180 tks).
- Data: Tool use reference — TypeScript - Same beta→GA migration as Python; structured output example updated from `output_format` to `output_config.format` (3294 → 3228 tks).
- Data: Claude API reference — Python - Added explicit TTL support for `cache_control` (`"ttl": "1h"`); extended adaptive thinking note to include Sonnet 4.6; added Stop Reasons table (`end_turn`, `max_tokens`, `tool_use`, `pause_turn`, `refusal`); updated rate limit error handling; changed Sonnet reference to `claude-sonnet-4-6` (2905 → 3248 tks).
- Data: Claude API reference — TypeScript - Added explicit TTL for `cache_control`; extended adaptive thinking to Sonnet 4.6; added Stop Reasons table (2024 → 2388 tks).
- Data: Claude API reference — Java - Updated SDK version 2.11.1 → 2.14.0; improved streaming with fluent stream API; added `anthropic-beta` header for structured outputs; added non-beta tool use section (1073 → 1226 tks).
- Data: Claude API reference — C# - Removed "beta" label; expanded streaming example with typed `RawMessageStreamEvent` handling (458 → 550 tks).
- Data: Claude API reference — Ruby - Updated tool runner to use `BaseModel` input schema pattern with `doc` method and `input` parameter (603 → 622 tks).
- Data: Claude API reference — Go - Updated model constants from `ModelClaudeOpus4_5_20251101` to `ModelClaudeOpus4_6` (629 → 621 tks).
- Data: Claude API reference — PHP - Removed "beta" label; updated SDK 0.4.0 → 0.5.0; switched from array syntax to named parameters (410 → 394 tks).
- Data: Claude model catalog - Added Max Output column (128K for Opus, 64K for Sonnet/Haiku); Opus 4.6 now shows 1M beta context; added Model Descriptions section; moved Sonnet 3.7 and Haiku 3.5 from "deprecated" to "retired"; updated alias table accordingly (1349 → 1510 tks).
- Data: HTTP error codes reference - Replaced human-readable error names with API error type strings (e.g., `invalid_request_error`); removed 422 status code, merging validation errors into 400; stripped escaped markdown formatting (1460 → 1387 tks).
- Skill: Build with Claude API - Opus 4.6 now shows 1M beta context; stronger default-model guidance ("ALWAYS use `claude-opus-4-6`"); extended adaptive thinking and effort parameter to Sonnet 4.6; expanded thinking/budget_tokens deprecation notes; removed "beta" labels from C#/PHP SDKs (token count unchanged).
- Skill: Build with Claude API (trigger) - Simplified trigger criteria to explicit SDK import checks (`anthropic`, `claude_agent_sdk`); clearer DO NOT TRIGGER rules (token count unchanged).
- Tool Description: EnterWorktree - Added explicit "When NOT to Use" section; narrowed activation to only when user explicitly says "worktree"; no longer triggers for general isolation or branch requests (284 → 334 tks).
- Data: Agent SDK patterns — TypeScript - Fixed session init check from `"subtype" in message` to `message.type === "system"` (1067 → 1069 tks).
- Data: Message Batches API reference — Python - Added `"canceled"` result type handling (1481 → 1505 tks).
- Widespread internal variable renames across 12 files (e.g., `ADDITIONAL_USER_INPUT` → `USER_INPUT`, `PREVIOUS_AGENT_SUMMARY` → `PREVIOUS_SUMMARY`, `SYSTEM_REMINDER` → `PLAN_STATE`, `COMMIT_CO_AUTHORED_BY_CLAUDE_CODE` → `ATTRIBUTION_TEXT`, `IS_TRUTHY_FN` → `IS_BACKGROUND_TASKS_DISABLED_FN`, `CAN_READ_PDF_FILES` → `IS_PDF_SUPPORTED_FN`, and others).


# [2.1.50](https://github.com/Piebald-AI/claude-code-system-prompts/commit/5fa66df)

_+110 tokens_

- Tool Description: EnterWorktree - Generalized from git-only to support VCS-agnostic isolation via `WorktreeCreate`/`WorktreeRemove` hooks; requirements now allow non-git repos with hooks configured (237 → 284 tks).
- Tool Description: ReadFile - Replaced hardcoded "cat -n format" line-number note with a `CONDITIONAL_READ_LINES` variable (476 → 468 tks).
- Tool Description: Task - Added `isolation: "worktree"` option to run agents in temporary git worktrees with automatic cleanup (1228 → 1299 tks).

#### [2.1.49](https://github.com/Piebald-AI/claude-code-system-prompts/commit/8da43fb)

<sub>_No changes to the system prompts in v2.1.49._</sub>

# [2.1.48](https://github.com/Piebald-AI/claude-code-system-prompts/commit/0d57836)

_-1,082 tokens_

- **NEW:** Tool Description: EnterWorktree - Tool description for the EnterWorktree tool (237 tks).
- **REMOVED:** System Prompt: MCP CLI - Removed instructions for using mcp-cli to interact with Model Context Protocol servers (1333 tks).
- Tool Description: Task - Simplified background agent output-file guidance; removed `BASH_TOOL` variable and `tail` instructions; added new "Foreground vs background" bullet explaining when to use each mode (1214 → 1228 tks).

# [2.1.47](https://github.com/Piebald-AI/claude-code-system-prompts/commit/f58cba9)

_+34,752 tokens_

- **NEW:** Data: Agent SDK patterns — Python (2080 tks), Agent SDK patterns — TypeScript (1067 tks), Agent SDK reference — Python (1718 tks) - SDK pattern guides and reference for Python and TypeScript Agent SDKs.
- **NEW:** Data: Claude API reference — C# (458 tks), Go (629 tks), Java (1073 tks), PHP (410 tks), Python (2905 tks), Ruby (603 tks), TypeScript (2024 tks) - SDK references for all supported Claude API client languages.
- **NEW:** Data: Claude model catalog (1349 tks) - Catalog of current and legacy Claude models with IDs, aliases, context windows, and pricing.
- **NEW:** Data: Files API reference — Python (1303 tks), TypeScript (798 tks) - References for the Files API covering upload, listing, deletion, and message usage.
- **NEW:** Data: HTTP error codes reference (1460 tks) - Reference for Claude API HTTP error codes with common causes and handling strategies.
- **NEW:** Data: Live documentation sources (2337 tks) - WebFetch URLs for fetching current Claude API and Agent SDK documentation from official sources.
- **NEW:** Data: Message Batches API reference — Python (1481 tks) - Batches API reference including batch creation, status polling, and result retrieval.
- **NEW:** Data: Streaming reference — Python (1534 tks), TypeScript (1553 tks) - Streaming references covering sync/async streaming and content type handling.
- **NEW:** Data: Tool use concepts (2820 tks) - Conceptual foundations of tool use including definitions, tool choice, and best practices.
- **NEW:** Data: Tool use reference — Python (4261 tks), TypeScript (3294 tks) - Tool use references covering tool runner, agentic loops, code execution, and structured outputs.
- **REMOVED:** Agent Prompt: Prompt Suggestion Generator (Coordinator) - Removed the coordinator-mode prompt suggestion generator that predicted what a team supervisor would type next (283 tks).
- **REMOVED:** System Reminder: Delegate mode prompt - Removed the delegate mode system reminder that restricted tool usage to team coordination tools (185 tks).
- **REMOVED:** System Reminder: Exited delegate mode - Removed the notification shown when exiting delegate mode (50 tks).
- Agent Prompt: Status line setup - Added `added_dirs` field to the workspace schema for directories added via `/add-dir` (1482 → 1502 tks).
- Tool Description: AskUserQuestion - Added `EXIT_PLAN_MODE_TOOL_NAME` variable; expanded plan mode guidance to warn against referencing "the plan" in questions, since users cannot see the plan until `ExitPlanMode` is called (194 → 287 tks).

# [2.1.45](https://github.com/Piebald-AI/claude-code-system-prompts/commit/36d2856)

_+276 tokens_

- **NEW:** Agent Prompt: Single-word search term extractor - System prompt for extracting single-word search terms from a user's query (361 tks).
- **NEW:** System Prompt: Option previewer - System prompt for previewing UI options in a side-by-side layout (129 tks).
- **REMOVED:** Agent Prompt: Prompt Suggestion Generator (Stated Intent) - Removed the stated-intent prompt suggestion generator that returned a user's explicitly stated next step (166 tks).
- Agent Prompt: /review-pr slash command - Replaced `${BASH_TOOL_OBJECT.name}(...)` template expressions with plain backtick-quoted `gh` commands; removed `BASH_TOOL_OBJECT` variable (243 → 211 tks).
- Tool Description: Bash (sandbox note) - Removed `CONDITIONAL_NEWLINE_IF_SANDBOX_ENABLED` variable; the conditional newline before the "Set dangerouslyDisableSandbox" bullet is now always included (454 → 438 tks).

#### [2.1.44](https://github.com/Piebald-AI/claude-code-system-prompts/commit/eb6a818)

<sub>_No changes to the system prompts in v2.1.44._</sub>

# [2.1.42](https://github.com/Piebald-AI/claude-code-system-prompts/commit/8a1123a)

_-1,060 tokens_

- **REMOVED:** Agent Prompt: Remember skill - Removed the `/remember` skill prompt that reviewed session memories and updated CLAUDE.local.md with recurring patterns and learnings (1048 tks).
- Tool Description: WebSearch - Simplified date-awareness variables; replaced `GET_CURRENT_DATE_FN` and `CURRENT_YEAR` with a single `CURRENT_MONTH_YEAR` variable; updated example to use plain text ("with the current year, NOT last year") instead of template expressions (331 → 319 tks).

# [2.1.41](https://github.com/Piebald-AI/claude-code-system-prompts/commit/91732e4)

_+262 tokens_

- **NEW:** System Prompt: Conditional delegate codebase exploration - Added instructions for when to use the Explore subagent versus calling tools directly (249 tks).
- System Prompt: Tool usage policy - Replaced inline "VERY IMPORTANT" block and examples about delegating codebase exploration to the Explore agent with a conditional variable reference; removed `GLOB_TOOL_NAME` and `GREP_TOOL_NAME` variables (564 → 352 tks).
- System Prompt: Skillify Current Session - Added Round 2 prompt to ask the user where to save the skill (repo-specific vs personal); updated Step 3 to use the user-chosen location instead of hardcoded `.claude/skills/`; changed Step 4 to output the SKILL.md as a YAML code block for review and use a simpler AskUserQuestion confirmation (1750 → 1882 tks).
- System Reminder: Plan mode is active (5-phase) - Made Explore subagent usage conditional; when disabled, Phase 1 now instructs Claude to use Glob, Grep, and Read tools directly; updated Phase 2 variable references for plan subagent and agent count (1429 → 1500 tks).
- Agent Prompt: Status line setup - Added `session_name` field (optional human-readable session name set via `/rename`) to the JSON input spec (1460 → 1482 tks).

# [2.1.40](https://github.com/Piebald-AI/claude-code-system-prompts/commit/06ce2b9)

_-293 tokens_

- **REMOVED:** Agent Prompt: Evolve currently-running skill - Removed agent prompt for evolving a currently-running skill based on user requests or preferences (293 tks).

# [2.1.39](https://github.com/Piebald-AI/claude-code-system-prompts/commit/11e9ec6)

_+293 tokens_

- **NEW:** Agent Prompt: Evolve currently-running skill - Added new agent prompt for evolving a currently-running skill based on what the user is implicitly or explicitly requesting (293 tks).

# [2.1.38](https://github.com/Piebald-AI/claude-code-system-prompts/commit/30adcee)

_+105 tokens_

- **NEW:** Agent Prompt: Prompt Suggestion Generator (Coordinator) - Added new agent prompt for prompt suggestion generation in coordinator mode (283 tks).
- **NEW:** System Prompt: Context compaction summary - Added new prompt used for context compaction summary for the SDK (278 tks).
- **NEW:** Tool Description: TaskList (teammate workflow) - Added conditional section appended to the TaskList tool description for teammate workflows (133 tks).
- **REMOVED:** Agent Prompt: Prompt Suggestion Generator (for Agent Teams) - Removed agent-teams-specific prompt suggestion generator (209 tks).
- **REMOVED:** System Prompt: Accessing past sessions - Removed instructions for searching past session data including memory summaries and transcript logs (352 tks).
- Tool Description: Sleep - Simplified description; replaced "Wakes early if the user sends a message" with "The user can interrupt the sleep at any time" and removed other references to early wake behavior.
- Tool Description: Task - Fixed typo in example agent description ("when to respond" → "to respond") and corrected mismatched XML closing tag.
- Tool Description: Bash (Git commit and PR creation instructions) - Minor formatting cleanup in the git amend warning text.

#### [2.1.37](https://github.com/Piebald-AI/claude-code-system-prompts/commit/e687bd6)

<sub>_No changes to the system prompts in v2.1.37._</sub>

#### [2.1.36](https://github.com/Piebald-AI/claude-code-system-prompts/commit/933e339)

<sub>_No changes to the system prompts in v2.1.36._</sub>

#### [2.1.34](https://github.com/Piebald-AI/claude-code-system-prompts/commit/0e01416)

<sub>_No changes to the system prompts in v2.1.34._</sub>

# [2.1.33](https://github.com/Piebald-AI/claude-code-system-prompts/commit/38ebc6b)

_-1,086 tokens_

- **NEW:** Agent Prompt: Prompt Suggestion Generator (for Agent Teams) - Instructions for generating prompt suggestions when agent swarms are enabled
- **NEW:** Tool Description: TeamDelete - Tool description for deleting/cleaning up team resources
- **REMOVED:** System Prompt: Action Suggestor for the Task Coordinator - Removed system prompt for suggesting actions to the task coordinator
- **REMOVED:** Tool Description: EnterPlanMode (ambiguous tasks) - Removed separate conditional description for entering plan mode on ambiguous tasks
- System Reminder: Plan mode is active (5-phase) - Added requirement to begin Phase 4's final plan with a **Context** section explaining why the change is being made
- System Reminder: Plan mode is active (iterative) - Major rewrite: consolidated variables; restructured from a 5-step "How to Work" section into a streamlined "The Loop" cycle (Explore → Update plan → Ask user); added new "First Turn", "Asking Good Questions", and "When to Converge" sections; reframed as pair-planning with the user; reduced from 909 to 797 tokens
- Tool Description: EnterPlanMode - Extracted "What Happens in Plan Mode" section into a conditional variable (`CONDITIONAL_WHAT_HAPPENS_NOTE`); reduced from 970 to 878 tokens
- Tool Description: Task - Removed `AGENT_TEAM_CHECK` variable and conditional note about Agent Teams not being available on certain plans; reduced from 1340 to 1215 tokens
- Tool Description: TeammateTool - Renamed tool heading from "TeammateTool" to "TeamCreate"; removed `spawnTeam` operation label and `cleanup` operation (now separate TeamDelete tool); added explicit file paths for created team and task list resources; added note about automatic message delivery; updated workflow to reference TeamCreate; reduced from 1790 to 1642 tokens

# [2.1.32](https://github.com/Piebald-AI/claude-code-system-prompts/commit/a362f28)

_+2,323 tokens_

- **NEW:** Agent Prompt: Recent Message Summarization - Agent prompt used for summarizing recent messages
- **NEW:** System Prompt: Action Suggestor for the Task Coordinator - System prompt used for suggesting actions to the task coordinator or team lead
- **NEW:** System Prompt: Agent Summary Generation - System prompt used for "Agent Summary" generation
- **NEW:** System Prompt: Skillify Current Session - System prompt for converting the current session into a skill
- System Prompt: Executing actions with care - Added guidance about lock files: investigate what process holds a lock file rather than deleting it
- System Prompt: Teammate Communication - Rebranded from "Teammate Communication" to "Agent Teammate Communication"; updated to reference SendMessage tool instead of Teammate tool; simplified and clarified communication instructions; reduced from 138 to 127 tokens
- System Reminder: Plan mode is active (iterative) - Updated guidance about using the Explore agent type, clarifying it's useful for parallelizing complex searches but direct tools are simpler for straightforward queries
- Tool Description: SendMessageTool - Updated terminology from "teammates in a swarm" to "agent teammates in a team"
- Tool Description: TeammateTool - Major refactoring: removed operations (discoverTeams, requestJoin, approveJoin, rejectJoin) and Environment Variables section; added "When to Use" and "Choosing Agent Types for Teammates" sections; added note about peer DM visibility in idle notifications; streamlined team workflow and coordination instructions; clarified that teammates should not send structured JSON status messages; reduced from 2393 to 1790 tokens

# [2.1.31](https://github.com/Piebald-AI/claude-code-system-prompts/commit/e273964400723d0b8b50b871aa056ba3a2267ad0)

_+693 tokens_

- **NEW:** System Prompt: Agent memory instructions - Instructions for including domain-specific memory update guidance in agent system prompts (e.g., for code reviewers, test runners, architects)
- **NEW:** System Prompt: Censoring assistance with malicious activities - Guidelines for assisting with authorized security testing, defensive security, CTF challenges, and educational contexts while refusing malicious requests (previously removed in v2.1.20, now re-added)
- **NEW:** System Prompt: Tool permission mode - Guidance on tool permission modes and handling denied tool calls; advises not to re-attempt denied tool calls and to adjust approach instead
- **NEW:** System Reminder: Hook stopped continuation prefix - Prefix for hook stopped continuation messages
- **NEW:** Tool Description: ToolSearch extended - Extended usage instructions for ToolSearch moved to separate conditional prompt (query modes, examples, correct/incorrect usage patterns)
- **REMOVED:** Tool Description: TeammateTool operation parameter - Description of the operation parameter for the TeammateTool (removed)
- Tool Description: Task - Added conditional note about "Agent Teams" feature (TeammateTool, SendMessage, spawnTeam) not being available on certain plans; clarifies this limitation only applies when users explicitly ask for agent teams or peer-to-peer messaging
- Tool Description: ToolSearch - Refactored: moved extended content to separate `ToolSearch extended` prompt; simplified base description now references `<available-deferred-tools>` messages and conditionally includes extended content via identifier


# [2.1.30](https://github.com/Piebald-AI/claude-code-system-prompts/commit/87f225d)

_+3,152 tokens_

- **NEW:** System Prompt: Executing actions with care - Instructions for executing actions carefully
- **NEW:** System Prompt: Insights at a glance summary - Generates a concise 4-part summary (what's working, hindrances, quick wins, ambitious workflows) for the insights report
- **NEW:** System Prompt: Insights friction analysis - Analyzes aggregated usage data to identify friction patterns and categorize recurring issues
- **NEW:** System Prompt: Insights on the horizon - Identifies ambitious future workflows and opportunities for autonomous AI-assisted development
- **NEW:** System Prompt: Insights session facets extraction - Extracts structured facets (goal categories, satisfaction, friction) from a single Claude Code session transcript
- **NEW:** System Prompt: Insights suggestions - Generates actionable suggestions including CLAUDE.md additions, features to try, and usage patterns
- **NEW:** System Prompt: Parallel tool call note - System prompt for telling Claude to use parallel tool calls
- **NEW:** Tool Description: Sleep - Tool for waiting/sleeping with early wake capability on user input
- System Prompt: Accessing past sessions - Added tip to truncate search results to 64 characters per match to keep context manageable
- System Prompt: Hooks Configuration - Significantly restructured hook response format with new fields including `suppressOutput`, `decision`, `reason`, and `hookSpecificOutput` with event-specific parameters
- System Reminder: Plan mode is active (5-phase) - Added guidance to actively search for and reuse existing functions, utilities, and patterns, with emphasis on including references to found utilities in the plan
- System Reminder: Plan mode is active (iterative) - Added similar guidance about reusing existing code and including references to found utilities in the plan
- Tool Description: ReadFile - Added requirement to use `pages` parameter for large PDFs (more than 10 pages), with maximum 20 pages per request
- Tool Description: SendMessageTool - Restructured message types (removed nested "request" and "response" types), added required `summary` field for message and broadcast types, flattened protocol to use specific types like `shutdown_request`, `shutdown_response`, `plan_approval_response`
- Tool Description: Task - Restructured preamble section
- Tool Description: TeammateTool - Clarified that teammates go idle after every turn (not just when done), explained that idle teammates can still receive messages and will wake up to process them, and clarified that idle notifications are automatic and normal

#### [2.1.29](https://github.com/Piebald-AI/claude-code-system-prompts/commit/e2d243c)

<sub>_No changes to the system prompts in v2.1.29._</sub>

#### [2.1.28](https://github.com/Piebald-AI/claude-code-system-prompts/commit/79616d9)

<sub>_No changes to the system prompts in v2.1.28._</sub>

#### [2.1.27](https://github.com/Piebald-AI/claude-code-system-prompts/commit/de0f1c3)

<sub>_No changes to the system prompts in v2.1.27._</sub>

# [2.1.26](https://github.com/Piebald-AI/claude-code-system-prompts/commit/f8e3357)

_+0 tokens_

- Agent Prompt: Prompt Suggestion Generator (Stated Intent) - Increased maximum suggestion length from 2-8 words to 2-12 words
- Agent Prompt: Prompt Suggestion Generator v2 - Increased maximum suggestion length from 2-8 words to 2-12 words

#### [2.1.25](https://github.com/Piebald-AI/claude-code-system-prompts/commit/5f194f5)

<sub>_No changes to the system prompts in v2.1.25._</sub>

# [2.1.23](https://github.com/Piebald-AI/claude-code-system-prompts/commit/44566a0)

_-383 tokens_

- **NEW:** System Reminder: /btw side question - System reminder for /btw slash command side questions without tools
- **REMOVED:** Agent Prompt: Exit plan mode with swarm - System reminder for when ExitPlanMode is called with `isSwarm` set to true
- System Prompt: Main system prompt - Removed trailing period after SECURITY_POLICY variable
- Tool Description: Skill - Simplified and streamlined: removed examples section, condensed important notes, changed from listing available skills inline to referencing system-reminder messages, updated variable references (FORMAT_SKILLS_AS_XML_FN → SKILL_TAG_NAME, removed LIMITED_COMMANDS)
- Tool Description: TeammateTool - Updated UI notification description: now shows "a brief notification with the sender's name" instead of "Queued teammate messages" when messages are waiting

#### [2.1.22](https://github.com/Piebald-AI/claude-code-system-prompts/commit/5c57ba3)

<sub>_No changes to the system prompts in v2.1.22._</sub>

# [2.1.21](https://github.com/Piebald-AI/claude-code-system-prompts/commit/51239d3)

_+442 tokens_

- **NEW:** System Prompt: Accessing past sessions - Instructions for searching past session data including memory summaries and transcript logs
- Tool Description: TeammateTool - Added guidance to prefer tasks in ID order (lowest ID first) when multiple tasks are available, as earlier tasks often set up context for later ones


# [2.1.20](https://github.com/Piebald-AI/claude-code-system-prompts/commit/18fd5f9)

_-1,928 tokens_

- **NEW:** System Prompt: Doing tasks - Instructions for performing software engineering tasks
- **NEW:** System Prompt: Task management - Instructions for using task management tools
- **NEW:** System Prompt: Tone and style - Guidelines for communication tone and response style
- **NEW:** System Prompt: Tool usage policy - Policies and guidelines for tool usage
- **NEW:** Tool Description: SendMessageTool - Tool for sending messages to teammates and handling protocol requests/responses in a swarm
- **NEW:** Tool Description: EnterPlanMode (ambiguous tasks) - Tool for entering plan mode when task has ambiguity
- **REMOVED:** System Prompt: Censoring assistance with malicious activities - Guidelines for assisting with authorized security testing
- **REMOVED:** System Reminder: Queued command (prompt) - Queued user message to address (prompt variant)
- **REMOVED:** System Reminder: Queued command - Queued user message to address
- **REMOVED:** System Reminder: Session memory - Past session summaries that may be relevant
- System Prompt: Main system prompt - Massively reduced from 2896 to 269 tokens; most content extracted into separate, focused system prompts (Doing tasks, Task management, Tone and style, Tool usage policy)
- Agent Prompt: Session title and branch generation - Changed output format from XML-style tags to JSON object with "title" and "branch" fields
- Agent Prompt: Bash command prefix detection - Changed from smart quotes to standard quotes
- Tool Description: TeammateTool - Removed protocol operations (approvePlan, rejectPlan, requestShutdown, approveShutdown, rejectShutdown, write, broadcast) and simplified to core team management operations
- Tool Description: TeammateTool operation parameter - Renamed from "TeammateTool's operation parameter" and condensed from 173 to 72 tokens
- Tool Description: Edit - Simplified by removing explicit read tool requirement from usage notes
- Tool Description: Write - Simplified by removing explicit read tool requirement from usage notes
- Tool Description: Bash (Git commit and PR creation instructions) - Added guidance to keep PR titles short (under 70 characters) and use description/body for details
- System Prompt: Tool execution denied - Streamlined wording
- Agent Prompt: Conversation summarization with additional instructions - Merged into base "Conversation summarization" prompt; additional instructions now added conditionally via code rather than as separate prompt string
- Agent Prompt: Prompt Hook execution - Shortened from 485 to 263 characters; removed verbose JSON formatting instructions


# [2.1.19](https://github.com/Piebald-AI/claude-code-system-prompts/commit/fcf3f24)

_+182 tokens_

- **NEW:** System Prompt: Tool Use Summary Generation - Prompt for generating summaries of tool usage
- **REMOVED:** Tool Description: TaskList - Description for the TaskList tool, which lists all tasks in the task list
- Agent Prompt: Status line setup - Added agent information (name and type) to the statusLine structure for agents started with --agent flag
- Tool Description: Skill - Updated wording from "Only use skills listed in 'Available skills' below" to "Skills listed below are available for invocation"
- Tool Description: TaskCreate - Added template variables for conditional notes and restructured task assignment instructions
- Tool Description: ToolSearch - Major expansion: reordered query modes (keyword search now first), clarified that both modes load tools immediately, added required keyword syntax with + prefix, expanded examples to show redundant selection patterns to avoid

#### [2.1.18](https://github.com/Piebald-AI/claude-code-system-prompts/commit/a3f5e2e)

<sub>_No changes to the system prompts in v2.1.18._</sub>

#### [2.1.17](https://github.com/Piebald-AI/claude-code-system-prompts/commit/4615ff3)

<sub>_No changes to the system prompts in v2.1.17._</sub>

# [2.1.16](https://github.com/Piebald-AI/claude-code-system-prompts/commit/e8da828)

_+7,114 tokens_

- **NEW:** Agent Prompt: Exit plan mode with swarm - System reminder for when ExitPlanMode is called with `isSwarm` set to true
- **NEW:** System Prompt: Teammate Communication - System prompt for teammate communication in swarm
- **NEW:** System Prompt: Tool execution denied - System prompt for when tool execution is denied
- **NEW:** System Reminder: Delegate mode prompt - System reminder for delegate mode
- **NEW:** System Reminder: Plan mode is active (5-phase) - Enhanced plan mode system reminder with parallel exploration and multi-agent planning
- **NEW:** System Reminder: Plan mode is active (iterative) - Iterative plan mode system reminder for main agent with user interviewing workflow
- **NEW:** System Reminder: Team Coordination - System reminder for team coordination
- **NEW:** System Reminder: Team Shutdown - System reminder for team shutdown
- **NEW:** Tool Description: TaskCreate - Tool description for TaskCreate tool
- **NEW:** Tool Description: TaskList - Description for the TaskList tool, which lists all tasks in the task list
- **NEW:** Tool Description: TeammateTool's operation parameter - Tool description for the TeammateTool's operation parameter
- **NEW:** Tool Description: TeammateTool - Tool description for the TeammateTool
- **NEW:** Tool Parameter: Computer action for Computer tool - Action parameter options for the Chrome browser computer tool (includes hover action and other actions)
- Agent Prompt: /security-review slash command - Renamed from "/security-review slash" for consistency
- System Prompt: Learning mode - Description metadata updated (removed "System Prompt:" prefix)
- System Reminder: Plan mode is active (subagent) - Renamed from "Plan mode is active (for subagents)" for consistency
- Tool Description: Bash (Git commit and PR creation instructions) - Added guidance to avoid using --no-edit flag with git rebase commands, as it is not a valid option for git rebase
- Tool Description: Write - Description clarified from "creating/overwriting writing individual files" to "for creating and overwriting individual files"

# [2.1.15](https://github.com/Piebald-AI/claude-code-system-prompts/commit/011066d)

_+183 tokens_

- Tool Description: Bash (Git commit and PR creation instructions) - expanded Git Safety Protocol with specific list of destructive commands and added detailed explanation about potential data loss; clarified that `--amend` should be avoided after pre-commit hook failures; added guidance to prefer staging specific files by name rather than using "git add -A" or "git add ." to avoid accidentally including sensitive files (.env, credentials) or large binaries
- Tool Description: Task - updated background agent output retrieval instructions from using TaskOutput tool to reading output_file path with Read tool or using Bash with `tail` to see recent output; added conditional note about run_in_background, name, team_name, and mode parameters not being available in certain contexts


# [2.1.14](https://github.com/Piebald-AI/claude-code-system-prompts/commit/8533e3b)

_-1,153 tokens_

- **NEW:** Agent Prompt: Prompt Suggestion Generator (Stated Intent) - instructions for generating prompt suggestions based on user's explicitly stated next steps
- **NEW:** Tool Description: ToolSearch - renamed from MCPSearch; tool description for loading and searching deferred tools before use
- **REMOVED:** Tool Description: ExitPlanMode v2 and ExitPlanMode v2 (security notes) - consolidated functionality into base ExitPlanMode
- **REMOVED:** Tool Description: MCPSearch and MCPSearch (with available tools) - replaced by ToolSearch
- Tool Description: ExitPlanMode - added "How This Tool Works" section explaining plan file workflow; clarified that tool reads from plan file rather than taking plan as parameter; simplified "Handling Ambiguity in Plans" section to "Before Using This Tool" with clearer guidance on when to use AskUserQuestion; removed variable references in favor of direct tool names
- Tool Description: Bash - clarified session persistence behavior: "Working directory persists between commands; shell state (everything else) does not. The shell environment is initialized from the user's profile (bash or zsh)"
- Tool Description: WebFetch - added guidance to prefer gh CLI via Bash for GitHub URLs (e.g., gh pr view, gh issue view, gh api)
- System Prompt: Chrome browser MCP tools - updated to reference ToolSearch instead of MCPSearch

#### [2.1.12](https://github.com/Piebald-AI/claude-code-system-prompts/commit/4277b8b)

<sub>_No changes to the system prompts in v2.1.12._</sub>

#### [2.1.11](https://github.com/Piebald-AI/claude-code-system-prompts/commit/b90a97d)

<sub>_No changes to the system prompts in v2.1.11._</sub>

# [2.1.10](https://github.com/Piebald-AI/claude-code-system-prompts/commit/9cb8c2c)

_-118 tokens_

- Agent Prompt: Session title and branch generation - added explicit instruction to use sentence case for titles (capitalize only the first word and proper nouns), not Title Case
- Tool Description: Bash (Git commit and PR creation instructions) - simplified git commit --amend guidance by removing complex conditional rules (5 conditions about when amending is allowed); replaced with simpler CRITICAL directive to always create new commits and never use --amend unless user explicitly requests it; removed reference to "amend rules above" in pre-commit hook failure step

# [2.1.9](https://github.com/Piebald-AI/claude-code-system-prompts/commit/0f37d97)

_+963 tokens_

- **NEW:** System Prompt: Hooks Configuration - system prompt for hooks configuration, used for Claude Code config skill
- **REMOVED:** System Prompt: Autonomous agent (standalone) - standalone autonomous agent mode prompt without system context prefix
- **REMOVED:** System Prompt: Autonomous agent (with context) - autonomous agent mode prompt prefixed with main system prompt
- System Prompt: Main system prompt - renamed "Planning without timelines" section to "No time estimates"; expanded guidance to explicitly prohibit giving time estimates for Claude's own work (e.g., "this will take me a few minutes," "should be done in about 5 minutes," "this is a quick fix") in addition to existing prohibition on suggesting project timelines; added emphasis that users should judge timing themselves

# [2.1.8](https://github.com/Piebald-AI/claude-code-system-prompts/commit/168ab21)

_-101 tokens_

- System Reminder: Plan mode is active - extracted inline plan file info section into separate, new section; converted hardcoded phase numbers (2-5) to dynamic variables for conditional user interview phase; replaced user interview guidance with a new phase explicitly for user interview
- Tool Description: WebSearch - updated year example to use the current year instead of hardcoded year value

# [2.1.7](https://github.com/Piebald-AI/claude-code-system-prompts/commit/3772a02)

_+74 tokens_

- **NEW:** Tool Description: ExitPlanMode v2 (security notes) - security guidelines for scoping permissions when using the ExitPlanMode tool
- System Prompt: Claude in Chrome browser automation - added IMPORTANT emphasis to alerts and dialogs warning about blocking browser events
- System Reminder: Plan mode is active - clarified that plan approval questions (e.g., "Is this plan okay?", "Should I proceed?") must use ExitPlanMode tool, not text questions or AskUserQuestion; expanded guidance distinguishing when to use AskUserQuestion (only for requirements/approach clarification) vs ExitPlanMode (for plan approval)
- Tool Description: ExitPlanMode v2 - extracted detailed security and permission scoping guidelines to new `PERMISSION_SCOPING_GUIDELINES` variable; replaced inline scoping instructions with variable reference; updated tool name references from `ASK_USER_QUESTION_TOOL_NAME` to `PERMISSION_SCOPING_GUIDELINES` in "Before Using This Tool" and "Important" sections

# [2.1.6](https://github.com/Piebald-AI/claude-code-system-prompts/commit/4843349)

_+742 tokens_

- **NEW:** System Prompt: Autonomous agent (standalone) - standalone autonomous agent mode prompt without system context prefix
- **NEW:** System Prompt: Autonomous agent (with context) - autonomous agent mode prompt prefixed with main system prompt
- **REMOVED:** Agent Prompt: Bash command explainer - removed in favor of integrated bash command explanation
- Agent Prompt: Status line setup - added pre-calculated `used_percentage` and `remaining_percentage` fields to context_window object; updated examples to use simpler syntax for displaying context usage
- Agent Prompt: Claude guide agent - fixed incorrect variable references in documentation source URLs and tool names throughout approach steps
- Agent Prompt: Session Search Assistant - simplified introduction text
- Tool Description: Bash - refactored variable usage, replacing `BASH_TOOL_NAME` with `RUN_IN_BACKGROUND_NOTE`
- Tool Description: ExitPlanMode v2 - added comprehensive "Requesting Permissions (allowedPrompts)" section with guidelines for requesting prompt-based permissions for bash commands, including security-conscious scoping practices

# [2.1.5](https://github.com/Piebald-AI/claude-code-system-prompts/commit/701b0e2)

_-24 tokens_

- Tool Description: Bash - replaced `GIT_COMMIT_AND_PR_CREATION_INSTRUCTION` variable with `BASH_TOOL_NAME` variable in metadata
- Tool Description: Task - reordered variable declarations, moving `IS_TRUTHY_FN` and `PROCESS_OBJECT` earlier in the list

# [2.1.4](https://github.com/Piebald-AI/claude-code-system-prompts/commit/42537cb)

_-19 tokens_

- Tool Description: Bash - moved `run_in_background` parameter documentation to new `BASH_BACKGROUND_TASK_NOTES_FN` function variable; added `BASH_TOOL_EXTRA_NOTES()` placeholder; fixed misaligned variable references in dedicated tools list (file search, content search, read files, edit files, write files were each referencing the wrong tool name)
- Tool Description: Task - added `IS_TRUTHY_FN` and `PROCESS_OBJECT` variables for conditional rendering; background task instructions now conditionally rendered based on `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` environment variable

# [2.1.3](https://github.com/Piebald-AI/claude-code-system-prompts/commit/3b9438c)

_+1,047 tokens_

- **NEW:** Agent Prompt: Bash command description writer - instructions for generating clear, concise command descriptions in active voice for bash commands
- **NEW:** Agent Prompt: Bash command explainer - instructions for explaining bash commands with reasoning, risk assessment, and risk level classification
- **NEW:** Agent Prompt: Remember skill - system prompt for the /remember skill that reviews session memories and updates CLAUDE.local.md with recurring patterns and learnings
- **REMOVED:** Agent Prompt: Bash command risk classifier - replaced with the new bash command explainer agent
- Tool Description: Bash - updated description field instructions to provide more context for complex commands (piped commands, obscure flags, etc.) while keeping simple commands brief
- Tool Description: Bash (Git commit and PR creation instructions) - added warning to never use `git status -uall` flag as it can cause memory issues on large repos
- Tool Description: Task - updated internal variable references and improved background agent monitoring instructions

# [2.1.2](https://github.com/Piebald-AI/claude-code-system-prompts/commit/25150a99c6a1bc916417476178008dbcfa740aa0)

_-374 tokens_

- **NEW:** Agent Prompt: Bash command risk classifier - classifies shell commands by risk level (LOW/MEDIUM/HIGH) to determine permission requirements
- **REMOVED:** Agent Prompt: Bash output summarization - system prompt for determining whether bash command output should be summarized
- **REMOVED:** Agent Prompt: Plan verification agent - agent prompt for verifying that the main agent correctly executed a plan

#### [2.1.1](https://github.com/Piebald-AI/claude-code-system-prompts/commit/9f507fd)

<sub>_No changes to the system prompts in v2.1.1._</sub>

#### [2.1.0](https://github.com/Piebald-AI/claude-code-system-prompts/commit/0280b7d)

<sub>_No changes to the system prompts in v2.1.0._</sub>

# [2.0.77](https://github.com/Piebald-AI/claude-code-system-prompts/commit/36f34b8)

_-128 tokens_

- **NEW:** Agent Prompt: Task tool (extra notes) - additional notes for Task tool usage (absolute paths, no emojis, no colons before tool calls)
- **NEW:** Agent Prompt: Command execution specialist - agent prompt for command execution focusing on bash commands
- **NEW:** Agent Prompt: Plan verification agent - agent prompt for verifying that the main agent correctly executed a plan
- **NEW:** System Prompt: Chrome browser MCP tools - instructions for loading Chrome browser MCP tools via MCPSearch before use
- **REMOVED:** Data: GitHub Actions workflow for automated code review (beta) - GitHub Actions workflow template for automated Claude Code reviews
- **REMOVED:** Tool Description: Task (async return note) - message returned to the model when a subagent launched successfully
- Agent Prompt: Agent creation architect - updated examples from code-reviewer to test-runner agent
- Agent Prompt: Status line setup - added vim mode information (INSERT/NORMAL) to available session data
- System Prompt: Main system prompt - removed "Looking up your own documentation" section with claude-guide agent instructions; added instruction about not using colons before tool calls; numerous variable reference corrections throughout
- System Reminder: Plan mode is active - added verification section requirement in plan files; clarified that AskUserQuestion is for clarifying requirements, not for plan approval
- Tool Description: AskUserQuestion - added plan mode note clarifying this tool is for clarifying requirements before finalizing plans, not for requesting plan approval
- Tool Description: Bash - updated run_in_background parameter description to clarify notification behavior
- Tool Description: Bash (Git commit and PR creation instructions) - simplified parallel command instructions; removed "You can call multiple tools in a single response" preambles; added GIT_COMMAND_PARALLEL_NOTE variable
- Tool Description: ExitPlanMode v2 - reorganized "Handling Ambiguity in Plans" section into "Before Using This Tool"; added clarification that this tool inherently requests user approval
- Tool Description: Skill - reformatted instructions removing XML wrapper tags; added check for already-loaded skills
- Tool Description: Task - updated background agent output retrieval instructions (now uses output_file with Read/Write tools instead of AgentOutputTool); removed pro-only parallel launch note; updated example agent from code-reviewer to test-runner

#### [2.0.76](https://github.com/Piebald-AI/claude-code-system-prompts/commit/3c9c213)

<sub>_No changes to the system prompts in v2.0.76._</sub>

# [2.0.75](https://github.com/Piebald-AI/claude-code-system-prompts/commit/d290cd4)

_-183 tokens_

- **REMOVED:** Agent Prompt: Task tool (extra notes) - additional notes for Task tool usage (absolute paths, no emojis, no colons before tool calls)
- Main system prompt - removed instruction about not using colons before tool calls

# [2.0.74](https://github.com/Piebald-AI/claude-code-system-prompts/commit/33fc177)

_-1693 tokens_

- **NEW:** Agent Prompt: Session Search Assistant - agent prompt for finding relevant sessions based on user queries, with priority matching on tags, titles, branches, summaries, and transcripts
- **REMOVED:** Agent Prompt: Exit plan mode with swarm - instructions for launching swarm teammates when ExitPlanMode is called with `isSwarm` set to true
- **REMOVED:** System Reminder: Delegate mode prompt - system reminder for delegate mode with restricted tool access
- **REMOVED:** System Reminder: Team Coordination - system reminder for team coordination with teammate identity and resources
- **REMOVED:** Tool Description: TaskList - tool for listing all tasks in the task list
- **REMOVED:** Tool Description: TaskUpdate - tool for updating task status and adding comments
- **REMOVED:** Tool Description: TeammateTool's operation parameter - description of TeammateTool operations
- Tool Description: Bash (Git commit and PR creation instructions) - simplified pre-commit hook failure handling; removed detailed amend rules for auto-modified files, now just advises to fix and create a new commit

# [2.0.73](https://github.com/Piebald-AI/claude-code-system-prompts/commit/085fb45)

_+91 tokens_

- **NEW:** Agent Prompt: Prompt Suggestion Generator v2 - V2 instructions for generating prompt suggestions, focusing on predicting what the user would naturally type next
- **REMOVED:** Tool Description: SlashCommand - functionality merged into Skill tool
- Tool Description: Skill - added guidance for invoking skills via slash command syntax (e.g., "/commit"), added `args` parameter for passing arguments to skills
- Tool Description: LSP - added call hierarchy operations (`prepareCallHierarchy`, `incomingCalls`, `outgoingCalls`)
- Tool Description: TeammateTool's operation parameter - added team discovery and join operations (`discoverTeams`, `requestJoin`, `approveJoin`, `rejectJoin`)
- Main system prompt - terminology update: "slash commands" → "skills"; removed duplicate "complete tasks fully" instruction
- Agent Prompt: Claude guide agent - terminology update: "slash commands" → "skills"

# [2.0.72](https://github.com/Piebald-AI/claude-code-system-prompts/commit/f415c3a)

_+47 tokens_

- Tool Description: Task - Added usage note requiring a short description (3-5 words) summarizing what the agent will do
- Tool Description: TaskUpdate - Added "Staleness" section with instruction to read task's latest state using `TaskGet` before updating

# [2.0.71](https://github.com/Piebald-AI/claude-code-system-prompts/commit/1be49c8)

_+948 tokens_

- **NEW:** System Prompt: Claude in Chrome browser automation - instructions for using Claude in Chrome browser automation tools effectively
- **NEW:** Tool Description: Computer - main description for the Chrome browser computer automation tool
- **NEW:** Tool Description: Computer action parameter - description for the computer action parameter used with the Computer tool
- Tool Description: Bash (Git commit and PR creation instructions) - expanded amend safety rules with explicit conditions: (1) user requested OR hook auto-modified files, (2) HEAD was created by you, (3) not yet pushed; added critical warnings for rejected hooks and already-pushed commits; clarified hook failure vs auto-modification handling
- **REMOVED:** Agent Prompt: Prompt suggestion generator
- **REMOVED:** System Reminder: MCP CLI large output

# [2.0.70](https://github.com/Piebald-AI/claude-code-system-prompts/commit/d1f3263)

_+2283 tokens_

- **NEW:** Agent Prompt: /review-pr slash command - system prompt for reviewing GitHub PRs with code analysis
- **NEW:** Agent Prompt: Task tool (extra notes) - additional notes for Task tool usage (absolute paths, no emojis, no colons before tool calls)
- **NEW:** System Reminder: Delegate mode prompt - system reminder for delegate mode with restricted tool access
- **NEW:** Tool Description: MCPSearch - tool for searching/selecting MCP tools before use (mandatory prerequisite)
- **NEW:** Tool Description: MCPSearch (with available tools) - MCPSearch variant that lists available MCP tools
- **NEW:** Tool Description: TaskList - tool for listing all tasks in the task list
- **NEW:** Tool Description: TeammateTool's operation parameter - description of TeammateTool operations (spawn, assignTask, claimTask, shutdown, etc.)
- Agent Prompt: Status line setup - Added `current_usage` object to context_window schema with `input_tokens`, `output_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens` fields; added example for calculating context window percentage
- Tool Description: TaskUpdate - Added instruction to call TaskList after resolving a task; added note about teammates adding comments while working

#### [2.0.69](https://github.com/Piebald-AI/claude-code-system-prompts/commit/b1a1784488f3f3bccdbe5bc6449c0ba6a34e4b39)

<sub>_No changes to the system prompts in v2.0.69._</sub>

# [2.0.68](https://github.com/Piebald-AI/claude-code-system-prompts/commit/56e7a6a14afc956118ad8458b23aaa073d97416b)

_-191 tokens_

- Main system prompt: Added instruction to not use colons before tool calls ("Let me read the file." instead of "Let me read the file:")
- **REMOVED:** Agent Prompt: /review-pr slash command

#### [2.0.67](https://github.com/Piebald-AI/claude-code-system-prompts/commit/11cb562530596ac533e8ca1c0b8e59c56d59e68a)

<sub>_No changes to the system prompts in v2.0.67._</sub>

# [2.0.66](https://github.com/Piebald-AI/claude-code-system-prompts/commit/fa26cb89380bbb0f83117a14015104defa41861e)

_+172 tokens_

- **NEW:** System Prompt: Scratchpad directory - instructions for using a dedicated session-specific scratchpad directory for temporary files instead of `/tmp`

# [2.0.65](https://github.com/Piebald-AI/claude-code-system-prompts/commit/c527901340dda30950eb667af9d7a31d7dcb30ee)

_+97 tokens_

- Agent Prompt: Status line setup - Added `context_window` object to status line data schema with `total_input_tokens`, `total_output_tokens`, and `context_window_size` fields
- `LSP` tool: Added `goToImplementation` operation; changed line/character documentation from 0-indexed to 1-based

#### [2.0.64](https://github.com/Piebald-AI/claude-code-system-prompts/commit/824243c6fb80fefb4f3ed1d5f6c489df908e0663)

<sub>_No changes to the system prompts in v2.0.64._</sub>

# [2.0.63](https://github.com/Piebald-AI/claude-code-system-prompts/commit/f3953ffe61eef3dbf6cdb232041f4b39bd2f4a7b)

_+10 tokens_

- Main system prompt: Added `BUILD_TIME` to config variables interpolation

# [2.0.62](https://github.com/Piebald-AI/claude-code-system-prompts/commit/69bdc5ab93ccf071b44eb4aac29507ccd64d0b25)

_+381 tokens_

- **NEW:** `AskUserQuestion` tool description - includes guidance on recommending options by adding "(Recommended)" to labels
- Main system prompt: Added instruction to complete tasks fully without stopping mid-task or claiming context limits prevent completion
- `EnterPlanMode` tool: Major rewrite encouraging proactive use for non-trivial tasks; expanded "when to use" examples including new features and code modifications; shifted guidance from "err on implementation" to "err on planning"
- `Skill` tool: Added blocking requirement to invoke skill tool immediately as first action when relevant, before generating any other response
- `Task` tool: Added `resume` parameter documentation for continuing agents with preserved context; clarified agent ID return for follow-up work
- `WebFetch` tool: Simplified MCP tool preference note (removed "All MCP-provided tools start with mcp__")

#### [2.0.61](https://github.com/Piebald-AI/claude-code-system-prompts/commit/09e9a9f1961da38ce3b9d6f771f071e43b4746ea)

<sub>_No changes to the system prompts in v2.0.61._</sub>

# [2.0.60](https://github.com/Piebald-AI/claude-code-system-prompts/commit/7b38ff38e8fc1b6f4e1a88b3d41f0a6d4e70f7c8)

_+1339 tokens_

- **NEW:** System Reminder: Team Coordination - instructions for team-based multi-agent workflows with team config, task list paths, and teammate messaging
- **NEW:** Agent Prompt: Exit plan mode with swarm - instructions for launching worker swarms when `ExitPlanMode` is called with `isSwarm` enabled
- Agent Prompt: Claude Code guide agent → **renamed** to Claude guide agent with expanded scope covering Claude Code, Claude Agent SDK, and Claude API (formerly Anthropic API)
- `Task` tool: Added `run_in_background` parameter documentation and `TaskOutput` tool usage for retrieving background agent results
- `TaskUpdate` tool: Major expansion with task ownership requirements, team coordination, claiming tasks, and detailed field documentation
- `WebFetch` tool: Added conditional instructions based on trusted domain status (simpler instructions for trusted domains)
- **REMOVED:** System Prompt: whenToUse note for claude-code-guide subagent (functionality merged into updated guide agent)

# [2.0.59](https://github.com/Piebald-AI/claude-code-system-prompts/commit/f01489b6be5c888d3e53a02609710628a29c9a0b)

_+140 tokens_

- **NEW:** Added new `TaskUpdate` tool which allows Claude to update the task list.

# [2.0.58](https://github.com/Piebald-AI/claude-code-system-prompts/commit/d1437449dddae84e888f4751e18add2e6153e135)

_+21 tokens_

- Session notes template: Added new "Current State" section for tracking active work and pending tasks
- Session notes template: Renamed "User Corrections / Mistakes" to "Errors & Corrections" with expanded description
- Session notes instructions: Added emphasis on updating "Current State" for continuity after compaction
- Session notes instructions: Removed instruction about not repeating past session summaries
- Session notes instructions: Fixed markdown header reference (`'##'` → `'#'`)
- Documentation URL: Changed from `docs.claude.com/s/claude-code` to `code.claude.com/docs/en/overview`
- GitHub Action templates: Updated CLI reference URL to `code.claude.com/docs/en/cli-reference`

#### [2.0.57](https://github.com/Piebald-AI/claude-code-system-prompts/commit/8b2ecb38493daf677fcba54746d2c3e40de6f657)

<sub>_No changes to the system prompts in v2.0.57._</sub>

# [2.0.56](https://github.com/Piebald-AI/claude-code-system-prompts/commit/47571b6ad6110bebc89553bba49ebcf94f4605fc)

_-134 tokens_

- Reinforced note about using the current year in the WebSearch tool description
- Added a note to the main system prompt instructing Claude to never include time estimates when presenting options or plans.
- Strengthened and elaborated "plan mode is active" system reminder
- Encouraged the Explore subagent to be more tool-call-efficient and token-efficient
- Added an instruction to _"Read any files provided to you in the initial prompt"_ to the Plan subagent
- Changed the theme of the prompt suggestion generator's prompt from _"predict what the user will type next"_ to _"suggest what Claude could help with"_
- Stopped directing the user to open a GH an on the Claude Code repo via `/feedback` when the `claude-code-guide` subagent is at a loss
- Removed the old plan mode's system reminder

# [2.0.55](https://github.com/Piebald-AI/claude-code-system-prompts/commit/5c2f24217280a6c0a0b0ae5f80ba7f195e874ed0)

_+121 tokens_

- **NEW:** Added **Agent Prompt: Suggested Prompt Generator** for suggesting a followup propmt after Claude response.  Requires [tweakcc](https://github.com/Piebald-AI/tweakcc) to enable the functionality in Claude Code: run `npx tweakcc@latest --apply` and then `claude` and then send a message.
- Modified interpolated formatting code in mcp-cli prompt

# [2.0.54](https://github.com/Piebald-AI/claude-code-system-prompts/commit/3bd3a890d18146df0f3699d276133fe92d68e4b5)

_+128 tokens_

- Multi-Agent Planning Note: Added a note discouraging overuse of multiple plan agents: _If the task is simple, you should try to use the minimum number of agents necessary (usually just 1)_
- Added a similar longer note to the "Plan mode is active" system reminder

#### [2.0.53](https://github.com/Piebald-AI/claude-code-system-prompts/commit/9e92d4f32a00e248ad0883ae432658caa2eb298b)

<sub>_No changes to the system prompts in v2.0.53._</sub>

# [2.0.52](https://github.com/Piebald-AI/claude-code-system-prompts/commit/74f41c979c84103343d0d92f086678911e0b7d36)

_+42 tokens_

- Add a 4th note to the procedure steps in the Plan Mode Re-entry System Prompt: _"Continue on with the plan process and most importantly you should always edit the plan file one way or the other before calling ExitPlanMode._"

# [2.0.51](https://github.com/Piebald-AI/claude-code-system-prompts/commit/fea594c92014ec7c6133e771afc1a55a034a15ee)

_+906 tokens_

- **NEW:** Prompt for the new `EnterPlanMode` tool.
- **NEW:** Prompt for agent hooks.

# [2.0.50](https://github.com/Piebald-AI/claude-code-system-prompts/commit/f19b049975ac24bf548b6c95dfe6a385c6bdf4a9)

_+465 tokens_

- **NEW:** System reminder sent when an `mcp-cli read` or `mcp-cli call` output is longer than the `MAX_MCP_OUTPUT_TOKENS` environment variable (defaults to `25000`)
- `WebSearch` tool description: Added a "CRITICAL REQUIREMENT" to include a "Sources:" section whenever performing a web search.
- Session notes template: Added a "Key results" section including "specific outputs" such as "an answer to question, a table, or other document."

# [2.0.49](https://github.com/Piebald-AI/claude-code-system-prompts/commit/ec960fe987da2dfdb026f733fcd30120ac1a116e)

- **Explore & Plan agents:**
  - Enhanced READ-ONLY restrictions with explicit bulleted list of prohibited operations
  - Added note that file editing tools are not available
  - Reformatted Bash tool restrictions for clarity

#### **2.0.48** &ndash; _This version does not exist._

# [2.0.47](https://github.com/Piebald-AI/claude-code-system-prompts/commit/62075a9489f7edb416970b9e67605c288ce562ac)

- **NEW:** Agent prompt: Multi-Agent Planning Note - instructions for multi-agent planning when `CLAUDE_CODE_PLAN_V2_AGENT_COUNT` > 1
- **NEW:** System reminder: Plan mode re-entry - sent when user re-enters Plan mode after exiting
- Main system prompt: Added "NEVER propose changes to code you haven't read" instruction
- Main system prompt: Added comprehensive "Avoid over-engineering" section with guidelines on simplicity
- Enhanced plan mode reminder: Refactored variable names and simplified structure
- Enhanced plan mode reminder: Fixed typo "Syntehsize" → "Synthesize", "alwasy" → "always"

#### [2.0.46](https://github.com/Piebald-AI/claude-code-system-prompts/commit/3f9c346)

<sub>_No changes to the system prompts in v2.0.46._</sub>

# [2.0.45](https://github.com/Piebald-AI/claude-code-system-prompts/commit/9ed4378)

- **NEW:** Agent prompt: Claude Code guide agent for helping users with Claude Code and Agent SDK
- **NEW:** Agent prompt: Session title and branch generation (replaces session title generation)
- **NEW:** System prompt: whenToUse note for claude-code-guide subagent
- Main system prompt: Updated to use `Task` tool with claude-code-guide subagent instead of `WebFetch` for documentation lookup
- Enhanced plan mode reminder: Added parallel exploration support with `PLAN_V2_EXPLORE_AGENT_COUNT`
- **REMOVED:** Agent prompt: Session title generation (replaced by session title and branch generation)

#### [2.0.44](https://github.com/Piebald-AI/claude-code-system-prompts/commit/1841396)

<sub>_No changes to the system prompts in v2.0.44._</sub>

# [2.0.43](https://github.com/Piebald-AI/claude-code-system-prompts/commit/36fded1)

- **NEW:** Tool description: `ExitPlanMode` v2
- **NEW:** System reminder: Plan mode is active (for subagents)
- Main system prompt: Added "Planning without timelines" section
- Main system prompt: Added instruction to avoid backwards-compatibility hacks
- Enhanced plan mode reminder: Major restructuring with plan file support and variable updates

#### [2.0.42](https://github.com/Piebald-AI/claude-code-system-prompts/commit/ec54e36)

<sub>_No changes to the system prompts in v2.0.42._</sub>

# [2.0.41](https://github.com/Piebald-AI/claude-code-system-prompts/commit/0540858)

- **NEW:** Agent prompt: Plan mode (enhanced)
- **NEW:** System reminder: Plan mode is active (enhanced)
- Explore agent: Strengthened READ-ONLY restrictions with explicit forbidden commands
- Prompt Hook execution: Fixed JSON format (added quotes around keys)
- Main system prompt: Added `FEEDBACK_CHANNEL` variable

#### **2.0.40** &ndash; _This version does not exist._

#### **2.0.39** &ndash; _This version does not exist._

#### **2.0.38** &ndash; _This version does not exist._

# [2.0.37](https://github.com/Piebald-AI/claude-code-system-prompts/commit/a6eb810)

- **NEW:** Agent prompt: Prompt Hook execution
- Main system prompt: Changed `isCodingRelated` to `keepCodingInstructions`

# [2.0.36](https://github.com/Piebald-AI/claude-code-system-prompts/commit/5fd0f76)

- MCP CLI: Added `mcp-cli read` command for reading resources
- Main system prompt: Removed empty bullet point in "Doing tasks" section
- `Skill` tool: Updated examples to use `skill:` instead of `command:`
- `SlashCommand` tool: Removed "Intent Matching" section, simplified formatting

#### [2.0.35](https://github.com/Piebald-AI/claude-code-system-prompts/commit/f07e330)

<sub>_No changes to the system prompts in v2.0.35._</sub>

# [2.0.34](https://github.com/Piebald-AI/claude-code-system-prompts/commit/66c833d)

- **NEW:** System prompt: MCP CLI instructions
- Main system prompt: Added "Asking questions as you work" section with `ASKUSERQUESTION_TOOL_NAME`
- `Task` tool: Added note about agents with "access to current context"
- Bash sandbox note: Added `CONDITIONAL_NEWLINE_IF_SANDBOX_ENABLED` variable

# [2.0.33](https://github.com/Piebald-AI/claude-code-system-prompts/commit/d5f6b72)

- Main system prompt: Removed extra blank lines

#### [2.0.32](https://github.com/Piebald-AI/claude-code-system-prompts/commit/8e7638b)

<sub>_No changes to the system prompts in v2.0.32._</sub>

#### [2.0.31](https://github.com/Piebald-AI/claude-code-system-prompts/commit/61f41c8)

<sub>_No changes to the system prompts in v2.0.31._</sub>

# [2.0.30](https://github.com/Piebald-AI/claude-code-system-prompts/commit/2c67463)

- **NEW:** Agent prompt: Update Magic Docs
- **NEW:** Tool description: `LSP`
- Main system prompt: Added security warning for OWASP top 10 vulnerabilities
- Plan mode reminder: Clarified `AskUserQuestion` tool usage
- `ExitPlanMode` tool: Added "Handling Ambiguity in Plans" section with example
- Bash sandbox note: Removed `RESTRICTIONS_LIST` and temp file instructions
- **REMOVED:** Agent prompt: Output style creation

# [2.0.29](https://github.com/Piebald-AI/claude-code-system-prompts/commit/772bca0)

- `Task` tool: Re-added `runsInBackground` property and `AgentOutputTool` usage note

# [2.0.28](https://github.com/Piebald-AI/claude-code-system-prompts/commit/91098d5)

- Main system prompt: Added "Avoid using over-the-top validation or excessive praise" guidance
- Plan mode reminder: Added `NOTE_ABOUT_USING_PLAN_SUBAGENT` variable
- `Task` tool: Removed `runsInBackground` property and background agent instructions

#### [2.0.27](https://github.com/Piebald-AI/claude-code-system-prompts/commit/88b0741)

<sub>_No changes to the system prompts in v2.0.27._</sub>

# [2.0.26](https://github.com/Piebald-AI/claude-code-system-prompts/commit/7a800b2)

- Bash sandbox note: Renamed `dangerouslyOverrideSandbox` to `dangerouslyDisableSandbox`

# [2.0.25](https://github.com/Piebald-AI/claude-code-system-prompts/commit/a0566f0)

- Session notes template: Added "Session Title" section
- Session notes update instructions: Enhanced with multi-edit support and clearer structure preservation rules
- `Bash` tool: Removed note about not using `run_in_background` with 'sleep'

# [2.0.24](https://github.com/Piebald-AI/claude-code-system-prompts/commit/bf4bfa4)

- **NEW:** Tool description: Bash (sandbox note)

#### **2.0.23** &ndash; _This version does not exist._

#### [2.0.22](https://github.com/Piebald-AI/claude-code-system-prompts/commit/f6910aa)

<sub>_No changes to the system prompts in v2.0.22._</sub>

# [2.0.21](https://github.com/Piebald-AI/claude-code-system-prompts/commit/01354e8)

- Plan mode reminder: Added `NOTE_ABOUT_AskUserQuestion` variable
- `ExitPlanMode` tool: Added `NOTE_ABOUT_AskUserQuestion` variables

# [2.0.20](https://github.com/Piebald-AI/claude-code-system-prompts/commit/9319b91)

- **NEW:** Tool description: `Skill`

#### [2.0.19](https://github.com/Piebald-AI/claude-code-system-prompts/commit/82803b4)

<sub>_No changes to the system prompts in v2.0.19._</sub>

# [2.0.18](https://github.com/Piebald-AI/claude-code-system-prompts/commit/327b3dc)

- Explore agent: Changed "Be thorough" guideline to "Adapt your search approach based on the thoroughness level specified by the caller"

# [2.0.17](https://github.com/Piebald-AI/claude-code-system-prompts/commit/8c27c21)

- Main system prompt: Added critical instruction to use `Task` tool with Explore subagent for codebase exploration
- Main system prompt: Added examples for when to use Explore agent vs direct search
- Main system prompt: Added new variables (`EXPLORE_AGENT`, `GLOB_TOOL_NAME`, `GREP_TOOL_NAME`)

#### **2.0.16** &ndash; _This version does not exist._

# [2.0.15](https://github.com/Piebald-AI/claude-code-system-prompts/commit/ed40efa)

- Updated `ExitPlanMode` tool description formatting (added "Examples" header)
- Minor punctuation fix in plan mode reminder

# [2.0.14](https://github.com/Piebald-AI/claude-code-system-prompts/commit/8b3c574)

Initial comprehensive system prompts collection.

**Agent Prompts:**
- Agent creation architect
- Bash command file path extraction
- Bash command prefix detection
- Bash output summarization
- Claude.md creation
- Conversation summarization (with additional instructions variant)
- Explore agent
- Output style creation
- PR comments slash command
- Review PR slash command
- Security review slash command
- Session notes template and update instructions
- Session title generation
- Status line setup
- Task tool agent
- User sentiment analysis
- WebFetch summarizer

**GitHub Integration:**
- GitHub Actions workflow for @claude mentions
- GitHub Actions workflow for automated code review (beta)
- GitHub App installation PR description

**System Prompts:**
- Main system prompt
- Learning mode and learning mode insights
- Plan mode is active reminder

**Tool Descriptions:**
- Bash (with git commit and PR creation instructions)
- Edit
- ExitPlanMode
- Glob
- Grep
- NotebookEdit
- Read file
- SlashCommand
- Task (with async return note)
- TodoWrite
- WebFetch
- WebSearch
- Write
