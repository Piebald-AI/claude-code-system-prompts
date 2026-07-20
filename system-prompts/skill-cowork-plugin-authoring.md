<!--
name: "Skill: Cowork plugin authoring"
description: "Skill instructions for creating or customizing Cowork plugins, including mode selection, research, implementation, packaging, connector replacement, and plugin delivery"
ccVersion: "2.1.163"
-->
# Cowork Plugin Authoring

Create a new Cowork plugin from scratch, or customize an existing one for a specific organization. Both paths deliver a ready-to-install `.plugin` file at the end.

## Determining the Mode

Decide from the user's request:

- **Customize** — the user names an existing installed plugin ("customize the X plugin", "configure X for my company", "set up the X plugin", "update the X skill"). Follow **Customizing an Existing Plugin** below.
- **Create** — the user wants to build a plugin from scratch ("create a plugin for X", "make a new plugin", "build a plugin that does X"). Follow **Creating a New Plugin** below.

> **Nontechnical output**: Keep all user-facing conversation in plain language. Never mention file paths, directory structures, schema fields, `~~` prefixes, or placeholders unless the user asks. Frame everything in terms of what the plugin will do.

> **AskUserQuestion**: When you need input, use AskUserQuestion. Don't assume "industry standard" defaults are correct. AskUserQuestion always includes a Skip button and a free-text input box for custom answers, so do not include `None` or `Other` as options.

## Plugin Architecture

A plugin is a self-contained directory that extends Claude with skills, agents, hooks, and MCP server integrations.

### Directory Structure

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json           # Required: plugin manifest
├── skills/                   # Skills (subdirectories with SKILL.md)
│   └── skill-name/
│       ├── SKILL.md
│       └── references/
├── agents/                   # Subagent definitions (.md files)
├── .mcp.json                 # MCP server definitions
└── README.md                 # Plugin documentation
```

> **Legacy `commands/` format**: Older plugins may include a `commands/` directory with single-file `.md` slash commands. This format still works, but new plugins should use `skills/*/SKILL.md` instead — the Cowork UI presents both as a single "Skills" concept, and the skills format supports progressive disclosure via `references/`. Treat `commands/*.md` files the same way you would `skills/*/SKILL.md` when customizing.

**Rules:**

- `.claude-plugin/plugin.json` is always required
- Component directories (`skills/`, `agents/`) go at the plugin root, not inside `.claude-plugin/`
- Only create directories for components the plugin actually uses
- Use kebab-case for all directory and file names

### plugin.json Manifest

Located at `.claude-plugin/plugin.json`. Minimal required field is `name`.

```json
{
  "name": "plugin-name",
  "version": "0.1.0",
  "description": "Brief explanation of plugin purpose",
  "author": {
    "name": "Author Name"
  }
}
```

**Name rules:** kebab-case, lowercase with hyphens, no spaces or special characters.
**Version:** semver format (MAJOR.MINOR.PATCH). Start at `0.1.0`.

Optional fields: `homepage`, `repository`, `license`, `keywords`.

Custom component paths can be specified (supplements, does not replace, auto-discovery):

```json
{
  "commands": "./custom-commands",
  "agents": ["./agents", "./specialized-agents"],
  "hooks": "./config/hooks.json",
  "mcpServers": "./.mcp.json"
}
```

### Component Summary

Detailed schemas for each component type are in `references/component-schemas.md`.

| Component                          | Location            | Format                      |
| ---------------------------------- | ------------------- | --------------------------- |
| Skills                             | `skills/*/SKILL.md` | Markdown + YAML frontmatter |
| MCP Servers                        | `.mcp.json`         | JSON                        |
| Agents (uncommonly used in Cowork) | `agents/*.md`       | Markdown + YAML frontmatter |
| Hooks (rarely used in Cowork)      | `hooks/hooks.json`  | JSON                        |
| Commands (legacy)                  | `commands/*.md`     | Markdown + YAML frontmatter |

This schema is shared with Claude Code's plugin system, but you're building for Claude Cowork, a desktop app for knowledge work. Cowork users will usually find skills the most useful. **Scaffold new plugins with `skills/*/SKILL.md` — do not create `commands/` unless the user explicitly needs the legacy single-file format.**

### Customizable plugins with `~~` placeholders

> **Do not use or ask about this pattern by default.** Only introduce `~~` placeholders if the user explicitly says they want people outside their organization to use the plugin. You can mention it as an option if they want to distribute externally, but do not proactively ask with AskUserQuestion.

When a plugin is intended to be shared outside the author's company, it might reference external tools by category rather than specific product (e.g., "project tracker" instead of "Jira"). Use generic language and mark these as requiring customization with two tilde characters: `create an issue in ~~project tracker`.

If any tool categories are used, write a `CONNECTORS.md` file at the plugin root to explain:

```markdown
# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user
connects in that category. Plugins are tool-agnostic — they describe
workflows in terms of categories rather than specific products.

## Connectors for this plugin

| Category        | Placeholder         | Options                         |
| --------------- | ------------------- | ------------------------------- |
| Chat            | `~~chat`            | Slack, Microsoft Teams, Discord |
| Project tracker | `~~project tracker` | Linear, Asana, Jira             |
```

### ${CLAUDE_PLUGIN_ROOT} Variable

Use `${CLAUDE_PLUGIN_ROOT}` for all intra-plugin path references in hooks and MCP configs. Never hardcode absolute paths.

## Creating a New Plugin

Build from scratch through a five-phase guided conversation.

### Phase 1: Discovery

Understand what the user wants to build and why. Ask (only what is unclear — skip questions the user's initial request already answers):

- What should this plugin do? What problem does it solve?
- Who will use it and in what context?
- Does it integrate with any external tools or services?
- Is there a similar plugin or workflow to reference?

Summarize understanding and confirm before proceeding.

### Phase 2: Component Planning

Based on discovery, determine which component types are needed:

- **Skills** — Specialized knowledge Claude loads on-demand, or user-initiated actions (domain expertise, reference schemas, workflow guides, deploy/configure/analyze/review actions)
- **MCP Servers** — External service integration (databases, APIs, SaaS tools)
- **Agents (uncommon)** — Autonomous multi-step tasks (validation, generation, analysis)
- **Hooks (rare)** — Automatic behavior on certain events (enforce policies, load context, validate operations)

Present a component plan table including types you decided not to create:

```
| Component | Count | Purpose |
|-----------|-------|---------|
| Skills    | 3     | Domain knowledge for X, /do-thing, /check-thing |
| Agents    | 0     | Not needed |
| Hooks     | 1     | Validate writes |
| MCP       | 1     | Connect to service Y |
```

Get user confirmation before proceeding.

### Phase 3: Design & Clarifying Questions

Specify each component in detail. Resolve all ambiguities before implementation. Present questions grouped by component type and wait for answers.

**Skills:**

- What user queries should trigger this skill?
- What knowledge domains does it cover?
- Should it include reference files for detailed content?
- If it represents a user-initiated action: what arguments does it accept, and what tools does it need? (Read, Write, Bash, Grep, etc.)

**Agents:**

- Should it trigger proactively or only when requested?
- What tools does it need?
- What output format?

**Hooks:**

- Which events? (PreToolUse, PostToolUse, Stop, SessionStart, etc.)
- What behavior — validate, block, modify, add context?
- Prompt-based (LLM-driven) or command-based (deterministic script)?

**MCP Servers:**

- What server type? (stdio for local, SSE for hosted with OAuth, HTTP for REST APIs)
- What authentication method?
- What tools should be exposed?

If the user says "whatever you think is best," provide specific recommendations and get explicit confirmation.

### Phase 4: Implementation

Create all plugin files following best practices.

1. Create the plugin directory structure
2. Create `plugin.json` manifest
3. Create each component (see `references/component-schemas.md` for exact formats)
4. Create `README.md` documenting the plugin

**Guidelines:**

- **Skills** use progressive disclosure: lean SKILL.md body (under 3,000 words), detailed content in `references/`. Frontmatter description must be third-person with specific trigger phrases. Skill bodies are instructions FOR Claude, not messages to the user — write them as directives.
- **Agents** need a description with `<example>` blocks showing triggering conditions, plus a system prompt in the markdown body.
- **Hooks** config goes in `hooks/hooks.json`. Use `${CLAUDE_PLUGIN_ROOT}` for script paths. Prefer prompt-based hooks for complex logic.
- **MCP configs** go in `.mcp.json` at plugin root. Use `${CLAUDE_PLUGIN_ROOT}` for local server paths. Document required env vars in README.

### Phase 5: Review

1. Summarize what was created — list each component and its purpose
2. Ask if the user wants any adjustments
3. Run `claude plugin validate <path-to-plugin-json>` to check the plugin structure. If this command is unavailable (e.g., when running inside Cowork), verify manually:
   - `.claude-plugin/plugin.json` exists and contains valid JSON with at least a `name` field
   - The `name` field is kebab-case (lowercase letters, numbers, and hyphens only)
   - Any component directories referenced by the plugin (`commands/`, `skills/`, `agents/`, `hooks/`) actually exist and contain files in the expected formats — `.md` for commands/skills/agents, `.json` for hooks
   - Each skill subdirectory contains a `SKILL.md`
   - Report what passed and what didn't, the same way the CLI validator would

   Fix any errors, then proceed to **Packaging**.

## Customizing an Existing Plugin

Customize a plugin for a specific organization — either by setting up a generic plugin template for the first time, or by tweaking an already-configured plugin.

### Finding the plugin

Run `find mnt/.local-plugins mnt/.plugins ~/.claude/plugins/synced -type d -name "*<plugin-name>*" 2>/dev/null` to locate the plugin directory, then read its files to understand its structure before making changes.

If you cannot find the plugin directory in any of those locations, let the user know: "I couldn't find an installed plugin named '<plugin-name>'. If it's installed on your desktop, open this task from the Cowork desktop app so I can access it."

### Determining the Customization Mode

After locating the plugin, check for `~~`-prefixed placeholders: `grep -rn '~~\w' /path/to/plugin --include='*.md' --include='*.json'`

> **Default rule**: If `~~` placeholders exist, default to **Generic plugin setup** unless the user explicitly asks to customize a specific part of the plugin.

**1. Generic plugin setup** — The plugin contains `~~`-prefixed placeholders. These are customization points in a template that need to be replaced with real values (e.g., `~~Jira` → `Asana`, `~~your-team-channel` → `#engineering`).

**2. Scoped customization** — No `~~` placeholders exist, and the user asked to customize a specific part of the plugin (e.g., "customize the connectors", "update the standup skill", "change the ticket tool"). Read the plugin files to find the relevant section(s) and focus only on those. Do not scan the entire plugin or present unrelated customization items.

**3. General customization** — No `~~` placeholders exist, and the user wants to modify the plugin broadly. Read the plugin's files to understand its current configuration, then ask the user what they'd like to change.

> **Important**: Never change the name of the plugin or skill being customized. Do not rename directories, files, or the plugin/skill name fields.

### Customization Workflow

#### Phase 0: Gather User Intent (scoped and general customization only)

Check whether the user provided free-form context alongside their request (e.g., "customize the standup skill — we do async standups in #eng-updates every morning").

- **If the user provided context**: Record it and use it to pre-fill answers in Phase 3 — skip asking questions the user already answered here.
- **If the user did not provide context**: Ask a single open-ended question using AskUserQuestion before proceeding. Tailor it to what they asked to customize — e.g., "What changes do you have in mind for the brief skill?" or "What would you like to change about how this plugin works?" Keep it short and specific.

#### Phase 1: Gather Context from Knowledge MCPs

Use company-internal knowledge MCPs to collect information relevant to the customization scope. See `references/search-strategies.md` for detailed query patterns.

**What to gather** (scope to what's relevant):

- Tool names and services the organization uses
- Organizational processes and workflows
- Team conventions (naming, statuses, estimation scales)
- Configuration values (workspace IDs, project names, team identifiers)

**Sources to search:**

1. **Chat/Slack MCPs** — tool mentions, integrations, workflow discussions
2. **Document MCPs** — onboarding docs, tool guides, setup instructions
3. **Email MCPs** — license notifications, admin emails, setup invitations

Record all findings for use in Phase 3.

#### Phase 2: Create Todo List

Build a todo list of changes to make, scoped appropriately:

- **Scoped customization**: Only items related to the specific section the user asked about.
- **Generic plugin setup**: Run `grep -rn '~~\w' /path/to/plugin --include='*.md' --include='*.json'` to find all placeholder customization points. Group them by theme.
- **General customization**: Read the plugin files, understand the current config, and based on the user's request, identify what needs to change.

Use user-friendly descriptions that focus on the plugin's purpose:

- **Good**: "Learn how standup prep works at Company"
- **Bad**: "Replace placeholders in skills/standup-prep/SKILL.md"

#### Phase 3: Complete Todo Items

Work through each item using context from Phase 0 and Phase 1.

**If the user's free-form input (Phase 0) or knowledge MCPs (Phase 1) provided a clear answer**: Apply directly without confirmation.

**Otherwise**: Use AskUserQuestion. Don't assume "industry standard" defaults are correct — if neither the user's input nor knowledge MCPs provided a specific answer, ask.

**Types of changes:**

1. **Placeholder replacements** (generic setup): `~~Jira` → `Asana`, `~~your-org-channel` → `#engineering`
2. **Content updates**: Modifying instructions, skills, workflows, or references to match the organization
3. **URL pattern updates**: `tickets.example.com/your-team/123` → `app.asana.com/0/PROJECT_ID/TASK_ID`
4. **Configuration values**: Workspace IDs, project names, team identifiers

If the user doesn't know or skips, leave the value unchanged (or the `~~`-prefixed placeholder, for generic setup).

#### Phase 4: Search for Useful MCPs

After customization items are resolved, connect MCPs for any tools that were identified or changed. See `references/mcp-servers.md` for the full workflow, category-to-keywords mapping, and config file format.

For each tool identified during customization:

1. Search the registry: `search_mcp_registry(keywords=[...])` using category keywords from `references/mcp-servers.md`, or search for the specific tool name if already known
2. If unconnected: `suggest_connectors(directoryUuids=["chosen-uuid"])` — user completes auth
3. Update the plugin's MCP config file (check `plugin.json` for custom location, otherwise `.mcp.json` at root)

Collect all MCP results and present them together in the summary output — don't present MCPs one at a time during this phase.

### Summary Output

After customization, present the user with a summary of what was learned grouped by source. Always include the MCPs sections showing which were connected and which the user should still connect:

```markdown
## From searching Slack

- You use Asana for project management
- Sprint cycles are 2 weeks

## From searching documents

- Story points use T-shirt sizes

## From your answers

- Ticket statuses are: Backlog, In Progress, In Review, Done
```

Then present the MCPs that were connected during setup and any that the user should still connect, with instructions.

If no knowledge MCPs were available in Phase 1, and the user had to answer at least one question manually, include a note at the end:

> By the way, connecting sources like Slack or Microsoft Teams would let me find answers automatically next time you customize a plugin.

Then proceed to **Packaging**.

## Packaging

After create or customize completes, package the plugin as a `.plugin` file and deliver it with the SendUserFile tool:

1. Zip the plugin directory:
   ```bash
   cd /path/to/plugin-dir && zip -r /tmp/plugin-name.plugin . -x "setup/*" -x "*.DS_Store"
   ```
2. Call `SendUserFile` with `files: ["/tmp/plugin-name.plugin"]`, `status: "normal"`, and a short caption summarizing what was built or changed.

The `.plugin` file will appear in the chat as a rich preview where the user can browse the files and accept the plugin by pressing a button.

> **Naming**: Use the plugin name from `plugin.json` (for create) or the original plugin directory name (for customize) as the `.plugin` filename. Do not rename the plugin or its files during customization — only replace placeholder values and update content.

## Best Practices

- **Start small**: Begin with the minimum viable set of components. A plugin with one well-crafted skill is more useful than one with five half-baked components.
- **Progressive disclosure for skills**: Core knowledge in SKILL.md, detailed reference material in `references/`, working examples in `examples/`.
- **Clear trigger phrases**: Skill descriptions should include specific phrases users would say. Agent descriptions should include `<example>` blocks.
- **Skills are for Claude**: Write skill body content as instructions for Claude to follow, not documentation for the user to read.
- **Imperative writing style**: Use verb-first instructions in skills ("Parse the config file," not "You should parse the config file").
- **Portability**: Always use `${CLAUDE_PLUGIN_ROOT}` for intra-plugin paths, never hardcoded paths.
- **Security**: Use environment variables for credentials, HTTPS for remote servers, least-privilege tool access.

## Additional Resources

- **`references/component-schemas.md`** — Detailed format specifications for every component type (skills, agents, hooks, MCP, legacy commands, CONNECTORS.md)
- **`references/example-plugins.md`** — Three complete example plugin structures at different complexity levels
- **`references/mcp-servers.md`** — MCP discovery workflow, category-to-keywords mapping, config file locations, example `.mcp.json`
- **`references/search-strategies.md`** — Knowledge MCP query patterns for finding tool names and org values
