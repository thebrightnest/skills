# Templates: creating the contract for the first time

Use these only in `apply` (app side) or `intake` (business side), when a file
doesn't exist yet. Create only your own half, plus `contract.json`,
`README.md` and `fit.md`. The other half arrives by copy (see `orient.md`
step 2).

## Layout (identical on both sides)

```text
<contract_dir>/
├── contract.json    per side, never copied across
├── README.md
├── business/        owned on the business side, received by copy on the app side
│   ├── personas.md
│   ├── journeys.md
│   └── promises.md
├── app/             owned on the app side, received by copy on the business side
│   ├── capabilities.md
│   ├── journeys.md
│   ├── boundaries.md
│   ├── grounding.md     (unless contract.json app_files drops it)
│   └── glossary.md
├── fit.md           how well the product serves the business today
└── decisions.md     everything still to clarify or decide (shared by both sides)
```

## contract.json

See `orient.md` step 1. On creation, fill `product`, `side`, `contract_dir`,
and on the app side `repos`, `app_files` and `run`. Fill the version fields on
the first `apply` or `intake`. On the business side, `repos`, `app_files` and
`run` are left out.

## README.md

```markdown
# Product contract: <product>

This folder is the contract between the business side and the product.

- **business/**: who we serve, how their journey should go, what we say publicly. Owned by the business side.
- **app/**: what the product does **today**, in present tense. Owned by the app side. Nothing planned appears here.
- **fit.md**: whether the product serves the business, with evidence and ranked gaps.
- **decisions.md**: everything still to clarify or decide. Shared by both sides.

The product is built from these repos (cited as `<key>:<path>`):

| Key | Repo | Surface | Role |
|---|---|---|---|
| <key> | <home repo> (this one) | user | … |
| <key> | <repo> | operator | … |

Each side owns one half and receives the other by copy, read-only. Edit a half
only on the side that owns it. Maintained with `/product-pass`.

| Half | As of | Updated |
|---|---|---|
| app | <key>@<sha> · <key>@<sha> | YYYY-MM-DD |
| business | <sha/date> | YYYY-MM-DD |
| fit | app as above + business <sha/date> | YYYY-MM-DD |
```

The repo table is app-side knowledge. The business side copies it as it
arrives and never edits it.

## Owned file frontmatter

```yaml
---
contract: app            # or business
file: capabilities       # personas | journeys | promises | capabilities | boundaries | grounding | glossary
as_of:                   # app side: one sha per repo that feeds this file
  <repo>: <sha>
updated: YYYY-MM-DD
sources:                 # app side: repo-qualified code/doc paths that feed this file
  - <repo>:<path>/       # business side: the materials it was built from (plain paths)
---
```

On the business side `as_of` is a single sha or date.

## Mirrored file header

Placed directly under the frontmatter of every file received from the other
side:

```text
> Received from the <side> side at <version> on <date>. Read-only here. Edit at the source.
```

## Section skeletons

- `personas.md`: see `business-inputs.md` (minimum per persona, evidence log).
- `journeys.md` (either side): see `journeys.md` (intended and actual formats).
- `promises.md`: the table in `business-inputs.md`.
- `capabilities.md`, `boundaries.md`, `grounding.md`, `glossary.md`: see
  `app-snapshot.md`.
- `fit.md`: see `fit.md`, "Write fit.md".
- `decisions.md`: see `decisions.md`, "Layout".
