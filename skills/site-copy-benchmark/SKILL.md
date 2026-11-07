---
name: site-copy-benchmark
description: Researches 5 to 8 comparable websites across the target regions and languages, extracts positioning, structure, headlines, calls to action, proof, tone, SEO signals, offer elements and gaps, and concludes what to borrow, avoid and differentiate on. Researches its own set and invites the user's benchmarks (a document, pasted notes or links), asking what they like and dislike about each. Runs alone or as stage 3 of website-copy-builder.
---

# Site copy: benchmark

Stage 3 of the website copy set. It works alone or inside `website-copy-builder`.

## Goal
Show, with evidence from 5 to 8 comparable sites, what the copy should borrow, avoid and differentiate on.

## Shared rules (identical in every website-copy skill)
**Questions.** One question per message, with AskUserQuestion: 2 to 4 options, the recommended reply first with its label ending in "(Recommended)", and no "Other" option (the user can always type their own answer). Name the item inside the question so it reads on its own, and build the options from the brief so one click answers. For facts only the user knows, offer "I'll type it now", "I don't know yet: mark it [TO VERIFY]" and "Skip this item". Without AskUserQuestion, ask in plain text with numbered replies, the recommended one first.

**The brief.** `brief.md` lives where its `Project folder:` line (second line) says: a folder on the user's computer, the claude.ai Project attached to the chat (Projects tool: `project_read`, `project_write`), or this chat only. The `analysis/` and `pages/` files live in the same place (as Project docs when the Project is the location). Read the latest version just before writing, change only the sections this skill owns plus rows of `## 10. Feedback register`, write the whole file back, then read it back to confirm. Never say "saved" without that read. If the brief belongs to a different business than the one the user names, do not touch it: start a new brief. Before saying a file cannot be read or written, try every file tool available in the session.

**The user sees every change.** After every change to `brief.md`, share it in the chat so the user can read it inside Claude: send the file with SendUserFile (display: render) with one line saying what changed, then ask one question: "Approve this version and continue (Recommended)" or "Change something". Wait for the answer. One share per change: never group several changes into one share, never skip a share to save time, and never continue past an unanswered checkpoint.

**Feedback becomes a requirement.** Whenever the user asks for a change (a tone, a value, the mission, a fact, a claim, a page, a word to avoid), first add it to `## 10. Feedback register` as one row: ID (R1, R2…), date, stage, the user's own words, type (voice, value, mission, fact, claim, offer, structure, copy, location, other), the sections and pages it affects, status `open`. Then apply it and set `applied`. Only the quality check sets `verified`, after comparing the output with the user's words. Every later stage re-checks the requirements that touch its own output. A requirement is never dropped silently: if it conflicts with a guardrail (for example a claim that cannot be proven), say so and ask.

**Quality check.** Run the checklist at the end of this file before the gate. Record each item as pass or fail with one line of evidence in this stage's analysis file, and show the user the result in a compact table. Check every number (counts, lengths, limits) by counting or with a script, never by eye. Fix a fail before the gate; if only the client can fix it, list it as open and let the user decide at the gate. The goal item comes first: if it fails, the stage is not done.

## Owns
`## 4. Benchmark`. Writes `analysis/03-benchmark.md`: full notes per site (every page read, every extract with its URL, pages that could not be read, why each site was chosen) and the quality check.

## Inputs
Business summary, regions and languages (sections 1 and 2), and the competitor list and objections (section 3). If there is no brief, ask for the business, then the regions, then the languages, one question at a time, and find competitors yourself.

## Steps
1. **Invite the user's benchmarks.** The research runs in every case; the user's own benchmarks make the brief richer. Ask: "Do you have benchmarks to share: competitors you know or sites you admire? You can attach a document, paste notes or paste links." with "Yes, I'll share them now (Recommended)", "Not now: research them for me", "Include a specific competitor from the research". Read whatever is given: fetch links, read attached documents (PDF, Word, slides, images or screenshots) and pasted notes; a document or note may name sites or describe what the user likes without a link, so record those too. For each benchmark the user shares, ask one question at a time: "What do you like or dislike about [site]?" with "I'll type it (Recommended)", "The tone and wording", "The structure and layout", "The offer and how it is presented" (the user can type a mix). Record the answer in the user's own words. User benchmarks count toward the 5 to 8 and are marked "user" in the Source column.
2. **Select 5 to 8 sites**, starting from the competitor list in section 3 without repeating its research: 2 to 3 direct competitors in the primary region; 1 to 2 in a secondary region or language; 1 to 2 adjacent leaders (same audience, different offer) known for strong sites; 1 outlier from another sector for tone or structure. If no good candidate exists for a slot, say so, fill it with another adjacent leader, and note why. Search in the target languages, not only English. Note why each site was chosen; mark each "research" in the Source column.
3. **Read each site** (Firecrawl scrape if available, otherwise fetch): home, about, the main offer page, pricing or the contact flow, one proof or case-study page, and the navigation. List pages that could not be read.
4. **Extract per site:** positioning (the promise in one line, for whom); site structure (main navigation labels, page count, depth, what is one click from home); headline pattern (home H1 and sub-line, a short phrase with URL); CTA pattern (primary and secondary wording and placement); proof (types and where they sit); tone (3 adjectives and one example); SEO signals (titles and metas of key pages, keyword focus, languages, hreflang); **offer elements** (named offers, what is included, bonuses, guarantee, scarcity or urgency shown); **location use** (where and how often the site names its city, region or country: title, H1, headings, body, contact, footer); **gaps** (what they do not say that the audience needs, especially section 3 objections left unanswered). Quote sparingly, with the URL; paraphrase the rest.
5. **Synthesis.** Patterns (what most sites do); Borrow (specific practices, each with the site it comes from; what the user said they like comes first, checked against what the business can prove); Avoid (clichés, claims everyone makes, structures that bury the offer); Differentiate (open space this business can credibly own, each item tied to a fact in section 1). Say plainly if the space is crowded.
6. Write the files, present a compact table and the synthesis, run the quality check, share the brief.
7. **Ask what the user likes in the researched set.** Show the researched sites in a compact table and ask: "Which of these sites do you like, and what about them?" with "I'll type what I like and dislike (Recommended)", "None stands out: use your synthesis", "Add more benchmarks: a document, notes or links". Record likes and dislikes per site in the "What the user likes / dislikes" column, update Borrow and Avoid with them, and analyze any additions the same way. Then update the files and share the brief.

## Guardrails
- Never quote at length; never present a paraphrase as a quote.
- Never recommend borrowing a claim the business cannot prove.
- Never call a differentiator "open" without having checked the sites in the set.

## Quality check
| Item | Pass when |
|---|---|
| **Goal** | Borrow, avoid and differentiate lists exist; every item names its site and URL; every differentiate item is tied to a fact in section 1 |
| Set | 5 to 8 sites covering the four slots, or the missing slot explained |
| Extracts | Every site has every extract filled, or "not found" |
| Offer elements and gaps | Filled for every site; gaps refer to section 3 objections where they apply |
| Pages | Pages read and pages not readable are listed per site |
| Languages | Searches were run in the target languages |
| User benchmarks | The user was invited to share benchmarks by document, pasted notes or links, and was asked what they like and dislike about their own and the researched sites; every answer is recorded in their words and reflected in Borrow and Avoid |
| Location use | Filled for every site, or "not found" |
| Requirements | Section 10 rows touching this stage are `verified` |
| Brief visible | The brief was shared after every change |

## Gate
"Approve the benchmark conclusions (Recommended)", "Change the borrow / avoid / differentiate lists", "Swap a site for another". Wait for the answer.
