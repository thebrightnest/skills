# Journeys: intended and actual

A journey is how one persona gets one job done, from the **moment that
triggers it** to **what they walk away with**. It's the unit the fit review
works on. Personas and capabilities are too coarse to show where the product
fails someone. Journeys show it step by step.

There are two kinds, and they live in different halves:

| | Intended journey | Actual journey |
|---|---|---|
| Lives in | `business/journeys.md` | `app/journeys.md` |
| Written by | business side (`intake`) | app side (`apply`) |
| Describes | how it *should* go for this persona | how it *does* go in the product today |
| Evidence | the persona's evidence (Real / Observed / Inferred) | code paths (`traced`) or the running app (`walked`) |

**Same IDs on both sides.** An actual journey takes the ID of the intended
journey it serves (`J-C1-1`). A path the product supports that no intended
journey asks for gets an `A-` ID (`A-3`). Those are the code-ahead candidates.

---

## Intended journey format (business side)

```markdown
### J-C1-1: Check a post before publishing

- **Persona:** C1 · **Jobs:** C1.1, C1.3 · **Evidence:** Real (1 person) · **Priority:** now
- **Trigger:** "I'm about to publish." A post is drafted, about 10 minutes before it goes out.
- **Stakes:** a post that reads as disrespect in one market is screenshotted before it's deleted.

| # | Step | What the user needs at this step | Gives up if |
|---|---|---|---|
| 1 | Entry | Paste text or a screenshot, first. Nothing to set up before value. (guide) | Asked to configure anything first |
| 2 | Choose audiences | Several audiences by market and role, remembered after first use. | |
| 3 | Read | Per audience, leading with risk: understood or risky, the line that causes it, the reason. (guide) | It's a score without a reason |
| 4 | Ambiguity | Where readings of humor diverge, it says "ambiguous" instead of choosing. | |
| 5 | Decide | Publish, adjust or drop. Adjusting retests against the same audiences in one step. (guide) | |
| 6 | Return | Next week, same audiences already selected. (guide) | |

- **Trusts it when:** each reading gives a cultural reason, not a score, and ambiguity is admitted.
- **Shows it to:** nobody. The decision is theirs.
- **Walks away with:** a publish / adjust / drop decision, with the risky line named, per audience.
- **Must not:** predict engagement or reach. Give a confident verdict when readings diverge.
- **Time budget:** minutes. The alternative is a message to a colleague.
- **Variants:** —
- **Scenarios:** C1-a (Real), C1-b, C1-c.
```

The same shape for a platform product (example B in `app-snapshot.md`):

```markdown
### J-T2-1: Let an agent work from my inbox

- **Persona:** T2 · **Job:** T2.1 · **Evidence:** Observed · **Priority:** now
- **Trigger:** "Monday morning, 200 unread."
- **Stakes:** a missed client email, or a credential leaked to a tool they didn't vet.

| # | Step | What the user needs at this step | Gives up if |
|---|---|---|---|
| 1 | Entry | Arrive in my workspace already signed in. (guide) | Asked to sign in twice |
| 2 | Connect | Connect the mail account once, see exactly which scopes, revoke any time. | Scopes aren't shown |
| 3 | Delegate | Ask in plain words; the agent uses the connection without asking again. | |
| 4 | Check | See what the agent read and did. | |

- **Trusts it when:** every action is listed with what it touched, and nothing happened that wasn't asked.
- **Shows it to:** their team lead, when a triage rule changes.
- **Walks away with:** a triaged inbox and a list of what the agent touched.
- **Must not:** store the mail password, or let another workspace see the mail.
- **Time budget:** under 5 minutes to first result.
- **Scenarios:** T2-a.
```

Fields:

| Field | Tier | Why the fit review needs it |
|---|---|---|
| Persona, jobs, evidence, priority | Required | Ranking |
| Trigger, in their words | Required | Entry-point check |
| Steps: what the user needs | Required | Step-by-step alignment |
| Walks away with | Required | Output check |
| Must not | Required | Boundary and contradiction check |
| Trusts it when | Depth | Trust check: the most common silent gap |
| Time budget | Depth | Friction check on a walked journey |
| Stakes | Depth | Severity of a `diverges` or `missing` step |
| Gives up if | Depth | Turns friction into a rated failure |
| (guide) steps | Depth | Checks entry, defaults and what leads the result |
| Shows it to | Depth | Hand-over and export needs |
| Variants | Depth, when the persona has them | A step that differs by variant |
| Scenarios | Depth | Links the persona's worked scenarios the fit review runs |

**(guide) steps.** How a persona should be guided (the entry, the defaults,
what the result leads with) is a need like any other. Write it at the step it
applies to and mark it `(guide)`. "Stimulus-first entry" becomes "paste first,
nothing to set up before value". Never drop guidance because it sounds like a
feature. Rephrase it as a need.

### Depth check

A journey is **thin** when any of these hold:

- a step a reviewer couldn't rate `match` or `missing` ("a good experience");
- the entry step has no (guide) need, so how they start is unspecified;
- no **Trusts it when**;
- **Walks away with** isn't a concrete thing (a decision, a list, a file);
- a job in `personas.md` has no journey and no line saying which journey carries it.

Thin journeys are reported in the intake summary with the persona depth
check (`business-inputs.md` step 5).

Intended journeys describe needs, never repos or screens. The business side
doesn't know or care how many services deliver them.

---

## Actual journey format (app side)

```markdown
### J-T2-1: Let an agent work from my inbox

- **Verification:** walked 2026-09-26 (identity :8000 → workspace :8788) | traced
- **Entry points:** account page → workspace card · workspace Settings → Connectors · MCP `gmail_search`
- **Repos:** identity, workspace

| # | Step | What happens in the product | Evidence |
|---|---|---|---|
| 1 | Entry | User signs in on the account site, picks a workspace, and is handed over with a one-time ticket. | identity:app/Http/Controllers/SsoController.php:42 · workspace:api/sso.py:18 |
| 2 | Connect | Settings → Connectors → Google. Consent happens on the account site, then the user returns to the workspace. | workspace:src/pages/Connectors.tsx:31 · identity:routes/web.php:77 |
| … | | | |

- **Walks away with:** <what the product actually gives them>
- **Friction:** <counted clicks, required fields before value, waiting time, hand-offs between sites>
- **Limits:** <what this path can't do today>
```

Rules:

- **Describe what happens, not what's intended.** If the product requires an
  audience before the stimulus, or a workspace grant before sign-in, write
  that, even if the intended journey says otherwise. The fit review is where
  the difference is judged.
- **Every step cites evidence, qualified by repo.** A `repo:path:line` for
  `traced`. The screen, the URL, and what you did, for `walked`.
- **Hand-offs between repos are steps.** When the user leaves one surface for
  another (a redirect to an account site, an email link, a wait while
  something is provisioned), write it as its own step. That's where
  multi-service products lose people, and a trace that reads only one repo
  never sees it.
- **Present tense**, as everywhere in `app/`.

## Tracing a journey (always possible)

Start from the entry point and follow the code a user would trigger:

route → page component → form or fields required → API call → handler → what's
returned → what's rendered → where the user can go next.

When the call leaves the repo (an HTTP call to another service, a redirect to
another domain, a queued job another repo consumes), **follow it into the repo
that owns it** using the `repos` map. Find the receiving route or handler
there, and carry on. If that repo isn't in `repos` or can't be reached, stop
the trace there. Mark the step `leaves the snapshot: <where>`. If the repo
matters, that's a `clarify` item to add it.

Record what's **required before value** (fields, uploads, setup, grants,
connected accounts, provisioning), because that's where most intended
journeys break. Count the steps honestly.

## Walking a journey (when it matters)

Traced journeys miss what users feel: slowness, confusing copy, an empty
state that looks broken, a jarring jump between two sites with different
styles. **Walk the journeys of the highest-priority persona with the
strongest evidence** before marking them `served` in the fit review.

- Orient found the dev command, port and auth for each repo (`contract.json`
  `run`). A cross-repo journey needs every service it touches, plus whatever
  connects them locally. Ask before starting any server.
- If the app is behind auth, say so and offer two ways forward: open a headed
  browser for the user to sign in, or have them supply a throwaway local
  credential. Never read `.env`.
- Use real-looking input from the persona's trigger (their kind of post, their
  kind of inbox), not lorem ipsum.
- Note the time to first useful result, and every point where you had to
  guess what to do.
- No browser, or some services can't run locally? Say so once, walk what you
  can, and keep the rest `traced`.

## Which journeys to write

On the app side, write an actual journey for **every intended journey in the
received `business/`**, plus the product's main paths that serve none of them
(`A-` IDs). If `business/` doesn't exist yet, write the product's main paths
with `A-` IDs only, and say that fit can't be reviewed until the business side
provides intended journeys.

Admin and operator-facing paths (granting access, creating a workspace)
count when some persona does them. Give them `A-` IDs if no intended journey
asks for them yet.
