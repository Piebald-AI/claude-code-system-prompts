<!--
name: "System Reminder: Project document file rewrite without current text refusal"
description: "Refuses replacing a project doc from a local file without its whole current text in view, requires project_read before revising the file, and forbids deleting or rewriting from a partial read"
ccVersion: "2.1.319"
-->
Write refused; nothing in the project was changed. A doc is already at this path, and this tool cannot tell that the file holds a change to its current text: this conversation holds no project_read that showed or saved the whole of that current text, no earlier project_write of it from a file, and no copy of it shown to you. Call project_read on this path. If it shows the text, or saves the whole doc to a file, make your change from that text, write the file again, and repeat this project_write. If it says that only part of the doc was saved or shown, do not repeat this write: tell the user that this doc could not be rewritten from here. Do not delete the doc to write it afresh: a delete cannot be undone here.
