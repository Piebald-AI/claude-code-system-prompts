<!--
name: "Data: SDK ui_invalidate event"
description: "Documents plugin UI invalidation events, redraw scope, evaluation deduplication and per-plugin notification coalescing"
ccVersion: "2.1.318"
-->
@internal Fire-and-forget push from the hooks engine when a plugin called `$.ui.invalidate("ui.render")`, a plugin loaded or reloaded, or a mobile client already known to the session named a field in `draws` it had not named before: every tree a remote surface drew through ui_render may be stale. The surface re-asks each mounted instance; the engine dedups the evaluations. Bumps from one plugin fold to at most one per 100 ms. With `instances`, a state write or a `Client` that failed made only those stale.
