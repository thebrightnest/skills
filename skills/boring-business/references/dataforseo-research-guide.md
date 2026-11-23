# Market Research & Search Demand Guide

To evaluate search demand, competition, and keyword economics accurately, use either:
1. **DataForSEO MCP Tools** (if configured in environment / `.mcp.json`)
2. **Web Search & SERP Analysis** (via native search tools)

---

## 1. Using DataForSEO (When Available)

If DataForSEO MCP tools are available:

### Step 1: Keyword Overview (`google_keyword_overview`)
- **Tool**: `mcp__dataforseo__dataforseo_labs_google_keyword_overview`
- **Inputs**:
  - `keywords`: Array of 5-7 target terms (e.g. `["slack attendance bot", "slack clock in bot", "time tracking slack"]`)
  - `location_name`: `"United States"`
  - `language_code`: `"en"`
  - `include_clickstream_data`: `true`
- **Metrics to extract**:
  - `search_volume`: Monthly searches
  - `cpc`: Cost per click (high CPC > $3.00 indicates strong commercial intent)
  - `competition`: Level from 0.0 to 1.0

### Step 2: SERP Competitor Analysis (`google_organic_serp`)
- **Tool**: `mcp__dataforseo__serp_google_organic_live_advanced`
- **Inputs**: Target core keyword, `"United States"`, `"en"`
- **Assess SERP Quality**:
  - Top 3 domain ratings
  - Presence of Reddit / Quora / forum threads (strong signal of underserved demand)
  - Dated competitors with poor UI

### Step 3: Related Keywords (`keyword_ideas`)
- Discover long-tail variations and alternative search intents.

---

## 2. Using Native Web Search / SERP Analysis (Fallback)

When DataForSEO is not active or for quick checks:

### Query Formats:
1. **Demand & Alternatives**:
   - `"[problem] alternative"`
   - `"[competitor] pricing"`
   - `"best software for [specific workflow]"`
2. **Community Pain**:
   - `site:reddit.com "[problem] tool"`
   - `site:producthunt.com "[category]"`
3. **Marketplace Discovery**:
   - `site:apps.shopify.com "[feature]"`
   - `site:chromewebstore.google.com "[utility]"`
