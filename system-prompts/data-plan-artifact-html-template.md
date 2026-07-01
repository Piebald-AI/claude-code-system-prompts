<!--
name: 'Data: Plan artifact HTML template'
description: Standalone HTML template used for published plan artifacts, including layout, fill contract, and light/dark styling
ccVersion: 2.1.198
-->
<!--
name: plan
description: Implementation plans, technical designs, RFCs, and architecture proposals — a phased document with context, approach, and verification sections.
fill contract: the automatic publish path (src/frame/planArtifactHtml.ts) fills this
  mechanically — {{TITLE}}, {{EYEBROW}}, and {{SUMMARY}} are replaced by a fixed regex,
  and everything from the first <section> through the LAST </section> is replaced
  wholesale by the rendered plan body. Keep those three slots and the section run, and
  put nothing after the last </section> except </article>; tests in
  test/frame/planArtifactHtml.test.ts assert this shape.
style: colors and spacing mirror @ant/cds tokens (comfortable density) as
  literals — a published artifact is standalone, so it cannot import the package.
  Typography is deliberately a plain system stack — no Anthropic brand fonts
  and no serif voice (owner + brand call, thread ts 1782852395) — and the
  light background is white rather than the CDS cream surface-0; those are
  the deliberate deviations from CDS values. Dark mode keys off
  prefers-color-scheme (the standalone equivalent of CDS data-mode).
-->
<title>{{TITLE}}</title>
<style>
  :root {
    color-scheme: light;
    /* @ant/cds purpose tokens, comfortable density, light mode */
    --cds-surface-0: #ffffff;
    --cds-text-primary: #0b0b0b;
    --cds-text-secondary: #52514e;
    --cds-text-muted: #898781;
    --cds-text-accent: #184f95;
    --cds-fill-accent: #2a78d6;
    --cds-border: rgb(11 11 11 / 10%);
    --cds-border-strong: rgb(11 11 11 / 20%);
    --cds-border-stronger: rgb(11 11 11 / 40%);
    --cds-fill-control: rgb(11 11 11 / 10%);
    --cds-font-sans: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    --cds-font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
    --cds-radius: 8px;
    --cds-gap-xs: 8px;
    --cds-gap-sm: 12px;
    --cds-gap-md: 16px;
    --cds-gap-lg: 28px;
    --cds-gap-xl: 40px;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      color-scheme: dark;
      --cds-surface-0: #0d0d0d;
      --cds-text-primary: #ffffff;
      --cds-text-secondary: #c3c2b7;
      --cds-text-muted: #898781;
      --cds-text-accent: #6da7ec;
      --cds-border: rgb(255 255 255 / 10%);
      --cds-border-strong: rgb(255 255 255 / 20%);
      --cds-border-stronger: rgb(255 255 255 / 40%);
      --cds-fill-control: rgb(255 255 255 / 10%);
    }
  }
  body {
    background: var(--cds-surface-0);
    color: var(--cds-text-primary);
    font: 14px/1.5 var(--cds-font-sans);
    overflow-wrap: break-word;
  }
  article {
    max-width: 76ch;
    margin: 0 auto;
    padding: var(--cds-gap-xl) 24px 72px;
    display: flex;
    flex-direction: column;
    gap: var(--cds-gap-xl);
  }
  header { display: flex; flex-direction: column; gap: var(--cds-gap-sm); }
  .eyebrow {
    font: 600 12px/14px var(--cds-font-sans);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--cds-text-accent);
  }
  /* Document heading scale: 24/19/16/14 over the 14px body (~1.19 steps).
     Deliberately looser than the closed CDS UI scale — a long document
     needs more size differentiation between levels than app chrome does
     (owner call, thread ts 1782848120). */
  h1 {
    font: 600 24px/30px var(--cds-font-sans);
    letter-spacing: -0.01em;
    text-wrap: balance;
    margin: 0;
  }
  h2 {
    font: 600 19px/25px var(--cds-font-sans);
    text-wrap: balance;
    margin: 0;
  }
  h3 {
    font: 600 16px/22px var(--cds-font-sans);
    text-wrap: balance;
    margin: 0;
  }
  h4, h5, h6 {
    font: 600 14px/20px var(--cds-font-sans);
    text-wrap: balance;
    margin: 0;
  }
  section { display: flex; flex-direction: column; gap: var(--cds-gap-md); }
  /* Heading rhythm inside the single mechanical-fill section: headings group
     with the content below them, not the paragraph above. Inert in the
     skill's multi-section flow, where each h2 is its section's first child. */
  section > :is(h2, h3, h4):not(:first-child) { margin-top: var(--cds-gap-sm); }
  section > h2:not(:first-child) { margin-top: var(--cds-gap-md); }
  p, li { margin: 0; max-width: 68ch; }
  .lede { font-size: 15px; line-height: 1.5; color: var(--cds-text-secondary); }
  .lede:empty { display: none; }
  a { color: var(--cds-text-accent); }
  code {
    font: 0.92em/1.5 var(--cds-font-mono);
    background: var(--cds-fill-control);
    padding: 1px 3px;
    border-radius: 4px;
  }
  a > code { background: none; color: inherit; }
  pre {
    font: 13px/19px var(--cds-font-mono);
    background: var(--cds-fill-control);
    border: 1px solid var(--cds-border);
    border-radius: var(--cds-radius);
    padding: var(--cds-gap-sm) var(--cds-gap-md);
    overflow-x: auto;
    margin: 0;
  }
  pre code { background: none; padding: 0; font: inherit; }
  blockquote {
    border-left: 2px solid var(--cds-border-strong);
    padding-left: var(--cds-gap-sm);
    color: var(--cds-text-secondary);
    margin: 0;
  }
  table {
    display: block;
    width: max-content;
    max-width: 100%;
    overflow-x: auto;
    border-collapse: collapse;
    font-variant-numeric: tabular-nums;
  }
  th, td {
    text-align: left;
    vertical-align: top;
    padding: var(--cds-gap-xs) var(--cds-gap-sm);
    border-bottom: 1px solid var(--cds-border);
  }
  th {
    font: 600 12px/14px var(--cds-font-sans);
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--cds-text-secondary);
    border-bottom-color: var(--cds-border-strong);
  }
  ul, ol { margin: 0; padding-left: 1.25rem; display: flex; flex-direction: column; gap: var(--cds-gap-xs); }
  /* Task-list items: the box replaces the bullet in the same gutter, and the
     native disabled-checkbox rendering (dim, sub-pixel) is replaced with a
     CDS-colored box so checks read at a glance in both modes. fill-accent
     has no dark override in CDS, so the white check passes contrast in both.
     Both tight (`li > input`) and loose (`li > p > input` — marked wraps
     multi-block items in <p>) task-list shapes are covered. */
  li:has(> input[type="checkbox"]),
  li:has(> p:first-child > input[type="checkbox"]:first-child) {
    list-style: none;
    margin-left: -1.25rem;
  }
  :is(li, li > p:first-child) > input[type="checkbox"] {
    appearance: none;
    width: 14px;
    height: 14px;
    border: 1.5px solid var(--cds-border-stronger);
    border-radius: 4px;
    background: var(--cds-surface-0);
    margin: 0 6px 0 0;
    vertical-align: -2px;
  }
  :is(li, li > p:first-child) > input[type="checkbox"]:checked {
    background: var(--cds-fill-accent) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'%3E%3Cpath d='M2.5 6.5 5 9l4.5-5.5' fill='none' stroke='%23fff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/10px 10px no-repeat;
    border-color: var(--cds-fill-accent);
  }
  /* Loose / multi-block list items: space the blocks inside an item. */
  :is(li, td, th) > * + :is(p, ul, ol, blockquote, pre) { margin-top: var(--cds-gap-xs); }
  img { max-width: 100%; height: auto; border-radius: var(--cds-radius); }
  hr { border: none; border-top: 1px solid var(--cds-border); margin: 0; }
</style>

<article>
  <header>
    <span class="eyebrow">{{EYEBROW}}</span>
    <h1>{{TITLE}}</h1>
    <p class="lede">{{SUMMARY}}</p>
  </header>

  <section>
    <h2>Context</h2>
    <!-- SLOT: context -->
  </section>

  <section>
    <h2>Approach</h2>
    <!-- SLOT: approach -->
  </section>

  <section>
    <h2>Phases</h2>
    <!-- SLOT: phases -->
  </section>

  <section>
    <h2>Verification</h2>
    <!-- SLOT: verification -->
  </section>
</article>
