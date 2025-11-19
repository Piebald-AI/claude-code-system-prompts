<!--
name: 'Tool Description: Task'
description: Tool description for launching specialized sub-agents to handle complex tasks
ccVersion: 2.0.14
variables:
  - AGENT_TYPE_REGISTRY
  - agentTypeEntry
  - propertiesText
  - runsInBackground
  - hasAccessToCurrentContext
  - TOOL_REGISTRY
  - READ_TOOL
  - GLOB_TOOL
  - TASK_TOOL
  - WRITE_TOOL
-->
Launch a new agent to handle complex, multi-step tasks autonomously. 

Available agent types and the tools they have access to:
${AGENT_TYPE_REGISTRY.map((agentTypeEntry)=>{let propertiesText="";if(agentTypeEntry?.runsInBackground||agentTypeEntry?.hasAccessToCurrentContext)propertiesText="Properties: "+(agentTypeEntry?.runsInBackground?"runs in background; ":"")+(agentTypeEntry?.hasAccessToCurrentContext?"access to current context; ":"");return`- ${agentTypeEntry.agentType}: ${agentTypeEntry.whenToUse} (${propertiesText}Tools: ${agentTypeEntry.tools.join(", ")})`}).join(`
`)}

When using the ${TOOL_REGISTRY} tool, you must specify a subagent_type parameter to select which agent type to use.

When NOT to use the Agent tool:
- If you want to read a specific file path, use the ${READ_TOOL.name} or ${GLOB_TOOL.name} tool instead of the Agent tool, to find the match more quickly
- If you are searching for a specific class definition like "class Foo", use the ${GLOB_TOOL.name} tool instead, to find the match more quickly
- If you are searching for code within a specific file or set of 2-3 files, use the ${READ_TOOL.name} tool instead of the Agent tool, to find the match more quickly
- Other tasks that are not related to the agent descriptions above


Usage notes:
- Launch multiple agents concurrently whenever possible, to maximize performance; to do that, use a single message with multiple tool uses
- When the agent is done, it will return a single message back to you. The result returned by the agent is not visible to the user. To show the user the result, you should send a text message back to the user with a concise summary of the result.
- For agents that run in the background, you will need to use AgentOutputTool to retrieve their results once they are done. You can continue to work while async agents run in the background - when you need their results to continue you can use AgentOutputTool in blocking mode to pause and wait for their results.
- Each agent invocation is stateless. You will not be able to send additional messages to the agent, nor will the agent be able to communicate with you outside of its final report. Therefore, your prompt should contain a highly detailed task description for the agent to perform autonomously and you should specify exactly what information the agent should return back to you in its final and only message to you.
- The agent's outputs should generally be trusted
- Clearly tell the agent whether you expect it to write code or just to do research (search, file reads, web fetches, etc.), since it is not aware of the user's intent
- If the agent description mentions that it should be used proactively, then you should try your best to use it without the user having to ask for it first. Use your judgement.
- If the user specifies that they want you to run agents "in parallel", you MUST send a single message with multiple ${TASK_TOOL.name} tool use content blocks. For example, if you need to launch both a code-reviewer agent and a test-runner agent in parallel, send a single message with both tool calls.

Example usage:

<example_agent_descriptions>
"code-reviewer": use this agent after you are done writing a signficant piece of code
"greeting-responder": use this agent when to respond to user greetings with a friendly joke
</example_agent_description>

<example>
user: "Please write a function that checks if a number is prime"
assistant: Sure let me write a function that checks if a number is prime
assistant: First let me use the ${WRITE_TOOL.name} tool to write a function that checks if a number is prime
assistant: I'm going to use the ${WRITE_TOOL.name} tool to write the following code:
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
Since a signficant piece of code was written and the task was completed, now use the code-reviewer agent to review the code
</commentary>
assistant: Now let me use the code-reviewer agent to review the code
assistant: Uses the ${TASK_TOOL.name} tool to launch the with the code-reviewer agent 
</example>

<example>
user: "Hello"
<commentary>
Since the user is greeting, use the greeting-responder agent to respond with a friendly joke
</commentary>
assistant: "I'm going to use the ${TASK_TOOL.name} tool to launch the with the greeting-responder agent"
</example>
