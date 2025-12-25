<div>
<div align="right">
<a href="https://piebald.ai"><img width="200" top="20" align="right" src="https://github.com/Piebald-AI/.github/raw/main/Wordmark.svg"></a>
</div>

<div align="left">

### Announcement: Piebald is released!
We've released **Piebald**, the ultimate agentic AI developer experience. \
Download it and try it out for free!  **https://piebald.ai/**

<sub>[Scroll down for Claude Code's system prompts.](https://github.com/Piebald-AI/claude-code-system-prompts#claude-code-system-prompts) :point_down:</sub>

</div>
</div>

<div align="left">
<a href="https://piebald.ai">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/79c18689-e2f0-4008-a13f-61c80756286a">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/25cb5df8-cf15-4cae-9c1e-e88645f06ee1">
  <img alt="hero" width="600" src="https://github.com/user-attachments/assets/25cb5df8-cf15-4cae-9c1e-e88645f06ee1">
</picture>
</a>
</div>

# Claude Code System Prompts

[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)

This repository contains an up-to-date list of all Claude Code's various system prompts and their associated token counts as of **[Claude Code v2.0.76](https://www.npmjs.com/package/@anthropic-ai/claude-code/v/2.0.76) (December 22nd, 2025).**  It also contains a [**CHANGELOG.md**](./CHANGELOG.md) for the system prompts across 57 versions since v2.0.14.  From the team behind [<img src="https://github.com/Piebald-AI/piebald/raw/main/assets/logo.svg" width="15"> **Piebald.**](https://piebald.ai/)

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
- [Agent Prompt: Task tool](./system-prompts/agent-prompt-task-tool.md) (**294** tks) - System prompt given to the subagent spawned via the Task tool.

### Creation Assistants

- [Agent Prompt: Agent creation architect](./system-prompts/agent-prompt-agent-creation-architect.md) (**1111** tks) - System prompt for creating custom AI agents with detailed specifications.
- [Agent Prompt: CLAUDE.md creation](./system-prompts/agent-prompt-claudemd-creation.md) (**384** tks) - System prompt for analyzing codebases and creating CLAUDE.md documentation files.
- [Agent Prompt: Status line setup](./system-prompts/agent-prompt-status-line-setup.md) (**1310** tks) - System prompt for the statusline-setup agent that configures status line display.

### Slash commands

- [Agent Prompt: /pr-comments slash command](./system-prompts/agent-prompt-pr-comments-slash-command.md) (**402** tks) - System prompt for fetching and displaying GitHub PR comments.
- [Agent Prompt: /review-pr slash command](./system-prompts/agent-prompt-review-pr-slash-command.md) (**243** tks) - System prompt for reviewing GitHub pull requests with code analysis.
- [Agent Prompt: /security-review slash](./system-prompts/agent-prompt-security-review-slash.md) (**2610** tks) - Comprehensive security review prompt for analyzing code changes with focus on exploitable vulnerabilities.

### Utilities

- [Agent Prompt: Agent Hook](./system-prompts/agent-prompt-agent-hook.md) (**133** tks) - Prompt for an 'agent hook'.
- [Agent Prompt: Bash command file path extraction](./system-prompts/agent-prompt-bash-command-file-path-extraction.md) (**286** tks) - System prompt for extracting file paths from bash command output.
- [Agent Prompt: Bash command prefix detection](./system-prompts/agent-prompt-bash-command-prefix-detection.md) (**835** tks) - System prompt for detecting command prefixes and command injection.
- [Agent Prompt: Bash output summarization](./system-prompts/agent-prompt-bash-output-summarization.md) (**605** tks) - System prompt for determining whether bash command output should be summarized.
- [Agent Prompt: Claude guide agent](./system-prompts/agent-prompt-claude-guide-agent.md) (**763** tks) - System prompt for the claude-guide agent that helps users understand and use Claude Code, the Claude Agent SDK and the Claude API effectively..
- [Agent Prompt: Conversation summarization with additional instructions](./system-prompts/agent-prompt-conversation-summarization-with-additional-instructions.md) (**1133** tks) - Extended summarization prompt with support for custom additional instructions.
- [Agent Prompt: Conversation summarization](./system-prompts/agent-prompt-conversation-summarization.md) (**1121** tks) - System prompt for creating detailed conversation summaries.
- [Agent Prompt: Prompt Hook execution](./system-prompts/agent-prompt-prompt-hook-execution.md) (**134** tks) - Prompt given to Claude when acting evaluating whether to pass or fail a prompt hook..
- [Agent Prompt: Prompt Suggestion Generator v2](./system-prompts/agent-prompt-prompt-suggestion-generator-v2.md) (**296** tks) - V2 instructions for generating prompt suggestions for Claude Code.
- [Agent Prompt: Session Search Assistant](./system-prompts/agent-prompt-session-search-assistant.md) (**444** tks) - Agent prompt for the session search assistant that finds relevant sessions based on user queries and metadata.
- [Agent Prompt: Session notes template](./system-prompts/agent-prompt-session-notes-template.md) (**292** tks) - Template structure for session notes tracking coding work and decisions.
- [Agent Prompt: Session notes update instructions](./system-prompts/agent-prompt-session-notes-update-instructions.md) (**756** tks) - Instructions for updating session notes files during conversations.
- [Agent Prompt: Session title and branch generation](./system-prompts/agent-prompt-session-title-and-branch-generation.md) (**333** tks) - System prompt for generating succinct titles and git branch names for coding sessions.
- [Agent Prompt: Update Magic Docs](./system-prompts/agent-prompt-update-magic-docs.md) (**718** tks) - Prompt for the magic-docs agent..
- [Agent Prompt: User sentiment analysis](./system-prompts/agent-prompt-user-sentiment-analysis.md) (**205** tks) - System prompt for analyzing user frustration and PR creation requests.
- [Agent Prompt: WebFetch summarizer](./system-prompts/agent-prompt-webfetch-summarizer.md) (**185** tks) - Prompt for agent that summarizes verbose output from WebFetch for the main model.

<!--
### Data

Misc large strings.

- [Data: GitHub Actions workflow for @claude mentions](./system-prompts/data-github-actions-workflow-for-claude-mentions.md) (**527** tks) - GitHub Actions workflow template for triggering Claude Code via @claude mentions.
- [Data: GitHub Actions workflow for automated code review (beta)](./system-prompts/data-github-actions-workflow-for-automated-code-review-beta.md) (**569** tks) - GitHub Actions workflow template for automated Claude Code reviews using direct_prompt.
- [Data: GitHub App installation PR description](./system-prompts/data-github-app-installation-pr-description.md) (**424** tks) - Template for PR description when installing Claude Code GitHub App integration.
-->

### System Prompt

Parts of the main system prompt.

- [**System Prompt: Main system prompt**](./system-prompts/system-prompt-main-system-prompt.md) (**2981** tks) - Core system prompt for Claude Code defining behavior, tone, and tool usage policies.
- [System Prompt: Claude in Chrome browser automation](./system-prompts/system-prompt-claude-in-chrome-browser-automation.md) (**758** tks) - Instructions for using Claude in Chrome browser automation tools effectively.
- [System Prompt: Git status](./system-prompts/system-prompt-git-status.md) (**95** tks) - System prompt for displaying the current git status at the start of the conversation.
- [System Prompt: Learning mode (insights)](./system-prompts/system-prompt-learning-mode-insights.md) (**142** tks) - Instructions for providing educational insights when learning mode is active.
- [System Prompt: Learning mode](./system-prompts/system-prompt-learning-mode.md) (**1042** tks) - System Prompt: Main system prompt for learning mode with human collaboration instructions.
- [System Prompt: MCP CLI](./system-prompts/system-prompt-mcp-cli.md) (**1335** tks) - Instructions for using mcp-cli to interact with Model Context Protocol servers.
- [System Prompt: Scratchpad directory](./system-prompts/system-prompt-scratchpad-directory.md) (**172** tks) - Instructions for using a dedicated scratchpad directory for temporary files.

### System Reminders

Text for large system reminders.

> [!NOTE]
> Note that we're planning to add a **system reminder creator/editor** to [tweakcc](https://github.com/Piebald-AI/tweakcc); :+1: [this issue](https://github.com/Piebald-AI/tweakcc/issues/113) if you're interested in that idea.

- [System Reminder: Plan mode is active (for subagents)](./system-prompts/system-reminder-plan-mode-is-active-for-subagents.md) (**310** tks) - Simplified plan mode system reminder for sub agents.
- [System Reminder: Plan mode is active](./system-prompts/system-reminder-plan-mode-is-active.md) (**1211** tks) - Enhanced plan mode system reminder with parallel exploration and multi-agent planning.
- [System Reminder: Plan mode re-entry](./system-prompts/system-reminder-plan-mode-re-entry.md) (**236** tks) - System reminder sent when the user enters Plan mode after having previously exited it either via shift+tab or by approving Claude's plan..

### Builtin Tool Descriptions

- [Tool Description: AskUserQuestion](./system-prompts/tool-description-askuserquestion.md) (**137** tks) - Tool description for asking user questions..
- [Tool Description: Bash](./system-prompts/tool-description-bash.md) (**1074** tks) - Description for the Bash tool, which allows Claude to run shell commands.
- [Tool Description: Computer](./system-prompts/tool-description-computer.md) (**161** tks) - Main description for the Chrome browser computer automation tool.
- [Tool Description: Edit](./system-prompts/tool-description-edit.md) (**278** tks) - Tool description for performing exact string replacements in files.
- [Tool Description: EnterPlanMode](./system-prompts/tool-description-enterplanmode.md) (**970** tks) - Tool description for entering plan mode to explore and design implementation approaches.
- [Tool Description: ExitPlanMode v2](./system-prompts/tool-description-exitplanmode-v2.md) (**450** tks) - V2 description for the ExitPlanMode tool, which presents a plan dialog for the user to approve.
- [Tool Description: ExitPlanMode](./system-prompts/tool-description-exitplanmode.md) (**342** tks) - Description for the ExitPlanMode tool, which presents a plan dialog for the user to approve.
- [Tool Description: Glob](./system-prompts/tool-description-glob.md) (**122** tks) - Tool description for file pattern matching and searching by name.
- [Tool Description: Grep](./system-prompts/tool-description-grep.md) (**300** tks) - Tool description for content search using ripgrep.
- [Tool Description: LSP](./system-prompts/tool-description-lsp.md) (**255** tks) - Description for the LSP tool..
- [Tool Description: MCPSearch](./system-prompts/tool-description-mcpsearch.md) (**477** tks) - Tool description for the MCPSearch tool.
- [Tool Description: NotebookEdit](./system-prompts/tool-description-notebookedit.md) (**121** tks) - Tool description for editing Jupyter notebook cells.
- [Tool Description: ReadFile](./system-prompts/tool-description-readfile.md) (**439** tks) - Tool description for reading files.
- [Tool Description: Skill](./system-prompts/tool-description-skill.md) (**399** tks) - Tool description for executing skills in the main conversation.
- [Tool Description: Task](./system-prompts/tool-description-task.md) (**1214** tks) - Tool description for launching specialized sub-agents to handle complex tasks.
- [Tool Description: TodoWrite](./system-prompts/tool-description-todowrite.md) (**2167** tks) - Tool description for creating and managing task lists.
- [Tool Description: WebFetch](./system-prompts/tool-description-webfetch.md) (**265** tks) - Tool description for web fetch functionality.
- [Tool Description: WebSearch](./system-prompts/tool-description-websearch.md) (**334** tks) - Tool description for web search functionality.
- [Tool Description: Write](./system-prompts/tool-description-write.md) (**159** tks) - Tool description creating/overwriting writing individual files.

**Additional notes for some Tool Desscriptions**

- [Tool Description: Bash (Git commit and PR creation instructions)](./system-prompts/tool-description-bash-git-commit-and-pr-creation-instructions.md) (**1615** tks) - Instructions for creating git commits and GitHub pull requests.
- [Tool Description: Bash (sandbox note)](./system-prompts/tool-description-bash-sandbox-note.md) (**454** tks) - Note about bash command sandboxing.
- [Tool Description: MCPSearch (with available tools)](./system-prompts/tool-description-mcpsearch-with-available-tools.md) (**510** tks) - Tool description for the MCPSearch tool with available tools listed.
- [Tool Description: Task (async return note)](./system-prompts/tool-description-task-async-return-note.md) (**201** tks) - Message returned to the model when a subagent launched successfully.
