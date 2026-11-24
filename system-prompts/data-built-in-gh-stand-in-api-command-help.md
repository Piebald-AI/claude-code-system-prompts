<!--
name: "Data: Built-in gh stand-in api command help"
description: "Usage text for Claude Code's built-in gh stand-in, which supports only gh api REST requests to GitHub hosts through the session's GitHub proxy, listing its flags and how {owner}, {repo} and {branch} placeholders are filled in"
ccVersion: "2.1.331"
variables:
  - "BUILT_IN_GH_CLIENT_DESCRIPTION"
  - "NO_GITHUB_CLI_REASON"
  - "ALLOWS_ANY_GITHUB_HOST"
  - "DEFAULT_GITHUB_HOST"
  - "ADDITIONAL_GITHUB_HOSTS"
  - "ALLOWS_ADDITIONAL_GITHUB_HOSTS"
  - "TEXT_FILE_INPUT_GUIDANCE"
-->
Usage: gh api <endpoint> [flags]

This gh is ${BUILT_IN_GH_CLIENT_DESCRIPTION}:
${NO_GITHUB_CLI_REASON}.
${ALLOWS_ANY_GITHUB_HOST?`It makes GitHub REST API requests to ${DEFAULT_GITHUB_HOST}, or to the GitHub Enterprise
host of this checkout's remote (or --hostname <host>), through this session's
GitHub proxy, which supplies the credential for the hosts and repositories this
session is connected to, and has no other gh command.`:`It makes GitHub REST API requests to ${[DEFAULT_GITHUB_HOST,...ADDITIONAL_GITHUB_HOSTS].join(", ")} through this session's GitHub
proxy, already authenticated, and has no other gh command.`}
A GitHub CLI installed during the session takes this one's place once it is on
PATH. On a self-hosted runner that one has only the GitHub credentials the
runner's operator provides and does not go through this session's GitHub proxy.

Flags:${ALLOWS_ADDITIONAL_GITHUB_HOSTS?`
      --hostname <host>     GitHub host of the request${ALLOWS_ANY_GITHUB_HOST?"":", as GH_HOST"} (default ${DEFAULT_GITHUB_HOST}, or the
                            host of the repository that fills {owner}, {repo} in the endpoint)`:""}
  -X, --method <method>     HTTP method (default GET, or POST with parameters or --input)
  -f, --raw-field key=value String parameter
  -F, --field key=value     Typed parameter: true, false, null and integers become JSON
                            values, {owner} {repo} {branch} are filled in, @file reads a
                            file, @- reads standard input
  -H, --header 'Name: v'    Request header
      --input <file>        File to send as the request body (- for standard input)
  -i, --include             Print the response status line and headers
      --paginate            Follow the response's rel="next" links (GET only)
  -q, --jq <expression>     Filter the response with jq (needs jq on PATH; without it, pipe the
                            output to a JSON tool that is installed)
      --silent              Do not print the response body

{owner}, {repo} and {branch} (or :owner, :repo, :branch) in the endpoint and in
-F values are filled in from GH_REPO, else from the ${ALLOWS_ADDITIONAL_GITHUB_HOSTS&&!ALLOWS_ANY_GITHUB_HOST?"remotes on those hosts":`${DEFAULT_GITHUB_HOST} remotes`} of the
current repository: upstream, github, origin, then the others by name.${ALLOWS_ANY_GITHUB_HOST?`
A repository with no ${DEFAULT_GITHUB_HOST} remote is read for its other remotes the same
way, and the remote chosen names the host the request goes to.
GH_HOST and a host in GH_REPO pick no host other than ${DEFAULT_GITHUB_HOST} here: name one
with --hostname. A request to another host says so in one line on standard error.`:""}

Example: gh api repos/{owner}/{repo}/pulls -F title=@<title-file> -f head='my-branch' -f base='main'
${TEXT_FILE_INPUT_GUIDANCE}
