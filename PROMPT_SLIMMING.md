# Prompt Slimming Candidates

Prompts analyzed: 610
README token total: 795,823 tokens

## Token Totals By Category

| Category | Prompts | Tokens |
| --- | ---: | ---: |
| data | 92 | 325,379 |
| skill | 81 | 279,892 |
| agent | 66 | 84,548 |
| tool | 154 | 49,351 |
| system | 133 | 44,476 |
| reminder | 84 | 12,177 |

## Highest Priority Candidates

1. Data: Tool use concepts (11,835 tokens, data-tool-use-concepts.md)
   - Category: data
   - Why: very large token footprint; rule-heavy wording; example-heavy content; long checklist shape
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
2. Skill: Model migration guide (64,238 tokens, skill-model-migration-guide.md)
   - Category: skill
   - Why: very large token footprint; many imperative rules; example-heavy content; long checklist shape
   - Suggested cut: keep a short trigger and load step-specific guidance only after invocation; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
3. Data: Workshop artifact HTML template (46,885 tokens, data-workshop-artifact-html-template.md)
   - Category: data
   - Why: very large token footprint; many imperative rules
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; deduplicate repeated must/never/always rules into a smaller contract
4. Skill: Design sync Storybook source shape (25,255 tokens, skill-design-sync-storybook-source-shape.md)
   - Category: skill
   - Why: very large token footprint; many imperative rules; example-heavy content; long checklist shape
   - Suggested cut: keep a short trigger and load step-specific guidance only after invocation; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
5. Skill: /design-sync package source shape (16,174 tokens, skill-design-sync-package-source-shape.md)
   - Category: skill
   - Why: very large token footprint; many imperative rules; example-heavy content; long checklist shape
   - Suggested cut: keep a short trigger and load step-specific guidance only after invocation; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
6. Data: Managed Agents endpoint reference (12,152 tokens, data-managed-agents-endpoint-reference.md)
   - Category: data
   - Why: very large token footprint; rule-heavy wording; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
7. Skill: Building LLM-powered applications with Claude (27,570 tokens, skill-building-llm-powered-applications-with-claude.md)
   - Category: skill
   - Why: very large token footprint; many imperative rules; long checklist shape
   - Suggested cut: keep a short trigger and load step-specific guidance only after invocation; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
8. Agent Prompt: Security monitor for autonomous agent actions (second part) (25,099 tokens, agent-prompt-security-monitor-for-autonomous-agent-actions-second-part.md)
   - Category: agent
   - Why: very large token footprint; many imperative rules; long checklist shape
   - Suggested cut: keep a short trigger and load step-specific guidance only after invocation; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
9. Skill: /doctor slash command (15,359 tokens, skill-doctor-slash-command.md)
   - Category: skill
   - Why: very large token footprint; many imperative rules; long checklist shape
   - Suggested cut: keep a short trigger and load step-specific guidance only after invocation; deduplicate repeated must/never/always rules into a smaller contract
10. Skill: Artifact PR review (14,651 tokens, skill-artifact-pr-review.md)
   - Category: skill
   - Why: very large token footprint; many imperative rules; long checklist shape
   - Suggested cut: keep a short trigger and load step-specific guidance only after invocation; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
11. Agent Prompt: Security monitor for autonomous agent actions (first part) (11,418 tokens, agent-prompt-security-monitor-for-autonomous-agent-actions-first-part.md)
   - Category: agent
   - Why: very large token footprint; many imperative rules; long checklist shape
   - Suggested cut: keep a short trigger and load step-specific guidance only after invocation; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
12. Skill: Artifact workshop (10,143 tokens, skill-artifact-workshop.md)
   - Category: skill
   - Why: very large token footprint; many imperative rules; example-heavy content
   - Suggested cut: keep a short trigger and load step-specific guidance only after invocation; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
13. Data: Managed Agents core concepts (8,016 tokens, data-managed-agents-core-concepts.md)
   - Category: data
   - Why: large token footprint; rule-heavy wording; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
14. Data: Managed Agents tools and skills (7,589 tokens, data-managed-agents-tools-and-skills.md)
   - Category: data
   - Why: large token footprint; rule-heavy wording; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
15. Data: Managed Agents events and steering (6,639 tokens, data-managed-agents-events-and-steering.md)
   - Category: data
   - Why: large token footprint; rule-heavy wording; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
16. Data: HTTP error codes reference (4,809 tokens, data-http-error-codes-reference.md)
   - Category: data
   - Why: large token footprint; example-heavy content; long checklist shape
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
17. Data: Plan artifact HTML template (19,011 tokens, data-plan-artifact-html-template.md)
   - Category: data
   - Why: very large token footprint
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; deduplicate repeated must/never/always rules into a smaller contract
18. Data: Managed Agents reference — Go (8,273 tokens, data-managed-agents-reference-go.md)
   - Category: data
   - Why: large token footprint; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
19. Data: Claude API reference — C# (7,997 tokens, data-claude-api-reference-c.md)
   - Category: data
   - Why: large token footprint; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
20. Data: Tool use reference — TypeScript (7,559 tokens, data-tool-use-reference-typescript.md)
   - Category: data
   - Why: large token footprint; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
21. Data: Claude API reference — Python (7,423 tokens, data-claude-api-reference-python.md)
   - Category: data
   - Why: large token footprint; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
22. Data: Tool use reference — Python (7,076 tokens, data-tool-use-reference-python.md)
   - Category: data
   - Why: large token footprint; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
23. Data: Managed Agents reference — Java (6,740 tokens, data-managed-agents-reference-java.md)
   - Category: data
   - Why: large token footprint; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
24. Data: Prompt Caching — Design & Optimization (6,056 tokens, data-prompt-caching-design-optimization.md)
   - Category: data
   - Why: large token footprint; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
25. System Prompt: Coordinator mode orchestration (5,916 tokens, system-prompt-coordinator-mode-orchestration.md)
   - Category: system
   - Why: large token footprint; rule-heavy wording; example-heavy content; long checklist shape
   - Suggested cut: keep only global invariants in the prompt and move situational policy to runtime state; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
26. Data: Claude API reference — TypeScript (5,854 tokens, data-claude-api-reference-typescript.md)
   - Category: data
   - Why: large token footprint; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
27. Data: Managed Agents reference — PHP (5,420 tokens, data-managed-agents-reference-php.md)
   - Category: data
   - Why: large token footprint; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
28. Data: Claude API reference — Java (4,844 tokens, data-claude-api-reference-java.md)
   - Category: data
   - Why: large token footprint; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
29. Skill: Cowork plugin authoring (4,791 tokens, skill-cowork-plugin-authoring.md)
   - Category: skill
   - Why: large token footprint; rule-heavy wording; example-heavy content; long checklist shape
   - Suggested cut: keep a short trigger and load step-specific guidance only after invocation; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract
30. Data: Anthropic CLI (4,615 tokens, data-anthropic-cli.md)
   - Category: data
   - Why: large token footprint; example-heavy content
   - Suggested cut: move reference material behind retrieval or an explicit help/docs command; collapse examples into one canonical positive case plus one failure case; deduplicate repeated must/never/always rules into a smaller contract

