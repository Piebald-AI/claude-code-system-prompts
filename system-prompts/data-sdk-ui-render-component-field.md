<!--
name: "Data: SDK ui_render component field"
description: "Describes the internal ui_render field naming what to draw, including the Theme component that the engine answers itself with the standing colors, color scheme override and still backdrop, and the Backdrop component drawn by a mod's hook"
ccVersion: "2.1.324"
-->
@internal What to draw, or `Theme`, the session's theme, by `instance_id`. Under `theme` and `image:<id>:<n>` no hook draws: the engine answers itself, `props` of `plugin` with whichever of `colors`, `overrideColorScheme` and a still `backdrop` stands, or `data`, `index`, `of`, `hash` and `bytes` for a piece of an image, to `desktop` and `mobile`, and `{}` with none standing, with a scene and no `colors`, under another id or to any other surface. Under `backdrop` a mod's `ui.render` hook for `Backdrop` draws the scene that stands, with `props` of `scene`, `plugin`, `glass` and `overrideColorScheme` where a plugin said it.
