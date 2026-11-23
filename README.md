# brightnest

A Claude Code plugin with five skills:

| Skill | What it does |
|---|---|
| `design-pass` | Understand a product's frontend, then audit it, propose directions, and build the agreed one. |
| `product-pass` | Keep the business side (personas, jobs, problems, intended journeys, promises, positioning) and the product codebase (what it does today) telling the same story. Guides you through each definition and keeps only what you confirm. |
| `behavior-pass` | Review the product with the Hook Model and behavioral science: which habits are worth forming, the loop each journey runs today, hook designs that pass the Regret Test, and habit test plans. Needs a `product-pass` contract. |
| `compliance-pass` | Scan product and website codebases at exact git commits, audit against GDPR, the EU AI Act, and national law packs (such as Portugal B2B + consumer rules), track legal/entity decisions, and draft or publish clean Privacy Policy, Terms of Service, and Subprocessors pages. |
| `boring-business` | Discover, ideate, validate, and launch profitable bootstrapped micro-SaaS and workflow businesses with Tier 1 quick scorecards, Tier 2 deep validation, a searchable database of 137+ case studies, and landing page copy blueprints. |

## Install

You need [Claude Code](https://docs.claude.com/en/docs/claude-code). Then:

1. Open Claude Code in any project and run:

   ```text
   /plugin marketplace add thebrightnest/skills
   /plugin install brightnest@thebrightnest
   ```

2. Restart Claude Code so the skills load.

Prefer the terminal? This does the same:

```bash
claude plugin marketplace add thebrightnest/skills
claude plugin install brightnest@thebrightnest
```

To check it worked, run `/plugin` and look for **brightnest** under installed
plugins.

## Use

Describe what you want and Claude picks the right skill:

- "Audit the onboarding screen" or "propose a redesign for the settings page"
  runs `design-pass`.
- "Does the product serve our personas?" or "can we claim this on the website?"
  runs `product-pass`.
- "Why don't users come back?" or "is this habit forming?" runs
  `behavior-pass`.
- "Audit our privacy practices" or "draft Terms of Service and Privacy Policy"
  runs `compliance-pass`.
- "Give me boring business ideas" or "quick validate this micro-SaaS idea"
  runs `boring-business`.

Or call a skill directly:

```text
/brightnest:design-pass audit /settings
/brightnest:product-pass understand
/brightnest:behavior-pass audit
/brightnest:compliance-pass scan
/brightnest:boring-business quick validate this idea
```

## Update

```text
/plugin marketplace update thebrightnest
```

Then restart Claude Code. `CHANGELOG.md` lists what changed.

## Uninstall

```text
/plugin uninstall brightnest@thebrightnest
```

## Develop locally

```bash
claude --plugin-dir /path/to/skills
```

See `AGENTS.md` for the repo rules.
