<!--
name: "Agent Prompt: App task list interrupted turn check"
description: "Checks which tasks were already complete when a turn was cut short"
ccVersion: "2.1.328"
variables:
  - "INTERRUPTED_TURN_NOTES"
  - "INTERRUPTION_KIND"
  - "TASK_LIST"
-->
[Note from the app, not from the person] ${INTERRUPTED_TURN_NOTES[INTERRUPTION_KIND]} The work was cut off partway. The task list beside the chat holds these items:
${TASK_LIST}
For each, say whether the work it names was already complete at the last step, so the app can check it off. First give the step numbers that bear on it (evidence), then finished.
Finished: the work exists in complete form, even with caveats or small flaws left to polish, even if done another way than planned or as part of another item. An item about asking or handing over is finished once you asked or handed over. A step that belongs to the person (choose, review, approve, sign, send) is finished only once they have done it; pausing for it is not enough.
Not finished: it never started, you were still in the middle of it (a script written but not run, an outline with parts missing, an error not yet fixed), it waits for the person, or it was blocked, refused or skipped. A checking item is finished only when everything it covers existed, was checked after its last change, and the last check showed nothing more to fix. Reply with JSON only.
