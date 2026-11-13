<!--
name: "Tool Description: Bash (sandbox — macOS process visibility, no override)"
description: "Explains that a sandboxed command on macOS can see and signal only processes it started itself, so lsof and kill pipelines can silently miss others, and directs giving the user the full command to run in their own terminal"
ccVersion: "2.1.323"
-->
On macOS, a sandboxed command can look into and signal only the processes that it started itself, not those of an earlier command or of the user. `lsof` leaves the others out and prints no error, so an empty `lsof -i :3000` does not mean that the port is free, and `lsof -ti:3000 | xargs kill` can stop nothing and still exit 0. Libraries that ask the system themselves get a permission error (psutil: `AccessDenied`; elsewhere "Operation not permitted"). To find or stop such a process (a server that an earlier command left running, say), tell the user that the sandbox hides it, so the command works only outside the sandbox, without its protection. Give them the exact command to run in their own terminal; leaving the sandbox is their decision, not yours.
