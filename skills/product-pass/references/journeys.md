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

- **Persona:** C1 Global voice without local teams
- **Job:** Check a piece before publishing: how each audience reads it, and which line carries the risk.
- **Evidence:** Real (1 person)    **Priority:** now
- **Trigger:** A post is drafted. About 10 minutes before posting.

| # | Step | What the user needs at this step |
|---|---|---|
| 1 | Entry | Paste text or a screenshot first. Nothing to set up. |
| 2 | Choose audiences | Ready-made audiences by market and role, remembered after first use. |
| 3 | Read | Per audience: understood / risky, the line that causes it, the reason. |
| 4 | Decide | Publish, adjust, drop. Adjust = one click to retest against the same audiences. |
| 5 | Return | Next week, same audiences already selected. |

- **Walks away with:** a publish / adjust / drop decision, with the risky line named, per audience.
- **Must not:** predict engagement or reach. Say "ambiguous" when readings diverge.
- **Time budget:** minutes.
```

The same shape for a platform product (example B in `app-snapshot.md`):

```markdown
### J-T2-1: Let an agent work from my inbox

- **Persona:** T2 Operator running a small team's workspace
- **Job:** Have an agent triage my email and calendar without handing my password to anything.
- **Evidence:** Observed    **Priority:** now
- **Trigger:** Monday morning backlog.

| # | Step | What the user needs at this step |
|---|---|---|
| 1 | Entry | Arrive in my workspace already signed in. |
| 2 | Connect | Connect Google once, see exactly which scopes, revoke any time. |
| 3 | Delegate | Ask in plain words; the agent uses the connection without asking again. |
| 4 | Trust | See what the agent read and did. |

- **Walks away with:** a triaged inbox and a list of what the agent touched.
- **Must not:** store my Google password, or let another workspace see my mail.
- **Time budget:** under 5 minutes to first result.
```

Required fields: persona, job, evidence, priority, trigger, steps, walks away
with. `Must not` and `Time budget` are strongly recommended, because they're
what the fit review checks boundaries and friction against.

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
