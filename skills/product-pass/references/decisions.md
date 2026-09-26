# Decisions: one place for everything we still have to settle

`decisions.md` is the contract's work queue. Every open question, finding,
inconsistency, proposal and unconfirmed draft lands here as **one item to
clarify or decide**, and nowhere else. Personas, journeys, promises, the app
snapshot and `fit.md` state what *is*. This file holds what's *not settled
yet*.

**This is not a gate.** Nothing in it blocks work. An unconfirmed persona is
still used, a contradicted promise can still ship, and a gap can stay open for
months. The register makes what's unsettled visible and ordered, so choosing
to leave something open is a conscious choice rather than an accident.

`fit.md` answers *how well do we fit today?* `decisions.md` answers *what do we
need to settle, and in what order?* Every non-served cell and every
contradiction in `fit.md` points to an item here by ID.

---

## What becomes an item

Everything that needs a human choice or a missing fact:

- a **fit gap** or **contradiction** from the fit review (one item per
  underlying issue, even if it shows up in several journeys);
- an **open question** found during intake (who pays, how often, which
  segments or regions, who administers the account);
- a **proposal** to change the business half, from intake of new material
  (another model's analysis, meeting notes, a new deck);
- an **unconfirmed draft** waiting to be adopted;
- an **inconsistency** between documents on either side, or inside the product
  (a term used two ways, a card that promises something its page doesn't do);
- a **validation** that needs outside evidence (an interview, walking a
  journey in the running app).

Don't write open questions, "TBD", "needs a decision" or "Open:" lines into
personas, journeys, promises, the snapshot or `fit.md`. Write the item here and
reference its ID from there if useful (`see D-007`).

## Item format

```markdown
### D-007: Should customer-facing announcements be a job we serve?

- **Kind:** decide            <!-- decide | clarify | validate | confirm -->
- **Status:** open            <!-- open | decided | parked | dismissed -->
- **Weight:** now · Real · high   <!-- priority · evidence · severity: for ordering only -->
- **Who decides:** business   <!-- business | product | both -->
- **Raised:** 2026-09-26 · intake of GLM (P6, N9) and Gemini (Persona 4) analyses
- **Touches:** personas C1, C4 · promises P10–P12, H10 · app A-4

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
| **clarify** | A fact someone has but the contract doesn't | An answer |
| **validate** | Needs outside evidence (interviews, walking the app, data) | Evidence, then usually a decision |
| **confirm** | A draft waiting to be adopted, changed or rejected | Adoption |

**Weight** is only for ordering. It's the priority of the persona it touches,
the strength of the evidence, and the severity: high = contradicts what we
say publicly or leaves a core step missing, medium = diverges or has major
friction, low = polish. It never means "must". Items that touch no persona
take the priority of whoever raised them, or `—`.

## Layout

```markdown
---
contract: decisions
updated: YYYY-MM-DD
---

# Decisions

<one line: N open (x decide, y clarify, z validate, w confirm), M decided since last review>

## Open

| ID | Question | Kind | Weight | Who |
|---|---|---|---|---|
<ordered by weight: now before later before vision, then Real before Observed before Inferred, then high before low>

<items, in the same order>

## Parked
<items deliberately left open, with why and when to revisit>

## Decided
<newest first. Each keeps its question and adds the lines below>
```

When an item is decided, move it to **Decided** and add:

```markdown
- **Decision:** 2026-09-27 · <who> · <the choice, in a sentence>
- **Consequence:** <what changes where: "personas.md C1 gains a job", "promise P8 reworded", "product: backlog">
- **Applied:** yes | pending on <side>
```

**Decided** is the one history in the contract. The snapshots don't keep
history, so this is how anyone finds out *why* a persona, promise or boundary
is the way it is. Don't delete decided items.

**Dismissed** means "not an issue". Keep it, with one line of why, so the same
finding isn't raised again next audit. When an audit finds something already
dismissed, it stays dismissed unless the evidence changed.

## Ownership and sync

The register is **shared**: either side adds items and records decisions.
Both sides hold the full file.

- The register travels by copy, like the halves. The other side's copy
  arrives as `decisions.incoming.md` (the handoff tells the user to save it
  under that name, so it never overwrites yours).
- In Movement 0, before adding anything, **merge** it: take the union of items
  by ID. For an ID present on both sides, keep the version with the later
  status change. Then delete `decisions.incoming.md`.
- If a copy overwrote `decisions.md` directly instead, recover yours from git
  and merge the two. Never silently lose an item.
- New IDs continue the highest ID in the merged file. If both sides created the
  same ID before syncing, renumber the newer one and note `(was D-012)`.
- A decision whose consequence falls on the other side's half is recorded
  here with `Applied: pending on <side>`. The owning side applies it on its
  next `apply` or `intake`. The register doesn't edit the other half.

## Tone

- Phrase every item as a question someone can answer, not a verdict. Write
  "Should P8 keep the 'any language' claim?", not "P8 is false".
- Always include "leave as is" as an option, with its consequence.
- Suggestions are welcome and labelled. The user decides, and "decided" means
  the user said so.
- Model-generated analyses, however persuasive, raise items as **Inferred**. Two
  models agreeing is still Inferred.
