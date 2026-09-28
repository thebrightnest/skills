# Proposal: hook designs for one journey

Movement 3. For one journey, design the hook that would close its loop.
Present two or three designs as text first. The user picks one. Only the
chosen design is written to `hooks/`.

---

## 1. Pick the journey

The top-ranked break in `review.md`, unless the user named one. Before
designing, check:

- **Fit.** The journey's verdict in the contract's `fit.md` is `served`. If
  it isn't, stop and say so (SKILL.md rule 2). The only proposal allowed is
  the fix to the step that breaks, and that fix is product work, raised in
  the contract's register, not a hook.
- **Habit zone.** The persona is a `habit candidate`. For `not a habit
  product`, propose recall and trust at the trigger moment instead, and say
  so.
- **Existing items.** No decided item here or in the contract already rules
  on this.

## 2. Find the bottleneck phase

From the audit table, the **earliest** phase that is `missing`, `weak` or
`at risk`. Fixing a later phase while an earlier one is missing changes
nothing: a better reward nobody returns to is still not a habit.

## 3. Generate two or three designs that disagree

Each design is a bet about **why the loop breaks**. They should differ in the
phase they lean on, not just in execution.

| | Design 1 bets on | Design 2 bets on | Design 3 bets on |
|---|---|---|---|
| A, J-C1-1 | **Action**: returning users can't get to the reward fast. Paste first, saved audiences preselected | **Next trigger**: users forget. An owned trigger at the publishing moment: a browser extension button in the editor they already use | **Investment**: nothing makes it theirs. Offer to save the audiences after the first read, and a "posts you checked" history that shows their flags going down |
| B, J-T2-1 | **External trigger**: the email arrives at the wrong moment. One summary, Monday at the start of their day, their time zone, frequency chosen by them | **Action**: the hand-off between sites costs the most. The summary links straight into the triage, already signed in | **Reward**: the triage doesn't end the worry. Lead with "nothing else needs you" and what the agent didn't touch |

Each design, in text:

```markdown
### Design <n>: <the bet, in a line>

**Habit.** After <stable moment>, <persona> <behavior>, because <internal trigger>. (from review.md)

| Phase | Today | This design | Principle | Evidence tag |
|---|---|---|---|---|
| Internal trigger | … | unchanged / how it's met | … | Real / Observed / Inferred |
| External trigger | … | … | owned trigger at a stable moment (Wood) | |
| Action | … | … | scarcest element: brain cycles (Fogg) | |
| Variable reward | … | … | hunt, variability from the post itself | |
| Investment | … | … | loads the next trigger | |

- **Ethics.** Quadrant: facilitator, because … · Regret test: passes, because … · Turned down by: …
- **Asks of the product.** What a user would see that they don't today, in the glossary's words.
- **Cost.** Rough size, and what it risks (a trigger users mute, a flow that gets longer).
- **What would prove it wrong.** The result in the habit test that drops it.
```

Rules for the designs:

- **Change as few phases as possible.** A design that changes everything
  can't be tested. One bottleneck, plus the phases it touches directly.
- **Every design passes `ethics.md`.** Run it before presenting. A design
  that fails isn't shown, even as a contrast.
- **Use principles as reasons, not decoration.** "Preselect saved audiences
  because brain cycles are the scarcest element at the publishing moment"
  is a reason. "Leverage the IKEA effect" alone is not.
- **Keep the product's words** from the contract's glossary, including what
  it forbids.
- **Stay present-tense about the product.** "Today" describes what exists,
  with evidence. "This design" describes the proposal. Don't blur them.

Say which design you'd start with and why, in a line. Then let the user
choose, combine or reject.

## 4. Write the chosen design

To `hooks/H-<journey ID without the J->.md` (`hooks/H-C1-1.md`), from the
template in `templates.md`. Status `chosen`. Include the designs not chosen
in one line each, with why, so the choice can be revisited.

## 5. Hand off

| The design needs | Hand to |
|---|---|
| New or changed screens | `/design-pass propose <surface>`, with the hook file as the brief |
| A test | `test H-C1-1` (Movement T) |
| A product decision (build it or not, when) | An item here, `who: product`. Not a plan |
| A change to the contract (a return step in the intended journey, a new Rhythm) | An item marked `Raise in the contract` |

You never build it yourself. You never edit the contract.
