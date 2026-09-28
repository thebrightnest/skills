# Decisions: the choices the review raises

`behavior/decisions/` holds one file per choice the review raises: fix a
trigger, drop a tactic, test a hook, ask the business side for a persona's
Rhythm. It is this skill's own register. The product contract has its own,
and this skill never writes to it.

**Not a gate.** Nothing here blocks work. A tactic at risk can stay. The
register makes it a choice instead of a default.

---

## What becomes an item

| Becomes an item | Doesn't |
|---|---|
| A ranked loop break (one per underlying issue) | A break already open in the contract's register: reference its ID |
| An existing tactic that fails the ethics check | A tactic that passes |
| A hook to build or test | A design not chosen: it's a line in the hook file |
| Missing contract depth (Rhythm, a "feel", a return step) | Anything `Inferred · low`: that's Noticed |
| A user's choice to keep a failing tactic | |

**At most five new items per run**, highest weight first. The rest go under
Noticed, one line each. Refreshing an existing item doesn't count.

## Layout

```text
decisions/
├── README.md    index and Noticed, rebuilt on every write
├── B-001.md
└── …
```

One file per item, named by ID. `B-` keeps IDs apart from the contract's
`D-` items. Never rename, move or delete an item file. Status lives inside.

## Item format

```markdown
---
id: B-003
kind: decide              # decide | clarify | validate
status: open              # open | decided | parked | dismissed
weight: now · Real · high # persona priority · evidence · severity
who: product              # product | business | both
raised: YYYY-MM-DD · audit of contract app@<sha> business@<v>
status_changed: YYYY-MM-DD
touches: C1 · J-C1-1 · H-C1-1
contract: D-012           # optional: the contract item it relates to
---

# B-003: Should the daily digest move to Monday morning, at a frequency users choose?

**Question.** One or two sentences, answerable.

**Context.** The finding, with evidence and its phase rating. Short.

**Options.**
1. …, with its consequence
2. …, with its consequence
3. Leave as is, with its consequence (always an option)

**Suggestion.** Optional, labelled, one line of why.
```

| Kind | Means | Closed by |
|---|---|---|
| **decide** | A choice between options | A decision |
| **clarify** | A fact the contract lacks (a persona's Rhythm, who the users include) | An answer, then `Raise in the contract` |
| **validate** | Needs outside evidence (a habit test, analytics, interviews) | Evidence, then usually a decision |

**Weight:** persona priority, evidence, and severity. High: an `at risk`
tactic, or a missing trigger on a `now` persona. Medium: `missing` later in
the loop, or `weak` at the trigger or action. Low: other `weak` phases.

When decided, set `status: decided`, update `status_changed`, and add:

```markdown
**Decision.** YYYY-MM-DD · <who> · <the choice, in a sentence>

**Consequence.** <what changes: "H-C1-1 chosen", "digest moved: product backlog", "keep streak: user's call, fails the Regret Test (informed)">

**Raise in the contract.** <what the business or app side should record, for /product-pass decide> | none
```

A decision to keep a failing tactic records the check it fails and the
user's reason (`ethics.md`).

## The index: `decisions/README.md`

Rebuilt from the item files on every write. Never edited by hand.

```markdown
# Behavior decisions

<one line: N open (x decide, y clarify, z validate), M decided since last review>

## Open
| ID | Question | Kind | Weight | Who |
|---|---|---|---|---|

## Parked
| ID | Question | Revisit |
|---|---|---|

## Decided
| ID | Question | Decision | Date |
|---|---|---|---|

## Dismissed
| ID | Question | Why |
|---|---|---|

## Noticed
<one line each: date, what, where, would-be weight>
```

## Tone

- Phrase each item as a question, never a verdict. "Should the streak reset
  after one missed day?", not "the streak is a dark pattern".
- Always include "leave as is", with its consequence.
- "Decided" means the user said so.
