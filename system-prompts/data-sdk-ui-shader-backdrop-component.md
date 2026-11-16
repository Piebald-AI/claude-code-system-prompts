<!--
name: "Data: SDK UI Shader backdrop component"
description: "Internal SDK UI component for a GPU shader backdrop in a Theme answer, sent only to clients that draw Shader, carrying checked shader IR and its values with an Svg fallback child"
ccVersion: "2.1.326"
-->
@internal A backdrop the surface plays on its GPU, at most one, in the answer to a `Theme` ask under `backdrop`, and sent only to a client that names `Shader` in `ui_attach`'s `draws`; any other client is sent its Svg in its place. `ir` is the checked IR the engine compiled from the mod's shader file, which the surface checks again before it runs it, and `values` one number for each entry of `ir.values`, in that order: never source, a path or GLSL. `irHash` stands in place of `ir` where the ask's `held` names it. The one child is the Svg that shows wherever the shader does not run.
