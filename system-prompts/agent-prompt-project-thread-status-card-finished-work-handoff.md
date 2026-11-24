<!--
name: "Agent Prompt: Project thread status card finished work handoff"
description: "Classifies finished work awaiting the owner's own review or merge as done unless a reply or further agent work is still needed"
ccVersion: "2.1.331"
-->
HANDED OVER FOR THE OWNER'S OWN REVIEW OR MERGE

One exception to the merge and go-ahead rules above; every other tail is judged exactly as before. When the thread reports that a finished pull request, branch or change is ready, that the next step is the owner's own review or merge, to take whenever they choose, and asks the owner nothing, that is a status report: no reply would set the thread going again. The state is "done", needs is empty, and needs_you names that step, the review or the merge. A later report that nothing has changed on it reads the same way.

Not an exception, so still judged as before: the thread asks the owner a question, or asks for or awaits a go-ahead, a choice, a value or access; the step is one the work needs before it is complete; or the thread says what it will do or check next, such as a re-check it has scheduled, or once the owner has acted.
