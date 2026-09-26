# Fit: does the product serve the business?

`fit.md` is the contract review. It's a **snapshot of fit today**: what's
served, where it breaks, what contradicts. It is not a plan. It never says
what to build next, only where the gaps are and how much evidence stands
behind each one.

It can be built on either side, because both halves are present (one owned,
one received by copy). It's stamped with the versions of both, so either side
can tell whether it's current. When the other half is a mirror, every finding
carries `mirror as of <version>`, because the other side may have moved on.

---

## 1. Align every intended journey with its actual journey

For each intended journey in `business/journeys.md`, take the actual journey
with the same ID from `app/journeys.md` (or trace it now if it's missing) and
compare them step by step:

| # | Intended | Actual | Status | Evidence |
|---|---|---|---|---|
| 1 | Paste text first, nothing to set up | Must choose job and audience before pasting | **diverges** | web:src/pages/Setup.tsx:40 |
| 2 | Audiences remembered | Saved audiences, last one preselected | match | web:src/components/AudiencePicker.tsx:22 |
| 3 | Arrive already signed in | Signs in on the account site, then a redirect with a one-time ticket | friction | identity:app/Http/Controllers/SsoController.php:42 |

Step statuses:

| Status | Means |
|---|---|
| `match` | The product does this step as intended |
| `friction` | It works, with extra steps, waiting, unclear copy or required setup |
| `diverges` | The product does something different at this step |
| `missing` | Nothing in the product does this step |
| `refused` | The step asks for something `app/boundaries.md` refuses |

Also check the journey-level fields:

- **Walks away with:** does the actual output give them this?
- **Must not:** does anything in the actual journey do it anyway?
- **Time budget:** does the actual path fit it? (a walked journey only)

Then give the journey one overall verdict:

| Verdict | When |
|---|---|
| **served** | All steps `match` or minor `friction`, and the output matches. Requires `walked` for `now` priority |
| **partial** | The job can be done, but at least one step `diverges`, `missing` or has major `friction` |
| **missing** | The core step (usually the output) doesn't exist |
| **refused** | The job itself sits outside the boundaries. That's a business conversation, not a gap |

A `now` journey that is only `traced` can be at most **partial (unverified)**.

## 2. Persona × job matrix

One row per persona, one cell per job, each cell holding the verdict and the
journey ID. It's the one-screen answer to "does the product work for our
personas?".

| Persona | Evidence | Priority | Job 1 | Job 2 | Job 3 |
|---|---|---|---|---|---|
| C1 | Real | now | partial (J-C1-1) | served (J-C1-2) | missing (J-C1-3) |

## 3. Contradictions

Check every row of `business/promises.md` against `app/capabilities.md` and
`app/boundaries.md`:

- **Unbacked:** the claim describes something the product doesn't do today.
- **Over-claimed:** the product does it, but with limits the claim ignores
  (for example "validated insights" for a directional tool).
- **Refused:** the claim promises something the product actively refuses.
  A: conversion prediction, prices, individual prediction. B: "we never touch
  your data" when an operator can, or "works with any account" when only one
  provider is supported.

Also check each persona's `Boundaries` and each journey's `Must not` against
what the product does. A persona that must never get a prediction, on a path
that shows a score, is a contradiction. So is a persona whose credentials must
never be stored, on a path that stores them.

## 4. Code-ahead

Actual journeys with `A-` IDs, and capabilities no intended journey uses.
List them briefly, with what they do and which persona they *might* serve. This
is information for the business side, not a gap. The business side decides
whether it matters.

## 5. Rank the gaps and hand them to the register

`fit.md` states the fit. What to do about it lives in `decisions.md`. Group
the non-`served` steps and contradictions by **underlying issue**. One missing
capability that breaks three journeys is one item, not three. Then rank the
issues by:

1. **Priority** of the persona: `now` > `later` > `vision`.
2. **Evidence**: Real > Observed > Inferred > Unconfirmed draft.
3. **Severity**: `refused` contradiction or `missing` core step > `diverges` >
   `friction`.

Each ranked gap has a **direction**:

| Direction | Means | Addressed to |
|---|---|---|
| `business-ahead` | The persona or journey needs something the product doesn't do | Product/roadmap owner |
| `contradiction` | What we say and what the product does disagree | Whoever owns the wrong side. The user decides which |
| `stale` | The snapshot or mirror is out of date | This skill (`apply`) |
| `code-ahead` | The product does it and nobody uses it | Business side |

You rank gaps. **You don't turn them into a plan.** "J-C1-1 step 1 diverges:
Real / now" is a finding. "Build stimulus-first entry next sprint" is a
decision that isn't yours.

Each issue becomes (or updates) an item in `decisions.md` (see
`references/decisions.md`). A contradiction is a `decide` item ("change the
product, change the promise, or leave both?"). A `business-ahead` gap is a
`decide` item for the product side ("serve this step, and how?"). A traced-only
`now` journey is a `validate` item ("walk it"). `code-ahead` is a `decide` item
for the business side ("use this in a journey or a promise?"). Check the
register first: don't re-raise what's already open, decided or dismissed.
Refresh an existing item's weight and context instead.

---

## Write fit.md

```markdown
---
contract: fit
updated: YYYY-MM-DD
app_as_of:
  <repo>: <sha>
business_as_of: <sha|date>
---

# Fit review: <product>

## Summary
<3–5 sentences: how well the product serves the now-priority personas, the single most important gap, the most dangerous contradiction.>

## Persona × job matrix
…

## Ranked gaps
| # | Gap | Direction | Persona / evidence / priority | Evidence | Item |
…   <!-- Item = the decisions.md ID that carries it. No options or recommendations here -->

## Contradictions
…

## Code-ahead
…

## Journey alignment
<one table per intended journey, as in step 1>

## Not verified
<journeys only traced, the mirror's age, repos that couldn't be reached, unconfirmed business drafts. Each one is also a validate or confirm item>
```

No open questions, options or suggestions in `fit.md`. Those are items in
`decisions.md`, referenced by ID.

The **Summary** and **Ranked gaps** are what the business side reads. Keep
them in plain language. The alignment tables are the evidence behind them.
