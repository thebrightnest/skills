# Check: review a piece of business material against the product

`check <material>` runs on the business side. The material can be a homepage
draft, a deck, a sales email, a persona study, a positioning doc, or another
model's output. The question is always the same: **does this say anything the
product doesn't do, refuses to do, or can't back?**

It's the cheapest way to stop over-claiming before it ships. It's also the way
to vet strategy work produced by a model that couldn't see the product.

Input: a file path, a URL (fetch it), or pasted text. Read it all before
judging any of it.

---

## What to check, line by line

| Check | Against | Flag when |
|---|---|---|
| **Capability claims** | `app/capabilities.md` | It describes something the product doesn't do today |
| **Limits** | `app/capabilities.md`, `app/boundaries.md` | It drops a limit ("compare any number of variants" when there's a cap) |
| **Refused territory** | `app/boundaries.md` | It promises or implies what the product refuses. A: prediction of conversion, engagement, reach, individual behaviour, price points, representativeness. B: guarantees the product doesn't give, such as "your data never leaves your workspace" when a central service holds tokens, certifications it doesn't hold, or providers it doesn't support |
| **Output and trust claims** | `app/boundaries.md` (claims we can back) | "validated", "accurate", "predicts", "representative", "statistically", percentages from a directional tool, "secure", "private", "compliant", "enterprise-grade", uptime figures |
| **Journeys** | `app/journeys.md` | It describes a flow the product doesn't have ("paste and get results in 30 seconds" when setup comes first) |
| **Grounding** | `app/grounding.md` | It overstates what grounds the output or guarantees the service, or states current coverage (markets, integrations, models) as a fixed list |
| **Tense** | — | Planned or partial features described as current |
| **Invented specifics** | the material's own sources | Figures, prices, customer outcomes or results that nothing supports. Common in model-written scenarios |
| **Words** | `app/glossary.md` | Terms the product doesn't use, or the glossary's "avoid" list |
| **Personas** | `business/personas/` | It targets a persona or job not in the contract, or states an Inferred persona as proven |
| **Positioning** | `business/promises.md` "Positioning", `business/personas/` | Its target, need or alternative matches no confirmed persona, job or **Today they…**, or it contradicts the recorded positioning |

Scenarios and case examples need extra care. A scenario that ends "and the
persona said Concept A converts better, so they split the budget" is a
refused claim, even though it reads as a story. So is "she connected her
Outlook and the agent cleared her week" for a Google-only product. Flag the
outcome, not only the setup.

When the business side lives in a website repo, the material is often a page
source (`.astro`, `.mdx`, `.tsx`). Check the rendered copy, not the markup:
headings, body, buttons, meta descriptions, pricing tables and FAQ entries all
count as promises.

## Findings

One row per issue, quoting the material exactly:

| # | Quote | Problem | Against | Severity | Suggested rewrite |
|---|---|---|---|---|---|

Severity:

- **high:** refused territory, an unbacked capability, or an output claim the
  product can't support. Likely to embarrass someone in front of a client.
- **medium:** a dropped limit, the wrong tense, an invented specific, or a
  journey that doesn't exist.
- **polish:** vocabulary, or an Inferred persona stated too confidently.

Suggested rewrites keep the author's intent and say what the product can
honestly back. For example:

- A ❌ "Find out which concept converts best."
- A ✅ "See how each market reads each concept, and why."
- B ❌ "Your data never leaves your workspace."
- B ✅ "Each workspace runs in isolation, and your Google tokens stay in our
  vault. Workspaces only ever get short-lived access."

End with the number of findings by severity and what the high ones would
cost if the material went out as is. Whether it goes out is the user's call.
If the user wants to track any finding, add it to `decisions/` as a
`decide` item ("reword, change the product, or keep the claim?").

## The received `app/` is a copy

Run the check anyway, and always head the result with `Checked against app/ as
of <version>, received <date>. The product may have changed since.` An old
snapshot beats checking against memory.
