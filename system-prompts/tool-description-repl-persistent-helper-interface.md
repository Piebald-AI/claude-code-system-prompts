<!--
name: "Tool Description: REPL persistent helper interface"
description: "Describes the persistent JavaScript helper interface, batching costs, returned and logged output, asynchronous execution and generated helper and tool declarations"
ccVersion: "2.1.319"
variables:
  - "REPL_TOOL_ACCESS_GUIDANCE_BLOCK"
  - "REPL_OUTPUT_TRUNCATION_NOTE"
  - "REPL_OUTPUT_DELIVERY_GUIDANCE_BLOCK"
  - "REPL_PERMISSION_MODE_TIMEOUT_NOTE"
  - "REPL_BATCHED_OPERATIONS_EXAMPLE"
  - "BUILD_REPL_HELPER_DECLARATIONS_FN"
  - "FORMAT_REPL_TOOL_TYPE_DECLARATIONS_FN"
  - "GET_REPL_TOOL_SCHEMAS_FN"
  - "AVAILABLE_TOOLS"
  - "TOOL_PERMISSION_CONTEXT"
  - "MCP_SERVER_DISCOVERY_GUIDANCE_BLOCK"
  - "GIT_WORKFLOW_GUIDANCE_BLOCK"
-->

${REPL_TOOL_ACCESS_GUIDANCE_BLOCK}

The REPL is one persistent JavaScript context: variables and functions you define in one call are there in the next, so keep results in variables (`const out = await $`…`.text()`) instead of re-reading a file or re-running a command whose output you already hold. Those variables last between calls, but not across a restart, a resume, a fork or a wake: the first result after one of those says so. Top-level `await` works. There is no `import`, `require` or `process`: the context is sealed, and the globals below are how it reaches the machine. The REPL language is always JavaScript, whatever the codebase is written in — run the codebase's own tools (pytest, cargo, go test, …) with `$`.

What a `REPL` call costs: each call is a full model round-trip — the whole conversation is re-read before your script runs, and you wait for the reply — while the work inside a script (shell commands, file reads, searches, tool calls) is comparatively free, and runs concurrently when you fan it out with `Promise.all`. So the expensive thing is coming back to decide, not doing more in one go: gather what a decision could plausibly need in the script you are already writing, and come back for another call when the next step depends on what this one shows you.

A script's output is its last expression's value plus anything it `self.log(...)`s along the way. What it returns is added to your context and stays there; the value itself stays in the REPL whether you return it or not. So return what you want to read now, and keep the rest in variables to slice or search later.${REPL_OUTPUT_TRUNCATION_NOTE} Promise values inside a returned object are awaited for you (`({status: $`git status`, branches: $`git branch`})` needs no awaits); a promise used inline — concatenated, interpolated, passed to another call — needs `await`. `console.*` goes to a bounded in-memory ring rather than into your context; `console.tail(n)` reads it back.

To keep a long output out of your context, return `preview(out)` or `preview(out, 2000)` instead of the output itself: it gives the first characters, and when `out` is an awaited `$` result (not its `.text()` string) whose output the shell tool saved to a file, it starts with the output's size and the file's path.
${REPL_OUTPUT_DELIVERY_GUIDANCE_BLOCK}${REPL_PERMISSION_MODE_TIMEOUT_NOTE}
${REPL_BATCHED_OPERATIONS_EXAMPLE}
## Declarations
${await BUILD_REPL_HELPER_DECLARATIONS_FN({agent:H,isBash:c,asyncLane:T,mcpThrows:s,tools:FORMAT_REPL_TOOL_TYPE_DECLARATIONS_FN(await GET_REPL_TOOL_SCHEMAS_FN(AVAILABLE_TOOLS,TOOL_PERMISSION_CONTEXT))})}
${MCP_SERVER_DISCOVERY_GUIDANCE_BLOCK}${GIT_WORKFLOW_GUIDANCE_BLOCK?`
${GIT_WORKFLOW_GUIDANCE_BLOCK}
`:""}
