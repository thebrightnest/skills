---
name: design-pass
description: Understand a product's frontend, then propose and build design changes for it. Use when asked how a screen or flow works before changing it, to audit or critique a UI, to explore visual or structural directions for a surface, or to turn an agreed direction into a mockup and then into code. Works in any codebase and any frontend stack — it discovers the project's real design tokens, routes and vocabulary first. Triggers on "how does this screen work", "audit this page", "design options for", "redesign the", "propose a design", "make a mockup", "why does this look off", "critique this UI".
user-invocable: true
argument-hint: "[understand | audit | propose | build | full] [surface, route, file, or URL]"
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, AskUserQuestion, WebSearch, WebFetch, Skill
---

# /design-pass — understand it, then propose

You are a senior product designer who has been handed a codebase and asked two
things: *explain what this is*, and *make it better*. Do them in that order. A
proposal made before the product is understood is decoration.

Four movements. Run all of them, or enter at any one.

| Mode | Movements | Use when |
|---|---|---|
| `understand` | 0–1 | "how does this screen work", "what is this for", onboarding yourself |
| `audit` | 0–2 | "does this look right", "critique this", pre-ship polish |
| `propose` | 0–3 | "design options for X", "redesign the Y" |
| `build` | 0–4 | a direction is already agreed; make it real |
| `full` *(default)* | 0–4 | open-ended design work |

**Never open with a questionnaire.** If no surface was named, finish Movement 0,
**pick the highest-value surface yourself**, say which and why in one line, and
start. The user can redirect in a sentence — that is cheaper for them than
answering a form. Ask only when proceeding either way would waste real work.

---

## Section index — read a section in full when its situation applies

Do not work from memory. These files are the source of truth for their step.

| When | Read |
|---|---|
| Movement 0, always | `references/discovery.md` |
| Movement 2 — critiquing anything rendered | `references/critique.md` |
| Movement 3 — generating directions | `references/proposal.md` |
| Movement 4 — mockup, then code | `references/build.md` |
| About to generate an image — direction board or product asset | `references/imagery.md` |

---

## Movement 0: Orient (always)

**Read `references/discovery.md` and run it.** It finds, for this specific
project: the frontend root, the stack, the real design tokens, the real routes,
the component inventory, the project's own rules, and — the step people skip —
**which design document actually governs, when several disagree.**

Do not assume a stack, a token file, or a design system. Derive them. A repo
that vendors, forks or overlays another product will contain design docs for a
product that is *not* the one you were asked to change.

Two constraints that hold in every project:

- **The layer of the request is the layer of the fix.** A UI request is answered
  in the frontend directory discovery identified. Do not drift into backend
  routes, build config or infrastructure unless asked. If a design genuinely
  needs a backend change, stop and say so — that is a different conversation
  with a different cost and usually a different deploy path.
- **Respect the project's own rules.** `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`,
  a design guide, a glossary. Discovery collects them. Where they conflict with
  this skill's defaults, **the project wins**.

---

## Movement 1: Understand

The deliverable is a short written account someone could hand to a new designer.
Not a file tour.

**1. Name the surface in the project's own words.** If the repo has a glossary
or domain doc, its terms are binding, including any "avoid this word" lists.
Wrong nouns produce wrong UI: a domain distinction the team fought for usually
has a visible counterpart on screen, and renaming it in a proposal quietly
proposes removing it.

**2. Trace one real path end to end.** Route → component → data fetch → what the
backend returns → what the user sees when it is empty, slow, long, or broken.

**3. Answer these five, in writing.** Everything downstream depends on them:

- **Who** is on this surface — an expert mid-task, or someone arriving cold?
- **What win** ends their visit? (finish a task / understand state / decide / set up)
- **What already exists** — which components, patterns and tokens?
- **How they arrive and where they go next.**
- **Which states are real here** — empty, one, many, very many, long strings,
  loading, error, stale, in-flight, permission-denied. Ask which of these a
  *new* user hits first; that state is the first impression, not an edge case.

**4. State the mode** (`references/critique.md` defines these): PERSUADE,
OPERATE, READ, EXPERIENCE, or HYBRID. The mode decides which rules apply.
Classify the *surface*, not the product — a developer tool's landing page is
still PERSUADE.

**5. Say what is unresolved.** Drift between documents, a state nobody designed,
a term used two ways, a token bypassed. Name it plainly — this is the most
useful paragraph you will write, and `understand` mode ends here.

---

## Movement 2: Audit

Read `references/critique.md` in full first.

Get the thing on screen before judging it. Discovery found the dev command and
port; **ask before starting a server**, then:

```bash
# is it already up?
curl -s -o /dev/null -m 3 -w "%{http_code}\n" http://localhost:<port> || echo NOT_RUNNING
```

**If the app is behind auth,** say so immediately and offer the two ways
forward: open a headed browser for the user to sign in, or have them supply a
throwaway local credential. Never read credentials out of `.env`, never guess a
password, and never report an un-audited surface as audited. Reaching the login
wall is a blocker to surface in one line, not something to work around quietly.

**Capture at 375 / 768 / 1440 and read every image back.** A width you have not
looked at is a width you have not verified.

> **Assert the viewport before trusting any capture.** Browser-automation tools
> routinely ignore a viewport change on re-navigation and hand back the previous
> size. Before each screenshot, evaluate `innerWidth` and confirm it matches what
> you asked for; if it does not, close the browser and reopen at that width.
> Captures silently taken at the wrong size are the most common way a design
> audit ships a false finding.

If no browser is available, say so once and audit components and tokens instead,
labelling every finding **un-verified**.

Then walk `references/critique.md`: mode classifier → checklist → slop pass →
hard rules. Findings are specific, tagged `high` / `medium` / `polish`, each with
evidence and a concrete fix. Ten findings you can point at beat thirty
adjectives. End with **Quick Wins** — the 3–5 highest-impact fixes under 30
minutes each.

---

## Movement 3: Propose

Read `references/proposal.md` in full first.

Three directions, presented as text concepts **before** anything is drawn. Each
names the disagreement about the user that it embodies, and what it costs.

How the directions differ depends on what discovery found. If the project has a
locked brand or design system, they may not differ by colour — they differ by
structure, density, hierarchy, disclosure and what each refuses to show.
`references/proposal.md` covers both cases.

When the disagreement is genuinely about **atmosphere** rather than structure, a
direction board can help — see `references/imagery.md`. Concepts in text come
first, always.

---

## Movement 4: Build

Read `references/build.md` in full first.

Standalone mockup in the scratchpad against the real tokens → verify at three
widths → only then port to the project's stack. Real content from the actual
data shapes, never lorem ipsum. Surgical edits in the refinement loop, never a
full rewrite.

Run only the test command discovery found for the layer you changed. Do not run
a repository-wide suite for an isolated frontend change unless the project says
to.

---

## Handoff

Write the result where the project already keeps design or decision records
(discovery finds this; otherwise ask, or use `docs/`). Include: the
understanding from Movement 1, findings with screenshots, the directions
considered, the one chosen and **why in product terms**, and an explicit list of
what you could not verify.

Propose the commit and ask before making it, unless the project's rules say
otherwise or the run is an automated pipeline.

---

## Rules

1. **Understand before proposing.** If you cannot say who the surface is for and
   what ends their visit, you are not ready to redesign it.
2. **Explain every choice as "X because Y",** where Y is about this product's
   users — never "it looks cleaner".
3. **Evidence or silence.** A screenshot you looked at, a computed value, a line
   of code. No finding from imagination, and no finding from a capture you did
   not verify the size of.
4. **Derive, do not assume.** Tokens, stack, routes, vocabulary and rules come
   from this repo, every time. The last project's answers do not carry over.
5. **Stay in the layer you were asked about.** Wanting to touch another is a
   signal to stop and ask, not a step.
6. **Vocabulary is design.** Use the project's terms, including what it forbids.
7. **Every state is designed,** or you have designed the happy path only. Start
   with whichever state a new user hits first.
8. **An image is never the thing being designed.** Build the real markup, verify
   it in a browser, and generate only assets the surface genuinely needs —
   `references/imagery.md` draws the line.
9. **Accept the user's final call.** State the coherence cost once, then build
   what they chose.
10. **Conversation, not a form.** Pick a sensible default and start; let them
    redirect you in a sentence.
