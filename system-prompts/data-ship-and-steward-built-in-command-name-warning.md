<!--
name: "Data: Ship and steward built-in command name warning"
description: "Explains a name collision with a built-in command, how to run the custom alternative, and why the user must repeat the command before it starts"
ccVersion: "2.1.331"
variables:
  - "HIDDEN_CUSTOM_COMMAND_NAME"
  - "USER_WATCH_COMMAND"
  - "PLURALIZE_FN"
  - "SAME_NAME_COMMANDS"
  - "CUSTOM_COMMAND_INVOCATIONS"
  - "IS_SHIP_COMMAND"
-->
Nothing started. ${HIDDEN_CUSTOM_COMMAND_NAME!==void 0?`A custom /${HIDDEN_CUSTOM_COMMAND_NAME} isn't loaded, because Claude Code has a built-in command of that name. To use the custom one, rename it, then restart Claude Code.`:`${USER_WATCH_COMMAND} is a command built into Claude Code. ${PLURALIZE_FN(SAME_NAME_COMMANDS.length,"Another command here has","Other commands here have")} that name too: ${CUSTOM_COMMAND_INVOCATIONS.length===0?`type / to find ${PLURALIZE_FN(SAME_NAME_COMMANDS.length,"it in the menu, under a longer name","them in the menu, under longer names")}`:`to run ${PLURALIZE_FN(SAME_NAME_COMMANDS.length,"that one","one of those")}, type ${CUSTOM_COMMAND_INVOCATIONS.join(" or ")}`}.`} The built-in ${USER_WATCH_COMMAND} ${IS_SHIP_COMMAND?"commits and pushes your work and opens a pull request as you, if there is none yet, then reviews it and watches it":"watches your open pull request and pushes fixes to it as you"}. To run it, type the same line again.
