# App snapshot: what the product does today

The `app/` half is written on the app side, from the code and the running app.
It's the only part of the contract that says what exists. Anyone on the
business side, or any model doing strategy work, reads it to know what they can
build a story on.

Five files, unless `contract.json` `app_files` drops `grounding`. Each one
answers one question, in present tense.

| File | Answers |
|---|---|
| `capabilities.md` | What can a user do today? |
| `journeys.md` | How is each job actually done, step by step? (see `journeys.md` in references) |
| `boundaries.md` | What does the product refuse, redirect or qualify, and what claims can it back? |
| `grounding.md` | Why should a customer trust what the product does or produces? |
| `glossary.md` | What does the product call things, and how do we say them to customers? |

Throughout this file, examples come in pairs from two kinds of product, so
the question is clear whatever the product is:

- **A, output product:** the user gets something generated or computed, like a
  reading, a score, a draft or an analysis (e.g. an AI tool that simulates how
  audiences in different countries react to a message).
- **B, platform product:** the user gets a place to work, store or run
  things, like a workspace, a hosted runtime or an integration hub (e.g. a
  multi-tenant agent workspace with SSO and connected accounts).

---

## Which repo feeds which file

`contract.json` `repos` gives each repo a `surface`:

| File | `user` repos | `operator` / `internal` repos |
|---|---|---|
| `capabilities.md` | yes | no, unless the operator layer *is* sold (e.g. "bring your own cloud") |
| `journeys.md` | yes, including steps that hop between them | only when a step visibly waits on it (provisioning a workspace) |
| `boundaries.md` | yes | yes: the limits and refusals it enforces |
| `grounding.md` | yes | yes: the guarantees it provides |
| `glossary.md` | yes (the words users see) | no |

A capability is described **once, by what the user gets**, even when three repos
cooperate to deliver it. "Sign in once and reach every workspace you've been
given" is one capability, even if the identity service, the workspace app and
the deploy layer each do a part. The sources list all three.

## Writing rules for every `app/` file

1. **Present tense only.** "Users can compare two variants." Never "will",
   "soon", "planned", "roadmap", "next". If it's behind an unreleased flag, on
   an unmerged branch, only in a PRD, or deployed in one repo but not wired up in
   the one users reach, it doesn't exist here.
2. **User level, not implementation.** Say what a user can do and see. Mention a
   table, a service, a model or a repo only when the business side must know it,
   because it's what a claim rests on:
   - A: "results cite the country profile that shaped them"
   - B: "connected-account tokens are held centrally, and a workspace only
     ever receives short-lived access"
3. **Structure, not inventory.** Describe the **unit of coverage and how it
   grows**, not the content that fills it today. Content changes weekly. The
   contract shouldn't.
   - A: ✅ "a profile exists per country, optionally per region and segment,
     and a new market can be commissioned". ❌ "we have profiles for BR, PT, DE…"
   - B: ✅ "each customer gets its own workspace at its own address, and an
     admin grants people access per workspace". ❌ "we run 12 tenants"
   - Same for integrations, templates, models and plans: ✅ "Google accounts
     can be connected (Gmail, Calendar, Drive), and the connector list is
     server-defined". ❌ a pasted list that will be wrong next month.
4. **Cite sources, qualified by repo.** Each section ends with the paths it was
   derived from: `Sources: web:src/pages/Setup.tsx, identity:routes/web.php`.
   These feed the frontmatter `sources`, which drives staleness detection per
   repo.
5. **Limits are part of the capability.** The limits are what stop marketing
   from over-claiming.
   - A: "compares up to N variants", "results are directional, never
     percentages"
   - B: "one workspace per invitation", "connectors are Google-only", "files up
     to N MB", "a workspace sleeps after N minutes idle"
6. **Say what you couldn't verify.** A capability found in code but not seen in
   the running app is marked `(traced, not walked)`. A capability whose parts
   span repos and was only verified in one is marked the same way.

## Frontmatter

```yaml
---
contract: app
file: capabilities
as_of:
  web: <sha>
  identity: <sha>
updated: YYYY-MM-DD
sources:
  - web:src/pages/
  - web:src/lib/scoring.ts
  - identity:app/Http/Controllers/
---
```

`sources` are repo-qualified paths or directories. Keep them tight enough that
an unrelated change doesn't mark the file stale, and wide enough that a
relevant one always does. `as_of` lists only the repos this file cites.

---

## Deriving each file

### capabilities.md

Start from what a user can reach, not from the code tree. Run discovery **in
each `user` repo**, adapted to the stack orient found:

```bash
cd <repo path>
# SPA routes (React Router, Vue Router)
grep -rhoE "path:\s*['\"][^'\"]+['\"]|<Route[^>]+path=['\"][^'\"]+" src app 2>/dev/null | sort -u | head -60
# file-based routes (Next, Nuxt, Astro, SvelteKit, Remix)
find . -path ./node_modules -prune -o \( -path "*/pages/*" -o -path "*/app/*/page.*" -o -path "*/routes/*" \) -type f -print 2>/dev/null | head -60
# Laravel / Rails-style route files
grep -rhoE "Route::(get|post|put|patch|delete|resource|apiResource)\(['\"][^'\"]+" routes/ 2>/dev/null | sort -u | head -60
# FastAPI / Flask / Express handlers
grep -rhoE "@(app|router|bp)\.(get|post|put|patch|delete|route)\(['\"][^'\"]+|(app|router)\.(get|post|put|patch|delete)\(['\"][^'\"]+" --include=*.py --include=*.ts --include=*.js . 2>/dev/null | grep -v node_modules | sort -u | head -60
# non-UI surfaces: MCP tools, CLI commands, webhooks, emails, exports
grep -rliE "mcp|@tool|server\.tool|click\.command|typer|webhook|Mailable|sendMail|export" --include=*.py --include=*.ts --include=*.php . 2>/dev/null | grep -v -E "node_modules|test" | head -30
```

Group capabilities by **what the user gets done**, not by screen or repo. For
each one, cover what it does, its limits, and where a user starts it. Include
non-UI surfaces (API, MCP, CLI, exports, emails, sharing, admin consoles)
because the business side sells those too. An admin console is a capability of
the *admin* persona, so name who uses it.

Existing product docs (a PRODUCT.md, a feature list, a status page, one repo's
description of another) are **leads, not truth**. Confirm each claim in the
code of the repo that owns it before carrying it over. Where a doc claims
something the code doesn't do, that's a finding.

### journeys.md

Read `references/journeys.md`.

### boundaries.md

What the product **won't** do is as important to the business side as what it
does. Find it where it's enforced, in every repo:

```bash
cd <repo path>
# refusals, redirects, guards, disclaimers
grep -rniE "refus|redirect|not supported|out of scope|disclaim|directional|representative|guard|forbidden|abort\(40[13]|raise HTTPException|throw new .*Exception" \
  --include=*.ts --include=*.tsx --include=*.php --include=*.py . 2>/dev/null | grep -vE "node_modules|test" | head -40
# policies, middleware, permissions, plan/rate limits, quotas, validation caps
grep -rliE "policy|middleware|gate|permission|role|rate.?limit|throttle|quota|max_|MAX_|limit" \
  --include=*.ts --include=*.php --include=*.py . 2>/dev/null | grep -vE "node_modules|test" | head -30
# feature flags: anything behind one that's off by default is not a capability
grep -rhoiE "feature[_-]?flag[^)]*|FEATURE_[A-Z_]+|flags?\.[a-zA-Z_]+" --include=*.ts --include=*.py --include=*.php . 2>/dev/null | sort -u | head -20
ls docs/adr docs/decisions docs/reference 2>/dev/null
```

Write three short sections:

- **Refused or redirected:** what the product actively stops, where it
  redirects instead, and where that's enforced (a qualified path).
  - A: asking for a conversion prediction is redirected to a qualitative
    reading.
  - B: a user without a grant can't open a workspace and is sent to the account
    page. A workspace can't reach another workspace's files.
- **Qualified:** what every result or action carries, such as a caveat, an
  evidence level, "directional, not predictive", a quota notice, or a
  data-retention statement.
- **Claims we can back:** the strongest honest sentence about the product,
  plus the claims we must never make.
  - A: "shows how each audience is likely to read it, and why", never
    "predicts performance".
  - B: "each workspace is isolated in its own runtime", never "SOC 2
    compliant" unless it is.

  If the project has a claim ladder, positioning ADRs or a security/boundaries
  doc, consolidate them here in plain language. Don't link to them as required
  reading.

Decisions (ADRs) are sources, not content. Extract the business consequence of
each relevant one in a sentence ("results never predict an individual's
behaviour: `web:docs/adr/0022.md`", "tenants never store refresh tokens:
`identity:docs/adr/0004.md`") and move on.

### grounding.md

**Why should a customer believe the output, or trust the product with their
work?** Describe the **mechanism**, never the current content. Answer each
probe, or say it doesn't apply and why:

1. **What is it built from?** The inputs that make the output or the service
   what it is.
   - A: how an audience is built (from documents, from a description, from a
     research profile, or a mix).
   - B: what a workspace runs on, and what it's connected to (the runtime, the
     models, the user's connected accounts).
2. **What must the user supply?** Uploads, descriptions, credentials, consent,
   configuration. Record it, because that's where trust starts and where
   journeys break.
3. **What is the unit of coverage made of, and how is it researched or
   secured?**
   - A: what a country/segment profile contains, where its content comes from,
     and how its depth is shown to the user.
   - B: what isolation a workspace gets (process, container, database,
     network), where data and secrets live, and who can reach them.
4. **How does coverage grow?** How a *new* unit becomes available, and
   roughly what that takes.
   - A: a new market or segment is commissioned, generated or requested.
   - B: a new workspace is provisioned (self-serve, admin grant, operator
     action), and a new connector is added.
5. **What does the user see at the moment they rely on it?** Provenance,
   evidence level, who has access, which account is connected, where their data
   went.
   - A: each result names the profile and sources that shaped it.
   - B: the user sees which Google account is connected, and can revoke it.
6. **What does the operator layer guarantee?** From `operator` repos, only
   the guarantees a customer would care about: isolation, backups, data
   location, secret handling, uptime mechanisms. Say what's guaranteed, and
   cite where it's enforced.

Don't list the markets, tenants, models or connectors currently covered.
That's inventory (rule 3).

### glossary.md

The words the UI actually uses, taken from the rendered text and the code in
every `user` repo, not from a doc:

| Term in the product | Means | Say to customers | Avoid |
|---|---|---|---|

If a repo has a domain glossary (CONTEXT.md, a ubiquitous-language doc), it's
the source for *meaning*. The UI is the source for *which words users see*.

A term used two ways is a finding. Multi-repo products drift here most. The
identity service says "tenant", the workspace app says "workspace", marketing
says "studio". Record which word the user sees at each surface. The mismatch
itself is a `decide` item.

---

## Updating (apply, app side)

1. Take the per-repo staleness worklist from orient step 3.
2. For each stale file, read its changed sources and rewrite **only the
   affected sections**. Don't regenerate the file.
3. If a change adds a source path the file doesn't list yet, add it to
   `sources`, qualified by repo.
4. Bump the affected repos' shas in the file's `as_of`, `updated`, and in
   `contract.json` `app.as_of`.
5. If a capability disappeared, remove it. The snapshot has no history. Git
   has it.
