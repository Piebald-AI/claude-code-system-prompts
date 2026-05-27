import json

with open("scratch/records_subagent1.json", "r") as f:
    records = json.load(f)

# Define the updates
updates = {
    1: {
        "gemini_rationale": "In Antigravity, we utilize Gemini Pro's massive 2M token context window, eliminating the need to isolate the planner in a separate docker container to save context. However, Gemini models are susceptible to instruction dilution when loaded with too much conversational prose or redundant warnings. This requires converting the detailed architectural principles into explicit directives and strict tool-usage policies.",
        "gemini_strategy": "We integrate these planning rules into the Antigravity `planning-and-verification` skill. To enforce the read-only boundary during exploration, the agent's write tools (`write_to_file`, `replace_file_content`, `multi_replace_file_content`) are disabled, and a `pre_tool_call_decide` hook blocks state-altering shell commands (like `touch`, `mkdir`, `git add`, `npm install`). We also register a post-turn validation hook that rejects the turn unless the response ends with the structured '### Critical Files for Implementation' section listing exactly 3-5 files."
    },
    2: {
        "gemini_rationale": "Without a structured gating pipeline, Gemini tends to skip exploration and immediately start editing source files, resulting in broken builds and redundant code. Enforcing a multi-phase workflow ensures that existing helpers and codebase conventions are identified before modification. The five planning phases are: Phase 1: Exploration (reading codebase, launching up to 10 parallel Explore agents), Phase 2: Design (proposing approaches, launching up to 3-5 parallel Plan agents), Phase 3: Review (reading critical files, verifying alignment, using AskUserQuestion), Phase 4: Final Plan (compiling the implementation plan file), and Phase 5: Approval (calling ExitPlanMode).",
        "gemini_strategy": "We implement the 5-phase planning flow directly in the Antigravity `planning-and-verification` skill. Since Antigravity does not spawn external subagent docker containers, Phase 1 (Exploration) and Phase 2 (Design) leverage Gemini Flash's parallel tool calling to run up to 10 codebase searches (`grep_search`, `list_dir`, `view_file`) simultaneously in a single turn. Write permissions are programmatically restricted exclusively to `implementation_plan.md` during Phases 1-4, and the user-facing QA gate is handled by the `ask_question` tool in Phase 3."
    },
    3: {
        "gemini_rationale": "Gemini frequently concludes planning turns with conversational text questions (e.g., 'Does this plan look good?') rather than programmatic tool calls. This halts automated scripts that rely on tool responses to proceed. Under the 5-phase model, Phase 5 requires calling a specific Exit tool to submit the plan for approval, preventing informal text-only transitions.",
        "gemini_strategy": "We enforce the approval gate in the agent's turn loop using the `post_turn` lifecycle hook. The hook scans the output for approval queries (e.g., 'Is this plan okay?', 'Should I proceed?'); if found without a corresponding call to `ExitPlanMode` or `ask_question`, the hook rejects the turn and returns a system error: 'You must call ExitPlanMode to submit the plan for approval or ask_question to clarify designs.'"
    },
    4: {
        "gemini_rationale": "Gemini models are prone to hallucinating paths and locations of active planning documents (e.g., creating `docs/plan.md` or `plan.md` at the root) if not given a specific path. In Phase 4, the final plan must be written to the exact designated planning file.",
        "gemini_strategy": "When plan mode is active, the Antigravity pre-turn hook reads the current content of `implementation_plan.md` from the local workspace and injects its absolute path and current contents into the system instructions under `[Active Plan File]`, ensuring the agent edits the correct file directly."
    },
    5: {
        "gemini_rationale": "Upon returning to plan mode after a rejection or modification request, Gemini can suffer from recency bias and forget the developer's original feedback, leading to the same rejected designs. It must know how to update the plan rather than rewrite it.",
        "gemini_strategy": "We mount the user's rejection comments and feedback history directly into the re-entry prompt. We configure the `ExitPlanMode` tool to calculate the hash of the plan file on re-entry; if the hash matches the exit hash, the tool call fails with a validation error, forcing the agent to modify the plan before submitting."
    },
    6: {
        "gemini_rationale": "Launchings separate, isolated subagent containers for simple read-only code exploration incurs significant startup latency. Gemini's native parallel tool execution handles multi-file grepping and directory listing much faster than serial subagent dispatch.",
        "gemini_strategy": "We bypass the Explore subagent. Instead, the main agent runs exploration using parallel calls to `grep_search`, `list_dir`, and `view_file` (up to 10 in a single turn). The prompt's thoroughness directives ('quick', 'medium', 'very thorough') are mapped directly to query parameter limits in the tool definitions."
    },
    7: {
        "gemini_rationale": "LLM agents often default to running unit tests or typecheck scripts rather than validating the runtime behavior of their changes. Verification must happen at the user-facing 'surface' (CLI, API socket, Web GUI) to prevent undetected integration failures. Relying strictly on mock environments can miss critical integration bugs.",
        "gemini_strategy": "We implement these rules in our custom `verification` skill. The SDK inspects git diffs using `git log --oneline` and `git diff` to determine the change scope. It prioritizes executing local Python verification scripts (stored in `scratch/test_verify.py`) over generic test runners. If no verifier script is found, the agent is forced to perform a 'cold start' verification by launching the service and using `curl` to assert responses, writing stdout/stderr verbatim to `walkthrough.md`."
    },
    8: {
        "gemini_rationale": "Reinforces task discipline by reminding the agent of its planned verification recipe right before completing the task. The verification recipe from the final plan (Phase 4) must be followed precisely.",
        "gemini_strategy": "When the agent enters the validation state, the Antigravity lifecycle hook parses `implementation_plan.md`, extracts the verification recipe, and appends it to the system instructions: 'Run the exact Verification Recipe defined in your approved plan and capture the outputs.'"
    },
    9: {
        "gemini_rationale": "Claude's JavaScript-based verifier skill setup is complex and introduces heavy prompt overhead. Gemini is highly proficient at writing clean Python scripts, enabling a simplified verifier creation process.",
        "gemini_strategy": "We simplify the verifier creation instructions. The agent is directed to create a standalone Python script under `scratch/test_verify.py` that handles port acquisition (scanning for free ports), boots the service as a subprocess, runs test requests, asserts JSON schemas, and terminates the subprocess on exit."
    },
    10: {
        "gemini_rationale": "Scanning diff hunks from multiple concurrent 'angles' running in parallel containers is inefficient. Gemini Pro's long context window allows auditing all three angles simultaneously. The three finder angles are: Angle A: Line-by-Line diff scan of enclosing functions (checking for inverted conditions, off-by-one, null derefs, missing awaits, wrong-variable copy-paste, unescaped regex); Angle B: Removed-behavior auditor (mapping deleted code to invariants and finding where they are re-established); Angle C: Cross-file tracer (grepping call sites of modified functions to check signature/precondition breaks).",
        "gemini_strategy": "We combine the three finder angles into a single prompt for our `code-review` tool hook. When a PR or commit is analyzed, the hook passes the diff along with full source files to Gemini Pro, instructing the model to audit all three angles and return findings in a structured markdown table. The analysis runs locally as a python package rather than invoking a separate docker container."
    },
    11: {
        "gemini_rationale": "Code reviewers are prone to reporting false positives by overlooking adjacent guards. Enforcing a strict 3-state classification forces the model to look for counter-proofs before flagging a bug. Bugs are classified as: CONFIRMED (proven error), PLAUSIBLE (state-dependent/speculative), or REFUTED (proven impossible due to types or adjacent guards).",
        "gemini_strategy": "We embed the CONFIRMED, PLAUSIBLE, and REFUTED classification directly in the schema of our code review tool. The reviewer must cite the exact file and line of the counter-proof or guard logic before classifying any potential bug as REFUTED, which prevents lazy filtering of real edge cases."
    },
    12: {
        "gemini_rationale": "For security audits, catching suspicious edge cases (high recall) is more critical than avoiding false positives. In standard reviews, precision is favored to avoid developer alert fatigue. Under high recall-bias, speculative findings are retained as PLAUSIBLE unless explicitly disproved.",
        "gemini_strategy": "We expose a `sensitivity_mode` parameter in the Antigravity code review configuration. In `recall_bias` mode, we append the recall-biased verification prompt, instructing the model to classify ambiguous bugs as PLAUSIBLE rather than refuting them, ensuring potential security escapes are flagged."
    },
    13: {
        "gemini_rationale": "Claude's system uses a local `.claude` memory index with kebab-case YAML/frontmatter markdown files (slug, description, metadata type: user|feedback|project|reference). Managing dozens of tiny files introduces massive listing and retrieval overhead. Gemini's attention works best on large, coherent documents.",
        "gemini_strategy": "We consolidate local workspace memories into three key files: `user_profile.md` (preferences), `past_corrections.md` (successful build/test fixes), and `project_scope.md` (context/constraints). The pre-turn hook mounts these files into the context as structured markdown blocks. We keep the frontmatter schema (name, description, type metadata) for compatibility but eliminate the fragmented file layout."
    },
    14: {
        "gemini_rationale": "In Claude Code, a synthesizer subagent reads selected memory Markdown files and compiles a JSON array of up to 7 discrete, highly relevant facts. Launching a separate subagent for this is an optimization for small context windows that adds significant latency under Gemini's 2M context window.",
        "gemini_strategy": "Bypassed. We eliminate the synthesis step entirely. The Antigravity loader reads the consolidated memory files directly from disk and mounts them in the context, allowing Gemini Pro to perform direct, in-context semantic retrieval over the entire memory profile without a synthesis model."
    },
    15: {
        "gemini_rationale": "Running a selector subagent to scan a `MEMORY.md` manifest and select a maximum of 5 files to load adds API latency. Gemini's context window can easily ingest the entire memory directory, making selector agents redundant.",
        "gemini_strategy": "Bypassed. The Antigravity loader reads all markdown files from the workspace memory directory locally in Python and appends them to the context, removing the selector agent and eliminating the latency of the pre-session analysis."
    },
    16: {
        "gemini_rationale": "Consolidation must happen offline to prevent active session latency. Running the 4-phase dreaming cycle (Orient, Signal Extraction from session logs, Consolidation of topic files, and Pruning/indexing of the MEMORY.md manifest under 150 lines and 25KB) keeps memory updated without blocking developer interaction.",
        "gemini_strategy": "We implement the 4-phase dreaming cycle as a background cron task managed by the Antigravity `schedule` tool or triggered at session shutdown. The task reads append-only session logs (`logs/YYYY/MM/DD/`) and updates the consolidated memory files. The index `MEMORY.md` is updated programmatically to ensure it stays within size limits."
    },
    17: {
        "gemini_rationale": "Memory indices must be kept clean to avoid conflicting guidelines. Collapsing duplicate files requires finding '*.md' memories, deleting redundant copies, and merging them. The combined file must copy the oldest `created:` timestamp from the source frontmatter to maintain correct manifest sorting.",
        "gemini_strategy": "The background dreaming task executes a self-pruning prompt on `past_corrections.md` and `user_profile.md`, merging duplicate preference rules, resolving contradictions against the codebase, and keeping the oldest creation timestamps to preserve chronology."
    },
    18: {
        "gemini_rationale": "Workspace rules (like CLAUDE.md) are the authoritative source of truth. Consolidated memories must be checked against them to prevent the agent from developing deviating rules. Contradictions must be resolved or flagged to the user.",
        "gemini_strategy": "During the background dreaming cycle, the agent reconciles memory files against the workspace `CLAUDE.md` or `.cursorrules`. Contradictory memories are pruned, and critical contradictions are flagged in a start-up warning, ensuring personal memory does not bypass repo guidelines."
    },
    19: {
        "gemini_rationale": "Personal agent sessions should not delete or corrupt shared team memory assets (`memory/team/`), protecting collaborative rules in shared environments. Team memories are conservative and require codebase contradiction to be deleted.",
        "gemini_strategy": "The consolidation script enforces strict boundaries: write access is restricted on `memory/team/` paths. Shared team memories are treated as read-only during personal dreaming cycles and can only be modified via explicit PR review."
    },
    20: {
        "gemini_rationale": "Compaction is rarely triggered under Gemini's 2M context window. When it does trigger (at 85% capacity), it is critical to copy all user safety limits, restricted operations, and sensitive files verbatim inside the summary (specifically Section 6) to prevent security policy leakage in subsequent turns.",
        "gemini_strategy": "We implement a sliding window compaction hook. The compaction handler extracts conversation history, constructs a structured summary (Intents, Concepts, Files, Errors, Problem Solving, All user messages, Pending tasks, Work Completed), and appends a `[🛡️ VERBATIM SAFETY CONSTRAINTS]` block containing all active directory blocks and tool restrictions verbatim."
    },
    21: {
        "gemini_rationale": "Informs the agent that the conversation history has been compacted so it knows to orient on the newly injected summary block for current context, preventing it from hallucinating past context.",
        "gemini_strategy": "The compaction reminder header is prepended to the system prompt in the turn immediately following a history compaction, directing the agent to rely on the compaction summary."
    },
    22: {
        "gemini_rationale": "Ensuring clear citations of loaded memory sources helps prevent hallucinations and tracks the source of preferences.",
        "gemini_strategy": "The memory loader prepends `[Memory Source: memory/<filename>.md]` headers to each attached memory block in the context."
    },
    23: {
        "gemini_rationale": "Namespace conflicts must be avoided when personal and team memories share names or rules.",
        "gemini_strategy": "We format nested or team memories with explicit directory headers: `[Team Source: memory/team/<filename>.md]`."
    },
    24: {
        "gemini_rationale": "Invoking an LLM to audit every single action adds significant latency (3-5s). Hard boundaries can be instantly validated in local Python code.",
        "gemini_strategy": "Bypassed as an LLM call. We implement the security monitor as a Python hook registered at `hooks.pre_tool_call_decide`. The hook analyzes command strings and intercepts shell injections (`&&`, `;`, `||`, `$()`) and path escapes in 0ms."
    },
    25: {
        "gemini_rationale": "High-risk actions like force-pushing or accessing production environments should be blocked programmatically rather than depending on LLM judgment.",
        "gemini_strategy": "Bypassed as an LLM call. The hard block and soft block threat matrix is coded directly into the `pre_tool_call_decide` filter, immediately blocking `git push --force` or `kubectl` commands and raising permission validation prompts."
    },
    26: {
        "gemini_rationale": "Gemini is prone to using shortcuts (like bypassing checks with `--no-verify` or force-pushing) to finish tasks quickly. Forcing caution around destructive and hard-to-reverse actions maintains codebase integrity.",
        "gemini_strategy": "Adopted and adapted. The guidelines are injected into the agent system prompt. In addition, the Antigravity `run_command` tool hook programmatically intercepts commands with `--no-verify` or `git reset --hard` and prompts the user for explicit confirmation."
    },
    27: {
        "gemini_rationale": "Gemini models sometimes omit or hide test errors to make their execution appear successful. Factual reporting of outcomes is essential.",
        "gemini_strategy": "Enforced in verification hooks. The agent is instructed to write stdout/stderr of execution and test runs verbatim to `walkthrough.md`. The file edit tools verify target content before replacing, raising validation errors on mismatch."
    },
    28: {
        "gemini_rationale": "Conflicting rules in safety configurations can cause unexpected locks or security escapes.",
        "gemini_strategy": "Adopted and simplified. When custom safety rules are modified (e.g. in `.cursorrules` or `.gemini/safety.json`), Antigravity executes a validation check during startup to verify that they do not conflict with the system's hard blocks."
    },
    29: {
        "gemini_rationale": "Runaway loops in background cron jobs can list directories endlessly and cause excessive API consumption if not capped. The coordinator must act as a steward of existing work (CI failures, unresolved threads) and stop after 3 consecutive idle checks.",
        "gemini_strategy": "The autonomous execution engine tracks empty runs. If 3 consecutive background ticks result in 'no modifications or actions needed', the engine shuts down the session. Git status and SCM PR threads are checked programmatically using git and SCM APIs to avoid redundant LLM calls."
    },
    30: {
        "gemini_rationale": "For persistent loops (CLAUDE_CODE_LOOP_PERSISTENT), the agent must persistently wait and check adjacent branches, sibling PRs, and re-read original task framing rather than exiting after 3 idle ticks, favoring local exploration over shutdown.",
        "gemini_strategy": "When `persistent_loop=True` is enabled in the configuration, the idle check handler is modified. Instead of halting after 3 empty loops, the agent enters a 'broaden' state, checking sibling branches, fetching unresolved review comments, and verifying deferred items."
    },
    31: {
        "gemini_rationale": "If a tool call is blocked by a safety monitor, the agent should degrade gracefully (e.g., using specialized read tools instead of shell commands) rather than attempting to tunnel commands through other tools.",
        "gemini_strategy": "When the `pre_tool_call_decide` hook blocks a tool execution, the error message returned to the agent includes these graceful degradation instructions, prompting the model to use safer alternatives or stop and ask."
    },
    32: {
        "gemini_rationale": "Sandbox isolation parameters are best managed at the environment level rather than relying on LLM parameters.",
        "gemini_strategy": "Replaced by Python hooks. Unsandboxed command execution requires explicit approval from the developer via the interactive SDK prompt, removing the need for `dangerouslyDisableSandbox: true` prompt logic."
    },
    33: {
        "gemini_rationale": "The execution tool's error response should explain the failure details directly so the model does not have to guess.",
        "gemini_strategy": "Replaced by Python hooks. The Antigravity `run_command` tool wrapper catches permission errors and returns a structured message specifying the restricted boundary. Since Antigravity does not use the `/sandbox` command, that reference is bypassed."
    },
    34: {
        "gemini_rationale": "Sleep commands in scripts block execution threads and waste API call turns. The agent should run immediate checks or use background tasks instead.",
        "gemini_strategy": "Adopted and enforced. In the system prompt, sleeping in loops is prohibited. In addition, the shell tool hook blocks commands containing sleep durations over 2 seconds, instructing the model to use background tasks or event-driven checks."
    }
}

updated_count = 0
for r in records:
    rid = r["id"]
    if rid in updates:
        r["gemini_rationale"] = updates[rid]["gemini_rationale"]
        r["gemini_strategy"] = updates[rid]["gemini_strategy"]
        updated_count += 1

with open("scratch/records_subagent1.json", "w") as f:
    json.dump(records, f, indent=2)

print(f"Successfully updated {updated_count} records in scratch/records_subagent1.json")
