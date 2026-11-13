<!--
name: "Data: Sandbox unchecked protected paths warning"
description: "Warns that unchecked protected paths disable project-supplied filesystem grants and directs the user to remove unexpected links or use user settings"
ccVersion: "2.1.324"
variables:
  - "UNCHECKED_PROTECTED_PATHS"
-->
[Sandbox] ${UNCHECKED_PROTECTED_PATHS.join(", ")} (among the paths Claude Code itself keeps from sandboxed commands) could not be checked without following a link that may lead to another computer, or could not be checked at all. While that is so, no sandbox filesystem grant from the project's settings files is applied: sandbox.filesystem.allowRead and allowWrite, additionalDirectories, and Edit allow rules as write roots, from .claude/settings.json and .claude/settings.local.json (a remembered /add-dir lands there), or from a Windows registry policy key the user can write. Grants from your user settings, administrator-managed settings and the command line still apply. If a link on that path is not one you or your administrator made, remove it; otherwise put the grants you need in your user settings.
