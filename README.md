# brightnest

A Claude Code plugin with two skills:

| Skill | What it does |
|---|---|
| `design-pass` | Understand a product's frontend, then audit it, propose directions, and build the agreed one. |
| `product-pass` | Keep the business side (personas, intended journeys, promises) and the product codebase (what it does today) telling the same story. |

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

Or call a skill directly:

```text
/brightnest:design-pass audit /settings
/brightnest:product-pass understand
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
