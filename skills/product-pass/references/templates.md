# Templates: creating the contract for the first time

Use these only in `apply` (app side) or `intake` (business side), when a file
doesn't exist yet. Create only your own half, plus `contract.json`,
`README.md`, `fit.md` and `decisions/`, and on the business side `staging/`.
The other half arrives by copy (see `orient.md`
step 2).

## Layout (identical on both sides, except `staging/`)

```text
<contract_dir>/
├── contract.json    per side, never copied across
├── README.md
├── business/        owned on the business side, received by copy on the app side
│   ├── personas/
│   │   ├── README.md    at a glance, triggers → jobs, evidence log
│   │   └── C1.md        one confirmed persona per file
│   ├── journeys/
│   │   └── C1.md        that persona's intended journeys
│   └── promises.md      promises and positioning
├── app/             owned on the app side, received by copy on the business side
│   ├── capabilities.md
│   ├── journeys.md
│   ├── boundaries.md
│   ├── grounding.md     (unless contract.json app_files drops it)
│   └── glossary.md
├── fit.md           how well the product serves the business today
├── decisions/       choices still to make, one file per item (shared by both sides)
│   ├── README.md        index and Noticed, rebuilt on every write
│   └── D-001.md
└── staging/         business side only, never copied
    ├── README.md        the walk queue
    ├── SOURCES.md       where every source section went
    └── <candidate>.md   one candidate definition each
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
- **decisions/**: the choices still to make, one file per item, with an index. Shared by both sides.
- **staging/** (business side only): harvested material not yet confirmed, and the walk queue. Never copied.

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
file: capabilities       # persona | personas-index | journeys | promises | capabilities | boundaries | grounding | glossary
as_of:                   # app side: one sha per repo that feeds this file
  <repo>: <sha>
updated: YYYY-MM-DD
sources:                 # app side: repo-qualified code/doc paths that feed this file
  - <repo>:<path>/       # business side: the materials it was built from (plain paths)
---
```

On the business side `as_of` is a single sha or date. A persona file also
carries `id` and `confirmed: YYYY-MM-DD · <who>` (`business-inputs.md`).
Files in `staging/` carry no contract frontmatter. They aren't part of the
contract.

## Mirrored file header

Placed directly under the frontmatter of every file received from the other
side:

```text
> Received from the <side> side at <version> on <date>. Read-only here. Edit at the source.
```

## Section skeletons

- `business/personas/`: see `business-inputs.md` (persona shape, README sections).
- `business/journeys/<persona>.md` and `app/journeys.md`: see `journeys.md` (intended and actual formats).
- `business/promises.md`: see `business-inputs.md`, "Promise template".
- `staging/README.md`, `staging/SOURCES.md`, candidates: see `business-inputs.md`, intake steps 3–5.
- `capabilities.md`, `boundaries.md`, `grounding.md`, `glossary.md`: see
  `app-snapshot.md`.
- `fit.md`: see `fit.md`, "Write fit.md".
- `decisions/`: see `decisions.md`, "Item format" and "The index".
