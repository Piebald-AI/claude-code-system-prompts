<!--
name: "Data: Gateway GovCloud upstream isolation warning"
description: "Gateway startup warning that developers can reach both GovCloud and other upstreams and recommends disjoint upstream groups and developer memberships to prevent conversations crossing that boundary"
ccVersion: "2.1.319"
variables:
  - "GOVCLOUD_UPSTREAM"
  - "OVERLAPPING_NON_GOVCLOUD_UPSTREAMS"
  - "NON_GOVCLOUD_UPSTREAM"
-->
upstream '${GOVCLOUD_UPSTREAM.name}' is in AWS GovCloud (its region starts with us-gov-), but developers it serves can also use these upstreams outside GovCloud: ${OVERLAPPING_NON_GOVCLOUD_UPSTREAMS.map((NON_GOVCLOUD_UPSTREAM)=>`'${NON_GOVCLOUD_UPSTREAM.name}'`).join(", ")}. Their whole conversation can go there without notice, for example when they pick a model served there, or when a request or token count for a model both serve fails and the gateway fails over. To keep each developer on one side, set groups on '${GOVCLOUD_UPSTREAM.name}' and on each upstream named here, so that no group is listed on both sides and no developer belongs to groups on both sides.
