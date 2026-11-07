---
name: website-copy-builder
description: Runs the 9-stage website copy workflow (intake, audience, benchmark, offer, positioning and voice, SEO, site structure, page copy, QA). Keeps one brief.md that the user sees after every change, turns every piece of feedback into a tracked requirement, and moves on only when each stage's quality check meets its goal and the user approves.
---

# Website Copy Builder (orchestrator)

## Goal
Take a project from first contact to an approved copy deck by running the nine stages in order, each one starting from a brief the user has seen and approved.

This skill only sequences and holds the rules every stage shares. Each stage is its own skill with one goal, its own questions, guardrails, quality check and gate. Load it with the Skill tool and follow it; do not redo its work here.

## Shared rules (identical in every website-copy skill)
**Questions.** One question per message, with AskUserQuestion: 2 to 4 options, the recommended reply first with its label ending in "(Recommended)", and no "Other" option (the user can always type their own answer). Name the item inside the question so it reads on its own, and build the options from the brief so one click answers. For facts only the user knows, offer "I'll type it now", "I don't know yet: mark it [TO VERIFY]" and "Skip this item". Without AskUserQuestion, ask in plain text with numbered replies, the recommended one first.

**The brief.** `brief.md` lives where its `Project folder:` line (second line) says: a folder on the user's computer, the claude.ai Project attached to the chat (Projects tool: `project_read`, `project_write`), or this chat only. The `analysis/` and `pages/` files live in the same place (as Project docs when the Project is the location). Read the latest version just before writing, change only the sections this skill owns plus rows of `## 10. Feedback register`, write the whole file back, then read it back to confirm. Never say "saved" without that read. If the brief belongs to a different business than the one the user names, do not touch it: start a new brief. Before saying a file cannot be read or written, try every file tool available in the session.

**The user sees every change.** After every change to `brief.md`, share it in the chat so the user can read it inside Claude: send the file with SendUserFile (display: render) with one line saying what changed, then ask one question: "Approve this version and continue (Recommended)" or "Change something". Wait for the answer. One share per change: never group several changes into one share, never skip a share to save time, and never continue past an unanswered checkpoint.

**Feedback becomes a requirement.** Whenever the user asks for a change (a tone, a value, the mission, a fact, a claim, a page, a word to avoid), first add it to `## 10. Feedback register` as one row: ID (R1, R2…), date, stage, the user's own words, type (voice, value, mission, fact, claim, offer, structure, copy, location, other), the sections and pages it affects, status `open`. Then apply it and set `applied`. Only the quality check sets `verified`, after comparing the output with the user's words. Every later stage re-checks the requirements that touch its own output. A requirement is never dropped silently: if it conflicts with a guardrail (for example a claim that cannot be proven), say so and ask.

**Quality check.** Run the checklist at the end of this file before the gate. Record each item as pass or fail with one line of evidence in this stage's analysis file, and show the user the result in a compact table. Check every number (counts, lengths, limits) by counting or with a script, never by eye. Fix a fail before the gate; if only the client can fix it, list it as open and let the user decide at the gate. The goal item comes first: if it fails, the stage is not done.

## The stages
| # | Skill | Goal of the stage | Owns in `brief.md` | Gate |
|---|---|---|---|---|
| 1 | `site-copy-intake` | A sourced picture of the business, its claims, voice references, tools, regions and languages | 0, 1, 2 and the `Project folder:` line | Approval of the business analysis |
| 2 | `site-copy-audience` | Evidence about the buyers: pains in their words, objections, personas per language | 3, and the Audience cell of section 2 rows marked "audience not given" | Light check |
| 3 | `site-copy-benchmark` | What to borrow, avoid and differentiate on, from 5 to 8 researched sites plus the user's own benchmarks (documents, pasted notes or links) and what they like about each | 4 | Approval of the conclusions |
| 4 | `site-copy-offer` | An offer the client can deliver and stand behind | 5 | Client approval |
| 5 | `site-copy-positioning` | One provable promise and a voice, grounded in a voice benchmark | 6 | Approval after each round |
| 6 | `site-copy-seo` | Each page mapped to real searches per language, with data strength stated, and how often the location appears in the copy (geo-localization), recommended and confirmed by the user | 7 (except the Assigned page column) | Reviewed at the IA gate |
| 7 | `site-copy-ia` | A structure where every page has a goal and every section answers a visitor question from the brief | 8, and the Assigned page column of 7 | Explicit approval |
| 8 | `site-copy-pages` | Every approved page written in every offered language, shown in the wireframe | 9 (progress and assumptions) and the `pages/` files | Approval after each page |
| 9 | `site-copy-qa` | Accurate, consistent copy, delivered as one deck | 9 (status) and the deck | Final approval |
| all | every stage | | rows of 10 (add, update status) | |

## How to run
1. **Where to save, first.** If the location is not known, ask: "Where should this project be saved?" with "A folder on my computer (Recommended)" when the computer can be reached, "A custom folder path I type", "The claude.ai Project attached to this chat" when one is attached, "Just in this chat". For a folder, ask the exact path as a separate question, check that it exists, and request access to that folder only. For chat only, say once that the brief will not carry over to a new chat.
2. **Find the brief there**, and in the attached Project. If one exists, read its business name and status line and ask: "This brief is for [business]. Continue it, or start a new project for another business?" with "Continue (Recommended)" and "New business". Never write to a brief for a business the user did not name. On "Continue", resume from the first stage whose gate is not cleared and share the brief.
3. **No brief:** create it from the skeleton below, with the `Project folder:` line filled, and share it.
4. Tell the user in one line: nine stages run on their real project; the brief is shared after every change; every change they ask for becomes a tracked requirement; each stage ends with a quality check against its goal; any stage can be run alone later.
5. **Run the stages in order.** A stage is finished only when: its quality check ran and its goal item passed (or the user accepted named open items at the gate); every requirement touching it is `verified`; the status line is updated; the brief was shared and approved. Then say in one or two lines what was produced, the quality check result, and what comes next.
6. Do not start the next stage while a gate is open. Do not start `site-copy-pages` until `## 8` is marked `approved`.
7. The user can skip, repeat or reorder stages: say what a skipped stage would have fed, and continue only if they confirm.
8. If a stage skill is missing, say which, and offer to do that stage from its row above or to stop until it is installed.
9. At the end, run the project quality check below.

## Guardrails (all stages)
- Every run is a real client project. There is no test, trial or demo mode: never label a stage, gate, approval or brief as a test, never skip or soften a step because a project seems to be a trial, and record a missing fact as `[TO VERIFY]`, never as a test value.
- The business's place (city, region, country) appears in the copy only at the geo-localization level the user confirmed in section 7, in the places the site structure assigns: never more often, never in a heading unless the level is "headings", and never a place section 1 does not source.
- The audience drives every decision: each page serves one persona at one awareness level, with one goal and one primary action.
- No default page skeleton: each page's sections come from its goal and the visitor's questions, each answered from the brief, in the layout that fits the answer.
- Every claim in the copy traces to a source in the brief. No source: `[TO VERIFY]` in the brief, a highlighted assumption in the copy.
- Guarantees, scarcity and urgency appear only if the client approved them, they are true, and they are lawful in the regions of section 2.
- Claims marked "do not use" or restricted in section 1 never appear in copy, page names, menus or keywords.
- Be honest: say so when the context is thin, the offer is weak, the positioning space is crowded or search demand is low.
- Every language in section 2 is a real language of the site and is written natively, not translated. A language with no known audience is researched or limited at the site structure gate, never silently.
- Regions come only from section 2. Do not suggest markets the client did not choose.
- LinkedIn is never fetched or browsed: only a PDF export or pasted text.
- `jtbd-research` and `market-size-research` are not used.
- Never shorten a step the user is meant to see (a shared brief, a question, a gate) to save time.

## Quality check (orchestrator)
At the end of each stage:
| Item | Pass when |
|---|---|
| Goal of the stage | The stage's own quality check ran and its goal item passed, or the user accepted the named open items at the gate |
| Brief visible | The brief was shared after every change in the stage, and the last version was approved |
| Requirements | Every row of section 10 that touches this stage is `verified`; none is `open` without a decision from the user |
| Order | No stage started before the previous gate; page copy did not start before the IA was approved |
| Status | The status line names the stage and its gate result |

At the end of the project: all nine gates cleared; every requirement in section 10 `verified`; every assumption in the deck says what the client must confirm; the deck exists and was read back.

## Brief skeleton
```
# Website copy brief
Project folder: (not set)
Status: Stage 1 (intake) not started
Last updated:

## 0. Sources
| Source | Type (site / doc / LinkedIn PDF / pasted / voice reference / other) | How obtained | Notes (pages not readable) |
|---|---|---|---|

## 1. Business analysis
- Business name:
- Mission:
- Vision:
- Offer(s) (what, for whom, delivery, price level):
- Differentiators (stated by the client):
- Audience needs:
- Proof points (each with source):
- Offer raw material (time to first result, effort asked of the buyer, capacity, existing guarantee, reusable assets):
- Constraints (legal, brand, tone, deadlines, things to avoid):
- Primary conversion goal (one action) and smaller steps:
- Voice references (links, posts, brands, the client's own writing) or voice preference (3 adjectives, formality, words to avoid):
- Location (where the business is based: city, province or region, country; in person or remote; markets it also serves beyond the site's target regions):
- Unknowns / [TO VERIFY] (conflicting figures listed with both sources):
### Claims
| Claim the client wants to make | Status (provable / needs evidence / do not use) | Source or evidence needed | Reason |
|---|---|---|---|
### Third-party tools
| Tool | Type | Purpose on the site | Status (in use / planned / to choose) | Account exists | Languages and RTL supported | Notes (consent, cost, data) |
|---|---|---|---|---|---|---|

## 2. Regions and languages
| Priority | Region | Language | Locale | Audience (or "audience not given") | Notes (RTL, formality, variant) |
|---|---|---|---|---|---|

## 3. Audience and competitors
- Market context (direction only, dated sources):
- Evidence strength per language:
### Pain themes
| Theme | Value driver (outcome / likelihood / time / effort) | Phrase (original language) | Verbatim or snippet | Source URL | Date |
|---|---|---|---|---|---|
### Fears and objections
| Objection | Persona | Evidence (source) or "assumption" |
|---|---|---|
### Personas
| Persona (role + segment) | Region/language | Awareness level on arrival | Goal | Trigger | Pain | Objections | Where they search | Evidence |
|---|---|---|---|---|---|---|---|---|
### Competitors
| Name | Type (direct/indirect/alternative) | Core offer | Price level | Target segment | USP | Proof types | Guarantee | Contact model | Languages |
|---|---|---|---|---|---|---|---|---|---|

## 4. Benchmark
| Business | Source (research / user) | Region/language | Type | Positioning | Site structure | Headline pattern | CTA pattern | Proof used | Tone | SEO focus | Location use | Offer elements | Gaps | What the user likes / dislikes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
- Borrow:
- Avoid:
- Differentiate:
- Benchmarks shared by the user (document, pasted notes or links), with what they like and dislike about each:

## 5. Offer
Status: not started / proposed / approved
- Value equation scores (client vs competitors):
- Dream outcome:
- Obstacle → solution list:
- Core offer (stack):
- Bonuses:
- Risk reversal (client-approved only):
- Scarcity / urgency (real only):
- Offer name:
- Decisions left to the client:

## 6. Positioning and voice
- Core promise:
- Positioning statement:
### Message pillars
| Pillar | Claim | Proof | Objection answered | Pages |
|---|---|---|---|---|
### Voice benchmark
| Example | Language | Source (URL and date, or "user provided") | Why it fits | Patterns to borrow | Patterns to avoid |
|---|---|---|---|---|---|
- Voice rules (3 traits, each with the benchmark pattern it comes from, and sounds like / does not sound like per language):
- Formality and sentence length target per language:
- Use / avoid vocabulary:
- Per-language notes:

## 7. SEO plan
- Data strength (sources, dates, measured or estimated):
| Priority | Cluster | Language/region | Primary keyword | Intent | Weight /20 | What ranks today | Secondary keywords | Role (target / supporting / answer) | Assigned page |
|---|---|---|---|---|---|---|---|---|---|
- Dropped terms and why:
- Thin-demand warning and cheap channels:
- Languages flagged (no audience or no measurable demand):
- URL and hreflang strategy:
### Geo-localization
| Language | Level (headings / body / contact and footer / not mentioned) | Places named, as written | Markets also served, named in copy? | Reasons (evidence) | Decided by the user on |
|---|---|---|---|---|---|

## 8. Information architecture
Status: not started / proposed / approved
(sitemap tree)
| Page | Slug per language | Nav | Persona | Awareness level | Page goal | Keyword cluster | Primary action | Third-party tools | Languages |
|---|---|---|---|---|---|---|---|---|---|
### Section plan (one table per page, after its goal)
| # | Visitor question | Answer in the brief | Type and variant | Why this layout and position |
|---|---|---|---|---|
### Journey per persona
### Objection map
| Objection | Page | Section | Proof used |
|---|---|---|---|
### Tool placement
| Tool | Page(s) | Section | How it appears (embed / pop-up / link) | Fallback if it does not load | Language or RTL issue |
|---|---|---|---|---|---|
### Location mentions
| Page | Language | Element (title / H1 / H2 / H3 / body / contact / footer / meta / schema) | Wording |
|---|---|---|---|
- Navigation (main, footer, language switcher):
- Pages left out and why:

## 9. Copy progress
| Page | Language | Status (todo / draft / cold-read / approved) | Target words | Final words | Open flags |
|---|---|---|---|---|---|
### Assumptions
| Page | Item | Value used | What the client must confirm |
|---|---|---|---|

## 10. Feedback register
| ID | Date | Stage | User's words | Type | Affects (sections, pages) | Status (open / applied / verified) | Verified how |
|---|---|---|---|---|---|---|---|
```
