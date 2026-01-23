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

This repository contains an up-to-date list of all Claude Code's various system prompts and their associated token counts as of **[Claude Code v2.1.18](https://www.npmjs.com/package/@anthropic-ai/claude-code/v/2.1.18) (January 22nd, 2026).**  It also contains a [**CHANGELOG.md**](./CHANGELOG.md) for the system prompts across 76 versions since v2.0.14.  From the team behind [<img src="https://github.com/Piebald-AI/piebald/raw/main/assets/logo.svg" width="15"> **Piebald.**](https://piebald.ai/)

**This repository is updated within minutes of each Claude Code release.  See the [CHANGELOG](./CHANGELOG.md), and follow [@PiebaldAI](https://x.com/PiebaldAI) on X for a summary of the system prompt changes in each release.**

---

Why multiple "system prompts?"

**Claude Code doesn't just have one single string for its system prompt.**

Instead, there are:
- Large portions conditionally added depending on the environment and various configs.
- Descriptions for builtin tools like `Write`, `Bash`, and `TodoWrite`, and some are fairly large.
- Separate system prompts for builtin agents like Explore and Plan.
- Numerous AI-powered utility functions, such as conversation compaction, `CLAUDE.md` generation, session title generation, etc. featuring their own systems prompts.

The result&mdash;40+ strings that are constantly changing and moving within a very large minified JS file.

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

- [Agent Prompt: Explore](./system-prompts/agent-prompt-explore.md) (**516** tks) - System prompt for the Explore subagent.
- [Agent Prompt: Plan mode (enhanced)](./system-prompts/agent-prompt-plan-mode-enhanced.md) (**633** tks) - Enhanced prompt for the Plan subagent.
- [Agent Prompt: Task tool (extra notes)](./system-prompts/agent-prompt-task-tool-extra-notes.md) (**129** tks) - Additional notes for Task tool usage (absolute paths, no emojis, no colons before tool calls).
- [Agent Prompt: Task tool](./system-prompts/agent-prompt-task-tool.md) (**294** tks) - System prompt given to the subagent spawned via the Task tool.

### Creation Assistants

- [Agent Prompt: Agent creation architect](./system-prompts/agent-prompt-agent-creation-architect.md) (**1110** tks) - System prompt for creating custom AI agents with detailed specifications.
- [Agent Prompt: CLAUDE.md creation](./system-prompts/agent-prompt-claudemd-creation.md) (**384** tks) - System prompt for analyzing codebases and creating CLAUDE.md documentation files.
- [Agent Prompt: Status line setup](./system-prompts/agent-prompt-status-line-setup.md) (**1394** tks) - System prompt for the statusline-setup agent that configures status line display.

### Slash commands

- [Agent Prompt: /pr-comments slash command](./system-prompts/agent-prompt-pr-comments-slash-command.md) (**402** tks) - System prompt for fetching and displaying GitHub PR comments.
- [Agent Prompt: /review-pr slash command](./system-prompts/agent-prompt-review-pr-slash-command.md) (**243** tks) - System prompt for reviewing GitHub pull requests with code analysis.
- [Agent Prompt: /security-review slash command](./system-prompts/agent-prompt-security-review-slash-command.md) (**2610** tks) - Comprehensive security review prompt for analyzing code changes with focus on exploitable vulnerabilities.

### Utilities

- [Agent Prompt: Agent Hook](./system-prompts/agent-prompt-agent-hook.md) (**133** tks) - Prompt for an 'agent hook'.
- [Agent Prompt: Bash command description writer](./system-prompts/agent-prompt-bash-command-description-writer.md) (**207** tks) - Instructions for generating clear, concise command descriptions in active voice for bash commands.
- [Agent Prompt: Bash command file path extraction](./system-prompts/agent-prompt-bash-command-file-path-extraction.md) (**286** tks) - System prompt for extracting file paths from bash command output.
- [Agent Prompt: Bash command prefix detection](./system-prompts/agent-prompt-bash-command-prefix-detection.md) (**835** tks) - System prompt for detecting command prefixes and command injection.
- [Agent Prompt: Claude guide agent](./system-prompts/agent-prompt-claude-guide-agent.md) (**761** tks) - System prompt for the claude-guide agent that helps users understand and use Claude Code, the Claude Agent SDK and the Claude API effectively..
- [Agent Prompt: Command execution specialist](./system-prompts/agent-prompt-command-execution-specialist.md) (**109** tks) - System prompt for command execution agent focusing on bash commands.
- [Agent Prompt: Conversation summarization with additional instructions](./system-prompts/agent-prompt-conversation-summarization-with-additional-instructions.md) (**1133** tks) - Extended summarization prompt with support for custom additional instructions.
- [Agent Prompt: Conversation summarization](./system-prompts/agent-prompt-conversation-summarization.md) (**1121** tks) - System prompt for creating detailed conversation summaries.
- [Agent Prompt: Exit plan mode with swarm](./system-prompts/agent-prompt-exit-plan-mode-with-swarm.md) (**440** tks) - System reminder for when ExitPlanMode is called with `isSwarm` set to true..
- [Agent Prompt: Prompt Hook execution](./system-prompts/agent-prompt-prompt-hook-execution.md) (**134** tks) - Prompt given to Claude when acting evaluating whether to pass or fail a prompt hook..
- [Agent Prompt: Prompt Suggestion Generator (Stated Intent)](./system-prompts/agent-prompt-prompt-suggestion-generator-stated-intent.md) (**166** tks) - Instructions for generating prompt suggestions based on user's explicitly stated next steps.
- [Agent Prompt: Prompt Suggestion Generator v2](./system-prompts/agent-prompt-prompt-suggestion-generator-v2.md) (**296** tks) - V2 instructions for generating prompt suggestions for Claude Code.
- [Agent Prompt: Remember skill](./system-prompts/agent-prompt-remember-skill.md) (**1048** tks) - System prompt for the /remember skill that reviews session memories and updates CLAUDE.local.md with recurring patterns and learnings.
- [Agent Prompt: Session Search Assistant](./system-prompts/agent-prompt-session-search-assistant.md) (**439** tks) - Agent prompt for the session search assistant that finds relevant sessions based on user queries and metadata.
- [Agent Prompt: Session notes template](./system-prompts/agent-prompt-session-notes-template.md) (**292** tks) - Template structure for session notes tracking coding work and decisions.
- [Agent Prompt: Session notes update instructions](./system-prompts/agent-prompt-session-notes-update-instructions.md) (**756** tks) - Instructions for updating session notes files during conversations.
- [Agent Prompt: Session title and branch generation](./system-prompts/agent-prompt-session-title-and-branch-generation.md) (**355** tks) - System prompt for generating succinct titles and git branch names for coding sessions.
- [Agent Prompt: Update Magic Docs](./system-prompts/agent-prompt-update-magic-docs.md) (**718** tks) - Prompt for the magic-docs agent..
- [Agent Prompt: User sentiment analysis](./system-prompts/agent-prompt-user-sentiment-analysis.md) (**205** tks) - System prompt for analyzing user frustration and PR creation requests.
- [Agent Prompt: WebFetch summarizer](./system-prompts/agent-prompt-webfetch-summarizer.md) (**185** tks) - Prompt for agent that summarizes verbose output from WebFetch for the main model.

<!--
### Data

Misc large strings.

- [Data: GitHub Actions workflow for @claude mentions](./system-prompts/data-github-actions-workflow-for-claude-mentions.md) (**527** tks) - GitHub Actions workflow template for triggering Claude Code via @claude mentions.
- [Data: GitHub App installation PR description](./system-prompts/data-github-app-installation-pr-description.md) (**424** tks) - Template for PR description when installing Claude Code GitHub App integration.
-->

### System Prompt

Parts of the main system prompt.

- [**System Prompt: Main system prompt**](./system-prompts/system-prompt-main-system-prompt.md) (**2896** tks) - Core system prompt for Claude Code defining behavior, tone, and tool usage policies.
- [System Prompt: Censoring assistance with malicious activities](./system-prompts/system-prompt-censoring-assistance-with-malicious-activities.md) (**98** tks) - Guidelines for assisting with authorized security testing, defensive security, CTF challenges, and educational contexts while censoring requests for malicious activities.
- [System Prompt: Chrome browser MCP tools](./system-prompts/system-prompt-chrome-browser-mcp-tools.md) (**158** tks) - Instructions for loading Chrome browser MCP tools via MCPSearch before use.
- [System Prompt: Claude in Chrome browser automation](./system-prompts/system-prompt-claude-in-chrome-browser-automation.md) (**761** tks) - Instructions for using Claude in Chrome browser automation tools effectively.
- [System Prompt: Git status](./system-prompts/system-prompt-git-status.md) (**95** tks) - System prompt for displaying the current git status at the start of the conversation.
- [System Prompt: Hooks Configuration](./system-prompts/system-prompt-hooks-configuration.md) (**1268** tks) - System prompt for hooks configuration.  Used for above Claude Code config skill..
- [System Prompt: Learning mode (insights)](./system-prompts/system-prompt-learning-mode-insights.md) (**142** tks) - Instructions for providing educational insights when learning mode is active.
- [System Prompt: Learning mode](./system-prompts/system-prompt-learning-mode.md) (**1042** tks) - Main system prompt for learning mode with human collaboration instructions.
- [System Prompt: MCP CLI](./system-prompts/system-prompt-mcp-cli.md) (**1335** tks) - Instructions for using mcp-cli to interact with Model Context Protocol servers.
- [System Prompt: Scratchpad directory](./system-prompts/system-prompt-scratchpad-directory.md) (**172** tks) - Instructions for using a dedicated scratchpad directory for temporary files.
- [System Prompt: Teammate Communication](./system-prompts/system-prompt-teammate-communication.md) (**138** tks) - System prompt for teammate communication in swarm.
- [System Prompt: Tool execution denied](./system-prompts/system-prompt-tool-execution-denied.md) (**157** tks) - System prompt for when tool execution is denied.

### System Reminders

Text for large system reminders.

- [System Reminder: Agent mention](./system-prompts/system-reminder-agent-mention.md) (**45** tks) - Notification that user wants to invoke an agent.
- [System Reminder: Compact file reference](./system-prompts/system-reminder-compact-file-reference.md) (**57** tks) - Reference to file read before conversation summarization.
- [System Reminder: Delegate mode prompt](./system-prompts/system-reminder-delegate-mode-prompt.md) (**185** tks) - System reminder for delegate mode.
- [System Reminder: Exited delegate mode](./system-prompts/system-reminder-exited-delegate-mode.md) (**50** tks) - Notification when exiting delegate mode in swarm.
- [System Reminder: Exited plan mode](./system-prompts/system-reminder-exited-plan-mode.md) (**73** tks) - Notification when exiting plan mode.
- [System Reminder: File exists but empty](./system-prompts/system-reminder-file-exists-but-empty.md) (**27** tks) - Warning when reading an empty file.
- [System Reminder: File modified by user or linter](./system-prompts/system-reminder-file-modified-by-user-or-linter.md) (**97** tks) - Notification that a file was modified externally.
- [System Reminder: File opened in IDE](./system-prompts/system-reminder-file-opened-in-ide.md) (**37** tks) - Notification that user opened a file in IDE.
- [System Reminder: File shorter than offset](./system-prompts/system-reminder-file-shorter-than-offset.md) (**59** tks) - Warning when file read offset exceeds file length.
- [System Reminder: File truncated](./system-prompts/system-reminder-file-truncated.md) (**74** tks) - Notification that file was truncated due to size.
- [System Reminder: Hook additional context](./system-prompts/system-reminder-hook-additional-context.md) (**35** tks) - Additional context from a hook.
- [System Reminder: Hook blocking error](./system-prompts/system-reminder-hook-blocking-error.md) (**52** tks) - Error from a blocking hook command.
- [System Reminder: Hook stopped continuation](./system-prompts/system-reminder-hook-stopped-continuation.md) (**30** tks) - Message when a hook stops continuation.
- [System Reminder: Hook success](./system-prompts/system-reminder-hook-success.md) (**29** tks) - Success message from a hook.
- [System Reminder: Invoked skills](./system-prompts/system-reminder-invoked-skills.md) (**33** tks) - List of skills invoked in this session.
- [System Reminder: Lines selected in IDE](./system-prompts/system-reminder-lines-selected-in-ide.md) (**66** tks) - Notification about lines selected by user in IDE.
- [System Reminder: MCP resource no content](./system-prompts/system-reminder-mcp-resource-no-content.md) (**41** tks) - Shown when MCP resource has no content.
- [System Reminder: MCP resource no displayable content](./system-prompts/system-reminder-mcp-resource-no-displayable-content.md) (**43** tks) - Shown when MCP resource has no displayable content.
- [System Reminder: Malware analysis after Read tool call](./system-prompts/system-reminder-malware-analysis-after-read-tool-call.md) (**87** tks) - Instructions for analyzing malware without improving or augmenting it.
- [System Reminder: Memory file contents](./system-prompts/system-reminder-memory-file-contents.md) (**38** tks) - Contents of a memory file by path.
- [System Reminder: Nested memory contents](./system-prompts/system-reminder-nested-memory-contents.md) (**33** tks) - Contents of a nested memory file.
- [System Reminder: New diagnostics detected](./system-prompts/system-reminder-new-diagnostics-detected.md) (**35** tks) - Notification about new diagnostic issues.
- [System Reminder: Output style active](./system-prompts/system-reminder-output-style-active.md) (**32** tks) - Notification that an output style is active.
- [System Reminder: Output token limit exceeded](./system-prompts/system-reminder-output-token-limit-exceeded.md) (**35** tks) - Warning when response exceeds output token limit.
- [System Reminder: Plan file reference](./system-prompts/system-reminder-plan-file-reference.md) (**62** tks) - Reference to an existing plan file.
- [System Reminder: Plan mode is active (5-phase)](./system-prompts/system-reminder-plan-mode-is-active-5-phase.md) (**1348** tks) - Enhanced plan mode system reminder with parallel exploration and multi-agent planning.
- [System Reminder: Plan mode is active (iterative)](./system-prompts/system-reminder-plan-mode-is-active-iterative.md) (**854** tks) - Iterative plan mode system reminder for main agent with user interviewing workflow.
- [System Reminder: Plan mode is active (subagent)](./system-prompts/system-reminder-plan-mode-is-active-subagent.md) (**310** tks) - Simplified plan mode system reminder for sub agents.
- [System Reminder: Plan mode re-entry](./system-prompts/system-reminder-plan-mode-re-entry.md) (**236** tks) - System reminder sent when the user enters Plan mode after having previously exited it either via shift+tab or by approving Claude's plan..
- [System Reminder: Queued command (prompt)](./system-prompts/system-reminder-queued-command-prompt.md) (**35** tks) - Queued user message to address (prompt variant).
- [System Reminder: Queued command](./system-prompts/system-reminder-queued-command.md) (**31** tks) - Queued user message to address.
- [System Reminder: Session continuation](./system-prompts/system-reminder-session-continuation.md) (**37** tks) - Notification that session continues from another machine.
- [System Reminder: Session memory](./system-prompts/system-reminder-session-memory.md) (**105** tks) - Past session summaries that may be relevant.
- [System Reminder: Task status](./system-prompts/system-reminder-task-status.md) (**18** tks) - Task status with TaskOutput tool reference.
- [System Reminder: Task tools reminder](./system-prompts/system-reminder-task-tools-reminder.md) (**123** tks) - Reminder to use task tracking tools.
- [System Reminder: Team Coordination](./system-prompts/system-reminder-team-coordination.md) (**247** tks) - System reminder for team coordination.
- [System Reminder: Team Shutdown](./system-prompts/system-reminder-team-shutdown.md) (**136** tks) - System reminder for team shutdown.
- [System Reminder: Todo list changed](./system-prompts/system-reminder-todo-list-changed.md) (**61** tks) - Notification that todo list has changed.
- [System Reminder: Todo list empty](./system-prompts/system-reminder-todo-list-empty.md) (**83** tks) - Reminder that todo list is empty.
- [System Reminder: TodoWrite reminder](./system-prompts/system-reminder-todowrite-reminder.md) (**98** tks) - Reminder to use TodoWrite tool for task tracking.
- [System Reminder: Token usage](./system-prompts/system-reminder-token-usage.md) (**39** tks) - Current token usage statistics.
- [System Reminder: USD budget](./system-prompts/system-reminder-usd-budget.md) (**42** tks) - Current USD budget statistics.
- [System Reminder: Verify plan reminder](./system-prompts/system-reminder-verify-plan-reminder.md) (**47** tks) - Reminder to verify completed plan.

### Builtin Tool Descriptions

- [Tool Description: AskUserQuestion](./system-prompts/tool-description-askuserquestion.md) (**194** tks) - Tool description for asking user questions..
- [Tool Description: Bash](./system-prompts/tool-description-bash.md) (**1067** tks) - Description for the Bash tool, which allows Claude to run shell commands.
- [Tool Description: Computer](./system-prompts/tool-description-computer.md) (**161** tks) - Main description for the Chrome browser computer automation tool.
- [Tool Description: Edit](./system-prompts/tool-description-edit.md) (**278** tks) - Tool description for performing exact string replacements in files.
- [Tool Description: EnterPlanMode](./system-prompts/tool-description-enterplanmode.md) (**970** tks) - Tool description for entering plan mode to explore and design implementation approaches.
- [Tool Description: ExitPlanMode](./system-prompts/tool-description-exitplanmode.md) (**417** tks) - Description for the ExitPlanMode tool, which presents a plan dialog for the user to approve.
- [Tool Description: Glob](./system-prompts/tool-description-glob.md) (**122** tks) - Tool description for file pattern matching and searching by name.
- [Tool Description: Grep](./system-prompts/tool-description-grep.md) (**300** tks) - Tool description for content search using ripgrep.
- [Tool Description: LSP](./system-prompts/tool-description-lsp.md) (**255** tks) - Description for the LSP tool..
- [Tool Description: NotebookEdit](./system-prompts/tool-description-notebookedit.md) (**121** tks) - Tool description for editing Jupyter notebook cells.
- [Tool Description: ReadFile](./system-prompts/tool-description-readfile.md) (**439** tks) - Tool description for reading files.
- [Tool Description: Skill](./system-prompts/tool-description-skill.md) (**444** tks) - Tool description for executing skills in the main conversation.
- [Tool Description: TaskCreate](./system-prompts/tool-description-taskcreate.md) (**570** tks) - Tool description for TaskCreate tool.
- [Tool Description: TaskList](./system-prompts/tool-description-tasklist.md) (**313** tks) - Description for the TaskList tool, which lists all tasks in the task list.
- [Tool Description: Task](./system-prompts/tool-description-task.md) (**1311** tks) - Tool description for launching specialized sub-agents to handle complex tasks.
- [Tool Description: TeammateTool's operation parameter](./system-prompts/tool-description-teammatetools-operation-parameter.md) (**173** tks) - Tool description for the TeammateTool's operation parameter.
- [Tool Description: TeammateTool](./system-prompts/tool-description-teammatetool.md) (**3811** tks) - Tool description for the TeammateTool.
- [Tool Description: TodoWrite](./system-prompts/tool-description-todowrite.md) (**2167** tks) - Tool description for creating and managing task lists.
- [Tool Description: ToolSearch](./system-prompts/tool-description-toolsearch.md) (**520** tks) - Tool description for loading and searching deferred tools before use.
- [Tool Description: WebFetch](./system-prompts/tool-description-webfetch.md) (**297** tks) - Tool description for web fetch functionality.
- [Tool Description: WebSearch](./system-prompts/tool-description-websearch.md) (**329** tks) - Tool description for web search functionality.
- [Tool Description: Write](./system-prompts/tool-description-write.md) (**159** tks) - Tool description for creating and overwriting individual files.

**Additional notes for some Tool Desscriptions**

- [Tool Description: Bash (Git commit and PR creation instructions)](./system-prompts/tool-description-bash-git-commit-and-pr-creation-instructions.md) (**1557** tks) - Instructions for creating git commits and GitHub pull requests.
- [Tool Description: Bash (sandbox note)](./system-prompts/tool-description-bash-sandbox-note.md) (**454** tks) - Note about bash command sandboxing.
