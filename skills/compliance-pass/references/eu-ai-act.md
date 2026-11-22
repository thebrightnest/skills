# EU AI Act (Regulation (EU) 2024/1689)

Read this in Movement 3 (`audit`) and Movement 4 (`draft`) whenever `eu-ai-act`
is in `jurisdictions` and the product embeds LLMs, generative media, or
autonomous agents. By late 2026, prohibited-practice rules (Art. 5, Feb 2025),
GPAI rules (Title VIII, Aug 2025), and transparency rules (Art. 50, Aug 2026)
are all in force.

---

## 1. Role & Risk Classification (Audit Step)

Classify the product accurately in `review.md` before drafting clauses:

| Concept | Question to check against `app/ai-systems.md` | Typical SaaS / Workspace Verdict |
|---|---|---|
| **Operator Role (Art. 3)** | Does the company pre-train foundational GPAI models, fine-tune weights at scale, or orchestrate third-party GPAI APIs with prompts/tools/UI? | **Deployer** (and **Downstream AI System Provider** of a limited-risk application orchestrating upstream GPAI providers such as Anthropic, Google, OpenAI) |
| **Prohibited Practices (Art. 5)** | Subliminal manipulation, exploiting vulnerabilities, social scoring, untargeted facial scraping, workplace/education emotion recognition? | Must be **None** in product design, and **explicitly forbidden** in ToS Acceptable Use |
| **High-Risk Annex III (Art. 6)** | Is the product marketed or intended as a safety component or for Annex III decisions (recruitment/CV screening, worker evaluation/firing, credit scoring, education grading, biometric ID, critical infrastructure, law enforcement)? | Typically **Not intended as High-Risk**. ToS Acceptable Use must **prohibit customers from using the workspace for unassessed Annex III high-risk automated decisions** (or require prior human-in-the-loop compliance by the customer as Deployer) |
| **Transparency Risk (Art. 50)** | Do humans interact with AI chatbots/agents, or does the product generate synthetic text, images, audio, or video? | **Yes: Art. 50 applies directly** |

*Warning:* Under Art. 25(1), rebranding an upstream high-risk system or
modifying intended purpose into an Annex III domain turns a Deployer into a
High-Risk Provider. Preventing unintentional Annex III scope creep via clear
intended-purpose boundaries in ToS is essential.

## 2. Article 50 Transparency Disclosures (Privacy Policy & AI Notice)

When Art. 50 applies, weave clear, plain-language AI disclosures into **both**
the Privacy Policy ("How AI Processes Data") and Terms of Service ("AI Features,
Transparency & Human Oversight"):

1. **Human-AI Interaction (Art. 50(1)):**
   Users interacting with workspace chat, specialist agents, scheduled routines,
   or connected messaging bots (Slack, Telegram, WhatsApp, Discord) are
   interacting with AI systems powered by large language models. Where workspace
   members connect external channels or share public links, the customer is
   responsible for ensuring external recipients know when a bot or output is
   AI-driven.
2. **Synthetic Media & Content Marking (Art. 50(2) & Art. 50(4)):**
   If `app/ai-systems.md` includes image, audio, or video generation, or public
   editorial/content drafting:
   - State that AI-generated media may include machine-readable provenance
     metadata/watermarks embedded by upstream model providers (such as C2PA /
     SynthID) and users must not strip mandatory provenance markers where law
     requires them.
   - Remind users publishing AI-generated text on matters of public interest (or
     synthetic deepfake imagery) of their Art. 50(4) deployer disclosure duties
     unless human editorial review and editorial responsibility apply.
3. **Model Training & Data Retention Commitment:**
   State unambiguously:
   - Whether **your company** uses customer workspace files, prompts, or outputs
     to train or fine-tune foundational AI models (default best practice for
     SaaS workspaces: **No**).
   - How **upstream AI providers** handle API inputs (commercial API tiers where
     inputs/outputs are not used to train upstream foundational models, subject
     to short-term provider abuse-monitoring retention if applicable; verify in
     `decisions/` if custom/OpenRouter endpoints are enabled).

## 3. Mandatory AI Clauses for Terms of Service

Include four concrete clauses in the Terms of Service whenever AI systems exist:

1. **Probabilistic Nature & No Professional Advice:**
   AI outputs are probabilistic and may be incomplete, inaccurate, or outdated
   ("hallucinations"). Outputs do not constitute legal, financial, tax, medical,
   or regulated professional advice.
2. **Human Oversight & Autonomous Actions:**
   When users enable autonomous tasks, scheduled cron routines, email sending,
   or third-party connectors (such as Google Ads, Analytics, Slack, or Gmail),
   the customer retains full human oversight and responsibility for reviewing
   actions, configuring permissions, and verifying outputs before relying on or
   publishing them.
3. **Input & Output Ownership:**
   As between the parties, the customer retains all rights to Customer Inputs
   (prompts, uploaded files, project memory) and receives all rights the company
   can hold in AI Outputs, noting that similar outputs may be generated for
   other users due to the nature of machine learning.
4. **AI Acceptable Use & EU AI Act Boundaries:**
   Prohibit using the platform for:
   - Any prohibited AI practice under **Article 5 of the EU AI Act**;
   - Solely automated high-risk decision-making under **Annex III of the EU AI
     Act** (such as automated candidate screening, employee performance
     scoring/termination, creditworthiness scoring, or biometric categorization)
     without independent legal compliance;
   - Generating unlawful content, non-consensual intimate imagery, deceptive
     impersonation, malware, or violating upstream model provider usage policies.
