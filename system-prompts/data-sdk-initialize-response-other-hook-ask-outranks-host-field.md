<!--
name: "Data: SDK initialize response other_hook_ask_outranks_host field"
description: "Documents when an SDK initialize reply reports support for giving other PreToolUse hooks priority over hooks registered by the spawning host"
ccVersion: "2.1.321"
-->
@internal True on an initialize reply that goes over the pipes of the host that spawned this CLI, from a CLI that ranks another PreToolUse hook's ask above the host's own: where a hook that this host registered asks, and any other hook asks on the same call, the can_use_tool request carries the other hook's reason, whichever finished first. A plugin's hooks module may still re-word an ask, and a hook may copy the host's words (docs/desktop-host-contract.md D65a). Absent for a remote client, whose hooks are never the host's own, in a Cowork cloud session or a Code cloud worker, and on CLIs that predate it, which may send the host's own reason even when another hook asked: there a host must not take its own reason to mean that nobody else asked.
