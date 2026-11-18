<!--
name: "Agent Prompt: /code-review GitLab comment posting"
description: "Directs code review findings to a general GitLab merge request note when the comment flag is enabled"
ccVersion: "2.1.328"
variables:
  - "GITLAB_MR_IID"
  - "GLAB_MR_NOTE_OPTIONS"
  - "GITLAB_REPOSITORY_REFERENCE"
  - "IS_BUGS_ONLY_REVIEW"
  - "FINDING_SEVERITY_COMMENT_GUIDANCE"
-->


## Posting to GitLab (--comment)

The `--comment` flag was passed. After producing the findings list, if the
review target is a GitLab merge request, post the findings as one general MR
note via `${`glab mr note${GITLAB_MR_IID?` ${GITLAB_MR_IID}`:""}${GLAB_MR_NOTE_OPTIONS} -m "<body>"`}`${GITLAB_REPOSITORY_REFERENCE?"":" from inside that project's checkout"}
(every finding with its file:line, the issue, and the suggested fix).${IS_BUGS_ONLY_REVIEW?` ${FINDING_SEVERITY_COMMENT_GUIDANCE}`:""} glab has no single verb for line-anchored
comments; those require `glab api projects/:id/merge_requests/:iid/discussions`,
so post the general note unless the user asks for inline threads. If glab is
not available in this session, print the findings instead. If the target is
not an MR, print the findings to the terminal and note that `--comment` was
ignored.
