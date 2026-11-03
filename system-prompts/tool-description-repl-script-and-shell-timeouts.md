<!--
name: "Tool Description: REPL script and shell timeouts"
description: "Explains the synchronous script lifetime, the shorter timeout needed for long shell commands and how timed-out commands may continue as background tasks"
ccVersion: "2.1.318"
-->
A script is stopped 600000 ms after it starts, counting the time spent waiting on permission prompts, and a command still running then is stopped too and its output is lost. So give a long command a timeout that ends well before that. At its own timeout a command moves to the background and keeps running (one that starts with sleep is stopped instead, and so is every command if background tasks are disabled): the await resolves without throwing, with exitCode null, and running names the task and the file its output streams to, so read that file instead of running the command again.
