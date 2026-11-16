<!--
name: "Data: SDK ui_message control request"
description: "Internal SDK control request for a post from a desktop-drawn Client instance, which runs the owning plugin's ui.message chain, or for a Theme click that runs the theme plugin's ui.pointer hooks"
ccVersion: "2.1.326"
-->
@internal A post from a `Client` instance the desktop drew: runs the owning plugin's `ui.message` chain alone (origin `client`) with `surface: "desktop"`. One naming a Client the latest ui_render of that instance did not carry answers `{handled: false}`; data past the bounds errors. One whose `component` is `Theme` is a click on the backdrop instead, `data` `{ type: "click", x, y }` with `x` and `y` 0 to 1 from the top left: it runs the `ui.pointer` hooks of the plugin that set the theme, and answers `{handled: false}` when `plugin` is not that one.
