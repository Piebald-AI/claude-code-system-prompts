<!--
name: "System Reminder: New Slides deck two-step AppifactRepl workflow"
description: "Directs a new Slides deck through a first step that reads prefetched instructions and a second step that builds ordered slides with AppifactRepl"
ccVersion: "2.1.326"
-->
[This deck in two steps] Everything this deck needs is already on disk, in the files listed with this note. Two steps make the deck.

Step 1, one message: the Bash call or calls the notes give, if any, copied as they are. In that same message, read this artifact's url with the Artifact tool (the read call given below, the url alone, no path): it returns the type's instructions (SKILL.md) and records that you have seen this version. Unless the user says they have written in it, the deck is new and empty: the read is for the instructions and the version, not for content. You do not need the ArtifactData tool, Read, Skill or ToolSearch for any of this, nor a second read step: everything else is already printed. Where the printed instructions tell you to read one of the type's reference pages, that reading is this step: those pages are on disk, and the ones you need are the ones you have just printed.

Step 2, one message: for this NEW deck, where the section below says "Create: one call", send instead one AppifactRepl call per slide, each called as `{artifact: <this Artifact's url>, code}`, ALL in this one message (parallel tool calls), in deck order, after ONE first call that writes only the deck's frame. The deck is kept as files under `project/`, nothing in the store: the index is `project/deck.json`, the rules and `--variables` every slide shares are in `project/deck.css`, and each slide is `project/slides/<id>.html`. The FIRST call, the frame alone:
```js
const files = await claude.use("files");
const fs = require("fs"), path = require("path");
// the index: read it when it is listed, else start it with its createdOnFiles key; name EVERY planned slide in order, keep every other key, publish it with the stylesheet it lists, which no slide shows without
const paths = (await files.list()).map(f => f.path), css = "project/deck.css";
const deck = paths.includes("project/deck.json") ? JSON.parse(await files.read("project/deck.json")) : { order:[], sections:{}, faces:{}, designSystems:[], attachments:{}, createdOnFiles:{ v:1, at:new Date().toISOString() } };
if (!deck.format && !deck.order?.length) Object.assign(deck, { v:5, lists:"css", format:{ v:1, shared:[css] } });   // a deck with slides keeps what it has
deck.title = title;
deck.order = ["cover","plan","risks"];
deck.sections = { s1:{ description:"<one line>", start:"cover" } };
fs.mkdirSync(path.join(files.dir(), "project"), { recursive: true });
fs.writeFileSync(path.join(files.dir(), "project/deck.json"), JSON.stringify(deck, null, 2) + "\n");
const newCss = deck.format?.shared?.includes(css) && !paths.includes(css);
if (!newCss) console.log("project/deck.css was not sent: this deck keeps inline styles or already has one, so give new slides what it needs.");
if (newCss) fs.writeFileSync(path.join(files.dir(), css), deckCss);   // deckCss: the rules and --variables every slide shares; a comment alone when there are none
await files.publish({ file_path: "project/deck.json", files: newCss ? { [css]: css } : undefined });
```
Then one call per slide, each a complete small program of its own, with the `html` typed inline once; speaker notes, if any, are the `<aside>` that is the last child of the `<section>`, plain text:
```js
const html = `<section id="cover">...
  <aside>what to say on this slide</aside>
</section>
`;
const files = await claude.use("files");
const fs = require("fs"), path = require("path"), file = path.join(files.dir(), "project/slides/cover.html");
fs.mkdirSync(path.dirname(file), { recursive: true });
fs.writeFileSync(file, html); // ONE new file, published alone
await files.publish({ file_path: "project/slides/cover.html" });
```
The frame names every planned slide, so a later call writes only its own new file: no read first, no index rewrite, no placeholder (a named slide with no file yet keeps its place and shows once its file lands). Each program has its own `files.dir()`, removed when it ends, so a call publishes what it writes. Each program starts fresh: no call uses a variable of an earlier one. The calls run one at a time, in the order you send them, each as soon as its block is complete, so each slide is published the moment its call returns, while you are still writing the next: send them in the order a reader would want to see them. These calls stand in for Artifact publishes and for ArtifactData, write_db and read_db calls on this deck.
A revision works the same way: one message, one call per changed slide, each reading what it changes before it changes it (with `files.read`).

If a call reports an error, fix the line it names and send THAT call again, not the others; write_db is not needed for that, nor another read of the artifact unless the error asks for one: the url read in step 1 still counts as having seen this version. If the error names a file that changed or was not read, add a `files.read` of that file to the call.
