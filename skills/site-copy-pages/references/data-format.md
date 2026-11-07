# Page data format

Read this before writing `site.json` or any `pages/<slug>.json`.

`site.json`:
```
{"brand": "...", "langs": ["xx", "yy"], "rtl": ["yy"], "order": ["home", "..."],
 "names": {"home": {"xx": "...", "yy": "..."}}, "slugs": {"home": {"xx": "/xx/", "yy": "/yy/"}},
 "offered": {"home": ["xx", "yy"], "...": ["xx"]},
 "nav": {"items": [{"id": "page"}, {"label": {"xx": "..."}, "children": ["page", "page"]}], "cta": [{"xx": "..."}, "page"]},
 "footer": {"columns": [["page"], ["page"]], "titles": {"xx": ["...", "..."]}, "copy": {"xx": "..."}, "legal": "page"},
 "ui": {"xx": {}}, "types": {"xx": {}}, "assume": {"xx": "..."}}
```
`ui`, `types` and `assume` are needed only for languages the script does not already know (it knows en, fr, ar, de).
`pages/<slug>.json`:
```
{"slug": "home", "langs": {"xx": {"title": "...", "meta": "...", "sections": [
  {"type": "Header", "variant": "split", "tag": "...", "desc": "sitemap card text", "q": "visitor question", "ans": "s6 core promise",
   "src": {"h1": "...", "sub": "...", "btn": ["label", "contact"], "tlink": ["label", "page"], "image": true}},
  {"type": "Comparison", "desc": "...", "q": "...", "ans": "s5 core stack",
   "src": {"h2": "...", "p": "...", "head": ["", "A", "B"], "rows": [["For", "...", "..."], ["Price", "...", "..."]], "links": [["label", "page"]]}},
  {"type": "Tool", "desc": "...", "q": "...", "ans": "...", "tool": {"kind": "booking", "tag": "tool name", "h2": "...", "sub": "...", "label": "...", "fb": "fallback line", "ok": "button"}}
]}}}
```
Link targets are a page id, or `page#n` for section n of that page. Unknown facts are written inside the copy as `{{ASSUMED: complete text}}` (one space after the colon). `desc` is the sitemap card: 1 to 3 lines saying what this section contains on this site, quoting its real heading or button.

