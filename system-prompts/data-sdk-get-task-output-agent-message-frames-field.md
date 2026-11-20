<!--
name: "Data: SDK get_task_output agent message frames field"
description: "Describes the tool calls, results and narration sent as an agent's message frames and what the stream leaves out"
ccVersion: "2.1.329"
-->
The agent's messages in the order to show them, one content block each, in the form of a foreground agent's assistant and user messages: parent_tool_use_id and uuid are set. They are its tool calls, their results, and its words: a text block, or a thinking block that narration_block_indexes lists. Words are sent only just ahead of the next call of their response, and only if that call is sent, so a run's closing words are not; a run that ends without any can have a task_notification whose summary repeats words sent here. Also left out are what it was told, its reasoning, and SubagentHandback and StructuredOutput calls, which hold its report. Long texts are cut; images and tool_use_result are left out, citations and signatures are blanked.
