<!--
name: "Data: SDK ui_invalidate instances field"
description: "Documents the optional list of stale plugin UI instances that clients may redraw independently after state, fault or backdrop changes, with full redraw as the compatible fallback"
ccVersion: "2.1.323"
-->
@internal Present when a plugin wrote state (`$.state.set`) that these instances read while they were drawn, or a `Client` drawn in them failed and its plugin heard it (`ui.fault`), or the theme of the session was set or cleared, or a client of a surface that draws it joined where one ever stood (`$.theme.set` and `$.theme.clear`: on each such surface a `Theme` whose `instance_id` is `theme`, and one whose `instance_id` is `backdrop` where the scene changed or a client joined), and nothing else moved: only they are stale, and the surface may re-ask them alone. Absent, every mounted instance may be stale, as before. A surface that ignores the field re-asks everything and stays correct.
