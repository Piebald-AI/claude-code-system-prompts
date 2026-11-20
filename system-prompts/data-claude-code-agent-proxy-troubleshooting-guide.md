<!--
name: "Data: Claude Code agent proxy troubleshooting guide"
description: "Troubleshooting guide for Claude Code's policy-enforcing HTTPS agent proxy, covering TLS trust setup, status checks, git, docker, and unsupported traffic"
ccVersion: "2.1.329"
variables:
  - "AGENT_PROXY_PORT"
  - "AGENT_PROXY_CA_BUNDLE_PATH"
  - "BASH_TOOL_NAME"
  - "AGENT_PROXY_STATE_DIR"
-->
# Claude Code agent proxy

Outbound HTTPS from this session goes through a local proxy at ${`http://127.0.0.1:${AGENT_PROXY_PORT}`}
(set via HTTPS_PROXY) which tunnels to a policy-enforcing egress proxy. TLS is
re-terminated there, so every tool must trust the CA bundle at
${AGENT_PROXY_CA_BUNDLE_PATH}. The standard CA environment variables, the system trust
store (where possible), a JVM truststore, the Bazel system bazelrc, the
browser NSS store, and gsutil's boto config are already set up.

## Quick diagnosis

1. Read the end of the failed command's output. When the proxy refused or lost
   a connection while a ${BASH_TOOL_NAME} command ran, Claude Code adds [agent-proxy] lines
   there with the host and the reason. A command that ran in the background,
   or whose exit status hides the failure (piped into another command, or
   followed by "|| true"), gets none.
2. Find the failure class below and apply the matching fix.
3. Never disable TLS verification, never unset HTTPS_PROXY, and do not retry
   policy denials (403/407) — report them instead.

## Failure classes and fixes

### "certificate verify failed" / "self-signed certificate in chain" / PKIX errors

The failing tool is not reading the pre-set CA configuration. In order:

- If the tool has a CA flag or env var, point it at ${AGENT_PROXY_CA_BUNDLE_PATH}
  (examples: --cacert, SSL_CERT_FILE, NODE_EXTRA_CA_CERTS, REQUESTS_CA_BUNDLE,
  AWS_CA_BUNDLE, DENO_CERT, CARGO_HTTP_CAINFO, PIP_CERT, GIT_SSL_CAINFO,
  BUNDLE_SSL_CA_CERT, HEX_CACERTS_PATH, NIX_SSL_CERT_FILE).
- Tool config files override environment variables. If one of these sets its
  own CA or disables verification, point it at the bundle instead:
  pip.conf "cert", npm "cafile" (npm config get cafile), ~/.curlrc "cacert",
  .wgetrc "ca_certificate", conda "ssl_verify", git "http.sslCAInfo",
  gradle.properties / MAVEN_OPTS "-Djavax.net.ssl.trustStore".
- JVM tools (Maven, Gradle, plain Java): when a JDK is present,
  JAVA_TOOL_OPTIONS points JVMs at a truststore that holds the proxy CA: the
  JDK's own store if the system trust install already added the CA there,
  otherwise ${AGENT_PROXY_STATE_DIR}/java-truststore.p12 (password "changeit"). Confirm
  that JAVA_TOOL_OPTIONS sets a trustStore before pointing a build at either:
  where it sets none, set-up was skipped, has not finished or has failed. If
  the image or the build sets its own trustStore, that one wins — import the
  proxy CA into it with
  keytool -importcert -noprompt -alias ccr-agent-proxy -file ${AGENT_PROXY_STATE_DIR}/agent-proxy-ca.crt -keystore <their store>
  or point the build at the ready-made one. Bazel reads the managed block in
  /etc/bazel.bazelrc rather than JAVA_TOOL_OPTIONS.

### "405 Method Not Allowed" from the proxy

The tool sent a plain-HTTP (non-CONNECT) request: usually axios older than
1.16.1 (upgrade it) or a tool configured with HTTP_PROXY (unset HTTP_PROXY for
that tool — only HTTPS_PROXY is supported).

### 403 / 407 from the proxy

Most often the destination host is not allowed for this session. Do not retry
or route around it — report the blocked host.
Note: curl hides response bodies on failed CONNECTs; the [agent-proxy] lines
give the host and, where the egress proxy answered one, the HTTP status.

### 429 / 503 from the proxy

Too many connections or requests went through the proxy, or the egress proxy
was busy. The proxy can hold a connection for about a minute before it refuses
it, so a tool with a short timeout of its own may report only a timeout. Run
fewer downloads or requests at once, then retry.

The proxy also answers 429 immediately when too many connections to it are open,
idle ones included (too_many_connections in the [agent-proxy] lines under a
failed command). Look for a program that opens connections and never closes
them. New connections work again once some have closed.

### 408 from the proxy

The tool opened a connection to the proxy and sent no complete request within 30
seconds, so the proxy closed it. Retry once. If it happens again, the tool opens
connections before it has a request to send, it is paused or short of CPU, or its
request never ends with an empty line in CRLF form (bare LF line ends, or another
protocol such as SOCKS).

### "connection reset" / "unexpected disconnect" / "RPC failed" mid-transfer

Once a tunnel is up the proxy cannot send an error response, so a connection
it aborts (tunnel to the egress proxy lost, or an upload the tunnel stopped
accepting) reaches the tool as a bare reset. The [agent-proxy] lines name the
host and reason; look for them before concluding the remote service refused the
operation.

### Tool ignores the proxy entirely (timeouts with no proxy error)

Some clients do not read HTTPS_PROXY: Node's built-in fetch (run that command
with NODE_USE_ENV_PROXY=1 on Node >= 22.21), aiohttp (pass trust_env=True),
Ruby bundler (reads only HTTP_PROXY, which this proxy does not serve),
hand-rolled Go dialers. Prefer the tool's own proxy option where one exists.

### git

SSH-form GitHub remotes (git@github.com:...) are rewritten to HTTPS
automatically unless this session has its own SSH setup or supplies its own
GIT_CONFIG_*. A gitconfig that sets http.proxy / http.<url>.proxy (even empty),
its own http.sslCAInfo, or an https-to-ssh insteadOf makes git bypass the proxy
or fail verification; adjust those keys for this session if git times out.

### docker build / docker run

Processes inside containers cannot reach 127.0.0.1:${AGENT_PROXY_PORT} and do not trust
the CA. Workarounds: run builds with --network host, copy ${AGENT_PROXY_CA_BUNDLE_PATH}
into the build context and install it in an early layer, and pass proxy/CA
settings explicitly to the build.

### Not supported through the proxy (report, do not work around)

gRPC / HTTP/2-only APIs, WebSocket upgrades, client-mTLS, certificate-pinned
clients (e.g. Snowflake, ngrok), non-443 HTTPS ports, raw-TCP databases.

If a tool still cannot work through the proxy, report it so the policy or
tooling can be fixed.
