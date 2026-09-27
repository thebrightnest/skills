# Definitions: what a good one looks like, and how to coach it

The business half is made of a few kinds of definition. Each has a bar. A
candidate is graded against its bar before the walk (`business-inputs.md`),
and the audit grades confirmed definitions against the same bar
(`fit.md` step 0).

The bar is how you **guide the user**. You don't hand them a template to
fill. You show them their draft, say which test it fails, and ask the one
question that fixes it, with your best guess as the default answer.

| Type | Lives in | One per |
|---|---|---|
| Persona | `business/personas/<ID>.md` | kind of customer, in one situation |
| Job | inside its persona | distinct progress they hire the product for |
| Problem | inside its persona, per core job | job the persona can't get done today |
| Scenario | inside its persona | concrete situation that exercises a job |
| Intended journey | `business/journeys/<persona>.md` | persona × job |
| Promise | `business/promises.md` | public claim, verbatim |
| Positioning | `business/promises.md`, "Positioning" | product, or product line |

Grades:

| Grade | Means | In the walk |
|---|---|---|
| **passes** | Meets every test | Offered for a one-word yes |
| **weak** | Fails one or two tests, fixable by the user in a sentence | Shown with the failing test and one question |
| **fails** | Fails the core test, or is invented | Shown with why. Default answer: drop or rewrite |

A candidate built only from model-written sources can be **passes** in
shape and still carry `Inferred`. Grade and evidence are separate. The grade
says whether it's well formed. The tag says whether it's true.

---

## Persona

**Is:** a kind of customer in one situation, recognisable to someone who
knows them. **Is not:** a demographic profile, a job title, or several
situations merged because one person holds them all.

| Test | Fails when |
|---|---|
| **Recognisable** | A customer couldn't say "that's me". "Marketing manager" alone fails |
| **One situation** | Its jobs have different triggers, material and stakes that never meet. That is two personas, or variants |
| **Behaviour, not demographics** | Age, location or seniority appear without saying why they change a need |
| **Earned size** | It has more jobs, needs or scenarios than its evidence supports. One real conversation doesn't earn five jobs |
| **Evidence per claim** | A Real tag covers the existence of the persona, but the depth fields are unmarked guesses |

Coaching questions:

- "Who is the one real person closest to this? What did they say?"
- "These jobs start from different moments. Is it one person doing both, or two personas?"
- "Which of these would you defend in front of that customer? The rest can stay staged."

| | Weak | Passes |
|---|---|---|
| A, output product | "Marketing manager, 30–45, owns strategy, planning and content" | "A marketing manager posting to audiences in several cultures from one small team, with nobody local to ask" |
| B, platform product | "SMB owner who wants automation" | "An agency owner whose inbox is the client queue, who has to show clients what was sent on their behalf" |

## Job

**Is:** progress the persona wants in a situation, free of any solution.
**Is not:** a feature, a task in the product, or a wish for a benefit
("save time").

Shape: `When <situation>, I want <progress>, so <outcome>.` Tag each job:

| Kind | Asks | Example A | Example B |
|---|---|---|---|
| **functional** | What are they trying to get done? | "When a post is drafted, I want to know how each audience reads it, so I don't damage the brand" | "When the inbox is full on Monday, I want the routine replies handled, so I start on client work" |
| **social** | How do they want to be seen, and by whom? | "When my lead questions a post, I want to point to the reason, so I look careful, not lucky" | "When IT asks what the agent can touch, I want a list to forward, so I don't look reckless" |
| **emotional** | What feeling do they seek or avoid? | "I want to stop dreading a post going wrong in a market I don't know" | "I want to stop wondering what was sent while I wasn't looking" |

| Test | Fails when |
|---|---|
| **Solution-free** | The "I want" names a feature, a screen or a mechanic ("a comparison view") |
| **Has a "so"** | There's no outcome, or the outcome restates the want |
| **Specific** | "Be more productive", "make better decisions" |
| **Distinct** | Two jobs differ only in wording, or one is a step of another |
| **Social and emotional, when they drive the choice** | Only functional jobs, while the evidence shows who they answer to or what they fear |

Social and emotional jobs are never invented. They come from a quote, an
observed behaviour, or the user's own account. Otherwise they stay staged.

Coaching questions:

- "Why do they want that? What happens after?" (finds the "so")
- "Who notices when this goes well, or badly?" (finds the social job)
- "How do they feel just before they do this?" (finds the emotional job)

## Problem

**Is:** why a core job can't be done well today, from the persona's side.
**Is not:** a missing feature, a company metric, or a symptom.

Shape:

```text
I am <the persona in its situation>,
trying to <the job's outcome>,
but <the barrier>,
because <the root cause>,
which makes me feel <the emotion, from evidence>.
In one line: <persona> needs a way to <outcome> because <cause>, which today <impact>.
```

| Test | Fails when |
|---|---|
| **No solution smuggled in** | "But there's no tool that…", "because they lack a dashboard" |
| **Root cause, not symptom** | The "because" restates the "but" ("because it's confusing"). Ask "why?" until it names a cause the persona would recognise |
| **The user's problem** | "Churn is high", "revenue is down" |
| **Feeling from evidence** | "Empowered", "delighted", or any feeling nobody said |
| **Checkable** | You couldn't tell whether a product removes the barrier |

The problem is what the fit review judges the product against. A product
can serve a job's steps and still leave its "because" in place. That is a gap
(`fit.md` step 1b).

| | Weak | Passes |
|---|---|---|
| A | "…but there's no cultural review tool, because the market lacks one" | "…but I can't tell how a joke reads outside my culture, because nobody local sees it before it's out, which makes me hold back humour" |
| B | "…but the inbox is slow, because email is inefficient" | "…but I can't delegate replies, because any tool that could needs my password and I can't see what it did, which makes me do it all myself" |

## Scenario

**Is:** one concrete situation that exercises a job, with what the persona
needs to walk away with. **Is not:** a story with an outcome, or a figure
nobody measured.

| Test | Fails when |
|---|---|
| **Concrete** | No material, no audience, no moment |
| **No outcome** | It says what the result was ("concept A wins") |
| **Inside the boundaries** | It asks for what the persona's boundaries or the product's refuse |
| **Sourced** | It has no source, or its only source is a model and the user hasn't recognised it |

One real scenario outweighs five invented ones. Keep only the model-written
scenarios the user recognises as realistic ("yes, that happens").

## Intended journey

The format and its depth check are in `journeys.md`. The bar adds:

| Test | Fails when |
|---|---|
| **Needs, not screens** | A step names a page, a button or a feature |
| **Rateable** | A reviewer couldn't rate a step `match` or `missing` |
| **Traces to a job** | It carries no job ID, or a job it doesn't serve |
| **Earned** | It exists for a job the user hasn't confirmed |

## Promise

**Is:** a public claim, copied verbatim with where it appears. **Is not:** an
intention, or a paraphrase.

| Test | Fails when |
|---|---|
| **Verbatim** | It's reworded, which hides the problem |
| **Checkable** | Nothing in `app/` could back or refute it ("world-class", "seamless") |
| **Located** | No page, deck or document it appears in |

## Positioning

**Is:** who the product is for, the need, the category, the benefit, the
alternative it replaces and the difference. **Is not:** a tagline or a
feature list.

Shape, one row per slot:

| Slot | Text (verbatim) | Points to |
|---|---|---|
| For | … | persona IDs |
| that need | … | job IDs |
| <product> is a | … | a category word in `app/glossary.md` |
| that | … | the benefit, checked like a promise |
| Unlike | … | the persona's **Today they…** |
| provides | … | the difference, checked like a promise |

| Test | Fails when |
|---|---|
| **Someone specific** | "For" matches no persona, or matches only an Inferred one |
| **A real need** | "that need" matches no job |
| **A real alternative** | "Unlike" names a competitor no persona reaches for. Their Today they… says what they actually use |
| **Provable** | The benefit or the difference couldn't be shown with a demo or the product today |

Positioning is a business choice. Record what the sources say, and coach it
with these tests. Never write one from scratch without the user asking for
it.
