<!--
name: "Data: Sandbox filesystem disabled setting"
description: "Describes sandbox.filesystem.disabled behavior, platform limits, read-protection effects, and configuration precedence"
ccVersion: "2.1.324"
-->
Sandboxed commands get unrestricted read/write access to the host filesystem; network egress is still confined to network.allowedDomains. Intended for deployments whose goal is egress control rather than filesystem containment. Does not change Bash prompting: sandbox.autoAllowBashIfSandboxed is independent and still defaults to false, so sandboxed commands keep going through the permission flow unless it is set to true. Drops the read protection from filesystem.denyRead and credentials.files deny entries for sandboxed commands, since both are enforced by the filesystem layer this turns off; credentials.files mask entries (sentinel binds) and credentials.envVars deny/mask are unaffected. 
