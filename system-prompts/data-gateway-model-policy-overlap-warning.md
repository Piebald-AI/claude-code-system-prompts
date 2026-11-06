<!--
name: "Data: Gateway model policy overlap warning"
description: "Gateway startup warning that family or prefix matching lets other managed policies use a custom model and recommends group-restricted upstreams or a nonmatching model name"
ccVersion: "2.1.319"
variables:
  - "GATEWAY_MODEL"
  - "EXPLICIT_MODEL_POLICY_PATHS"
  - "OTHER_MATCHING_MODEL_POLICY_PATHS"
-->
model '${GATEWAY_MODEL.id}' is listed by name in availableModels of ${EXPLICIT_MODEL_POLICY_PATHS.join(", ")}, but developers under ${OTHER_MATCHING_MODEL_POLICY_PATHS.join(", ")} can use it too. An availableModels entry can also match ids that it does not name: a family word such as opus matches ids with that word in them and, unless availableModelsMatch is exact, a model name matches ids that begin with it. If this model is meant only for the policies that list it, map it only to upstreams that set groups, which serve only the IdP groups they list, or rename it so that no other policy's entries match it.
