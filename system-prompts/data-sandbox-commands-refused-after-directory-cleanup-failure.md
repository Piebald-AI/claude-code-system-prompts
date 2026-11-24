<!--
name: "Data: Sandbox commands refused after directory cleanup failure"
description: "Explains why commands are refused when Claude Code cannot leave a directory and how to recover"
ccVersion: "2.1.331"
-->
Sandboxed commands are refused: Claude Code could not leave a folder that it should have left, and the sandbox would let commands write there. This can happen when the disk is full, and a sandboxed command may have caused it. Freeing space does not lift this. Restarting does, and moving the session to a folder other than the one it is in usually does. Running outside the sandbox (dangerouslyDisableSandbox) is refused too, so retrying will not help. `!` commands and commands excluded from the sandbox in settings still run.
