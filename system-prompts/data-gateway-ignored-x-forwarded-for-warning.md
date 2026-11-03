<!--
name: "Data: Gateway ignored X-Forwarded-For warning"
description: "Gateway startup warning that an X-Forwarded-For header was ignored because the requesting address is not covered by listen.trusted_proxies, and what to configure when a load balancer or ingress fronts the gateway"
ccVersion: "2.1.318"
variables:
  - "CLIENT_ADDRESS"
  - "TRUSTED_PROXIES_LIST"
-->
request from ${CLIENT_ADDRESS} carried an X-Forwarded-For header, but ${TRUSTED_PROXIES_LIST.length===0?"listen.trusted_proxies is not set":`${CLIENT_ADDRESS} is not in listen.trusted_proxies`}, so the gateway ignored the header and used ${CLIENT_ADDRESS} as the client address. If ${CLIENT_ADDRESS} is your load balancer or ingress, every developer behind it shares one sign-in rate limit (rate_limits), and access_control and audit events see only that address. List its source range, and nothing wider, in listen.trusted_proxies only if it adds the connecting address to the header itself, or if clients can reach it only through another proxy that does. If it only passes on what clients send, listing it lets them fake their address and get past access_control and rate_limits. Have it add the address before you list it, or raise rate_limits instead. If developers connect to the gateway directly and something on their side adds the header, nothing needs to change. Logged once per start, however many requests are affected.
