---
name: site-copy-qa
description: Checks the whole site's drafted copy and assembles the final copy deck - edit pass, conversion, SEO, voice, language parity, claims and assumptions, feedback requirements, the automated wireframe check and a cold-reader test of key pages. Runs alone or as stage 9 of website-copy-builder.
---

# Site copy: edit and QA

Stage 9 of the website copy set. It works alone or inside `website-copy-builder`.

## Goal
Confirm the whole site's copy is accurate, consistent and ready to hand over, and deliver it as one copy deck.

## Shared rules (identical in every website-copy skill)
**Questions.** One question per message, with AskUserQuestion: 2 to 4 options, the recommended reply first with its label ending in "(Recommended)", and no "Other" option (the user can always type their own answer). Name the item inside the question so it reads on its own, and build the options from the brief so one click answers. For facts only the user knows, offer "I'll type it now", "I don't know yet: mark it [TO VERIFY]" and "Skip this item". Without AskUserQuestion, ask in plain text with numbered replies, the recommended one first.

**The brief.** `brief.md` lives where its `Project folder:` line (second line) says: a folder on the user's computer, the claude.ai Project attached to the chat (Projects tool: `project_read`, `project_write`), or this chat only. The `analysis/` and `pages/` files live in the same place (as Project docs when the Project is the location). Read the latest version just before writing, change only the sections this skill owns plus rows of `## 10. Feedback register`, write the whole file back, then read it back to confirm. Never say "saved" without that read. If the brief belongs to a different business than the one the user names, do not touch it: start a new brief. Before saying a file cannot be read or written, try every file tool available in the session.

**The user sees every change.** After every change to `brief.md`, share it in the chat so the user can read it inside Claude: send the file with SendUserFile (display: render) with one line saying what changed, then ask one question: "Approve this version and continue (Recommended)" or "Change something". Wait for the answer. One share per change: never group several changes into one share, never skip a share to save time, and never continue past an unanswered checkpoint.

**Feedback becomes a requirement.** Whenever the user asks for a change (a tone, a value, the mission, a fact, a claim, a page, a word to avoid), first add it to `## 10. Feedback register` as one row: ID (R1, R2…), date, stage, the user's own words, type (voice, value, mission, fact, claim, offer, structure, copy, location, other), the sections and pages it affects, status `open`. Then apply it and set `applied`. Only the quality check sets `verified`, after comparing the output with the user's words. Every later stage re-checks the requirements that touch its own output. A requirement is never dropped silently: if it conflicts with a guardrail (for example a claim that cannot be proven), say so and ask.

**Quality check.** Run the checklist at the end of this file before the gate. Record each item as pass or fail with one line of evidence in this stage's analysis file, and show the user the result in a compact table. Check every number (counts, lengths, limits) by counting or with a script, never by eye. Fix a fail before the gate; if only the client can fix it, list it as open and let the user decide at the gate. The goal item comes first: if it fails, the stage is not done.

## Owns
The status in `## 9. Copy progress`, the edited `pages/` files and the rebuilt wireframe, `analysis/09-qa.md` (every check result, every edit with its reason, the cold readers' reports, the assumption list, open items with the user's answers, the quality check) and the deck.

## Inputs
The `pages/` files and wireframe (or copy the user pastes), personas and objections (section 3), the offer (section 5), voice rules and benchmark (section 6), SEO plan (section 7), IA with menu and objection map (section 8), proof points and Claims (section 1), and the feedback register (section 10). With pasted copy and no brief, ask: "Answer a few questions about the audience, keywords and voice (Recommended)" or "Check only what can be checked without them".

## Checks
1. **Edit pass**, every language: clarity, specifics over adjectives, filler and stock phrases cut, one idea per sentence, voice consistent with section 6, no translated-sounding phrasing or calques.
2. **Conversion**, per page: every section answers its planned visitor question with the answer from the brief, in the planned order, and no section is filler; one primary action matching the IA, nothing competing with it; primary buttons within the limit; the opening matches the awareness level; key pages cover the outcome, why it will work for them, how fast and how little effort; every objection the map assigns to the page is answered with proof.
3. **SEO**, per page and language: one H1; primary keyword in title, H1 and early copy without stuffing; title 50 to 60 and meta 140 to 160 characters (counted by script), no duplicate metas; internal links to parent, related pages and the conversion page; hreflang and URL notes present.
4. **Voice**, per page and language: person, formality and sentence length against the rules (sentence length computed), no word from the avoid list (searched), and patterns consistent with the voice benchmark.
5. **Language parity and localization:** the same sections in the same order, the same menu and sitemap; each language within 20 percent below its own target; each non-source language read for literal translation. A language missing sections is a failure, not a note.
6. **Claims and assumptions:** list every highlighted assumption and any number, award, client name or result without a source; every guarantee, scarcity or urgency statement checked against section 5 (approved, true, lawful). Never remove or invent a claim silently; confirm no slot is empty. Then ask about the most important items one at a time (home and offer pages first), for example "Is [claim] confirmed? ([evidence] needed)" with "I'll send the evidence (Recommended)", "Keep it as a highlighted assumption", "Remove the claim"; after the first, offer "Leave the rest as assumptions".
7. **Geo-localization**, per page and language: search the copy for every place name in section 7 (and its variants, for example Montreal / Montréal) and count each by element (title, H1, H2, H3, body, contact, footer, meta). Compare with the Location mentions table and the level the user confirmed: a missing planned mention or an extra one is a failure. Report the counts in a table.
8. **Feedback register:** every row of section 10 is applied everywhere it applies and `verified`; list any row still open and ask about it.
9. **Automated output check:** run `check_wireframe.js` (from `site-copy-pages`) on the wireframe; record the results. If it cannot run, say so and read the file for the same problems, labelled as a weaker check.
10. **Cold readers** (home and core offer pages). Separate reader agents need the user's permission in some environments: ask once, "Run separate readers (Recommended)" or "Self-read, labelled as a weaker check". Give each reader only the persona card and the page copy in that persona's language, with no brief and no explanation of intent, and ask: what the page offers and to whom, in one sentence; what is unclear; what it does not believe and why; which objection is still open; whether it would take the primary action and what would make it. Fix what they reveal, or list it as open. If a fix changes meaning or a claim, ask first: "Apply the fix (Recommended)", "Keep the original", "Show me both".

## Assemble the deck
One document: the sitemap and IA, the offer summary, a short voice guide with the voice benchmark, the keyword map with the geo-localization decision and location mentions, then the pages in sitemap order with each language grouped under its page, then the assumption list (value used and what the client must confirm), then the feedback register. Ask the format: "A shareable doc and a file in my project folder (Recommended)", "Only a file in my project folder", "A Word file". Save `website-copy-deck.md` (or `.docx`) in the project folder; when a doc is chosen, also create it as a Docs artifact. Read every file back.

## Report
In a few lines: what changed, the parity and output-check results, what the readers found, the assumptions the client must confirm, and the path of each file. End with: "Done: mark the project complete (Recommended)", "Go through the assumptions now", "Rework a page".

## Guardrails
- Never change a claim's meaning without asking.
- Never mark the project complete with a section 10 row still `open`, unless the user decides to.
- Never report a check as passed without having run it.

## Quality check
| Item | Pass when |
|---|---|
| **Goal** | The deck exists with every part listed above and was read back, and every check below passed or its open items were accepted by the user |
| Checks 1 to 7 | Each ran on every page and language, with results in `analysis/09-qa.md` |
| Geo-localization | Place-name counts per page, language and element match the confirmed level and the Location mentions table |
| Numbers | Every length, count and limit was checked by script |
| Requirements | Every section 10 row is `verified`, or open with the user's decision recorded |
| Output check | The wireframe check passed, or failures are listed with the user's decision |
| Cold readers | Ran on home and core offer pages (agents, or a labelled self-read); findings fixed or open |
| Assumptions | Every assumption in the deck names what the client must confirm |
| Brief visible | The brief was shared after every change |
