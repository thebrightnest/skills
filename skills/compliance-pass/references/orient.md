# Orient: side, commits, received copies, and compliance drift

Run this in Movement 0 on every invocation. Compliance reviews rot whenever a
migration, SDK, OAuth scope, or AI model lands without updating the legal pages.

---

## 1. Find `compliance.json` and optional `contract.json`

```bash
root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"; cd "$root"
find . -maxdepth 4 -name compliance.json -not -path "*/node_modules/*" 2>/dev/null | head
find . -maxdepth 4 -name contract.json -not -path "*/node_modules/*" 2>/dev/null | head
```

- **`compliance.json` exists:** read it. Its `side` (`app`, `site`, or
  `unified`), `compliance_dir`, `jurisdictions`, and `customer_model` govern.
- **No `compliance.json`, `contract.json` exists:** read `contract.json`
  read-only. Reuse its `product` name and `repos` map if its `side` is `app`. If
  its `side` is `business` inside a website repo, propose `side: "site"`.
- **Neither exists (first run):** detect the side and confirm in one line:
  - **app:** backend/product manifests (`composer.json`, `pyproject.toml`,
    `go.mod`, `Cargo.toml`, or full-stack app routes/controllers/migrations)
    plus a sibling `-website` repo or separate marketing site.
  - **site:** static/content/marketing site repo (Astro, Next, Eleventy, Hugo)
    with landing copy, pricing, and public marketing pages.
  - **unified:** one repo serves both the product application and public
    marketing/legal pages.

On the `app` side, map all product repos (`home: true` for this repo, `path` for
sibling product repos that run the application or infrastructure, never the
marketing website repo). Default `compliance_dir` is `docs/compliance`. Create
files only in writing modes (`scan`, `audit` on site/unified, `decide`, `draft`,
`publish`).

## 2. Check received copies and `decisions.incoming/`

Between `app` and `site`, files move by manual copy:

- **From `app` to `site`:** `app/` folder and `decisions/` (copied as
  `decisions.incoming/`).
- **From `site` to `app`:** `decisions/` (copied as `decisions.incoming/`) when
  a technical decision needs product input.

On `site`, inspect `app/*.md` frontmatter (`as_of`, `updated`):

- **Newer than `compliance.json` `app_received`:** a fresh `app/` inventory
  arrived. Note what moved and absorb it on the next write.
- **Same as recorded:** report `app inventory as of <repo@sha>, received <date>`.
- **Missing:** `site` can still scan `site/` and walk `business/entity.md`
  decisions, but `draft` cannot complete until `app/` arrives (unless the
  website is standalone with no product backend).

**Overwrite guard.** If `app` finds its own `app/*.md` stamped with `mirrored:
true`, or `site` finds `business/entity.md` overwritten, stop and ask the user
to restore from git.

If `decisions.incoming/` exists, merge it into `decisions/` (`decisions.md`) and
remove `decisions.incoming/`.

## 3. Compute git commit drift on compliance-sensitive paths

Never re-read an entire unchanged monorepo when `as_of` exists. For each repo in
`repos` (on `app`/`unified`) or the website repo itself (`site.as_of` on
`site`/`unified`):

```bash
repo_path=<"." or expanded sibling path>
last_sha=<recorded sha>
current_sha=$(git -C "$repo_path" rev-parse --short HEAD)
git -C "$repo_path" log --oneline "$last_sha"..HEAD | wc -l
git -C "$repo_path" diff --name-status "$last_sha"..HEAD
```

Group changed files into six **compliance triggers**:

| Trigger | Paths / Patterns | Legal Docs Affected |
|---|---|---|
| **1. Schema & PII** | `migrations/`, `drizzle/`, `prisma/`, `models/`, `schema.*` | Privacy Policy (data collected, retention) |
| **2. Subprocessors & SDKs** | `composer.json`, `package.json`, `pyproject.toml`, `requirements*.txt`, `.env.example`, `config/services*`, `config/mail*`, `config/sentry*` | Privacy Policy, Subprocessors list, international transfers |
| **3. Auth, OAuth & Connectors** | `Auth/`, `OAuth`, `Socialite`, `sso`, `Connector`, token brokers, scopes | Privacy Policy (third-party data, Google Limited Use), ToS (account security) |
| **4. AI Models & Agents** | `AiProvider`, `AiModel`, LLM clients, system prompts, cron/routines, image/audio generators, MCP tools | Privacy Policy (AI processing/training), ToS & AI Act Art. 50 transparency |
| **5. Billing & Plans** | `Stripe`, `Cashier`, `Plan`, `Checkout`, `Subscription`, quotas, usage boosts | ToS (pricing, renewal, boost/refund rules, consumer withdrawal) |
| **6. Cookies, Sharing & Lifecycle** | `session.*`, cookie setters, `localStorage`, analytics scripts, public share routes, deletion/deprovision jobs, infrastructure regions | Privacy Policy (cookies, transfers, retention, security), ToS (acceptable use, termination) |

If 0 compliance-trigger files changed since `last_sha`, report `current at
<current_sha>` and skip re-scanning code.

## 4. Check document freshness (`site` and `unified`)

Read frontmatter of `documents/privacy-policy.md`,
`documents/terms-of-service.md`, and `documents/subprocessors.md` if they exist.
Compare their `built_from` (`app_as_of`, `site_as_of`, `entity_updated`) against
current `app/`, `site/`, and `business/entity.md`. Any mismatch marks that
document `stale` with the specific trigger(s) that moved.

---

## Handoff instructions (end of writing runs on `app` or `site`)

On `app`, end `scan` with exact copy instructions:

```text
Handoff to the marketing website repo (<compliance_dir>/):
  1. Replace <compliance_dir>/app/ with this repo's docs/compliance/app/
  2. If decisions/ changed, copy docs/compliance/decisions/ to <compliance_dir>/decisions.incoming/
```

`compliance.json` never travels. Each repo keeps its own `compliance.json`.

---

## Orientation summary

Print this block before moving past Movement 0:

```text
Product:         <name>
Side:            app | site | unified (<compliance_dir>)
Jurisdictions:   <e.g. eu-gdpr, eu-ai-act, pt>
Customer model:  <b2b_only | b2b_and_consumers | unconfirmed>
App inventory:   <repo@sha (current | N commits behind HEAD: triggers ...) | received <date> | missing>
Site inventory:  <sha (current | N commits behind HEAD) | n/a on app side>
Entity & policy: <confirmed YYYY-MM-DD | N mandatory fields unconfirmed>
Documents:       <privacy: current/stale/missing | terms: current/stale/missing | subprocessors: current/stale/missing>
Decisions:       <N open (N blocking draft)>, <N noticed>
Target:          <what this run will do next>
```
