# GDPR, ePrivacy & API Data Protection Rules

Read this in Movement 3 (`audit`) and Movement 4 (`draft`) whenever `eu-gdpr` is
in `jurisdictions` (default for any EU company or product serving EEA users).

---

## 1. Controller vs Processor Split (GDPR Art. 4, Art. 24, Art. 28)

SaaS products frequently act in **two distinct GDPR roles**. Confusing them is
the single most common SaaS privacy-policy flaw.

| Context | Role | Examples |
|---|---|---|
| **Account, Billing, Security & Marketing** | **Data Controller** | User signup (`name`, `email`), password hashes, Google Sign-In identity, Stripe billing & VAT IDs, platform telemetry/quotas, security/SSO logs, marketing waitlist |
| **B2B Customer Workspace Content & Connectors** | **Data Processor** (Customer is Controller) | Files uploaded to a company workspace, team chat prompts/outputs, client data inside tasks/routines, connected Google Analytics / Search Console / Ads / Gmail data processed at the customer's instruction |
| **Individual Consumer Workspace (`b2b_and_consumers`)** | **Data Controller** (or household carve-out context) | Personal workspace data of an individual consumer acting outside a trade or profession |

**Drafting requirement:**
- In the **Privacy Policy**, state both roles clearly right after Controller
  Identity: the Privacy Policy governs personal data where the company acts as
  **Data Controller**, and summarizes security/subprocessor commitments where it
  acts as **Data Processor** on behalf of business customers.
- In the **Terms of Service**, include a dedicated **Data Protection & Data
  Processing (B2B)** clause incorporating Art. 28 processor commitments (process
  only on documented instructions, confidentiality, technical/organizational
  measures under Art. 32, subprocessor notice + list at `/subprocessors` or
  section, assistance with data subject requests and breaches, deletion/return
  upon workspace termination) and offer a standalone signed DPA on request if
  enterprise customers need one.

## 2. Lawful Basis Matrix (GDPR Art. 6(1))

**Anti-pattern warning:** Never cite **Consent (`Art. 6(1)(a)`)** as the lawful
basis for core account creation, workspace hosting, authentication, or billing.
Consent under GDPR Art. 7 must be freely withdrawable without detriment; core
service delivery runs on **Contract (`Art. 6(1)(b)`)**.

Every processing activity in the Privacy Policy must appear in a structured
table mapping **Purpose -> Data Categories -> Lawful Basis -> Retention**:

| Processing Activity | Proper GDPR Art. 6(1) Basis | Notes |
|---|---|---|
| Creating accounts, authenticating users, dispatching SSO, provisioning and running workspaces, AI chat/tasks/routines | **Art. 6(1)(b) Contract** | Necessary to perform the Terms of Service |
| Subscription checkout, invoicing, VAT calculation, tax record-keeping | **Art. 6(1)(b) Contract** & **Art. 6(1)(c) Legal obligation** | Tax/accounting statutes mandate retention (for example 10 years in Portugal) |
| Platform security, rate limiting, fraud/abuse prevention, crash diagnostics (Sentry with PII off), fair-use quota enforcement | **Art. 6(1)(f) Legitimate interests** | Name the specific legitimate interest (service integrity, security, cost control) |
| Connecting optional third-party OAuth integrations (Google Workspace/Analytics/Ads, Slack, Telegram) | **Art. 6(1)(a) Consent** / user-initiated authorization (or Processor instruction for B2B) | Revocable anytime in Workspace Settings or the provider's security console |
| Optional newsletter, waitlist, or non-essential analytics cookies | **Art. 6(1)(a) Consent** | Opt-in only; one-click unsubscribe |

## 3. Mandatory GDPR Art. 13 & Art. 14 Disclosures Checklist

Audit and draft against all 14 points:

1. **Controller identity and contact details** (legal entity name, registered
   address, privacy contact email; DPO contact if appointed, or explicit note
   that privacy inquiries reach the privacy team).
2. **Categories of personal data** collected directly, automatically, and from
   third parties (such as Google Sign-In or Stripe).
3. **Specific purposes + Art. 6(1) legal basis table** (no vague "improve our
   product" catch-alls).
4. **Legitimate interests specified** wherever Art. 6(1)(f) is relied upon.
5. **Named recipients / subprocessors** (or link/table naming exact providers,
   roles, and locations).
6. **International data transfers (GDPR Chapter V, Art. 44-49):**
   - Identify primary hosting location (for example EU/EEA data centers such as
     Paris `europe-west9`).
   - Where US-based subprocessors (Stripe, Resend, Sentry, Google, Anthropic,
     OpenAI, OpenRouter) process data outside the EEA, specify the transfer
     safeguard: **EU-US Data Privacy Framework (DPF)** adequacy (Art. 45) where
     certified, and **European Commission Standard Contractual Clauses (SCCs,
     Decision 2021/914)** with supplementary encryption/minimization measures
     (Art. 46). Flag the vendor transfer mechanism list in the Counsel Review
     Brief for verification against live DPAs.
7. **Concrete retention periods** per category (active account duration,
   workspace soft-delete grace window such as 24 hours, backup snapshot rotation
   window, statutory tax invoice retention, log expiry). Never write "as long as
   necessary" without a concrete rule or period.
8. **Data Subject Rights (Art. 15-22):** access, rectification, erasure,
   restriction, portability, objection (Art. 21, highlighted clearly when Art.
   6(1)(f) applies), withdrawal of consent at any time without affecting prior
   lawfulness.
9. **How to exercise rights + response SLA:** email address, self-service
   controls, and GDPR Art. 12(3) **1-month** response timeframe (extendable by 2
   months for complex requests with notice). Notice that for B2B workspace data
   where the company is Processor, end-user requests are redirected to the
   Workspace Owner (Controller).
10. **Right to lodge a complaint** with the lead EU Supervisory Authority (with
    name, address/website from `jurisdictions.md`, plus the user's local EEA
    authority).
11. **Statutory or contractual requirement:** state which fields are required to
    create an account/subscribe (email, billing details) and that omitting them
    prevents account creation.
12. **Automated decision-making & profiling (Art. 22):** state clearly whether
    the platform performs solely automated decisions with legal or similarly
    significant effects on individuals (typically **No**; AI agents assist users
    within workspaces under human direction).
13. **Security measures (Art. 32):** TLS in transit, encryption at rest for
    vaulted OAuth/API tokens, hashed passwords, container/tenant isolation,
    least-privilege short-lived token brokerage.
14. **Children's data (Art. 8):** minimum age threshold and statement that the
    service does not knowingly target children.

## 4. ePrivacy Directive (Art. 5(3)): Cookies & Local Storage

- **Strictly necessary exemption:** Session cookies, CSRF tokens, short-lived
  SSO state, and user-requested UI preferences (`locale`, sidebar state) do
  **not** require prior opt-in consent, but **must still be disclosed** (name or
  purpose, duration, first-party scope).
- **Non-essential cookies/scripts:** Analytics, session replay, or ad pixels
  that store/read terminal equipment identifiers require prior opt-in consent
  before firing. If `code-scan.md` finds non-essential trackers without a
  consent gate, raise a **Critical (`high`)** gap in `review.md`.
- **Remote Google Fonts / third-party CDNs on marketing sites:** Flag in
  `review.md` if `site-scan.md` detects unproxied requests to
  `fonts.googleapis.com` (discloses visitor IP to Google without consent under
  EU court rulings; self-hosting fonts is a 10-minute fix).

## 5. Google API Services User Data Policy (Limited Use)

Whenever `code-scan.md` sets `google_limited_use_required: true` (scopes such as
`gmail.*`, `analytics.*`, `webmasters.*`, `adwords`, `drive.*`):

1. Include an explicit **Google Workspace & Google API Data (Limited Use)**
   section in the Privacy Policy.
2. State verbatim-aligned commitments: use and transfer to any other app of
   information received from Google APIs adheres to the **Google API Services
   User Data Policy**, including the **Limited Use** requirements.
3. State explicitly that data obtained via Google Workspace / Google APIs:
   - is accessed only to perform user-configured workspace features (such as
     reading analytics metrics or drafting Gmail messages requested by the user);
   - had its refresh tokens encrypted centrally and never exposed raw;
   - is **never** sold, used for advertising, or used to train, fine-tune, or
     improve generalized AI or machine-learning models.
