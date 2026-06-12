<!--
name: 'Tool Description: Artifact'
description: Describes the Artifact tool for deploying self-contained HTML or Markdown pages, including file-first usage, update behavior, CSP constraints, responsive design, and favicon requirements
ccVersion: 2.1.176
-->
Render an HTML or Markdown file to an Artifact — a default-private web page hosted on claude.ai that the user can later choose to share with their teammates. Use this when communicating visually with an image, diagram, or rich HTML/Markdown would be clearer than terminal text.

Write the content to a file first (via Write/Edit), then call Artifact with its path.

**Content**: Disclose progressively: high level first, supporting detail next. Assume the reader wasn't in the session — what's obvious from the transcript isn't obvious to them. Balance brevity with depth: skimmable at the top, complete underneath.

**Design**: Design is for information hierarchy — the page should be visually easier to parse than plain text, or it shouldn't be a page. Use size, weight, color, and space to make the important things unmissable and the supporting things quiet. Commit to a clear aesthetic direction. System font stacks are fine (the CSP blocks font CDNs).

**Title**: Set a concise `<title>` in the HTML — it names the artifact in the browser tab, gallery, and lists. Keep it stable across redeploys unless the page's purpose genuinely changes; files without one fall back to the basename, so still pick a short, distinctive filename (e.g. `token-usage.html`).

**To update**: Edit the file, then call Artifact again with the same file path — it redeploys to the same URL. A different file path claims a new URL so only use a different path if you intend to create a separate new Artifact.

**To update an artifact the user gives you a URL for** (an artifact link not published in this session): pass the URL as `url`. Without it, a fresh session always mints a new URL — there is no other way to target an existing one.

**To read an existing artifact's content**: call WebFetch with its URL.

**Self-contained only**: A strict CSP blocks requests to any external host — CDN scripts, external stylesheets, fonts, remote images, fetch/XHR/WebSockets. Blocked resources don't error the page; it just renders without them. Relative paths won't resolve (nothing else is deployed alongside the page). Inline all CSS/JS and embed assets as data: URIs.

**Responsive**: viewport is unknown and could be a mobile device or a desktop browser. Use relative units (%, vw/vh, em), flexbox/grid, `max-width:100%` on images. Wide content (tables, diagrams, code blocks) must scroll inside its own container — wrap it in an `overflow-x: auto` div. The page body must never scroll horizontally.

**Favicon** (required): Pass one or two emoji as `favicon` (e.g. `"📊"`, `"🐛"`, `"⚡🔥"`). It becomes the browser-tab icon. Emoji only — no SVG, no markup. Keep it the **same** across redeploys of an artifact — users find their tab by its icon, and a changed favicon reads as a different page. Only pick a new emoji on a hard pivot in what the artifact is about (new investigation, new deliverable), not for incremental updates.
