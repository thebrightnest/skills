---
name: boring-business
description: >-
  End-to-end system for discovering, ideating, validating, and launching profitable,
  bootstrapped "boring businesses" (cash cows, micro-SaaS, niche directories, workflow tools).
  Covers the "Selling Shovels" ideation framework, 10-minute Tier 1 Quick Validation (Go/No-Go scorecards),
  30-minute Tier 2 Deep Validation (SERP intelligence, unit economics, organic distribution),
  searchable catalog of 137+ verified profitable bootstrapped businesses, and conversion landing page blueprints.
  Triggers on: "boring business", "cash cow", "validate idea", "business ideation", "micro-saas idea",
  "quick validation", "deep validation", "search case studies", "selling shovels", "unsexy business",
  "boringbiz", "business validation scorecard".
---

# Boring Business — Complete Cash Cow System

> **A self-contained methodology and toolkit for discovering, validating, and launching high-margin, highly automated, unsexy businesses.**

Unlike venture-backed startups that burn capital chasing category creation, a **boring business** targets existing, painful workflow bottlenecks with proven commercial search demand and 80-95%+ operational automation.

---

## ⚡ Command & Request Router

| Action / Request | Trigger Examples | Sub-Workflow | Reference & Scripts |
| :--- | :--- | :--- | :--- |
| **Ideate Concepts** | *"give me boring business ideas"*, *"ideate for Shopify merchants"*, *"what can I build with python in 10h/wk"* | [1. Ideation Workflow](#1-ideation-workflow) | [`references/finding-ideas.md`](./references/finding-ideas.md) |
| **Tier 1 Quick Validation** | *"quick validate this idea"*, *"is this idea viable"*, *"give me a go/no-go on X"* | [2. Quick Validation (Tier 1)](#2-quick-validation-tier-1) | [`templates/quick-validation-scorecard.md`](./templates/quick-validation-scorecard.md), [`scripts/score_calculator.py`](./scripts/score_calculator.py) |
| **Tier 2 Deep Validation** | *"deep validate this idea"*, *"full market analysis for X"*, *"unit economics and GTM plan for X"* | [3. Deep Validation (Tier 2)](#3-deep-validation-tier-2) | [`templates/deep-validation-report.md`](./templates/deep-validation-report.md), [`references/validation-criteria.md`](./references/validation-criteria.md) |
| **Search Case Studies** | *"find businesses doing SEO"*, *"show me Slack bot case studies"*, *"case studies over $20k MRR"* | [4. Knowledge & Case Study Search](#4-knowledge--case-study-search) | [`scripts/search_case_studies.py`](./scripts/search_case_studies.py), [`data/case_studies.json`](./data/case_studies.json) |
| **Landing Page Blueprint** | *"write landing page copy for this idea"*, *"boring business hero section"* | [5. Landing Page Blueprint](#5-landing-page-copy-blueprint) | [`templates/landing-page-copy.md`](./templates/landing-page-copy.md), [`references/copywriting-guide.md`](./references/copywriting-guide.md) |

---

## 1. Ideation Workflow

**Goal**: Generate 5–10 practical, profitable, high-automation business concepts customized to the user's skills, available hours, and domain context.

### Step 1: Context & Constraint Gathering
Extract or prompt the user for:
- **Skills & Expertise**: Technical (languages, stacks), domain experience (real estate, accounting, e-commerce, marketing).
- **Constraints**: Weekly hours (e.g. 5–15 hrs/week), budget for MVP, comfort with outbound sales vs pure SEO.
- **Audience Preference**: B2B SMBs, solo professionals, or agencies.

### Step 2: Query Bundled Case Studies for Inspiration
Run the bundled search script to identify patterns in the user's domain:
```bash
python3 skills/boring-business/scripts/search_case_studies.py "[domain or keyword]" -n 5
```

### Step 3: Apply the "Selling Shovels" Mental Model
Consult [`references/finding-ideas.md`](./references/finding-ideas.md):
- Don't build the fragile trend itself (e.g., another AI writer).
- Build the unsexy infrastructure: data conversion, compliance reporting, cost tracking, template packs, webhook monitors.

### Step 4: Output Structured Concept Pitches
Format output using [`templates/ideation-output.md`](./templates/ideation-output.md). For each concept, provide:
1. One-liner problem/solution.
2. Target customer segment & pain point severity.
3. Selling shovels angle.
4. Top 3 primary search terms.
5. Distribution channel (e.g. Programmatic SEO, Shopify App Store, Chrome Web Store).
6. Monetization model ($29-$99/mo).
7. Comparable case study from bundled data.

---

## 2. Quick Validation (Tier 1)

**Goal**: Generate a rapid **Go / No-Go scorecard in 10–15 minutes** to filter out non-viable ideas before investing heavy research.

### Step 1: Extract Keyword Targets
Identify 5–7 specific search queries a desperate buyer would type (e.g., `"shopify tax exempt certificate app"`, `"convert bank pdf to qbo"`).

### Step 2: Evaluate Demand & Competition
- Look up monthly search demand and keyword difficulty using DataForSEO or web search (see [`references/dataforseo-research-guide.md`](./references/dataforseo-research-guide.md)).
- Benchmark targets:
  - Total Monthly Volume across core terms: **> 1,000 searches/mo**
  - Commercial intent: Queries must be problem-focused or transactional, not purely academic.
  - SERP gaps: Are top results outdated tools, forum threads, or clunky enterprise software?

### Step 3: Calculate Quick Score
Run the bundled scoring calculator:
```bash
python3 skills/boring-business/scripts/score_calculator.py quick \
  --volume [total_volume] \
  --difficulty [low|medium|high] \
  --commercial-intent \
  --automatable
```

### Step 4: Render Scorecard
Fill out [`templates/quick-validation-scorecard.md`](./templates/quick-validation-scorecard.md):
- 🟢 **GO (Score >= 70)**: High signal. Advance immediately to Tier 2 Deep Validation.
- 🟡 **PIVOT (Score 50-69)**: Reposition angle, customer persona, or primary channel.
- 🔴 **NO-GO (Score < 50)**: Discard idea. Preserve resources for better candidates.

---

## 3. Deep Validation (Tier 2)

**Goal**: Produce a comprehensive 30–45 minute strategic validation report covering the **5 Core Weighted Pillars**, unit economics, and 14-day MVP roadmap.

### The 5 Core Pillars (Consult [`references/validation-criteria.md`](./references/validation-criteria.md))

1. **Search Demand (25% weight)**: Monthly volume, trend direction, CPC commercial value.
2. **Distribution Potential (25% weight)**: Low-CAC organic channels (SEO, marketplaces, integrations, communities).
3. **Organic Growth Potential (20% weight)**: Viral loops, public artifacts, programmatic flywheel, retention moat.
4. **Automation Level (15% weight)**: Self-service onboarding, digital delivery, minimal customer support burden. Consult [`references/automation-assessment.md`](./references/automation-assessment.md).
5. **Willingness to Pay (15% weight)**: B2B ROI, critical pain, budget availability ($49–$299/mo).

### Calculate Weighted Score
```bash
python3 skills/boring-business/scripts/score_calculator.py deep \
  --search [1-5] \
  --dist [1-5] \
  --organic [1-5] \
  --auto [1-5] \
  --wtp [1-5]
```

### Decision Thresholds
- **4.0 – 5.0**: 🟢 **BUILD IT** — Build MVP immediately. Target 14-day launch.
- **3.5 – 3.9**: 🟡 **PRE-SELL & VALIDATE** — Build landing page, collect 10 pre-orders.
- **3.0 – 3.4**: 🟡 **INVESTIGATE** — 5 customer discovery interviews to clarify problem severity.
- **2.5 – 2.9**: 🟠 **PIVOT** — Rethink angle or target customer.
- **< 2.5**: 🔴 **ABANDON** — Reject idea.

Deliver the final output formatted according to [`templates/deep-validation-report.md`](./templates/deep-validation-report.md).

---

## 4. Knowledge & Case Study Search

Search 137+ verified profitable, bootstrapped businesses bundled directly in [`data/case_studies.json`](./data/case_studies.json) or query the SQLite database [`data/boringbiz.db`](./data/boringbiz.db) using the zero-dependency Python script or direct SQL:

```bash
# Basic keyword search via Python script
python3 skills/boring-business/scripts/search_case_studies.py "seo" -n 5

# Filter by business type (tool, saas, content, directory)
python3 skills/boring-business/scripts/search_case_studies.py --type saas --min-revenue 20000

# Direct SQLite query
sqlite3 skills/boring-business/data/boringbiz.db "SELECT business_name, revenue_raw, distribution_channels FROM content_metadata WHERE revenue_normalized >= 20000 LIMIT 5;"

# Output as JSON
python3 skills/boring-business/scripts/search_case_studies.py "pdf" --json
```

---

## 5. Landing Page Copy Blueprint

When creating landing page copy for a validated boring business:
- Follow [`references/copywriting-guide.md`](./references/copywriting-guide.md).
- Use the formula: `[Specific Outcome] in [Time Frame] for [Target Customer]`.
- Output using the 6-section conversion template in [`templates/landing-page-copy.md`](./templates/landing-page-copy.md):
  1. Hero (Problem-focused, clear value proposition, immediate CTA)
  2. Proof & Logos (Credibility before features)
  3. Pain Point Deep Dive (Agitate current manual/costly workflow)
  4. 3-Step Solution (Simplicity & automation)
  5. Transparent Pricing (Flat monthly/annual, clear limits)
  6. FAQ & Risk Reversal (Refund guarantee, export data anytime)

---

## 📚 Bundled References Directory

* **Principles & Definitions**: [`references/principles.md`](./references/principles.md)
* **Ideation & Shovels Framework**: [`references/finding-ideas.md`](./references/finding-ideas.md)
* **The 7 Proven Business Archetypes**: [`references/proven-patterns.md`](./references/proven-patterns.md)
* **Validation Rubrics & Scoring**: [`references/validation-criteria.md`](./references/validation-criteria.md)
* **Automation Auditing & Reduction**: [`references/automation-assessment.md`](./references/automation-assessment.md)
* **Distribution Playbooks**: [`references/distribution-strategies.md`](./references/distribution-strategies.md)
* **SEO Content & Programmatic Blueprints**: [`references/seo-content-strategy.md`](./references/seo-content-strategy.md)
* **B2B Copywriting Playbook**: [`references/copywriting-guide.md`](./references/copywriting-guide.md)
* **DataForSEO & SERP Guide**: [`references/dataforseo-research-guide.md`](./references/dataforseo-research-guide.md)
* **Bundled Data & Knowledge Base**:
  * Case Studies JSON: [`data/case_studies.json`](./data/case_studies.json)
  * SQLite Database: [`data/boringbiz.db`](./data/boringbiz.db)
* **Real-world Worked Examples**:
  * Quick Validation: [`examples/example-quick-validation.md`](./examples/example-quick-validation.md)
  * Deep Validation: [`examples/example-deep-validation.md`](./examples/example-deep-validation.md)
  * Ideation Session: [`examples/example-ideation-session.md`](./examples/example-ideation-session.md)
