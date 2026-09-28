# The Hook Model, and the research that checks it

A **habit** is a behavior done with little or no conscious thought, cued by a
situation. A **hook** is an experience designed to connect the user's
problem to the product often enough to form one. Nir Eyal's *Hooked: How to
Build Habit-Forming Products* (2014, revised 2019) describes the hook as a
loop of four phases:

```text
  Trigger ──▶ Action ──▶ Variable reward ──▶ Investment
     ▲                                          │
     └────────── loads the next trigger ────────┘
```

Each pass through the loop makes the next one more likely. Over enough
passes, the external trigger stops being needed: the user's own feeling sends
them to the product. That's the habit.

Throughout, examples come from two kinds of product, the same archetypes the
product contract uses:

- **A, output product:** the user gets something generated, like a reading
  of how audiences in different countries react to a post before it's
  published. Persona C1 checks a post before publishing (J-C1-1).
- **B, platform product:** the user gets a place to work, like an agent
  workspace connected to their inbox. Persona T2 lets an agent triage the
  inbox (J-T2-1).

---

## 1. Trigger

What cues the behavior. Two kinds.

**External triggers** carry the information about what to do next inside the
trigger itself.

| Type | Is | Earns attention by | A | B |
|---|---|---|---|---|
| **Paid** | Ads, search marketing | Money. Expensive to repeat | A search ad for "check post tone" | An ad for "inbox agent" |
| **Earned** | Press, app store features, word of mouth at scale | Reputation. Short-lived | An article on culture gaffes | A review listing it |
| **Relationship** | One person telling another, an invite, a shared result | The relationship. Viral when the product is worth telling about | A colleague forwards a read | A teammate invites them to the workspace |
| **Owned** | Something that occupies the user's space by their consent: an icon, a digest, a notification they opted into | The user's choice to keep it | A weekly "posts you checked" email | The Monday triage summary |

Paid and earned triggers acquire users. Relationship and owned triggers bring
them **back**. Owned triggers only work after the user has opted in, which
is why the investment phase matters (section 4).

**Internal triggers** are associations in memory, usually with an emotion or
a situation. Negative feelings are the most frequent: boredom, loneliness,
frustration, confusion, indecision, fear of missing or getting something
wrong. When the product relieves the feeling reliably, the feeling itself
becomes the cue.

The design question is: **what is the user feeling, just before the moment
we want them to act?** Not what they want to do. What they feel.

| | Internal trigger | Where it comes from in the contract |
|---|---|---|
| A | "I'm about to publish and I'm not sure how this lands in a market I don't know." Fear of looking careless. | C1's Problem ("which makes me feel…"), emotional job, Stakes |
| B | "It's Monday and I'm already behind." Overwhelm, and fear of missing a client. | T2's Trigger ("200 unread"), Problem, Stakes |

Probes:

- What feeling precedes the trigger moment in the persona's words? Is it
  Real, or guessed?
- Which external triggers does the product send today, and which internal
  trigger does each one point to? One that points to none is noise.
- Does the external trigger arrive **at** the moment the internal trigger
  happens, or at a time that suits the product?

## 2. Action

The simplest behavior done in anticipation of a reward. Eyal builds on BJ
Fogg's Behavior Model: **a behavior happens when motivation, ability and a
trigger (Fogg now says prompt) converge at the same moment**. Fogg writes it
**B = MAP**. When a prompt arrives and the behavior doesn't happen, either
motivation or ability was too low.

**Motivation** has three core pairs: seeking pleasure and avoiding pain,
seeking hope and avoiding fear, seeking acceptance and avoiding rejection.

**Ability** is simplicity, and simplicity is a function of the **scarcest
resource at that moment**. Six elements:

| Element | Asks | A | B |
|---|---|---|---|
| **Time** | How long does it take? | Paste and read in under a minute | First result under 5 minutes |
| **Money** | What does it cost, now? | Free for the first posts | No card before the first triage |
| **Physical effort** | How much work? | Paste, not retype | Connect once, not per session |
| **Brain cycles** | How much thinking? | Audiences remembered | Plain-words request, no rule builder |
| **Social deviance** | Does it clash with what others do? | Checking isn't seen as "not knowing the market" | The team accepts delegating mail |
| **Non-routine** | How far is it from what they already do? | Happens inside the publishing routine | Happens where they already read mail |

Increase ability before motivation. Motivation is expensive and fades.
Ability, once built, stays.

Heuristics that raise motivation or ability, with their ethics condition
(`ethics.md` has the pattern list):

| Heuristic | Means | Honest when |
|---|---|---|
| **Scarcity** | Rare looks valuable | The scarcity is real |
| **Framing** | Context changes perceived value | The frame is true |
| **Anchoring** | The first number seen sets the reference | The anchor is a real option |
| **Endowed progress** | People persist when they feel they've started (Nunes and Drèze, 2006) | The progress is real work already done |
| **Defaults** | People keep what's preselected | The default is what most of them would choose |

Probes:

- In the actual journey, what's required before the first reward? Count it.
- Which of the six elements is scarcest for this persona **at the trigger
  moment**? Remove that one first.
- Does the action happen inside a routine the persona already has, or does
  it ask for a new one?

## 3. Variable reward

A reward relieves the itch that the trigger created. **Variability** is what
makes it compelling: the brain's anticipation system responds most to
rewards it can't fully predict. A fixed reward satisfies. A variable one
creates wanting.

Three kinds:

| Kind | The user seeks | A | B |
|---|---|---|---|
| **Tribe** | Social rewards: acceptance, recognition, belonging | A colleague agrees the flagged line was risky | A client thanks them for a fast reply |
| **Hunt** | Resources and information | Which audience reads it differently this time, and why | What the agent found in the pile |
| **Self** | Mastery, competence, completion, control | Fewer flags over time: they're getting better at it | Inbox at zero, rules working |

What the book asks of a reward:

- **It answers the job.** A reward unrelated to why the user came feels like
  a trick. The best variability comes from the content of the job itself: a
  different post reads differently, a different Monday has different mail.
- **It ends the search.** The user finds what they came for, then leaves.
  A reward that never finishes becomes compulsion (`ethics.md`).
- **It keeps autonomy.** People resist being pushed. Saying "you are free to
  choose" increases compliance. Self-determination theory (Deci and Ryan)
  agrees: autonomy, competence and relatedness sustain motivation.
  Controlling rewards (points for doing what they'd do anyway) can crowd out
  the intrinsic kind.
- **Finite vs infinite variability.** A reward that becomes predictable with
  use (a game finished, a feed exhausted) loses its pull. One that stays
  variable because users or the world keep producing it lasts.

Probes:

- Which of tribe, hunt and self does the persona seek, from their emotional
  and social jobs?
- Where does the reward's variability come from: the job's content, or a
  mechanic added to it?
- Does the user know when they're done?

## 4. Investment

The user puts something into the product that makes it better for them next
time. Investment comes **after** the reward, when the user feels they've
received something, not before.

**Stored value** is what the investment builds:

| Stored value | A | B |
|---|---|---|
| **Data** | Saved audiences, brand voice notes | Connected accounts, triage rules |
| **Content** | A history of checked posts and their reads | An archive of what the agent did |
| **Followers and connections** | Colleagues sharing reads | Teammates in the workspace |
| **Reputation** | Being the one who "checks" in their team | Clients trusting the reply speed |
| **Skill** | Knowing how to read the flags | Knowing how to phrase requests |

Stored value raises the cost of leaving and the value of staying. Three
effects explain why: **the IKEA effect** (people value what they helped make,
Norton, Mochon and Ariely, 2012), **commitment and consistency** (people act
in line with what they did before), and **cognitive dissonance** (having
invested, they value the product more).

**Loading the next trigger.** The investment should set up the next pass:
the audiences saved today make the next check one step shorter; the triage
rule written today produces Monday's summary. An investment that loads no
trigger is storage, not a hook.

Probes:

- What does the persona leave behind after the reward, and is it asked for
  after the reward, not before?
- Which investment makes the next pass easier or better?
- Which investment creates the next external trigger (an owned trigger the
  user asked for)?

---

## 5. The habit zone

Eyal plots behaviors by **frequency** against **perceived utility**. A
behavior becomes a habit when it's frequent enough, or useful enough, that
the user stops deliberating. Infrequent behaviors need very high utility to
become habits at all. Most products that aim for a habit need at least weekly
frequency. `habit-potential.md` turns this into a verdict per persona.

**Vitamins and painkillers.** A painkiller relieves a felt pain and is needed
now. A vitamin is nice to have. Habit-forming products start as vitamins
and become painkillers: once the habit forms, not using the product itself
creates the itch.

---

## 6. Beyond the book: what the habit research adds

The Hook Model is a design frame. It was synthesized from practice and
research, not tested as a whole. These findings refine it. Use them as
checks.

| Finding | Source | What it changes in the review |
|---|---|---|
| Habits form from **repetition in a stable context**. The cue is a place, a time, a preceding action or a person, more than a feeling alone | Wood and Neal (2007), Wood, Tam and Witt (2005) | Tie the trigger to a stable moment in the persona's Rhythm. A random-time notification builds less habit than one at the same moment each week |
| When the context changes, the habit breaks | Wood, Tam and Witt (2005): students who changed university | Journeys that change entry point, device or time break the loop. Watch redesigns |
| Anchor new behaviors to an existing routine: "After I…, I will…" | Fogg, *Tiny Habits* (2019) | Every habit hypothesis names the moment it follows |
| Forming a habit took a median of 66 days, ranging 18 to 254. Missing one day didn't derail it | Lally et al. (2010) | Habit tests run for weeks, not days. Punishing a missed day (a streak reset) isn't needed and costs goodwill |
| Autonomy, competence and relatedness sustain motivation. Controlling rewards can undermine it | Deci and Ryan, self-determination theory | Maps to self, hunt and tribe. Prefer rewards the user would seek anyway |
| Losses weigh roughly twice as much as equal gains | Kahneman and Tversky, prospect theory | Explains why loss-based retention works, and why it fails the Regret Test so often (`ethics.md`) |
| Friction breaks habits as well as preventing them | Wood (2019), *Good Habits, Bad Habits* | To displace the habit in Today they…, make the old path harder only where the user wants it, and the new one easier |

## 7. Sources

- Eyal, N. with Hoover, R. (2014, revised 2019). *Hooked: How to Build
  Habit-Forming Products.* Portfolio / Penguin.
- Eyal, N. (2018). "Want to design user behavior? Pass the Regret Test first."
- Fogg, B. J. (2009). A behavior model for persuasive design. *Persuasive
  '09.* And (2019), *Tiny Habits.* Houghton Mifflin Harcourt.
- Wood, W. and Neal, D. T. (2007). A new look at habits and the habit–goal
  interface. *Psychological Review.*
- Wood, W., Tam, L. and Witt, M. G. (2005). Changing circumstances,
  disrupting habits. *Journal of Personality and Social Psychology.*
- Wood, W. (2019). *Good Habits, Bad Habits.* Farrar, Straus and Giroux.
- Lally, P. et al. (2010). How are habits formed: modelling habit formation
  in the real world. *European Journal of Social Psychology.*
- Deci, E. L. and Ryan, R. M. (2000). Self-determination theory and the
  facilitation of intrinsic motivation. *American Psychologist.*
- Kahneman, D. and Tversky, A. (1979). Prospect theory. *Econometrica.*
- Nunes, J. C. and Drèze, X. (2006). The endowed progress effect. *Journal
  of Consumer Research.*
- Norton, M. I., Mochon, D. and Ariely, D. (2012). The IKEA effect. *Journal
  of Consumer Psychology.*
