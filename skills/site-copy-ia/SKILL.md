---
name: site-copy-ia
description: Proposes the full information architecture of a multi-page website around its audience - sitemap, a journey per persona, a goal and a section plan for every page (each section answering a visitor question from the brief), an objection map, third-party tool placement, navigation, languages per page and the keyword-to-page mapping - and waits for explicit approval. Runs alone or as stage 7 of website-copy-builder.
---

# Site copy: information architecture

Stage 7 of the website copy set. It works alone or inside `website-copy-builder`. This is for a whole website, not a landing page.

## Goal
Agree a site structure in which every page has one goal, and every section on it answers a question the visitor has on the way to that goal, with the answer taken from the brief.

## Shared rules (identical in every website-copy skill)
**Questions.** One question per message, with AskUserQuestion: 2 to 4 options, the recommended reply first with its label ending in "(Recommended)", and no "Other" option (the user can always type their own answer). Name the item inside the question so it reads on its own, and build the options from the brief so one click answers. For facts only the user knows, offer "I'll type it now", "I don't know yet: mark it [TO VERIFY]" and "Skip this item". Without AskUserQuestion, ask in plain text with numbered replies, the recommended one first.

**The brief.** `brief.md` lives where its `Project folder:` line (second line) says: a folder on the user's computer, the claude.ai Project attached to the chat (Projects tool: `project_read`, `project_write`), or this chat only. The `analysis/` and `pages/` files live in the same place (as Project docs when the Project is the location). Read the latest version just before writing, change only the sections this skill owns plus rows of `## 10. Feedback register`, write the whole file back, then read it back to confirm. Never say "saved" without that read. If the brief belongs to a different business than the one the user names, do not touch it: start a new brief. Before saying a file cannot be read or written, try every file tool available in the session.

**The user sees every change.** After every change to `brief.md`, share it in the chat so the user can read it inside Claude: send the file with SendUserFile (display: render) with one line saying what changed, then ask one question: "Approve this version and continue (Recommended)" or "Change something". Wait for the answer. One share per change: never group several changes into one share, never skip a share to save time, and never continue past an unanswered checkpoint.

**Feedback becomes a requirement.** Whenever the user asks for a change (a tone, a value, the mission, a fact, a claim, a page, a word to avoid), first add it to `## 10. Feedback register` as one row: ID (R1, R2…), date, stage, the user's own words, type (voice, value, mission, fact, claim, offer, structure, copy, location, other), the sections and pages it affects, status `open`. Then apply it and set `applied`. Only the quality check sets `verified`, after comparing the output with the user's words. Every later stage re-checks the requirements that touch its own output. A requirement is never dropped silently: if it conflicts with a guardrail (for example a claim that cannot be proven), say so and ask.

**Quality check.** Run the checklist at the end of this file before the gate. Record each item as pass or fail with one line of evidence in this stage's analysis file, and show the user the result in a compact table. Check every number (counts, lengths, limits) by counting or with a script, never by eye. Fix a fail before the gate; if only the client can fix it, list it as open and let the user decide at the gate. The goal item comes first: if it fails, the stage is not done.

## Owns
`## 8. Information architecture` (with its status line `proposed` or `approved`), and the Assigned page column of `## 7. SEO plan`, where the provisional page types are replaced by the final pages. Writes `analysis/07-ia.md`: pages considered and left out with reasons, tool placements considered, every round of changes, open questions with their answers, and the quality check.

## Inputs
Conversion goal, offers, Claims and the Third-party tools table (section 1), regions, languages and audiences (section 2), personas, awareness levels and objections (section 3), benchmark structures (section 4), the offer (section 5), pillars (section 6), keyword clusters and flagged languages (section 7). If the SEO plan is missing, say keyword assignment is pending and recommend `site-copy-seo` next. If there is no Third-party tools table, ask: "Will the site use any third-party tools such as booking, reviews, chat or ticketing?" before planning.

## Method
1. **Start from the conversion goal** and work back: which pages must exist for each persona to reach it?
2. **A journey per persona:** entry point (search term, referral, social) → the page that meets them → what that page must make them believe → the next step, until the conversion goal.
3. **One persona, one awareness level, one job, one primary action per page.** A page serving two personas with different needs is split, or its sections are clearly signposted. Secondary actions support the primary one.
4. **The core offer gets its own page,** built as the offer in section 5; each further offer gets a page if it has its own cluster or audience.
5. **Objection map:** every section 3 objection placed on a page and section with the proof that answers it. An objection with no place or no proof is an open question.
6. **Tools:** for every tool in section 1, the page and section, how it appears (inline embed, button opening a pop-up, link to the tool's page), and what the visitor sees if it fails to load. A tool that performs the conversion goal is the primary action of its page. A review widget sits where the objection map needs proof. Never plan a section showing ratings or counts the client has not provided.
7. **Navigation** grouped by what visitors try to do, 5 to 7 main items, informed by the benchmark. The language switcher links to the equivalent page.
8. **Proof and support pages** where trust is a barrier (case studies, testimonials, about) and where needed (contact, FAQ, legal, privacy), noting which are legally required in the regions. The privacy page lists every tool.
9. **Languages per page.** By default every page exists in every section 2 language. If the audience or SEO stage flagged a language (no known audience, no measurable demand), propose as an option: "Write [language] later, once its audience is confirmed", or limit it to named pages, with the reason. Any language that has pages also has its legal pages. The Languages column is binding for the page copy stage; never leave it empty or write "all" without checking it against section 2.
10. **Location mentions.** Turn the geo-localization level in section 7 into placements, per page and language, in the Location mentions table of section 8: the element (title, H1, H2, H3, body, contact, footer, meta, schema) and the wording. "Headings": the place in the title and H1 of the key pages and in H2 or H3 where it answers a visitor question, plus body, contact and footer. "Body": one or two body sentences on the pages where place answers a question (time zone, language variant, local law, meetings), plus contact and footer; never in a title or heading. "Contact and footer": the contact page and footer only. "Not mentioned": only legally required addresses. Name markets also served only if the decision says so. A place in a heading must not crowd out the primary keyword.
11. **Page plan: goal first, then sections.** There is no default page skeleton. For each page, in this order:
    1. **Set the page goal** in one sentence: who it is for (persona, awareness level), what they must believe or do by the end, and the one primary action.
    2. **List the visitor's questions** on the way to that action, in the order this persona asks them. Take them from the objection map, the persona's trigger and objections, the offer's obstacles and the SEO questions. Problem-aware visitors first need to recognise their situation; solution-aware ones compare approaches; product-aware ones check proof, price, process and risk.
    3. **Keep only questions the brief can answer.** A question with no answer in the brief is an open question for the client, never a section filled with generic text.
    4. **One section per question** (merge two only when one answer covers both). Choose the type and variant from the shape of the answer: options compared on the same attributes → Comparison; a sequence → Process; 2 to 4 parallel points → Feature grid (one column per point); points that each need a visual and an explanation → Feature alternating; a few sourced numbers → Stats; a story or the people behind the business → About; permitted quotes → Testimonial (one strong quote: single; several: cards; none: statement); remaining doubts → FAQ; a question a tool answers (booking, reviews, video) → Tool; permitted client logos → Logos; the final step → CTA (dark banner or bordered box).
    5. **Place the sections in the order of the questions.** The Header answers the first question. It carries the primary action as a button only if the persona can act on arrival; a second button only if it leads to the answer of the very next question; otherwise a text link. The primary action comes back where the last big doubt has been answered.
    6. **Write the plan** in section 8: page goal, then one row per section: visitor question, where the answer is in the brief, type and variant, and why this layout and this position.
    Two pages may share a sequence of sections only with a stated reason. Use only the types and variants the wireframe supports: Header (split, centered, text), Content, About, Feature (grid, list, alternating), Process, Pricing, Comparison, Stats, Testimonial (statement, cards, single), Logos, FAQ, CTA (dark, box), Form, Legal, and Tool (booking, reviews, video, generic). In the wireframe sitemap every page, legal pages included, is its own column, and each section card shows the question it answers.

## What to present (compact)
- Sitemap tree.
- Journey per persona, one line each.
- Page table: Page | Slug per language | Nav | Persona | Awareness level | Page goal | Keyword cluster | Primary action | Third-party tools | Languages.
- Section plan per page: # | Visitor question | Answer in the brief | Type and variant | Why this layout and position.
- Objection map: Objection | Page | Section | Proof used.
- Tool placement: Tool | Page(s) | Section | How it appears | Fallback if it does not load | Language or RTL issue.
- Navigation model; the keyword mapping (each cluster next to its page, flagging clusters with no page and pages competing for one keyword); pages left out with reasons; open questions.

## Then
1. Write the files with status `proposed`, run the quality check, share the brief.
2. Ask the open questions one at a time, recommendation first (for example "Where should the booking tool appear?" with "Inline on the contact page (Recommended)", "On its own booking page", "Leave it open for now"). Update and share the brief after each answer.

## Guardrails
- Restricted or "do not use" claims never appear in page names, menu labels or planned sections.
- Never plan a page or language the brief gives no reason for.
- Never mark the IA `approved` without the user's explicit approval.

## Quality check
| Item | Pass when |
|---|---|
| **Goal** | Every page has a goal (persona, awareness level, what they must believe or do, one primary action), and every section in its plan answers a visitor question from a named place in the brief |
| Journeys | Every persona's journey ends at the conversion goal |
| Section plans | Sections follow the order of the visitor's questions; each layout fits the shape of its answer, with the reason written; no section without a question or without an answer source; no two pages share a sequence without a stated reason |
| Objections | Every section 3 objection is placed with proof, or listed as open |
| Tools | Every section 1 tool is placed with its appearance and fallback; no rating or count planned without client data |
| Keywords | Every cluster maps to exactly one page; no two pages compete; pages without a cluster have a reason |
| Navigation | 5 to 7 main items, grouped by visitor task; the switcher links to equivalent pages |
| Languages | The Languages column is filled for every page and checked against section 2; legal pages exist in every language that has pages; every limited language has a reason |
| Section types | Every planned section uses a supported type and variant |
| Location mentions | Every placement matches the confirmed geo-localization level per language; no place in a title or heading unless the level is "headings"; the section 10 `location` row is `verified` |
| Restricted claims | None in page names, menu or sections |
| Requirements | Section 10 rows of type structure, page or language are `verified` |
| Brief visible | The brief was shared after every change |

## Gate
Ask: "Do the structure, the page goals and section plans, the journeys, the tool placement and the keyword mapping work?" with "Approve the structure (Recommended)", "Add, remove or merge pages", "Change a page plan, a journey, a tool or the keyword mapping". On changes, show only what changed, update the files, share the brief and ask again. Page copy must not start before approval.
