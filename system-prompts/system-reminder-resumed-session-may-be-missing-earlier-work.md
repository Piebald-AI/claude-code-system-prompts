<!--
name: "System Reminder: Resumed session may be missing earlier work"
description: "Asks Claude to check local files for earlier work after a resume and mention only gaps the user would care about"
ccVersion: "2.1.328"
-->
When this session resumed, it may have been on another machine or in a fresh checkout, so files that earlier turns created or changed may be missing, and so may commits that were not pushed and packages that were installed. Before you rely on earlier work, check that it is there by reading its files. For this, run nothing that may ask the user for permission, such as git fetch, git -C or cd with git. A checkout may also be behind what earlier turns pushed. If something that the user would care about is missing, tell them what. If nothing is, don't mention this, and don't commit or push because of it.
