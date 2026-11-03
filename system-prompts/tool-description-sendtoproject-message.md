<!--
name: "Tool Description: SendToProject message"
description: "Describes posting one approved message as the user to a new or existing Claude Project without saving project memory or posting a setup card"
ccVersion: "2.1.318"
-->
A Claude Project is a cloud workspace on claude.ai/code: it has a coordinator and threads that do the work. This tool posts one message there as the user. It is the last step of /send-to-project and works only in the turn where the user ran that command themselves: anywhere else it refuses, so when the user wants this and has not run the command, tell them to run /send-to-project. Call it with the inputs the command gives. Its confirmation pane is where the user reads the message and decides, so do not paste the message into the conversation or ask for a go-ahead before calling.

What it does. The tool first shows the user its own confirmation pane, with the message, and it does nothing unless they choose Send. Then:
- Without `project_id` it creates a personal project under the name the command chose. If `attach_git_remote` is true it also adds this folder’s GitHub origin as the project’s repository, which it reads from git itself.
- With `project_id` it uses that existing project; nothing is created and no repository is added.
- Either way it posts the message in the project as the user, with this session’s Remote Control id under it, so the project can read the session when it needs detail. The project’s Claude answers it there. It saves nothing to project memory and posts no setup card. It needs Remote Control on for this session and refuses without it.

The inputs. `proposal` takes only `summary`, which is the message. When the user typed the message themselves, with the command or in the field it opened, the tool sends their words as typed and ignores `summary`, until they ask for a change. Otherwise write it in the user’s voice, in at most three plain sentences, with no secrets, tokens or credentials. If the user declines the pane, nothing was created or sent: when the rejection carries what they want changed, revise and call again; on a bare decline, stop. After a call that went through, do not call again in this run.
