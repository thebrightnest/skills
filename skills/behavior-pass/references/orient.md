# Orient: which contract, how old, and where the loop lives in the code

Run this in Movement 0, every time. The review is only as current as the
contract it reads, and the contract moves.

---

## 1. Find the product contract

```bash
root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"; cd "$root"
find . -maxdepth 4 -name contract.json -not -path "*/node_modules/*" 2>/dev/null | head
find . -maxdepth 4 -name behavior.json -not -path "*/node_modules/*" 2>/dev/null | head
```

- **`behavior.json` exists:** read it. Its `contract` field says which
  contract this review reads. Use that one.
- **Only `contract.json` exists:** first run. Read it for `product`, `side`
  and `contract_dir`.
- **Several contracts:** ask which one, in one line.
- **None:** stop. Say there is no product contract and offer
  `/product-pass intake` on the business side or `/product-pass apply` on
  the app side.

## 2. Check what the contract holds

```bash
cd "<contract_dir>"
ls business/personas business/journeys app 2>/dev/null
grep -rh -A8 '^---' --include=*.md business app fit.md 2>/dev/null | grep -E '^(contract|as_of|updated):' | sort -u
```

| Present | What runs |
|---|---|
| `business/` and `app/` | Everything |
| `business/` only | `understand` only. Say the audit needs the actual journeys |
| `app/` only | Stop. Personas come from the business side |
| `staging/` but no `business/` | Stop. Staged candidates aren't confirmed. Offer `/product-pass intake` to walk them |

Read `fit.md` if it exists. Note each journey's verdict: rule 2 depends on it.
Read the contract's `decisions/README.md` so nothing already open, decided or
dismissed there is raised again here.

**Which half is a mirror.** On the app side, `business/` arrived by copy. On
the business side, `app/` did. Either way, label findings that rest on the
mirror `mirror as of <version>`. You can't see the other side's current state.

## 3. Find or create `behavior.json`

The review lives in its own folder, next to the contract:

| Contract side | Contract at | Review at (default) |
|---|---|---|
| app | `docs/product/` | `docs/behavior/` |
| business | `product-contract/` | `behavior/` |

Use the project's existing docs location if it has one. The schema is in
`templates.md`. On a first run, propose the location in one line and create
it only in a writing mode.

**Staleness.** Compare `built_from` in `behavior.json` with the contract's
current versions:

- the contract's `app.as_of` (per repo), `business.as_of` and `fit.updated`
  match: the review is current;
- any differ: the review is stale. Say which half moved, and rebuild the
  parts that rest on it. A persona that changed its Rhythm or Problem
  changes its habit hypothesis. A journey that changed changes its loop.

## 4. App side: find where the loop lives in the code

The snapshot says what a user can do. It rarely lists every notification,
badge or saved preference. On the app side, look for them directly, in every
`user` repo of the contract's `repos` map.

```bash
# triggers the product sends
grep -rniE "notif|push|reminder|digest|schedule|cron|mail(able|er)|send_?email|webhook|sms" \
  --include=*.{ts,tsx,js,py,php,rb,go} -l . | grep -vE "node_modules|vendor|test" | head -30
# rewards and progress shown
grep -rniE "streak|badge|points|level|progress|achievement|unread|count|feed|recommend" \
  --include=*.{ts,tsx,js,vue,svelte,py,php} -l . | grep -vE "node_modules|vendor|test" | head -30
# what the user stores (investment)
grep -rniE "saved|favorite|history|preference|template|follow|profile|settings" \
  --include=*.{ts,tsx,js,py,php} -l . | grep -vE "node_modules|vendor|test" | head -30
# analytics
grep -rniE "posthog|amplitude|mixpanel|segment|gtag|plausible|umami|track\(|capture\(" \
  --include=*.{ts,tsx,js,py,php,html} -l . | grep -vE "node_modules|vendor" | head -20
```

Read what you find. A match is a lead, not a trigger: confirm that a user
receives it, when, and whether they can turn it off. Record the analytics
tool and where events are defined in `behavior.json` `analytics`.

On the business side there is no code. Work from `app/` and label every phase
rating `from snapshot`.

## 5. Pick the target

The `now` persona with the strongest evidence, and its job with the highest
Rhythm. If the user named a persona, journey or hook, use that. Say which and
why in one line.

---

## Orientation summary

Write this before any other movement:

```text
Product:        <name>
Contract:       <contract_dir> (<side> side): business as of <v>, app as of <v>, fit <updated | missing>
Mirror:         <which half is a copy, and how old>
Review:         <behavior_dir>: <first run | current | stale: which half moved>
Personas:       <N now, N later>: <IDs with Rhythm and a "feel" | IDs missing them>
Fit:            <journeys served / partial / missing>
Code:           <triggers found, rewards found, investment found, analytics tool> | business side: from snapshot
Register:       <N open here>, <N open in the contract that touch habits>
Target:         <persona, job, journey, and why>
```

Carry it into every later movement. When something contradicts it, the
contradiction is a finding.
