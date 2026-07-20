<!--
name: "Data: Governed GitHub CLI shim routing"
description: "Shell routing logic for the governed gh shim, including GitHub host detection, real gh fallback execution, agent proxy settings, CA bundle configuration, and proxy-injected tokens"
ccVersion: "2.1.202"
variables:
  - "GITHUB_HOST"
  - "REAL_GH_PATH"
  - "AGENT_PROXY_URL"
  - "AGENT_PROXY_CA_BUNDLE_PATH"
-->
# non-github.com origin as a GHE signal. An EXPLICIT github.com host
# above skips the origin probe: it must not be kicked off the relay
# by the checkout heuristic.
rhost=''
if [ -n "$repo" ]; then
  case "$repo" in
    *://*) rhost="${repo#*://}"; rhost="${rhost%%/*}"; rhost="${rhost##*@}"; rhost="${rhost%%:*}" ;;
    */*/*) rhost="${repo%%/*}" ;;
  esac
elif [ -z "$host" ]; then
  origin="$(git config --get remote.origin.url 2>/dev/null || true)"
  case "$origin" in
    *://*) rhost="${origin#*://}"; rhost="${rhost%%/*}"; rhost="${rhost##*@}"; rhost="${rhost%%:*}" ;;
    *@*:*) rhost="${origin#*@}"; rhost="${rhost%%:*}" ;;
  esac
fi
rhost="$(printf %s "$rhost" | tr '[:upper:]' '[:lower:]')"
if [ -n "$rhost" ] && [ "$rhost" != '${GITHUB_HOST}' ]; then
  exec '${REAL_GH_PATH}' "$@"
fi
# NO_PROXY cleared: an ambient runner-host NO_PROXY covering
# github.com would make gh skip the relay and send the literal dummy
# token to the real GitHub API (hard 401).
HTTPS_PROXY='${AGENT_PROXY_URL}' https_proxy='${AGENT_PROXY_URL}' \
NO_PROXY='' no_proxy='' \
SSL_CERT_FILE='${AGENT_PROXY_CA_BUNDLE_PATH}' \
GH_TOKEN='proxy-injected' GITHUB_TOKEN='proxy-injected' \
exec '${REAL_GH_PATH}' "$@"
