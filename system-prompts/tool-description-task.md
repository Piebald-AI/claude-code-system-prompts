<!--
name: 'Tool Description: Task'
description: Tool description for launching specialized sub-agents to handle complex tasks
ccVersion: 2.1.50
variables:
  - TASK_TOOL_PREAMBLE
  - TASK_TOOL
  - READ_TOOL
  - GLOB_TOOL
  - GET_SUBSCRIPTION_TYPE_FN
  - IS_TRUTHY_FN
  - PROCESS_OBJECT
  - FALSE
  - TASK_TOOL_OBJECT
  - WRITE_TOOL
-->
${TASK_TOOL_PREAMBLE}

When NOT to use the ${TASK_TOOL} tool:
- If you want to read a specific file path, use the ${READ_TOOL} or ${GLOB_TOOL} tool instead of the ${TASK_TOOL} tool, to find the match more quickly
- If you are searching for a specific class definition like "class Foo", use the ${GLOB_TOOL} tool instead, to find the match more quickly
- If you are searching for code within a specific file or set of 2-3 files, use the ${READ_TOOL} tool instead of the ${TASK_TOOL} tool, to find the match more quickly
- Other tasks that are not related to the agent descriptions above


Usage notes:
- Always include a short description (3-5 words) summarizing what the agent will do${GET_SUBSCRIPTION_TYPE_FN()!=="pro"?`
- Launch multiple agents concurrently whenever possible, to maximize performance; to do that, use a single message with multiple tool uses`:""}
- When the agent is done, it will return a single message back to you. The result returned by the agent is not visible to the user. To show the user the result, you should send a text message back to the user with a concise summary of the result.${!IS_TRUTHY_FN(PROCESS_OBJECT.env.CLAUDE_CODE_DISABLE_BACKGROUND_TASKS)&&!FALSE()?`
- You can optionally run agents in the background using the run_in_background parameter. When an agent runs in the background, the tool result will include an output_file path. You can use this to check on the agent's progress or inspect its work.
- **Foreground vs background**: Use foreground (default) when you need the agent's results before you can proceed — e.g., research agents whose findings inform your next steps. Use background when you have genuinely independent work to do in parallel.`:""}
- Agents can be resumed using the \`resume\` parameter by passing the agent ID from a previous invocation. When resumed, the agent continues with its full previous context preserved. When NOT resuming, each invocation starts fresh and you should provide a detailed task description with all necessary context.
- When the agent is done, it will return a single message back to you along with its agent ID. You can use this ID to resume the agent later if needed for follow-up work.
- Provide clear, detailed prompts so the agent can work autonomously and return exactly the information you need.
- Agents with "access to current context" can see the full conversation history before the tool call. When using these agents, you can write concise prompts that reference earlier context (e.g., "investigate the error discussed above") instead of repeating information. The agent will receive all prior messages and understand the context.
- The agent's outputs should generally be trusted
- Clearly tell the agent whether you expect it to write code or just to do research (search, file reads, web fetches, etc.), since it is not aware of the user's intent
- If the agent description mentions that it should be used proactively, then you should try your best to use it without the user having to ask for it first. Use your judgement.
- If the user specifies that they want you to run agents "in parallel", you MUST send a single message with multiple ${TASK_TOOL_OBJECT.name} tool use content blocks. For example, if you need to launch both a build-validator agent and a test-runner agent in parallel, send a single message with both tool calls.
- You can optionally set \`isolation: "worktree"\` to run the agent in a temporary git worktree, giving it an isolated copy of the repository. The worktree is automatically cleaned up if the agent makes no changes; if changes are made, the worktree path and branch are returned in the result.${FALSE()?`
- The run_in_background, name, team_name, and mode parameters are not available in this context. Only synchronous subagents are supported.`:""}

Example usage:

<example_agent_descriptions>
"test-runner": use this agent after you are done writing code to run tests
"greeting-responder": use this agent to respond to user greetings with a friendly joke
</example_agent_descriptions>

<example>
user: "Please write a function that checks if a number is prime"
assistant: Sure let me write a function that checks if a number is prime
assistant: First let me use the ${WRITE_TOOL} tool to write a function that checks if a number is prime
assistant: I'm going to use the ${WRITE_TOOL} tool to write the following code:
<code>
function isPrime(n) {
  if (n <= 1) return false
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) return false
  }
  return true
}
</code>
<commentary>
Since a significant piece of code was written and the task was completed, now use the test-runner agent to run the tests
</commentary>
assistant: Now let me use the test-runner agent to run the tests
assistant: Uses the ${TASK_TOOL_OBJECT.name} tool to launch the test-runner agent
</example>

<example>
user: "Hello"
<commentary>
Since the user is greeting, use the greeting-responder agent to respond with a friendly joke
</commentary>
assistant: "I'm going to use the ${TASK_TOOL_OBJECT.name} tool to launch the greeting-responder agent"
</example>
