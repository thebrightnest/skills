# Templates: `<compliance_dir>/` layout and schemas

Keep this layout identical to `orient.md` and every reference file. Create only
the files owned by the current side and needed by the current mode.

---

## Directory Layout

```text
<compliance_dir>/              default: docs/compliance/
├── compliance.json            local to each repo (never copied)
├── README.md
├── app/                       owned by app side (copied to site side)
│   ├── data-flows.md
│   ├── subprocessors.md
│   ├── ai-systems.md
│   └── cookies-security.md
├── site/                      owned by site side (omitted on app side)
│   └── site-scan.md
├── business/                  owned by site / unified side
│   └── entity.md
├── review.md                  audit findings, drift, and Counsel Review Brief
├── documents/                 clean publishable markdown (no placeholders)
│   ├── privacy-policy.md
│   ├── terms-of-service.md
│   └── subprocessors.md
└── decisions/                 C-001.md ... + rebuilt README.md index
    ├── README.md
    └── C-001.md
```

---

## `compliance.json`

### On `app` side

```json
{
  "product": "<product name>",
  "side": "app",
  "compliance_dir": "docs/compliance",
  "contract": null,
  "jurisdictions": ["eu-gdpr", "eu-ai-act", "pt"],
  "customer_model": "b2b_and_consumers",
  "repos": {
    "<home>": { "home": true, "role": "<what this repo runs>" }
  },
  "flags": {
    "google_limited_use_required": false,
    "cookie_banner_exempt": true,
    "uses_ai_systems": true
  },
  "app": {
    "as_of": { "<home>": "<short-sha>" },
    "updated": "YYYY-MM-DD"
  }
}
```

### On `site` (or `unified`) side

```json
{
  "product": "<product name>",
  "side": "site",
  "compliance_dir": "docs/compliance",
  "jurisdictions": ["eu-gdpr", "eu-ai-act", "pt"],
  "customer_model": "b2b_and_consumers",
  "doc_languages": ["en"],
  "app_received": {
    "as_of": { "<app-repo>": "<short-sha>" },
    "received": "YYYY-MM-DD"
  },
  "site": {
    "as_of": "<short-sha>",
    "updated": "YYYY-MM-DD"
  },
  "entity_updated": "YYYY-MM-DD",
  "published_routes": {
    "privacy": "/privacy",
    "terms": "/terms",
    "subprocessors": "/subprocessors"
  }
}
```

---

## `app/*.md` Frontmatter

Every file in `app/` carries this frontmatter so `site` can detect newly copied
inventories automatically:

```markdown
---
compliance: app
file: data-flows          # data-flows | subprocessors | ai-systems | cookies-security
as_of: { <repo>: <short-sha> }
updated: YYYY-MM-DD
---
```

When `site` absorbs a copied `app/` folder, prepend one notice line below the
frontmatter:

```markdown
> Received from the app side at <repo>@<sha> on YYYY-MM-DD. Read-only here. Update via `/compliance-pass scan` in the product repo.
```

---

## `business/entity.md`

```markdown
---
compliance: business
file: entity
updated: YYYY-MM-DD
status: partial           # partial | confirmed
---

# Provider & Policy Baseline: <Product>

## Corporate Identity (Mandatory under GDPR Art. 13 & PT DL 7/2004)
- **Legal entity name (*Denominação social*):** unconfirmed (see C-001)
- **Legal form & Share capital (*Capital social*):** unconfirmed (see C-001)
- **Registered address (*Sede*):** unconfirmed (see C-001)
- **NIPC / EU VAT ID:** unconfirmed (see C-001)
- **Commercial registry (*Conservatória*):** unconfirmed (see C-001)
- **Privacy & legal contact email:** unconfirmed (see C-001)
- **DPO status:** Not required / Privacy contact handles inquiries

## Scope & Jurisdiction
- **Governing law:** Portuguese Republic
- **Business forum:** Courts of the Comarca de Lisboa, Portugal
- **Supervisory authority:** CNPD (Comissão Nacional de Proteção de Dados)
- **Customer model:** B2B primary, individual consumers permitted (`b2b_and_consumers`)
- **Minimum user age:** 18 years

## Retention & AI Policy Choices
- **Active account & workspace data:** Retained while account/workspace is active
- **Deprovisioned / deleted workspace grace window:** <from code or C-xxx>
- **Backup snapshot retention:** <days, from infra or C-xxx>
- **Billing & tax invoices:** 10 calendar years (Portuguese tax law)
- **Foundational AI model training on customer data:** Prohibited (neither provider nor upstream commercial API tiers train on workspace content)
```

---

## `documents/*.md` Frontmatter

```markdown
---
document: privacy-policy   # privacy-policy | terms-of-service | subprocessors
effective_date: YYYY-MM-DD
updated: YYYY-MM-DD
built_from:
  app_as_of: { <repo>: <short-sha> }
  site_as_of: <short-sha>
  entity_updated: YYYY-MM-DD
jurisdictions: [eu-gdpr, eu-ai-act, pt]
---
```

---

## `review.md`

```markdown
---
file: compliance-review
updated: YYYY-MM-DD
built_from:
  app_as_of: { <repo>: <short-sha> }
  site_as_of: <short-sha>
  entity_updated: YYYY-MM-DD
---

# Compliance Review: <Product>

> Automated compliance engineering analysis, not legal advice. Have qualified Portuguese/EU counsel review before relying on high-stakes clauses.

## Executive Summary
<3 to 5 sentences: Controller/Processor split, key regulatory obligations triggered, whether cookie consent banner is exempt, blocking items.>

## Commit Drift Since Last Document Build
| Surface | Previous SHA | Current SHA | Compliance Triggers Changed | Docs Affected |
|---|---|---|---|---|

## Audit Findings
| # | Severity | Framework | Gap or Risk | Evidence | Resolution / Item |
|---|---|---|---|---|---|

## Statutory Checklist Summary
| Framework | Status | Notes |
|---|---|---|

## Counsel Review Brief
| Clause | Document | Code / Fact Grounding | Question for Legal Counsel |
|---|---|---|---|
```
