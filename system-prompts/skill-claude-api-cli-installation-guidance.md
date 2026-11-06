<!--
name: "Skill: Claude API CLI installation guidance"
description: "Claude API skill section giving Anthropic CLI installation routes and requiring its full path when Apache Ant shares the ant command name"
ccVersion: "2.1.319"
-->
- **`ant` is missing, or is Apache Ant** (it answers about `build.xml`): the sign-in still comes first. Offer to install Anthropic's CLI: `brew install anthropics/tap/ant` (macOS), `go install github.com/anthropics/anthropic-cli/v2/cmd/ant@latest` (with Go), or on Linux/WSL the command at `https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart` (it uses `sudo`, so they run it; it names a release, so never make one up). Beside Apache Ant, never use the bare name: each command you run, and each you give them (the login too), takes the full path of Anthropic's `ant`, as in `! $(go env GOPATH)/bin/ant auth login` after `go install`; `which -a ant` lists every `ant` on `PATH`.
