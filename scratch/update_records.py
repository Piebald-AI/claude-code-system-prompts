import json

db_path = "prompts_db.json"
out_path = "scratch/records_subagent_run_51.json"

with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

targets = {257, 258, 259}
records = [p for p in db if p.get("id") in targets]

updates = {
    257: {
        "gemini_rationale": "In Google Antigravity SDK, agent behaviors and task flows are governed by specialized 'skills' (folders with SKILL.md, scripts, and examples) and custom subagents. When a long session runs and memory compaction ('Dreaming' or compaction loops) is triggered to reduce token usage, the original invocation history of these skills is compressed. However, the system must retain awareness of the guidelines from previously active skills to maintain consistent behavior. Providing this system reminder ensures that Gemini 3.5 remains aware of active skill guidelines from earlier in the session, preventing context loss while explicitly instructing the model not to repeat one-off initialization actions (like scheduling or file creation) or mistake historical inputs for new user commands.",
        "gemini_strategy": "Implement a post-compaction context-restoration hook within the Antigravity session orchestrator. When the session's chat history is compacted, the orchestrator reads the list of skills that were executed prior to the compaction point. It formats these skills' guidelines and parameters into the FORMATTED_SKILLS_LIST variable and injects this system reminder prompt. Gemini 3.5, with its advanced instruction-following capabilities, is explicitly instructed to treat the ## Input sections as read-only historical context. In the system prompt, this reminder is wrapped in strict XML tags (e.g., <historical_skills_context>) to delineate it from the current turn's active instructions, preventing the model from re-executing scripts or stateful setup procedures."
    },
    258: {
        "gemini_rationale": "Google Antigravity SDK projects can be run across distributed environments, shared workspaces, or cloned branches (using the branch or share workspace mode). When a session is resumed or transferred from another machine or workspace clone, the absolute paths, current working directory (CWD), or shell environment settings can change. For Antigravity and Gemini 3.5, this reminder is critical because the agent relies on absolute paths for all read/write file operations (per system rules) and runs shell commands that expect the correct CWD. If the CWD shifts without the model's awareness, relative paths will fail, and tool invocations will break.",
        "gemini_strategy": "Integrate a session-resume detector in the Antigravity environment auditor. Upon initiating a session or restoring it from serialized state, the SDK runs a check comparing the current CWD (retrieved dynamically via the GET_CWD_FN() function or equivalent Node/Python process API) and system hostname against the last-saved state. If a change is detected, the SDK prepends this session continuation system reminder to the first user turn. Gemini 3.5 will receive this reminder and must immediately adjust its internal state, update any cached file trees, and prioritize running path verification checks to ensure subsequent tool calls use the correct absolute paths."
    },
    259: {
        "gemini_rationale": "In Google Antigravity SDK, hooks (like pre-tool execution or post-tool execution checks, lint validators, and git commit hooks) are utilized to maintain workspace integrity. A 'stop hook' is executed at the end of a session or when preparing to conclude execution to ensure there are no lingering locks, syntax errors, or uncommitted files. If a command defined as a blocking stop hook fails (for instance, a lint command or a Git hook blocking on pre-commit check), the system must halt and return the error trace. Gemini 3.5 needs to receive this error message directly to understand exactly why the execution was blocked, identifying the specific hook command (HOOK_NAME) and its output, so it can diagnose and resolve the issue.",
        "gemini_strategy": "Implement stop-hook monitoring in the Antigravity task runner. When a task completes and the runner attempts to finalize execution, it runs all registered stop hooks. If a hook command returns a non-zero exit status, the runner intercepts the completion, generates a blocking error notification, and formats the output of the hook. This system reminder is then injected into the chat context. Gemini 3.5 is trained to recognize this error format, interpret the stack trace/stdout of the failed command, locate the offending code or configuration, fix the root cause, and then re-execute the stop/commit flow until all hooks pass successfully."
    }
}

for r in records:
    rid = r["id"]
    if rid in updates:
        r["gemini_rationale"] = updates[rid]["gemini_rationale"]
        r["gemini_strategy"] = updates[rid]["gemini_strategy"]

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2, ensure_ascii=False)
print("Done updating records")
