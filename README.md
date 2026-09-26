# brightnest

A Claude Code plugin with two skills:

| Skill | What it does |
|---|---|
| `design-pass` | Understand a product's frontend, then audit it, propose directions, and build the agreed one. |
| `product-pass` | Keep the business side (personas, intended journeys, promises) and the product codebase (what it does today) telling the same story. |

## Install

```text
/plugin marketplace add thebrightnest/skills
/plugin install brightnest@thebrightnest
```

Invoke with `/brightnest:design-pass` or `/brightnest:product-pass`, or just
describe the task and Claude picks the skill.

Update with `/plugin marketplace update thebrightnest`.

## Develop locally

```bash
claude --plugin-dir /path/to/skills
```

See `AGENTS.md` for the repo rules and `CHANGELOG.md` for history.
