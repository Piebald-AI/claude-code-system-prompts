<!--
name: "Data: SDK model fallback api_refusal_cyber_verification field"
description: "Documents the API's Cyber Verification Program status on session-level cyber-refusal fallback notices, including multi-hop attribution and unknown-status handling"
ccVersion: "2.1.317"
-->
@internal Cyber Verification Program status of the account that made the request, as the API gave it for original_model: type, tier and reason of stop_details.cyber_verification. From the refusal that caused the switch (the first one, if the switch went through several models) or, when the API made the switch itself, from the turn's first refusal if the same model made it, so it may not belong to request_id. On a server-lane switch without streaming, one message can stand for several hops, and the status is then the first model's. Only on session-scope notices whose api_refusal_category is 'cyber'. Absent, or {type:'inactive'} with no reason, means unknown, not 'no access'. Map known values to your own text; never display them.
