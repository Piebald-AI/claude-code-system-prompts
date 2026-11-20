<!--
name: "Skill: Design-sync Artifact tool call instructions"
description: "Explains design-system listing, reading, creation and publishing with the Artifact tool, including file limits and conflict recovery"
ccVersion: "2.1.329"
-->
## The four calls

This session makes them with the `Artifact` tool. Every call names the artifact by its link, as `url`: `link` in DATA or, where that is null, `https://claude.ai/code/artifact/` followed by the `slug`. In `.design-sync/artifact.json`, record the link as `url`, as MAKE's answer gives it or LIST's after "Published files of", and leave `slug` out. Make each call in a message of its own, and wait for its answer before the next. An action's older spelling stands in brackets: the tool takes either.

- **LIST**: two calls. First `action: "list"` with `scope: "files"` (`action: "list_files"`), and `url`: save the line of the answer that begins "Published files of", whole, as `listing.txt` in the cache (an answer too long for the conversation is saved to a file for you: copy that file). Then `action: "read"` (`"read_file"`) with `url` and `path: "_files.json"`, the service's own list of the files with their hashes: the answer says where on this machine it was saved, so copy it from there with `cp`, as `files.json` in the cache. If the read answers that no list of files is served for this version, save nothing as `files.json` and go on.
- **READ**: `action: "read"` (`"read_file"`) with `url` and the file's `path`, or several as `paths`. The answer says where on this machine each file was saved: copy it from there with `cp`.
- **MAKE**: these two calls stand in for the tool's `quickstart`. To look for the type, `action: "list"` with `scope: "types"` (`action: "list_types"`): each row is a type's title and its `type_url`. If the answer says that more types exist than it shows, list again with `type_query: "Design System"`. To make the artifact, `action: "publish"` with that `type_url`, the name as `title`, `auto_open: "after_first_write"`, and no file. The answer gives the new artifact's link.
- **PUBLISH**: open the call file, and call `Artifact` with the arguments it holds and no others. Where the call file has `overwrite_unread`, it names the files this sync replaces: the plan compared each one, and you asked the user where that was needed. Keep it as it is, whatever the tool's description says of that key, and make no LIST between a plan and its calls: a LIST there would let these names pass a change made after the plan. An artifact that this session did not MAKE has to be read once before the session's first PUBLISH: `action: "read"` with `url` alone. That answer brings the type's instructions for filling a design system by hand; the call files do the filling, so go on with them.

**Size.** The tool lists 1,024 of an artifact's files, the type's own among them, and a publish may remove only a file that the session has seen listed or has read. A design system comes to two files a component, and its fonts, guidelines and a dozen more. Where the repo has over 450 components, tell the user before the build that a system of this size can't be published from this session yet, and ask whether to build and verify locally all the same. Do the same where `ANCHORED` has `cutAfter`: a moved design system keeps its old files until the sync finishes, and its old and new files together would be more than the tool lists. (The tool's description gives a lower number of files as a version's limit. It doesn't apply to an artifact of this type.)

**If the `Artifact` tool is gone from this session** in the middle of a run, its tools have changed. Tell the user, and ask them to run /design-sync again: it goes on with the same artifact.

What a refusal means:

- **"This session has read-only access to this artifact"**: its owner can give the user edit access on claude.ai. Until then, the user can't publish to this artifact, whatever else the refusal offers.
- **"this publish touches files whose published content is not what you last saw"**: READ each file the refusal names, several at once as `paths`, without copying them into the cache. After that, treat it as: the artifact changed since the listing.
- **"You haven't viewed the latest version of this artifact"**, **"is live and this publish was not built on it"**, or **"Publish again in your next turn"**: read the artifact again, `action: "read"` with `url` alone. After that, treat it as: the artifact changed since the listing.
