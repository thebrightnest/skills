# Orient: which side, which repos, which versions, which document governs

Run this in Movement 0, every time. It takes a few minutes. It is the difference
between reviewing the contract as it is and reviewing one you remembered.

---

## 1. Find the contract

```bash
root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"; cd "$root"
find . -maxdepth 4 -name contract.json -not -path "*/node_modules/*" 2>/dev/null | head
```

If `contract.json` exists, read it. **Its `side` is final.** Don't second-guess
it with detection. A business half can live in a website repo with a
`package.json`, and an app contract can live in a repo that's mostly docs.

```json
{
  "product": "<product name>",
  "side": "app",
  "contract_dir": "docs/product",
  "repos": {
    "<home>":   { "home": true,              "surface": "user",     "role": "<what this repo is to a user, one line>" },
    "<name>":   { "path": "~/Sites/<repo>",   "surface": "user",     "role": "…" },
    "<name>":   { "path": "~/Sites/<repo>",   "surface": "operator", "role": "…" }
  },
  "app_files": ["capabilities", "journeys", "boundaries", "grounding", "glossary"],
  "run": { "<repo>": "<dev command> (:<port>, auth: <yes|no>)" },
  "app":      { "as_of": { "<repo>": "<commit sha>" }, "updated": "YYYY-MM-DD" },
  "business": { "as_of": "<sha or YYYY-MM-DD>", "received": "YYYY-MM-DD" },
  "fit":      { "app_as_of": { "<repo>": "<sha>" }, "business_as_of": "<sha|date>", "updated": "YYYY-MM-DD" }
}
```

Fields:

- **`repos`** (app side only): every code repo the product is made of. A
  product is often several repos: a user-facing app, an account/identity
  service, an API, an infrastructure or deploy repo. The repo holding the
  contract is `home: true` and has no path. The others have a `path`. A
  single-repo product has one entry. The key (`cloud`, `api`, `web`) is
  the **repo prefix** used in every source and evidence citation.
- **`surface`:** who meets that repo's behaviour.
  - `user`: people who use the product reach it directly (screens, API, MCP,
    emails, exports). It feeds `capabilities` and `journeys`.
  - `operator` / `internal`: it runs the product but nobody uses it directly
    (provisioning, deploys, isolation, billing jobs). It feeds only
    `boundaries` and `grounding`. What it guarantees ("each customer runs in an
    isolated container", "credentials never leave the vault") is what trust
    claims in marketing rest on. What it merely *does* (render configs, rotate
    certs) is implementation and stays out of the contract.
- **`app_files`:** which `app/` files this product keeps. `capabilities`,
  `journeys`, `boundaries` and `glossary` are always kept. `grounding` is
  kept whenever a customer has to *trust* something they can't inspect, which
  covers almost every product. Drop it only when you and the user agree there's
  nothing to say.
- **`run`:** how to start each `user` repo locally (see step 6).
- **`app.as_of`:** one commit per repo. That is the version the `app/` half
  was built from.
- **`business.as_of` / `received`** on the app side, **`app.as_of` /
  `received`** on the business side: the version of the other half you hold
  and the day it arrived.

The contract never records where the other side lives. The halves travel by
**copy** (step 2).

### First run: no `contract.json` yet

**Detect the side**, then confirm it with the user in the same message as the
repo map:

- **app:** a build manifest (`package.json`, `composer.json`, `pyproject.toml`,
  `go.mod`, …) plus source directories with routes, handlers or screens.
- **business:** mostly prose (`.md`, `.pdf`, decks) with folders like
  `strategy/`, `sales/`, `marketing/`, `fundraising/`, `knowledge/`.
- **Ambiguous: a website or marketing repo** (Astro, Next, Hugo, Eleventy,
  with `content/`, `src/pages/` or `src/content/` full of marketing copy). It
  has a build manifest but it's where **promises** are made. Treat it as a
  business-side candidate and ask.

**On the app side, map the repos.** The home repo is rarely the whole product.
Look for its siblings before writing anything:

```bash
name=$(basename "$root"); parent=$(dirname "$root")
ls -d "$parent/$name"-* "$parent"/*-"$name" 2>/dev/null
# how the repo describes its layers or siblings
grep -niE "repo|layer|control plane|data plane|service|monorepo|packages/" \
  README.md AGENTS.md CLAUDE.md ARCHITECTURE.md docs/*.md 2>/dev/null | head -30
ls packages apps services 2>/dev/null   # monorepo: one repo, several surfaces
```

Read the README and AGENTS/CLAUDE files of each candidate. Many multi-repo
products state their split in one table ("control plane / data plane / fleet").
Propose the `repos` map in **one message**: the key, path, surface and role for
each repo, plus the side and the `contract_dir`. Let the user correct it in a
sentence. A monorepo stays one repo. Its packages are just paths inside it.

Default `contract_dir` is `docs/product/` on the app side and
`product-contract/` on the business side, unless the project already keeps its
docs elsewhere. Create the files from `references/templates.md` only in `apply`
or `intake`.

## 2. Receive the other half (it arrives by copy)

The user moves the contract between sides by copying files. At the end of
`apply` or `intake` you tell them exactly what to copy (see "Handoff" below).
When you start, find out what arrived.

**Read the other half's version from its own files.** Every owned file carries
`contract`, `as_of` and `updated` in its frontmatter. The copy describes itself.

```bash
cd "<contract_dir>"
other=business   # or app, on the business side
grep -h -A8 '^---' "$other"/*.md 2>/dev/null | grep -E '^(contract|as_of|updated):' | sort -u
grep -h -A8 '^---' app/*.md business/*.md 2>/dev/null | grep -E '^(contract|as_of):' | sort | uniq -c
```

Compare with what `contract.json` says you hold:

- **Newer than recorded:** a new copy arrived. Say "received the <side> half as
  of <version>, not yet absorbed". In `audit`, review against it. In `apply`,
  record it in `contract.json` (`as_of`, `received`), add the mirrored header
  where it's missing, and rebuild what depends on it (`fit.md`).
- **Same as recorded:** the mirror is what it was. Say "mirror as of
  <version>, received <date>". Label every fit finding `mirror as of
  <version>`. **You can't see the other side's current state. Never claim the
  mirror is current**, only how old it is. If it's more than a few weeks old, a
  `validate` item asking for a fresh copy is worth adding.
- **Missing:** the other side has no contract yet, or it was never copied. On
  the business side, `intake` can start one. On the app side, fit review needs
  `business/`. Offer to draft personas from existing materials, marked
  Unconfirmed (see `business-inputs.md`).

**Overwrite guard.** Copying a whole folder can clobber *your own* half with an
older version. If your half's frontmatter `as_of` is older than what
`contract.json` records for it (or its `contract:` field names the other side
while sitting in your half), **stop**. Say what happened and ask the user to
restore it from git before doing anything else. Never "fix" it by merging.

Mirrored files carry a header. Never edit below it:

```text
> Received from the <side> side at <version> on <date>. Read-only here. Edit at the source.
```

### Handoff (end of `apply` and `intake`)

Tell the user exactly what to copy and where it lands:

```text
Copy to the <other side>'s <contract_dir>/:
  <my half>/            → replaces their mirror
  fit.md               → replaces theirs
  decisions.md         → save as decisions.incoming.md (they merge it)
```

`contract.json` never travels. Each side keeps its own.

## 3. App side: what changed since the snapshot, per repo

Every `sources` entry and every evidence citation is qualified with its repo
key: `<repo>:<path>[:<line>]`. For each repo in `repos`:

```bash
repo_path=<"." for home, else the expanded path>
as_of=<app.as_of[repo]>
git -C "$repo_path" rev-parse --verify -q "$as_of^{commit}" >/dev/null || echo "UNKNOWN SHA"
git -C "$repo_path" log --oneline "$as_of"..HEAD | wc -l
# the sources of each app/ file that belong to this repo, prefix stripped
git -C "$repo_path" diff --stat "$as_of"..HEAD -- <paths>
```

Map each changed path back to the `app/` file(s) whose `sources` cite
`<repo>:<that path>`. That's the staleness worklist, one line per repo:

```text
web:      23 commits, capabilities + journeys stale
identity: 4 commits, boundaries stale
infra:    0 commits
```

A file whose sources didn't change isn't reviewed for staleness this run.

Also list **changed paths no file cites** in `user`-surface repos when they
touch routes, screens, public API or user-facing copy. That's where new
capabilities appear unnoticed. An `operator` repo only matters when a change
touches what it guarantees (isolation, secrets, data location, limits).

- **Repo unreachable** (path missing, another machine): say so, keep its part
  of the snapshot as it is, and label it `<repo> snapshot as of <sha>, not
  checked`.
- **Repo not in `as_of`** (newly added): everything in it is new for this run.
- **First run:** everything is new. Build the source map in
  `app-snapshot.md` before writing anything.

## 4. Business side: what changed since the last intake or fit

```bash
git log --since="<business.as_of or fit.updated>" --name-only --format='' -- . | sort -u | head -40
# not a git repo: find files newer than the contract
find . -newer "<contract_dir>/contract.json" -type f -not -path "*/node_modules/*" -not -path "*/<contract_dir>/*" | head -40
```

New decks, positioning docs, meeting notes, studies, **and site pages** can all
change personas or promises without anyone touching `business/`. If the
business side lives in a website repo, a changed page is a changed promise.
List them as **unabsorbed material**. They're candidates for `intake`, not
automatic edits.

## 4b. Merge the decisions register

If `decisions.incoming.md` exists, merge it into `decisions.md` by ID (rules in
`decisions.md`), then delete it. Every later movement checks the merged
register before raising anything, so findings already open, decided or
dismissed aren't raised twice. A dismissed finding stays dismissed unless the
evidence changed.

## 5. Decide which document governs

**This is the step that goes wrong.** A strategy folder easily holds several
persona lists: last quarter's roster, an investor-deck version, a JTBD study,
a sales deck. A repo easily holds PRDs for features that were never built,
product docs that lag the code, and plans that were abandoned. A multi-repo
product multiplies this. Each repo has its own README, PRODUCT.md and
roadmap, and they drift apart. Docs in one repo often describe the others as
they were months ago.

For each candidate source, ask:

1. **What does it describe?** Today's product, an intended product, a pitch,
   or a study? Which repo or layer?
2. **Is it confirmed by the thing it describes?** For product claims, does the
   code or the running app do it, in the repo that owns it? For persona claims,
   does it cite real evidence (a customer, an interview, an inbound request)?
3. **When did it last change relative to its subject?**
   `git -C <repo> log -1 --format=%ci -- <doc>` against the code it describes
   (which may be in another repo) or the newest material.

Write the table before reviewing anything:

| Source | Describes | Confirmed by | Authority here |
|---|---|---|---|

Standing order of authority:

- **About what exists:** running app > code (in the repo that owns the
  behaviour) > `app/` > product docs > PRDs and plans (never)
- **About which repo owns what:** an explicit boundaries/ownership doc that
  the code agrees with > READMEs > inference from the code
- **About who we serve and why:** `business/` > the newest dated study or
  positioning doc > decks > older rosters

If two sources disagree and neither clearly wins, that is a finding. Report
it; don't pick a side silently.

**Governing settles conflicts. It doesn't decide what's kept.** When several
sources describe the same personas (three analyses of one founder
conversation, a study and a deck), the governing one wins where they
disagree. Everything else they say that doesn't conflict is harvested
(`business-inputs.md` step 2). Ruling a source "not governing" never means
ignoring it.

## 6. App side: how to run it

For each `user` repo, record the dev command, the port, and whether it needs
auth, in `contract.json` `run`. You need these to **walk** a journey (see
`journeys.md`). A journey that crosses repos (sign in on one service, land in
another) needs all of them up, plus whatever connects them locally (a shared
docker-compose, a local stack script). Look for it before starting services
one by one. Ask before starting any server. Never read credentials out of
`.env`.

```bash
sed -n '/"scripts"/,/}/p' package.json 2>/dev/null
ls Makefile justfile Procfile docker-compose*.yml 2>/dev/null
grep -nE "^[a-z-]+:" Makefile 2>/dev/null | head -20
grep -rliE "local.?dev|local stack|getting started" docs README.md 2>/dev/null | head
```

---

## Orientation summary

Write this before any other movement:

```text
Product:         <name>
Side:            app | business: <repo or folder>
Contract:        <contract_dir>: <exists | first run>
Repos:           <key>@<short sha>: <N commits since, files stale | unreachable>   (one line each, app side)
My half:         as of <version>: <N changes since | unabsorbed material: …>
Other half:      <received <version> on <date>: newly arrived | unchanged | missing>
Fit:             built from app <versions> + business <v>: <current | stale>
Decisions:       <N open (by kind)>, incoming merged: <yes | none>
Governing docs:  <which, and which were ruled out and why>
Run:             <per repo: command, port, auth?> (app side)
Target:          <what this run will focus on, and why>
```

Carry it into every later movement. When something contradicts it, the
contradiction is a finding.
