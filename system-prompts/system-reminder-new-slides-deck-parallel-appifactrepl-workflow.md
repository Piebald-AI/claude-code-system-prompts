<!--
name: "System Reminder: New Slides deck parallel AppifactRepl workflow"
description: "Directs a new Slides deck to be framed and populated through ordered parallel AppifactRepl calls, one per slide"
ccVersion: "2.1.326"
-->
One AppifactRepl call per slide, all calls in one message (parallel tool calls), in deck order. Call it as {artifact: <the new Artifact's url>, code}. The calls run one at a time, in the order you send them, each as soon as its block is complete, so the page shows each slide the moment its call returns, while you are still writing the next.
The deck is kept as files under `project/`, none of it in the store. The FIRST call writes only the deck's index, `project/deck.json`, naming EVERY planned slide in order, and the stylesheet it lists, `project/deck.css`, with the rules and `--variables` every slide shares; no slide shows until that file lands:
```js
const files = await claude.use("files"), fs = require("fs"), path = require("path");
const index = "project/deck.json", css = "project/deck.css", paths = (await files.list()).map(f => f.path), made = paths.includes(index);   // the page may have made the index already: keep its keys
const deck = { sections:{}, faces:{}, designSystems:[], attachments:{}, createdOnFiles:{ v:1, at:new Date().toISOString() }, ...(made ? JSON.parse(await files.read(index)) : {}) };
if (!deck.format && !deck.order?.length) Object.assign(deck, { v:5, lists:"css", format:{ v:1, shared:[css] } });   // a deck with slides keeps what it has
deck.title = title;
deck.order = ["cover","plan","risks"];
deck.sections = { s1:{ description:"<one line>", start:"cover" } };
deck.faces = { lora:{ family:"Lora", href:"https://fonts.googleapis.com/css2?family=Lora:wght@400;600&display=swap" } };
fs.mkdirSync(path.join(files.dir(), "project"), { recursive: true });
fs.writeFileSync(path.join(files.dir(), index), JSON.stringify(deck));
const newCss = deck.format?.shared?.includes(css) && !paths.includes(css);
if (!newCss) console.log("project/deck.css was not sent: this deck keeps inline styles or already has one, so give new slides what it needs.");
if (newCss) fs.writeFileSync(path.join(files.dir(), css), deckCss);   // deckCss: the rules and --variables every slide shares; a comment alone when there are none
await files.publish({ file_path: index, files: newCss ? { [css]: css } : undefined });
```
Then one call per slide, each a complete small program of its own, with the html typed inline:
```js
const files = await claude.use("files"), fs = require("fs"), path = require("path");
const slide = "project/slides/cover.html", file = path.join(files.dir(), slide);
fs.mkdirSync(path.dirname(file), { recursive: true });
fs.writeFileSync(file, `<section id="cover">...</section>`);
await files.publish({ file_path: slide });
```
The index names every planned slide, so each later call writes only its own new file (a named slide with no file yet keeps its place and shows once its file lands). Each program starts fresh: no call uses a variable of an earlier one, and each has its own `files.dir()`, removed when it ends, so a call publishes what it writes. These calls stand in for Artifact publishes and for ArtifactData, write_db and read_db calls on this deck. With a design system, the colours, type and spacing are the ones in the files you printed.
A revision works the same way: one message, one call per changed slide, each reading the file it changes before it changes it:
```js
const files = await claude.use("files"), fs = require("fs"), path = require("path");
const slide = "project/slides/plan.html", file = path.join(files.dir(), slide), html = await files.read(slide);
fs.mkdirSync(path.dirname(file), { recursive: true });
fs.writeFileSync(file, html.replace("Q3", "Q4"));
await files.publish({ file_path: slide });
```
If a call reports an error, fix the line it names and send THAT call again, not the others. If the error names a file that changed or was not read, add a `files.read` of that file to the call.
