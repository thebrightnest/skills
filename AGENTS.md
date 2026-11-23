# brightnest: agent context

A Claude Code plugin, written entirely in Markdown. No runtime, no
dependencies, no scripts, hooks, linters or tests, on purpose. Reviewing a
skill is reading it.

## Structure

```text
.claude-plugin/
  plugin.json         plugin manifest: name, version, description
  marketplace.json    single-plugin marketplace, so the repo installs from GitHub
skills/
  design-pass/        SKILL.md + references/
  product-pass/       SKILL.md + references/
  behavior-pass/      SKILL.md + references/
  compliance-pass/    SKILL.md + references/
  boring-business/    SKILL.md + references/ + templates/ + examples/ + scripts/ + data/
AGENTS.md             this file (CLAUDE.md imports it)
CHANGELOG.md          one entry per plugin version, bullets scoped by skill
README.md             what the plugin is and how to install it
```

Each skill folder holds only `SKILL.md` and `references/`. Repo-level files
(changelog, agent rules) live at the root, never inside a skill.

**Local dev:** the plugin is installed from GitHub
(`brightnest@thebrightnest`) and runs from a cached copy, so edits here aren't
live. To test uncommitted changes, disable the installed plugin and run
`claude --plugin-dir .`, or each skill loads twice. To release: bump `version`
in `plugin.json`, push, then run `/plugin marketplace update thebrightnest`.

## Rules for every skill

- A behaviour change bumps `version` in `.claude-plugin/plugin.json` (semver)
  and adds a `CHANGELOG.md` entry with bullets scoped by skill:
  `**product-pass:** …`. `SKILL.md` has no `version` field.
- Adding a skill: new folder under `skills/`, a row in `README.md`, and a
  mention in the `plugin.json` description.
- Adding a reference file means listing it in that skill's `SKILL.md` section
  index.
- Before saying a change is done, re-read every file it touched, and check that
  each `SKILL.md` section index still matches its `references/`.
- Style: short sentences, present tense, no em-dash asides, tables for anything
  compared.

## product-pass

Keeps a contract between a product's business side (personas, intended
journeys, promises) and its codebase (a present-tense snapshot of what the
product does). Both sides share a fit review and a decisions register. On the
business side it guides: sources are harvested into staging and walked with
the user, and only what they confirm enters the contract. Works for any
product, including one spread across several repos.

```text
SKILL.md              entry point: sides, modes, movements, rules, section index
references/           one file per step, loaded only when that step runs
  orient.md           Movement 0: side, repos, received copies, governing docs
  app-snapshot.md     the app/ half: capabilities, boundaries, grounding, glossary
  journeys.md         intended vs actual journeys, tracing and walking
  business-inputs.md  the business/ half and intake: harvest, stage, walk, confirm
  definitions.md      the quality bar and coaching questions for each definition type
  fit.md              the fit review
  check.md            reviewing material against app/
  decisions.md        the shared register, one file per item
  templates.md        first-time file creation
```

### Forbidden

- **Naming a real product** (a client, or one of the user's own) in `SKILL.md`
  or `references/`. Examples use unnamed archetypes: **A, output product** and
  **B, platform product**.
- **Recording where the other side lives.** The halves travel by manual copy.
  No counterpart path, URL or "kind" in `contract.json`.
- **Dropping a probe to make wording general.** When a sentence is generalised,
  every question it asked must survive, with an A and a B example that are as
  concrete as the original.
- Planned-tense language ("will", "coming soon") in anything the skill tells
  agents to write into `app/`.
- Backward-compatibility branches. When the contract format changes, migrate
  the existing contracts instead.

### Mandatory

- Keep the contract schema in `references/orient.md` step 1 in sync with
  `references/templates.md` and every example that shows `as_of`, `sources` or
  evidence citations (`<repo>:<path>[:<line>]`). The folder layout in
  `templates.md` is part of the schema: keep it in sync with the handoff in
  `orient.md` and the paths in every reference.
- Nothing reaches `business/` without the user confirming it in the walk. A
  change that lets drafts in unconfirmed breaks the skill's core promise.
- When the schema changes, list the live contracts that need migrating and
  offer to migrate them. They live in the product repos (`docs/product/`) and
  business folders (`product-contract/`).

## behavior-pass

Reviews a product through behavioral science and the Hook Model (trigger,
action, variable reward, investment). It reads a product-pass contract
(personas, intended and actual journeys, fit) and writes only to its own
folder, `behavior/`: a review, chosen hooks, habit test plans and its own
register of choices (`B-` IDs).

```text
SKILL.md              entry point: inputs, modes, movements, rules, section index
references/
  orient.md           Movement 0: the contract, its age, behavior.json, loop code
  hook-model.md       the frame: four phases, habit zone, research, sources
  habit-potential.md  habit hypotheses and the habit zone verdict per persona
  hook-audit.md       the loop each journey runs today, phase ratings, tactics
  ethics.md           Manipulation Matrix, Regret Test, patterns that fail
  proposal.md         two or three hook designs per journey
  habit-testing.md    identify, codify, modify, events and guardrails
  decisions.md        its own register, one file per item
  templates.md        behavior/ layout and first-time files
```

### Forbidden

- **Writing to the product contract.** `business/`, `app/`, `fit.md` and the
  contract's `decisions/` are read-only. What they lack becomes a `B-` item
  marked "Raise in the contract".
- **Proposing a hook that fails `ethics.md`**, or showing one as a contrast.
- **Naming a real product** in `SKILL.md` or `references/`, including the
  book's own case studies. Examples use the contract's archetypes: **A,
  output product** (C1, J-C1-1) and **B, platform product** (T2, J-T2-1).
- **Stating a research finding as evidence about users.** It's a reason to
  test.

### Mandatory

- Keep the contract fields this skill reads (the table in `SKILL.md`, "What
  it needs from the contract", and `habit-potential.md` step 1) in sync with
  product-pass's persona and journey templates. When product-pass renames or
  drops a field, update behavior-pass in the same change.
- Keep the `behavior/` layout in `templates.md` in sync with `orient.md`
  step 3 and the paths in every reference.
- Keep the phase ratings and loop verdicts identical across `hook-audit.md`,
  `templates.md` and `decisions.md`.

## compliance-pass

Audits product and website codebases at exact git commits (`as_of`), extracts
data flows, subprocessors, OAuth scopes, cookies, and AI systems, checks them
against GDPR, the EU AI Act, and modular national jurisdiction packs (starting
with Portugal B2B and consumer rules), keeps unconfirmed corporate and policy
choices in `decisions/` (`C-` IDs), separates a Counsel Review Brief in
`review.md` from clean publishable markdown in `documents/`, and renders native
legal pages on the website.

```text
SKILL.md              entry point: sides, modes, movements, rules, section index
references/
  orient.md           Movement 0: side, repo SHAs, git-diff triggers, copy handoff
  code-scan.md        extracting schemas, subprocessors, OAuth vaults, AI, cookies
  gdpr.md             Controller/Processor split, Art. 6 bases, ePrivacy, Google Limited Use
  eu-ai-act.md        Reg. 2024/1689 role classification, Art. 50 transparency, AI clauses
  jurisdictions.md    national law packs: Portugal (DL 7/2004, Lei 58/2019, Art. 809 CC, B2C)
  drafting.md         layered plain-language structure, Counsel Review Brief, publishing
  decisions.md        C- register for entity facts, retention choices, and policy questions
  templates.md        compliance/ layout and compliance.json schemas
```

### Forbidden

- **Naming a real product** in `SKILL.md` or `references/`. Use **A, output
  product** and **B, platform product**.
- **Inventing corporate or statutory entity facts** (company name, tax ID,
  address, retention choices) or placing `[TBD]` / `[⚠️ LEGAL REVIEW]` markers
  inside `documents/`.
- **Recording where the other side lives** in `compliance.json`. The `app/`
  inventory travels to `site` by manual copy.
- **Writing to a `product-pass` contract.** `contract.json` and its folders are
  strictly read-only.

### Mandatory

- Keep `<compliance_dir>/` paths and `compliance.json` schemas identical across
  `orient.md`, `decisions.md`, and `templates.md`.
- Every statement in `app/` and `site/` cites `<repo>:<path>[:<line>]`.

## boring-business

Discovers, ideates, validates, and prepares launches for profitable bootstrapped
micro-SaaS, niche directories, and workflow businesses. Bundles references,
templates, worked examples, zero-dependency Python helper scripts, and a
searchable case-study catalog (`case_studies.json` and `boringbiz.db`).

```text
SKILL.md              entry point: request router, five workflows, bundled index
references/           playbooks for ideation, validation, automation, SEO, copywriting
templates/            output templates for ideation, scorecards, deep reports, landing copy
examples/             worked examples for ideation, quick validation, deep validation
scripts/              score_calculator.py and search_case_studies.py (stdlib only)
data/                 case_studies.json and boringbiz.db (137+ case studies)
```

### Mandatory

- Keep `SKILL.md` references, templates, scripts, and data links in sync with
  the files on disk.
- Keep `scripts/` zero-dependency Python 3 (standard library only).

## Git

- Conventional commits, scoped by skill: `feat(product-pass): …`,
  `docs(design-pass): …`. Plugin-wide changes use `chore(plugin): …`.
- Branches: `feat/<skill>-<topic>`, `fix/<skill>-<topic>`.
- Remote: `origin` (GitHub, `thebrightnest/skills`). Ask before pushing.
