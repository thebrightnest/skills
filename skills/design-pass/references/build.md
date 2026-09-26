# Build: mockup first, then the real stack

Read in full before writing markup. The order is not optional — a standalone
mockup costs minutes and is thrown away; a wrong refactor in the real codebase
costs an afternoon and a review round.

---

## Step 1 — the mockup

One self-contained HTML file in the scratchpad. Not in the repo — it is a
thinking artifact, not source.

```text
<scratchpad>/design/<surface>-<direction>.html
```

Rules:

- **Real tokens, copied exactly** from whatever discovery identified as the token
  source. If the mockup needs a value the token set does not have, that is a
  finding about the token set — write it down, do not quietly invent one.
- **Real content.** Pull actual strings from the running app or its fixtures:
  real record titles, a real name, an actual error message. Never lorem ipsum,
  never "Your text here".
- **Real states on the page.** Build the empty state and the loaded state in the
  same file, stacked with a divider. You will otherwise ship a happy path.
- **No generated images.** Placeholder blocks with a note, or a real asset that
  already exists. If the surface needs art that does not exist, see `imagery.md`
  — a separate, approved step after structure is settled, never a way to fill a
  hole mid-mockup.
- **Plain CSS, no build step, no CDN framework.** A mockup needing tooling is not
  faster than the real thing.
- **`prefers-reduced-motion` and `:focus-visible` from the start**, so the mockup
  is not a lie about accessibility.
- Match the project's theme posture. If it is deliberately single-theme, do not
  introduce the other one here.

## Step 2 — verify at three widths

**375 · 768 · 1440.** Screenshot each and **read every image back**.

> **Assert the viewport first.** Browser-automation tools routinely ignore a
> viewport change on re-navigation and return the previous size. Evaluate
> `innerWidth` before each capture and confirm it matches; if not, close the
> browser and reopen at that width. A capture silently taken at the wrong size is
> how a design audit ships a false finding.

For multiple widths or files, a short Playwright script is more reliable than
driving a browser tool interactively, and it can assert and measure in one pass:

```js
for (const w of [375, 768, 1440]) {
  const page = await browser.newPage({ viewport: { width: w, height: 900 } });
  await page.goto(url);
  const m = await page.evaluate(() => ({
    vw: innerWidth,
    pageH: document.documentElement.scrollHeight,
    overflowX: document.documentElement.scrollWidth > innerWidth,
    smallTargets: [...document.querySelectorAll('button,a,select,input')]
      .filter(e => { const r = e.getBoundingClientRect(); return r.height > 0 && r.height < 44; }).length,
    clipped: [...document.querySelectorAll('h1,h2,h3,h4,.title')]
      .filter(e => e.scrollWidth > e.clientWidth + 1).length,
  }));
  console.log(w, m);            // vw must equal w, or the capture is worthless
  await page.screenshot({ path: `shot-${w}.png`, fullPage: true });
}
```

Check for text overflow, layout collapse, horizontal scroll at 375, targets under
44px, and whether the narrow layout makes *design* sense rather than being
stacked desktop columns. Fix what you find before showing anything.

## Step 3 — refine

Show the file path and the screenshots inline. Then loop:

- **Edit, never rewrite.** Surgical changes. A full regeneration loses accumulated
  decisions and drifts.
- One round of changes, then re-screenshot the widths that changed.
- Cap it. If you are on round five and still circling, stop and name the
  disagreement — it is nearly always about Movement 1, not CSS.

Get explicit approval before touching the repo.

---

## Step 4 — port to the real stack

Now, and only now.

**Match the codebase; do not improve it in passing.** Open a neighbouring
component and follow its shape: how it declares props, handles state, fetches
data, names files, and where its tests live.

- **Use the token layer, not raw values.** Whatever form it takes — utility
  classes, CSS variables, a theme object — go through it. Reaching for an
  arbitrary value means either you missed the token or the token is missing; both
  are worth saying out loud.
- **Use what is already a dependency.** The icon set, the component library, the
  data-fetching layer, the markdown renderer. Adding a dependency needs a reason
  and usually an ask.
- **Extend the mechanism, do not copy it.** If three components need the same
  badge, the third is telling you to extract one — not to paste the classes
  again. Editing N parallel blocks identically means you missed a chokepoint.
- **Stay in the layer you were asked about.** If the design genuinely needs new
  data from the backend, stop and say so. In projects where frontend and backend
  deploy separately, that changes the release path for the whole change, not just
  the part that needed it.
- **Respect API compatibility.** Where a client may be older than the server
  serving it, a response-shape change is not safe merely because today's frontend
  matches. Make it additive, or ship the backend first.

## Step 5 — verify the real thing

Run the app, screenshot the **real component** at 375 / 768 / 1440 with the same
viewport assertion, and read the images. Compare against the approved mockup.
Differences are either bugs or decisions — say which, for each.

Then run **only the test command for the layer you changed**, as discovery
recorded it. Do not run a repository-wide suite for an isolated frontend change
unless the project says to. If you changed behaviour, add or update a test,
placed where the project already puts them.

Lint if you touched much, using the project's linter.

## Step 6 — hand off

Where the project keeps design records:

- Before and after screenshots at desktop and narrow.
- Which files changed and why.
- What you could not verify.
- Anything the work revealed that is out of scope — a missing token, a state
  nobody designed, a data gap. **In the write-up, not in the diff.** The diff is
  the task and nothing else.

Propose the commit message and file list, then ask before committing, unless the
project's rules say otherwise.

---

## Things that will tempt you, and should not

- **Adding a dependency** for something the project already solves another way.
- **Introducing a theme the project deliberately does not have.** Product
  decision, not a design pass — raise it separately.
- **Changing brand colours** when discovery found them fixed.
- **Refactoring while you are in there.** Different change, different review.
- **Touching vendored, generated or upstream-tracked directories.** Discovery
  listed them. Edits there are debt someone else pays at the next upgrade.
