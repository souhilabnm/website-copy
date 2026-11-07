---
name: site-copy-pages
description: Writes the page-by-page copy of a website from an approved site structure, in every language each page is offered in, at an agreed length, in the brief's voice, and shows it in one wireframe file (Sitemap and Wireframe views) built from the template in this skill. No empty slots, no invented facts. Requires an approved information architecture.
---

# Site copy: page copy

Stage 8 of the website copy set. It works alone or inside `website-copy-builder`.

## Goal
Write each approved page, in every language it is offered in, as complete copy the client can check in the wireframe.

## Shared rules (identical in every website-copy skill)
**Questions.** One question per message, with AskUserQuestion: 2 to 4 options, the recommended reply first with its label ending in "(Recommended)", and no "Other" option (the user can always type their own answer). Name the item inside the question so it reads on its own, and build the options from the brief so one click answers. For facts only the user knows, offer "I'll type it now", "I don't know yet: mark it [TO VERIFY]" and "Skip this item". Without AskUserQuestion, ask in plain text with numbered replies, the recommended one first.

**The brief.** `brief.md` lives where its `Project folder:` line (second line) says: a folder on the user's computer, the claude.ai Project attached to the chat (Projects tool: `project_read`, `project_write`), or this chat only. The `analysis/` and `pages/` files live in the same place (as Project docs when the Project is the location). Read the latest version just before writing, change only the sections this skill owns plus rows of `## 10. Feedback register`, write the whole file back, then read it back to confirm. Never say "saved" without that read. If the brief belongs to a different business than the one the user names, do not touch it: start a new brief. Before saying a file cannot be read or written, try every file tool available in the session.

**The user sees every change.** After every change to `brief.md`, share it in the chat so the user can read it inside Claude: send the file with SendUserFile (display: render) with one line saying what changed, then ask one question: "Approve this version and continue (Recommended)" or "Change something". Wait for the answer. One share per change: never group several changes into one share, never skip a share to save time, and never continue past an unanswered checkpoint.

**Feedback becomes a requirement.** Whenever the user asks for a change (a tone, a value, the mission, a fact, a claim, a page, a word to avoid), first add it to `## 10. Feedback register` as one row: ID (R1, R2…), date, stage, the user's own words, type (voice, value, mission, fact, claim, offer, structure, copy, location, other), the sections and pages it affects, status `open`. Then apply it and set `applied`. Only the quality check sets `verified`, after comparing the output with the user's words. Every later stage re-checks the requirements that touch its own output. A requirement is never dropped silently: if it conflicts with a guardrail (for example a claim that cannot be proven), say so and ask.

**Quality check.** Run the checklist at the end of this file before the gate. Record each item as pass or fail with one line of evidence in this stage's analysis file, and show the user the result in a compact table. Check every number (counts, lengths, limits) by counting or with a script, never by eye. Fix a fail before the gate; if only the client can fix it, list it as open and let the user decide at the gate. The goal item comes first: if it fails, the stage is not done.

## Prerequisite
An approved information architecture: `## 8` status `approved`. If it is missing or only `proposed`, ask: "Run the site structure stage first (Recommended)" or "I have my own sitemap to use". With the user's own sitemap, ask "Is this the final structure?" ("Yes, it is final (Recommended)", "Not yet") and treat yes as approval.

## Inputs
The approved IA (journeys, menu, page goals and section plans, objection map, tool placement, Languages column), the offer (section 5; if not `approved`, offer pages are a labelled draft), positioning, voice rules and voice benchmark (section 6), the SEO plan (section 7), personas, objections and phrases (section 3), Claims, proof points and tools (section 1), languages (section 2), and every requirement in section 10. If positioning or SEO is missing, say so and ask: "Answer the missing items now" or "Write with labelled assumptions".

## Files
In the project folder:
- `site.json`: the site-wide data (written once, updated when the IA changes).
- `pages/<slug>.json`: one file per page, every offered language inside.
- `pages/<slug>.md`: the readable copy of the page, every language grouped under it.
- `<business>-wireframe.html`: one file with every page so far, rebuilt after each page.
- `brief.md`: only section 9 (progress table and assumptions list).

## The wireframe template (do not restyle)
Build the wireframe only from the files in this skill's folder (paths below are relative to the skill's base directory):
- `templates/wireframe_template.html`: the design. Never change its look, write another design, or add external resources.
- `scripts/build_wireframe.py PROJECT_FOLDER`: fills the template from `site.json` and `pages/*.json`, refuses bad data (unsupported section type or variant, empty sitemap card, a section without its visitor question or answer source, sections that differ between languages, a page written in a language it is not offered in), flags pages that share the same skeleton, and prints the section plan and the sections, words, assumptions and title and meta length per page and language.
- `scripts/check_wireframe.js FILE.html [SCREENSHOT_DIR]`: the output check (Playwright).
If the template or a script is missing, stop and ask the user to attach it. Never invent a replacement design.

What the template shows. Top bar: the business name, a **Sitemap | Wireframe** toggle, a **language dropdown**, **Flags** (assumption highlights on or off) and **SEO** (title, meta, URL with character counts). Sitemap view: the site node, connector lines, one column per page in IA order (legal pages included), white section cards with a page-specific description and the visitor question the section answers, an amber dot on cards holding an assumption, dashed cards for tools, pages not yet written or not offered in a language shown as such, zoom. Wireframe view: one page in a browser frame or **All pages** side by side, a device switch (1440, 768, 390 px), the navbar and footer from `site.json`, burger menu on mobile, right-to-left mirroring.

Supported section types and variants: `Header` (`split` with image, `centered`, `text`: tag, h1, sub, btn, link, tlink, reassure; every button is optional), `Content` (h2, p), `About` (split: h2, p), `Feature` (`grid` of 2, 3 or 4 cards, `list`, or `alternating` rows with a visual: h2, p, items, links), `Process` (numbered steps), `Pricing` (cards with prices), `Comparison` (a table: head, rows, optional links), `Stats` (sourced numbers with labels), `Testimonial` (`statement` when there is no permitted quote, `cards`, or `single` for one strong quote), `Logos` (permitted client logos only), `FAQ` (accordion), `CTA` (`dark` banner or bordered `box`), `Form` (fields, consent, button), `Legal` (template text), `Tool` with kind `booking`, `reviews`, `video` or `generic` (labelled fields and a button, for payments, maps, tickets or forms). A tagline appears only in the Header. Image placeholders appear only where the final site will show a real visual: a split Header, About, or alternating Feature rows. If the plan needs another type, ask the user before extending the template, and extend it in the same style.

## Sections come from the page plan, never from a skeleton
There is no default page layout. Each page follows its plan in section 8: the page goal, then one section per visitor question, in the order the visitor asks them, each answered from the place in the brief the plan names, in the layout that fits the shape of the answer. Before writing a page, restate its goal and its questions. While writing, if an answer turns out to have a different shape (five options instead of three, a sequence instead of a list), change the variant and record why; adding, removing or reordering a section changes the approved plan, so ask first. Never copy another page's or another project's sequence of sections. Every section's data carries `q` (the visitor question, in the page's language, shown on its sitemap card) and `ans` (where the answer is in the brief); the build script refuses a section without them.

## Data format
Before writing `site.json` or a `pages/<slug>.json` file, read `references/data-format.md` in this skill's folder: it gives both formats with examples. In short: link targets are a page id or `page#n`; unknown facts are written as `{{ASSUMED: complete text}}`; every section has `desc` (its sitemap card), `q` (the visitor question) and `ans` (where the answer is in the brief).

## Facts before copy
Before writing a page, list the facts it needs (names, numbers, prices, dates, contents, legal details). For each fact the brief does not state, ask one question with "I'll type it now", "Write it as a highlighted assumption (Recommended)" and "Skip this item". Never present an invented fact as real, and never leave a slot empty.

## Assumed content: no empty slots
- Where a fact is unknown, write complete, plausible content as `{{ASSUMED: ...}}`; it shows in amber with "Assumption: must be verified". Add it to the Assumptions table in section 9 with the value used and what the client must confirm.
- Never write "to be confirmed" or `[TO VERIFY]` in the copy. For an unknown person or qualification, write a neutral role ("a specialist from our team"). Never invent a name, title, diploma, registration number, award, certification, rating, review count or result.
- **Testimonials:** if the brief has no quote the client is permitted to publish, write no quote: write one sentence saying feedback is shared on request (highlighted) and list "no publishable testimonial" in the assumptions. Never show stars, scores or counts.
- Legal pages: full template text with placeholder company details, all highlighted, plus "Lawyer review required before publication". The privacy text names every tool in section 1.
- Real facts from the brief stay unhighlighted. Never use a claim marked "needs evidence" or "do not use".

## Page length (ask before each page type)
Ask: "How long should the [page] copy be?" with three options in source-language words, recommended first, based on the strongest relevant results in `analysis/06-seo.md` and typical ranges (home 500-800; core offer or service 1,000-1,500; detail 500-900; category 400-700; about 600-1,000; proof 600-1,000; FAQ 700-1,200 with 8 to 15 questions; delivery and terms 400-800; contact or booking 100-250; thank-you 50-100), the awareness level (problem-aware pages need more room) and the number of objections the page answers. Apply the choice to later pages of the same type. Text inside a tool widget does not count.
**Targets per language:** a Latin-script language gets the source target; a language that attaches particles to words (for example Arabic) gets 80 percent of it. **Length gate:** a language more than 20 percent below its own target is not done: ask for missing facts or extend with highlighted substance. No upper limit beyond the agreed range. Report the counts printed by the build script, never estimated ones.

## Languages: localized, identical structure
Same sections in the same order, the same number of items, buttons and tools in every language of a page; only wording changes (the build script enforces it). Write each language natively for its readers; avoid calques. The menu is identical in every language; a page not offered in a language stays in the menu and shows a note. Flag headlines that may not fit, and tools that do not support a language or right-to-left text.

## Voice and requirements
Write to the voice rules and the voice benchmark in section 6: the person used, the formality, the sentence-length target, the words to use and avoid. Apply every section 10 requirement that touches copy to every page, not only the next one.

## Order and rhythm
Home, the core offer page, other offer pages, proof pages, supporting pages (contact, booking, FAQ, resources), legal pages. Deliver one or two pages at a time.

## Before writing each page
Restate from the plan: the page goal (persona, awareness level, what they must believe or do, the one primary action), the visitor questions in order, the tools placed on the page, and the location mentions planned for this page and language in section 8 (element and wording). Every section answers its question.
- **Problem-aware:** open with their situation and pain in their own words, then show it can be solved, then the offer.
- **Solution-aware:** open with the outcome and why this approach beats the alternatives they know.
- **Product-aware:** open with the offer, its name, proof and risk reversal, and make the action easy.
**Core offer page** (unless the plan says otherwise): name and dream outcome; the situation and obstacles in the buyer's words; how each obstacle is removed; proof for people like them; bonuses with the obstacle each removes; risk reversal; real scarcity or urgency only if approved in section 5; the primary action and what happens after the click.

## Writing rules
Lead with the visitor's outcome. Say how fast the first result comes and what the client does not have to do, where true. One idea per section, short paragraphs, specifics over adjectives. Reach the length with substance (answers, proof, examples, steps), never filler. Use customers' phrases where they fit. At most 3 primary buttons in the body (1 on a page under about 250 words, 2 up to about 600, 3 above), equal in every language; secondary actions are outlined buttons or text links.

## After each page
1. Write `pages/<slug>.json` and `pages/<slug>.md`, run `build_wireframe.py`, run `check_wireframe.js`, fix every failure, run the quality check, read the files back.
2. Send the one HTML file into the chat (do not publish it as an artifact unless the user asks) with a short summary (H1, sub-line, sections, words per language, assumptions count). Update section 9 and share the brief.
3. If a missing fact blocks the copy, ask it first, one question per fact, with "Skip the rest for now" after the first.
4. Then ask one question, which is also the brief checkpoint: "Approve this page and the brief, and write the next page (Recommended)", "Change the tone or length", "Change a section, a tool or the CTA". A change becomes a section 10 requirement and is carried to later pages.

`pages/<slug>.md` per language: page, language, URL, page goal, persona, awareness level, target and final word count; SEO title and meta with character counts; sections in order (type and variant, the visitor question it answers, sitemap description, headings, body, proof with its source); tools with placement, surrounding copy and fallback; primary action with its reassurance; internal links; assumptions with values used.

## Guardrails
- Never restyle the template or deliver a wireframe not built from it.
- Never invent a fact, a person, a quote, a rating or a result; never leave a slot empty.
- Never use a guarantee, limit or deadline section 5 has not approved.
- Never name the business's place (city, region, country) anywhere the Location mentions table does not plan it, and never leave out a planned mention; use the place names exactly as written in section 7.
- Never send a page whose check script or quality check has an unexplained failure.

## Quality check (per page)
| Item | Pass when |
|---|---|
| **Goal** | The page exists in every language it is offered in, follows its plan (every section answers its visitor question with the answer from the brief), and no slot is empty |
| Section plan | Sections, order, types and variants match the approved plan, or each change is recorded with its reason and was approved; every section has `q` and `ans`; the build script reports no unexplained shared skeleton |
| Facts | Every fact is sourced in the brief or is a highlighted assumption listed in section 9 with its value |
| Claims | No "needs evidence" or "do not use" claim; no unapproved guarantee, scarcity or urgency; no invented testimonial, rating, count or name |
| Length | Each language is within 20 percent below its own target (counts from the build script) |
| Parity | Same sections, order, buttons and tools in every language (build script passed) |
| Action | One primary action matching the IA; primary buttons within the limit and equal across languages |
| Voice | Person, formality and sentence length match section 6 (sentence length computed); no word from the avoid list (searched) |
| SEO | Title 50 to 60 and meta 140 to 160 characters (script); primary keyword in title, H1 and first paragraph |
| Location | Place names found by search match the planned mentions for this page and language: every planned one present, none extra, none in a heading unless planned |
| Requirements | Every section 10 row touching copy is applied on this page and `verified` |
| Output check | `check_wireframe.js` reports all checks passed |
| Brief visible | The brief was shared after section 9 changed |
