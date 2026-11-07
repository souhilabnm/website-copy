# Geo-localization: how often the location appears in the copy

Read this before recommending the geo-localization level. The decision says where, and how often, the business's place (country, province or region, city) is named in the copy, per site language. The user confirms it; the SEO stage only recommends.

## The four levels
| Level | Where the place is named | Fits when |
|---|---|---|
| **Headings** | SEO title and H1 of the key pages, H2 or H3 where natural, plus body, contact page, footer and schema | Buyers search with the place ("web agency Montreal"), the results for the primary keyword are local (map pack, local directories, local firms), and the business serves mainly that place |
| **Body** | Sentences in the body of key pages (for example a proof line, how it works, about), plus contact page, footer and schema; never in titles or headings | The place is a trust or practical reason to buy (time zone, regional language variant, currency, local law, in-person meetings), but buyers do not search with the place, or the business also serves other markets |
| **Contact and footer** | Contact page, footer address line and schema only | The place is a plain fact that buyers may want to check, but it is not a reason to buy, and the business works for clients anywhere |
| **Not mentioned** | Nowhere in the copy, except where a law requires an address (legal notice, privacy policy) | The client does not want to be seen as local, or naming the place would narrow the audience with no gain |

Levels can differ per language: a fr-CA version may name Quebec in the body while the en version names only Canada in the footer, and a fr-FR version may name nothing.

## Evidence to gather (record each with its source in `analysis/06-seo.md`)
1. **Local search demand.** For each primary keyword, check the same keyword with the place added (country, province or region, main city) in that language and region. Compare measured volumes when a tool returns them; otherwise use autocomplete and say it is a signal.
2. **Local intent in the results.** In the ranking check, note whether the top results for the primary keyword show a map pack, local directories or firms from that place. Local results mean the search engine treats the intent as local.
3. **Why the place matters to buyers.** From section 3: objections or pains tied to place (time zone, language variant, currency, taxes, local law, meeting in person). From section 1: whether the business works in person or remotely.
4. **Markets beyond the base.** From section 1: markets the business also serves (for example based in Montreal, also working for clients in France). A city in the H1 tells those visitors the site is not for them.
5. **What comparable sites do.** From section 4: where the benchmark sites name their place, and how often.
6. **Voice and positioning.** From section 6: a voice trait or pillar that relies on place (for example "local").

## Recommending
- Recommend one level per language, with two or three reasons tied to the evidence above, and name the risk of the level above and the level below (over-localizing narrows the audience; under-localizing misses local searches and a trust signal).
- When the business also serves other markets, do not recommend Headings unless local demand clearly outweighs those markets; prefer Body with a line that names both ("Based in Montreal, working with agencies in Canada and France").
- Use only places the brief sources (section 1 Location). Never invent an office, a city served or an address.
- Name the exact wording of the place per language (for example "Montréal" in French, "Montreal" in English; "Québec" for the province) and whether markets served beyond the base are named too.

## Asking
Ask one question per language, or one for all languages when the recommendation is the same:
"How often should the location appear in the [language] copy?" with the recommended level first, ending in "(Recommended)", then the other three levels, each with a one-line description of where the place appears. Then, if a place will appear, ask one question about which places to name (for example "Canada only", "Quebec and Canada", "Montreal, Quebec and Canada", "Montreal, plus the markets also served"), built from section 1.

Record the answer as a section 10 row of type `location` (the user's words, status `applied` once written into section 7). The site structure stage turns it into a placement table, the page copy stage writes it, and the QA stage counts it.

## What to write in section 7
```
### Geo-localization
| Language | Level (headings / body / contact and footer / not mentioned) | Places named, as written | Markets also served, named in copy? | Reasons (evidence) | Decided by the user on |
|---|---|---|---|---|---|
```
