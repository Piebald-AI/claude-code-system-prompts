<!--
name: "Data: SDK reload_plugins refuse_if_busy field"
description: "Documents the reload_plugins option that rejects a reload while the session has active work and the capability hosts use to detect support"
ccVersion: "2.1.324"
-->
When true, a request that finds the session busy reloads nothing and gets an error whose error_code is reload_plugins_busy; ask again once the session is idle. Busy: a turn is running or still ending, a message is queued for one, a permission prompt taken over from an earlier process is unanswered, background work that keeps the session at running (an agent, a workflow and the like) is live, or an in-process teammate is at work; a session that only waits for a background shell command is not busy. For a host whose request can arrive late, such as one that reaches the session over SSH: a reload changes the commands, agents, hooks and servers under a running turn, agent or teammate. Default false: the request is served in a turn too. Only `claude -p` reads it, and says so in system/init.capabilities (reload_plugins_refuse_if_busy_v1) to a host on its pipes; a CLI that does not say so may ignore the field.
