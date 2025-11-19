# Claude Code System Prompts

This repository contains an up-to-date list of all Claude Code's various system prompts and their associated token counts as of **[Claude Code v2.0.33](https://www.npmjs.com/package/@anthropic-ai/claude-code/v/2.0.33) (November 4th, 2025).**

Why multiple "system prompts?"

**Claude Code doesn't just have one single string for its system prompt.**

Instead, there are:
- Large portions conditionally added depending on the environment and various configs.
- Descriptions for builtin tools like `Write`, `Bash`, and `TodoWrite`, and some are fairly large.
- Separate system prompts for builtin agents like Explore and Plan.
- Numerous AI-powered utility functions, such as conversation compaction, `CLAUDE.md` generation, session title generation, etc. featuring their own systems prompts.

The result&mdash;40+ strings that are constantly changing and moving within a very large minified JS file.

> [!NOTE]
> Want to **modify a particular piece of the system prompt** in your own Claude Code installation?  **Use [tweakcc](https://github.com/Piebald-AI/tweakcc).**  It&mdash;
> - lets you customize the the individual pieces of the system prompt as markdown files, and then
> - patches your npm-based or native (binary) Claude Code installation with them, and also
> - provides diffing and conflict management for when both you and Anthropic have conflicting modifications to the same prompt file.

## Prompts

Note that some prompts contain interpolated bits such as builtin tool name references, lists of available sub agents, and various other context-specific variables, so the actual counts in a particular Claude Code session will differ slightly&mdash;likely not beyond ±20 tokens, however.

### Agent Prompts

Sub-agents and utilities.

#### Sub-agents

- [Agent Prompt: Explore](./system-prompts/agent-prompt-explore.md) (**230** tks) - System prompt for the Explore subagent.
- [Agent Prompt: Task tool](./system-prompts/agent-prompt-task-tool.md) (**294** tks) - System prompt given to the subagent spawned via the Task tool.

### Creation Assistants

- [Agent Prompt: Agent creation architect](./system-prompts/agent-prompt-agent-creation-architect.md) (**1111** tks) - System prompt for creating custom AI agents with detailed specifications.
- [Agent Prompt: CLAUDE.md creation](./system-prompts/agent-prompt-claudemd-creation.md) (**384** tks) - System prompt for analyzing codebases and creating CLAUDE.md documentation files.
- [Agent Prompt: Status line setup](./system-prompts/agent-prompt-status-line-setup.md) (**993** tks) - System prompt for the statusline-setup agent that configures status line display.

### Slash commands

- [Agent Prompt: /pr-comments slash command](./system-prompts/agent-prompt-pr-comments-slash-command.md) (**404** tks) - System prompt for fetching and displaying GitHub PR comments.
- [Agent Prompt: /review-pr slash command](./system-prompts/agent-prompt-review-pr-slash-command.md) (**245** tks) - System prompt for reviewing GitHub pull requests with code analysis.
- [Agent Prompt: /security-review slash](./system-prompts/agent-prompt-security-review-slash.md) (**2614** tks) - Comprehensive security review prompt for analyzing code changes with focus on exploitable vulnerabilities.

### Utilities

- [Agent Prompt: Bash command file path extraction](./system-prompts/agent-prompt-bash-command-file-path-extraction.md) (**286** tks) - System prompt for extracting file paths from bash command output.
- [Agent Prompt: Bash command prefix detection](./system-prompts/agent-prompt-bash-command-prefix-detection.md) (**835** tks) - System prompt for detecting command prefixes and command injection.
- [Agent Prompt: Bash output summarization](./system-prompts/agent-prompt-bash-output-summarization.md) (**605** tks) - System prompt for determining whether bash command output should be summarized.
- [Agent Prompt: Conversation summarization with additional instructions](./system-prompts/agent-prompt-conversation-summarization-with-additional-instructions.md) (**1133** tks) - Extended summarization prompt with support for custom additional instructions.
- [Agent Prompt: Conversation summarization](./system-prompts/agent-prompt-conversation-summarization.md) (**1121** tks) - System prompt for creating detailed conversation summaries.
- [Agent Prompt: Session notes template](./system-prompts/agent-prompt-session-notes-template.md) (**226** tks) - Template structure for session notes tracking coding work and decisions.
- [Agent Prompt: Session notes update instructions](./system-prompts/agent-prompt-session-notes-update-instructions.md) (**730** tks) - Instructions for updating session notes files during conversations.
- [Agent Prompt: Session title generation](./system-prompts/agent-prompt-session-title-generation.md) (**159** tks) - System prompt for generating succinct titles for coding sessions.
- [Agent Prompt: Update Magic Docs](./system-prompts/agent-prompt-update-magic-docs.md) (**718** tks) - Prompt for the magic-docs agent..
- [Agent Prompt: User sentiment analysis](./system-prompts/agent-prompt-user-sentiment-analysis.md) (**205** tks) - System prompt for analyzing user frustration and PR creation requests.
- [Agent Prompt: WebFetch summarizer](./system-prompts/agent-prompt-webfetch-summarizer.md) (**147** tks) - Prompt for agent that summarizes verbose output from WebFetch for the main model.

<!--
### Data

Misc large strings.

- [Data: GitHub Actions workflow for @claude mentions](./system-prompts/data-github-actions-workflow-for-@claude-mentions.md) (**531** tks) - GitHub Actions workflow template for triggering Claude Code via @claude mentions.
- [Data: GitHub Actions workflow for automated code review (beta)](./system-prompts/data-github-actions-workflow-for-automated-code-review-beta.md) (**573** tks) - GitHub Actions workflow template for automated Claude Code reviews using direct_prompt.
- [Data: GitHub App installation PR description](./system-prompts/data-github-app-installation-pr-description.md) (**424** tks) - Template for PR description when installing Claude Code GitHub App integration.
-->

### System Prompt

Parts of the main system prompt.

- [**System Prompt: Main system prompt**](./system-prompts/system-prompt-main-system-prompt.md) (**2326** tks) - Core system prompt for Claude Code defining behavior, tone, and tool usage policies.
- [System Prompt: Learning mode (insights)](./system-prompts/system-prompt-learning-mode-insights.md) (**142** tks) - Instructions for providing educational insights when learning mode is active.
- [System Prompt: Learning mode](./system-prompts/system-prompt-learning-mode.md) (**1042** tks) - System Prompt: Main system prompt for learning mode with human collaboration instructions.

### System Reminders

Text for large system reminders.

> [!NOTE]
> Note that we're planning to add a **system reminder creator/editor** to [tweakcc](https://github.com/Piebald-AI/tweakcc); :+1: [this issue](https://github.com/Piebald-AI/tweakcc/issues/113) if you're interested in that idea.

- [System Reminder: Plan mode is active](./system-prompts/system-reminder-plan-mode-is-active.md) (**242** tks) - System reminder sent to Claude when the user enters plan mode.

### Builtin Tool Descriptions

- [Tool Description: Bash](./system-prompts/tool-description-bash.md) (**1074** tks) - Description for the Bash tool, which allows Claude to run shell commands.
- [Tool Description: Edit](./system-prompts/tool-description-edit.md) (**278** tks) - Tool description for performing exact string replacements in files.
- [Tool Description: ExitPlanMode](./system-prompts/tool-description-exitplanmode.md) (**342** tks) - Description for the ExitPlanMode tool, which presents a plan dialog for the user to approve.
- [Tool Description: Glob](./system-prompts/tool-description-glob.md) (**122** tks) - Tool description for file pattern matching and searching by name.
- [Tool Description: Grep](./system-prompts/tool-description-grep.md) (**300** tks) - Tool description for content search using ripgrep.
- [Tool Description: LSP](./system-prompts/tool-description-lsp.md) (**172** tks) - Description for the LSP tool..
- [Tool Description: NotebookEdit](./system-prompts/tool-description-notebookedit.md) (**121** tks) - Tool description for editing Jupyter notebook cells.
- [Tool Description: ReadFile](./system-prompts/tool-description-readfile.md) (**439** tks) - Tool description for reading files.
- [Tool Description: Skill](./system-prompts/tool-description-skill.md) (**270** tks) - Tool description for executing skills in the main conversation.
- [Tool Description: SlashCommand](./system-prompts/tool-description-slashcommand.md) (**381** tks) - Tool description for executing slash commands.
- [Tool Description: Task](./system-prompts/tool-description-task.md) (**987** tks) - Tool description for launching specialized sub-agents to handle complex tasks.
- [Tool Description: TodoWrite](./system-prompts/tool-description-todowrite.md) (**2167** tks) - Tool description for creating and managing task lists.
- [Tool Description: WebFetch](./system-prompts/tool-description-webfetch.md) (**278** tks) - Tool description for web fetch functionality.
- [Tool Description: WebSearch](./system-prompts/tool-description-websearch.md) (**166** tks) - Tool description for web search functionality.
- [Tool Description: Write](./system-prompts/tool-description-write.md) (**159** tks) - Tool description creating/overwriting writing individual files.

**Additional notes for some Tool Desscriptions**

- [Tool Description: Bash (Git commit and PR creation instructions)](./system-prompts/tool-description-bash-git-commit-and-pr-creation-instructions.md) (**1598** tks) - Instructions for creating git commits and GitHub pull requests.
- [Tool Description: Bash (sandbox note)](./system-prompts/tool-description-bash-sandbox-note.md) (**438** tks) - Note about bash command sandboxing.
- [Tool Description: Task (async return note)](./system-prompts/tool-description-task-async-return-note.md) (**202** tks) - Message returned to the model when a subagent launched successfully.
