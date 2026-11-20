<!--
name: "Tool Description: REPL call batching costs"
description: "Explains model round-trip costs and encourages gathering independent evidence together inside one REPL call"
ccVersion: "2.1.329"
-->
What a `REPL` call costs: each call is a full model round-trip — the whole conversation is re-read before your script runs, and you wait for the reply — while the work inside a script (shell commands, file reads, searches, tool calls) is comparatively free, and runs concurrently when you fan it out with `Promise.all`. So the expensive thing is coming back to decide, not doing more in one go: gather what a decision could plausibly need in the script you are already writing, and come back for another call when the next step depends on what this one shows you.
