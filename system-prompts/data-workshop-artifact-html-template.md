<!--
name: "Data: Workshop artifact HTML template"
description: "Standalone HTML template used for published workshop artifacts, including decision rendering, fill contract, interaction controls, and light/dark styling"
ccVersion: "2.1.216"
-->
<!--
name: workshop
description: An iteratively-republished decision document — the model presents choices as decision blocks, the reader answers from the published page, and the session republishes updated contents until the workshop is finalized.
fill contract: the automatic publish path (src/frame/planArtifactHtml.ts
  renderWorkshopArtifact) fills this mechanically — {{TITLE}}, {{TAB_TITLE}},
  {{EYEBROW}}, and {{SUMMARY}} are replaced by a fixed regex ({{TAB_TITLE}} is the
  <title> element and keeps the workshop FILENAME while the h1 shows the document
  heading), and everything from the first <section> through the LAST </section> is
  replaced wholesale by the rendered body (decision fences become call-items).
  Keep those four slots and the section run, and put nothing after the last
  </section> except </article>; tests in test/frame/decisionBlocks.test.ts
  assert the decision styling and test/frame/planArtifactHtml.test.ts the shape.
style: tokens come from @ant/cds's own vanilla export, embedded verbatim
  (a published artifact is standalone, so the generated tokens.vanilla.css is
  vendored and inlined rather than imported; a drift test keeps it canonical).
  Typography is deliberately a plain system stack — no Anthropic brand fonts
  and no serif voice — and the light background is white rather than the
  CDS cream surface-0; those are the deliberate deviations from CDS values.
  Dark mode keys off both theme axes: prefers-color-scheme, and the viewer
  toggle's data-theme root stamp (mirrored onto data-mode by the script
  below so the vendored token block's own toggle selectors serve it).
-->
<title>{{TAB_TITLE}}</title>
<script>
  /* The viewer toggle stamps data-theme on the root element; the vendored
     CDS token block below keys its toggle axis on data-mode (the CDS
     convention) and cannot be edited (provenance-tested byte-identical).
     Mirroring the attribute lets that block serve the viewer toggle with
     its own precedence rules — toggle beats OS in both directions. Static,
     no author bytes. Without JS the toggle axis is inert and the OS axis
     (pure CSS) still themes the page. */
  (function () {
    var root = document.documentElement;
    var sync = function () {
      var t = root.getAttribute('data-theme');
      if (t) root.setAttribute('data-mode', t);
      else root.removeAttribute('data-mode');
    };
    sync();
    if (typeof MutationObserver !== 'undefined') {
      new MutationObserver(sync).observe(root, {
        attributes: true,
        attributeFilter: ['data-theme'],
      });
    }
  })();
</script>
<style>
  /* ===== BEGIN vendored @ant/cds tokens (src/frame/cdsTokens.vanilla.generated.css) =====
     Byte-identical to that file (drift-tested in test/frame/planArtifactHtml.test.ts).
     Do not edit this block: refresh the vendored file from @ant/cds and re-embed. */
/*
 * VENDORED — verbatim copy of @ant/cds tokens.vanilla.css (the CDS team's
 * framework-agnostic token export) from anthropics/apps@230786b7e9757b07527ac4283db9b19676a8ae91
 * (packages/cds/src/generated/tokens.vanilla.css).
 * upstream-sha256: 94f136cf38cc5f54c1b6dda76677c466b122f6b7e6f8702ef18774cbc7643152
 *   (sha256 of everything below this header comment, i.e. of the raw
 *   upstream file — recomputed and asserted by the "provenance hash"
 *   test, so a refresh that swaps bytes without updating this line
 *   fails CI rather than shipping a lying header.)
 *
 * Browser floor: the export uses hsl(from …) and color-mix() — ~Chrome 119 /
 * Safari 16.4. On older viewers the consuming declarations are dropped
 * SILENTLY (no error, no telemetry): borders, the alpha ramp, and dark
 * surfaces degrade. This line is the triage breadcrumb for "published
 * artifact looks broken" reports — ask the browser version first.
 *
 * The plan-artifact template embeds this file byte-for-byte between
 * BEGIN/END markers; a drift test asserts the two stay identical. To
 * refresh: copy the upstream generated file below this header, update the
 * commit hash and upstream-sha256 above, run
 * `bun scripts/embed-cds-tokens.ts`, then
 * `bun test test/frame/planArtifactHtml.test.ts`.
 */

/**
 * GENERATED — do not edit. Run `yarn workspace @ant/cds gen:tokens`.
 *
 * Framework-agnostic CDS token export: unprefixed `--*` custom
 * properties under `:root`, with dark-mode overrides under
 * `[data-mode="dark"]` and `@media (prefers-color-scheme: dark)`.
 * No `.cds-root` scoping, density steps, or component-private tokens.
 *
 * Source: `packages/cds/tokens/`. For the full React/Tailwind build
 * (scoped under `.cds-root`), see `tokens.css`.
 */

:root {
  --radius: 8px;
  --h-control: 32px;
  --h-control-nested: 22px;
  --icon: 20px;
  --pad-sm: 8px;
  --pad-md: 12px;
  --pad-lg: 16px;
  --pad-xl: 24px;
  --gap-xs: 8px;
  --gap-sm: 12px;
  --gap-md: 16px;
  --gap-lg: 28px;
  --gap-xl: 40px;
  --outset-x: 0px;
  --outset-y: 0px;
  --border: var(--alpha-2);
  --border-accent: var(--blue-250);
  --border-danger: var(--red-250);
  --border-success: var(--green-250);
  --border-warning: var(--yellow-250);
  --border-pro: var(--violet-250);
  --border-git-added: color-mix(in srgb, var(--text-git-added) 40%, transparent);
  --border-git-removed: color-mix(in srgb, var(--text-git-removed) 40%, transparent);
  --border-git-modified: color-mix(in srgb, var(--text-git-modified) 40%, transparent);
  --border-git-merged: color-mix(in srgb, var(--text-git-merged) 40%, transparent);
  --border-git-closed: color-mix(in srgb, var(--text-git-closed) 40%, transparent);
  --border-git-conflicting: color-mix(in srgb, var(--text-git-conflicting) 40%, transparent);
  --border-git-draft: color-mix(in srgb, var(--text-git-draft) 40%, transparent);
  --border-git-opened: var(--border-git-added);
  --border-git-queued: var(--border-git-modified);
  --border-strong: var(--alpha-3);
  --border-stronger: hsl(from var(--neutral-900) h s l / 40%);
  --shadow-sm: 0 1px 2px 0 hsl(from var(--gray-900) h s l / 6%), 0 2px 8px 0 var(--shadow-color);
  --shadow-md: 0 2px 4px 0 hsl(from var(--gray-900) h s l / 7%), 0 6px 16px 0 var(--shadow-color);
  --shadow-lg: 0 4px 8px 0 hsl(from var(--gray-900) h s l / 8%), 0 12px 28px -2px var(--shadow-color);
  --shadow-color: hsl(from var(--gray-900) h s l / 8%);
  --shadow-popover: 0 8px 24px rgb(0 0 0 / 0.12), 0 2px 6px rgb(0 0 0 / 0.08);
  --ring-outer: 1px;
  --ring-inner: 0px;
  --ring-color: var(--border);
  --focus-shadow: inset 0 0 0 1px var(--page-bg), 0 0 0 1px var(--fill-accent), 0 0 6px 1px var(--bg-accent);
  --font-mono: var(--font-anthropic-mono, "Anthropic Mono Variable"), "Anthropic Mono", "SF Mono", ui-monospace, Menlo, Consolas, monospace;
  --font-system: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-sans: var(--font-anthropic-sans, "Anthropic Sans Variable", "Anthropic Sans"), var(--font-system);
  --font-voice: var(--font-anthropic-serif, "Anthropic Serif Variable", "Anthropic Serif"), ui-serif, Georgia, "Times New Roman", serif;
  --ease-out: cubic-bezier(0.165, 0.84, 0.44, 1);
  --ease-snap: cubic-bezier(0.32, 0.72, 0, 1);
  --ease-overshoot: cubic-bezier(0.34, 1.3, 0.64, 1);
  --dur-fast: 60ms;
  --dur-snap: 120ms;
  --dur-base: 200ms;
  --dur-slow: 450ms;
  --btn-spring: linear(0, 0.2459, 0.6526, 0.9468, 1.0764, 1.0915, 1.0585, 1.0219, 0.9993, 0.9914, 0.9921, 0.9957, 0.9988, 1.0004, 1);
  --black: #000000;
  --oncolor-200: hsl(60 6.7% 97.1% / 0.75);
  --oncolor-300: hsl(60 6.7% 97.1% / 0.5);
  --clay: #d97757;
  --clay-emphasized: #c6613f;
  --heather: #cbcadb;
  --plum: #827dbd;
  --cactus: #bcd1ca;
  --mineral: #629987;
  --peach: #ebc9b7;
  --gray-0: #ffffff;
  --gray-10: #fcfcfb;
  --gray-20: #f9f9f7;
  --gray-30: #f6f6f4;
  --gray-40: #f3f3f0;
  --gray-50: #f0efec;
  --gray-60: #edece8;
  --gray-70: #eae9e4;
  --gray-80: #e7e6e1;
  --gray-90: #e4e3dd;
  --gray-100: #e1e0d9;
  --gray-150: #d2d1c7;
  --gray-200: #c3c2b7;
  --gray-250: #b4b3a8;
  --gray-300: #a5a49a;
  --gray-350: #97958d;
  --gray-400: #898781;
  --gray-450: #7b7974;
  --gray-500: #6d6b67;
  --gray-550: #5f5e5a;
  --gray-600: #52514e;
  --gray-650: #454442;
  --gray-700: #383835;
  --gray-750: #2c2c2a;
  --gray-800: #20201f;
  --gray-810: #1e1e1d;
  --gray-820: #1c1c1b;
  --gray-830: #1a1a19;
  --gray-840: #181817;
  --gray-850: #151515;
  --gray-860: #131313;
  --gray-870: #111111;
  --gray-880: #0f0f0f;
  --gray-890: #0d0d0d;
  --gray-900: #0b0b0b;
  --red-0: #ffffff;
  --red-10: #fffbfb;
  --red-20: #fef7f7;
  --red-30: #fef3f3;
  --red-40: #fdefef;
  --red-50: #fbebeb;
  --red-60: #fae7e7;
  --red-70: #fae3e3;
  --red-80: #fadfdf;
  --red-90: #fadada;
  --red-100: #fad6d6;
  --red-150: #f7c1c1;
  --red-200: #f4abab;
  --red-250: #f09595;
  --red-300: #ec7e7e;
  --red-350: #e66767;
  --red-400: #e34948;
  --red-450: #d03b3b;
  --red-500: #b93535;
  --red-550: #a32c2c;
  --red-600: #8e2626;
  --red-650: #791e1e;
  --red-700: #641919;
  --red-750: #511212;
  --red-800: #3c0e0e;
  --red-810: #380d0d;
  --red-820: #340c0c;
  --red-830: #310b0b;
  --red-840: #2d0a0a;
  --red-850: #280a0a;
  --red-860: #230b0a;
  --red-870: #1d0b0a;
  --red-880: #170c0b;
  --red-890: #110c0b;
  --red-900: #0b0b0b;
  --orange-0: #ffffff;
  --orange-10: #fefbfa;
  --orange-20: #fdf7f5;
  --orange-30: #fcf4f0;
  --orange-40: #faf0ec;
  --orange-50: #f9ece7;
  --orange-60: #f8e9e2;
  --orange-70: #f7e5dd;
  --orange-80: #f7e1d7;
  --orange-90: #f7dcd1;
  --orange-100: #f7d8cb;
  --orange-150: #f3c5b2;
  --orange-200: #f4ae94;
  --orange-250: #f09978;
  --orange-300: #ec835a;
  --orange-350: #eb6834;
  --orange-400: #d95926;
  --orange-450: #c25124;
  --orange-500: #ae461c;
  --orange-550: #993d19;
  --orange-600: #863311;
  --orange-650: #712b0f;
  --orange-700: #5d230b;
  --orange-750: #4b1b08;
  --orange-800: #371407;
  --orange-810: #341307;
  --orange-820: #301106;
  --orange-830: #2d1006;
  --orange-840: #290f06;
  --orange-850: #240e07;
  --orange-860: #1f0e08;
  --orange-870: #1a0e09;
  --orange-880: #150d0a;
  --orange-890: #100c0b;
  --orange-900: #0b0b0b;
  --yellow-0: #ffffff;
  --yellow-10: #fefcf8;
  --yellow-20: #fcf8f1;
  --yellow-30: #fbf5ea;
  --yellow-40: #f9f2e4;
  --yellow-50: #f9eeda;
  --yellow-60: #faebce;
  --yellow-70: #fae7c2;
  --yellow-80: #fae3b8;
  --yellow-90: #f9e0b0;
  --yellow-100: #f9dca4;
  --yellow-150: #f9c868;
  --yellow-200: #fab219;
  --yellow-250: #eda100;
  --yellow-300: #db9300;
  --yellow-350: #c98500;
  --yellow-400: #b77700;
  --yellow-450: #a66a00;
  --yellow-500: #945d00;
  --yellow-550: #835100;
  --yellow-600: #734500;
  --yellow-650: #623900;
  --yellow-700: #512e00;
  --yellow-750: #412400;
  --yellow-800: #311a00;
  --yellow-810: #2e1800;
  --yellow-820: #2b1700;
  --yellow-830: #271500;
  --yellow-840: #231402;
  --yellow-850: #1f1204;
  --yellow-860: #1b1106;
  --yellow-870: #171007;
  --yellow-880: #130e09;
  --yellow-890: #0f0d0a;
  --yellow-900: #0b0b0b;
  --green-0: #ffffff;
  --green-10: #fafdfa;
  --green-20: #f5fbf4;
  --green-30: #f0f9ef;
  --green-40: #ebf7e9;
  --green-50: #e5f4e4;
  --green-60: #e0f2de;
  --green-70: #dbf0d8;
  --green-80: #d5eed3;
  --green-90: #d0eccd;
  --green-100: #caeac7;
  --green-150: #aee0a9;
  --green-200: #91d68b;
  --green-250: #73cb6d;
  --green-300: #55bf50;
  --green-350: #35b231;
  --green-400: #0ca30c;
  --green-450: #009300;
  --green-500: #008300;
  --green-550: #007300;
  --green-600: #006300;
  --green-650: #005400;
  --green-700: #074506;
  --green-750: #0f350d;
  --green-800: #11260f;
  --green-810: #10230f;
  --green-820: #10210f;
  --green-830: #101e0f;
  --green-840: #101b0f;
  --green-850: #0f180e;
  --green-860: #0e160e;
  --green-870: #0e130d;
  --green-880: #0d100d;
  --green-890: #0c0e0c;
  --green-900: #0b0b0b;
  --aqua-0: #ffffff;
  --aqua-10: #f9fdfb;
  --aqua-20: #f3fbf8;
  --aqua-30: #edf9f4;
  --aqua-40: #e8f7f1;
  --aqua-50: #e2f4ed;
  --aqua-60: #dcf2ea;
  --aqua-70: #d5f0e6;
  --aqua-80: #ceefe2;
  --aqua-90: #c7eddf;
  --aqua-100: #bfebdb;
  --aqua-150: #a0e1c9;
  --aqua-200: #7ad7b4;
  --aqua-250: #5acba0;
  --aqua-300: #3bbd8c;
  --aqua-350: #1baf7a;
  --aqua-400: #199e70;
  --aqua-450: #138e65;
  --aqua-500: #0f7e5c;
  --aqua-550: #0e6e53;
  --aqua-600: #065f49;
  --aqua-650: #095040;
  --aqua-700: #034235;
  --aqua-750: #02342b;
  --aqua-800: #022720;
  --aqua-810: #02241e;
  --aqua-820: #02221c;
  --aqua-830: #021f1a;
  --aqua-840: #031c18;
  --aqua-850: #051a16;
  --aqua-860: #071713;
  --aqua-870: #081411;
  --aqua-880: #0a110f;
  --aqua-890: #0b0e0d;
  --aqua-900: #0b0b0b;
  --blue-0: #ffffff;
  --blue-10: #fafcff;
  --blue-20: #f5f9fe;
  --blue-30: #f0f7fe;
  --blue-40: #ebf4fc;
  --blue-50: #e7f1fb;
  --blue-60: #e2eefa;
  --blue-70: #ddebfa;
  --blue-80: #d7e8fa;
  --blue-90: #d2e5fa;
  --blue-100: #cde2fb;
  --blue-150: #b7d3f6;
  --blue-200: #9ec5f4;
  --blue-250: #86b6ef;
  --blue-300: #6da7ec;
  --blue-350: #5598e7;
  --blue-400: #3987e5;
  --blue-450: #2a78d6;
  --blue-500: #256abf;
  --blue-550: #1c5cab;
  --blue-600: #184f95;
  --blue-650: #104281;
  --blue-700: #0d366b;
  --blue-750: #062b57;
  --blue-800: #032042;
  --blue-810: #031e3d;
  --blue-820: #021c39;
  --blue-830: #021a36;
  --blue-840: #021831;
  --blue-850: #03162c;
  --blue-860: #051426;
  --blue-870: #07121f;
  --blue-880: #091018;
  --blue-890: #0a0d11;
  --blue-900: #0b0b0b;
  --violet-0: #ffffff;
  --violet-10: #fcfbff;
  --violet-20: #f8f8ff;
  --violet-30: #f5f4ff;
  --violet-40: #f2f1ff;
  --violet-50: #efedff;
  --violet-60: #ebeafe;
  --violet-70: #e8e6fe;
  --violet-80: #e5e2fd;
  --violet-90: #e2dffd;
  --violet-100: #dfdbfd;
  --violet-150: #cfcafb;
  --violet-200: #bfb9f5;
  --violet-250: #b0a7f2;
  --violet-300: #a096eb;
  --violet-350: #9085e9;
  --violet-400: #8173e3;
  --violet-450: #7161e0;
  --violet-500: #6250d6;
  --violet-550: #5645be;
  --violet-600: #4a3aa7;
  --violet-650: #3e318e;
  --violet-700: #322777;
  --violet-750: #271e60;
  --violet-800: #1d1649;
  --violet-810: #1b1544;
  --violet-820: #19133f;
  --violet-830: #17123b;
  --violet-840: #151036;
  --violet-850: #130f32;
  --violet-860: #110e2b;
  --violet-870: #0f0e23;
  --violet-880: #0e0d1b;
  --violet-890: #0c0c13;
  --violet-900: #0b0b0b;
  --magenta-0: #ffffff;
  --magenta-10: #fefbfc;
  --magenta-20: #fef6f9;
  --magenta-30: #fdf2f6;
  --magenta-40: #fbeff3;
  --magenta-50: #faebf0;
  --magenta-60: #f9e6ed;
  --magenta-70: #f9e2eb;
  --magenta-80: #f9dee8;
  --magenta-90: #f9d9e5;
  --magenta-100: #f9d4e2;
  --magenta-150: #f3c0d3;
  --magenta-200: #f3a8c3;
  --magenta-250: #ed93b4;
  --magenta-300: #e87ba4;
  --magenta-350: #e46191;
  --magenta-400: #d55181;
  --magenta-450: #c04873;
  --magenta-500: #ad3d66;
  --magenta-550: #993458;
  --magenta-600: #862a4c;
  --magenta-650: #722340;
  --magenta-700: #5e1c34;
  --magenta-750: #4c1429;
  --magenta-800: #390f1f;
  --magenta-810: #360d1c;
  --magenta-820: #320c1a;
  --magenta-830: #2f0b18;
  --magenta-840: #2b0a16;
  --magenta-850: #270a14;
  --magenta-860: #220a12;
  --magenta-870: #1c0b11;
  --magenta-880: #170b0f;
  --magenta-890: #110b0d;
  --magenta-900: #0b0b0b;
  --pictogram-highlight-default: var(--gray-80);
  --pictogram-highlight-heather: var(--heather);
  --pictogram-highlight-cactus: var(--cactus);
  --pictogram-highlight-peach: var(--peach);
  --cursor-interactive: pointer;
  --neutral-0: var(--gray-0);
  --neutral-10: var(--gray-10);
  --neutral-20: var(--gray-20);
  --neutral-30: var(--gray-30);
  --neutral-40: var(--gray-40);
  --neutral-50: var(--gray-50);
  --neutral-60: var(--gray-60);
  --neutral-70: var(--gray-70);
  --neutral-80: var(--gray-80);
  --neutral-90: var(--gray-90);
  --neutral-100: var(--gray-100);
  --neutral-150: var(--gray-150);
  --neutral-200: var(--gray-200);
  --neutral-250: var(--gray-250);
  --neutral-300: var(--gray-300);
  --neutral-350: var(--gray-350);
  --neutral-400: var(--gray-400);
  --neutral-450: var(--gray-450);
  --neutral-500: var(--gray-500);
  --neutral-550: var(--gray-550);
  --neutral-600: var(--gray-600);
  --neutral-650: var(--gray-650);
  --neutral-700: var(--gray-700);
  --neutral-750: var(--gray-750);
  --neutral-800: var(--gray-800);
  --neutral-810: var(--gray-810);
  --neutral-820: var(--gray-820);
  --neutral-830: var(--gray-830);
  --neutral-840: var(--gray-840);
  --neutral-850: var(--gray-850);
  --neutral-860: var(--gray-860);
  --neutral-870: var(--gray-870);
  --neutral-880: var(--gray-880);
  --neutral-890: var(--gray-890);
  --neutral-900: var(--gray-900);
  --alpha-0: hsl(from var(--neutral-900) h s l / 0%);
  --alpha-1: hsl(from var(--neutral-900) h s l / 5%);
  --alpha-2: hsl(from var(--neutral-900) h s l / 10%);
  --alpha-3: hsl(from var(--neutral-900) h s l / 20%);
  --alpha-4: hsl(from var(--neutral-900) h s l / 35%);
  --alpha-5: hsl(from var(--neutral-900) h s l / 50%);
  --alpha-6: hsl(from var(--neutral-900) h s l / 60%);
  --alpha-7: hsl(from var(--neutral-900) h s l / 70%);
  --alpha-8: hsl(from var(--neutral-900) h s l / 85%);
  --alpha-9: hsl(from var(--neutral-900) h s l / 95%);
  --surface-0: var(--gray-20);
  --surface-1: var(--gray-10);
  --surface-2: var(--gray-0);
  --surface-3: var(--gray-0);
  --surface-popover: var(--surface-3);
  --surface-panel: var(--surface-2);
  --page-bg: var(--surface-0);
  --fill-accent: var(--blue-450);
  --fill-accent-hover: var(--blue-400);
  --fill-danger: var(--red-450);
  --fill-danger-hover: var(--red-400);
  --fill-success: var(--green-450);
  --fill-success-hover: var(--green-400);
  --fill-warning: var(--yellow-200);
  --fill-warning-hover: var(--yellow-250);
  --fill-pro: var(--violet-450);
  --fill-pro-hover: var(--violet-400);
  --fill-git-added: #1a8633;
  --fill-git-added-hover: #1e9b3b;
  --fill-git-removed: var(--text-git-removed);
  --fill-git-removed-hover: #de295f;
  --fill-git-modified: #8b751c;
  --fill-git-modified-hover: #a08720;
  --fill-git-merged: #855fd6;
  --fill-git-merged-hover: #9473db;
  --fill-git-closed: #ed0b00;
  --fill-git-closed-hover: #ff1307;
  --fill-git-conflicting: #b85b19;
  --fill-git-conflicting-hover: #c5621b;
  --fill-git-draft: var(--text-git-draft);
  --fill-git-draft-hover: #808080;
  --fill-git-opened: var(--fill-git-added);
  --fill-git-opened-hover: var(--fill-git-added-hover);
  --fill-git-queued: var(--fill-git-modified);
  --fill-git-queued-hover: var(--fill-git-modified-hover);
  --fill-brand: var(--clay-emphasized);
  --fill-brand-hover: var(--clay);
  --fill-primary: var(--neutral-900);
  --fill-primary-hover: var(--neutral-750);
  --fill-secondary: hsl(0 0% 100% / 0.1);
  --fill-secondary-hover: var(--alpha-1);
  --fill-secondary-ring: var(--border);
  --fill-field: hsl(0 0% 100% / 0.5);
  --fill-ghost-hover: var(--alpha-1);
  --fill-disabled: var(--alpha-1);
  --fill-control: var(--alpha-2);
  --fill-control-hover: var(--alpha-3);
  --bg-accent: var(--blue-100);
  --bg-danger: var(--red-100);
  --bg-success: var(--green-100);
  --bg-warning: var(--yellow-100);
  --bg-pro: var(--violet-100);
  --bg-git-added: color-mix(in srgb, var(--text-git-added) 20%, transparent);
  --bg-git-removed: color-mix(in srgb, var(--text-git-removed) 20%, transparent);
  --bg-git-modified: color-mix(in srgb, var(--text-git-modified) 20%, transparent);
  --bg-git-merged: color-mix(in srgb, var(--text-git-merged) 20%, transparent);
  --bg-git-closed: color-mix(in srgb, var(--text-git-closed) 20%, transparent);
  --bg-git-conflicting: color-mix(in srgb, var(--text-git-conflicting) 20%, transparent);
  --bg-git-draft: color-mix(in srgb, var(--text-git-draft) 20%, transparent);
  --bg-git-opened: var(--bg-git-added);
  --bg-git-queued: var(--bg-git-modified);
  --bg-neutral: var(--alpha-1);
  --bg-neutral-hover: var(--alpha-2);
  --backdrop: rgb(0 0 0 / 0.4);
  --text-accent: var(--blue-600);
  --text-danger: var(--red-600);
  --text-success: var(--green-600);
  --text-warning: var(--yellow-600);
  --text-pro: var(--violet-600);
  --text-git-added: #1e9e3c;
  --text-git-removed: #cd2054;
  --text-git-modified: #98801f;
  --text-git-merged: #8e6bd9;
  --text-git-closed: #ff3a30;
  --text-git-conflicting: #c5621b;
  --text-git-draft: #737373;
  --text-git-opened: var(--text-git-added);
  --text-git-queued: var(--text-git-modified);
  --text-primary: var(--neutral-900);
  --text-secondary: var(--neutral-600);
  --text-muted: var(--neutral-400);
  --text-disabled: var(--alpha-4);
  --font-size-caption: 12px;
  --font-size-footnote: 13px;
  --font-size-code: 13px;
  --font-size-body: 14px;
  --font-size-heading: 15px;
  --font-size-title: 22px;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  --leading-caption: 14px;
  --leading-footnote: 16px;
  --leading-code: 19px;
  --leading-body: 20px;
  --leading-heading: 20px;
  --leading-title: 26px;
  --on-primary: var(--neutral-0);
  --on-accent: var(--gray-0);
  --on-danger: var(--gray-0);
  --on-success: var(--gray-900);
  --on-warning: var(--gray-900);
  --on-pro: var(--gray-0);
  --on-git-added: var(--gray-0);
  --on-git-removed: var(--gray-0);
  --on-git-modified: var(--gray-0);
  --on-git-merged: var(--gray-0);
  --on-git-closed: var(--gray-0);
  --on-git-conflicting: var(--gray-0);
  --on-git-draft: var(--gray-0);
  --on-git-opened: var(--on-git-added);
  --on-git-queued: var(--on-git-modified);
  --on-brand: var(--gray-0);
  --z-modal: 40;
  --z-coachmark: 35;
  --z-popover: 50;
  --z-tooltip: 50;
  --z-toast: 60;
}

[data-mode="dark"] {
  --border-accent: var(--blue-700);
  --border-danger: var(--red-700);
  --border-success: var(--green-700);
  --border-warning: var(--yellow-700);
  --border-pro: var(--violet-700);
  --shadow-color: hsl(0 0% 0% / 0.24);
  --shadow-popover: 0 8px 24px rgb(0 0 0 / 0.32), 0 2px 6px rgb(0 0 0 / 0.2);
  --ring-outer: 0px;
  --ring-inner: 1px;
  --ring-color: var(--alpha-2);
  --focus-shadow: inset 0 0 0 1px var(--page-bg), 0 0 0 1px var(--fill-accent), 0 0 6px 1px hsl(from var(--blue-600) h s l / 60%);
  --pictogram-highlight-default: var(--gray-650);
  --pictogram-highlight-heather: var(--plum);
  --pictogram-highlight-cactus: var(--mineral);
  --pictogram-highlight-peach: var(--clay-emphasized);
  --neutral-0: var(--gray-900);
  --neutral-10: var(--gray-890);
  --neutral-20: var(--gray-880);
  --neutral-30: var(--gray-870);
  --neutral-40: var(--gray-860);
  --neutral-50: var(--gray-850);
  --neutral-60: var(--gray-840);
  --neutral-70: var(--gray-830);
  --neutral-80: var(--gray-820);
  --neutral-90: var(--gray-810);
  --neutral-100: var(--gray-800);
  --neutral-150: var(--gray-750);
  --neutral-200: var(--gray-700);
  --neutral-250: var(--gray-650);
  --neutral-300: var(--gray-600);
  --neutral-350: var(--gray-550);
  --neutral-400: var(--gray-500);
  --neutral-450: var(--gray-450);
  --neutral-500: var(--gray-400);
  --neutral-550: var(--gray-350);
  --neutral-600: var(--gray-300);
  --neutral-650: var(--gray-250);
  --neutral-700: var(--gray-200);
  --neutral-750: var(--gray-150);
  --neutral-800: var(--gray-100);
  --neutral-810: var(--gray-90);
  --neutral-820: var(--gray-80);
  --neutral-830: var(--gray-70);
  --neutral-840: var(--gray-60);
  --neutral-850: var(--gray-50);
  --neutral-860: var(--gray-40);
  --neutral-870: var(--gray-30);
  --neutral-880: var(--gray-20);
  --neutral-890: var(--gray-10);
  --neutral-900: var(--gray-0);
  --surface-0: var(--gray-890);
  --surface-1: var(--gray-830);
  --surface-2: var(--gray-750);
  --surface-3: var(--gray-700);
  --fill-git-added: var(--text-git-added);
  --fill-git-added-hover: #27c840;
  --fill-git-removed-hover: #ff1342;
  --fill-git-modified: var(--text-git-modified);
  --fill-git-modified-hover: #fac800;
  --fill-git-merged: var(--text-git-merged);
  --fill-git-merged-hover: #a67dff;
  --fill-git-closed: var(--text-git-closed);
  --fill-git-closed-hover: #ff4940;
  --fill-git-conflicting: var(--text-git-conflicting);
  --fill-git-conflicting-hover: #f97a1f;
  --fill-git-draft-hover: #999999;
  --fill-primary-hover: var(--gray-100);
  --fill-secondary: var(--alpha-2);
  --fill-secondary-hover: hsl(0 0% 100% / 0.14);
  --fill-secondary-ring: transparent;
  --fill-field: var(--fill-secondary);
  --bg-accent: var(--blue-800);
  --bg-danger: var(--red-800);
  --bg-success: var(--green-800);
  --bg-warning: var(--yellow-800);
  --bg-pro: var(--violet-800);
  --backdrop: rgb(0 0 0 / 0.5);
  --text-accent: var(--blue-300);
  --text-danger: var(--red-300);
  --text-success: var(--green-400);
  --text-warning: var(--yellow-300);
  --text-pro: var(--violet-300);
  --text-git-added: #32d74b;
  --text-git-removed: #ff2c56;
  --text-git-modified: #ffd014;
  --text-git-merged: #b796ff;
  --text-git-closed: #ff6159;
  --text-git-conflicting: #fa832e;
  --text-git-draft: #a6a6a6;
  --text-secondary: var(--gray-200);
  --text-muted: var(--gray-400);
  --on-git-added: var(--gray-900);
  --on-git-removed: var(--gray-900);
  --on-git-modified: var(--gray-900);
  --on-git-merged: var(--gray-900);
  --on-git-closed: var(--gray-900);
  --on-git-conflicting: var(--gray-900);
  --on-git-draft: var(--gray-900);
}

@media (prefers-color-scheme: dark) {
  :root:where(:not([data-mode="light"])) {
    --border-accent: var(--blue-700);
    --border-danger: var(--red-700);
    --border-success: var(--green-700);
    --border-warning: var(--yellow-700);
    --border-pro: var(--violet-700);
    --shadow-color: hsl(0 0% 0% / 0.24);
    --shadow-popover: 0 8px 24px rgb(0 0 0 / 0.32), 0 2px 6px rgb(0 0 0 / 0.2);
    --ring-outer: 0px;
    --ring-inner: 1px;
    --ring-color: var(--alpha-2);
    --focus-shadow: inset 0 0 0 1px var(--page-bg), 0 0 0 1px var(--fill-accent), 0 0 6px 1px hsl(from var(--blue-600) h s l / 60%);
    --pictogram-highlight-default: var(--gray-650);
    --pictogram-highlight-heather: var(--plum);
    --pictogram-highlight-cactus: var(--mineral);
    --pictogram-highlight-peach: var(--clay-emphasized);
    --neutral-0: var(--gray-900);
    --neutral-10: var(--gray-890);
    --neutral-20: var(--gray-880);
    --neutral-30: var(--gray-870);
    --neutral-40: var(--gray-860);
    --neutral-50: var(--gray-850);
    --neutral-60: var(--gray-840);
    --neutral-70: var(--gray-830);
    --neutral-80: var(--gray-820);
    --neutral-90: var(--gray-810);
    --neutral-100: var(--gray-800);
    --neutral-150: var(--gray-750);
    --neutral-200: var(--gray-700);
    --neutral-250: var(--gray-650);
    --neutral-300: var(--gray-600);
    --neutral-350: var(--gray-550);
    --neutral-400: var(--gray-500);
    --neutral-450: var(--gray-450);
    --neutral-500: var(--gray-400);
    --neutral-550: var(--gray-350);
    --neutral-600: var(--gray-300);
    --neutral-650: var(--gray-250);
    --neutral-700: var(--gray-200);
    --neutral-750: var(--gray-150);
    --neutral-800: var(--gray-100);
    --neutral-810: var(--gray-90);
    --neutral-820: var(--gray-80);
    --neutral-830: var(--gray-70);
    --neutral-840: var(--gray-60);
    --neutral-850: var(--gray-50);
    --neutral-860: var(--gray-40);
    --neutral-870: var(--gray-30);
    --neutral-880: var(--gray-20);
    --neutral-890: var(--gray-10);
    --neutral-900: var(--gray-0);
    --surface-0: var(--gray-890);
    --surface-1: var(--gray-830);
    --surface-2: var(--gray-750);
    --surface-3: var(--gray-700);
    --fill-git-added: var(--text-git-added);
    --fill-git-added-hover: #27c840;
    --fill-git-removed-hover: #ff1342;
    --fill-git-modified: var(--text-git-modified);
    --fill-git-modified-hover: #fac800;
    --fill-git-merged: var(--text-git-merged);
    --fill-git-merged-hover: #a67dff;
    --fill-git-closed: var(--text-git-closed);
    --fill-git-closed-hover: #ff4940;
    --fill-git-conflicting: var(--text-git-conflicting);
    --fill-git-conflicting-hover: #f97a1f;
    --fill-git-draft-hover: #999999;
    --fill-primary-hover: var(--gray-100);
    --fill-secondary: var(--alpha-2);
    --fill-secondary-hover: hsl(0 0% 100% / 0.14);
    --fill-secondary-ring: transparent;
    --fill-field: var(--fill-secondary);
    --bg-accent: var(--blue-800);
    --bg-danger: var(--red-800);
    --bg-success: var(--green-800);
    --bg-warning: var(--yellow-800);
    --bg-pro: var(--violet-800);
    --backdrop: rgb(0 0 0 / 0.5);
    --text-accent: var(--blue-300);
    --text-danger: var(--red-300);
    --text-success: var(--green-400);
    --text-warning: var(--yellow-300);
    --text-pro: var(--violet-300);
    --text-git-added: #32d74b;
    --text-git-removed: #ff2c56;
    --text-git-modified: #ffd014;
    --text-git-merged: #b796ff;
    --text-git-closed: #ff6159;
    --text-git-conflicting: #fa832e;
    --text-git-draft: #a6a6a6;
    --text-secondary: var(--gray-200);
    --text-muted: var(--gray-400);
    --on-git-added: var(--gray-900);
    --on-git-removed: var(--gray-900);
    --on-git-modified: var(--gray-900);
    --on-git-merged: var(--gray-900);
    --on-git-closed: var(--gray-900);
    --on-git-conflicting: var(--gray-900);
    --on-git-draft: var(--gray-900);
  }
}

  /* ===== END vendored @ant/cds tokens ===== */

  /* Deviations from stock CDS — the only hand-maintained token values.
     De-brand invariant: published artifacts use plain system font stacks
     (no Anthropic fonts or serif voice) and a white light surface. Both
     font overrides are load-bearing — the vendored stacks lead with
     Anthropic Sans/Mono. The --hl-* highlight theme is this template's
     own extension, mapped to canonical CDS palette stops above. */
  :root {
    color-scheme: light dark;
    --font-sans: var(--font-system);
    --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
    --surface-0: #ffffff;
    --hl-comment: var(--gray-400);
    --hl-keyword: var(--violet-600);
    --hl-string: var(--green-600);
    --hl-number: var(--magenta-600);
    --hl-title: var(--blue-600);
    --hl-attr: var(--aqua-600);
    --hl-deletion: var(--red-600);
  }
  /* Dark re-overrides: the white-surface deviation above is light-only,
     and source order would otherwise beat the vendored dark block (equal
     :root specificity), so dark restores the canonical surface here —
     under both axes, mirroring the vendored block's own structure: the
     media block carries the same :where() zero-specificity guard so an
     explicit light stamp beats OS-dark, and the attribute block forces
     dark on an OS-light machine. */
  @media (prefers-color-scheme: dark) {
    :root:where(:not([data-mode="light"])) {
      --surface-0: var(--gray-890);
      --hl-keyword: var(--violet-300);
      --hl-string: var(--green-300);
      --hl-number: var(--magenta-300);
      --hl-title: var(--blue-300);
      --hl-attr: var(--aqua-300);
      --hl-deletion: var(--red-300);
    }
  }
  :root[data-mode="dark"] {
    color-scheme: dark;
    --surface-0: var(--gray-890);
    --hl-keyword: var(--violet-300);
    --hl-string: var(--green-300);
    --hl-number: var(--magenta-300);
    --hl-title: var(--blue-300);
    --hl-attr: var(--aqua-300);
    --hl-deletion: var(--red-300);
  }
  :root[data-mode="light"] { color-scheme: light; }
  /* Print is always light, regardless of the OS scheme or the toggle stamp
     (browsers don't print backgrounds by default). The vendored dark block
     cannot be switched off in print, so this re-pins — as literals — every
     token this template's element rules actually paint with; the selector
     list ties the attribute-dark scope and wins by source order. */
  @media print {
    :root, :root[data-mode="dark"] {
      color-scheme: light;
      --surface-0: #ffffff;
      --text-primary: #0b0b0b;
      --text-secondary: #52514e;
      --text-accent: #184f95;
      --border: rgba(11, 11, 11, 0.1);
      --border-strong: rgba(11, 11, 11, 0.2);
      --border-stronger: rgba(11, 11, 11, 0.4);
      --fill-control: rgba(11, 11, 11, 0.1);
      --hl-keyword: #4a3aa7;
      --hl-string: #006300;
      --hl-number: #862a4c;
      --hl-title: #184f95;
      --hl-attr: #065f49;
      --hl-deletion: #8e2626;
    }
  }

  body {
    background: var(--surface-0);
    color: var(--text-primary);
    font: 14px/1.5 var(--font-sans);
    overflow-wrap: break-word;
  }
  article {
    max-width: 76ch;
    margin: 0 auto;
    padding: var(--gap-xl) 24px 72px;
    display: flex;
    flex-direction: column;
    gap: var(--gap-xl);
  }
  header { display: flex; flex-direction: column; gap: var(--gap-sm); }
  .eyebrow {
    font: 600 12px/14px var(--font-sans);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-accent);
  }
  /* Document heading scale: 24/19/16/14 over the 14px body (~1.19 steps).
     Deliberately looser than the closed CDS UI scale — a long document
     needs more size differentiation between levels than app chrome does. */
  h1 {
    font: 600 24px/30px var(--font-sans);
    letter-spacing: -0.01em;
    text-wrap: balance;
    margin: 0;
  }
  h2 {
    font: 600 19px/25px var(--font-sans);
    text-wrap: balance;
    margin: 0;
  }
  h3 {
    font: 600 16px/22px var(--font-sans);
    text-wrap: balance;
    margin: 0;
  }
  h4, h5, h6 {
    font: 600 14px/20px var(--font-sans);
    text-wrap: balance;
    margin: 0;
  }
  section { display: flex; flex-direction: column; gap: var(--gap-md); }
  /* Heading rhythm inside the single mechanical-fill section: headings group
     with the content below them, not the paragraph above. Inert in the
     skill's multi-section flow, where each h2 is its section's first child. */
  section > :is(h2, h3, h4):not(:first-child) { margin-top: var(--gap-sm); }
  section > h2:not(:first-child) { margin-top: var(--gap-md); }
  p, li { margin: 0; max-width: 68ch; }
  .lede { font-size: 15px; line-height: 1.5; color: var(--text-secondary); }
  .lede:empty { display: none; }
  a { color: var(--text-accent); }
  code {
    font: 0.92em/1.5 var(--font-mono);
    background: var(--fill-control);
    padding: 1px 3px;
    border-radius: 4px;
  }
  a > code { background: none; color: inherit; }
  pre {
    font: 13px/19px var(--font-mono);
    background: var(--fill-control);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: var(--gap-sm) var(--gap-md);
    overflow-x: auto;
    margin: 0;
  }
  pre code { background: none; padding: 0; font: inherit; }
  /* Syntax-highlight theme for the hljs-* spans the injected client-side
     runtime (hljsHighlight.ts) emits. Colors are @ant/cds base-palette
     stops (600s light / 300s dark) — the hue families CDS derives its role
     colors from. */
  .hljs-comment, .hljs-quote, .hljs-meta { color: var(--hl-comment); font-style: italic; }
  .hljs-keyword, .hljs-selector-tag, .hljs-literal, .hljs-type, .hljs-doctag { color: var(--hl-keyword); }
  .hljs-string, .hljs-regexp, .hljs-addition { color: var(--hl-string); }
  .hljs-number, .hljs-symbol { color: var(--hl-number); }
  .hljs-title, .hljs-name, .hljs-section, .hljs-built_in { color: var(--hl-title); }
  .hljs-attr, .hljs-attribute, .hljs-variable, .hljs-template-variable, .hljs-params, .hljs-selector-attr, .hljs-selector-class, .hljs-selector-id { color: var(--hl-attr); }
  .hljs-deletion { color: var(--hl-deletion); }
  .hljs-emphasis { font-style: italic; }
  .hljs-strong { font-weight: 600; }
  blockquote {
    border-left: 2px solid var(--border-strong);
    padding-left: var(--gap-sm);
    color: var(--text-secondary);
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
    padding: var(--gap-xs) var(--gap-sm);
    border-bottom: 1px solid var(--border);
  }
  th {
    font: 600 12px/14px var(--font-sans);
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--text-secondary);
    border-bottom-color: var(--border-strong);
  }
  ul, ol { margin: 0; padding-left: 1.25rem; display: flex; flex-direction: column; gap: var(--gap-xs); }
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
    border: 1.5px solid var(--border-stronger);
    border-radius: 4px;
    background: var(--surface-0);
    margin: 0 6px 0 0;
    vertical-align: -2px;
  }
  :is(li, li > p:first-child) > input[type="checkbox"]:checked {
    background: var(--fill-accent) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'%3E%3Cpath d='M2.5 6.5 5 9l4.5-5.5' fill='none' stroke='%23fff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/10px 10px no-repeat;
    border-color: var(--fill-accent);
  }
  /* Loose / multi-block list items: space the blocks inside an item. */
  :is(li, td, th) > * + :is(p, ul, ol, blockquote, pre) { margin-top: var(--gap-xs); }
  img { max-width: 100%; height: auto; border-radius: var(--radius); }
  hr { border: none; border-top: 1px solid var(--border); margin: 0; }
  /* Decision blocks ("Needs your call" items): filled by the mechanical
     render from decision-fenced code blocks in the workshop doc
     (src/frame/decisionBlocks.ts), or authored directly in the hand-edit
     flow. Derived from the artifact-pr-review template's call-items, but
     deliberately divergent on the options surface: one full-width row
     per option (PR-review keeps inline pills), so the lean renders as a
     highlighted Recommended row with its reason in-row. Rows are inert
     spans until the artifact-interactions script leg wires them. */
  .call-item {
    display: flex;
    gap: var(--gap-sm);
    /* Right padding mirrors the marker column (card padding + marker
       width + flex gap) so option rows sit equidistant from the card's
       left and right edges. */
    padding: var(--gap-sm) calc(var(--gap-md) + 14px + var(--gap-sm)) var(--gap-sm) var(--gap-md);
    border: 1px solid var(--border-strong);
    border-radius: var(--radius);
    background: var(--fill-control);
  }
  .call-item .marker { flex: 0 0 14px; color: var(--text-accent); line-height: 1.5; }
  /* flex: 1 (not shrink-wrap): the body — and so every option row —
     spans the full card width regardless of the longest text line. */
  .call-body { display: flex; flex-direction: column; gap: var(--gap-xs); flex: 1 1 0%; min-width: 0; }
  .call-body .q { font-weight: 600; }
  .call-body .anchor { color: var(--text-secondary); font-size: 13px; }
  .call-body .decided { color: var(--text-secondary); font-size: 13px; font-weight: 600; }
  .options { display: flex; flex-direction: column; gap: 6px; margin-top: 2px; }
  .option {
    display: flex;
    align-items: baseline;
    flex-wrap: wrap;
    gap: 4px 8px;
    /* No fixed height, and break anywhere: labels (≤60 chars) and
       reasons (≤200 chars) must wrap within the row even when they are
       a single unbroken token — an unbreakable word would otherwise set
       the flex item's min-content width and overflow the card. */
    overflow-wrap: anywhere;
    min-width: 0;
    padding: 6px 10px;
    border-radius: 5px;
    font-size: 12px;
    color: var(--text-primary);
    box-shadow: inset 0 0 0 1px var(--border-stronger);
    opacity: 0.75;
    cursor: default;
  }
  .option .option-label { font-weight: 500; }
  .option.recommended {
    opacity: 1;
    box-shadow: inset 0 0 0 1.5px var(--fill-accent);
    background: color-mix(in srgb, var(--fill-accent) 8%, transparent);
  }
  .option .badge {
    display: inline-flex;
    align-items: center;
    height: 16px;
    padding: 0 6px;
    border-radius: 999px;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.02em;
    text-transform: uppercase;
    color: #fff;
    background: var(--fill-accent);
  }
  .option .why { color: var(--text-secondary); }
  .option.chosen { background: var(--fill-accent); color: #fff; opacity: 1; box-shadow: none; }
  .option.chosen .why { color: #fff; opacity: 0.85; }
  .option.dim { opacity: 0.4; }
</style>

<article>
  <header>
    <span class="eyebrow">{{EYEBROW}}</span>
    <h1>{{TITLE}}</h1>
    <p class="lede">{{SUMMARY}}</p>
  </header>

  <section>
    <h2>What we're deciding</h2>
    <!-- SLOT: context -->
  </section>

  <section>
    <h2>Working draft</h2>
    <!-- SLOT: draft -->
  </section>

  <section>
    <h2>Decisions</h2>
    <!-- SLOT: decisions -->
  </section>
</article>
