# Business inputs: what the business side owes the contract

The `business/` half is written on the business side. The product follows it
for **who we serve, why, and how their journey should go**. The app side never
edits it. It only receives it by copy and reviews fit against it.

Three files:

| File | Answers | Template |
|---|---|---|
| `personas.md` | Who hires the product, for what, what they need, and how sure are we? | "Persona template" below |
| `journeys.md` | How should each job go for that persona, step by step? | `journeys.md`, "Intended journey format" |
| `promises.md` | What do we say publicly? | "Promise template" below |

**The fit review is only as sharp as these files.** A persona without its
needs, or a journey without its trust line, can't produce a gap. The product
looks like it fits because nobody said what fitting means. A shallow business
half is a defect, not a simplification.

---

## Persona template

Every field has a tier:

| Tier | Means | When missing |
|---|---|---|
| **Required** | The fit review can't run without it | `clarify` item, weight of the persona. Draft a labelled assumption and carry on |
| **Depth** | What makes gaps findable. Its absence hides them | Ask the user in the depth round (below). Unanswered: `clarify` item |
| **Optional** | Useful when the sources have it | Keep it if a source has it. Never ask |

A field in any tier that **a source has** is kept. Tiers decide what to ask
for, never what to keep.

| Field | Tier | What it holds | Thin if |
|---|---|---|---|
| **ID and name** | Required | Short stable ID (`C1`, `V2`), a name a customer would recognize | The name is a job title only ("Marketing manager") |
| **Who** | Required | Role, organization, team size, context | No organization or context |
| **Variants** | Depth | Sub-types with different needs, material or stakes | Two kinds of buyer are merged into one list of needs |
| **Triggers** | Required | The moments that send them to the product, **in their words** | Generic ("wants insights", "needs to test") |
| **Jobs** | Required | "When …, I want …, so …", one per distinct job, numbered (`C1.1`) | No "so", or a feature in the "I want" |
| **Today they…** | Depth | What they do instead, and **the bar it sets** (speed, cost, trust) | No named alternative, or no bar |
| **What they need** | Depth | Needs across the whole journey, feature-free and checkable | Fewer than three, or phrased as features |
| **What they need to trust it** | Depth | What makes a result believable to them | Missing. It's the field most often lost |
| **What they bring** | Depth | The material they start from (a post, a catalogue, a CSV, an inbox) | Missing when the product takes input |
| **Stakes** | Depth | What getting it wrong costs them | Missing |
| **Rhythm** | Depth | How often the trigger happens | Missing |
| **Buyer, user, approver** | Optional | Who pays, who operates, who signs off, if they differ | |
| **Channel role** | Optional | Whether one of them brings others (an advisor with clients) | |
| **Not this persona** | Optional | Near neighbours this persona is not | |
| **Evidence** | Required | Tag, plus the source. Tag individual claims that differ | Tag without source |
| **Priority** | Required | `now` / `later` / `vision`. **A business decision.** Never inferred | |
| **Boundaries** | Required | What the product must not do for them | Copied from another persona unchanged |
| **Worked scenarios** | Depth | At least one concrete situation per job, tagged | None, or outcomes written as findings |
| **Open** | — | IDs of their items in `decisions.md`. No questions inline | Questions written inline |

Evidence tags:

| Tag | Meaning |
|---|---|
| **Real** | Someone outside the team said or did this |
| **Observed** | The team used the product this way |
| **Inferred** | Hypothesis. Plausible, unconfirmed, and must not drive a bet alone |

### Shape

```markdown
## C1: <name>

- **Who:** …
- **Variants:** (only if needs differ)
  - **<variant>:** … Their material is … Their stakes are …
- **Triggers:** "…", "…"
- **Jobs:**
  1. When …, I want …, so …
- **Today they…** … The bar this sets: …
- **What they need:**
  - …
- **What they need to trust it:** …
- **What they bring:** …
- **Stakes:** …
- **Rhythm:** …
- **Boundaries:** …
- **Evidence:** <tag>. <source, quote>
- **Priority:** now (D-NNN)
- **Open:** D-NNN, D-NNN

**Worked scenarios**

| # | Scenario | Job | Walks away with | Source |
|---|---|---|---|---|
| C1-a | … | 1 | <the kind of read they need, never an outcome> | Real / Inferred, <source> |
```

Two examples of a **thin** and a **full** needs line:

| | Thin | Full |
|---|---|---|
| A, output product | "Wants to test posts" | "The read per audience, leading with risk: the line that causes it and the cultural reason" |
| B, platform product | "Needs integrations" | "Connect the mail account once, see exactly which scopes, revoke any time" |

### Worked scenarios

Scenarios are where a persona becomes testable. The fit review runs each one
through the product (see `fit.md`). Rules:

- One row per situation, tagged, with its source.
- **Walks away with** says what kind of answer the persona needs. It never
  states an outcome ("Concept A wins in market X"). An invented outcome in a
  business file reads as a finding a year later.
- When a source's scenario breaks a boundary (predicts conversion, states a
  regulation as fact, quotes an unsourced figure), keep the situation and
  reframe the output. Note the reframe in the source column.

## File-level sections of `personas.md`

- **At a glance:** ID, name, one-line job, rhythm, evidence, priority.
- **Triggers → jobs:** each moment, its job statement, the personas it serves,
  the journeys that carry it. One job often serves several personas; this is
  the only place that shows it.
- **Personas**, in the shape above.
- **Evidence log:** when, source, what happened, which persona. Append only.
  Upgrade a persona's tag when evidence arrives.

## Promise template

| Claim (as written) | Where it appears | Persona(s) | Since |
|---|---|---|---|

Copy the claim verbatim. The fit review checks it against `app/capabilities.md`
and `app/boundaries.md`, and paraphrase hides the problem. When the site lives
in this repo, "where it appears" is the page source path, which lets orient's
step 4 flag a promise as changed when its page changes.

---

## Intake: running it

### 1. Find every source

Search the business folder, and anything the user points to, for personas,
JTBD studies, positioning docs, decks, meeting notes and customer signals.

```bash
grep -rliE "persona|jobs.to.be.done|JTBD|ICP|segment|positioning|pitch|tagline" \
  --include=*.md --include=*.mdx . | grep -v node_modules | head -40
# website repo: the pages are where promises live
find . -path ./node_modules -prune -o \( -path "*/pages/*" -o -path "*/content/*" \) \
  \( -name "*.astro" -o -name "*.md" -o -name "*.mdx" -o -name "*.tsx" \) -print 2>/dev/null | head -40
```

### 2. Harvest, don't pick

Orient step 5 decides which source **governs**. That settles conflicts: two
priorities for one persona, two names for one job. **It doesn't decide what's
kept.** Harvest every non-conflicting field from every source, into the
template above.

| Source says | Goes to |
|---|---|
| A persona field (needs, trust, rhythm, stakes, variants) | That field, with the source's evidence tag |
| A concrete situation | Worked scenarios, tagged, outcome reframed |
| "The app should…" (UX guidance) | A journey step marked **(guide)**, rewritten as a need |
| A persona or job no one has decided on | A `decide` item. The persona file doesn't change yet |
| An open question | A `clarify` or `validate` item |
| A claim about what the product does today | Nothing in `business/`. It's the app half's job. Note it in the ledger |
| An unsourced figure (fees, market sizes, percentages) | Nothing. Note it in the ledger |

**Convert, don't drop.** Guidance that names features ("a comparison view",
"remembered audiences") is still a need. Rewrite it at the step where it
applies: "the same audiences already selected".

### 3. Keep a source coverage ledger

Every intake writes `business/SOURCES.md`: one row per section of every
source, saying where it landed.

```markdown
| Source | Section | Landed in | Note |
|---|---|---|---|
| personas-analysis-1.md | C1 "What they need to trust it" | personas.md C1 | |
| personas-analysis-1.md | C1 "How the app should guide" | journeys.md J-C1-1 steps 1, 5, 6 (guide) | converted |
| personas-analysis-2.md | Scenario 3 | personas.md C2-c | reframed: no conversion claim |
| personas-analysis-2.md | Persona 4 | decisions.md D-017 | undecided persona |
| personas-analysis-3.md | "Today the product does N runs" | — | product claim, app side's job |
```

A row reading "—" with no note is a loss. The ledger makes it visible, and the
next audit checks it (`orient.md` step 4).

### 4. Draft, labelled

Drafts are allowed and used right away. Mark every drafted section:

```text
> **Unconfirmed:** drafted by product-pass from <sources>. See D-NNN.
```

Adopting a draft is a `confirm` item. An unconfirmed section is reviewed for
fit, and its findings are labelled unconfirmed and ranked below confirmed
ones.

### 5. Depth check

Check every `now` persona against the **Depth** fields above (variants count
only when the persona has them), and its journeys against `journeys.md`,
"Depth check". A field that's present but matches "Thin if" counts as missing.
Write the result into the intake summary:

```text
C1  now  Real      depth 7/7: complete
C2  now  Real      depth 5/8: missing Trust, Rhythm; 2 needs phrased as features
C3  now  Real      depth 3/7: no scenarios, Today-they has no bar, no Stakes
```

### 6. Depth round: ask for what's missing

"Never open with a questionnaire" still holds. **Draft first**, then ask. Once
the draft exists, ask the user for what only they know, in one message:

- only for `now` personas, highest evidence first;
- at most five questions, each tied to a field and a persona;
- each with the draft's current assumption, so a one-word answer is enough.

| Missing field | Ask |
|---|---|
| Triggers | "When did <persona> last reach for something like this? What had just happened?" |
| Today they… | "What did they do instead? How long did it take, and who did they ask?" |
| Trust | "What would <persona> need to see before acting on a result? What would make them dismiss it?" |
| What they bring | "What do they have in hand when they start: a file, a link, a draft, nothing?" |
| Stakes | "What happens if they get this wrong?" |
| Rhythm | "How often does this happen: weekly, per project, once a year?" |
| Scenario | "Tell me one real case, even roughly." |
| Priority | "Is <persona> `now`, `later` or `vision`?" |

Unanswered questions become `clarify` items. The user can skip the round in a
word.

### 7. Keep the business half free of product facts

Personas and intended journeys describe needs, not features. "Needs to compare
two versions" is right. "Uses the Comparison view" is wrong. That mapping
belongs to fit. This rule governs **how** a need is phrased, never **whether**
it's kept (step 2).

## Unabsorbed material

Orient step 4 lists new business material since the last intake. For each one,
decide whether it changes a persona, a journey, a promise, the scenarios, or
the evidence log, and add its rows to `SOURCES.md`. Propose the change and
don't apply it silently. A new customer signal usually means an evidence-log
row and maybe a tag upgrade. A new deck usually means new promises.
