<!--
Note: Only use **NEW:** for entirely new prompt files, NOT for new additions/sections within existing prompts.
-->

### Claude Code System Prompts Changelog

#### [2.1.49](https://github.com/Piebald-AI/claude-code-system-prompts/commit/8da43fb)

<sub>_No changes to the system prompts in v2.1.49._</sub>

#### [2.1.48](https://github.com/Piebald-AI/claude-code-system-prompts/commit/0d57836)

_-1,082 tokens_

- **NEW:** Tool Description: EnterWorktree - Tool description for the EnterWorktree tool (237 tks).
- **REMOVED:** System Prompt: MCP CLI - Removed instructions for using mcp-cli to interact with Model Context Protocol servers (1333 tks).
- Tool Description: Task - Simplified background agent output-file guidance; removed `BASH_TOOL` variable and `tail` instructions; added new "Foreground vs background" bullet explaining when to use each mode (1214 → 1228 tks).

#### [2.1.47](https://github.com/Piebald-AI/claude-code-system-prompts/commit/f58cba9)

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

#### [2.1.45](https://github.com/Piebald-AI/claude-code-system-prompts/commit/36d2856)

_+276 tokens_

- **NEW:** Agent Prompt: Single-word search term extractor - System prompt for extracting single-word search terms from a user's query (361 tks).
- **NEW:** System Prompt: Option previewer - System prompt for previewing UI options in a side-by-side layout (129 tks).
- **REMOVED:** Agent Prompt: Prompt Suggestion Generator (Stated Intent) - Removed the stated-intent prompt suggestion generator that returned a user's explicitly stated next step (166 tks).
- Agent Prompt: /review-pr slash command - Replaced `${BASH_TOOL_OBJECT.name}(...)` template expressions with plain backtick-quoted `gh` commands; removed `BASH_TOOL_OBJECT` variable (243 → 211 tks).
- Tool Description: Bash (sandbox note) - Removed `CONDITIONAL_NEWLINE_IF_SANDBOX_ENABLED` variable; the conditional newline before the "Set dangerouslyDisableSandbox" bullet is now always included (454 → 438 tks).

#### [2.1.44](https://github.com/Piebald-AI/claude-code-system-prompts/commit/eb6a818)

<sub>_No changes to the system prompts in v2.1.44._</sub>

#### [2.1.42](https://github.com/Piebald-AI/claude-code-system-prompts/commit/8a1123a)

_-1,060 tokens_

- **REMOVED:** Agent Prompt: Remember skill - Removed the `/remember` skill prompt that reviewed session memories and updated CLAUDE.local.md with recurring patterns and learnings (1048 tks).
- Tool Description: WebSearch - Simplified date-awareness variables; replaced `GET_CURRENT_DATE_FN` and `CURRENT_YEAR` with a single `CURRENT_MONTH_YEAR` variable; updated example to use plain text ("with the current year, NOT last year") instead of template expressions (331 → 319 tks).

#### [2.1.41](https://github.com/Piebald-AI/claude-code-system-prompts/commit/91732e4)

_+262 tokens_

- **NEW:** System Prompt: Conditional delegate codebase exploration - Added instructions for when to use the Explore subagent versus calling tools directly (249 tks).
- System Prompt: Tool usage policy - Replaced inline "VERY IMPORTANT" block and examples about delegating codebase exploration to the Explore agent with a conditional variable reference; removed `GLOB_TOOL_NAME` and `GREP_TOOL_NAME` variables (564 → 352 tks).
- System Prompt: Skillify Current Session - Added Round 2 prompt to ask the user where to save the skill (repo-specific vs personal); updated Step 3 to use the user-chosen location instead of hardcoded `.claude/skills/`; changed Step 4 to output the SKILL.md as a YAML code block for review and use a simpler AskUserQuestion confirmation (1750 → 1882 tks).
- System Reminder: Plan mode is active (5-phase) - Made Explore subagent usage conditional; when disabled, Phase 1 now instructs Claude to use Glob, Grep, and Read tools directly; updated Phase 2 variable references for plan subagent and agent count (1429 → 1500 tks).
- Agent Prompt: Status line setup - Added `session_name` field (optional human-readable session name set via `/rename`) to the JSON input spec (1460 → 1482 tks).

#### [2.1.40](https://github.com/Piebald-AI/claude-code-system-prompts/commit/06ce2b9)

_-293 tokens_

- **REMOVED:** Agent Prompt: Evolve currently-running skill - Removed agent prompt for evolving a currently-running skill based on user requests or preferences (293 tks).

#### [2.1.39](https://github.com/Piebald-AI/claude-code-system-prompts/commit/11e9ec6)

_+293 tokens_

- **NEW:** Agent Prompt: Evolve currently-running skill - Added new agent prompt for evolving a currently-running skill based on what the user is implicitly or explicitly requesting (293 tks).

#### [2.1.38](https://github.com/Piebald-AI/claude-code-system-prompts/commit/30adcee)

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
