<!--
name: "Data: Steward security plugin setup guidance"
description: "Tells the user how to move a security plugin outside the checkout, verify its marketplace and install or enable the user-level copy before restarting the watch"
ccVersion: "2.1.331"
variables:
  - "IS_SETTINGS_SOURCE_ENABLED_FN"
  - "PLUGIN_ID"
-->
To watch: (1) If the settings of this checkout or of an --add-dir folder declare this plugin's marketplace, take it out of them. (2) If the plugin's folder lies inside the checkout or a folder added with --add-dir, move it out. ${IS_SETTINGS_SOURCE_ENABLED_FN("userSettings")?`(3) From outside any checkout: first check in /plugin's Marketplaces tab that the row claude-plugins-official names the GitHub repository anthropics/claude-plugins-official (the tab shows no branch or path). If it names another, don't install. Then, if the plugin isn't installed for you at user scope, run /plugin install ${PLUGIN_ID} and pick "Install for you (user scope)", which takes the plugin anew from that repository. If it is installed, but switched off, switch it on in /plugin. Then start Claude Code again in this checkout (don't resume a session). Installing it checks nothing that is named above, and if this project has an install of another version, that one still loads here`:"(3) This session doesn't read your own settings (as with --setting-sources without user), so an install for you changes nothing here. Start a session that reads them, and run the command again"}
