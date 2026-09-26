# Discovery: derive this project's design truth

Run this in Movement 0, every time, in every project. It takes a few minutes and
it is the difference between designing for the product in front of you and
designing for one you imagined.

Work through the six steps, then write the summary at the end. Nothing here is
assumed from a previous project.

---

## 1. Find the frontend and its stack

```bash
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
# candidate frontend roots, most specific first
find . -name package.json -not -path "*/node_modules/*" -maxdepth 4 | head -10
# what is it built with?
for p in $(find . -name package.json -not -path "*/node_modules/*" -maxdepth 4 | head -5); do
  echo "── $p"; grep -oE '"(react|vue|svelte|@angular/core|solid-js|preact|next|nuxt|astro|remix|vite|tailwindcss|styled-components|@emotion/react|sass|@mui/material|@chakra-ui/react|bootstrap|lucide-react|@radix-ui/[a-z-]+)"' "$p" | sort -u | tr '\n' ' '; echo
done
```

Not a JS project? Look for the equivalent: `*.templ`/`templates/` (Go), `app/views`
(Rails), `templates/` + `static/` (Django/Flask), `resources/views` (Laravel),
`*.razor` (Blazor), or plain `*.html` + `*.css`. The method below does not change.

Note whether a **component library** is present (MUI, Radix, Chakra, shadcn,
Bootstrap). If one is, its conventions usually outrank your preferences, and
"add a dependency" is almost always the wrong answer.

## 2. Find the real design tokens

Tokens are wherever this project actually keeps them. Look, in this order, and
stop at the first that is clearly in use:

```bash
# CSS custom properties / Tailwind v4 @theme
grep -rlE "@theme|--color-|--bg-|:root\s*\{" --include=*.css --include=*.scss . \
  --exclude-dir=node_modules --exclude-dir=dist --exclude-dir=build | head -10
# Tailwind v3 config
ls tailwind.config.* 2>/dev/null
# JS/TS theme objects, design-token files
find . \( -iname "theme.*" -o -iname "tokens.*" -o -iname "*design-system*" -o -iname "variables.*" \) \
  -not -path "*/node_modules/*" | head -10
```

Read the winner and write down the actual palette, type scale, spacing, radii
and fonts. **Copy values; do not approximate.**

Then check how faithfully the codebase uses them — this is often the single most
valuable measurement in the whole audit:

```bash
# hardcoded hex outside the token file
grep -rhoE "#[0-9a-fA-F]{6}\b" --include=*.tsx --include=*.jsx --include=*.vue \
  --include=*.svelte --include=*.css src app 2>/dev/null | sort | uniq -c | sort -rn | head -15
# framework default palettes leaking past the tokens (Tailwind shown; adapt per stack)
grep -rhoE '\b(bg|text|border|from|to)-(slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-[0-9]{2,3}' \
  --include=*.tsx --include=*.jsx --include=*.vue --include=*.svelte src app 2>/dev/null \
  | sed -E 's/^[a-z]+-//; s/-[0-9]+$//' | sort | uniq -c | sort -rn | head
```

A long tail of stock palette names beside a defined brand means there is **no
semantic token layer**, so every component invents its own. That is a chokepoint
finding: fix the class, not the instance.

## 3. Find the real surfaces

```bash
# explicit route config
grep -rlE "createBrowserRouter|<Route|useRoutes|defineRoutes|routes\s*[:=]|createRouter" \
  --include=*.ts --include=*.tsx --include=*.js --include=*.vue src app 2>/dev/null | head
# file-based routing
ls app/ pages/ src/routes/ src/pages/ 2>/dev/null | head -30
# component inventory by weight — where the complexity actually lives
find src app -name "*.tsx" -o -name "*.jsx" -o -name "*.vue" -o -name "*.svelte" 2>/dev/null \
  | grep -v -E "\.(test|spec|stories)\." | xargs wc -l 2>/dev/null | sort -rn | head -20
```

Line count is a crude proxy for complexity, but the top of that list is reliably
where the design debt is.

## 4. Find the project's rules and vocabulary

```bash
ls AGENTS.md CLAUDE.md CONTRIBUTING.md README.md 2>/dev/null
find . -maxdepth 2 \( -iname "DESIGN*.md" -o -iname "*STYLE*.md" -o -iname "*BRAND*.md" \
  -o -iname "CONTEXT.md" -o -iname "GLOSSARY.md" -o -iname "*UIUX*" \) \
  -not -path "*/node_modules/*" 2>/dev/null
ls docs/ 2>/dev/null | head -20
```

Read anything that names: a brand constraint, a directory you must not touch, a
test command, a glossary, a commit convention, a deploy consequence. **These
outrank this skill's defaults.**

A glossary with "avoid this word" entries is a design constraint, not a style
note — the distinctions it protects usually have visible counterparts on screen.

## 5. Decide which design document actually governs

**This is the step that goes wrong, and it goes wrong expensively.** A repo can
easily contain three design documents describing three different products:

- a **vendored, forked or overlaid upstream** whose design docs describe the
  engine, not the product you were asked to change;
- a **superseded** system from a rewrite that nobody deleted;
- a **sibling surface** — the marketing site's brand guide sitting next to the app;
- an **aspirational** doc describing an unbuilt redesign.

For each design document found in step 4, ask three questions:

1. **Whose product does it describe?** Check its title, its frontmatter, and the
   stack it assumes. A doc describing "no build step, vanilla JS, three panels"
   does not govern a React SPA, whatever directory it sits in.
2. **Do its values appear in the running code?** This is decisive. Compare its
   palette and fonts against the tokens from step 2 and against what the browser
   computes. A design doc whose colours appear nowhere is documentation of
   something else.
3. **When did it last change, relative to the code?**
   `git log -1 --format=%ai -- <doc>` against `git log -1 --format=%ai -- <frontend>`.

```bash
for f in $(find . -maxdepth 2 -iname "DESIGN*.md" -o -maxdepth 2 -iname "*STYLE*.md" 2>/dev/null); do
  echo "── $f  (last touched $(git log -1 --format=%ai -- "$f" 2>/dev/null))"; head -12 "$f"; done
```

Then write the table explicitly, before designing anything:

| Source | Whose design it describes | Authority here |
|---|---|---|

**The running code wins over any document.** Tokens in use beat tokens written
down. If a document and the rendered app disagree, that gap is itself a finding
— report it, and do not silently pick a side.

**If the user says "follow <doc>" and you have reason to think it governs a
different product, say so once in a sentence and ask.** This is the one question
always worth asking, because getting it wrong wastes the entire session.

## 6. Find how to run and test it

```bash
sed -n '/"scripts"/,/}/p' package.json 2>/dev/null
ls Makefile justfile Taskfile.yml docker-compose*.yml 2>/dev/null
grep -rhoE "localhost:[0-9]{4,5}|127\.0\.0\.1:[0-9]{4,5}" \
  README.md Makefile package.json vite.config.* next.config.* 2>/dev/null | sort -u | head
```

Record: the dev command, the port the **app you care about** serves on, the test
command for the frontend layer specifically, and whether the app requires auth.

If several ports are involved, be sure which one is the surface under design. A
repo that runs more than one server will happily show you the wrong product on
the wrong port, and it will look plausible.

---

## Write the orientation summary

Six lines, before any design work:

```text
Frontend root:  <path>
Stack:          <framework, styling, component lib, icons>
Tokens:         <file> — <palette / type / spacing in brief>
Token fidelity: <how consistently they are used; stock-palette leakage>
Surfaces:       <route pattern, the main ones, where the weight is>
Governing doc:  <which, and which others were ruled out and why>
Rules:          <project constraints that bind this work>
Run / test:     <command, port, auth?> / <frontend test command>
```

Carry this into every later movement. When something contradicts it, the
contradiction is a finding.
