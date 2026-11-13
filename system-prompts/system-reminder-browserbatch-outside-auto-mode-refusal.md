<!--
name: "System Reminder: BrowserBatch outside auto mode refusal"
description: "Tells Claude that nothing in a browser_batch ran because, outside auto mode, a batch may hold only same-tab read and interaction actions on an allowed site, and explains how to split out navigation and order the calls"
ccVersion: "2.1.323"
-->
Nothing in this call ran. Outside auto mode a browser_batch runs only if every action is a computer, find, form_input, get_page_text, read_page, read_console_messages, read_network_requests or javascript_tool call with the same tabId, and that tab shows a site that the user has allowed for this chat. If this batch holds another action, such as navigate, make that action its own call, and batch the actions before it and the actions after it separately. You can send these calls together in one reply: they run in order. But a later call still runs if an earlier one fails, so send a click, typing or a script only after you have the result of the navigate. If the actions name no tabId or different ones, correct that. If every action already fits, this batch can't run here: make each action its own call.
