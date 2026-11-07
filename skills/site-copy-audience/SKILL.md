---
name: site-copy-audience
description: Builds the customer evidence behind website copy - real pain points with verbatim phrases, objections, evidence-based personas per region and language, and a competitor list - and asks who reads any site language whose audience is unknown. Runs alone or as stage 2 of website-copy-builder.
---

# Site copy: audience and competitors

Stage 2 of the website copy set. It works alone or inside `website-copy-builder`.

## Goal
Give the copy real evidence about its buyers, per region and language: their pains in their own words, their objections, and who they are.

## Shared rules (identical in every website-copy skill)
**Questions.** One question per message, with AskUserQuestion: 2 to 4 options, the recommended reply first with its label ending in "(Recommended)", and no "Other" option (the user can always type their own answer). Name the item inside the question so it reads on its own, and build the options from the brief so one click answers. For facts only the user knows, offer "I'll type it now", "I don't know yet: mark it [TO VERIFY]" and "Skip this item". Without AskUserQuestion, ask in plain text with numbered replies, the recommended one first.

**The brief.** `brief.md` lives where its `Project folder:` line (second line) says: a folder on the user's computer, the claude.ai Project attached to the chat (Projects tool: `project_read`, `project_write`), or this chat only. The `analysis/` and `pages/` files live in the same place (as Project docs when the Project is the location). Read the latest version just before writing, change only the sections this skill owns plus rows of `## 10. Feedback register`, write the whole file back, then read it back to confirm. Never say "saved" without that read. If the brief belongs to a different business than the one the user names, do not touch it: start a new brief. Before saying a file cannot be read or written, try every file tool available in the session.

**The user sees every change.** After every change to `brief.md`, share it in the chat so the user can read it inside Claude: send the file with SendUserFile (display: render) with one line saying what changed, then ask one question: "Approve this version and continue (Recommended)" or "Change something". Wait for the answer. One share per change: never group several changes into one share, never skip a share to save time, and never continue past an unanswered checkpoint.

**Feedback becomes a requirement.** Whenever the user asks for a change (a tone, a value, the mission, a fact, a claim, a page, a word to avoid), first add it to `## 10. Feedback register` as one row: ID (R1, R2…), date, stage, the user's own words, type (voice, value, mission, fact, claim, offer, structure, copy, location, other), the sections and pages it affects, status `open`. Then apply it and set `applied`. Only the quality check sets `verified`, after comparing the output with the user's words. Every later stage re-checks the requirements that touch its own output. A requirement is never dropped silently: if it conflicts with a guardrail (for example a claim that cannot be proven), say so and ask.

**Quality check.** Run the checklist at the end of this file before the gate. Record each item as pass or fail with one line of evidence in this stage's analysis file, and show the user the result in a compact table. Check every number (counts, lengths, limits) by counting or with a script, never by eye. Fix a fail before the gate; if only the client can fix it, list it as open and let the user decide at the gate. The goal item comes first: if it fails, the stage is not done.

## Owns
`## 3. Audience and competitors`, and the Audience cell of section 2 rows marked "audience not given". Writes `analysis/02-audience.md`: every query run, every source with URL and date, every phrase found and how it was checked, pages that could not be read, the long competitor notes, the reasoning behind each persona, and the quality check.

## Inputs
What the business offers and its conversion goal, the regions, the languages and their audiences (sections 1 and 2). If there is no brief, ask for each, one question at a time.

## Steps
1. **Languages with no audience.** For every section 2 row marked "audience not given", ask before researching: "Who reads the [language] version, and in which country?" with options built from the regions and personas in the brief, plus "No one specific yet: decide at the site structure stage" and "I don't know yet: mark it [TO VERIFY]". Record the answer in section 2. A language whose audience stays unknown is flagged for the site structure stage; it is not researched on guesses.
2. **Set up the research.** Write in the chat: the business summary, the regions, the languages and "this is for website copy, not product development". The research skills below then skip their own intake. They handle one region per run: run the primary region fully, secondary regions lightly. A language the user describes as a general international version with no market of its own reuses the other personas; every other language is researched for its own audience. Load each skill with the Skill tool and copy only the conclusions into the brief; if a skill is unavailable, do the same work with web search.
3. **`customer-pain-point-collection` (first).** Search reviews, forums, Reddit, app stores and social posts from the last 12 months, in the target languages and regions, naming the sources (Google reviews, local forums, social groups, review sites). Coverage can be thin outside English-language markets: say so instead of padding.
   - For each theme, record 2 to 3 short phrases in the original language with URL and date. A phrase is **verbatim** only after reading it in the page text. Phrases seen only in a search snippet or a page summary are labelled **snippet** and are not used in headlines until checked.
   - Tag each theme with the value driver it hits: **outcome**, **likelihood**, **time**, **effort**.
   - Collect fears and objections separately; each needs a source or is marked "assumption".
4. **`persona-research` (2 to 4 segments)**, fed with step 3. Mark each statement as evidence (with source) or assumption. Drop invented profile fields (fictional name, age range, income, lifestyle, tech familiarity) unless a source supports them; label personas by role and segment. Add to each card: the trigger, a "When [situation], I want [outcome], so I can [result]" line, objections, trust signals needed before contact, search terms in their language, preferred channels in the region, and the usual **awareness level** on arrival (unaware, problem-aware, solution-aware, product-aware).
5. **`market-competition-research`.** Keep the competitor list, the gaps and the takeaway. Replace software-style feature rows with: core offer, price level, target segment, USP, proof types, guarantee, contact model, languages offered. The list feeds the benchmark and offer stages.
6. **Write** section 3 and `analysis/02-audience.md`, run the quality check, share the brief.
7. **Present** compactly: top pain themes with one phrase and driver each, top objections, personas in one line each with awareness level, main competitors, and how strong the evidence is per language.
8. **Open questions** the research raised, one at a time, most important first; offer "Skip the rest for now" after the first.

`jtbd-research` and `market-size-research` are not used. A market figure goes into copy only with a dated source.

## Guardrails
- Never invent a demographic, an income, a quote or a source.
- Never present a snippet as a verbatim phrase.
- Never research a language on a guessed audience: ask, or flag it.
- Never pad thin evidence: state the strength per language.

## Quality check
| Item | Pass when |
|---|---|
| **Goal** | Each primary-region persona has sourced pains and objections, and evidence strength is stated per language |
| Phrases | Each pain theme has at least 2 phrases with URL and date, each labelled verbatim (read on the page) or snippet |
| Driver tags | Every theme carries a value driver |
| Objections | Every objection has a source or is marked "assumption" |
| Personas | Labelled by role and segment; no invented demographics; awareness level, trigger, "When I want so I can" line and search terms present |
| Languages | Every section 2 language is researched for its own audience, reuses others with the user's stated reason, or is flagged for the site structure stage |
| Competitors | The table uses the override fields, with no empty cell left unexplained |
| Requirements | Section 10 rows touching this stage are `verified` |
| Brief visible | The brief was shared after every change |

## Gate
A light check: "Looks right, continue to the benchmark (Recommended)", "Correct a persona or objection", "Add a competitor I know".
