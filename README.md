# Website Copy

Builds the full copy of a multi-page website, stage by stage, with the client's approval at every step.

## Install
In Claude Code:
```
/plugin marketplace add souhilabnm/website-copy
/plugin install website-copy@souhilabnm
```
To get a new version later: `/plugin marketplace update souhilabnm`, then update the plugin from `/plugin`.

## How it works
Start with **website-copy-builder** ("build the website copy for my client"). It runs nine stages in order; each stage can also be run alone:

1. **site-copy-intake**: the business as sourced facts, the claims it wants to make, voice references, tools, regions and languages.
2. **site-copy-audience**: pains in buyers' own words, objections, personas per language, competitors.
3. **site-copy-benchmark**: 5 to 8 comparable sites, researched and shared by the client (a document, pasted notes or links), with what the client likes about each; what to borrow, avoid and differentiate on.
4. **site-copy-offer**: an offer the client can deliver, scored with the value equation.
5. **site-copy-positioning**: one provable promise and a voice, grounded in a voice benchmark.
6. **site-copy-seo**: keywords per language and region, with the strength of the data stated, and a recommended geo-localization level (how often the business's place appears in the copy) that the client confirms.
7. **site-copy-ia**: the site structure; each page gets a goal, and each section answers a visitor question from the brief.
8. **site-copy-pages**: the copy of every page in every language, shown in a wireframe with a Sitemap view and a Wireframe view.
9. **site-copy-qa**: checks, cold readers, and the final copy deck.

Every run is a real client project: there is no test mode.

Rules shared by every stage: one question at a time; the brief (`brief.md`) is shared in the chat after every change; every change the user asks for becomes a tracked requirement; every stage ends with a quality check against its goal.

The research skills **customer-pain-point-collection**, **persona-research** and **market-competition-research** are used by the audience stage and also work alone.

## What you need
- Python 3 to build the wireframe (`skills/site-copy-pages/scripts/build_wireframe.py`).
- Node.js with Playwright to run the automated check (`skills/site-copy-pages/scripts/check_wireframe.js`); without it the skill does a labelled manual check.
- Optional connectors: Firecrawl for research; an SEO tool (OpenSEO, Ahrefs, Semrush, Ubersuggest) for keyword data. Without them the skills fall back to web search and labelled estimates.

## The wireframe
The design lives in `skills/site-copy-pages/templates/wireframe_template.html`. It is an empty shell: opened alone it shows a short note. The page-copy skill fills it from the project's page data and produces one HTML file with every page.
