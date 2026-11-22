# Code Scan: extracting technical reality with evidence

Run this in Movement 2. Never ask the user to describe what the app collects
when the code is present. Extract facts directly and cite `<repo>:<path>:<line>`.

Use archetypes **A, output product** (single-purpose generator or content tool)
and **B, platform product** (multi-tenant workspace with identity, connectors,
and background agents) to distinguish simple vs multi-layered architectures.

---

## 1. Data categories and database schemas (`app/data-flows.md`)

Locate every persistent store across product repos (and `drizzle/`, `prisma/`,
or form handlers on `site`):

```bash
find . -maxdepth 5 \( -path "*/migrations/*" -o -path "*/drizzle/*" -o -name "schema.prisma" -o -path "*/Models/*" -o -name "*models*.py" \) \
  -not -path "*/vendor/*" -not -path "*/node_modules/*" 2>/dev/null
```

Classify every personal or customer-linked record into four buckets:

| Bucket | Typical tables / sources | Controller or Processor? |
|---|---|---|
| **Account & Identity** | `users`, `sessions`, `password_reset_tokens`, SSO nonces, OAuth login profiles | **Controller** |
| **Billing & Commercial** | `subscriptions`, `customers`, tax IDs, `usage_boosts`, plan assignments | **Controller** |
| **Telemetry & Operational Logs** | daily token/cost ledgers, member activity counts, error traces, rate-limit keys | **Controller** (security, billing, quota enforcement) |
| **Workspace & Customer Content** | project files, chat messages, tasks, scheduled routine outputs, connected third-party accounts, public share links | **Processor** for B2B customers; **Controller** for individual consumers |

For each bucket, record:
- Exact fields collected (for example: `name`, `email`, `avatar_url`, hashed
  `password`, OAuth tokens, IP/user-agent in sessions).
- At-rest protection in code (for example: Eloquent `'encrypted'` casts on
  refresh tokens or API keys, `hashed` passwords, isolated per-tenant SQLite or
  disk quotas).
- Deletion and retention mechanics implemented in code (soft-delete grace
  windows such as 24-hour deprovisioning, cascade deletes, backup snapshot
  schedules). Distinguish **code-enforced retention** from **policy retention**
  (which belongs in `business/entity.md`).

## 2. Subprocessors, hosting, and third-party APIs (`app/subprocessors.md`)

Inspect dependency manifests, `.env.example`, mail/error/payment configs, and
deployment scripts:

```bash
grep -rnE "stripe|resend|sendgrid|postmark|mailgun|sentry|posthog|plausible|mixpanel|segment|cloudflare|googleapis|openai|anthropic|openrouter|deepseek|gemini|aws|gcloud|europe-|us-" \
  .env.example */.env.example composer.json package.json pyproject.toml scripts/ config/ 2>/dev/null | head -60
```

For each external vendor that touches personal or workspace data, record:
1. **Vendor name** (exact entity/service, such as Stripe, Resend, Functional
   Software / Sentry, Google Cloud Platform, Google OAuth APIs, Anthropic,
   OpenAI, OpenRouter). Never write generic labels like "a cloud provider".
2. **Purpose** (for example: transactional password-reset and notification
   emails, VAT-inclusive subscription checkout, crash reporting, container
   hosting, LLM inference).
3. **Data categories shared** (check config flags such as Sentry's
   `send_default_pii` and `sql_bindings` so you report accurately whether PII is
   scrubbed by default).
4. **Region / transfer clues in code** (for example: `europe-west9` Paris GCE
   zones in deploy scripts vs US-headquartered API endpoints). Mark unknown
   regions `verify in vendor dashboard` so they surface in `decisions/` if
   needed.
5. **Conditional vs universal** (for example: Slack, Telegram, Discord, or
   Google Analytics connectors run only when a workspace owner configures them).

## 3. OAuth scopes and connector vaults (`app/data-flows.md` & `app/cookies-security.md`)

Search for OAuth drivers, scopes, and token brokers:

```bash
grep -rnE "scopes\(|googleapis\.com/auth|Socialite|oauth|refresh_token" --include=*.{php,py,ts,js,go} . 2>/dev/null | grep -vE "vendor|node_modules|test"
```

Record every exact OAuth scope requested. Pay special attention to **Google
Sensitive and Restricted Scopes** (`gmail.readonly`, `gmail.compose`,
`adwords`, `analytics.*`, `webmasters.*`, `drive.*`, `calendar.*`). Whenever any
Google Workspace or Google API scope beyond basic `openid email profile` is
present, flag `google_limited_use_required: true` so Movement 3 and Movement 4
mandate the Google API Services User Data Policy (Limited Use) disclosure and
prohibit training generalized AI models on Google API data.

Also check token architecture (for **B, platform product**): does the control
plane vault encrypted `refresh_token` values centrally and broker short-lived
`access_token` values to isolated runtimes? Cite the exact model and broker
controller.

## 4. AI systems, autonomous execution, and media generation (`app/ai-systems.md`)

Scan for LLM providers, agent loops, scheduled cron routines, task runners, and
image/audio/video generation skills:

- **AI features exposed to users:** interactive chat, specialist agent personas,
  autonomous Kanban task execution, cron-scheduled routines, image/media
  generation, external messaging channel bots (Slack, Telegram, WhatsApp,
  Discord).
- **Model governance:** how upstream providers and allowed models are selected
  (central allowlist, user model switcher, fallback behavior).
- **Data sent to models:** prompts, attached project files, memory files, tool
  outputs.
- **Human oversight & guardrails in code:** approval gates, read-only system
  paths, blocked package managers, command scanners, review columns on task
  boards, manual routine confirmation dialogs.
- **Synthetic content outputs:** whether the product generates images, HTML
  pages, or external social/blog copy, and whether public share links (`/s/...`)
  exist.

## 5. Cookies, browser storage, and security (`app/cookies-security.md` & `site/site-scan.md`)

Scan both server session configs and client code:

```bash
grep -rnE "SESSION_DRIVER|cookie|set_cookie|localStorage|sessionStorage|gtag|fbq|plausible|posthog|umami" \
  config/ src/ runtime/ public/ 2>/dev/null | grep -vE "vendor|node_modules|dist|test" | head -50
```

Classify every cookie and localStorage key:
- **Strictly necessary:** authentication session cookies, CSRF tokens
  (`XSRF-TOKEN`), short-lived SSO nonce handoffs, UI language/theme/layout
  state in `localStorage`.
- **Analytics / Performance:** first-party or third-party analytics.
- **Marketing / Targeting:** ad pixels, retargeting tags.

**Important:** if both `app/` and `site/` set **only strictly necessary**
cookies and UI-preference `localStorage` keys with zero analytics/marketing
cookies, record `cookie_banner_exempt: true` with citations (ePrivacy Directive
Art. 5(3) exemption). Do not recommend a cookie consent banner when no
non-essential cookies or trackers exist; disclose the strictly necessary cookies
clearly in the Privacy Policy instead.

## 6. Website-specific scan (`site/site-scan.md`)

On the `site` side, scan the marketing website repo specifically for:
- Lead capture, waitlist, newsletter, or contact forms and their database tables
  (`drizzle/`, Supabase, Resend Audiences, Loops, ConvertKit).
- Client-side analytics, tag managers, video embeds (YouTube/Loom), or external
  font CDNs (Google Fonts vs self-hosted fonts; note German/EU IP-disclosure
  sensitivity if Google Fonts CDN is loaded remotely).
- Existing `/privacy`, `/terms`, `/cookies`, or `/dpa` routes and links from
  headers, footers, and checkout/signup CTAs.
