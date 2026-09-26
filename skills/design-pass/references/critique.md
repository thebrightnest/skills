# Critique: how to audit a surface

Read in full before judging a pixel. Order: classify → checklist → slop pass →
hard rules → report.

Where this conflicts with the project's own design rules, the project wins. Note
the override rather than silently following either.

---

## 1. Classify the mode before you judge anything

The mode is what the visitor's win looks like on **this surface**, not what the
product is. A developer tool's landing page is PERSUADE; a fashion house's docs
are READ.

- **PERSUADE** — marketing, landing, pricing, campaigns. They decide and act.
  Design *is* the product.
- **OPERATE** — dashboards, admin, settings, editors, tools. They finish a task.
  Scanability and native expectations beat expression; the brand lives in details.
- **READ** — docs, articles, guides, changelogs, logs. They understand something.
  Structure for comprehension, then make staying worth it.
- **EXPERIENCE** — portfolios, galleries, showcases. They are inside the work.
  The artifact owns the first viewport; the interface gets out of the way.
- **HYBRID** — classify per section, never per page.

The most common failure in an OPERATE product is **a tool dressed as a marketing
page**: card mosaics, hero spacing on a work surface, decorative iconography
where density was needed. The most common failure in a PERSUADE surface is a
page that states features and never makes an argument.

---

## 2. Checklist

Each hit becomes a finding tagged `high` (blocks or misleads), `medium` (costs
real effort or trust), or `polish` (note, do not grade).

### Hierarchy & composition

- One clear focal point; one primary action per view.
- Squint test: does hierarchy survive blur?
- Purpose readable in three seconds above the fold.
- White space intentional, not leftover.
- Density appropriate to how long someone sits here, not to a screenshot.
- Assume everything is visual noise until it earns its place.

### Typography

- ≤3 families. More is a finding.
- A ratio-based scale; no ad-hoc sizes.
- Line height ~1.5 body, 1.15–1.25 headings. Measure 45–75ch (66 ideal).
- No skipped heading levels.
- `text-wrap: balance` or `pretty` on headings.
- Curly quotes, real ellipsis `…`, `tabular-nums` on any column of numbers.
- Body ≥16px, labels ≥12px, no letterspacing on lowercase.
- **A neutral UI font as body/UI is fine** and usually correct on OPERATE
  surfaces. Flag it only when it is carrying the *display* voice on a surface
  whose job is brand — especially if the project defines a display face and
  leaves it unused. Check before flagging; do not spend a finding on a
  legitimate body face.

### Colour & contrast

- **Compute contrast, never eyeball it.** WCAG AA: 4.5:1 body, 3:1 for large text
  (≥18px or ≥14px bold) and UI components. Muted secondary text on a tinted
  ground is the most common real failure — measure it specifically.
- Palette coherent: ≤12 non-gray colours.
- Neutrals consistently warm or cool — a stray opposite-temperature gray from a
  framework default is a finding.
- Semantic colours consistent and never the sole encoding: status, provenance and
  severity each need a label or shape too.
- Dark mode, if present: elevation not just inversion, off-white text, accent
  desaturated 10–20%, `color-scheme` set. If the project is deliberately
  single-theme, do not relitigate that in a critique — raise it separately.

### Spacing & layout

- Consistent scale (4/8px base), not arbitrary values.
- Radius hierarchy, not one large radius on everything. Inner = outer − gap.
- No horizontal scroll at 375. Max width on body text.
- Related items closer than unrelated; **more space above a heading than below**.
  Read the computed values.

### Interaction states

- Hover on everything interactive; `focus-visible` always (never `outline: none`
  without a replacement); real active and disabled states.
- Touch targets ≥44px. Count them; do not assume.
- Loading: skeletons shaped like real content, not spinners.
- **Mindless-click audit.** Three mindless clicks beat one that needs thought.
  Anything requiring thought about whether it is the right click is `high`.
- Browser surfaces themed from the palette: `::selection`, caret, scrollbars,
  focus ring. Left at defaults, the page reads as assembled, not designed.

### Every state, not the happy path

For each component confirm all are designed: **empty · one · many · very many ·
long strings · loading · error · stale · in-flight · permission-denied**.

Identify which state a *new* user hits first — often empty — and treat it as the
first impression. "No items." is a failure: a warm line, one primary action, and
something to look at.

### Motion

- 50–700ms; ease-out entering, ease-in exiting.
- Only `transform` and `opacity`. Never `transition: all`.
- `prefers-reduced-motion` respected.
- One authored motion moment per surface, not an entrance on every section.

### Content & microcopy

- Buttons name the outcome ("Add task", not "Submit").
- Errors: what happened + why + what to do next.
- No happy talk; no instructions longer than a sentence. If users must read
  instructions, flag the instructions *and* the interaction they compensate for.
- **Vocabulary check against the project's glossary,** including forbidden terms.
  Naming drift is a design defect, not a copy nit.
- Destructive actions have confirmation or undo.

### Performance as design

- CLS < 0.1; no shift as data and fonts arrive.
- `font-display: swap`; no FOUT on brand faces.
- Images sized, lazy below the fold, modern formats.

### Navigation — the trunk test

Cover everything but the navigation. Can you still answer: what product is this,
where am I, what are the major sections, what are my options, how do I get back?
A failure here is `high` however polished the pixels are.

**Check it at 375 specifically.** Navigation that silently overflows, clips, or
renders items outside the viewport with no scroll and no menu is a functional
defect, not a styling one — and it is invisible at desktop width.

---

## 3. Slop pass

The test: would a designer at a respected studio ship this?

**Blacklist** — the 3-column icon-in-a-circle feature grid; centred everything;
uniform bubbly radius; decorative blobs and wavy dividers; emoji as design
elements; coloured left-borders on cards; gradient buttons; generated SVG
mascots; frosted glass as the default surface; fake avatars and sparklines
filling space; purple-to-blue gradients; "Get Started / Learn More" as the only
CTAs; cookie-cutter section rhythm; `system-ui` as the display voice.

**In an OPERATE product the two that actually bite:**

- **Stacked cards instead of layout.** Equal rounded cards with drop shadows are
  not composition. A card earns its place only when the card *is* the
  interaction.
- **Equal boxes for unequal content.** A grid giving a two-line item and a
  forty-line item the same frame.

**Calibration — the three looks.** AI-built interfaces land in one of three looks
whatever the product is: (1) cream ground, high-contrast serif or geometric
display, terracotta or signal-red accent; (2) near-black, one neon accent,
glowing edges; (3) broadsheet hairlines, italic display serif, tiny tracked mono
labels. Each is fine when the brief asks for it.

Two ways to use this:

- **Designing:** if the brief left the look open and you landed in one anyway,
  you stopped looking. Could someone guess your look from the category alone?
  Start over.
- **Auditing:** if the product's *existing* palette already sits in one of these
  looks, that is not a reason to change it — it may be deliberate and
  brand-mandated. It *is* a reason the bar is higher: the palette gives nothing
  for free, and density, structure, type and restraint have to do the work of
  making it read as made rather than generated. Never conclude "it matches the
  tokens, so it's fine."

---

## 4. Hard rules

**Instant fails**

1. App UI made of stacked cards instead of layout.
2. Generic card grid as first impression.
3. Strong headline, no clear action.
4. Sections repeating the same mood.
5. Only the happy path designed.
6. Body text under 16px or under 4.5:1 contrast.
7. Placeholder-as-only-label in a form.
8. A heading floating equidistant between two sections.
9. Primary navigation unreachable at any supported width.

**OPERATE rules**

- Calm surface hierarchy, strong typography, few colours.
- Dense but readable; minimal chrome.
- Organise as: primary workspace · navigation · secondary context · one accent.
- Avoid dashboard-card mosaics, thick borders, decorative gradients, ornamental icons.
- Copy is utility language — orientation, status, action. Not aspiration.
- Section headings say what the area *is* or what you can *do* there.

**PERSUADE rules**

- First viewport is one composition, not a document.
- Brand > headline > body > CTA. Expressive, purposeful type.
- Hero: one headline, one supporting sentence, one CTA group, one image. No cards.
- One job per section. If deleting 30% of the copy improves it, keep deleting.

**READ rules**

- 65–75ch, one column, headings closer to what follows than what precedes.
- Wayfinding is a feature: where am I, what is next, where do I search.

**EXPERIENCE rules**

- The work fills the first viewport; chrome earns every pixel.
- One authored transition, never a scroll-jacked tour.

**Reflexes no checklist catches**

- Depth has an offset. A zero-offset coloured halo is decoration, not depth.
- Secondary text on a coloured surface is tinted from that hue, never gray.
- More space above a heading than below it.
- Light or dark comes from the use scene — who, where, under what light — not
  from the category. If the project already decided, respect it.

---

## 5. Report

Structured observations, not opinions:

- **"I notice…"** — observation, with the screenshot or computed value.
- **"I wonder…"** — the question it raises about the user.
- **"What if…"** — a specific alternative.
- **"I think X because Y"** — where Y is about this product's users.

Every finding: *impact tag · category · evidence · the fix, concretely.*

Prefer a **chokepoint** finding to a list of its symptoms. If the same defect
appears in twenty components, the finding is the missing abstraction, not the
twenty instances — name the shared fix and cite two or three examples.

Close with **Quick Wins**: 3–5 highest-impact fixes under 30 minutes each.

Finally, say what you could not verify — surfaces unreachable, states you could
not produce, values you could not compute. An honest gap is worth more than a
confident guess.
