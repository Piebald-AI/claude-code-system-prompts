<!--
name: "Data: SDK initialize response hook_on_failure_supported field"
description: "Documents the initialize capability confirming hook matcher onFailure support and the host checks needed to avoid silently accepting failed blocking hooks"
ccVersion: "2.1.317"
-->
True on every initialize reply from a CLI that honors `onFailure` on hook matchers. Absent on CLIs that predate the option, which ignore it (a failed callback set to "block" lets the action run), and from responders that do not run the host's hooks. A host that sets "block" must not go on without it; the TypeScript SDK refuses the session. It says nothing of this request's hooks: `hooks_applied` does, and the TypeScript SDK also refuses a first initialize that reads `hooks_applied: false` when a matcher sets "block".
