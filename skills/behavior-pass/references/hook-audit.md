# Hook audit: the loop each journey runs today

Movement 2. For each `habit candidate` persona, take its actual journeys from
the contract's `app/journeys.md` and describe the hook the product **already
runs**, phase by phase, with evidence. Then say where it breaks.

Describe what happens, not what's intended. A product with no notifications
has no owned triggers, whatever the roadmap says.

---

## 1. Which journeys

- Every actual journey with the ID of an intended journey for the target
  persona (`J-C1-1`), plus any `A-` journey that the persona repeats.
- Read its `fit.md` verdict first. A `partial`, `missing` or `refused`
  journey is still mapped, because the map shows where the loop breaks. But
  it gets no hook proposal (SKILL.md rule 2). Its top finding is "fix the
  journey first", pointing at the contract's item if one exists.
- **The return matters most.** A journey done once is an acquisition path.
  The hook lives in how the persona comes back the second, fifth and
  twentieth time. If the contract only has the first-time path, trace the
  return path yourself (app side) or mark it `not in snapshot`.

## 2. Map each phase

Fill one table per journey. Every cell cites evidence: a repo-qualified path
and line, a screen you saw, a contract line (`business/personas/C1.md:
Problem`), or a measured number.

| Phase | Asks | Look at |
|---|---|---|
| **Internal trigger** | Which feeling does this journey answer? Does the product ever name it or meet it? | Persona Problem and emotional jobs. Landing and entry copy |
| **External trigger** | What brings the user back, of which type (paid, earned, relationship, owned)? When does it arrive, and can they turn it down? | Orient step 4: notifications, emails, digests, invites, share links, the icon or bookmark |
| **Action** | What's the first thing they do on return, and what's required before the reward? Which of the six elements costs most? | The actual journey's steps and **Friction** line. Count clicks, fields, waits, hand-offs |
| **Variable reward** | What do they get, of which kind (tribe, hunt, self)? Where does the variability come from? Do they know when they're done? | The result screen, feed or summary. The persona's **Trusts it when** |
| **Investment** | What do they leave behind, and is it asked for after the reward? | Saved items, settings, history, invites. Orient step 4 |
| **Next trigger** | Does the investment make the next pass easier, or send the next owned trigger? | Whether saved data preloads the next session, whether an opt-in digest exists |

Worked example, A (output product), J-C1-1:

| Phase | Today | Rating | Evidence |
|---|---|---|---|
| Internal trigger | Fear of a post reading wrong. The landing page names it | holds | web:src/pages/index.astro:12 · C1 Problem |
| External trigger | None after the first visit. No email, no digest. Return depends on the user remembering | missing | no mail or notification code in web |
| Action | Returning user lands on a setup screen, re-picks audiences before pasting | weak: brain cycles, time | web:src/pages/Setup.tsx:40 |
| Variable reward | A read per audience, with the line that causes risk and the reason. Varies with every post (hunt, self) | holds | web:src/components/Reading.tsx:88 |
| Investment | Audiences can be saved, but only from settings, never offered after a read | weak | web:src/pages/Settings.tsx:22 |
| Next trigger | Saved audiences aren't preselected on return | missing | web:src/pages/Setup.tsx:40 |

Worked example, B (platform product), J-T2-1:

| Phase | Today | Rating | Evidence |
|---|---|---|---|
| Internal trigger | Monday overwhelm. Not named anywhere in the product | weak | T2 Trigger |
| External trigger | A daily email at 06:00 UTC with "your agent did 14 things". Arrives on Sunday too. Unsubscribe only in account settings | at risk | workspace:jobs/digest.py:30 · identity:templates/digest.html |
| Action | Sign in on the account site, then redirect to the workspace | weak: time, hand-off | identity:app/Http/Controllers/SsoController.php:42 |
| Variable reward | Triaged list, varies with the week's mail (hunt). Clear end: "nothing else needs you" | holds | workspace:src/pages/Triage.tsx:61 |
| Investment | Triage rules written in plain words, stored per workspace | holds | workspace:api/rules.py:18 |
| Next trigger | Rules shape next Monday's triage, but the email isn't timed to Monday morning | weak | workspace:jobs/digest.py:12 |

## 3. Rate each phase

| Rating | Means |
|---|---|
| `holds` | The phase does its job for this persona, with evidence |
| `weak` | Present but not doing its job: a trigger at the wrong moment, an action with a costly element, a fixed reward, an investment asked for before the reward or loading nothing |
| `missing` | Nothing in the product does this phase |
| `at risk` | Works through a tactic that fails the ethics check (`ethics.md`). Rated this way even when it works |

Say which element makes a phase `weak`: "action weak: brain cycles
(re-picks audiences)", not "action could be smoother".

## 4. Give each loop a verdict

| Verdict | When |
|---|---|
| **closed** | Every phase `holds`, and the investment loads the next trigger |
| **external only** | The loop runs, but only while the product sends triggers. No sign the internal trigger leads here (no unprompted returns in analytics, or none measured) |
| **open** | A phase is `missing`. Usually the return trigger or the investment. The product is used, not returned to |
| **at risk** | Any phase is `at risk`, whatever the others |

A `closed` verdict needs a walked journey or measured returns. From code
alone, the best verdict is **closed (unverified)**.

## 5. Inventory the tactics

List every mechanic the product uses to bring users back or keep them
engaged: notifications, emails, digests, badges, streaks, counters, feeds,
autoplay, red dots, trials, cancellation flows, default opt-ins. For each,
run the checks in `ethics.md` and record:

| Tactic | Where | Phase | Quadrant | Regret test | Pattern | Evidence |
|---|---|---|---|---|---|---|
| Daily digest email, Sundays included | workspace:jobs/digest.py:30 | external trigger | facilitator | fails: arrives when nothing needs them | unasked frequency | … |

A tactic that fails is `at risk` in its phase, and a candidate item
("change it, or leave as is?").

## 6. Rank where the loops break

Group breaks by **underlying issue**. One missing return trigger across three
journeys is one issue. Rank by:

1. **Persona priority**: `now` > `later` > `vision`.
2. **Evidence**: Real > Observed > Inferred.
3. **Phase order**: a break earlier in the loop outranks a later one. No
   trigger means nothing else runs.
4. **Severity**: `at risk` > `missing` > `weak`.

Each ranked break is a finding. The top five become items in `decisions/`,
unless the contract's register already holds them (then reference its ID).
The rest go under Noticed.

## 7. What the audit never does

- It doesn't propose. "Preselect saved audiences" is a proposal
  (`proposal.md`). The finding is "next trigger missing: saved audiences
  aren't preselected".
- It doesn't rate a phase `holds` because a feature exists. It holds when it
  does its job for the persona, with evidence.
- It doesn't count engagement as success. A loop that brings users back to a
  reward they don't value is `at risk`, not `closed`.
