# Templates: creating `behavior/` for the first time

Create files only in a writing mode (`audit`, `propose`, `test`, `decide`),
and only the ones that mode needs. Never create anything inside the product
contract.

## Layout

```text
<behavior_dir>/
├── behavior.json    which contract it reads, and the versions it was built from
├── README.md
├── review.md        habit hypotheses, the loop per journey, tactics, ranked breaks
├── hooks/           chosen hook designs, one per journey
│   └── H-C1-1.md
├── tests/           habit test plans, one per hook
│   └── T-C1-1.md
└── decisions/       choices, one file per item (decisions.md)
    ├── README.md
    └── B-001.md
```

The folder lives next to the contract, on the side where it was run
(`orient.md` step 3). It doesn't travel between sides. If the user wants it
on the other side, they copy the folder whole.

## behavior.json

```json
{
  "product": "<name, from contract.json>",
  "contract": "<path to the contract_dir, relative to this repo or folder>",
  "contract_side": "app",
  "built_from": {
    "app_as_of": { "<repo>": "<sha>" },
    "business_as_of": "<sha|date>",
    "fit_updated": "YYYY-MM-DD"
  },
  "analytics": { "tool": "<name | none>", "events": "<repo>:<path where events are defined>" },
  "updated": "YYYY-MM-DD"
}
```

`contract` is a path on this side. It never points to the other side of the
contract.

## README.md

```markdown
# Behavior review: <product>

How <product> can form habits its users would not regret, reviewed with the
Hook Model against the product contract at `<contract path>`.

- **review.md**: which habits are worth forming, the loop each journey runs today, the tactics in use, where loops break.
- **hooks/**: chosen hook designs.
- **tests/**: habit test plans.
- **decisions/**: choices still to make.

Built from the contract: app <repo>@<sha>, business <v>, fit <date>. The
contract is read-only here. Maintained with `/behavior-pass`.
```

## review.md

```markdown
---
file: behavior-review
updated: YYYY-MM-DD
built_from: { app_as_of: { <repo>: <sha> }, business_as_of: <v>, fit_updated: <date> }
---

# Behavior review: <product>

## Summary
<3–5 sentences: which persona has a habit worth forming, whether any loop is closed, the single biggest break, the riskiest tactic.>

## Habit hypotheses
<table from habit-potential.md>

## Loops
<one table per journey from hook-audit.md step 2, with its verdict>

| Journey | Persona | Fit | Trigger | Action | Reward | Investment | Next trigger | Verdict |
|---|---|---|---|---|---|---|---|---|

## Where loops break
| # | Break | Phase | Persona / evidence / priority | Evidence | Item |
|---|---|---|---|---|---|

## Tactics
<table from hook-audit.md step 5>

## Not verified
<journeys traced only, phases rated from snapshot, the mirror's age, assumptions marked Inferred (assumed here)>
```

No proposals and no open questions in `review.md`. Proposals are in
`hooks/`. Questions are items in `decisions/`, referenced by ID.

## hooks/H-<id>.md

```markdown
---
id: H-C1-1
journey: J-C1-1
persona: C1
status: chosen            # chosen | built | tested | dropped
bottleneck: action
updated: YYYY-MM-DD
test: T-C1-1
---

# H-C1-1: <the bet, in a line>

<the chosen design, in the format from proposal.md step 3>

## Not chosen
- Design <n>: <the bet>. Not chosen because …
```

## tests/T-<id>.md

```markdown
---
id: T-C1-1
hook: H-C1-1
status: planned           # planned | running | done
updated: YYYY-MM-DD
---

# T-C1-1: <hypothesis, in a line>

## Habitual user
## Habit path
## Modification
## Plan
<the table from habit-testing.md step 4>
## Events
## Guardrails
## Result
<empty until the user reports one: date, source, numbers, what it means for the hook>
```
