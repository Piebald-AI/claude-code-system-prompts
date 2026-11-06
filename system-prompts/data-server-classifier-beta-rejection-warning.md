<!--
name: "Data: Server classifier beta rejection warning"
description: "Explains an HTTP 400 rejection of server safety-check headers or fields, their suppression for the session and the setting that disables sending them"
ccVersion: "2.1.319"
-->
[server-classifier] a request was refused (HTTP 400), most likely because of the dangerous-tool-use beta header or the safeguards field. Claude Code sends these on a direct connection to api.anthropic.com even with CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS set. The API, or something between this machine and it, refused them. Until Claude Code restarts, it sends neither again, and auto mode no longer asks the server to check actions. To stop sending them on this machine at all, set CLAUDE_CODE_AUTO_MODE_SERVER=0.
