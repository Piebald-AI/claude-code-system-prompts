import json
import os

ROOT_DIR = "/Users/cyberial/.gemini/antigravity/worktrees/friendly-chandrasekhar/audit-claude-system-prompts"
METADATA_PATH = os.path.join(ROOT_DIR, "scratch/part_1_metadata.json")
RECORDS_PATH = os.path.join(ROOT_DIR, "scratch/records_part1.json")

# Load existing metadata to get IDs, filenames, names, categories, tokens, word_count
with open(METADATA_PATH, "r", encoding="utf-8") as f:
    metadata_list = json.load(f)

# Define the detailed audit mapping for IDs 151 to 206
audit_map = {
    151: {
        "status": "Adopted & Highly Adapted",
        "description": "System prompt for creating custom AI agents with detailed specifications",
        "audit_details": "Defines instructions for designing agent personas, extracting core user intents, establishing clear behavioral boundaries, and optimizing system prompts for performance and self-verification.",
        "gemini_rationale": "Creating specialized subagents is fully supported in Google Antigravity SDK. Persona design and prompt structuring guidelines are directly relevant to writing clean system instructions for Gemini-based agents.",
        "gemini_strategy": "Adopt the architect instructions. Use them to guide the creation of custom subagents in Antigravity. Adapt the output schema to produce LocalAgentConfig instances instead of Claude-specific JSON definitions."
    },
    152: {
        "status": "Adopted & Highly Adapted",
        "description": "Classifies the tail of a background agent transcript as working, blocked, done, or failed and returns concise state JSON",
        "audit_details": "Provides guidelines for classifying background agent state based on conversational transitions. Distinguishes between completed tasks, waiting on external processes, blocked on user inputs, and failed runs.",
        "gemini_rationale": "The classification rules are model-agnostic and help manage asynchronous workflows. Antigravity can run background tasks and needs to monitor their status to know when to ping or resume.",
        "gemini_strategy": "Adopt the classifier schema and state transition rules. Integrate this classification logic into the Antigravity background task manager, mapping state JSON to notifications or task files."
    },
    153: {
        "status": "Adopted & Highly Adapted",
        "description": "Instructs the built-in background job agent to narrate progress, restate tool results, and emit explicit result, needs input, or failed status signals",
        "audit_details": "Instructs agents running in background mode to continuously narrate their actions, restate results in text, perform final checks, and output explicit signals: result:, needs input:, or failed:.",
        "gemini_rationale": "Antigravity background tasks require clear, parser-friendly status markers. Using standard indicators avoids parsing errors when monitoring runs.",
        "gemini_strategy": "Adopt the status indicators. Adapt 'result:', 'needs input:', and 'failed:' output tags to update task.md or write to the background task's telemetry file in the app data directory."
    },
    154: {
        "status": "Adopted & Highly Adapted",
        "description": "Instructions for generating clear, concise command descriptions in active voice for bash commands",
        "audit_details": "Specifies how to write active-voice, short descriptions for shell commands, keeping them under 10 words for standard tools and adding context for complex pipelines.",
        "gemini_rationale": "The Antigravity SDK displays summaries of proposed terminal commands to the user for approval. Having clear descriptions helps developers judge command safety.",
        "gemini_strategy": "Adopt the active voice style. Use this prompt in the Antigravity shell execution wrapper to summarize commands in the user approval dialogs."
    },
    155: {
        "status": "Adopted & Highly Adapted",
        "description": "System prompt for detecting command prefixes and command injection",
        "audit_details": "Contains rules for parsing command lines to identify their primary command prefix (e.g. git status, cat) and flags potential command injection attempts.",
        "gemini_rationale": "Detecting command injection and command prefixes is essential for Antigravity's security layer, since terminal execution requires user confirmation.",
        "gemini_strategy": "Adopt prefix detection logic. Use it in the command verification hook to confirm that requested terminal command matches the permission policy and contains no hidden injection patterns."
    },
    156: {
        "status": "Adopted & Highly Adapted",
        "description": "System prompt for the claude-guide agent that helps users understand and use Claude Code, the Claude Agent SDK and the Claude API effectively",
        "audit_details": "Configures a guide agent to answer questions about Claude Code features, config, MCP servers, the Agent SDK, and the API using specific documentation sources.",
        "gemini_rationale": "A guide agent is very useful for developers learning the Antigravity SDK and Gemini API. We can adapt this guide to help with Antigravity-specific components.",
        "gemini_strategy": "Adopt the guide agent structure. Replace Claude Code and Anthropic API documentation references with Google Antigravity SDK and Gemini API references, pointing to local markdown guides."
    },
    157: {
        "status": "Adopted & Highly Adapted",
        "description": "Low-effort /code-review prompt that reads the diff once and returns up to four hunk-visible runtime correctness findings",
        "audit_details": "Optimizes code review for speed and low cost by analyzing the diff once, ignoring test files, and outputting up to four runtime correctness bugs in a single-line format.",
        "gemini_rationale": "Varying code review effort levels matches Gemini's pricing/speed tradeoffs. A low-effort, high-speed mode is perfect for quick sanity checks during edits.",
        "gemini_strategy": "Adopt the single-pass diff review format. Map low-effort reviews to faster models (like Gemini 1.5 Flash) and enforce the 4-finding limit."
    },
    158: {
        "status": "Adopted & Highly Adapted",
        "description": "Extra-high and maximum-effort /code-review prompt that runs five finder angles, one-vote verification, a gap sweep, and capped JSON findings",
        "audit_details": "Details a deep multi-agent review pipeline: running 5 independent finder angles, verifying candidates using a single-vote metric, performing a gap sweep, and capping JSON findings.",
        "gemini_rationale": "Complex multi-step reasoning is supported by Antigravity using subagents. Multi-angle reviews maximize recall for critical releases.",
        "gemini_strategy": "Adopt the multi-step verification pipeline. Implement the 5 finder angles using parallel subagents, and use a coordinator to aggregate and verify findings."
    },
    159: {
        "status": "Adopted & Highly Adapted",
        "description": "Medium-effort /code-review prompt that favors precision with three finder angles, one-vote verification, and up to eight JSON findings",
        "audit_details": "Configures medium effort code review balancing speed and recall, utilizing 3 independent finder angles, verification, and outputting up to 8 JSON findings.",
        "gemini_rationale": "Medium effort is the default review mode. Balancing cost and precision fits Gemini 1.5 Pro's capabilities perfectly.",
        "gemini_strategy": "Adopt the medium-effort schema. Implement the 3 finder angles and verification pipeline using dynamic prompt structures and structured JSON output."
    },
    160: {
        "status": "Adopted & Highly Adapted",
        "description": "High-effort /code-review prompt that favors recall with three finder angles, recall-biased verification, and up to ten JSON findings",
        "audit_details": "Outlines high-effort review settings prioritizing recall over false positives, using 3 finder angles, recall-biased verification, and capping output at 10 findings.",
        "gemini_rationale": "High recall reviews are useful for security-sensitive or complex code changes. Using recall-biased verification reduces missed bugs.",
        "gemini_strategy": "Adopt the recall-biased verification rules. Set the coordinator's prompt to keep findings unless they are explicitly refuted by file content."
    },
    161: {
        "status": "Adopted & Highly Adapted",
        "description": "Optional /code-review instructions for posting findings as GitHub inline PR comments when --comment is passed",
        "audit_details": "Directs the agent to post inline code review comments to GitHub pull requests via MCP tools, falling back to the GitHub CLI or terminal prints.",
        "gemini_rationale": "Posting comments directly to GitHub PRs is highly useful for CI/CD integrations. Antigravity can use MCP or git tools to post PR feedback.",
        "gemini_strategy": "Adopt the PR commenting workflow. Map the inline comment tool calls to Antigravity's GitHub MCP server or the git/gh shell command execution."
    },
    162: {
        "status": "Adopted & Highly Adapted",
        "description": "System prompt for creating detailed conversation summaries",
        "audit_details": "Details rules for summarizing conversation history, focusing on user intents, developer decisions, files edited, errors, and security constraints within <analysis> tags.",
        "gemini_rationale": "Summarizing history is a core technique in Antigravity to manage large context windows. We must preserve details like function signatures and security rules.",
        "gemini_strategy": "Adopt the summarization guidelines. Use this prompt in the Antigravity compaction pipeline to generate rich context summaries before pruning messages."
    },
    163: {
        "status": "Adopted & Highly Adapted",
        "description": "System prompt for the general-purpose subagent that searches, analyzes, and edits code across a codebase while reporting findings concisely to the caller",
        "audit_details": "Instructs the general-purpose agent to search broadly, analyze architecture, edit files only when necessary, and avoid creating unnecessary docs or readme files.",
        "gemini_rationale": "General-purpose research and refactoring is a primary subagent type. The guidelines keep the agent focused and prevent bloat.",
        "gemini_strategy": "Adopt the research and editing guidelines. Use this as the base system instruction for the general-purpose subagent in Antigravity."
    },
    164: {
        "status": "Adopted & Highly Adapted",
        "description": "System prompt for evaluating hook conditions, specifically stop conditions, in Claude Code",
        "audit_details": "Guides evaluating whether conversation transcripts satisfy stop-conditions, outputting structured JSON with ok, reason, or impossible fields.",
        "gemini_rationale": "Evaluating complex stop conditions is useful for autonomous loop control. Antigravity can use this to decide if a task's success criteria have been met.",
        "gemini_strategy": "Adopt the JSON evaluation schema. Run this evaluator on the recent conversation logs when verifying task completion in continuous execution mode."
    },
    165: {
        "status": "Adopted & Highly Adapted",
        "description": "V2 instructions for generating prompt suggestions for Claude Code",
        "audit_details": "Defines instructions for predicting what a user might type next based on recent turns, enforcing conciseness and avoiding Claude-voice or evaluative suggestions.",
        "gemini_rationale": "Auto-suggesting next commands is a useful CLI interface feature. The formatting and voice constraints apply equally to a Gemini CLI.",
        "gemini_strategy": "Adopt the suggestion constraints. Adapt the predicted commands to suggest Antigravity-specific actions (e.g. running tests, committing, or checking task.md)."
    },
    166: {
        "status": "Adopted & Highly Adapted",
        "description": "Agent prompt used for summarizing recent messages",
        "audit_details": "Outlines instructions for summarizing only the recent turns of a conversation, using structured headers and analysis tags to capture files, code edits, and errors.",
        "gemini_rationale": "Incremental summarization is critical for token efficiency, summarizing only new blocks of messages and appending them to the global summary.",
        "gemini_strategy": "Adopt the incremental summarization flow. Inject this system prompt when summarizing the latest turns before context window compaction."
    },
    167: {
        "status": "Adopted & Highly Adapted",
        "description": "Subagent prompt for searching past Claude Code conversation sessions by scanning .jsonl transcript files and returning matching session IDs",
        "audit_details": "Configures a session search agent to grep through JSONL session transcripts and return a sorted JSON list of relevant session IDs.",
        "gemini_rationale": "Searching past conversation transcripts is a helpful feature for retrieving past decisions. Antigravity stores transcripts in a similar JSONL format.",
        "gemini_strategy": "Adopt the grep-search search pattern. Adapt the target directory to ~/.gemini/antigravity/brain/ and parse the resulting session UUIDs."
    },
    168: {
        "status": "Adopted & Highly Adapted",
        "description": "System prompt for the statusline-setup agent that configures status line display",
        "audit_details": "Instructs the status line agent to read zshrc/bashrc, extract the user's PS1 prompt configuration, and convert escape sequences to shell commands.",
        "gemini_rationale": "Helping users personalize their CLI status line or environment is a nice feature. Converting PS1 to plain command equivalents works similarly.",
        "gemini_strategy": "Adopt the PS1 conversion mappings. Use this agent configuration to support status line customization commands in the Antigravity CLI."
    },
    169: {
        "status": "Adopted & Highly Adapted",
        "description": "Prompt for agent that summarizes verbose output from WebFetch for the main model",
        "audit_details": "Directs summarizing fetched web page content, enforcing character limits on quotes, using quotes for exact language, and avoiding legal opinions or song lyrics.",
        "gemini_rationale": "Web pages can contain massive amounts of text. Summarizing them before putting them in the main context prevents context bloating and enforces licensing safety.",
        "gemini_strategy": "Adopt the licensing and quotation restrictions. Use this prompt in the web search/fetch wrapper to summarize HTML content before returning it to the coordinator."
    },
    170: {
        "status": "Adopted & Highly Adapted",
        "description": "System prompt for a forked worker sub-agent that executes a single directive from the parent agent and reports back concisely",
        "audit_details": "Guides worker forks to execute exactly one directive, refrain from spawning subagents, omit proposed next steps, and report results concisely without meta-commentary.",
        "gemini_rationale": "Workers are lightweight, single-turn tasks. Enforcing boundaries prevents workers from initiating infinite loops or wasting tokens.",
        "gemini_strategy": "Adopt the worker fork constraints. Set these system instructions when invoking subagents for single-turn code generation or test execution tasks."
    },
    171: {
        "status": "Adopted & Highly Adapted",
        "description": "GitHub Actions workflow template for triggering Claude Code via @claude mentions",
        "audit_details": "Provides a YAML workflow template that triggers a GitHub Runner on issue comments, PR comments, or issues containing the '@claude' keyword.",
        "gemini_rationale": "Running coding agents inside GitHub Actions allows automated PR handling. We can adapt this template to trigger Antigravity agents on '@gemini' or '@antigravity'.",
        "gemini_strategy": "Adopt the workflow triggers. Replace the Claude CLI call with the Antigravity CLI call, and customize the run commands to use Gemini API keys."
    },
    172: {
        "status": "Adopted & Highly Adapted",
        "description": "Template for PR description when installing Claude Code GitHub App integration",
        "audit_details": "Provides a markdown template explaining the purpose of the GitHub integration, how it works, and notes on how it processes PR comments.",
        "gemini_rationale": "Explaining CI integrations to team members is standard. The explanation can be updated to explain the Antigravity/Gemini integration.",
        "gemini_strategy": "Adopt the description layout. Replace references to Claude with Google Antigravity, and update links to point to the Antigravity documentation."
    },
    173: {
        "status": "Bypassed",
        "description": "Provides cURL and raw HTTP request examples for the Managed Agents API including environment, agent, and session lifecycle operations",
        "audit_details": "Lists detailed cURL command examples for managing environments, agents, and sessions on Anthropic's Managed Agents API, using beta headers.",
        "gemini_rationale": "Google Antigravity SDK does not use Anthropic's Managed Agents REST endpoints. It operates locally or uses Google Cloud Vertex/Vertex AI Agent Engine APIs.",
        "gemini_strategy": "Bypass the Anthropic cURL commands. Replace with Vertex AI Agent Builder or Agent Engine cURL examples for environment and session setup."
    },
    174: {
        "status": "Bypassed",
        "description": "Reference guide for using the Anthropic Python SDK to create and manage agents, sessions, environments, streaming, custom tools, files, and MCP servers",
        "audit_details": "Details Anthropic Python SDK bindings for the beta Managed Agents API, covering class initializations, session creations, and MCP server options.",
        "gemini_rationale": "The SDK bindings are specific to Anthropic. Google Antigravity uses its own SDK classes (e.g. LocalAgentConfig, Agent, runtime hooks) to configure agents.",
        "gemini_strategy": "Bypass the Anthropic SDK reference. Replace with the Google Antigravity SDK Python reference, demonstrating LocalAgentConfig and Agent instantiation."
    },
    175: {
        "status": "Bypassed",
        "description": "Reference guide for using the Anthropic TypeScript SDK to create and manage agents, sessions, environments, streaming, custom tools, file uploads, and MCP server integration",
        "audit_details": "Details Anthropic TypeScript SDK bindings for the beta Managed Agents API, covering session lifecycle, file uploads, and tool definitions.",
        "gemini_rationale": "Specific to Anthropic's TypeScript SDK and Managed Agents beta. Antigravity uses Python-based agent architectures and standard Node SDKs for simple chat.",
        "gemini_strategy": "Bypass the TypeScript Managed Agents SDK reference. Provide guides for creating local TypeScript agents using the Google Gen AI SDK or LangChain."
    },
    176: {
        "status": "Bypassed",
        "description": "Reference documentation for Managed Agents webhooks, including endpoint registration, signature verification, payload envelopes, supported event types, delivery behavior, and pitfalls",
        "audit_details": "Explains webhooks for receiving resource changes from Anthropic's Managed Agents, covering Console registration, signature verification, and SDK helpers.",
        "gemini_rationale": "Antigravity runs locally or uses standard cloud webhook events that do not use Anthropic's custom HMAC envelope or signing keys.",
        "gemini_strategy": "Bypass this document. If cloud-based triggers are needed, write standard Google Cloud Function or Pub/Sub event handlers to trigger agent runs."
    },
    177: {
        "status": "Adopted & Highly Adapted",
        "description": "Document on how to design prompt-building code for effective caching, including placement patterns and anti-patterns",
        "audit_details": "Explains prompt caching design principles: prefix matching, arranging prompts by stability (tools first, then system, then messages), and tracking breakpoints.",
        "gemini_rationale": "Gemini supports context caching (e.g., caching system instructions and tool definitions). The stability principles (static prefix caching) are highly applicable.",
        "gemini_strategy": "Adopt the caching design principles. Map the breakpoint guidelines to Gemini context caching, placing static tools and guidelines early in the prompt structure."
    },
    178: {
        "status": "Adopted & Highly Adapted",
        "description": "Template content for the user profile memory file, covering personal details, work context, schedule, and communication preferences",
        "audit_details": "Provides a markdown template for storing user details, including timezone, timezone work schedule, primary repo, and communication preferences.",
        "gemini_rationale": "Personalization is useful for developer agents. The template can be used in Antigravity's user profile memory to tailor agent responses.",
        "gemini_strategy": "Adopt the template fields. Save user profiles in ~/.gemini/antigravity/memory/profile.md and use them to initialize agent persona details."
    },
    179: {
        "status": "Adopted & Highly Adapted",
        "description": "Instructions for using computer-use MCP tools including tool selection tiers, app access tiers, link safety, and financial action restrictions",
        "audit_details": "Details tiers for using desktop control tools (computer use, Chrome MCP, dedicated MCPs), managing permission tiers (read/click/full), and link safety rules.",
        "gemini_rationale": "Operating systems and browsers can be controlled using computer use APIs. Enforcing access tiers and link safety is important for agent security.",
        "gemini_strategy": "Adopt computer use safety guidelines. Map tools to Antigravity's internal browser control or desktop OS tools, enforcing identical click/read restriction policies."
    },
    180: {
        "status": "Adopted & Highly Adapted",
        "description": "Instructions for debugging an issue that the user is encountering in the Claude Code session",
        "audit_details": "Guides debugging issues inside the CLI session itself, activating debug logging, reading settings file paths, and diagnosing startup or tool failures.",
        "gemini_rationale": "Debugging issues within the active agent session is useful. Antigravity agents can look at local log files to troubleshoot their own execution errors.",
        "gemini_strategy": "Adopt local debugging instructions. Map settings paths to ~/.gemini/antigravity/config.json and log files to ~/.gemini/antigravity/logs/session.log."
    },
    181: {
        "status": "Adopted & Highly Adapted",
        "description": "Skill definition for the /dream nightly housekeeping job that consolidates recent logs and transcripts into persistent memory topics, learnings, and a pruned MEMORY.md index",
        "audit_details": "Outlines a nightly reflection job (dream) that reads transcripts, extracts key decisions and lessons into topic files, resolves conflicts, and prunes the memory index.",
        "gemini_rationale": "Consolidating agent memory improves long-term accuracy and prevents context bloat. Running cleanups during off-hours is a great background pattern.",
        "gemini_strategy": "Adopt the dream consolidation pattern. Implement a cron task in Antigravity that runs memory consolidation scripts, compiling transcripts into key topics."
    },
    182: {
        "status": "Adopted & Highly Adapted",
        "description": "Analyzes session transcripts to extract frequently used read-only tool-call patterns and adds them to the project's .claude/settings.json permission allowlist to reduce permission prompts",
        "audit_details": "Analyzes logs to extract frequent read-only command prefixes and adds them to an allowlist to minimize user permission prompts while blocking unsafe wildcards.",
        "gemini_rationale": "Antigravity has a permission manager. Automatically generating permission grants based on past safe operations reduces interactive overhead.",
        "gemini_strategy": "Adopt the allowlist generation logic. Update settings targets to ~/.gemini/antigravity/permissions.json and map read-only command patterns to the allowed list."
    },
    183: {
        "status": "Adopted & Highly Adapted",
        "description": "Formats and displays the insights usage report results after the user runs the /insights slash command",
        "audit_details": "Formats the output of the session insights report, using a verbatim <message> block to display the shareable report URL and summary.",
        "gemini_rationale": "Displaying usage statistics and reports helps users track agent productivity. The formatting style is clean and directly reusable.",
        "gemini_strategy": "Adopt the message format. Map the insights data parsing to local Antigravity metrics, outputting the results in the CLI or web UI dashboard."
    },
    184: {
        "status": "Adopted & Highly Adapted",
        "description": "Example file for the Run app skill showing how to start a web dev server, drive it with chromium-cli, capture screenshots, and document app-specific gotchas",
        "audit_details": "Provides guidelines for launching dev servers in the background, polling ports, driving Chromium-cli for screenshots, and cleaning up processes.",
        "gemini_rationale": "Web application development often requires running and testing locally. Standard dev server management and headless screenshots are directly applicable.",
        "gemini_strategy": "Adopt dev server and headless browser guidelines. Ensure agents use standard shell commands to poll ports and run browser drivers for testing."
    },
    185: {
        "status": "Adopted & Highly Adapted",
        "description": "Example file for the Run app skill showing how to document building, invoking, and testing a CLI tool",
        "audit_details": "Outlines best practices for running and testing CLI tools, documenting PATH setups, representative invocations, expected exit codes, and stdin behavior.",
        "gemini_rationale": "Testing CLI tools is a common developer task. Having structured instructions for CLI run skills ensures consistent testing.",
        "gemini_strategy": "Adopt CLI testing guidelines. Apply this format when creating run scripts and task verification routines for CLI projects."
    },
    186: {
        "status": "Adopted & Highly Adapted",
        "description": "Example file for the Run app skill showing how to launch an Electron desktop app under xvfb and drive it through a Playwright REPL driver",
        "audit_details": "Provides a detailed workflow for running and driving GUI/Electron applications in headless environments using xvfb, Playwright REPL drivers, and screenshot captures.",
        "gemini_rationale": "Headless testing of GUI applications is a powerful capability. The architecture (xvfb + Playwright wrapper) allows the model to interact with native desktop apps.",
        "gemini_strategy": "Adopt the xvfb + Playwright driver architecture. Package the driver scripts in the Antigravity skill directory for projects requiring GUI test verification."
    },
    187: {
        "status": "Adopted & Highly Adapted",
        "description": "Template file for the Run skill generator showing the frontmatter and section structure for a project-specific run skill",
        "audit_details": "Provides a markdown template for writing project-specific run skills, including sections for prerequisites, target paths, dev servers, and drivers.",
        "gemini_rationale": "Templates ensure that custom skills written by the agent are consistent and complete. Using a standard structure improves skill reliability.",
        "gemini_strategy": "Adopt the skill template. Use this template when the agent generates new run skills or test drivers in the project's .gemini/skills/ directory."
    },
    188: {
        "status": "Adopted & Highly Adapted",
        "description": "Example file for the Run app skill showing how to drive an interactive terminal app with tmux, readiness polling, pane capture, key references, and cleanup",
        "audit_details": "Explains how to drive terminal user interface (TUI) apps inside a detached tmux session, sending keys, capturing pane output, and killing sessions.",
        "gemini_rationale": "TUIs block standard shell execution. Wrapping them in tmux allows the agent to interact with and test TUIs without locking the execution terminal.",
        "gemini_strategy": "Adopt the tmux wrapper pattern. When the agent needs to drive interactive CLIs (e.g. vim, custom REPLs), wrap execution in tmux commands."
    },
    189: {
        "status": "Adopted & Highly Adapted",
        "description": "A skill that guides Claude through a 7-step process to construct and verify hooks for Claude Code, ensuring they work correctly in the user's specific project environment",
        "audit_details": "Details a 7-step process for safe hook creation: checking duplicates, constructing command strings, test piping synthetic stdin payloads, writing JSON, and validating syntax.",
        "gemini_rationale": "Safely configuring environment settings and lifecycle events is important. Testing command strings with synthetic payloads avoids broken configurations.",
        "gemini_strategy": "Adopt the 7-step verification flow. Apply it to configuring Antigravity lifecycle events, verifying commands with mock inputs before writing to settings."
    },
    190: {
        "status": "Adopted & Highly Adapted",
        "description": "Example workflow for verifying a CLI change, as part of the Verify skill",
        "audit_details": "Guides verifying CLI changes by compiling the CLI, running with test arguments, capturing exit codes and outputs, and comparing with expected behavior.",
        "gemini_rationale": "Verifying changes via direct execution is a core test-driven step. Enforcing this workflow improves code correctness.",
        "gemini_strategy": "Adopt the verification pattern. When changes are made to a CLI command, run the build step and verify output flags before completing the task."
    },
    191: {
        "status": "Bypassed",
        "description": "Instructions for using the Advisor tool",
        "audit_details": "Directs the agent to call an advisor tool (backed by a stronger reviewer model) before major work, upon completion, or when stuck, weighting its advice highly.",
        "gemini_rationale": "Antigravity uses a direct model-to-system loop and has no dedicated external advisor model tool. Instead, complex steps are reviewed by standard subagents.",
        "gemini_strategy": "Bypass the advisor tool guidelines. Use standard invoke_subagent calls with a reviewer role to verify code changes instead of calling advisor()."
    },
    192: {
        "status": "Adopted & Highly Adapted",
        "description": "Instructions for including memory update guidance in agent system prompts",
        "audit_details": "Specifies how to add domain-specific memory update instructions to system prompts, telling agents what details to record (e.g. style conventions, database layouts).",
        "gemini_rationale": "Guiding agents on what to memorize prevents generic, useless notes. Specifying domain-specific memory keys makes agent recall highly relevant.",
        "gemini_strategy": "Adopt the memory prompt formatting. When creating custom subagents, inject a customized memory instructions block matching the subagent's domain."
    },
    193: {
        "status": "Adopted & Highly Adapted",
        "description": "Continuous task execution, akin to a background agent",
        "audit_details": "Commands the agent to execute tasks immediately, minimize user questions, prefer action, accept course corrections, and avoid destructive actions.",
        "gemini_rationale": "Continuous/auto execution is supported by Antigravity. Guidelines for making safe assumptions and avoiding data loss are critical for autonomous operations.",
        "gemini_strategy": "Adopt auto mode rules. Inject these behavioral constraints when the agent is running in continuous mode, restricting destructive file commands."
    },
    194: {
        "status": "Adopted",
        "description": "Guidelines for assisting with authorized security testing, defensive security, CTF challenges, and educational contexts while censoring requests for malicious activities",
        "audit_details": "Limits assistance to defensive security, CTF, and authorized research. Bans destructive hacks, DoS attacks, and evasion tools without authorization context.",
        "gemini_rationale": "Safety and alignment rules are critical. Gemini models follow strict safety policies regarding malicious activities and dual-use tools.",
        "gemini_strategy": "Adopt the safety boundaries. Ensure that security tasks are validated for authorization context and refuse destructive exploits."
    },
    195: {
        "status": "Adopted & Highly Adapted",
        "description": "Instructions for loading Chrome browser MCP tools via MCPSearch before use",
        "audit_details": "Instructs the agent to call ToolSearch with select:mcp__claude-in-chrome__<tool_name> before invoking browser tools.",
        "gemini_rationale": "Google Antigravity SDK pre-loads or dynamically registers MCP tools based on user permissions, so manual select search call flows are not strictly required.",
        "gemini_strategy": "Adopt the tool checking concept, but adapt it to use standard Antigravity tool discovery. Enforce checking tool availability via list_permissions or listing tools first."
    },
    196: {
        "status": "Adopted & Highly Adapted",
        "description": "Instructions for using Claude in Chrome browser automation tools effectively",
        "audit_details": "Provides guidelines for browser automation, including recording GIFs, console debugging with pattern filters, and handling blocking JS dialogs.",
        "gemini_rationale": "Browser automation is supported in Antigravity (using Chrome DevTools or similar). Proper console filtering and dialog management prevent session lockups.",
        "gemini_strategy": "Adopt the browser automation rules. Ensure browser agents use regex patterns for logs, create recordings of key flows, and dismiss alerts safely."
    },
    197: {
        "status": "Adopted & Highly Adapted",
        "description": "Instructs Claude to give brief, user-facing updates at key moments during tool use, write concise end-of-turn summaries, match response format to task complexity, and avoid comments and planning documents in code",
        "audit_details": "Restricts prose output: state approach in 1 sentence, give brief updates, write 1-2 sentence summaries, write minimal code comments, and avoid planning files.",
        "gemini_rationale": "Concise communication saves tokens and keeps the CLI clean. However, in Antigravity, we explicitly encourage writing structured plans to files like task.md.",
        "gemini_strategy": "Adopt the concise output and minimal code comments rules. Adapt the planning document rule: allow and encourage plan files (task.md) for multi-turn tasks."
    },
    198: {
        "status": "Adopted & Highly Adapted",
        "description": "Prompt used for context compaction summary (for the SDK)",
        "audit_details": "Directs writing a continuation summary for context compaction, covering Task Overview, Current State, Important Discoveries, and Next Steps.",
        "gemini_rationale": "Generating structured summaries is key for long agentic sessions. It allows new models to pick up the task without loading the entire raw history.",
        "gemini_strategy": "Adopt the summary structure. Use this exact schema when summarizing active subagent sessions in Antigravity before compiling them."
    },
    199: {
        "status": "Adopted & Highly Adapted",
        "description": "Field for describing _what_ the memory is. Part of a bigger effort to instruct Claude how to create memories",
        "audit_details": "Describes user memory contents: user role, goals, and knowledge, emphasizing personalization and avoiding negative judgments.",
        "gemini_rationale": "Personalization guidelines ensure that agent memory updates are respectful and professional, keeping notes useful for development.",
        "gemini_strategy": "Adopt user memory guidelines. Apply these constraints when writing user memory updates to the persistent ~/.gemini/antigravity/memory/ directory."
    },
    200: {
        "status": "Adopted",
        "description": "Allow users to complete ambitious tasks; defer to user judgement on scope",
        "audit_details": "Instructs the agent to defer to user judgment on task complexity, undertaking ambitious and complex tasks instead of refusing them.",
        "gemini_rationale": "Coding agents should be helpful and not artificially limit scope. Deferring to user judgment fits Antigravity's cooperative model.",
        "gemini_strategy": "Adopt verbatim. Do not reject tasks for being too large or complex; instead, decompose them into manageable subtasks using subagents."
    },
    201: {
        "status": "Adopted & Highly Adapted",
        "description": "How to inform users about help and feedback channels",
        "audit_details": "Directs the agent to point users to specific channels (e.g. email, GitHub issues, Slack) when they ask for help or want to provide feedback.",
        "gemini_rationale": "Guiding users to help channels is helpful. We need to point them to the Antigravity project repository or Google support portals.",
        "gemini_strategy": "Adopt. Replace Claude Code feedback channels with Google Antigravity project repositories and issue trackers."
    },
    202: {
        "status": "Adopted",
        "description": "Delete unused code completely rather than adding compatibility shims",
        "audit_details": "Instructs the agent to avoid compatibility hacks (like renaming unused vars or adding removed comments) and delete unused code entirely when safe.",
        "gemini_rationale": "Clean code is easier to maintain. Avoiding shims reduces code debt and improves project structure.",
        "gemini_strategy": "Adopt verbatim. When refactoring or deleting features, remove the unused code blocks completely rather than commenting them out."
    },
    203: {
        "status": "Adopted & Highly Adapted",
        "description": "Do not add error handling for impossible scenarios; only validate at boundaries",
        "audit_details": "Tells the model to avoid validation or error handling for internal guarantees, validating only at system boundaries (user input, external APIs).",
        "gemini_rationale": "Excessive error catching makes code verbose and hides logical bugs. Boundary-only validation keeps code clean.",
        "gemini_strategy": "Adopt. Apply this rule during code generation: validate parameters at public API entry points, but avoid try-catch blocks for internal logic."
    },
    204: {
        "status": "Adopted",
        "description": "Avoid introducing security vulnerabilities like injection, XSS, etc",
        "audit_details": "Directs the agent to avoid OWASP Top 10 vulnerabilities (command injection, SQL injection, XSS) and immediately fix insecure code.",
        "gemini_rationale": "Security is paramount for code generation. Gemini models must prioritize secure coding patterns.",
        "gemini_strategy": "Adopt verbatim. Enforce secure coding patterns, avoiding raw shell executions, unsanitized inputs, or insecure serialization in code changes."
    },
    205: {
        "status": "Adopted & Highly Adapted",
        "description": "Users primarily request software engineering tasks; interpret instructions in that context",
        "audit_details": "Directs the agent to interpret vague requests (e.g. rename a method) in a software engineering context by actually modifying files rather than just printing text.",
        "gemini_rationale": "CLI coding assistants are action-oriented. Requests should lead to file edits or shell executions in the workspace rather than conversational chat.",
        "gemini_strategy": "Adopt the software engineering context interpretation. Guide the model to use file-editing tools directly to satisfy user requests."
    },
    206: {
        "status": "Adopted & Highly Adapted",
        "description": "Instructions for when to fork subagents and rules against reading fork output mid-flight or fabricating fork results",
        "audit_details": "Specifies fork rules: qualitative criteria for forking, avoiding reading intermediate fork files, and not guessing/fabricating running fork results.",
        "gemini_rationale": "Antigravity subagents execute asynchronously. Preventing the parent from peeking at unfinished subagent files saves context and avoids race conditions.",
        "gemini_strategy": "Adopt the fork guidelines. Enforce that coordinator models wait for subagent message notifications rather than attempting to read subagent logs directly."
    }
}

# Construct records list
records_list = []
for meta in metadata_list:
    file_id = meta["id"]
    if file_id in audit_map:
        record = {
            "id": file_id,
            "filename": meta["filename"],
            "name": meta["name"],
            "category": meta["category"],
            "status": audit_map[file_id]["status"],
            "description": audit_map[file_id]["description"],
            "tokens": meta["tokens"],
            "audit_details": audit_map[file_id]["audit_details"],
            "gemini_rationale": audit_map[file_id]["gemini_rationale"],
            "gemini_strategy": audit_map[file_id]["gemini_strategy"]
        }
        records_list.append(record)

# Write to file
with open(RECORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(records_list, f, indent=2)

print(f"Successfully generated {len(records_list)} records in {RECORDS_PATH}")
