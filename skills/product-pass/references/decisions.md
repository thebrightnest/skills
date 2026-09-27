# Decisions: the choices still to make

`decisions/` is the contract's register of choices. It holds one file per
item: a question someone has to answer or a choice someone has to make,
between the business side and the product. Personas, journeys, promises, the
app snapshot and `fit.md` state what *is*. The register holds what's *not
settled yet*.

It is **not** the place for unconfirmed drafts. On the business side, a
definition nobody confirmed lives in `staging/` and is walked in intake
(`business-inputs.md`). The register is for choices.

**This is not a gate.** Nothing in it blocks work. A contradicted promise can
still ship, and a gap can stay open for months. The register makes what's
unsettled visible and ordered, so leaving something open is a choice rather
than an accident.

**It stays small on purpose.** A register of fifty open items is a list
nobody reads. Every run adds only what someone could act on this month. The
rest is one line under **Noticed**.

---

## What becomes an item

| Becomes an item | Doesn't |
|---|---|
| A **fit gap** or **contradiction** (one per underlying issue, even across several journeys) | A definition waiting to be confirmed: that's staging |
| A **choice** about who we serve, what we say or what the product does | A question the user can answer in the walk: it stays in the candidate |
| An **inconsistency** between documents, or inside the product | Anything weighted `Inferred · low`: that's Noticed |
| A **fact** someone else has (`clarify`), or **outside evidence** needed (`validate`) | A second item for an issue already open, decided or dismissed |

### Limits per run

- `audit`, `apply` and `intake` add **at most five** new items per run, the
  highest weight first. The rest go under **Noticed**, one line each.
- A Noticed line becomes an item when the user asks, or when its evidence
  rises above `Inferred`.
- Refreshing an existing item's weight or context doesn't count.

Don't write open questions, "TBD", "needs a decision" or "Open:" lines into
personas, journeys, promises, the snapshot or `fit.md`. Write the item and
reference its ID from there (`see D-007`).

## Layout

```text
decisions/
├── README.md     index and Noticed. Rebuilt on every write, never edited by hand
├── D-001.md
├── D-002.md
└── …
```

- **One file per item, named by ID only.** A title can change without a
  rename.
- **Never delete or rename an item file, and never move it to a subfolder.**
  The register travels by copy, and a copy adds and overwrites files but never
  removes them. A renamed or moved file would come back as a duplicate on the
  other side. Status lives inside the file.

## Item format

```markdown
---
id: D-007
kind: decide              # decide | clarify | validate
status: open              # open | decided | parked | dismissed
weight: now · Real · high # priority · evidence · severity: for ordering only
who: business             # business | product | both
raised: 2026-09-26 · audit of app@<sha>
status_changed: 2026-09-26
touches: C1, C4 · P10 · A-4
---

# D-007: Should customer-facing announcements be a job we serve?

**Question.** One or two sentences, answerable.

**Context.** What was found, with evidence (paths, quotes, promise and journey IDs). Short.

**Options.**
1. …, with its consequence
2. …, with its consequence
3. Leave as is, with its consequence (always an option)

**Suggestion.** Optional. Labelled as the skill's suggestion, one line of why.
```

Kinds:

| Kind | Means | Closed by |
|---|---|---|
| **decide** | A choice between options | A decision |
| **clarify** | A fact someone has but the contract doesn't, and the user can't answer in the moment | An answer |
| **validate** | Needs outside evidence (interviews, walking the app, data) | Evidence, then usually a decision |

**Weight** is only for ordering. It's the priority of the persona it touches,
the strength of the evidence, and the severity: high = contradicts what we
say publicly or leaves a core step missing, medium = diverges or has major
friction, low = polish. It never means "must". Items that touch no persona
take the priority of whoever raised them, or `—`.

When an item is decided, set `status: decided`, update `status_changed`, and
add:

```markdown
**Decision.** 2026-09-27 · <who> · <the choice, in a sentence>

**Consequence.** <what changes where: "C1 gains a job", "promise P8 reworded", "product: backlog">

**Applied.** yes | pending on <side>
```

Decided items are the one history in the contract. The snapshots don't keep
history, so this is how anyone finds out *why* a persona, promise or boundary
is the way it is.

**Parked** keeps the item with a line saying why and when to revisit.
**Dismissed** means "not an issue". Keep it, with one line of why, so the
same finding isn't raised again. It stays dismissed unless the evidence
changed.

## The index: `decisions/README.md`

Rebuilt from the item files every time an item changes. Never edited by hand.

```markdown
---
contract: decisions
updated: YYYY-MM-DD
---

# Decisions

<one line: N open (x decide, y clarify, z validate), M decided since last review>

## Open

| ID | Question | Kind | Weight | Who |
|---|---|---|---|---|
<ordered by weight: now before later before vision, then Real before Observed before Inferred, then high before low>

## Parked

| ID | Question | Revisit |
|---|---|---|

## Decided

| ID | Question | Decision | Date |
|---|---|---|---|
<newest first>

## Dismissed

| ID | Question | Why |
|---|---|---|

## Noticed

<one line each: date, what, where, would-be weight. Not items. Promoted on request or new evidence>
```

To read the register, read the index. Open an item file only when you work
on that item.

## Ownership and sync

The register is **shared**: either side adds items and records decisions.
Both sides hold the full folder.

- It travels by copy, like the halves. The other side's copy arrives as
  `decisions.incoming/` (the handoff says so), so it never overwrites yours.
- In Movement 0, before adding anything, **merge** it file by file:
  - an ID only in `incoming/`: take it;
  - an ID in both: keep the one with the later `status_changed`. Same date
    and different content: keep yours and tell the user, with both versions;
  - the same ID with a **different question** (both sides created it before
    syncing): renumber the incoming one to the next free ID, and note
    `(was D-012 on the <side> side)`.
  Then merge the Noticed lines, rebuild the index and delete
  `decisions.incoming/`.
- If a copy landed straight in `decisions/` instead, recover yours from git
  and merge. Never silently lose an item.
- New IDs continue the highest ID in the merged folder.
- A decision whose consequence falls on the other side's half is recorded
  with `Applied: pending on <side>`. The owning side applies it on its next
  `apply` or `intake`. The register doesn't edit the other half.

## Tone

- Phrase every item as a question someone can answer, not a verdict. Write
  "Should P8 keep the 'any language' claim?", not "P8 is false".
- Always include "leave as is" as an option, with its consequence.
- Suggestions are welcome and labelled. The user decides, and "decided" means
  the user said so.
- Model-generated analyses, however persuasive, raise items as **Inferred**. Two
  models agreeing is still Inferred.
