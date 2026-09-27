# Business inputs: harvest, stage, walk, confirm

The `business/` half is written on the business side. The product follows it
for **who we serve, why, and how their journey should go**. The app side never
edits it. It only receives it by copy and reviews fit against it.

**Only what the user confirmed is in `business/`.** Sources are harvested
into `staging/`, graded, and walked with the user one definition at a time.
Staging is a workspace, not a contract. It stays on the business side and is
never copied.

| Path | Holds | Travels |
|---|---|---|
| `business/personas/README.md` | At a glance, triggers → jobs, evidence log | yes |
| `business/personas/<ID>.md` | One confirmed persona, its jobs, problems and scenarios | yes |
| `business/journeys/<persona ID>.md` | That persona's confirmed intended journeys | yes |
| `business/promises.md` | Confirmed promises and positioning | yes |
| `staging/README.md` | The walk queue: every candidate, its grade and state | **no** |
| `staging/SOURCES.md` | The ledger: where every source section went | **no** |
| `staging/<candidate>.md` | One candidate definition, with what each source said | **no** |

**The fit review is only as sharp as `business/`.** A persona without its
needs, or a journey without its trust line, can't produce a gap. So the walk
asks for depth. It also works the other way: a persona padded with guesses
makes gaps look real that nobody has. Depth has to be confirmed, not
harvested.

---

## Persona template

Every field has a tier. The tier decides what the walk asks for. The user
decides what's kept.

| Tier | Means | When missing |
|---|---|---|
| **Required** | The fit review can't run without it | Asked in the walk before the persona is confirmed |
| **Depth** | What makes gaps findable | Asked in the walk, `now` personas first. Skipped: noted in the queue |
| **Optional** | Useful when the sources have it | Offered if a source has it. Never asked |

| Field | Tier | What it holds | Thin if |
|---|---|---|---|
| **ID and name** | Required | Short stable ID (`C1`, `V2`), a name a customer would recognize | The name is a job title only ("Marketing manager") |
| **Who** | Required | Role, organization, team size, the situation | No organization or situation |
| **Variants** | Depth | Sub-types with different needs, material or stakes | Two kinds of buyer merged into one list of needs |
| **Triggers** | Required | The moments that send them to the product, **in their words** | Generic ("wants insights", "needs to test") |
| **Jobs** | Required | Numbered (`C1.1`), each tagged functional, social or emotional (`definitions.md`, "Job") | No "so", a feature in the "I want", or social and emotional jobs nobody said |
| **Problem** | Depth, per core job | I am / trying to / but / because / feel, and one line (`definitions.md`, "Problem") | A feature in the "but", a symptom in the "because" |
| **Today they…** | Depth | What they do instead, the bar it sets (speed, cost, trust), and what would make them switch | No named alternative, no bar, or no reason to leave it |
| **What they need** | Depth | Needs across the whole journey, feature-free and checkable | Fewer than three, or phrased as features |
| **What they need to trust it** | Depth | What makes a result believable to them, and what makes them dismiss it | Missing. It's the field most often lost |
| **What they bring** | Depth | The material they start from (a post, a catalogue, a CSV, an inbox) | Missing when the product takes input |
| **Stakes** | Depth | What getting it wrong costs them | Missing |
| **Rhythm** | Depth | How often the trigger happens | Missing |
| **In their words** | Optional | Verbatim quotes. **Real only**, with who and when | A quote nobody said |
| **Buyer, user, approver** | Optional | Who pays, who operates, who signs off, if they differ | |
| **Channel role** | Optional | Whether one of them brings others (an advisor with clients) | |
| **Not this persona** | Optional | Near neighbours this persona is not | |
| **Evidence** | Required | Tag, plus the source. Tag individual claims that differ | Tag without source |
| **Priority** | Required | `now` / `later` / `vision`. **A business decision.** Never inferred | |
| **Boundaries** | Required | What the product must not do for them | Copied from another persona unchanged |
| **Worked scenarios** | Depth | Concrete situations per job, tagged (`definitions.md`, "Scenario") | None, or outcomes written as findings |
| **Open** | — | IDs of their items in `decisions/`. No questions inline | Questions written inline |

Evidence tags:

| Tag | Meaning |
|---|---|
| **Real** | Someone outside the team said or did this |
| **Observed** | The team used the product this way |
| **Inferred** | Hypothesis. Plausible, unconfirmed, and must not drive a bet alone |

A persona's tag covers its existence and core job. Depth fields carry their
own tag when it differs.

### Shape of `business/personas/<ID>.md`

```markdown
---
contract: business
file: persona
id: C1
as_of: <business version>
updated: YYYY-MM-DD
confirmed: YYYY-MM-DD · <who>
sources:
  - <material the confirmed text rests on>
---

# C1: <name>

- **Who:** …
- **Variants:** (only if needs differ)
  - **<variant>:** … Their material is … Their stakes are …
- **Triggers:** "…", "…"
- **Jobs:**
  1. (functional) When …, I want …, so …
  2. (social) When …, I want …, so …
- **Problem (job 1):** I am …, trying to …, but …, because …, which makes me feel …
  In one line: …
- **Today they…** … The bar this sets: … They'd switch when: …
- **What they need:**
  - …
- **What they need to trust it:** …
- **What they bring:** …
- **Stakes:** …
- **Rhythm:** …
- **In their words:** "…" (<who>, <date>)
- **Boundaries:** …
- **Evidence:** <tag>. <source, quote>
- **Priority:** now (D-NNN)
- **Open:** D-NNN

## Worked scenarios

| # | Scenario | Job | Walks away with | Source |
|---|---|---|---|---|
| C1-a | … | 1 | <the kind of read they need, never an outcome> | Real / Inferred, <source> |
```

A field that wasn't confirmed is left out, not filled with a guess. The depth
check reports it as missing, and the next walk asks for it.

Two examples of a **thin** and a **full** needs line:

| | Thin | Full |
|---|---|---|
| A, output product | "Wants to test posts" | "The read per audience, leading with risk: the line that causes it and the cultural reason" |
| B, platform product | "Needs integrations" | "Connect the mail account once, see exactly which scopes, revoke any time" |

### `business/personas/README.md`

- **At a glance:** ID, name, one-line job, rhythm, evidence, priority, confirmed.
- **Triggers → jobs:** each moment, its job statement, the personas it serves,
  the journeys that carry it. One job often serves several personas; this is
  the only place that shows it.
- **Evidence log:** when, source, what happened, which persona. Append only.
  Upgrade a persona's tag when evidence arrives.

Rebuild the first two sections whenever a persona file changes. They are
derived. The evidence log is not.

## Promise template

`business/promises.md` has two sections.

**Promises**:

| ID | Claim (as written) | Where it appears | Persona(s) | Since |
|---|---|---|---|---|

Copy the claim verbatim. The fit review checks it against `app/capabilities.md`
and `app/boundaries.md`, and paraphrase hides the problem. When the site lives
in this repo, "where it appears" is the page source path, which lets orient's
step 4 flag a promise as changed when its page changes.

**Positioning**: the slot table from `definitions.md`, "Positioning", when
the business has one. Record it from its source. Don't invent one.

---

## Intake: running it

Harvest and draft first, silently. Then walk. **Never open with a
questionnaire**, and never write a candidate into `business/` without the
user saying so.

### 1. Find every source

Search the business folder, and anything the user points to, for personas,
JTBD studies, problem statements, positioning docs, decks, meeting notes and
customer signals.

```bash
grep -rliE "persona|jobs.to.be.done|JTBD|ICP|segment|problem statement|positioning|pitch|tagline" \
  --include=*.md --include=*.mdx . | grep -v node_modules | head -40
# website repo: the pages are where promises live
find . -path ./node_modules -prune -o \( -path "*/pages/*" -o -path "*/content/*" \) \
  \( -name "*.astro" -o -name "*.md" -o -name "*.mdx" -o -name "*.tsx" \) -print 2>/dev/null | head -40
```

### 2. Grade each source by who produced it

| Produced by | Can support | Note |
|---|---|---|
| A customer (interview, email, call notes with quotes) | Real | The strongest input. Keep their words |
| The team, from using the product or watching someone use it | Observed | |
| The team's belief (strategy doc, deck, founder notes) | Inferred | Governs **priority** and **who we serve**, not facts about customers |
| A model (an analysis, a generated persona set) | Inferred, **candidate only** | Never governs. Two models agreeing is still Inferred |

Model output is often the largest source and the least grounded. It is useful
for finding questions and wording. Don't let its volume set the size of the
contract.

### 3. Harvest everything into staging

Orient step 5 decides which source **governs** conflicts. Harvesting keeps
the rest. Every section of every source lands in `staging/SOURCES.md`:

```markdown
| Source | Produced by | Section | Staged as | Note |
|---|---|---|---|---|
| analysis-1.md | model | C1 "What they need to trust it" | C1 | |
| analysis-1.md | model | C1 "How the app should guide" | J-C1-1 steps 1, 5 (guide) | converted to needs |
| analysis-2.md | model | Scenario 3 | C1 | reframed: no conversion claim |
| call-notes-03.md | customer | quote on reading humour | C1 "In their words" | |
| analysis-3.md | model | "Today the product does N runs" | — | product claim, app side's job |
| deck-v2.md | team | Slide 4 figure "40% faster" | — | unsourced figure |
```

A row with "—" needs a note. That is the whole of "never lose": everything is
accounted for here, and nothing reaches `business/` unwalked.

| Source says | Staged as |
|---|---|
| A persona field | That persona's candidate, with the source and its tag |
| A job, problem or scenario | That persona's candidate |
| "The app should…" (UX guidance) | A journey step marked **(guide)**, rewritten as a need |
| A persona nobody decided on | Its own candidate. Priority is asked in the walk |
| A public claim or positioning | The promises candidate |
| An open question the user can answer | A question in the candidate's walk |
| A claim about what the product does today | Nothing. It's the app half's job. Ledger note |
| An unsourced figure | Nothing. Ledger note |

### 4. Draft each candidate and grade it

One file in `staging/` per candidate: a persona (with its jobs, problems and
scenarios), its journeys, or the promises and positioning. In each:

- **Merged draft.** Where sources agree, one line. Where they differ, the
  governing source's line, with the others listed under it.
- **Grade** per definition, against `definitions.md`: passes, weak (which
  test) or fails (why).
- **Questions:** at most three per candidate, each tied to a failing test or
  a missing Required/Depth field, each with the draft's answer as the default.
- **Cut list:** what you'd leave staged, and why. Usually: jobs,
  scenarios and needs from a single model source that no customer or team
  observation supports.

Keep candidates small. A persona supported by one conversation gets one or
two jobs in its draft, not everything the analyses imagined. The rest stays
in the cut list, one line each, where the user can pull it back.

### 5. Order the queue

`staging/README.md`:

```markdown
| # | Candidate | Grade | Evidence | State | Next question |
|---|---|---|---|---|---|
| 1 | C1 persona | weak: one situation? | Real | walking | "Strategy and posting: one person or two?" |
| 2 | J-C1-1 | passes | Real | queued | — |
| 3 | C4 persona | weak: no problem | Observed | queued | "What does a founder do today instead?" |
| 4 | C5 persona | fails: no evidence | Inferred (model) | queued | "Keep, park or drop?" |
```

States: `queued`, `walking`, `confirmed`, `parked` (with why), `dropped`
(with why). Order: personas the user already named or backed with Real
evidence first. A persona before its journeys. Promises and positioning after
the personas they name.

### 6. Walk it with the user

This is the core of intake. Tell the user what you found in one short
paragraph: how many sources, what they produced, how many candidates, and
where you'll start and why. Then walk **one candidate at a time**:

1. Show the draft compactly: the definitions, each with its grade. Not the
   raw sources.
2. Ask the candidate's questions in one message, defaults included, so a
   one-word answer works.
3. Show the cut list in one line: "Left staged: 3 jobs and 4 scenarios from
   the model analyses. Pull any back?"
4. Take the answer: **keep**, **edit** (take the user's words), **drop**
   (with a reason) or **park** (with when to revisit). Parts can differ: keep
   the persona, drop one job.

Pace:

- Batch what passes. "C1's triggers, boundaries and scenario C1-a pass. Keep
  them?" is one question, not three.
- Stop when the user stops. Suggest a stopping point after each persona.
  Unwalked candidates stay queued, and the next `intake` resumes there.
- A question the user can't answer now ("how often does this happen?") stays
  in the candidate. It is not a decisions item, unless it needs someone else
  or outside evidence (`validate`).
- A priority or a choice between personas **is** a decision. Record it in
  `decisions/` as decided, straight away.

### 7. Confirm into `business/`

Write what the user kept, in the template above, stamped with `confirmed`.
Update `personas/README.md` and the queue. Parts not walked or not kept stay
in staging.

### 8. Depth check and summary

Check every confirmed `now` persona against the **Depth** fields (variants
count only when the persona has them) and its journeys against `journeys.md`,
"Depth check". A field that matches "Thin if" counts as missing.

```text
C1  now  Real      confirmed 2026-09-27   depth 6/8: no Problem, no Rhythm
C2  now  Real      walking                3 questions open
C4  now  Observed  queued
Staging: 9 candidates (2 confirmed, 1 walking, 5 queued, 1 parked)
```

End with the handoff (`orient.md`): what to copy to the app side. Staging is
never in it.

### 9. Keep the business half free of product facts

Personas and intended journeys describe needs, not features. "Needs to compare
two versions" is right. "Uses the Comparison view" is wrong. That mapping
belongs to fit. Guidance that names features ("a comparison view",
"remembered audiences") is rewritten as a need at the step where it applies
("the same audiences already selected"), then walked like anything else.

## Unabsorbed material

Orient step 4 lists new business material since the last intake. Harvest it
into staging (steps 2–4), and add its candidates to the queue. A change to a
confirmed definition is walked like a new one: show the confirmed text, the
proposed change and its source, and ask. A new customer signal usually means
an evidence-log row and maybe a tag upgrade. A new deck usually means new
promises.
