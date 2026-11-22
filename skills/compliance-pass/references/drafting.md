# Drafting & Publishing Legal Pages

Read this in Movement 4 (`draft`) and Movement 5 (`publish`).

---

## 1. Core Drafting Principles

1. **Plain language, high specificity (GDPR Art. 12(1)).**
   Write for a thoughtful customer, not a courtroom. Replace vague filler ("we
   may use information to improve user experience") with concrete statements
   grounded in `app/` and `site/` ("we record daily token counts and workspace
   quotas so workspace owners can monitor their weekly AI allowance").
2. **Layered "At a Glance" summary at the top.**
   Open both the Privacy Policy and Terms of Service with a 4-to-6 bullet
   **Summary at a Glance** box stating clearly what the document covers, how
   workspace data and AI prompts are handled, what is never done (no selling
   data, no training foundational AI models on customer workspaces), and how to
   reach the company. State in one line that the full sections below govern.
3. **Zero inline warnings or placeholders in `documents/`.**
   Never write `[TBD]`, `[COMPANY NAME]`, or `[⚠️ LEGAL REVIEW REQUIRED]` inside
   `documents/*.md` or live HTML. If a mandatory `business/entity.md` field is
   missing, stop and run `decide`. Put every lawyer sign-off note in `review.md`
   under **Counsel Review Brief**.
4. **Language choice.**
   Check `compliance.json` `doc_languages` (default `["en"]`). Note in
   `review.md` when serving Portuguese consumers (`pt` + `b2b_and_consumers`)
   whether the website operates in English or also offers Portuguese (`pt-PT`),
   since Portuguese consumer rules favor clear pre-contractual information in a
   language matching how the service is marketed to Portuguese consumers.

---

## 2. Standard Structure: `documents/privacy-policy.md`

1. **Header & At a Glance** (Effective date, Last updated, Summary bullets)
2. **1. Who We Are & Our Role (Controller vs. Processor)** (Full corporate
   identity from `business/entity.md`, Controller scope vs B2B Processor scope)
3. **2. Personal Data We Collect** (Grouped clearly: Account & Identity,
   Billing, Workspace & Project Data, Optional Third-Party Connectors, Technical
   & Usage Telemetry, Website Inquiries)
4. **3. How We Use Personal Data & Legal Bases (GDPR Art. 6)** (Markdown table:
   Purpose | Data Categories | GDPR Legal Basis)
5. **4. AI Systems, Model Providers & Training Policy (EU AI Act Art. 50)**
   (How prompts/files flow to enabled models, no foundational model training,
   human oversight)
6. **5. Google Workspace & Third-Party Connectors (Limited Use)** *(Include
   whenever OAuth connectors exist; mandatory Google Limited Use wording when
   `google_limited_use_required` is true)*
7. **6. Subprocessors & International Data Transfers** (Summary table of core
   subprocessors + link/reference to `subprocessors.md`, EU hosting vs EEA-to-US
   DPF/SCC safeguards)
8. **7. Cookies & Browser Storage** (Exact cookies and `localStorage` keys from
   `cookies-security.md` and `site-scan.md`, stating strictly-necessary status
   or consent controls)
9. **8. Data Retention & Deletion** (Concrete rules per bucket: active account,
   soft-delete grace window, backup rotation, statutory 10-year tax invoice
   retention)
10. **9. Security Measures** (Encryption in transit, encrypted token vaults,
    password hashing, isolated workspaces, access controls)
11. **10. Your Privacy Rights & Supervisory Authority** (GDPR Art. 15-22 rights,
    1-month response SLA, B2B Processor redirection note, CNPD / EEA supervisory
    authority details, PT *Lei n.º 58/2019* post-mortem rights)
12. **11. Minimum Age** (18+ contracting threshold)
13. **12. Changes to This Policy & Contact** (Advance notice for material
    changes, contact email and postal address)

---

## 3. Standard Structure: `documents/terms-of-service.md`

1. **Header & At a Glance** (Effective date, Last updated, Summary bullets)
2. **1. Provider Identification & Scope** (Full statutory entity disclosures,
   who may contract, B2B primary + Consumer Provisions pointer if applicable)
3. **2. Accounts, Workspaces & Security** (Registration, SSO/Google Sign-In,
   owner vs member roles, credential confidentiality)
4. **3. Subscriptions, Plans, Usage Allowances & Billing** (Plans, Stripe
   VAT-inclusive billing, seat billing, fair-use AI allowances, one-off usage
   boosts, renewal, cancellation, price/plan change 30-day notice)
5. **4. Customer Content, Intellectual Property & Public Sharing** (Customer
   owns Inputs and Workspace Content; license strictly to host/operate; platform
   IP & protected skills remain company IP; customer responsibility for revocable
   public share links)
6. **5. AI Features, Transparency & Human Oversight (EU AI Act)** (Probabilistic
   outputs, no regulated professional advice, human oversight over autonomous
   tasks/routines/connected channels, input/output rights, Art. 50 provenance)
7. **6. Acceptable Use & Prohibited AI Practices** (Security boundaries, no
   abuse/reverse engineering, no EU AI Act Art. 5 prohibited uses or unassessed
   Annex III high-risk automated decisions)
8. **7. Third-Party Connectors & Messaging Channels** (Customer authorization
   for Google, Slack, Telegram, etc.; third-party terms; revoking access)
9. **8. Data Protection & Processor Commitments (B2B, GDPR Art. 28)** (Summary
   processor commitments for business workspaces, subprocessor authorization,
   availability of standalone DPA on request)
10. **9. Service Availability, Suspension & Termination** (Maintenance,
    suspension for non-payment or severe security breach, self-service
    cancellation, workspace soft-delete grace window and data export)
11. **10. Warranties & Limitation of Liability** (As-is commercial disclaimer
    for B2B subject to mandatory law, liability cap at 12 months' fees, explicit
    statutory carve-out for *dolo*, *culpa grave*, and personal injury under
    Portuguese *Art. 809.º Código Civil*)
12. **11. Consumer Provisions (*Disposições Aplicáveis a Consumidores*)** *(Include
    when `customer_model` is `b2b_and_consumers`: 14-day withdrawal under DL
    24/2014 + digital service/boost rules, DL 84/2021 conformity, CACCL/CNIACC
    RAL arbitration under Lei 144/2015, Livro de Reclamações Eletrónico,
    non-waiver of consumer domicile courts)*
13. **12. Changes to Terms, Governing Law & Jurisdiction** (30-day notice with
    right to cancel, Portuguese law, *Comarca de Lisboa* for Business Customers)

---

## 4. Counsel Review Brief (inside `review.md`)

Every `draft` or `audit` run maintains a dedicated section in `review.md` titled
`## Counsel Review Brief` listing the 5 to 8 clauses a qualified lawyer in the
target jurisdiction should verify first:
- Exact clause reference in `documents/*.md`
- Underlying code fact (`<repo>:<path>:<line>`)
- Statutory question (for example: verifying vendor DPF/SCC coverage for active
  LLM providers, confirming Stripe Checkout consent wording if immediate boost
  waivers are desired under *Art. 17.º DL 24/2014*, confirming whether a
  Portuguese translation of ToS/Privacy is required alongside English).

---

## 5. Publishing to the Website (Movement 5: `publish`)

Before creating or editing website files:
1. Inspect the website repo's framework (`astro.config.*`, `next.config.*`,
   `package.json`), existing layouts (`src/layouts/`, `src/components/`), footer
   links, and design tokens (`DESIGN.md`, global CSS).
2. Prefer rendering directly from clean Markdown/MDX collections or shared
   legal layout templates so future `draft` updates do not require hand-editing
   duplicated JSX/HTML paragraphs.
3. Include on every legal page:
   - Clear page title, effective date, and last-updated date
   - Table of contents or clean section navigation for long documents
   - Cross-links between `/privacy`, `/terms`, and `/subprocessors`
   - Footer link verification across the site (and note if the product login/
     signup screens should link to the published URLs).
4. Run the website's native build/check command (`npm run build` or `astro
   check`) to confirm zero broken imports or layout regressions.
