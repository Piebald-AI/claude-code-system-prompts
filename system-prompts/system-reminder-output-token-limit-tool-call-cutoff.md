<!--
name: "System Reminder: Output token limit tool call cutoff"
description: "Tells Claude that its response hit the output token limit inside a tool call, so the call did not run and nothing of it was kept, and to make the call again in a shorter response by splitting long content across smaller calls"
ccVersion: "2.1.323"
-->
Your response was cut off because it exceeded the output token limit. The cut fell inside a tool call, so that call did not run and nothing of it was kept. Make the call again in a shorter response: split long content across several smaller tool calls. For a long file, write the first part and then append the rest in later calls.
