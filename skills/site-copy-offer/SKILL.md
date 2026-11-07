---
name: site-copy-offer
description: Designs or sharpens the business offer before any copy is written, with the value equation (dream outcome, likelihood, time, effort) - scores it against competitors, maps every buyer obstacle to a solution, trims and stacks a core offer, and proposes honest bonuses, risk reversal, real scarcity or urgency, and a name. Waits for client approval. Runs alone or as stage 4 of website-copy-builder.
---

# Site copy: offer design

Stage 4 of the website copy set. It works alone or inside `website-copy-builder`. Read the **Offer frameworks** summary at the end of this file before starting.

## Goal
Agree, with the client, an offer they can deliver and stand behind, before any copy is written.

## Shared rules (identical in every website-copy skill)
**Questions.** One question per message, with AskUserQuestion: 2 to 4 options, the recommended reply first with its label ending in "(Recommended)", and no "Other" option (the user can always type their own answer). Name the item inside the question so it reads on its own, and build the options from the brief so one click answers. For facts only the user knows, offer "I'll type it now", "I don't know yet: mark it [TO VERIFY]" and "Skip this item". Without AskUserQuestion, ask in plain text with numbered replies, the recommended one first.

**The brief.** `brief.md` lives where its `Project folder:` line (second line) says: a folder on the user's computer, the claude.ai Project attached to the chat (Projects tool: `project_read`, `project_write`), or this chat only. The `analysis/` and `pages/` files live in the same place (as Project docs when the Project is the location). Read the latest version just before writing, change only the sections this skill owns plus rows of `## 10. Feedback register`, write the whole file back, then read it back to confirm. Never say "saved" without that read. If the brief belongs to a different business than the one the user names, do not touch it: start a new brief. Before saying a file cannot be read or written, try every file tool available in the session.

**The user sees every change.** After every change to `brief.md`, share it in the chat so the user can read it inside Claude: send the file with SendUserFile (display: render) with one line saying what changed, then ask one question: "Approve this version and continue (Recommended)" or "Change something". Wait for the answer. One share per change: never group several changes into one share, never skip a share to save time, and never continue past an unanswered checkpoint.

**Feedback becomes a requirement.** Whenever the user asks for a change (a tone, a value, the mission, a fact, a claim, a page, a word to avoid), first add it to `## 10. Feedback register` as one row: ID (R1, R2…), date, stage, the user's own words, type (voice, value, mission, fact, claim, offer, structure, copy, location, other), the sections and pages it affects, status `open`. Then apply it and set `applied`. Only the quality check sets `verified`, after comparing the output with the user's words. Every later stage re-checks the requirements that touch its own output. A requirement is never dropped silently: if it conflicts with a guardrail (for example a claim that cannot be proven), say so and ask.

**Quality check.** Run the checklist at the end of this file before the gate. Record each item as pass or fail with one line of evidence in this stage's analysis file, and show the user the result in a compact table. Check every number (counts, lengths, limits) by counting or with a script, never by eye. Fix a fail before the gate; if only the client can fix it, list it as open and let the user decide at the gate. The goal item comes first: if it fails, the stage is not done.

## Owns
`## 5. Offer`, with a status line: `proposed` or `approved`. Writes `analysis/04-offer.md`: score table with evidence, the full obstacle → solution list, items cut and why, every enhancer option considered, the client's decisions with dates, and the quality check.

## Inputs
Business analysis, offer raw material and Claims (section 1), regions (section 2), pain themes with driver tags, objections and personas (section 3), competitors' offer elements and gaps (section 4). If there is no brief, ask, one question at a time: the offer, who buys it, the outcome they want, and how long and how much effort it takes them today.

## Steps
1. **Market check.** One or two lines: does the brief show real pain, ability to pay and a reachable audience? If not, say so before going on.
2. **Missing raw material.** If section 1 lacks something the offer needs (first-result time, effort asked of the buyer, capacity, reusable assets, existing guarantee), ask for it, one question at a time.
3. **Score** the current offer and 2 to 3 competitors 1 to 5 on each driver (outcome, likelihood, time, effort), one line of evidence each. Show where the client loses and where open space exists.
4. **Dream outcome:** one sentence in the buyer's words, using section 3 phrases where they fit.
5. **Obstacle → solution list.** Start from the pain themes and objections, then walk the buyer's steps and add obstacles the research missed (marked as assumptions). For each: driver tag, solution, delivery (done for / with / by them; one-to-one or group; when).
6. **Trim and stack.** Keep high-value, low-cost items; flag high-cost, low-value ones to cut. Propose the core offer as a short stack.
7. **Enhancers** (propose, never decide):
   - Bonuses: built only from the reusable assets in section 1, each removing a named obstacle. If no asset removes an obstacle, propose none and say so.
   - Risk reversal: 2 to 3 options of different strength (conditional, service-based, anti-guarantee), each tied to the buyer's biggest fear, with what it would cost the client if triggered. If section 1 says a guarantee is not decided or not wanted, include "No guarantee for now" and respect it.
   - Scarcity and urgency: only from real limits in section 1 (capacity, cohort dates, seasonal windows). If there is none, say so and propose none.
   - Name: 3 options from the naming ingredients, for the core offer and each bonus.
8. **Honesty and law.** Every guarantee, limit, deadline and value claim must be true, deliverable, and lawful under consumer and advertising rules in the section 2 regions. Flag what needs the client's or a lawyer's confirmation.
9. **Present** one screen (scores, dream outcome, stack, enhancer options), then ask the client's decisions **one at a time**, recommendation first, in this order: the core stack, each bonus, the risk reversal, scarcity or urgency (only if a real limit exists), the name. Update the files after the decisions, run the quality check, share the brief.

## Guardrails
- Never invent a guarantee, a limit, a deadline, a price anchor or a result.
- Never use a claim marked "needs evidence" or "do not use" in the offer.
- Never mark the offer `approved` without the user confirming the client agreed.

## Quality check
| Item | Pass when |
|---|---|
| **Goal** | The offer is `approved` with the client's agreement confirmed, or `proposed` with the open decisions named |
| Market check | Written, and any weakness said plainly |
| Scores | Every score has one line of evidence |
| Obstacles | Every pain theme and objection has a solution, or is flagged as unsolved |
| Enhancers | Every bonus maps to an obstacle and a real asset; every guarantee, scarcity or urgency statement is client-stated, true and lawful in the regions |
| Claims | No "needs evidence" or "do not use" claim appears |
| Decisions | Each decision is recorded with its date |
| Requirements | Section 10 rows touching the offer are `verified` |
| Brief visible | The brief was shared after every change |

## Gate
This changes the business, not just the website. Ask: "The client has agreed: approve the offer (Recommended)", "Keep it as a draft until the client confirms", "Change something first". Mark `## 5` `approved` only when the user confirms the client agreed. Until then, later stages may use it only as a labelled draft.

## Offer frameworks (summary)

A working summary, in our own words, of the offer-design ideas in Alex Hormozi's *$100M Offers* (2021). It covers what the offer stage needs; it is not a substitute for the book.

### Order of leverage
The market (a group with real pain, the means to pay, and easy to reach) matters more than the offer, and the offer matters more than the persuasion. Copy cannot rescue a weak offer to the wrong market. If the brief shows a weak market, say so before designing the offer.

### Commodity vs. value
If prospects can line the offer up next to others and compare like for like, they decide on price. The aim is an offer distinct enough that the comparison breaks down, so the decision is made on value.

### The value equation
Perceived value rises with two things and falls with two:
- **Up:** the dream outcome (what the buyer really wants, in their terms, including status) and the perceived likelihood of getting it (proof, track record, specificity, guarantees).
- **Down:** the time until the result (especially the first visible win) and the effort and sacrifice asked of the buyer (work, hassle, things given up).
Big promises are easy to copy; reducing time and effort is hard and therefore differentiating. What counts is what the buyer *perceives*: making progress visible can matter as much as making it faster.

### Building the offer
1. **Dream outcome:** state it as the buyer would.
2. **Obstacles:** list every step the buyer must go through, and for each one, every reason it might go wrong, cost too much time, take too much effort, or not work for them. Tag each with its value driver.
3. **Solutions:** turn each obstacle into a "how to" solution, then decide how each is delivered: done for them, done with them, or done by them; one-to-one or group; live or recorded; and when they get it. Higher-touch delivery costs more to provide and is worth more.
4. **Trim and stack:** drop solutions that cost a lot to deliver and add little value; keep high-value, low-cost items. Bundle what remains into one offer that addresses every main obstacle.

### Enhancers
- **Bonuses:** separate, named items that remove a specific obstacle (templates, checklists, recorded sessions, partner deals). Each gets its own short value claim. Prefer adding bonuses to discounting.
- **Risk reversal (guarantees):** name the buyer's biggest fear and reverse it. Types: unconditional (refund, no questions), conditional (refund or more service if the buyer did their part and the result did not come), anti-guarantee (all sales final, with a stated reason), and implied (performance or revenue-share pricing). A guarantee enhances a good offer; it cannot rescue a bad one.
- **Scarcity:** a real limit on supply (capacity, cohort size, slots per month). The honest version states the real capacity.
- **Urgency:** a real time limit (cohort start dates, seasonal windows, a bonus that ends on a date).
- **Naming:** a name that attracts the right buyer and repels the wrong one. Ingredients: a reason for the offer now, who it is for, the goal, a time frame, and a container word (programme, sprint, system, audit). Use three to five of them. Name the bonuses too. Names wear out; the offer can be re-wrapped under new names without changing what it is.

### Pricing
Price to the value of the outcome, not the cost of delivery. Higher prices let the business deliver better, and buyers who pay more tend to commit more.
