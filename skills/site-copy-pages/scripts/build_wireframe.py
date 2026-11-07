#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the two-view website wireframe (Sitemap | Wireframe) from page data.

Usage:  python3 build_wireframe.py PROJECT_FOLDER [TEMPLATE_HTML]

Reads   PROJECT_FOLDER/site.json and PROJECT_FOLDER/pages/<slug>.json
Writes  PROJECT_FOLDER/<business-slug>-wireframe.html
Prints  a summary per page and language (sections, words, assumptions, title and meta length)
        that the quality check uses. Exits 1 on any data error or structure mismatch
        between languages, without writing the file.
Template default: ../templates/wireframe_template.html next to this script.
"""
import json, os, re, sys, glob, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "..", "templates", "wireframe_template.html")
TYPES = {"Header", "Content", "About", "Feature", "Process", "Pricing", "Testimonial", "FAQ", "CTA", "Form", "Legal", "Tool",
         "Stats", "Comparison", "Logos"}
VARIANTS = {"Header": {"split", "centered", "text"}, "Feature": {"grid", "list", "alternating"}, "CTA": {"dark", "box"},
            "Testimonial": {"statement", "cards", "single"}}
TOOL_KINDS = {"booking", "reviews", "video", "generic"}
RTL = ["ar", "he", "fa", "ur"]
LANGNAMES = {"en": "English", "fr": "Français", "ar": "العربية", "de": "Deutsch", "es": "Español", "it": "Italiano",
             "nl": "Nederlands", "pt": "Português", "tr": "Türkçe", "he": "עברית", "fa": "فارسی", "ur": "اردو"}
UI = {
 "en": {"more": "Learn more", "still": "Still have questions?", "write": "Write to us", "third": "Third-party tool", "all": "All pages",
        "open": "Open in wireframe", "pages": "pages", "nopage": "This link has no target page yet.", "notwritten": "Not written yet",
        "answers": "Answers", "notlang": "Not available in this language"},
 "fr": {"more": "En savoir plus", "still": "D'autres questions ?", "write": "Écrivez-nous", "third": "Outil tiers", "all": "Toutes les pages",
        "open": "Ouvrir dans la maquette", "pages": "pages", "nopage": "Ce lien n'a pas encore de page cible.", "notwritten": "Pas encore rédigée",
        "answers": "Répond à", "notlang": "Non disponible dans cette langue"},
 "ar": {"more": "اعرف المزيد", "still": "هل لديك أسئلة أخرى؟", "write": "راسلنا", "third": "أداة خارجية", "all": "كل الصفحات",
        "open": "فتح في الهيكل", "pages": "صفحات", "nopage": "لا توجد صفحة لهذا الرابط بعد.", "notwritten": "لم تُكتب بعد",
        "answers": "يجيب عن", "notlang": "غير متاحة بهذه اللغة"},
 "de": {"more": "Mehr erfahren", "still": "Noch Fragen?", "write": "Schreiben Sie uns", "third": "Drittanbieter-Tool", "all": "Alle Seiten",
        "open": "Im Wireframe öffnen", "pages": "Seiten", "nopage": "Dieser Link hat noch keine Zielseite.", "notwritten": "Noch nicht geschrieben",
        "answers": "Beantwortet", "notlang": "In dieser Sprache nicht verfügbar"},
}
TYPE_LABELS = {
 "en": {"Navbar": "Navbar", "Header": "Header Section", "Content": "Content Section", "About": "About Section", "Feature": "Feature Section",
        "Process": "Process Section", "Pricing": "Pricing Section", "Testimonial": "Testimonial Section", "FAQ": "FAQ Section", "CTA": "CTA Section",
        "Form": "Contact Form Section", "Legal": "Legal Page Body", "Tool": "Third-party Widget", "Footer": "Footer", "Stats": "Stats Section", "Comparison": "Comparison Section", "Logos": "Logo Strip"},
 "fr": {"Navbar": "Barre de navigation", "Header": "Section En-tête", "Content": "Section Contenu", "About": "Section À propos",
        "Feature": "Section Fonctionnalités", "Process": "Section Étapes", "Pricing": "Section Tarifs", "Testimonial": "Section Témoignages",
        "FAQ": "Section FAQ", "CTA": "Section CTA", "Form": "Section Formulaire de contact", "Legal": "Corps de page légale", "Tool": "Widget tiers",
        "Footer": "Pied de page", "Stats": "Section Chiffres", "Comparison": "Section Comparatif", "Logos": "Bandeau de logos"},
 "ar": {"Navbar": "شريط التنقل", "Header": "قسم الترويسة", "Content": "قسم المحتوى", "About": "قسم من نحن", "Feature": "قسم الميزات",
        "Process": "قسم الخطوات", "Pricing": "قسم الأسعار", "Testimonial": "قسم الآراء", "FAQ": "قسم الأسئلة الشائعة", "CTA": "قسم الدعوة إلى إجراء",
        "Form": "قسم نموذج الاتصال", "Legal": "نص الصفحة القانونية", "Tool": "أداة خارجية", "Footer": "التذييل", "Stats": "قسم الأرقام", "Comparison": "قسم المقارنة", "Logos": "شريط الشعارات"},
 "de": {"Navbar": "Navigationsleiste", "Header": "Header-Abschnitt", "Content": "Inhaltsabschnitt", "About": "Über-uns-Abschnitt",
        "Feature": "Feature-Abschnitt", "Process": "Ablauf-Abschnitt", "Pricing": "Preis-Abschnitt", "Testimonial": "Stimmen-Abschnitt",
        "FAQ": "FAQ-Abschnitt", "CTA": "CTA-Abschnitt", "Form": "Kontaktformular", "Legal": "Rechtstext", "Tool": "Drittanbieter-Widget",
        "Footer": "Fußzeile", "Stats": "Zahlen-Abschnitt", "Comparison": "Vergleichs-Abschnitt", "Logos": "Logo-Leiste"},
}
ASSUME = {"en": "Assumption: must be verified", "fr": "Hypothèse : à vérifier", "ar": "افتراض: يجب التحقق منه", "de": "Annahme: muss geprüft werden"}
AS_RE = re.compile(r"\{\{ASSUMED: (.*?)\}\}")
errors = []

def err(msg): errors.append(msg)
def plain(t): return AS_RE.sub(r"\1", t)
def slugify(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-") or "site"

def strings(o, pids):
    """All visitor-facing strings of a section (link targets excluded)."""
    if isinstance(o, str):
        return [] if (o in pids or re.fullmatch(r"[a-z0-9-]+#\d+", o)) else [o]
    if isinstance(o, list): return [s for x in o for s in strings(x, pids)]
    if isinstance(o, dict): return [s for k, v in o.items() if k not in ("desc", "variant", "type", "kind", "links", "image") for s in strings(v, pids)]
    return []

def words(texts, lang):
    t = " ".join(plain(x) for x in texts)
    return len(t.split())

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    proj = sys.argv[1]; tpl_path = sys.argv[2] if len(sys.argv) > 2 else TEMPLATE
    site = json.load(open(os.path.join(proj, "site.json"), encoding="utf-8"))
    for k in ("brand", "langs", "order", "names", "nav", "footer"):
        if k not in site: err("site.json: missing '%s'" % k)
    if errors: fail()
    langs, order = site["langs"], site["order"]; pids = set(order)
    offered = site.get("offered", {p: langs for p in order})
    for p in order:
        for l in langs:
            if l not in site["names"].get(p, {}): err("site.json names: '%s' has no name in '%s'" % (p, l))
    ui, types, assume = {}, {}, {}
    for l in langs:
        ui[l] = dict(UI.get(l, {})); ui[l].update(site.get("ui", {}).get(l, {}))
        types[l] = dict(TYPE_LABELS.get(l, {})); types[l].update(site.get("types", {}).get(l, {}))
        assume[l] = site.get("assume", {}).get(l) or ASSUME.get(l)
        missing = [k for k in UI["en"] if k not in ui[l]] + [k for k in TYPE_LABELS["en"] if k not in types[l]]
        if not assume[l]: missing.append("assume")
        if missing: err("site.json: language '%s' needs ui/types/assume entries: %s" % (l, ", ".join(missing)))
        ui[l]["foot"] = site["footer"]["titles"][l]; ui[l]["copy"] = site["footer"]["copy"][l]
    pages = {}
    for f in sorted(glob.glob(os.path.join(proj, "pages", "*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        if d.get("slug") not in pids: err("%s: slug '%s' is not in site.json order" % (os.path.basename(f), d.get("slug"))); continue
        pages[d["slug"]] = d
    data_pages, summary = {}, []
    for p in order:
        data_pages[p] = {}
        seqs = {}
        for l in langs:
            pl = pages.get(p, {}).get("langs", {}).get(l)
            if l not in offered.get(p, langs):
                if pl: err("%s/%s: written but not offered in this language (site.json 'offered')" % (p, l))
                data_pages[p][l] = {"title": site["names"][p][l], "meta": "", "sections": [], "stub": "notlang"}; continue
            if not pl:
                data_pages[p][l] = {"title": site["names"][p][l], "meta": "", "sections": [], "stub": "notwritten"}; continue
            secs = []
            for i, s in enumerate(pl.get("sections", [])):
                t = s.get("type")
                if t not in TYPES: err("%s/%s section %d: type '%s' is not supported (%s)" % (p, l, i, t, ", ".join(sorted(TYPES))))
                if not str(s.get("desc", "")).strip(): err("%s/%s section %d: empty sitemap description" % (p, l, i))
                if t == "Tool" and s.get("tool", {}).get("kind") not in TOOL_KINDS: err("%s/%s section %d: tool kind must be one of %s" % (p, l, i, sorted(TOOL_KINDS)))
                if t == "Header" and not s.get("src", {}).get("h1"): err("%s/%s: Header without h1" % (p, l))
                if t != "Legal" and not str(s.get("q", "")).strip(): err("%s/%s section %d: no visitor question ('q') - every section must answer one" % (p, l, i))
                if t != "Legal" and not str(s.get("ans", "")).strip(): err("%s/%s section %d: no answer source ('ans', the brief section that holds the answer)" % (p, l, i))
                if t in VARIANTS and s.get("variant") and s["variant"] not in VARIANTS[t]: err("%s/%s section %d: variant '%s' not supported for %s %s" % (p, l, i, s["variant"], t, sorted(VARIANTS[t])))
                s = dict(s); s.setdefault("src", {}); s["has"] = "{{ASSUMED:" in json.dumps(s, ensure_ascii=False)
                if "{{ASSUMED: }}" in json.dumps(s, ensure_ascii=False) or "{{ASSUMED:}}" in json.dumps(s, ensure_ascii=False): err("%s/%s section %d: empty assumption" % (p, l, i))
                secs.append(s)
            seqs[l] = [(s["type"], s.get("variant", "")) for s in secs]
            texts = [x for s in secs for x in strings(s, pids)]
            n_as = sum(len(AS_RE.findall(x)) for x in texts)
            title, meta = pl.get("title", ""), pl.get("meta", "")
            data_pages[p][l] = {"title": title, "meta": meta, "sections": secs}
            summary.append((p, l, len(secs), words(texts, l), n_as, len(plain(title)), len(plain(meta))))
        if len(set(map(tuple, seqs.values()))) > 1:
            err("%s: sections differ between languages: %s" % (p, {k: [t for t, _ in v] for k, v in seqs.items()}))
    if errors: fail()
    shapes = {}
    for p in order:
        for l in langs:
            d = data_pages[p][l]
            if not d.get("stub") and not any(x["type"] == "Legal" for x in d["sections"]):
                shapes.setdefault(tuple((x["type"], x.get("variant", "")) for x in d["sections"]), set()).add(p); break
    same = [sorted(v) for v in shapes.values() if len(v) > 1]
    data = {"PAGES": data_pages, "ORDER": order, "SLUG": site.get("slugs", {p: {l: "/" + l + "/" + p for l in langs} for p in order}),
            "NAMES": site["names"], "BRAND": site["brand"], "LANGS": langs, "LANGNAMES": {l: site.get("lang_names", {}).get(l) or LANGNAMES.get(l, l.upper()) for l in langs},
            "RTL": site.get("rtl", [l for l in langs if l in RTL]), "TYPE": types, "UI": ui, "ASSUME": assume,
            "NAV": site["nav"], "FCOLS": site["footer"]["columns"], "LEGAL": site["footer"]["legal"]}
    tpl = open(tpl_path, encoding="utf-8").read()
    if "/*DATA*/" not in tpl: sys.exit("template has no /*DATA*/ slot: %s" % tpl_path)
    html = tpl.replace("/*DATA*/", "window.D=" + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + ";")
    out = os.path.join(proj, slugify(site["brand"]) + "-wireframe.html")
    open(out, "w", encoding="utf-8").write(html)
    print("wrote", out, len(html), "bytes")
    print("page | lang | sections | words | assumptions | title chars | meta chars")
    for r in summary: print(" | ".join(str(x) for x in r))
    for g in same: print("SAME SKELETON on pages %s: justify it in the page plan or vary the sections" % ", ".join(g))
    print("section plan (first language):")
    for p in order:
        l0 = next((l for l in langs if not data_pages[p][l].get("stub")), None)
        if not l0: continue
        for i, x in enumerate(data_pages[p][l0]["sections"]):
            print("  %s #%d %s/%s | answers: %s | from: %s" % (p, i, x["type"], x.get("variant", "-"), x.get("q", "-"), x.get("ans", "-")))

def fail():
    print("BUILD FAILED"); [print(" -", e) for e in errors]; sys.exit(1)

if __name__ == "__main__":
    main()
