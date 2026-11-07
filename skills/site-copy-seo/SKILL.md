---
name: site-copy-seo
description: Builds the SEO plan for a website - keyword research per language and region, a ranking check of who ranks today, weighted keyword clusters mapped to pages, on-page rules, and hreflang and URL strategy - with the source and strength of every number stated. Runs alone or as stage 6 of website-copy-builder.
---

# Site copy: SEO plan

Stage 6 of the website copy set. It works alone or inside `website-copy-builder`.

## Goal
Map each planned page to the searches its buyers really make in each site language, with the strength of the data stated.

## Shared rules (identical in every website-copy skill)
**Questions.** One question per message, with AskUserQuestion: 2 to 4 options, the recommended reply first with its label ending in "(Recommended)", and no "Other" option (the user can always type their own answer). Name the item inside the question so it reads on its own, and build the options from the brief so one click answers. For facts only the user knows, offer "I'll type it now", "I don't know yet: mark it [TO VERIFY]" and "Skip this item". Without AskUserQuestion, ask in plain text with numbered replies, the recommended one first.

**The brief.** `brief.md` lives where its `Project folder:` line (second line) says: a folder on the user's computer, the claude.ai Project attached to the chat (Projects tool: `project_read`, `project_write`), or this chat only. The `analysis/` and `pages/` files live in the same place (as Project docs when the Project is the location). Read the latest version just before writing, change only the sections this skill owns plus rows of `## 10. Feedback register`, write the whole file back, then read it back to confirm. Never say "saved" without that read. If the brief belongs to a different business than the one the user names, do not touch it: start a new brief. Before saying a file cannot be read or written, try every file tool available in the session.

**The user sees every change.** After every change to `brief.md`, share it in the chat so the user can read it inside Claude: send the file with SendUserFile (display: render) with one line saying what changed, then ask one question: "Approve this version and continue (Recommended)" or "Change something". Wait for the answer. One share per change: never group several changes into one share, never skip a share to save time, and never continue past an unanswered checkpoint.

**Feedback becomes a requirement.** Whenever the user asks for a change (a tone, a value, the mission, a fact, a claim, a page, a word to avoid), first add it to `## 10. Feedback register` as one row: ID (R1, R2…), date, stage, the user's own words, type (voice, value, mission, fact, claim, offer, structure, copy, location, other), the sections and pages it affects, status `open`. Then apply it and set `applied`. Only the quality check sets `verified`, after comparing the output with the user's words. Every later stage re-checks the requirements that touch its own output. A requirement is never dropped silently: if it conflicts with a guardrail (for example a claim that cannot be proven), say so and ask.

**Quality check.** Run the checklist at the end of this file before the gate. Record each item as pass or fail with one line of evidence in this stage's analysis file, and show the user the result in a compact table. Check every number (counts, lengths, limits) by counting or with a script, never by eye. Fix a fail before the gate; if only the client can fix it, list it as open and let the user decide at the gate. The goal item comes first: if it fails, the stage is not done.

## Owns
`## 7. SEO plan`, except the Assigned page column once `site-copy-ia` has run. Writes `analysis/06-seo.md`: every keyword with its signals and sources, the queries run, the top results seen per primary keyword, weights with scores, dropped keywords and why, cluster reasoning, credits spent, and the quality check.

## Inputs
Regions, languages and audiences (section 2), personas, awareness levels and customer phrases (section 3), benchmark SEO signals (section 4), the offer (section 5), positioning (section 6), Claims (section 1). If the IA is approved, map clusters to its pages; otherwise use provisional page types ("service page", "FAQ") that `site-copy-ia` replaces. If a section 2 language still says "audience not given", ask: "Who reads the [language] version, and in which country?" with options from the brief.

## Before researching (one question each)
1. **Data sources.** Check which SEO connectors exist (ListConnectors with keywords such as seo, openseo, ahrefs, semrush, ubersuggest; SearchMcpRegistry for others). A connector is usable only if its tools are loaded in this chat (ToolSearch can load deferred tools). Say in one line which are usable, connected but not loaded, or unfinished. Ask: "Use my connected tools, falling back to estimates (Recommended)" when one is usable, otherwise "No, estimate from search signals (Recommended)", plus "Yes, I'll attach an export" and "Pause while I connect a tool".
2. **Budget.** If a paid tool will be used, state the expected cost of the planned calls (use the tool's estimate when it has one) and ask: "Spend up to [amount] (Recommended)", "Spend less: only primary keywords", "No paid calls". Stay within the answer.
3. "Are there keywords you already know your buyers use?" with "No, find them (Recommended)", "Yes, I'll type them".

## Data source chain
Use sources in this order, stopping at the first that answers each keyword: the user's export; the user's preferred connector (OpenSEO by default); the next usable connector (Ahrefs, Semrush, Ubersuggest, any other) for the remaining keywords; otherwise estimates from search autocomplete plus the ranking check. Rules:
- Pass the country and language codes of each section 2 row to every call; never rely on a project's default market.
- Record source and date next to every number. Never average or mix numbers from different tools in one column.
- Say which keywords are measured and which are estimated, and when a fallback happened.
- On a quota, plan or no-data error, do not retry: report it briefly and move to the next source. Never block the workflow.

## Connector notes
- Read each tool's description before the first call; prefer few, well-chosen calls.
- **OpenSEO:** keyword research tools for demand and difficulty; SERP tools for who ranks.
- **Ahrefs:** call `doc` before a tool's first use; `keywords-explorer-*` for volume, difficulty and related terms, `serp-overview` for top results, `site-explorer-*` for rivals. Monetary values are in USD cents (divide by 100). When a result says to render with a render tool, call it. Some plans return "Insufficient plan": report it and move on.
- **Semrush:** `keyword_research`, `competitors_research`, then `get_report_schema` and `execute_report`. An API-units error means the account needs more units: report it and move on.
- After launch, any connector linked to Google Search Console shows the real queries; suggest re-weighting then.
- Free or limited plans may return part of the data: say exactly what was and was not returned.

## Keyword research (per language and region)
- Never translate keywords: research each language for its own region.
- Sources: search suggestions, benchmark titles and headings, customer phrases, SEO tool data.
- Cover every awareness level in section 3: problem terms for problem-aware visitors, solution and comparison terms for solution-aware ones, provider terms for product-aware ones.
- For each keyword: language/region, intent, demand (measured or signal), competition (difficulty or signal), page types ranking.
- Drop terms the business cannot or should not answer (health claims, superlatives, restricted or "do not use" items in section 1), with the reason.

## Ranking check
For each primary keyword, run the real search in its language and region and record the top 10: who ranks, page type (shop, directory, marketplace, blog, authority, social), and for the 2 or 3 strongest relevant results, title and H1 and their angle. If the connector only compares domains and gives no page-level results, run a web search, read the top 3 pages, and label the check "partial". Note whether benchmark sites rank, whether results are price-led or brand-led, and any price gap with the business (flag it; do not change the offer here).

## Weighting and clusters
Score each primary keyword 1 to 5 on demand, competition (5 = weak competition), fit and visitor value, out of 20; label scores as judgement when no tool data exists. Decide per cluster: target, supporting term or answer. Say plainly when buyers type almost nothing into search, and list cheap channels the results reveal. One primary keyword per page plus 3 to 6 secondary terms; a cluster with no natural page is a candidate page; a page with no cluster needs a reason; no two pages compete for one keyword. If a language has no known audience or no measurable demand, flag it for the site structure stage instead of planning pages for it.

## On-page rules (used by the page copy stage)
Title 50 to 60 characters, keyword near the start, brand at the end. Meta description 140 to 160 characters: a benefit and a reason to click. One H1 containing the primary keyword naturally; H2 and H3 reflect secondary terms and real questions. No stuffing. Each page links to its parent, 2 to 3 related pages and the conversion page. Alt text describes the image; include a keyword only if it is natural. Answer common questions in short, direct sections where intent is informational. The offer name is not a search term: titles and H1s lead with the searched keyword.

## Geo-localization (how often the location appears)
Read `references/geo-localization.md` first. Using the place in section 1, the local search demand and local intent seen in the research and ranking check, the place-related objections in section 3, the markets also served, the benchmark's location use and the voice notes, recommend one level per language: headings, body, contact and footer, or not mentioned. Give two or three reasons from the evidence and the risk of the levels above and below. Ask the user to confirm the level (one question, recommendation first), then which places to name. Record the decision in the Geo-localization table of section 7 and as a section 10 row of type `location`. If section 1 has no place, ask for it first, or record "not mentioned" with the reason.

## Multilingual setup
Confirm the URL structure with one question: "Subfolders per language (Recommended)", "Subdomains per language", "Separate domains per country". hreflang pairs including `x-default`; the language switcher links to the equivalent page; right-to-left languages set `dir="rtl"`.

## Optional, later
Schema markup (Organization, LocalBusiness, FAQ, Service) and programmatic pages only if the site really needs many templated pages. Mention them as options; do not add them by default.

## Steps
Run the questions, research, ranking check, weighting and clusters, then the geo-localization recommendation and the user's decision; write the files; show the clusters ranked by weight with primary keywords, what ranks today, the URL strategy, the geo-localization level per language and how strong the data is; run the quality check; share the brief. Then ask: "Looks right, continue to the site structure (Recommended)", "Add keywords I know", "Remove or merge a cluster". The keyword mapping is approved at the site structure gate.

## Guardrails
- Never present an estimate as a measured number.
- Never use a restricted or "do not use" term as a primary or secondary keyword.
- Never exceed the budget the user approved.

## Quality check
| Item | Pass when |
|---|---|
| **Goal** | Every page type the site needs has a cluster or a stated reason, in every section 2 language that has an audience |
| Data | Every number has source and date; fallbacks and estimates are labelled |
| Ranking check | Top results are recorded for every primary keyword, or the check is labelled partial with its method |
| Weights | Each criterion is scored; judgement is labelled |
| Restricted terms | None is a primary or secondary keyword; dropped terms have reasons |
| Mapping | One primary keyword per cluster; no two clusters on one page |
| Demand | A thin-demand warning and cheap channels are given when demand is low |
| Languages | Every language without an audience or without measurable demand is flagged for the site structure stage |
| Budget | Paid calls stayed within the approved amount |
| Geo-localization | Every language has a level confirmed by the user, the places to name as written, and reasons tied to evidence (local demand, local intent, place-related objections, markets also served); recorded in section 7 and as a `location` row in section 10 |
| Requirements | Section 10 rows touching SEO are `verified` |
| Brief visible | The brief was shared after every change |
