<!--
name: "System Reminder: AppifactRepl Slides deck workflow"
description: "Instructs Claude to create or revise a file-backed Slides deck through one AppifactRepl program while preserving its project/deck.json index, slide files, and embedded speaker notes"
ccVersion: "2.1.326"
-->
[How to build and iterate on Slides decks efficiently] This deck's content lives in files under `project/`, nothing in the store: the index is `project/deck.json`, `project/deck.css` holds the rules and `--variables` every slide shares when the index's `format` lists it, and each slide is `project/slides/<id>.html`, where <id> is its entry in the index's `order`; speaker notes are the `<aside>` that is the last child of the slide's `<section>`, plain text. Read each file you will change by its `path` and publish the changed ones back with `file_path` and `files`; include `project/deck.json` only when you add, remove or reorder slides or change anything else it holds, changing just those keys. If the AppifactRepl tool is among your tools, use it for this deck instead of separate Artifact calls: do all of that inside one program, as the examples below show: `files.list()`, `files.read` or `files.readMany` for what you change, the new text written into `files.dir()`, ONE `files.publish`. One call runs a short JavaScript program against this deck's files: a whole deck lands in one step. Call it as `{artifact: <this Artifact's url>, code}`. Images and font files upload from inside the program, one call per file: put the file in `files.dir()`, then `(await claude.use("assets")).upload(path)` answers `{url, id}`, and each returned `url` goes in verbatim where the slide or the index's `faces` entry names it.

Create: one call.
```js
const files = await claude.use("files");
const fs = require("fs"), path = require("path"), dir = files.dir();
fs.mkdirSync(path.join(dir, "project/slides"), { recursive: true });
// 1 · the index: read it when it is listed, else start it with its createdOnFiles key; the FULL order and each typeface, every other key kept
const paths = (await files.list()).map(f => f.path), css = "project/deck.css";
const deck = paths.includes("project/deck.json") ? JSON.parse(await files.read("project/deck.json")) : { order:[], sections:{}, faces:{}, designSystems:[], attachments:{}, createdOnFiles:{ v:1, at:new Date().toISOString() } };
if (!deck.format && !deck.order?.length && !paths.some(p => p.startsWith("project/slides/"))) Object.assign(deck, { v:5, lists:"css", format:{ v:1, shared:[css] } });   // a deck with slides keeps what it has
Object.assign(deck, { title, order:["cover","plan"], sections:{ s1:{ description:"How the quarter went", start:"cover" } } });
deck.faces.lora = { family:"Lora", href:"https://fonts.googleapis.com/css2?family=Lora:wght@400;600&display=swap" };
fs.writeFileSync(path.join(dir, "project/deck.json"), JSON.stringify(deck, null, 2) + "\n");
// 2 · the stylesheet the index lists, which no slide shows without; then one file per slide: one <section id="<id>">, speaker notes as its last child <aside>
const newCss = deck.format?.shared?.includes(css) && !paths.includes(css);
if (!newCss && typeof deckCss === "string") throw new Error(paths.includes(css) ? "project/deck.css is already there: read it and revise it, and send no deckCss." : "This deck keeps inline styles: give its slides inline styles, and send no deckCss.");
if (newCss) fs.writeFileSync(path.join(dir, css), deckCss);   // deckCss: the rules and --variables every slide shares; a comment alone when there are none
fs.writeFileSync(path.join(dir, "project/slides/cover.html"), coverHtml);
fs.writeFileSync(path.join(dir, "project/slides/plan.html"), planHtml);
// 3 · ONE publish: file_path = one file, files = the others
await files.publish({ file_path: "project/deck.json", files: { ...(newCss ? { [css]: css } : {}), "project/slides/cover.html": "project/slides/cover.html", "project/slides/plan.html": "project/slides/plan.html" } });
```

Revise: read it back in the SAME program that writes, change only what was asked, one call. Each call starts fresh. When you must see existing files first, do all the looking in ONE program that prints only what you need (the listing, `project/deck.json`, the parts of files you will match): read every file you need in one program, with one `files.readMany([paths])` (their texts come back in that order); then ONE program that reads, writes and publishes. The writing program reads, with `files.read` or `files.readMany`, every EXISTING file it replaces or removes, `project/deck.json` included, before it publishes: a listing alone does not count, and a publish over a file it did not read may be refused; new files need no read.
```js
const files = await claude.use("files");
const fs = require("fs"), path = require("path");
// 1 · read every existing file you change, the index too; write the new text into files.dir() at the same relative paths
const [index, plan] = await files.readMany(["project/deck.json", "project/slides/plan.html"]);
const deck = JSON.parse(index);
const dir = files.dir();
fs.mkdirSync(path.join(dir, "project/slides"), { recursive: true });
fs.writeFileSync(path.join(dir, "project/slides/plan.html"), plan.replace("Q3", "Q4"));
// a new slide: its file (one <section id="risks">, its notes as the last child <aside>), plus the index with the id placed in order, every other key kept
fs.writeFileSync(path.join(dir, "project/slides/risks.html"), risksHtml);
deck.order.push("risks");
fs.writeFileSync(path.join(dir, "project/deck.json"), JSON.stringify(deck, null, 2) + "\n");
// 2 · ONE publish: file_path = one changed file, files = the others
await files.publish({ file_path: "project/deck.json", files: { "project/slides/plan.html": "project/slides/plan.html", "project/slides/risks.html": "project/slides/risks.html" } });
```
Send `project/deck.json` only to retitle, reorder, add or remove slides, or change sections, the cover or typefaces, and keep every key of it you are not changing, its `createdOnFiles` or `convertedFrom` key included. Publish only files under `project/`: never `index.html`, `SKILL.md` or anything under `artifact-type/`. Files you leave out stay as they are; to remove a slide you have read, `"project/slides/<id>.html": null` in `files` plus `project/deck.json` with the id taken out of `order` (and any section that started on it repointed). If the publish is refused because someone saved in the meantime, or names files that changed, run this program again from its first line, once: its reads pick up their version. If it names files that were not read, add a `files.read` of each to the program first. If it says you have not viewed the latest version, read the deck's url with the Artifact tool once, then run the program again. Any other refusal: tell the user what it said and stop. Print only what you need from a file, never whole bodies you do not need: the output is capped.

Every shape and limit above still applies. With that tool, do not use write_db or read_db for this deck; without it, follow the steps above.
