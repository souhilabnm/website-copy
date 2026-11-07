---
name: site-copy-positioning
description: Defines how a website speaks - one specific, provable promise, a positioning statement, three message pillars with proof, and voice rules per language - grounded in a voice benchmark built from the client's own voice references or, when they have none, from research matched to their stated voice preference. Runs alone or as stage 5 of website-copy-builder.
---

# Site copy: positioning and voice

Stage 5 of the website copy set. It works alone or inside `website-copy-builder`.

## Goal
Define how the site speaks: one provable promise and a voice, grounded in a voice benchmark, that every page can follow.

## Shared rules (identical in every website-copy skill)
**Questions.** One question per message, with AskUserQuestion: 2 to 4 options, the recommended reply first with its label ending in "(Recommended)", and no "Other" option (the user can always type their own answer). Name the item inside the question so it reads on its own, and build the options from the brief so one click answers. For facts only the user knows, offer "I'll type it now", "I don't know yet: mark it [TO VERIFY]" and "Skip this item". Without AskUserQuestion, ask in plain text with numbered replies, the recommended one first.

**The brief.** `brief.md` lives where its `Project folder:` line (second line) says: a folder on the user's computer, the claude.ai Project attached to the chat (Projects tool: `project_read`, `project_write`), or this chat only. The `analysis/` and `pages/` files live in the same place (as Project docs when the Project is the location). Read the latest version just before writing, change only the sections this skill owns plus rows of `## 10. Feedback register`, write the whole file back, then read it back to confirm. Never say "saved" without that read. If the brief belongs to a different business than the one the user names, do not touch it: start a new brief. Before saying a file cannot be read or written, try every file tool available in the session.

**The user sees every change.** After every change to `brief.md`, share it in the chat so the user can read it inside Claude: send the file with SendUserFile (display: render) with one line saying what changed, then ask one question: "Approve this version and continue (Recommended)" or "Change something". Wait for the answer. One share per change: never group several changes into one share, never skip a share to save time, and never continue past an unanswered checkpoint.

**Feedback becomes a requirement.** Whenever the user asks for a change (a tone, a value, the mission, a fact, a claim, a page, a word to avoid), first add it to `## 10. Feedback register` as one row: ID (R1, R2…), date, stage, the user's own words, type (voice, value, mission, fact, claim, offer, structure, copy, location, other), the sections and pages it affects, status `open`. Then apply it and set `applied`. Only the quality check sets `verified`, after comparing the output with the user's words. Every later stage re-checks the requirements that touch its own output. A requirement is never dropped silently: if it conflicts with a guardrail (for example a claim that cannot be proven), say so and ask.

**Quality check.** Run the checklist at the end of this file before the gate. Record each item as pass or fail with one line of evidence in this stage's analysis file, and show the user the result in a compact table. Check every number (counts, lengths, limits) by counting or with a script, never by eye. Fix a fail before the gate; if only the client can fix it, list it as open and let the user decide at the gate. The goal item comes first: if it fails, the stage is not done.

## Owns
`## 6. Positioning and voice`. Writes `analysis/05-positioning.md` (every promise and pillar option, the competitor test, full voice examples per language, the user's choices with dates, the quality check) and `analysis/05-voice-benchmark.md` (each example with source, date, short quotes and the patterns extracted).

## Inputs
Business analysis, Claims and voice references or preference (section 1), regions and languages (section 2), personas, objections and customer phrases (section 3), the benchmark's tone notes and differentiate findings (section 4), the offer (section 5). If items are missing, say which and ask: "Answer the missing items now" or "Continue with labelled assumptions", recommendation first. Never invent proof.

## Steps
1. **Voice benchmark.**
   - If section 1 lists voice references, read each one (public pages fetched; LinkedIn only from pasted text or a PDF). They are the benchmark.
   - If there are none, use the voice preference in section 1; if that is missing too, ask one question about it (options built from the brief). Then research 3 to 5 current public examples per primary language that match the preference and suit the audience: real organisations or people in the same or an adjacent market, written in that language, not translated. Quote 1 or 2 short phrases from each, with URL and date.
   - For each example, extract the patterns: person used (I, we, you), formality, average sentence length (count it), typical vocabulary, how proof is stated, call-to-action wording, what it avoids.
   - Write the Voice benchmark table in section 6 and `analysis/05-voice-benchmark.md`, share the brief, and ask: "Use this voice benchmark (Recommended)", "Swap an example", "Add my own example".
2. **Promise.** Build 2 or 3 core promises from the offer: the dream outcome, plus how fast, plus how little effort, plus the proof that makes it believable. Each must pass the test: could a competitor put their name on it? If yes, sharpen it with the offer's strongest driver and the benchmark's differentiate findings. Ask one question with the promises as options, your recommendation first.
3. **Positioning and pillars.** Statement: For [persona] who [need], [business] is the [category] that [key benefit], unlike [alternative] which [limitation]. Three pillars, each with a one-line claim, its proof, the objection it answers and the pages where it appears. Build them on the drivers where the offer scored best; if the offer trails competitors on every driver, build them on the benchmark's open space and on proof a buyer can check, and say plainly that the offer is weaker than its competitors. Ask: "Approve the statement and pillars (Recommended)", "Change a pillar", "Sharpen the statement".
4. **Voice rules.** Three traits, each citing the benchmark pattern it comes from, each with a "sounds like / does not sound like" example in every site language. A formality level and a sentence-length target (a number) per language. Vocabulary: words to use (customers' own words first) and words to avoid (clichés, jargon, unprovable superlatives, and every "do not use" claim from section 1). Per-language notes: register, formality conventions, regional vocabulary, text direction, expected line length. Ask: "Approve the voice rules (Recommended)", "Make it more formal", "Change the vocabulary lists".
5. Write the files, run the quality check, share the brief.

## Guardrails
- Never base a promise or pillar on a fact the brief does not source.
- Never copy a benchmark example's wording into the copy: borrow patterns, not phrases.
- Never translate voice examples between languages: write each natively.
- A voice change the user asks for is a requirement: it updates the rules, the examples and the vocabulary together.
- Do not decide how often the business's place appears in the copy: that is the geo-localization level, recommended in the SEO stage and confirmed by the user. If a voice trait, promise or pillar relies on place (for example "local", a time zone, a regional language variant), say so in the per-language notes so the SEO stage weighs it, and keep place names out of the promise unless the user later chooses the "headings" level.

## Quality check
| Item | Pass when |
|---|---|
| **Goal** | A promise, a statement, three pillars and voice rules exist, and every voice rule cites a benchmark pattern |
| Promise | Passes the competitor test; every part is backed by proof in the brief, or flagged |
| Pillars | Each has claim, proof, objection and pages; the basis (best drivers or open space) is stated |
| Voice benchmark | At least 3 examples per primary language (or the user's own references), each with source and date, patterns extracted |
| Voice rules | 3 traits with examples in every site language; formality and a sentence-length number per language |
| Vocabulary | The avoid list contains every "do not use" claim and restricted term from section 1 |
| Languages | Per-language notes for every section 2 language |
| Requirements | Every section 10 row of type voice, value or mission is applied in the rules and examples, and `verified` |
| Brief visible | The brief was shared after every change |
