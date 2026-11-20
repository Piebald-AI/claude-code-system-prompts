<!--
name: "Skill: Design-sync Artifacts MCP call instructions"
description: "Explains design-system listing, reading, creation and publishing with the Artifacts MCP tools and how to handle their refusals"
ccVersion: "2.1.329"
-->
## The four calls

This session makes them with the Artifacts tools: `mcp__claude-artifacts__list_types`, `mcp__claude-artifacts__create_from_type`, `mcp__claude-artifacts__list_files`, `mcp__claude-artifacts__read_file` and `mcp__claude-artifacts__publish_files` (below, without the `mcp__claude-artifacts__` in front). `publish_files` is always loaded; if the others aren't in your tool list yet, load them first: `ToolSearch(query: "select:mcp__claude-artifacts__list_types,mcp__claude-artifacts__create_from_type,mcp__claude-artifacts__list_files,mcp__claude-artifacts__read_file")`. An answer too long for the conversation is saved to a file for you: copy that file.

- **LIST**: `list_files` with the artifact's `slug`. Save the JSON object in its answer as `listing.json` in the cache. A link serves as the `slug` too: record that link, and the `slug` in the answer, a UUID.
- **READ**: `read_file` with the `slug` and the file's path. Save the file's text alone, exactly as it came.
- **MAKE**: to look for the type, `list_types` with query "Design System". To make the artifact, `create_from_type` with the type's slug and the name as `title`: it returns the link and the slug to record.
- **PUBLISH**: open the call file, and call `publish_files` with the arguments it holds and no others. From the second call of a plan on, its `base_version` reads `unknown`: put the `version` that the call before returned in its place.

**If these tools are gone from this session** in the middle of a run, its tools have changed. Tell the user, and ask them to run /design-sync again: it goes on with the same artifact.

What a refusal means:

- **The artifact is not theirs, or is served only to the user who owns it**: these tools don't serve this artifact to the user. Its owner can sync it, unless someone outside the owner's organization has written to it. The user can't publish to this artifact.
- **The caller's organization does not match the owner's**: the artifact is in another of the user's organizations, or one they are no longer part of. If they can still sign in to the organization that owns it, they can do that and run /design-sync again.
- **`base_version` is not the live version**, **the call must include, or must leave out, `shared_live`**, or **`artifact_title` is not the artifact's title**: the artifact changed since the listing.
- **The artifact's title could not be read**: a passing fault of the service. Go on as for too many requests, whatever else the refusal offers.
