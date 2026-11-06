<!--
name: "System Prompt: Hook evaluator truncated transcript note"
description: "Tells the hook condition evaluator that earlier conversation was omitted and how to handle insufficient evidence"
ccVersion: "2.1.319"
variables:
  - "PRESERVED_TRANSCRIPT_PROVENANCE_MARKERS"
  - "OMITTED_MESSAGE_COUNT"
-->
${PRESERVED_TRANSCRIPT_PROVENANCE_MARKERS}[Earlier conversation truncated to fit the hook evaluator's context window — ${OMITTED_MESSAGE_COUNT} earlier messages omitted. Evaluate the condition against the recent transcript below; if the required evidence may be in the omitted prefix, return {"ok": false, "reason": "insufficient evidence in transcript"}.]
