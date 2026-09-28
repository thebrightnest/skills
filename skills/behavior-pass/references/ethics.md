# Ethics: facilitator, not dealer

Habit-forming design is persuasion aimed at automatic behavior. That's why it
works, and why it can harm. This file holds the checks every tactic runs
through: every existing tactic in the audit, and every proposal before it is
shown to the user.

**The rule:** this skill proposes only hooks that pass all three checks
below. Existing tactics that fail are reported as risks with options,
including "leave as is". The user decides what ships.

---

## Check 1: the Manipulation Matrix

Eyal's two questions for whoever makes the product:

1. **Does it materially improve the user's life?** Would the persona say so,
   in terms of their own jobs?
2. **Would the maker use it themselves?** Is the team among its users, or
   could it be, for this behavior?

| | Maker uses it | Maker doesn't |
|---|---|---|
| **Improves users' lives** | **Facilitator** | **Peddler** |
| **Doesn't** | **Entertainer** | **Dealer** |

| Quadrant | Risk | In this skill |
|---|---|---|
| **Facilitator** | Blind spots: they assume users are like them | Proposals must sit here. Check the assumption against the persona's evidence |
| **Peddler** | Building for people they don't understand. Hubris, weak hooks | Allowed only when the persona evidence is Real: someone outside the team said it helps |
| **Entertainer** | Engagement without lasting value. Fades | Report. Not proposed |
| **Dealer** | Exploitation. Eyal: making something that doesn't improve lives and that you wouldn't use yourself "is called exploitation" | Report as `at risk`. Never proposed |

Judge the **behavior the tactic drives**, not the product. A useful product
can still run one dealer tactic.

## Check 2: the Regret Test

Eyal's later test, sharper than the matrix:

> If people knew everything the product designer knows, would they still
> execute the intended behavior? Are they likely to regret doing it?

Ask it concretely:

- **Informed:** if the persona saw the design reason ("we send this on
  Sunday because Sunday opens are high"), would they still act?
- **After:** an hour later, would they say the time was well spent?
- **Signals:** would they turn it off, unsubscribe or uninstall if they
  found the switch? Do they, when measured (`habit-testing.md`, guardrails)?

| Result | Means |
|---|---|
| **passes** | Informed users would act, and wouldn't regret it |
| **unclear** | Depends on the persona or the moment. Becomes a guardrail in the test plan |
| **fails** | Informed users wouldn't act, or would regret it |

## Check 3: autonomy and honesty

A tactic passes only when all hold:

- **The user can turn it down** in one step, from where it arrives
  (SKILL.md rule 7).
- **What it says is true.** Scarcity, counts, social proof and deadlines are
  real.
- **The reward ends.** The user can tell when they're done.
- **Variability comes from the job**, not from a mechanic added to it
  (SKILL.md rule 6).
- **It respects the persona's Boundaries and each journey's Must not** in
  the contract.

---

## Patterns that fail

These fail check 2 or 3 by construction. When the audit finds one, it's
`at risk`. A proposal never contains one.

| Pattern | Is | Why it fails | Honest alternative |
|---|---|---|---|
| **Punitive streak** | Progress lost after one missed day | Loss aversion used against the user. Lally: a missed day doesn't break a habit, so the punishment serves only the product | Progress that pauses, not resets. Weekly rather than daily when Rhythm is weekly |
| **Manufactured scarcity** | "Only 2 left", timers that reset | Untrue | Real limits, stated plainly |
| **Random rewards unrelated to the job** | Loot-box style surprises, points for opening the app | Variability from a mechanic, not the job | Variability from the content: this post, this Monday |
| **Bottomless feed without stopping cues** | No end to the reward | The search never ends. Compulsion | A clear "you're caught up" |
| **Unasked frequency** | Triggers at the product's convenience, not the user's moment | Fails the informed test | Triggers at the persona's stable moment, frequency chosen by the user |
| **Guilt and confirmshaming** | "No thanks, I don't care about my brand" | Shames a choice | Neutral decline |
| **Roach motel / forced continuity** | Easy in, hard out. Trials that roll into paid without warning | Fails the informed test | Leaving as easy as joining. Warn before charging |
| **Hidden defaults** | Opt-ins preselected, sharing on by default | Default not what most would choose | Defaults that match the persona's choice, visible |
| **Social pressure on invented data** | "Your team is waiting", read receipts turned into obligation | Relationship trigger bent into pressure | Real messages from real people |
| **Engineered anxiety** | Creating the negative feeling the product then relieves | Manufactures the internal trigger instead of answering one | Answer a feeling the persona already has, with evidence it's theirs |

The last one matters most for this skill. **An internal trigger has to come
from the persona's evidence.** A product can relieve an existing fear. It
must not teach users to fear something so it can relieve it.

## Vulnerable users and high stakes

Be stricter when the persona includes minors, people in financial, health or
emotional distress, or behaviors with money, health or safety at stake. In
those cases `unclear` counts as `fails`. When the contract doesn't say who
the users include, and the product could reach these groups, raise a
`clarify` item.

## When the user wants a failing tactic anyway

State what fails, once, in one or two sentences, with the pattern's honest
alternative. If they still want it, record a decided item: the tactic, the
check it fails, and their reason. Don't write its design. Their decision is
final, and the record says who made it.

## Wording in findings

Name the pattern and the evidence, never the intent. Write "the digest
arrives on Sundays when nothing needs the user: fails the informed test".
Don't write "the team is manipulating users". Most failing tactics are
defaults nobody revisited.
