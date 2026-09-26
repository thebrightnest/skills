# Imagery: when a generated image earns its place

Read before generating anything.

This skill **delegates**. If an image-generation skill is available in the
session (check the skills list — `image-studio` and similar), invoke it with the
Skill tool and hand it a brief. Do not reimplement its engine or restate its
flags. Your job is the brief, the guardrail, and the disposition of what comes
back. If no such skill is available, say so and stop — do not improvise a
generator.

**Project style constraints.** Many image tools read a project-level guidelines
file. Check whether one exists and whether the generator applies it. If none
exists and the project has a defined palette, either create one from the real
tokens first or put the constraints in the prompt — otherwise the generator
falls back to generic defaults and hands you off-brand output.

---

## The rule that governs everything else

**An image is never the thing being designed. It is a thing inside the design.**

A generated raster cannot be resized to 375, cannot use a token exactly, cannot
be tabbed through, and cannot become code. So it never substitutes for the
mockup in `build.md`. The verification hierarchy does not bend:

> real component in a browser > HTML mockup screenshotted at three widths >
> generated image > description

If you catch yourself about to generate "what the screen could look like", you
have skipped Movement 4. Build the markup. It is faster than you think and it
survives the meeting.

---

## Allowed: two cases

### 1. Direction boards — Movement 3, optional

*Before* structure is settled, to make an atmosphere argument concrete. Useful
when the disagreement is about **feel** — "should this be warm and slow, or tight
and instrumental?" — and words keep sliding.

Bounded hard:

- Only when the user asked to see directions, or you asked and they agreed.
- Texture, density and mood — **never a rendered interface**. A board full of
  fake UI is worse than no board: people critique invented details and you end up
  defending a hallucination.
- One image per named concept, same aspect ratio, one batch, so they compare.
- They illustrate a concept that already exists in text. If you cannot write the
  concept first, an image will not rescue it.
- Label each **"direction, not a design"** when presenting.
- Thrown away after the choice. They never enter the handoff as the proposal.

Most direction disagreements are structural, and structure is better argued in
markup. Reach for a board only when the argument is genuinely atmospheric.

### 2. Product assets — Movement 4

Real artefacts the product needs and does not have:

- **Empty-state art** — the strongest case, since empty is often the first
  impression and the place a warm line plus one action still leaves a hole.
- **Onboarding or first-run illustration**, where a surface carries warmth before
  there is content.
- **OG / social preview images** for a shipped surface.
- **Documentation imagery** where a photograph or texture beats a diagram.

---

## Never

- **UI mockups, or anything that reads as a screenshot.** Build it.
- **Icons**, when the project has an icon set. Generating one is a bug.
- **Logos, marks or brand lockups.** Those are fixed assets.
- **Charts, graphs, dashboards.** Real data or nothing.
- **Faces, testimonials, avatars.** Fabricated people in a real product.
- **Mascots and generated doodles.** See the tension below.

---

## The tension, and how to resolve it

`critique.md`'s slop list flags *"generated doodles and mascots in place of art
direction"* — and this file just authorised generating empty-state art. Both are
right, and the line between them is **whether a decision was made.**

Slop is an image generated *instead of* deciding what the surface should feel
like. An asset is an image generated *because* that decision was made and needs
rendering.

Before any asset generation, be able to state, in one sentence each:

1. What this surface is trying to make someone feel or do.
2. Why an image serves that better than type and space alone.
3. What it depicts, specifically — not "something friendly".

If you cannot write all three, generating is the wrong move. Restraint is a
legitimate answer: a well-set line of secondary text with one clear action often
beats an illustration, and it never ages.

Then apply `critique.md`'s three-looks calibration to the output. If the
product's palette already sits in one of those looks, a generated image in that
palette is the single most likely artefact to read as machine-made. Judge it by
"would a studio ship this", not "does it match the tokens" — matching is the
floor, not the bar.

---

## Procedure

**1. Get approval and a count first.** Generation costs money per image. Say how
many and what for, then wait. Never generate in a loop to see what sticks.

**2. Write the brief.** Carry the decision: subject, composition, what it must
not contain. If a guidelines file supplies palette and house style, do not repeat
those — spend the prompt on what is specific to this asset.

> Empty state for a task board in a brand-new workspace. A single flat-illustrated
> workbench seen from above, mostly bare, two or three small tools resting at one
> edge, clear space in the middle. Calm, patient, a room waiting to be used.
> No people, no text, no UI, no mascot. Aspect 4:3.

**3. Invoke the image skill**, do not duplicate it.

**4. Read the result back and judge it.** Look at the actual image. Then:

- On-palette without being generic?
- Does it survive at the size it will actually render — often 200–320px wide?
  Detail that disappears is detail that cost money.
- Any text, watermark, or accidental UI? Reject; do not "fix in CSS".
- Does it sit calmly behind the primary action, or compete with it?
- Would you defend it in a design review?

Two rounds maximum. If the third is not right, the brief is wrong or the asset
should not exist — say so rather than spending.

**5. Disposition.** Generator output directories are usually scratch, and often
gitignored — check before assuming anything persists for anyone else.

An asset ships only when you deliberately:

- move it into the project's static/public assets with a descriptive name, not a
  timestamped slug;
- check the weight — an empty state has no business costing 800KB;
- reference it with real `width`/`height`, meaningful `alt`, and lazy loading
  below the fold;
- get explicit approval, since this adds a binary to the repo.

A direction board never ships. Show it, decide, drop it.

**6. Record it.** In the handoff: what was generated, why, the brief, and what
was rejected. A future session should not re-derive the decision, or regenerate
the asset because it could not tell the shipped one from the scratch one.
