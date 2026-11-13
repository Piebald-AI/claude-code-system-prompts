<!--
name: "Data: askUserQuestionTimeout setting"
description: "Describes the setting for how long Claude's questions wait in the terminal before auto-continuing with the answers selected so far, how the desktop and web apps move on from unanswered questions, and which sessions and settings files ignore it"
ccVersion: "2.1.323"
-->
Idle time before Claude's questions in the terminal auto-continue with any answers selected so far. When unset, the terminal does not auto-continue. The Claude desktop and web apps show Claude's questions in their own interface and may move on from some unanswered ones after a wait the app sets. Claude is then told that nobody answered and uses its best judgment. In sessions that read this setting, only "never" stops the apps from moving on. Leaving it unset does not. Cloud sessions and Cowork tasks do not read your user settings file (~/.claude/settings.json), and managed settings do not reach all of them. This setting is ignored in a project's settings files.
