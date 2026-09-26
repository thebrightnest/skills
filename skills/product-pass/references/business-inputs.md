# Business inputs: what the business side owes the contract

The `business/` half is written on the business side. The product follows it
for **who we serve, why, and how their journey should go**. The app side never
edits it. It only receives it by copy and reviews fit against it.

Three files:

| File | Answers | Required content |
|---|---|---|
| `personas.md` | Who hires the product, for what, and how sure are we? | Personas, jobs, triggers, evidence tags, priority, evidence log |
| `journeys.md` | How should each job go for that persona? | Intended journeys (format in `journeys.md` reference) |
| `promises.md` | What do we say publicly? | Claims made on the site, decks, sales material, with where each appears |

---

## Minimum for each persona

- **ID and name.** Short, stable IDs (`C1`, `V2`). Don't reuse an ID for a
  different persona.
- **Who:** role, organization, context.
- **Triggers:** the moments that send them to the product, in their words.
- **Jobs:** "When …, I want …, so …", one per distinct job.
- **Today they…:** what they do instead. That's the real competitor.
- **Evidence tag:**

  | Tag | Meaning |
  |---|---|
  | **Real** | Someone outside the team said or did this |
  | **Observed** | The team used the product this way |
  | **Inferred** | Hypothesis. Plausible, unconfirmed, and must not drive a bet alone |

  Tag the persona and, where they differ, individual claims inside it.
- **Priority:** `now` / `later` / `vision`. **This is a business decision.** The
  skill never infers or changes it. Without priority, the fit review can't rank
  gaps. Record a `clarify` item and rank with priority `—` meanwhile.
- **Boundaries:** what the product must not do for this persona (A: predict
  demand, give prices, stand in for fieldwork. B: store their credentials,
  mix their data with another customer's, act without showing what it did).

Plus an **evidence log**: when, source, what happened, which persona. Append
only. A persona's tag is upgraded when evidence arrives.

## Minimum for each promise

| Claim (as written) | Where it appears | Persona(s) | Since |
|---|---|---|---|

Copy the claim verbatim. The fit review checks it against `app/capabilities.md`
and `app/boundaries.md`, and paraphrase hides the problem. When the site lives
in this repo, "where it appears" is the page source path, which lets orient's
step 4 flag a promise as changed when its page changes.

---

## Intake: running it

1. **Look before asking.** Search the business folder for existing personas,
   JTBD studies, positioning docs, decks, meeting notes and customer signals.
   Use orient step 5 to decide which ones govern.

   ```bash
   grep -rliE "persona|jobs.to.be.done|JTBD|ICP|segment|positioning|pitch|tagline" \
     --include=*.md --include=*.mdx . | grep -v node_modules | head -40
   # website repo: the pages are where promises live
   find . -path ./node_modules -prune -o \( -path "*/pages/*" -o -path "*/content/*" \) \
     \( -name "*.astro" -o -name "*.md" -o -name "*.mdx" -o -name "*.tsx" \) -print 2>/dev/null | head -40
   ```

2. **Build from what governs, and tag honestly.** A persona that appears only
   in a positioning brainstorm is Inferred, however confident the prose is. A
   customer quote in meeting notes is Real evidence, so log it.
3. **Record what's missing as items. Don't stop to ask.** Each gap becomes a
   `clarify` item in `decisions.md`, phrased as an answerable question:
   - "Is C2 `now`, `later` or `vision`?"
   - "Should C3's intended journey be drafted from the persona and meeting
     notes, or described by the business side?"
   - "The site claims 'validated insights'. Where else does this appear?"

   Carry on with a labelled assumption. At the end of the run, surface the
   three highest-weight open items so the user can answer if they want to.
4. **Drafts are allowed, and always labelled.** You may draft a missing input
   from the materials or the received `app/`. Mark every drafted section:

   ```text
   > **Unconfirmed:** drafted by product-pass from <sources>. See D-NNN.
   ```

   The banner is information, not a gate. The draft is used in fit reviews
   right away. Adopting it is a `confirm` item in `decisions.md`.

   An unconfirmed section can be reviewed for fit. Its findings are labelled
   unconfirmed and ranked below confirmed ones.
5. **Keep the business half free of product facts.** Personas and intended
   journeys describe needs, not features. "Needs to compare two versions" is
   right. "Uses the Comparison view" is wrong. That mapping belongs to fit.

## Unabsorbed material

Orient step 4 lists new business material since the last intake. For each one,
decide whether it changes a persona, a journey, a promise, or the evidence
log. Propose the change and don't apply it silently. A new customer signal
usually means an evidence-log row and maybe a tag upgrade. A new deck usually
means new promises.
