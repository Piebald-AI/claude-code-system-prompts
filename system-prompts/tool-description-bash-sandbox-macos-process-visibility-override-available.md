<!--
name: "Tool Description: Bash (sandbox — macOS process visibility, override available)"
description: "Explains that a sandboxed command on macOS can see and signal only processes it started itself, so lsof and kill pipelines can silently miss others, and directs retrying outside the sandbox while telling the user why"
ccVersion: "2.1.323"
-->
On macOS, a sandboxed command can look into and signal only the processes that it started itself, not those of an earlier command or of the user. `lsof` leaves the others out and prints no error, so an empty `lsof -i :3000` does not mean that the port is free, and `lsof -ti:3000 | xargs kill` can stop nothing and still exit 0. Libraries that ask the system themselves get a permission error (psutil: `AccessDenied`; elsewhere "Operation not permitted"). To find or stop such a process (a server that an earlier command left running, say), retry as described above for a sandbox-caused failure, and tell the user in the same message that the sandbox hides other processes and that the retry runs without its protection.
