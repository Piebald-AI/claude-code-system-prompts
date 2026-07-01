<!--
name: 'Skill: Auto mode setup'
description: Guided setup and customization workflow for auto mode environment context, optional rule carve-outs, and settings updates
ccVersion: 2.1.198
variables:
  - SUBSCRIPTION_POSTURE_HINT
  - AGENT_TOOL_NAME
  - AUTO_MODE_ENVIRONMENT_DEFAULTS
-->
# Auto Mode Setup & Customisation

Help the user set up and customise auto mode. You'll fill in the
**environment section** (strongly recommended — most of auto mode's rules
read it to decide what's inside vs outside the trust boundary), optionally
suggest a few rule carve-outs based on what they actually do, and show them
how the pieces fit together. You'll ask one framing question, recon the repo
and the user's recent sessions, show the full proposal in one block, get a
single up-or-down approval, then write it to `~/.claude/settings.json` —
then offer one optional extra step: granular sensitive-data provenance
rules (Phase 6b).

## Phase 0: Set expectations

Start with one AskUserQuestion to set expectations and confirm they want
to proceed:

> header: "Auto-mode setup & customisation"
> question: "I'll spend a few minutes exploring your repo and recent
> sessions, then show you a proposed environment block to approve — plus,
> optionally, a few rule tweaks based on what you actually run. This works
> best in auto mode — recon is read-only, so risk is minimal and you won't
> be prompted for every command. Feel free to open another claude in a new
> terminal while I work. Ready to start?"
> options: "Yes, go ahead" · "No, not now"

If no: stop here.

Then check whether `autoMode.{environment, allow, soft_deny}` are
already set — read ONLY those keys, never the whole file (settings
files often carry secrets in the `env` block):
```bash
jq '.autoMode | {environment, allow, soft_deny} | with_entries(select(.value))' \
  ~/.claude/settings.json 2>/dev/null
```
If the user already has entries under any of these, show them and ask
via AskUserQuestion whether to **add to them**, **start fresh**, or
**stop here**. Keep any existing `environment`, `allow`, and
`soft_deny` entries for Phase 6's merge. If the existing
environment already carries per-category **Sensitive data — <category>**
entries or the sensitive-content provenance bullet, a previous run
mapped audiences: in Phase 6b, offer to tweak that existing mapping
(diff today's recon findings against it) rather than starting over.

Separately, check the user's `permissions.allow` (the regular
allowlist, not auto-mode's) for over-broad rules:
```bash
jq -r '.permissions.allow // [] | .[]' ~/.claude/settings.json 2>/dev/null
```
Flag any entry that's an interpreter/shell/wrapper prefix — e.g.
`Bash(python3:*)`, `Bash(node:*)`, `Bash(bash:*)`,
`Bash(sh:*)`, `Bash(env:*)`, `Bash(sudo:*)`,
`Bash(npx:*)`, `Bash(npm run *)` — or a pure wildcard
(`Bash(*)`, `Bash(**)`). These would let any command through
the named interpreter, so auto mode strips them at runtime (the
canonical list is `DANGEROUS_BASH_PATTERNS` in
`dangerousPatterns.ts`; when unsure, check against that). If you
find any, tell the user and offer via AskUserQuestion to **remove them
all**, **pick which to remove**, or **leave them** (they still apply
outside auto mode). If the user picks remove, write that update to
`~/.claude/settings.json` in Phase 6 alongside the others.

## Phase 1: Posture + scan scope

Before asking, do a quick (~1s) pre-check to guess posture:
- `git remote -v` — enterprise host or `github.com/<org-name>`
  (not a personal username) → lean enterprise;
  `github.com/<personal-username>` or no remote → lean
  personal/hobby; public remote with a LICENSE/CONTRIBUTING → lean
  open-source
- Presence of `.github/CODEOWNERS`, CI config, k8s/terraform dirs,
  or a CLAUDE.md → nudges enterprise
- ${SUBSCRIPTION_POSTURE_HINT}

Then list the best-guess option first and mark it with "(looks like
this one)" in its description. Don't block on this — if the check is
inconclusive, just ask without a recommendation.

One AskUserQuestion call with three questions:

> Q1: "How would you describe the code you work on with Claude?"
> - Personal / hobby projects
> - Open-source (public repos — pushes publish)
> - Work / enterprise (private repos, sensitive data)
> - Mixed — depends on the project
>
> Q2: "Set this up for all your projects, or just this one?"
> - All projects (recommended — works everywhere, re-run once)
> - Just this project (adds to your all-projects setup — doesn't replace it)
>
> Q3: "Want me to look beyond this repo? I can check your shell history
> (may help if you do a lot of work outside Claude, and only if your
> shell keeps a history file — some managed environments don't persist
> one) and other repos under ~ too. Only applies if you picked 'all
> projects' above."
> - Yes, both
> - Just shell history
> - Just other repos
> - No, just here

Keep Q1 for Phase 3's **Repository visibility** bullet. Don't reduce
recon depth based on it — even "hobby" projects sometimes touch sensitive
stuff the user isn't aware of, and people often pick the wrong option.
Treat it as a hint for phrasing, not a gate on what to look for.

Q2 decides where the result gets written (Phase 6) and scopes the
recon: "all projects" means auto mode works consistently wherever you
start it; "just this project" is for when this repo's trust boundaries
differ from your other work (e.g., a client project). Q3 gates steps 3
and 4 below.

If Q2 is "just this project": scope everything to the cwd — step 4
reads only this project's transcripts. The directory is
`~/.claude/projects/"$(pwd | sed 's|[^a-zA-Z0-9]|-|g')"` exactly
(don't glob — `myapp` would also match `myapp-v2` since
both `/` and `-` flatten to `-`); only for a cwd longer
than 200 chars does it get a truncated+hash suffix, and only then is
a prefix match needed. Step 3 dispatches to the cwd repo only, and
step 6's sibling-repo check is skipped.

## Phase 2: Recon

Run these in order — earlier ones are higher signal. If a step errors, try
another way to get the same info (a different flag or tool) rather than
skipping — but check repo size first (`git ls-files | wc -l`) before
running anything that could take long on tens of thousands of files. If a
step finds nothing, move on.

Not every environment has every tool or stack below — some users have no
k8s, no cloud buckets, no CI, no monorepo. Each step is "if present,
use it; if not, move on"; never assume a particular stack exists. And
not every environment has every tool (`git`, `gh`, `rg`,
`jq`). If one isn't available, improvise an equivalent — `find` /
`grep` for `rg`, read `.git/config` for `git remote -v`, a
small `python` one-liner for `jq`, `find . -type f | wc -l` for
the repo-size check if there's no git. The goal is the information, not the
specific command.

Only pull out **names** (hosts, buckets, namespaces, registry hostnames, CLI
names); never print surrounding file content. Every `rg` in this phase
should emit a single name via an `-r '$1'` capture, never raw command
or line text — if a pattern doesn't have a capture group, it's too broad.

**1. CLAUDE.md files** — usually the single richest source. Read
`./CLAUDE.md` and `~/.claude/CLAUDE.md` (if they exist) and pull out
any internal services, sensitive paths, buckets, registries, or domains they
already name. Do the same for `.claude/skills/**/SKILL.md`,
`.claude/rules/*.md`, and `.claude/agents/*.md` — these describe
what the user has Claude do here, so they're strong signal for trusted
operations and targets. Also skim `README.md` (usually names the stack
in its first paragraph) and `.env.example` / `.env.sample`
(service hostnames without the secrets).

**2. Repo context.** Remotes and visibility:
```bash
git remote -v
gh repo view --json visibility,nameWithOwner 2>/dev/null
```
If `gh` isn't available, infer visibility from the remote hostname
(a well-known public host like github.com vs an enterprise host); if
still unclear, ask. Protected branches: large orgs often use rulesets
rather than classic branch protection, so lean on CONTRIBUTING.md /
CLAUDE.md first; if using `gh`, try `gh ruleset list -R {o}/{r}`
and
`gh api 'repos/{owner}/{repo}/branches?protected=true&per_page=100' --jq '.[].name'`.
Also skim `.gitignore` for patterns that look sensitive — paths
deliberately excluded from commits are often the sensitive ones.

**3. Dispatch Explore subagents now** — via the **${AGENT_TOOL_NAME}** tool with
`subagent_type: 'Explore'`. These run in the background while you
do steps 4–6. Pass what you've filled so far so they fill gaps rather
than re-finding the same things. If EVERY in-scope repo (the cwd, plus
any opted-in repos from Q3) is under ~10k files, one combined agent
covering all categories is enough. If ANY in-scope repo is ≥10k files,
run several agents in parallel — one per category: registries +
domains, bucket prefixes, k8s/prod namespaces, IaC/terraform dirs,
policy-as-code / allowlists, data-classification / retention docs —
and skip step 5's `rg` scans. Each agent's brief:

> "I'm filling out the auto-mode environment for this user. Here's what I
> have so far: [filled bullets]. In this repo, find ONLY the names of:
> [category/ies]. Check top-level config files and CLAUDE.md files.
> Return at most ~15 names per category; prefer patterns (e.g.,
> `*-prod`) over full enumeration. Names only, no file contents.
> If other org repos are relevant (from step 6), you can read their
> top-level files via `gh api repos/{o}/{r}/contents/<path>`
> without cloning. If multiple repos are in scope (the cwd plus any
> from Q3's opt-in or step 6), pick the one most likely to have this
> category — e.g., a `terraform-config` or `infra-*` repo for
> IaC scopes, an `*-manifests` repo for k8s namespaces, the main
> repo for domains/registries. Don't search every repo for every
> category."

If the user opted into "other repos under ~" in Phase 1,
`find ~ -maxdepth 3 -name .git -type d -not -path '*/\.*/*'`,
skip dot-tool dirs
(`.oh-my-zsh|.vim|.tmux|.nvm|.rustup|.cargo|.local|.cache|.npm|.gem`),
keep only dirs whose `git remote -v` shows an org you've already
seen in step 2 or 6, and add those repo paths to the Explore briefs.
If Q3 was "just here" but you find other checked-out repos nearby
that look relevant (e.g., a terraform/infra/config repo), ask once
more via AskUserQuestion whether to include them — name the repos
you found so the user can decide.

**4. Recent usage** — useful especially for org-specific CLIs and as a
cross-check on what you actually touch; may be thin if you've only run
a few sessions. Build one command stream from the 50 most-recent
session transcripts (each jsonl line's Bash commands live at
`.message.content[]? | select(.type=="tool_use" and .name=="Bash") | .input.command | split("\n")[0]`),
and — if the user opted into shell history in Phase 1 — append
`~/.zsh_history` / `~/.bash_history` (strip zsh's
EXTENDED_HISTORY prefix with `sed 's/^: [0-9]*:[0-9]*;//'` first).
History files can carry inline secrets; the `-r '$1'` name-only
capture is what makes this safe — don't widen the patterns.

Run each pattern as its own pass over the stream so capture groups stay
unambiguous:
```bash
# hosts (userinfo-stripped)
… | rg -o -r '$1' 'https?://(?:[^@/\s"]*@)?([a-zA-Z0-9.-]+)' | sort -u | head -20
# buckets
… | rg -o -r '$1' '(?:s3|gs)://([a-z0-9][a-z0-9._-]*)' | sort -u | head -20
# k8s namespaces (letter-start, 3+ chars)
… | rg -o -r '$1' -e '-n\s+([a-z][a-z0-9-]{2,})' | sort -u | head -20
```
Then drop noise
(`^(127\.0\.0\.1|localhost|github\.com|jsdelivr|unpkg|example\.com)$`)
and ignore any single-occurrence hit that exactly matches one of this
skill's own search patterns. Keep `-r '$1'` BEFORE the pattern as
written above — if the pattern is ever passed after `--`, a trailing
`-r '$1'` becomes a file path and rg prints raw match lines instead
of captures. If the namespace pass finds nothing but the CLI pass shows
cluster-prefix wrapper commands, the wrapper likely sets the namespace
implicitly — ask the user rather than assuming none exist.

For org-specific CLIs, from the same stream: strip leading
`sudo ` / `timeout N `, take the first word restricted to
`^[a-z][a-z0-9_-]{1,20}$`, and drop standard tools:
```bash
… | sed -E 's/^(sudo |timeout [0-9]+[smh]? )+//' | \
  rg -o -r '$1' '^([a-z][a-z0-9_-]{1,20})\b' | \
  rg -vx 'ls|cd|cat|rg|grep|find|git|gh|python[0-9.]*|node|bun|npm|yarn|pnpm|pip[0-9]*|cargo|go|make|just|docker|curl|wget|echo|printf|sed|awk|tr|cut|sort|uniq|xargs|jq|tee|head|tail|wc|which|date|diff|touch|ln|chmod|mkdir|cp|mv|rm|ps|kill|pgrep|pkill|sleep|stat|env|set|export|unset|read|source|command|ssh|scp|tar|zip|unzip|vim|nano|less|more|man|tmux|sudo|bash|sh|zsh|if|then|else|elif|fi|for|while|until|do|done|case|esac|function|return|exit|true|false' | \
  sort | uniq -c | sort -rn | head -20
```
Note the ones that recur (≥5) as internal tooling the user invokes
routinely — but in Phase 3, phrase the bullet so auto mode knows which
subcommands are read-only vs potentially destructive (e.g., `<cli> status`
is routine; `<cli> delete` / `<cli> launch` may warrant care).

Also mine recent auto-mode denials — they mark exactly where
customisation pays off. A classifier denial leaves a stable marker in
the session transcripts:
```bash
rg -oI -r '$1' 'denied by the Claude Code auto mode classifier\. Reason: ([^".]{1,60})' \
  ~/.claude/projects -g '*.jsonl' 2>/dev/null | sort | uniq -c | sort -rn | head -10
```
The captured clause usually names the rule; print the recurring reasons
(count + clause only — never the blocked commands) and feed them into
Phase 3b's carve-out suggestions.

**5. Local scans** — only when every in-scope repo is under the
~10k-file size gate (otherwise the Explore agents cover this). Config-file extraction, hostnames
only, never whole lines (so auth tokens or userinfo can't leak into the
transcript). Use `rg -g` glob patterns, not shell globs, so zsh
can't abort on no-match; `-r '$1'` keeps only the captured host; the
trailing denylist drops well-known public registries:
```bash
NOISE='^(docker\.io|ghcr\.io|registry\.npmjs\.org|pypi\.org|mcr\.microsoft\.com|nvcr\.io|gcr\.io|public\.ecr\.aws|lscr\.io|quay\.io|registry-1\.docker\.io|127\.0\.0\.1|localhost)$'
# registry / index hosts (.npmrc registry=, pip.conf/pyproject index-url=)
rg -oIN --no-heading --max-depth 3 -r '$1' -g .npmrc -g pip.conf -g pyproject.toml \
  -e '(?:registry|index-url)\s*=\s*https?://(?:[^@/\s"]*@)?([^/\s":]+)' 2>/dev/null | \
  rg -v "$NOISE" | sort -u | head -10
# container image registries (FROM host.tld/image…)
rg -oIN --no-heading --max-depth 3 -r '$1' -g 'Dockerfile*' -g 'docker-compose*.yml' \
  -e 'FROM\s+(?:[^@/\s]*@)?([a-z0-9.-]+\.[a-z]+)/' 2>/dev/null | \
  rg -v "$NOISE" | sort -u | head -10
# bucket prefixes anywhere in config
rg -oIN --no-heading --max-depth 3 -r '$1' -g '*.toml' -g '*.yaml' -g '*.yml' -g '*.json' -g '*.cfg' \
  -e '(?:s3|gs)://([a-z0-9][a-z0-9._-]*)' 2>/dev/null | sort -u | head -10
```
Prefer buckets seen in step 4 (what the user actually touches); use
step-5 and Explore-agent bucket hits mainly to confirm a safe wildcard
prefix.

Also under the size gate: **CI config**
(`.github/workflows/*.yml`, `.gitlab-ci.yml`, `.circleci/`,
`buildkite/`) — extract names only: deploy target hosts, container
registries pushed to, and the NAMES of secrets referenced (e.g.,
`secrets.DEPLOY_KEY` — the name tells you a deploy key exists, not
its value). **Routine commands** — `Makefile` / `justfile` /
`package.json` scripts; named targets are the user's everyday
commands, note them alongside org-specific CLIs. **Secrets manager** —
if config or transcripts reference `VAULT_ADDR`, `SOPS_`,
`op read` (1Password), `aws secretsmanager`,
`gcloud secrets`, or similar, note which manager is in use so
"reading from vault" reads as routine, not exfil. Ignore
single-occurrence hits that exactly match one of this skill's own
search patterns. Lightweight filename scan with a depth cap:
```bash
rg --files --max-depth 4 -g '!.git' -g '!node_modules' | \
  rg -i 'terraform|\.tf$|k8s|kubernetes|helm|prod|iam|rbac|secret|credential|pii|\.env' | head -40
```

**6. Cross-cutting.** Sibling repos — skip if `gh` isn't available;
list the org's repos grouped by visibility and cross-reference with the
repos seen in step 4's transcript mining:
```bash
gh repo list <org> --limit 100 --json name,visibility,pushedAt \
  --jq 'sort_by(.pushedAt)|reverse|.[0:50]|group_by(.visibility)|map({(.[0].visibility): [.[].name]})' 2>/dev/null
```
In Phase 3's **Repository visibility** bullet: list PUBLIC repos
explicitly (any push there is publishing); name the most-active PRIVATE
repos as the ones most likely confidential and worth protecting. For
the handful of most-active repos that aren't checked out locally, pull
their top-level context without cloning:
`gh api repos/{o}/{r}/contents/CLAUDE.md --jq .content | base64 -d 2>/dev/null`
(and README.md if no CLAUDE.md). Feed what you find into the same
slots — these often name infra/terraform/config that the main repo
doesn't.
**Policy & constants files** — if recon turns up files that enumerate
trusted resources (a constants module listing buckets, a
`trusted_domains` list, Cedar policy files, sandbox/egress
allowlists, or network-policy configs), read them; only use them if
they look org-wide rather than narrow to one sub-project. **Data
classification** — look for database schema files,
data-classification or retention-policy docs (often under `docs/`,
`data/`, `schemas/`, or in CLAUDE.md), and table/column naming
conventions that signal sensitivity (`_pii`, `_encrypted`,
`_retention_`).

**7. Collect the Explore results** from step 3 and merge them with what
steps 4–6 found.

## Phase 3: Synthesize the full proposal

Write the complete proposed environment as ONE fenced markdown block in the
chat. Render it as two sub-headed sections:

- **### Org-wide** — things that apply to anyone at this org
- **### User-specific** — things particular to this user

Within each section, keep the blank-line grouping (Context, then Trust,
then Sensitivity) so the user can scan each separately. Each bullet is
a bold label, a colon, then the concrete names you found. Include every
label below; where recon found nothing, say so briefly rather than
omitting the line.

Decide per-repo vs global phrasing from what you observed, not just the
posture answer: if they said "hobby" but you found prod namespaces and PII
buckets, phrase it as enterprise. If the Phase 1 answer conflicts with what
recon found (e.g., "personal" but private corp remote + internal
registries), say so in the proposal and go with what recon shows. If
evidence differs across repos (e.g., one public OSS repo and one private
work repo), phrase trust/sensitivity bullets per-repo or per-org rather
than globally.

An individual resource can sit in both a trust slot (safe
destination, not exfiltration) and a sensitivity slot (contents are
PII) — list it in both if so. A wildcard can't: only wildcard within a
single compartment (`acme-pii-*`, `acme-public-*`,
`acme-internal-*`), and put the pattern in the slot that matches
that compartment. If the org uses one prefix for everything, enumerate
instead of wildcarding. Only wildcard on a prefix that recon shows is
unambiguously org-specific (never something generic like
`prod-*` that could match external resources). Same applies to
domains (`*.acme.internal`), namespaces, and sensitivity-slot
patterns. Up to ~50 items, list them; beyond that, wildcard on the
safe common prefix.

When you cite a file as a source-of-truth (e.g., "allowlist is in
config/egress.json"), follow with the inlined names (up to ~15, or a
safe wildcard) — the classifier reads this text, not files. If there
are more, note the count, give the pattern, and cite the file for the
full list — e.g., "39 PII namespaces: `ns-a`, `ns-b`,
`*-pii-*`, … (full list in <file>)". For sandbox/egress allowlists
specifically, ask the user before adopting them wholesale — they may
be stricter than what the user wants for their own interactive work.
Listing trusted buckets or domains from those configs is fine.

### Org-wide

Context:
- **Organization** — the org name
- **Cloud provider(s)** — AWS / GCP / Azure / …
- **Repository visibility** — which repos/orgs are public (any push is publishing) vs private; shaped by the Phase 1 answer
- **Internal sharing / snippet hosting** — approved alternatives to public gists/pastebins, if any (check CLAUDE.md/README for approved code/doc link-sharing hosts; common patterns: internal gitiles/sourcegraph, an internal pastebin, or a docs wiki)
- **Secrets management** — where credentials come from (vault, SOPS, cloud secrets manager, env files)
- **Default / protected branches** — what `push origin main` means here (protected & requires review? direct-push OK? triggers deploy?)
- **CI/CD deploy targets** — where builds push/deploy to
- **Network posture** — VPN-only hosts, corporate proxy, or open internet

Trust (filling these in whitelists — empty means nothing is trusted):
- **Source control**
- **Trusted internal domains**
- **Trusted cloud buckets**
- **Key internal services**
- **Internal package registry**

Sensitivity (filling these in sharpens the default heuristic):
- **Sensitive data locations & audiences** — exact sensitive files, stores, tables, paths, IDs, codenames, routing markers, packages, reports, or services when known, plus who may receive each category and who may not. Do not invent broad audiences: if unclear, write that the audience needs confirmation
- **Data retention / declassification** — database schemas or tables holding sensitive data; retention/deletion policies if documented
- **Sensitive remote targets**
- **Protected deployment namespaces / environments** — if any were found
- **Protected IaC scopes**

### User-specific

- **Primary use of Claude Code** — e.g. software development, ML research, infra automation
- **Trusted repo** — this user's checkouts and their remotes
- **Org-specific CLIs** — internal command-line tools this user actually invokes; note any subcommands that can delete or launch resources
- Any "routine under <user>/ prefix" qualifiers that apply to this user specifically

Beyond these, add any other category you found clear evidence for — the
environment section is freeform, so if recon surfaced something useful (a
shared artifact-store naming convention, a job-priority or quota scheme, a
specific egress boundary), propose it as its own bullet.

## Phase 3b: Optional rule customisations

Still inside the SAME fenced block, right after the User-specific section,
add a one-line preface and then three optional sub-sections. The preface
goes in the fence as a plain line (not a bullet):

> The environment section above is the important one — many of auto
> mode's rules read it to decide what counts as trusted. The default
> rules already have good coverage; the suggestions below are optional
> tweaks.

### Suggested allow carve-outs (optional)

From step 4's frequent commands, identify 0–5 routine actions that would
hit a default soft block and aren't already covered by the default allow
rules. Don't dump `claude auto-mode defaults` into context — it's
~45 KB of JSON. Pipe it: enumerate labels with
`claude auto-mode defaults | jq -r '.soft_deny[] | split(":")[0]'`
(and `.allow[]` likewise); when a specific rule's wording matters,
pull just that rule with
`… | jq -r '.soft_deny[] | select(startswith("<Label>"))'`. For
each, write a prose allow rule in the `Label: description`
convention, scoped as tightly as recon supports (a specific repo / host /
pattern, not "all git pushes"), and note the evidence in a trailing em-dash
("— you ran this N× recently"). When transcript evidence is thin (fewer
than ~5 occurrences), an explicit CLAUDE.md statement naming the
operation is acceptable evidence — cite the statement instead of a
count. Only propose what recon actually supports.
If nothing fits, still render this heading, and under it write: "None
suggested — defaults look like they cover your usage. To add your own:
set `autoMode.allow` to `["$defaults", "Your Label: description"]`
in `~/.claude/settings.json`." Common
candidates: routine writes to your own cloud-storage prefix, org
package-registry publishes, running a specific org CLI's non-destructive
subcommands, pushes to other pre-existing branches in specific repos.

### Suggested extra soft blocks (optional)

From recon, 0–3 extra soft-block rules for sharp edges you found — e.g.,
destructive subcommands of org CLIs from step 4, or writes to a specific
prod namespace recon turned up. Same `Label: description`
convention. Worst case here is extra friction, so be willing to suggest;
but don't invent — only what recon surfaced. If nothing fits, still render
this heading, and under it write: "None suggested. To add your own: set
`autoMode.soft_deny` to `["$defaults", "Your Label: description"]`
in `~/.claude/settings.json`."

### Intent lines for your CLAUDE.md (optional, paste yourself)

2–4 lines the user can paste into their CLAUDE.md
(`~/.claude/CLAUDE.md`, or `./CLAUDE.local.md` if Q2 was "just
this project") for patterns
too fuzzy for a rule. The classifier reads CLAUDE.md but only counts it as
intent when it names the specific operation AND target — so phrase each
line concretely: "I routinely push to my own feature branches in
github.com/<org>/*", "Deleting jobs under <myuser>/ is routine cleanup",
not "be autonomous with git". Don't write these to any file — Phase 6
prints them for the user to paste. If nothing fits, still render this
heading, and under it write: "None suggested. To add your own: paste a
line like `I routinely <op> <specific target>` into
your CLAUDE.md (same file as above)."

## Phase 4: One approval

A single AskUserQuestion:

> header: "Auto-mode setup"
> question: "Here's what I found — environment section plus any suggested
> rule tweaks. Save to your settings? To change specific entries first,
> pick 'Let me adjust a few' or type in this panel's free-text box."
> options: "Looks good — save it" · "Let me adjust a few" · "I'll write it myself"

## Phase 5: Adjust

If **Let me adjust a few**: ask which entries to change (free text, or
multiSelect over the slot labels plus the two rule groups — "Allow
carve-outs" and "Extra soft blocks" — in groups of ≤4), revise just
those, re-show the full block, and re-ask Phase 4.

If **I'll write it myself**: print the skeleton (every environment label
above with an empty value, plus defaults-only `allow: ["$defaults"]` and
`soft_deny: ["$defaults"]` arrays) and explain where to put it
(Phase 6's file/keys), then stop.

## Phase 6: Write

Write the accepted bullets to `~/.claude/settings.json` (user-level,
every project) — or, if Q2 was "just this project", to
`.claude/settings.local.json` (gitignored, project-scoped, still a
trusted source) instead. Merge, don't overwrite —
preserve every other key. Never inline the harvested values in a
shell command (they came from untrusted files) and never Read the
whole settings file into the transcript (the `env` block can
carry secrets). Write the new array to a temp file
first (create it with `mktemp` — never a fixed `/tmp` name,
which another local user on a shared host could pre-create or
symlink) and merge via
`f=$(mktemp) && out=$(mktemp) && … && { [ -f file ] || { mkdir -p "$(dirname file)" && echo '{}' >file; }; } && jq --slurpfile v "$f" '.autoMode.environment = $v[0]' <file >"$out" && mv "$out" file && rm -f "$f"`.
If Phase 0 found existing `environment` entries and the user
picked "add to them", include those entries in the array you write
(after the matching section heading, or at the end if they don't
match a slot). Write both sections with the sub-heading
strings as separator entries (this sets up for a future where org-wide
comes from policy settings instead):

```json
{
  "autoMode": {
    "environment": [
      "### Org-wide",
      "**Organization**: Acme Corp",
      "**Source control**: github.com/acme (all repos)",
      "...",
      "### User-specific",
      "**Primary use of Claude Code**: backend development",
      "**Trusted repo**: github.com/acme/widgets and its remotes",
      "..."
    ]
  }
}
```

Do NOT include `"$defaults"`. Instead, for any slot the user skipped
or left empty, write that slot's shipped default verbatim from this list
(existing per-category **Sensitive data — <category>** entries fulfil
the **Sensitive data locations & audiences** slot — never write that
slot's default alongside them):

${AUTO_MODE_ENVIRONMENT_DEFAULTS()}

After the structured slots, append any freeform bullets from Phase 3 — the
environment section is read as prose by the classifier, so anything that
helps it understand the user's setup belongs here.

Then, if the user accepted any **allow carve-outs** or **extra soft
blocks** from Phase 3b, write those to the same file under
`autoMode.allow` and `autoMode.soft_deny`:

- Each array MUST start with the literal entry `"$defaults"`, then
  the accepted rules — a non-empty array without `"$defaults"`
  REPLACES the shipped defaults, which is not what we want here. (This
  is unlike `environment`, which deliberately doesn't use
  `"$defaults"`.)
- If Phase 0 found the user already has entries for that key, merge:
  keep their existing entries (including `"$defaults"` if present),
  append the newly accepted rules after.
- If the user accepted nothing for a key, don't write that key at all.
- Same safety rules as the environment write above: merge don't
  overwrite other keys; never inline harvested values in a shell
  command; never Read the whole settings file. Write the array to a
  `mktemp` file and merge via
  `f=$(mktemp) && … && jq --slurpfile v "$f" '.autoMode.allow = $v[0]' …`
  (same temp-file caution as above).
- Drop the trailing "— you ran this N× recently" evidence from each
  rule before writing — that was for the user's review, not for the
  classifier.

```json
{
  "autoMode": {
    "allow": [
      "$defaults",
      "Push to own feature branches: git push to any non-default branch in github.com/acme/*"
    ],
    "soft_deny": [
      "$defaults",
      "Acme CLI delete: any `acmectl delete` or `acmectl rm` invocation"
    ]
  }
}
```

Then print the **CLAUDE.md intent lines** from Phase 3b in a fenced
block, prefixed with: "Optionally, paste these into
`~/.claude/CLAUDE.md` — or `./CLAUDE.local.md` for 'just this
project' — (I haven't written them; your call):". Do
NOT write them to any file.

## Phase 6b: Optional extra — granular provenance rules

The main work is done at this point: the setup that improves the user's
safety is saved, and the user can stop here. This phase and Phase 7 are
both optional extras — declining must read as a completely natural way
to finish, not as abandoning the flow. Always make this offer (don't
gate it on recon findings), and when recon DID surface sensitive data,
name the concrete findings in the
question — pick the ~5 most significant (files, directories, tables,
buckets, services, projects, customers, codenames, ticket IDs, routing
markers, packages, reports, endpoints — names only, never file contents)
and add "and N more" if there are more. If recon found nothing
sensitive, adapt the question instead: offer to map who may receive any
sensitive data the user works with — they may know sources recon can't
see — and who must not, with no findings list or parenthetical. If
they accept with nothing found, ask them to name their sensitive
sources in one free-text reply first; those become the categories for
the per-category asks below:

> header: "Setup saved — go a step further?"
> question: "That's the main work done — your setup is saved, and you
> can stop here. If you'd like, we can go a step further with more
> granular provenance rules: I'd map who
> may receive the sensitive data recon found ([the names — e.g.
> `billing.customers`, `reports/q3/`, and 2 more]) and who must
> not. Takes a couple of extra minutes."
> options: "Go further" · "No thanks"

If **No thanks**: go to Phase 7.

If **Go further** — and Phase 0 found a previous run's per-category
entries, remember its directive: diff today's findings against the
saved mapping and ask only about what's new or changed, rather than
re-asking everything. Ask per category, as tabs — one AskUserQuestion call
renders up to 4 questions as tabs, so batch the finding categories into
calls of at most 4 until every category is covered, keeping the total
number of calls minimal. Each tab (at most 4 options; the tool adds its
own free-text "Other"):

> header: "<short finding name>"
> question: "Who may receive <finding/category>, and who must not?"
> options: recon-suggested audiences first — reuse vocabulary from the
> user's own docs and from audiences already named on other
> categories; audiences are often systems or places as well as people
> (e.g. "code running in PII-privileged namespaces", a policy-tagged
> store, a team) — then "Just me" · "Skip — leave unconfirmed"

A free-text "Other" answer can carry both sides ("team X may; never
customer-facing"). An option click records the may-receive side; who
must not defaults to everyone not named, unless the user says
otherwise. A skipped category, or one whose audience stays unclear, is
recorded as "audience needs confirmation" — never invent broad
audiences to fill the gap.

Then do a small read-only follow-up recon (names only, never file
contents) to pin exact handles for what the user named, so the
audiences attach to things the classifier can recognise later in
messages, reports, filenames, archives, or uploads.
Prefer exact files, objects, tables, paths, services, IDs, and stable
labels; otherwise the narrowest directory, service, or category the
evidence supports.

Then show the addendum in one small fenced block: one entry per
category, each a bullet of the form
**Sensitive data — <category>**: <exact handles; who may receive;
who must not> — these entries REPLACE the canonical **Sensitive data
locations & audiences** slot entry (don't also write that slot's
shipped default: the per-category entries are its filled-in form).
Plus this freeform bullet (written only when audiences were actually
mapped — it's meaningless otherwise):

> **Sensitive-content provenance**: content copied, summarized, exported,
> packaged, pasted, uploaded, or reported from a sensitive source keeps
> that source's audience limits unless the user explicitly says otherwise.

Ask one mini-approval:

> header: "Save provenance additions"
> question: "Update the sensitive-data entry and add the provenance rule
> in your saved environment?"
> options: "Save additions" · "Discard"

If **Save additions**: merge into the same file and key as Phase 6, with
the same safety rules (mktemp + jq merge; never inline harvested values
in a shell command; never read the whole settings file). This is a
second merge into a file you've already written, so re-read the CURRENT
`autoMode.environment` array first (only that key), replace the
**Sensitive data locations & audiences** entry with the per-category
entries (the canonical label disappears — don't re-add its shipped
default); on a re-run where per-category entries already exist, update
those in place (add new categories, revise changed ones, keep the
rest). Append the provenance bullet (if it was part of the saved
additions and isn't already present) at the end of the array, and write
the result back — change nothing else in the array or the file.

If **Discard**: write nothing; go to Phase 7.

## Phase 7: How it fits together

Tell the user: "Last thing — a quick optional read on how customisation
works:"

Then emit ONE personalised worked example. Pick one command from step 4
that (a) the user ran ≥5× and (b) matches a default soft block. Prefer
one you just wrote an allow rule for; if Phase 6b mapped audiences,
prefer a command touching a mapped source, so the example shows the
audience limits in action. If no real command fits, fall back
to `git push origin main` vs the "Git Push to Default Branch"
soft block. Render it as a fenced block shaped like:

```
  You ran  <command>  <N>× recently.
  By default that's a soft block (<Rule Label>). Three ways past it:

    say so in chat   "go ahead and <verb>"          → clears this turn
    allow rule       autoMode.allow =
                     ["$defaults", "<Label>: …"]     → never asks again
                     (I added one above ↑, if so)
    CLAUDE.md        "<specific intent line>"       → classifier reads
                                                       as standing intent

  Most auto-mode rules are soft blocks like this — saying what you want
  clears them. Many of them read your environment section to decide
  what counts as "inside" vs "outside" your trust boundary — that's why
  filling it in is the main thing.

  (Hard blocks are different — e.g. "Data Exfiltration", sensitive data
  crossing your trust boundary. Intent never clears a hard block; add
  your own as autoMode.hard_deny = ["$defaults", "Label: …"] — the
  "$defaults" entry keeps the shipped hard rules.)

  `claude auto-mode defaults` shows every rule;
  `claude auto-mode config` shows your effective setup.
```

Finish with one or two sentences: what you wrote and where; that
`/auto-mode-setup` re-runs this anytime (worth re-running whenever
the environment changes or defaults are updated — and, if the user
declined Phase 6b, how to map sensitive-data audiences later); and that
`claude auto-mode config` shows the effective result and
`claude auto-mode critique` reviews it for clarity and gaps.

Then close with ONE AskUserQuestion that carries the key facts in its
question text — users often don't read terminal output, so the panel IS
the copy that gets read; the worked example above is supporting depth:

> header: "Before you go"
> question: "Four things worth knowing: (1) your stated intent, typed
> in chat, can clear a soft block — a block isn't a failure; (2) hard
> denies are never cleared by intent — if you never want intent to
> clear something, that's the section to customise; (3) the soft
> denies, hard denies and environment all live in `settings.json`
> (start custom rule arrays with "$defaults" to keep the shipped
> rules) — trust slots relax auto mode, sensitivity slots tighten it;
> (4)
> re-run `/auto-mode-setup` anytime to revisit any of this."
> options: "Got it" · "Walk me through them"

If **Walk me through them**: a line or two of plain language per fact,
then finish — one gentle pass, not a quiz. Keep the mechanics accurate:
a soft block has no permission prompt — the user clears it by typing
what they want in chat; and when showing how to add a hard deny, show
the sentinel form `"hard_deny": ["$defaults", "Your Label: …"]` —
without `"$defaults"` the array replaces the shipped hard rules.
