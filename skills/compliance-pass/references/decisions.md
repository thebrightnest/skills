# Decisions: legal, entity, and compliance choices (`C-` items)

`<compliance_dir>/decisions/` holds one file per unsettled compliance fact or
policy choice. Code tells us what tables, cookies, and APIs exist; only the user
(or their counsel) can confirm corporate registration details, retention policy
targets, and commercial risk choices.

---

## What becomes a `C-` item

| Becomes an item | Kind | Blocking `draft`? |
|---|---|---|
| Missing statutory corporate identity (legal name, registered address, NIPC/VAT ID, share capital, contact email) | `clarify` | **Yes** |
| Unconfirmed `customer_model` (`b2b_only` vs `b2b_and_consumers`) or `jurisdictions` | `decide` | **Yes** |
| Policy retention periods not fixed by code (for example how long inactive accounts, logs, or backups are kept) | `decide` | **Yes** (or explicit rule confirmed) |
| Upstream AI provider data-retention / zero-training verification (for example OpenRouter routing or custom endpoints) | `validate` | **Yes** if unqualified zero-training is claimed |
| Checkout flow mechanics vs legal text (for example express consumer consent checkbox for instant digital boosts, or *Livro de Reclamações* footer link) | `decide` | No (noted in `review.md` until wired) |
| Non-essential cookies or remote Google Fonts found without consent | `decide` | No (flagged `high` in `review.md`) |

**At most five new items per run**, highest weight first (`blocking` > `high` >
`medium`). Anything lower goes under `Noticed` in `decisions/README.md`.

---

## Layout & Item Format

```text
decisions/
├── README.md     rebuilt on every write
├── C-001.md
└── ...
```

Use `C-` IDs (`C-001`, `C-002`) so items never collide with `product-pass`
(`D-`) or `behavior-pass` (`B-`). Never rename or delete an item file.

```markdown
---
id: C-001
kind: clarify             # clarify | decide | validate
status: open              # open | decided | parked | dismissed
weight: blocking          # blocking | high | medium | low
who: business             # business | product | counsel
raised: YYYY-MM-DD · scan of app@<sha>
status_changed: YYYY-MM-DD
touches: entity.md · terms-of-service.md · privacy-policy.md
---

# C-001: What are the registered Portuguese corporate details for the provider?

**Question.** Confirm the legal company name (*denominação social*), registered
Lisbon address (*sede*), NIPC / VAT number, share capital (*capital social*),
commercial registry (*Conservatória*), and privacy/legal contact email.

**Context.** Portuguese *DL n.º 7/2004* (Art. 10.º), *CSC* (Art. 171.º), and
GDPR Art. 13(1)(a) require these disclosures on public legal pages. None are
present in the codebase.

**Options / Defaults.**
1. Supply confirmed corporate details now (enables clean `draft` and `publish`).
2. Pre-incorporation / sole trader (*Empresário em Nome Individual*): disclose
   the individual operator's legal name, business address, NIF, and contact
   email (omitting *capital social*).
```

When answered in `decide`, set `status: decided`, update `status_changed`,
append `**Decision.**` and `**Consequence.**`, and immediately write the
confirmed values into `business/entity.md` so `draft` reads one clean source.

---

## Merging `decisions.incoming/`

When `decisions.incoming/` is present in Movement 0:
- New `C-` IDs not in local `decisions/` are copied in.
- Existing `C-` IDs where incoming `status_changed` is newer (or moves `open` ->
  `decided`) replace the local file.
- Rebuild `decisions/README.md` and delete `decisions.incoming/`.
