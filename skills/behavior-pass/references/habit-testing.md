# Habit testing: identify, codify, modify

Movement T. A hook is a hypothesis until users form the habit. Eyal's habit
testing has three steps. This file turns them into a plan for one chosen
hook, written to `tests/`.

The plan is written in present tense about what exists today, and in
conditional terms about what the test will show. It never claims a result
nobody measured.

---

## 0. Can it be measured?

Orient step 4 found the analytics tool, or found none.

| Situation | Plan |
|---|---|
| Analytics with user-level events | Full plan: cohorts, habit path, guardrails |
| Page views only | Plan the events to add first. Until then, the test can't identify habitual users |
| No analytics | Say so. Offer a qualitative test: a diary or interviews with users in the persona, at 1, 3 and 8 weeks |
| Business side, no code | Write the plan in product terms. The event names are for the app side to fill |

Use the product's existing event naming (`orient.md` step 4). Never read
secrets or production data to build the plan.

## 1. Identify: who counts as a habitual user

Define it from the habit hypothesis, not from a generic metric.

```text
A habitual <persona> user <does the behavior> at least <N> times per <period>,
for <M> consecutive periods, <unprompted share>.
```

- **N and period come from Rhythm.** A weekly persona isn't judged on
  daily use. DAU/MAU is the wrong lens for a weekly habit.
- **Consecutive periods** separate a habit from a burst. Lally: weeks to
  months, so M covers at least 3 weeks for a daily habit and 4 periods for a
  weekly one.
- **Unprompted share** is the best signal of an internal trigger: the share
  of sessions that didn't start from a product-sent trigger (email,
  notification). It rises as the habit forms.

| | Habitual user |
|---|---|
| A | Checks at least 2 posts a week, 4 weeks in a row, and at least half the sessions start without a product email |
| B | Opens the triage on Monday morning 4 weeks out of 5, and at least a third of those opens aren't from the summary email |

Then: **what share of the persona's users meet it today**, if measurable?
Eyal's rough bar: if fewer than about 5% of users are habitual, the product
may not yet deliver enough value. Treat that bar as a heuristic.

## 2. Codify: the habit path

Look at what habitual users did that others didn't, especially early on.
That's the **habit path**. It's a hypothesis until checked against
non-habitual users.

| | Candidate habit path |
|---|---|
| A | Saved at least 2 audiences in the first week, and checked a second post within 3 days of the first |
| B | Wrote at least one triage rule in the first session, and opened a Monday summary in week one |

Without data, list candidates from the audit (what investment loads the next
trigger) and mark them `to confirm`.

## 3. Modify: push new users down the path

The chosen hook is the modification. State how it moves users onto the
habit path: "preselected saved audiences shorten the second check; the offer
to save after the first read gets audiences saved in week one".

## 4. The test plan

| Part | Holds |
|---|---|
| **Hypothesis** | If <hook>, then more <persona> users become habitual (step 1), because <bottleneck phase is fixed> |
| **Cohorts** | New users of the persona, before and after. Or a holdout when the product supports it. Existing habitual users are excluded from the primary result |
| **Duration** | At least long enough for M consecutive periods, plus the first period. Weeks, not days |
| **Primary metric** | Share of the cohort that meets the habitual definition |
| **Secondary** | Time to habit (periods until the definition is met), unprompted share, habit path completion |
| **Guardrails** | Regret signals (below). A guardrail that moves the wrong way stops the test, whatever the primary metric does |
| **Drop rule** | The result that ends the hook: "habitual share doesn't rise, or any guardrail crosses its line" |

**Events to instrument**, one row per event, in the product's naming:

| Event | When it fires | Properties | Exists today? |
|---|---|---|---|
| `post_checked` | A read is shown | audiences count, saved audiences used, source (direct, email, extension) | web:src/lib/analytics.ts:40 · yes, no `source` |
| `audiences_saved` | User saves audiences | count, offered after read (y/n) | no |

The **source** property (which trigger started the session) is what
measures unprompted share. Most products don't track it. Add it first.

## 5. Guardrails: regret signals

A hook that raises use and raises regret has failed. Measure at least two:

| Signal | Means |
|---|---|
| Trigger opt-out rate | Users turning down notifications or emails after this change |
| Unsubscribe or uninstall after a session | Regret right after use |
| Short sessions from triggers | Pulled in, found nothing, left |
| Session length far above the job's time budget | The reward doesn't end (the contract's journey Time budget is the reference) |
| A regret question | "Was this worth your time?" asked occasionally after a session |
| Support mentions | "too many emails", "can't turn off" |

Set a line for each before the test starts. Write it in the plan.

## 6. Write the plan

To `tests/T-<hook ID without the H->.md` (`tests/T-C1-1.md`), from
`templates.md`. Status `planned`. When the user reports a result, record it
in the file and update the hook's status to `tested` or `dropped`. A result
is recorded as the user reports it, with its source. You don't infer one.
