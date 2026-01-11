<!--
Note: Only use **NEW:** for entirely new prompt files, NOT for new additions/sections within existing prompts.
-->

### Claude Code System Prompts Changelog

# [2.1.4](https://github.com/Piebald-AI/claude-code-system-prompts/commit/42537cb)

_-19 tokens_

- Tool Description: Bash - moved `run_in_background` parameter documentation to new `BASH_BACKGROUND_TASK_NOTES_FN` function variable; added `BASH_TOOL_EXTRA_NOTES()` placeholder; fixed misaligned variable references in dedicated tools list (file search, content search, read files, edit files, write files were each referencing the wrong tool name); corrected parallel command instruction references from `WRITE_TOOL_NAME` to `GIT_COMMIT_AND_PR_CREATION_INSTRUCTION`
- Tool Description: Task - added `IS_TRUTHY_FN` and `PROCESS_OBJECT` variables; background task instructions now conditionally rendered based on `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` environment variable; updated example variable references from `TASK_TOOL_OBJECT.name` to `IS_TRUTHY_FN.name` and from `WRITE_TOOL` to `PROCESS_OBJECT`

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
