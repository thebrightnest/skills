# Habit potential: which behavior, for whom, and should it be a habit

Movement 1. Before mapping any loop, decide **which behavior** you want to
become automatic, **for which persona**, and whether a habit is the right
goal at all. A hook designed for the wrong behavior works, and does harm.

The output is one **habit hypothesis** per `now` persona, then `later` ones
if the user asks. Each is built only from the contract. What the contract
lacks is a labelled assumption, never an invention.

---

## 1. Read the persona for habit material

| Contract field | Gives you | Thin when |
|---|---|---|
| **Rhythm** | Frequency: how often the trigger moment happens | Missing, or "regularly" |
| **Triggers** | The external moment, in their words | Generic ("wants insights") |
| **Problem**, "which makes me feel" | The internal trigger | Missing, or a feature in the "but" |
| **Jobs**, emotional and social | What relief and recognition look like | Only functional jobs |
| **Stakes** | Perceived utility: what getting it wrong costs | Missing |
| **Today they…** | The habit that already owns the moment, and its bar | No named alternative |
| **What they need to trust it** | What makes the reward believable | Missing |
| **Intended journey**, (guide) return steps | How the business side expects them to come back | No return step |

A persona without Rhythm or a "feel" can still get a hypothesis. Mark those
parts `Inferred (assumed here)` and raise a `clarify` item for the business
side.

## 2. Write the habit in one sentence

```text
After <stable moment>, <persona> <does the behavior>, because <internal trigger>.
```

| | Habit |
|---|---|
| A | After drafting a post for another market, C1 checks it here before publishing, because they fear it reads wrong where nobody local can tell them. |
| B | On Monday morning, before opening mail, T2 asks the agent for the triage, because the pile makes them feel behind before the week starts. |

Tests:

| Test | Fails when |
|---|---|
| **Stable moment** | "When they need it". Habits need a recurring cue (Wood) |
| **One behavior** | "Uses the product". Name the action |
| **Felt trigger** | The "because" is a benefit ("to save time") rather than a feeling or situation |
| **Evidence** | Nothing in the contract supports the moment or the feeling |

## 3. Place it in the habit zone

Two axes, from the contract:

- **Frequency**, from Rhythm: daily, several times a week, weekly, monthly,
  rarer.
- **Perceived utility**, from Stakes and the Problem: how much the persona
  gains or avoids each time, **as they see it**, not as the product sees it.

| Frequency | Utility needed for a habit | Verdict when utility falls short |
|---|---|---|
| Daily or several times a week | Moderate | `habit candidate` |
| Weekly | High | `habit candidate` if Stakes are real, else `unclear` |
| Monthly | Very high, and a fixed moment | Usually `not a habit product` |
| Rarer | Rarely enough | `not a habit product` |

Verdicts:

| Verdict | Means | What the review does |
|---|---|---|
| **habit candidate** | Frequent and useful enough for the behavior to become automatic | Audit and propose hooks |
| **not a habit product** | Too rare for automaticity | No hook. Aim for **recall at the trigger moment** (being the first thing they think of) and trust. Say so plainly |
| **unclear** | Rhythm or utility unknown | A `validate` item: measure frequency, or ask the persona |

A `not a habit product` verdict is a finding, not a failure. A tax filing
tool, a once-a-year audit, a hiring tool for a team that hires twice a year:
forcing a habit there produces nagging.

## 4. Name the habit it displaces

Every trigger moment is already owned by something: from Today they…

| | Today they… | What the old habit costs them | Switching bar |
|---|---|---|---|
| A | Message a colleague who knows the market, or publish and hope | Slow, depends on someone's goodwill, and nobody is local for most markets | Faster than the message, and gives a reason, not an opinion |
| B | Read the whole inbox themselves, first thing Monday | The first two hours of the week | A triage they trust enough not to reread everything |

The new habit has to beat the old one on the persona's **scarcest resource**
(`hook-model.md`, Action) at that moment. If Today they… has no bar, the
hypothesis is weaker: say so.

## 5. Vitamin or painkiller

| Is | When | Consequence |
|---|---|---|
| **Painkiller** | The Problem is felt at the trigger moment, and Stakes are real | The internal trigger already exists. The hook connects it to the product |
| **Vitamin** | The benefit is real but nothing hurts without it | The hook must create the association slowly, from a strong reward. Longer habit test |

## 6. Several personas, several habits

Different personas may need different habits from the same product. Keep one
hypothesis per persona. When two share a habit, say so once and link them.
When two habits conflict (one persona's trigger is another's noise), note it
for the audit: the triggers have to be set per persona.

---

## Output: the habit hypotheses table

Goes into `review.md`, section "Habit hypotheses", and the `understand`
account:

| Persona | Evidence · priority | Habit | Frequency | Utility | Zone | Displaces | Vitamin / painkiller |
|---|---|---|---|---|---|---|---|
| C1 | Real · now | After drafting…, checks…, because fear… | Several a week (Rhythm) | High (Stakes) | habit candidate | Message a colleague | painkiller |
| T2 | Observed · now | Monday, asks for triage… | Weekly, fixed moment | High | habit candidate | Reads it all | painkiller |

Then **Unresolved**: every cell marked `Inferred (assumed here)`, and what
would settle it.
