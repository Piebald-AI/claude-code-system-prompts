<!--
name: "Data: SSL name constraint unsupported type explanation"
description: "Explains a certificate refusal caused by a certificate authority whose name constraint covers a kind of name the client cannot check, usually IP addresses, and how the server's operator can fix it with a different certificate or chain"
ccVersion: "2.1.323"
-->
A certificate authority in the server's chain limits the names that it may certify (a name constraint), and the limit covers a kind of name that this client can't check, usually IP addresses. This client refuses any certificate under such an authority that lists a name of that kind, whether or not the name fits. Whoever runs the server, proxy or gateway can fix this with a new certificate whose chain, including the trusted root, has no such limit, or with one that lists only DNS names that every authority in the chain allows, which clients must then use to reach the server.
