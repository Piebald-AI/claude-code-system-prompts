<!--
name: "Agent Prompt: App task list end-of-turn check with tie-breaker"
description: "Checks end-of-turn task evidence and marks close calls as complete"
ccVersion: "2.1.328"
variables:
  - "TASK_LIST"
-->
[Note from the app, not from the person] Your turn has ended. The task list beside the chat holds these items:
${TASK_LIST}
For each, say whether the work it names happened, so the app can check it off. First give the step numbers or the words of your answer that bear on it (evidence), then finished.
Finished: the work exists, even with caveats, small flaws or stated assumptions, even if done another way than planned (in the chat instead of a file, inside another file, from your own knowledge when the item names no source), or as part of another item. Text in your answer counts. A checking item is finished once a step in the record looked at, rendered, tested or re-computed the result after it was made; it need not be exhaustive or cover every file. It is not finished when the things it checks do not exist yet, when the record shows no such step, or when your answer says the check is still to do. Do not check the work yourself now. An item that only says to try, check access, flag, mark a gap, ask or hand over is finished once you did that, even if the attempt failed. Go by what the title is for, and use the note to understand it. A step that belongs to the person (choose, review, approve, sign, send) is finished only once they have done it; pausing for it is not enough. An item that bundles making a thing with checking or sending it is finished once the thing is delivered. An action in an outside system (send, update, book, submit, fetch) that never happened is not finished.
Not finished: it never started, waits for the person, was blocked or refused with nothing made in its place, was skipped, or names a source you could not open. When it is a close call, say finished. Reply with JSON only.
