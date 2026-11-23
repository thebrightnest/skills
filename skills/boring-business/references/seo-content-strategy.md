# SEO Content Strategy for Boring Businesses

This guide provides proven SEO and content marketing strategies optimized for boring businesses - practical, search-driven content that ranks and converts.

## Table of Contents
1. [Core Principles](#core-principles)
2. [Keyword Research](#keyword-research)
3. [Topic Clustering](#topic-clustering)
4. [Content Brief Structure](#content-brief-structure)
5. [Publishing Schedule Strategy](#publishing-schedule-strategy)
6. [Distribution Channels](#distribution-channels)
7. [Metrics & Tracking](#metrics--tracking)

---

## Core Principles

### 1. Search Intent Drives Everything

**Four Types of Search Intent**:
- **Informational**: "How to track competitor pricing"
- **Navigational**: "Crayon competitive intelligence"
- **Commercial**: "Best competitive intelligence tools"
- **Transactional**: "Buy competitive intelligence software"

**Content Strategy by Intent**:
- **Month 1 (Education)**: Informational content builds trust
- **Month 2 (Comparison)**: Commercial/transactional content converts
- **Month 3 (Use Cases)**: Mix of informational + commercial

### 2. Long-Tail Keywords Win for Boring Businesses

**Why**:
- Lower competition (difficulty <30)
- Higher conversion rates
- Easier to rank as new site
- More specific = better qualified traffic

**Example Progression**:
- ❌ "competitive intelligence" (8,100/mo, difficulty 72) - Too competitive
- ⚠️ "competitive intelligence tools" (1,600/mo, difficulty 58) - Medium
- ✅ "track competitor pricing" (480/mo, difficulty 38) - Good target
- ✅ "automated competitor price tracking" (140/mo, difficulty 22) - Excellent

### 3. Comparison Content Converts Best

**High-Converting Content Types** (in order):
1. **"Alternative" posts**: "[Competitor] alternative" (e.g., "Crayon alternative")
2. **"vs" posts**: "[A] vs [B] vs [Your Product]"
3. **"Best [category]" posts**: "Best competitive intelligence tools for startups"
4. **Problem-solution posts**: "How to [solve problem] without [expensive solution]"
5. **Informational posts**: "What is [concept]" - Lower conversion but builds authority

**Distribution Strategy**:
- Month 1: 70% educational, 30% commercial
- Month 2: 40% educational, 60% commercial
- Month 3+: 50/50 mix

### 4. Topical Authority > Random Posts

**Don't**:
- Write 12 random posts on different topics
- Jump between unrelated keywords
- Chase trending topics outside your niche

**Do**:
- Build topic clusters around 3-4 pillars
- Create pillar content + 5-8 supporting posts per cluster
- Interlink aggressively within clusters
- Exhaust a topic before moving to next

**Example (CompeteIQ)**:
```
Pillar 1: Competitive Intelligence Basics
├── What is competitive intelligence (pillar post)
├── Competitive analysis frameworks
├── How to track competitors
├── Competitive intelligence for product managers
└── CI tools comparison

Pillar 2: Competitor Price Tracking
├── How to track competitor pricing (pillar post)
├── Automated price tracking tools
├── Web scraping vs Visual LLM
├── Price monitoring for SaaS
└── Competitor pricing dashboard setup

Pillar 3: Alternative Content (High-Converting)
├── Crayon alternatives
├── Klue alternatives
├── Kompyte alternatives
├── Klue vs Crayon vs CompeteIQ
└── Free competitive intelligence tools
```

### 5. Content Quality Thresholds

**Minimum Requirements**:
- **Word count**: 1,500-2,500 words for pillar, 1,000-1,500 for supporting
- **Headings**: H2/H3 structure matching top 10 SERP results
- **Visuals**: 3-5 images minimum (screenshots, comparison tables, infographics)
- **Links**: 3-5 internal links, 3-5 external authoritative links
- **Readability**: Flesch-Kincaid 60+ (8th-10th grade level)
- **Schema markup**: Article schema with FAQ markup if applicable

**Quality Indicators**:
- ✅ Answers the question in first 200 words (featured snippet optimization)
- ✅ Includes unique data or insights (not regurgitated from top 10)
- ✅ Has comparison tables or visual summaries
- ✅ Addresses related questions ("People Also Ask")
- ✅ Includes code examples or step-by-step tutorials (for technical topics)
- ✅ Updates with current year data (freshen annually)

---

## Keyword Research

### Target Keyword Criteria (DataForSEO Filters)

**Ideal Keywords for New Sites**:
```
Search Volume: 100-5,000/month
Keyword Difficulty: <50 (preferably <40)
Search Intent: Informational or Commercial
CPC: $1.00+ (indicates commercial value)
Trend: Stable or Growing
```

**Avoid**:
- Volume <100/month (too niche, won't move needle)
- Difficulty >60 (takes 12-18 months to rank)
- Declining trend (shrinking market)
- $0 CPC (no commercial intent)

### Keyword Expansion Strategy

**Seed Keywords** (from validation report):
- Primary product category (e.g., "competitive intelligence")
- Main problem solved (e.g., "track competitor pricing")
- Top 3 competitors (e.g., "Crayon", "Klue")

**Expansion Methods**:

**1. Related Keywords** (DataForSEO `google_related_keywords`):
```
Input: "competitive intelligence"
Output:
- "competitive intelligence tools" (1,600/mo, KD 58)
- "competitive analysis framework" (880/mo, KD 35)
- "track competitor pricing" (480/mo, KD 38)
- "competitor price monitoring" (260/mo, KD 28)
```

**2. Keyword Suggestions** (DataForSEO `google_keyword_suggestions`):
```
Input: "track competitor"
Output:
- "track competitor pricing" (480/mo, KD 38)
- "track competitor website changes" (140/mo, KD 22)
- "track competitor social media" (110/mo, KD 18)
- "track competitor features" (90/mo, KD 25)
```

**3. Keyword Ideas** (DataForSEO `google_keyword_ideas`):
- Provides broader category keywords
- Good for discovering adjacent topics
- Use for topic cluster ideation

**4. Competitor Keywords** (DataForSEO `google_ranked_keywords`):
```
Input: crayon.co
Output: Top 50 keywords Crayon ranks for
- Mine for content gaps
- Identify overlooked keyword opportunities
- See what works for competitors
```

**5. Question Keywords**:
- "how to [main keyword]"
- "what is [main keyword]"
- "best [category]"
- "why [problem occurs]"
- "[main keyword] vs [alternative]"

### Keyword Prioritization Matrix

**Score Formula**:
```
Priority Score = (Search Volume × Intent Match × (100 - Difficulty)) / 10000
```

**Intent Match Values**:
- Transactional: 1.5 (highest priority)
- Commercial: 1.3
- Informational: 1.0
- Navigational: 0.8 (only for brand terms)

**Example**:
```
Keyword: "Crayon alternative"
Volume: 480
Difficulty: 25
Intent: Commercial (1.3)

Score = (480 × 1.3 × (100-25)) / 10000 = 4.68

Keyword: "what is competitive intelligence"
Volume: 4,400
Difficulty: 38
Intent: Informational (1.0)

Score = (4,400 × 1.0 × (100-38)) / 10000 = 27.28
```

**Priority Tiers**:
- **Tier 1** (Score 20+): Write immediately
- **Tier 2** (Score 10-20): Month 2-3
- **Tier 3** (Score 5-10): Month 4-6
- **Tier 4** (Score <5): Backlog

---

## Topic Clustering

### Pillar + Cluster Structure

**Pillar Content**:
- Comprehensive guide (2,500-4,000 words)
- Targets primary keyword (higher difficulty OK)
- Links to all supporting content
- Updated quarterly with new insights

**Supporting Content**:
- Focused on specific subtopics (1,500-2,500 words)
- Targets long-tail variations
- Links back to pillar + related supporting posts
- Easier to rank (lower difficulty)

### Clustering Algorithm (for agents)

**Step 1: Group by Semantic Similarity**
- Use keyword overlap analysis
- Group keywords that share 2+ words
- Example: "track competitor pricing", "competitor price tracking", "price monitoring tools"

**Step 2: Identify Pillar Topics**
- Highest search volume keyword in each group
- Broadest search intent
- Example: "competitive intelligence" is pillar, "CI for startups" is supporting

**Step 3: Map Intent to Cluster Position**
- Informational keywords → Supporting content
- Commercial keywords → Supporting content (high conversion)
- Navigational keywords → Pillar content (if brand-related)

**Step 4: Validate Cluster Size**
- Minimum: 1 pillar + 3 supporting posts
- Maximum: 1 pillar + 10 supporting posts
- If fewer than 3 supporting posts, merge with another cluster
- If more than 10, split into 2 pillars

### Example Cluster Output

```json
{
  "cluster_name": "Competitive Intelligence for SaaS",
  "pillar_topic": {
    "keyword": "competitive intelligence",
    "volume": 4400,
    "difficulty": 38,
    "intent": "informational",
    "estimated_length": 3000
  },
  "supporting_topics": [
    {
      "keyword": "how to track competitor pricing",
      "volume": 480,
      "difficulty": 38,
      "intent": "informational",
      "estimated_length": 2000
    },
    {
      "keyword": "competitive analysis frameworks",
      "volume": 880,
      "difficulty": 35,
      "intent": "informational",
      "estimated_length": 1800
    },
    {
      "keyword": "best competitive intelligence tools",
      "volume": 720,
      "difficulty": 42,
      "intent": "commercial",
      "estimated_length": 2200,
      "conversion_potential": "high"
    }
  ],
  "internal_linking_map": {
    "pillar_links_to": ["all supporting topics"],
    "supporting_link_to": ["pillar", "related supporting topics"]
  }
}
```

---

## Content Brief Structure

### Template Overview

Every content brief should include:
1. **Target Keyword & Metadata**
2. **SERP Analysis** (top 10 competitor breakdown)
3. **Content Gaps** (what competitors miss)
4. **Recommended Outline** (H2/H3 structure)
5. **SEO Optimization Checklist**
6. **Internal Linking Opportunities**
7. **External Link Suggestions**
8. **Visual/Image Requirements**

### 1. Target Keyword & Metadata

```markdown
# Content Brief: [Title]

**Target Keyword**: [main keyword]
**Search Volume**: [X]/month
**Keyword Difficulty**: [Y]
**Search Intent**: [Informational/Commercial/Transactional]
**Target Length**: [1,500-2,500] words
**Estimated Time to Write**: [3-4] hours
**Publishing Priority**: [Tier 1/2/3]
**Conversion Potential**: [Low/Medium/High]
```

### 2. SERP Analysis

**What to Extract from Top 10**:
- **Common H2 headings**: What topics do 7+ results cover?
- **Average word count**: Median length of top 10
- **Content format**: How-to, listicle, comparison table, guide?
- **Visuals used**: Screenshots, infographics, videos, tables?
- **Author authority**: Industry experts, companies, blogs?

**Example**:
```markdown
## Top 10 Competitor Analysis

1. **[Title] - [Domain]** (Position 1)
   - Length: 2,400 words
   - Format: Step-by-step guide with code examples
   - Strengths: Comprehensive, includes Python scripts
   - Weaknesses: Outdated (2022), no Visual LLM mention

2. **[Title] - [Domain]** (Position 2)
   - Length: 1,800 words
   - Format: Comparison table of 10 tools
   - Strengths: Good comparison matrix
   - Weaknesses: Missing automation section, no pricing

[...continue for top 10]

**Common Patterns**:
- 8/10 include "manual methods" section (spreadsheets)
- 7/10 have comparison tables
- 5/10 mention web scraping
- 0/10 mention Visual LLM (opportunity!)
```

### 3. Content Gaps

**What Competitors Miss**:
- **Missing topics**: What do they NOT cover?
- **Outdated info**: Are they using 2022 data when it's 2025?
- **Lack of examples**: Do they explain but not show?
- **No code/screenshots**: Is it all theory, no practice?
- **Weak comparison**: Do they compare superficially?

**Example**:
```markdown
## Content Gaps (Opportunities)

✅ **Visual LLM Approach**: Zero results mention GPT-4 Vision for price extraction
✅ **Step-by-step Tutorial**: Most explain concepts but don't show implementation
✅ **Accuracy Comparison**: No one compares accuracy of different methods (90% for Visual LLM vs 60% for scrapers)
✅ **Pricing Breakdown**: Vague about tool costs, we can be specific ($10k-60k for enterprise, $49-199 for mid-market)
✅ **Decision Framework**: Missing "which method for which situation" guide
```

### 4. Recommended Outline

**Structure Based on SERP + Gaps**:
```markdown
## Recommended Outline

### 1. Introduction (150-200 words)
**Hook**: "[Startling stat or pain point]"
**Promise**: "This guide covers [5 methods] from [free] to [enterprise], with [accuracy comparisons] and [decision framework]"
**Who it's for**: "[Target audience]"

### 2. Why [Topic Matters] (300-400 words)
- **Benefit 1**: [Specific outcome]
- **Benefit 2**: [Specific outcome]
- **Benefit 3**: [Specific outcome]
- **Real cost**: [Quantify time/money wasted without solution]

### 3. Method 1: [Manual Approach] (400-500 words)
**How it works**: [Step-by-step]
**Example**: [Screenshot or walkthrough]
**Pros**:
- [Pro 1]
- [Pro 2]
**Cons**:
- [Con 1]
- [Con 2]
**When to use**: [Specific situation]
**Estimated cost**: [Time + money]

[...Repeat for each method]

### 8. Comparison Table (200 words)
| Method | Cost | Time | Accuracy | Maintenance | Best For |
|--------|------|------|----------|-------------|----------|
| Manual | $0 | 10h/mo | 95% | Low | <5 competitors |
| Google Alerts | $0 | 2h/mo | 40% | Low | Announcements only |
[...etc]

### 9. Which Method Should You Use? (300 words)
**Decision Framework**:
- If [condition], use [Method X]
- If [condition], use [Method Y]

**Example Scenarios**:
- "Small startup, <10 competitors, budget $0" → [Recommendation]
- "Mid-market SaaS, 50 competitors, budget $500/mo" → [Recommendation]

### 10. Conclusion & Next Steps (150 words)
**Summary**: [1-2 sentence recap]
**Recommendation**: [Default best choice for most readers]
**CTA**: [Link to your product with specific value prop]
```

### 5. SEO Optimization Checklist

```markdown
## SEO Optimization Checklist

**On-Page SEO**:
- [ ] H1 includes target keyword naturally
- [ ] Meta title (55-60 chars): "[Target Keyword]: [Benefit/Number]"
- [ ] Meta description (150-155 chars): "Learn [X methods] for [target keyword]. Compare [cost/time/accuracy]. [CTA]."
- [ ] URL slug: /blog/[target-keyword]
- [ ] Target keyword in first 100 words
- [ ] Target keyword in at least 2 H2 headings
- [ ] LSI keywords distributed throughout (related terms)
- [ ] Alt text on all images with keyword variations
- [ ] Image file names descriptive ([target-keyword]-comparison.png)

**Content Quality**:
- [ ] Answers question in first 200 words (for featured snippet)
- [ ] 3+ images with captions
- [ ] 1+ comparison table or visual summary
- [ ] Code examples or step-by-step screenshots (if applicable)
- [ ] Addresses "People Also Ask" questions
- [ ] External links to 3-5 authoritative sources (.edu, .gov, major publications)
- [ ] Internal links to 3-5 related posts
- [ ] Readability: Flesch-Kincaid 60+ (use Hemingway Editor)

**Schema Markup**:
- [ ] Article schema (headline, author, datePublished, dateModified)
- [ ] FAQ schema (if Q&A section included)
- [ ] HowTo schema (if step-by-step tutorial)
- [ ] Breadcrumb schema
```

### 6. Internal Linking Opportunities

```markdown
## Internal Linking Opportunities

**Link TO this post FROM**:
- [Pillar post title] (anchor: "[natural phrase with keyword]")
- [Related supporting post 1] (anchor: "[related topic]")
- [Related supporting post 2] (anchor: "[comparison phrase]")

**Link FROM this post TO**:
- **[Product landing page]** (primary CTA)
  - Anchor: "Try [Product] free for 14 days"
  - Placement: End of Method 4 section + Conclusion

- **[Pillar post: Competitive Intelligence Guide]**
  - Anchor: "comprehensive competitive intelligence guide"
  - Placement: Introduction

- **[Supporting post: Visual LLM vs Web Scraping]** (when published)
  - Anchor: "how Visual LLM compares to traditional scraping"
  - Placement: Method 4 section

- **[Supporting post: Crayon Alternatives]** (when published)
  - Anchor: "affordable Crayon alternatives"
  - Placement: Method 5 (Enterprise Tools) section
```

### 7. External Link Suggestions

```markdown
## External Links (Authority Building)

**Cite These Authoritative Sources**:
1. **[Gartner report on competitive intelligence]**
   - URL: [link]
   - Anchor: "Gartner estimates 85% of B2B companies use some form of competitive intelligence"
   - Placement: "Why [Topic] Matters" section

2. **[OpenAI GPT-4 Vision documentation]**
   - URL: https://platform.openai.com/docs/guides/vision
   - Anchor: "GPT-4 Vision API documentation"
   - Placement: Method 4 (Visual LLM) section

3. **[Price Intelligently pricing research]**
   - URL: [link]
   - Anchor: "pricing research from Price Intelligently"
   - Placement: Introduction

4. **[BeautifulSoup documentation]** (for technical accuracy)
   - URL: https://www.crummy.com/software/BeautifulSoup/
   - Anchor: "BeautifulSoup library"
   - Placement: Method 3 (Web Scraping) section

**Link Strategy**:
- Link to .edu/.gov when possible (highest authority)
- Link to established brands (Wikipedia, major publications)
- Link to primary sources (official documentation, original research)
- Use "nofollow" for competitors (if linking to their pricing pages)
```

### 8. Visual/Image Requirements

```markdown
## Images/Visuals Needed

**Required Images** (minimum 3):
1. **Comparison Table** (create in Canva or Figma)
   - Title: "5 Methods to Track Competitor Pricing: Cost, Time, Accuracy"
   - Format: PNG, 1200x800px
   - Alt text: "Comparison table showing cost, time investment, accuracy, and best use cases for 5 competitor pricing tracking methods"

2. **Screenshot: Manual Spreadsheet Example**
   - Description: Example spreadsheet with competitor pricing data
   - Format: PNG, annotated with red arrows
   - Alt text: "Excel spreadsheet template for manual competitor price tracking"

3. **Screenshot: Google Alerts Setup**
   - Description: Step-by-step Google Alerts configuration
   - Format: PNG, numbered steps
   - Alt text: "How to set up Google Alerts for competitor price changes"

4. **Code Example: Python Web Scraper**
   - Description: BeautifulSoup code snippet with syntax highlighting
   - Format: Screenshot or code block image
   - Alt text: "Python code example using BeautifulSoup to scrape competitor pricing from HTML"

5. **Screenshot: [Your Product] Dashboard**
   - Description: CompeteIQ dashboard showing automated price tracking
   - Format: PNG, 1200x800px
   - Alt text: "CompeteIQ competitor pricing dashboard with automated updates"

6. **Infographic: Decision Tree**
   - Title: "Which Competitor Pricing Method Should You Use?"
   - Format: PNG, vertical layout
   - Alt text: "Decision tree flowchart for choosing the right competitor price tracking method based on budget, team size, and number of competitors"

**Image Optimization**:
- Compress all PNGs with TinyPNG (<200KB each)
- Use descriptive file names: `competitor-pricing-comparison-table.png`
- Add captions below images with keyword variations
- Ensure images are responsive (max-width: 100%)
```

---

## Publishing Schedule Strategy

### Month 1: Education & Trust Building

**Goal**: Establish topical authority, rank for informational keywords

**Content Mix**:
- 70% Informational ("how to", "what is", "guide")
- 20% Commercial ("best tools", "comparison")
- 10% Use case/Case study

**Example Schedule** (4 posts):
- **Week 1**: Pillar post - "What is [Main Topic]? (Complete Guide)"
- **Week 2**: How-to post - "How to [Solve Main Problem]"
- **Week 3**: Framework post - "[Topic] Framework for [Target Audience]"
- **Week 4**: Technical post - "[Technology] vs [Traditional Method]"

### Month 2: Comparison & Conversion

**Goal**: Capture bottom-of-funnel traffic, drive conversions

**Content Mix**:
- 40% Informational
- 50% Commercial ("alternative", "vs", "best")
- 10% Use case

**Example Schedule** (4 posts):
- **Week 5**: Alternative post - "[Competitor] Alternatives for [Audience]" ⭐
- **Week 6**: Comparison post - "[Competitor A] vs [Competitor B] vs [Your Product]" ⭐
- **Week 7**: Best-of post - "Best [Category] Tools for [Specific Use Case]"
- **Week 8**: Problem-solution post - "How to [Goal] Without [Expensive Solution]"

### Month 3: Use Cases & Expansion

**Goal**: Cover long-tail variations, demonstrate expertise

**Content Mix**:
- 50% Informational
- 30% Commercial
- 20% Use case/Case study

**Example Schedule** (4 posts):
- **Week 9**: Use case post - "[Product] for [Specific Industry/Role]"
- **Week 10**: Advanced guide - "Advanced [Topic] Techniques"
- **Week 11**: Integration post - "How to Integrate [Your Product] with [Popular Tool]"
- **Week 12**: Case study - "How [Customer] Achieved [Outcome] with [Your Product]"

### Content Velocity Guidelines

**Recommended Publishing Frequency**:
- **Weeks 1-12**: 1 post/week (establish baseline)
- **Months 4-6**: 1-2 posts/week (accelerate growth)
- **Months 7+**: 1 post/week + quarterly pillar updates

**Quality > Quantity**:
- Better to publish 12 excellent posts than 24 mediocre posts
- Minimum time investment: 3-4 hours per post
- Use content briefs to maintain consistency

### Seasonal Timing

**When to Publish** (if applicable):
- **Tax software**: November-March
- **Event planning**: January-May (wedding season)
- **E-commerce tools**: September-November (holiday prep)
- **HR/recruiting**: January (new year hiring)

**General Rule**:
- Publish 2-3 months before peak season
- Example: Publish "Best HR tools" in October for January hiring season

---

## Distribution Channels

### Per-Post Distribution (1-2 hours)

**Immediately After Publishing**:

**1. Social Media**:
- **Twitter/X** (3 posts):
  - Day 1: Share with 1-2 key takeaways + link
  - Day 7: Reshare with different angle (pull quote or stat)
  - Day 30: Evergreen reshare
- **LinkedIn** (1 post):
  - Day 1: Professional summary (3-5 sentences) + link
  - Tag relevant people/companies in comments
- **Optional: Reddit** (1 post, carefully):
  - Relevant subreddit (r/SaaS, r/ProductManagement, etc.)
  - Provide value first, link second (in comment)
  - Don't spam or self-promote overtly

**2. Email Newsletter** (if 100+ subscribers):
- Subject: "[Number] Ways to [Benefit] [Specific Metric]"
- Preview: Top 3 takeaways + link to full post
- CTA: "Read the full guide"
- Timing: 2-3 days after publish (let SEO index first)

**3. Communities**:
- **Indie Hackers**: Share in weekly "Share Your Stuff" thread
- **Hacker News**: Only if genuinely technical/novel (or it'll get flagged)
- **Niche Slack/Discord**: Industry-specific communities (don't spam)

**Week 2-4 After Publishing**:

**4. Repurposing**:
- **Twitter Thread** (Day 3):
  - Break down post into 10-15 tweets
  - End with link to full post
- **LinkedIn Carousel** (Day 7):
  - 6-8 slides summarizing comparison table or framework
  - Use Canva or Figma
  - Last slide: "Read full guide [link]"
- **YouTube Video** (Optional, Week 4):
  - 5-10 minute walkthrough of guide
  - Embed video in blog post
  - Link to post in description

**5. Backlink Outreach** (Optional, Week 2-4):
- Find blogs that mention competitors
- Find "best [category] tools" listicles
- Outreach email template:
  ```
  Subject: Resource for [Their Article Title]

  Hi [Name],

  I noticed your article on [topic] at [URL]. Great breakdown!

  We just published a comprehensive comparison of [topic]:
  [Your URL]

  It includes [unique angle/data they don't have].
  If it's useful for your readers, feel free to link to it.

  Either way, thanks for the great content.

  [Your Name]
  ```
- Target: 5-10 outreach emails per post
- Success rate: 10-20% (1-2 backlinks per post)

### Distribution Metrics

**Immediate (Week 1)**:
- Social shares: 10-50 (depending on following)
- Reddit upvotes: 5-20 (if not removed)
- Email opens: 20-40% (newsletter)
- Click-through: 3-8% (newsletter)

**Medium-term (Month 1-3)**:
- Organic traffic: 10-50 visitors/month (first month)
- Ranking: Position 20-50 (first month)
- Backlinks: 1-3 (if outreach successful)

**Long-term (Month 6-12)**:
- Organic traffic: 100-500 visitors/month (top 10 ranking)
- Ranking: Position 5-15 (for low-difficulty keywords)
- Backlinks: 5-15 (natural accumulation)

---

## Metrics & Tracking

### Success Metrics by Timeframe

**Week 1-4** (Immediate):
- [ ] Post published and indexed (Google Search Console)
- [ ] Social shares: 10+ combined
- [ ] Email click-through: 5%+
- [ ] Initial ranking: Top 50 for target keyword

**Month 1-3** (Short-term):
- [ ] Ranking: Top 20 for target keyword
- [ ] Organic traffic: 50+ visitors/month per post
- [ ] Backlinks: 2+ per post
- [ ] Time on page: 2+ minutes
- [ ] Bounce rate: <70%

**Month 6-12** (Long-term):
- [ ] Ranking: Top 10 for target keyword
- [ ] Organic traffic: 200+ visitors/month per post
- [ ] Backlinks: 10+ per post
- [ ] Conversion rate: 2-5% (email signup)
- [ ] Engaged users: 30%+ (scroll depth 75%+)

### Key Metrics to Track

**Search Performance** (Google Search Console):
- Impressions (how often shown in search)
- Clicks (how often clicked)
- Average position (ranking)
- Click-through rate (CTR)

**Traffic** (Google Analytics):
- Organic sessions per post
- Pages per session (2.0+ is good)
- Average time on page (2:00+ is good)
- Bounce rate (<70% is good)

**Engagement**:
- Scroll depth (75%+ is good)
- Social shares
- Comments
- Backlinks (Ahrefs, SEMrush)

**Conversion**:
- Email signups from blog post
- Product trial signups
- Revenue attributed to blog (use UTM parameters)

### Tracking Setup

**Required Tools**:
1. **Google Search Console** (free)
   - Verify domain ownership
   - Submit sitemap
   - Track search performance

2. **Google Analytics 4** (free)
   - Install GA4 tracking code
   - Set up conversion events (email signup, trial signup)
   - Create custom report for blog performance

3. **Backlink Checker** (optional, paid):
   - Ahrefs ($99/mo) or SEMrush ($119/mo)
   - Track backlinks, domain authority
   - Monitor competitor rankings

### When to Update Content

**Quarterly Review** (every 3 months):
- Check rankings for target keywords
- If dropped >5 positions → investigate and update
- Update statistics/data with current year
- Add new sections for emerging trends
- Refresh screenshots if UI changed

**Annual Refresh** (every 12 months):
- Comprehensive rewrite of pillar content
- Update all statistics and research
- Add new methods/tools discovered
- Improve based on reader feedback (comments, support tickets)
- Re-publish with new date (signals freshness to Google)

**Triggers for Immediate Update**:
- Major industry change (new competitor, regulation)
- Your product launches new feature mentioned in post
- Ranking drops >10 positions suddenly
- Comment points out outdated/incorrect info
- Competitor launches similar content that outranks you

---

## Content Strategy Checklist

**Before Starting** (Planning Phase):
- [ ] Keyword research complete (100+ keywords identified)
- [ ] Keywords prioritized by score (Tier 1/2/3)
- [ ] Topic clusters defined (3-4 pillars + supporting content)
- [ ] Publishing schedule created (12 weeks)
- [ ] Distribution channels identified (social, email, communities)

**Per Content Brief** (Preparation Phase):
- [ ] SERP analysis complete (top 10 reviewed)
- [ ] Content gaps identified (3+ opportunities)
- [ ] Outline created (H2/H3 structure)
- [ ] Target length determined (1,500-2,500 words)
- [ ] Internal linking plan defined
- [ ] Visual requirements listed (3-5 images)

**After Writing** (Pre-Publish Phase):
- [ ] SEO checklist complete (meta title, description, schema)
- [ ] Readability score 60+ (Hemingway Editor)
- [ ] Images optimized (<200KB, descriptive alt text)
- [ ] Internal links added (3-5)
- [ ] External links added (3-5 authoritative)
- [ ] Proofread (no typos, grammar errors)

**After Publishing** (Distribution Phase):
- [ ] Submitted to Google Search Console
- [ ] Shared on social media (Twitter, LinkedIn)
- [ ] Sent in email newsletter (if applicable)
- [ ] Posted in relevant communities (Indie Hackers, etc.)
- [ ] Tracking set up (GA4 events, UTM parameters)

**Ongoing** (Optimization Phase):
- [ ] Monthly ranking check (Google Search Console)
- [ ] Quarterly content refresh (update stats, fix broken links)
- [ ] Annual comprehensive update (rewrite if needed)

---

## Agent Usage Guidelines

When the `content-strategy` agent generates a 90-day content calendar, it should:

1. **Read validation report** → Extract seed keywords, competitors, pain points
2. **Run DataForSEO queries** → Expand keywords (related, suggestions, competitor keywords)
3. **Filter and prioritize** → Apply keyword criteria (volume, difficulty, intent)
4. **Create topic clusters** → Group semantically similar keywords (3-4 pillars)
5. **Generate content briefs** → For top 12 topics (1 per week for 12 weeks)
6. **Build publishing schedule** → Optimize by conversion potential (Month 1: education, Month 2: comparison)
7. **Create distribution plan** → Channel-specific recommendations
8. **Output markdown files** → `90-day-calendar.md`, `keyword-research.json`, `briefs/*.md`, `distribution-plan.md`

### Quality Gates

**Before outputting content brief**:
- SERP analysis includes ≥5 competitors reviewed
- Content gaps list ≥3 opportunities
- Outline has ≥5 H2 sections
- SEO checklist is 100% complete
- Internal linking plan includes ≥3 links

**Before finalizing publishing schedule**:
- Month 1 is 70%+ informational (trust-building)
- Month 2 includes ≥2 high-conversion posts ("alternative", "vs")
- All topics map to a pillar cluster (no orphan posts)
- Publishing velocity ≤1 post/week (quality > quantity)

**Traffic Projection Formula** (for reporting):
```
Conservative: (Total keyword volume / 10) × 0.15 (15% CTR at position 8-10)
Realistic: (Total keyword volume / 10) × 0.25 (25% CTR at position 5-7)
Optimistic: (Total keyword volume / 10) × 0.40 (40% CTR at position 1-3)
```

Example:
```
12 keywords, avg 500/mo volume = 6,000 total volume
Conservative: (6,000 / 10) × 0.15 = 90 visitors/month
Realistic: (6,000 / 10) × 0.25 = 150 visitors/month
Optimistic: (6,000 / 10) × 0.40 = 240 visitors/month
```

---

## Resources

**SEO Tools**:
- Google Search Console (free) - Track rankings
- Google Analytics 4 (free) - Track traffic
- Hemingway Editor (free) - Check readability
- Ahrefs ($99/mo) - Backlink analysis, keyword research
- SEMrush ($119/mo) - All-in-one SEO suite

**Content Tools**:
- Grammarly (free/$12/mo) - Grammar and style checking
- Canva (free/$13/mo) - Create comparison tables, infographics
- TinyPNG (free) - Image compression
- Loom (free) - Create tutorial videos

**Inspiration** (boring business blogs done well):
- Stripe Blog (technical depth + SEO)
- HubSpot Blog (comprehensive guides)
- Ahrefs Blog (case studies with data)
- Close.com Blog (B2B SaaS playbook)

---

## Summary

**Content strategy for boring businesses**:
1. **Start with search demand** (keyword research, not guessing)
2. **Build topic clusters** (pillar + supporting content, not random posts)
3. **Target long-tail keywords** (<40 difficulty, 100-5,000 volume)
4. **Month 1: educate**, Month 2: convert, Month 3: expand
5. **Quality > quantity** (1 excellent post > 3 mediocre posts)
6. **Distribute consistently** (social, email, communities)
7. **Track and optimize** (Search Console, Analytics, quarterly updates)

**Expected timeline to traction**:
- **Month 1-3**: Index and crawl (minimal traffic)
- **Month 4-6**: Start ranking (50-200 visitors/month)
- **Month 7-12**: Mature rankings (500-2,000 visitors/month)
- **Year 2+**: Compound growth (2,000-10,000 visitors/month)

SEO is a long game. Boring businesses win by consistency, not tricks.
