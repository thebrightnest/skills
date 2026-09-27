# Changelog

All notable changes to the brightnest plugin. Versions follow `version` in
`.claude-plugin/plugin.json`. Scope each entry by skill: `**design-pass:** …`.

## 1.2.0 (2026-09-27)

- **product-pass:** intake guides instead of harvesting straight into the
  contract. Sources are graded by who produced them and harvested into
  `staging/`, which stays on the business side and is never copied. The user
  walks each candidate and keeps, edits, drops or parks it. Only what they
  confirm enters `business/`, stamped with the date.
- **product-pass:** new `references/definitions.md`: a quality bar, grades
  (passes, weak, fails) and coaching questions for personas, jobs, problems,
  scenarios, intended journeys, promises and positioning.
- **product-pass:** jobs are tagged functional, social or emotional. Personas
  gain a Problem per core job (I am, trying to, but, because, feel), a switch
  condition in Today they…, and optional "In their words" quotes (Real only).
- **product-pass:** `promises.md` can hold a positioning statement. The fit
  review and `check` test its slots against personas, jobs, Today they… and
  the app snapshot. The fit review also checks that the product removes each
  problem's cause, and that social and emotional jobs are served.
- **product-pass:** the fit review runs on confirmed definitions only. A
  review of staged candidates is provisional and raises nothing.
- **product-pass:** the register is a folder, `decisions/`, with one file per
  item and an index rebuilt on every write. Files are never renamed or
  deleted, so copies merge cleanly. The `confirm` kind is gone. Each run adds
  at most five items, and the rest go to a one-line Noticed list.
- **product-pass:** personas and intended journeys are one file per persona
  (`business/personas/`, `business/journeys/`). The handoff says to delete the
  old mirror before copying.
- **product-pass:** rule 13 is now "Stage everything, confirm deliberately",
  replacing "Never thin what you're given". The depth round is folded into
  the walk.

## 1.1.0 (2026-09-26)

- **product-pass:** a persona template with Required, Depth and Optional
  tiers, each field with a "thin if" test. It replaces the persona minimum,
  which intakes had been treating as the whole template.
- **product-pass:** intended journeys gain Trusts it when, Stakes, Gives up
  if, Shows it to, (guide) steps and a Scenarios link, plus a depth check.
- **product-pass:** intake harvests every source instead of picking one. The
  governing source settles conflicts only. Guidance becomes (guide) steps and
  situations become worked scenarios.
- **product-pass:** intake writes a source coverage ledger
  (`business/SOURCES.md`), runs a depth check, and ends with a depth round of
  at most five questions, asked after the draft exists.
- **product-pass:** the fit review checks input depth first (step 0) and runs
  trust needs and worked scenarios against the product (step 1b). A result the
  persona wouldn't trust rates the step `diverges`.
- **product-pass:** new rule 13, "Never thin what you're given".

## 1.0.0 (2026-09-26)

- The repo is a Claude Code plugin. Skills live in `skills/<name>/`, the
  manifest in `.claude-plugin/plugin.json`, and `.claude-plugin/marketplace.json`
  makes it installable with `/plugin marketplace add thebrightnest/skills`.
- One version for the plugin. `SKILL.md` files no longer carry `version`.
- One `CHANGELOG.md` and one `AGENTS.md` at the root, replacing the per-skill
  copies.
- Skill contents are unchanged: design-pass as of its 2.0.0, product-pass as
  of its 0.2.0 (history below).

## History before the plugin

Each skill was versioned on its own until 1.0.0.

### product-pass 0.2.0 (2026-09-26)

- A product can span several repos. `contract.json` gets a `repos` map (key,
  path, `surface`, role), and there's one `as_of` commit per repo. Sources and
  evidence are cited as `<repo>:<path>[:<line>]`. Staleness is checked per
  repo.
- The halves travel between sides by copy. The contract no longer records the
  counterpart's location. `apply` and `intake` end with a handoff that says
  what to copy. Orient detects what arrived and guards against a copy
  overwriting your own half. `decisions.incoming.md` is merged by ID.
- `side` in `contract.json` is final. On a first run, website/marketing repos
  are flagged as business-side candidates, and sibling repos are proposed as
  one repo map.
- References no longer use one product's terms. Every probe is kept, with
  paired unnamed examples (output product and platform product). `grounding.md`
  is now "why should a customer trust what the product does or produces?".
- Route and boundary discovery covers React Router, file-based routes, Laravel,
  FastAPI and Express, plus MCP and CLI entry points.
- `app_files` and a `run` entry per repo in `contract.json`.

### product-pass 0.1.0

- First version: app and business halves, fit review, and a shared decisions
  register, for a single-repo product.

### design-pass 2.0.0 (2026-09-25)

- Baseline for this changelog. Four movements (orient, understand, audit,
  propose, build) with discovery, critique, proposal, build and imagery
  references. Earlier history was not recorded.
