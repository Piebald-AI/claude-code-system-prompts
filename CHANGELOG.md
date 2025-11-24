<!--
Note: Only use **NEW:** for entirely new prompt files, NOT for new additions/sections within existing prompts.
-->

### Claude Code System Prompts Changelog

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
