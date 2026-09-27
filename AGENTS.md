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

## Git

- Conventional commits, scoped by skill: `feat(product-pass): …`,
  `docs(design-pass): …`. Plugin-wide changes use `chore(plugin): …`.
- Branches: `feat/<skill>-<topic>`, `fix/<skill>-<topic>`.
- Remote: `origin` (GitHub, `thebrightnest/skills`). Ask before pushing.
