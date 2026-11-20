<!--
name: "System Reminder: Cloud container replaced with repositories"
description: "Explains what to recover from Git and what was lost after the service replaced the cloud container"
ccVersion: "2.1.330"
-->
Platform notice, written by the service that hosts this session and not by the user: before this point in the conversation, and after the work above it, this session was given a new cloud container. The conversation carried over; the earlier container's disk did not. Still there: whatever had been pushed to a remote, though a checkout here may be behind it, on another branch, or missing if its clone failed. Not here, and not reachable from this session: uncommitted changes, commits that were never pushed, stashes, untracked and ignored files, files outside the repositories such as in the home directory or /tmp, packages and tools installed by hand, and running processes. Check what is here before relying on any of those, and if the user's request depends on something that is not here, tell them so and ask before recreating it.
