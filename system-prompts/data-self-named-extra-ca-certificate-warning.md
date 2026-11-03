<!--
name: "Data: Self-named extra CA certificate warning"
description: "Explains why a self-named certificate from NODE_EXTRA_CA_CERTS was ignored and how to restore trust without blindly keeping every unverified certificate"
ccVersion: "2.1.318"
variables:
  - "CERTIFICATE_SHA256_FINGERPRINT"
-->
Claude Code ignored the certificate with SHA-256 fingerprint ${CERTIFICATE_SHA256_FINGERPRINT} in the NODE_EXTRA_CA_CERTS file: it names itself as its issuer, but Claude Code could not confirm that the certificate's own key signed it. Run Claude Code with --debug to write the certificate's subject and the cause to the debug log. If you do not know where the certificate came from, remove it from the file. If another root certificate of the same CA signed it, as when a CA renews its root with a new key, add the root that signed it to the file, if you still trust that root. If connections still fail, take that root out of the file again. Then, or if no other root signed it, set CLAUDE_CODE_DISABLE_SELF_NAMED_CERT_DROP=1, but only if you trust the ignored certificate, such as a self-signed root whose signature Claude Code cannot check or a server's own certificate. The variable keeps every certificate that Claude Code would ignore for this reason, whoever signed it, and can break connections that work without it.
