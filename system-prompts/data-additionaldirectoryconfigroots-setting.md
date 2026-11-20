<!--
name: "Data: additionalDirectoryConfigRoots setting"
description: "Maps added folders to the checkout whose skills, commands, agents and plugin settings they read"
ccVersion: "2.1.329"
-->
@internal For the program that starts Claude Code only: read from --settings and from settings that program sends while the session runs; ignored in settings files. Maps an added folder (--add-dir, or a claim's additional_directories) by its absolute path, also matched by its real path, to the absolute path of the checkout whose .claude skills, commands, agents and plugin settings that folder then reads instead of its own; file access stays with the folder. Full contract, with when to send it and what makes a root unusable: apps/cli/docs/desktop-host-contract.md, entry additionalDirectoryConfigRoots.
