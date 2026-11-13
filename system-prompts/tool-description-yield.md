<!--
name: "Tool Description: Yield"
description: "Describes the Yield tool for pausing until an asynchronous tool reports something, to be called only with no other work, including when it resumes and that it wakes shortly before the prompt cache would expire"
ccVersion: "2.1.323"
-->
Pause until one of your asynchronous tools reports something. Call it only when you have no other work. You resume as soon as a report or a message arrives (shown after the line that follows this call's result, before your next reply, unless that line says it waits for the end of your turn), at once if none of your asynchronous tools has anything under way that could produce a report, or when a tool you are waiting on reaches its own time limit. Also resumes shortly before the prompt cache would expire, with a line saying how many tasks are still running; call it again to keep waiting.
