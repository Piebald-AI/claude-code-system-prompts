<!--
name: "Data: Self-named CA certificate drop debug guidance"
description: "Logs the fingerprint, subject and verification failure of a dropped self-named CA certificate and describes the trust-chain and override recovery options"
ccVersion: "2.1.318"
variables:
  - "CERTIFICATE_SHA256_FINGERPRINT"
  - "JSON_OBJECT"
  - "CERTIFICATE_SUBJECT"
  - "CA_CERTIFICATE_RECORD"
-->
CA certs: Dropped the certificate with SHA-256 fingerprint ${CERTIFICATE_SHA256_FINGERPRINT} and subject ${JSON_OBJECT.stringify(CERTIFICATE_SUBJECT??"")}: it names itself as its issuer, but ${CA_CERTIFICATE_RECORD.unconfirmed}, and no CA that chains to a root in the CA list signed it. If another root certificate of the same CA signed it, this one stays once this list holds that root certificate too. Only the lists for Claude Code's own connections take certificates from the NODE_EXTRA_CA_CERTS file. If you add that root and connections still fail, take it out again: while this list holds it, the variable below changes nothing. CLAUDE_CODE_DISABLE_SELF_NAMED_CERT_DROP=1 keeps every such certificate, whoever signed it, and can break connections that work without it.
