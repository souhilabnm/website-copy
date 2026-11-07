#!/usr/bin/env node
/* Output check for the website wireframe built by build_wireframe.py.
   Usage: node check_wireframe.js PATH/TO/<business>-wireframe.html [SCREENSHOT_DIR]
   Needs Playwright (require('playwright') or 'playwright-core'); set CHROME_PATH to use a specific browser.
   Prints one line per check and exits 1 if anything fails. */
const path = require('path');
let pw; try { pw = require('playwright'); } catch (e) { try { pw = require('playwright-core'); } catch (e2) { console.error('Playwright not found: npm i playwright-core'); process.exit(2); } }
const FILE = 'file://' + path.resolve(process.argv[2] || '');
const SHOTS = process.argv[3];
const LEGAL_RE = /privacy|legal|terms|cookie|mentions|datenschutz|impressum/i;
(async () => {
  const opts = { args: ['--no-sandbox'] };
  if (process.env.CHROME_PATH) opts.executablePath = process.env.CHROME_PATH;
  let b; try { b = await pw.chromium.launch(opts); } catch (e) {
    for (const p of ['/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser']) { try { b = await pw.chromium.launch({ ...opts, executablePath: p }); break; } catch (e2) {} }
  }
  if (!b) { console.error('No browser could be launched'); process.exit(2); }
  const bad = [], ok = [], errs = [], reqs = [];
  const p = await (await b.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
  p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  p.on('pageerror', e => errs.push('PAGEERR ' + e.message));
  p.on('request', r => { if (!/^(file|data|about|blob):/.test(r.url())) reqs.push(r.url()); });
  const go = async h => { await p.goto(FILE + h); await p.reload(); await p.waitForTimeout(120); };
  await go('#sm');
  const D = await p.evaluate(() => window.D);
  if (!D) { console.error('No data in the file'); process.exit(1); }
  const written = D.ORDER.filter(pid => D.LANGS.some(l => !D.PAGES[pid][l].stub));
  const navSig = new Set(), seq = {};
  for (const pid of written) for (const l of D.LANGS) {
    const pg = D.PAGES[pid][l]; if (pg.stub) continue;
    seq[pid] = seq[pid] || new Set(); seq[pid].add(pg.sections.map(s => s.type).join(','));
    for (const w of [1440, 390]) {
      await p.setViewportSize({ width: w, height: 900 });
      await go('#wf/' + l + '/' + pid);
      await p.click('.devices button[data-w="' + w + '"]');
      const tag = pid + '/' + l + '/' + w;
      const txt = (await p.innerText('#app')).toLowerCase();
      for (const x of ['undefined', 'null', 'lorem', 'goes here', 'to be confirmed', '[to verify']) if (txt.includes(x)) bad.push(tag + ': text contains "' + x + '"');
      const dir = await p.evaluate(() => document.documentElement.dir);
      if ((D.RTL.indexOf(l) >= 0) !== (dir === 'rtl')) bad.push(tag + ': dir=' + dir);
      const ov = await p.evaluate(() => { const f = document.getElementById('frame'); return f.scrollWidth - f.clientWidth; });
      if (ov > 2) bad.push(tag + ': horizontal overflow ' + ov + 'px');
      const prim = await p.evaluate(() => [...document.querySelectorAll('.site section .btn')].filter(x => !x.classList.contains('o')).length);
      if (prim > 3) bad.push(tag + ': ' + prim + ' primary buttons in the body (max 3)');
      const ph = await p.evaluate(() => [...document.querySelectorAll('.site section .ph')].filter(x => !x.closest('.tool')).map(x => x.closest('section').dataset.type));
      if (ph.some(t => t !== 'Header' && t !== 'About' && t !== 'Feature')) bad.push(tag + ': image placeholder outside a split Header, About or alternating Feature: ' + ph.join(','));
      navSig.add(await p.evaluate(() => [...document.querySelectorAll('#nv .lk')].map(a => a.getAttribute('onclick')).join('|')));
      const nTools = pg.sections.filter(s => s.type === 'Tool').length;
      const rTools = await p.$$eval('.site .tool', t => t.length);
      if (nTools !== rTools) bad.push(tag + ': ' + nTools + ' tools planned, ' + rTools + ' rendered');
      if (await p.$('.qa button')) { await p.click('.qa button'); if (!(await p.evaluate(() => document.querySelector('.qa').classList.contains('open')))) bad.push(tag + ': FAQ row did not open'); }
      const emptyAs = await p.$$eval('.as', a => a.filter(x => !(x.firstChild && x.firstChild.textContent.trim())).length);
      if (emptyAs) bad.push(tag + ': ' + emptyAs + ' empty assumption highlights');
      if (w === 390) {
        if ((await p.evaluate(() => getComputedStyle(document.querySelector('.burger')).display)) === 'none') bad.push(tag + ': no menu button on mobile');
        else { await p.click('.burger'); if (!(await p.evaluate(() => [...document.querySelectorAll('#nv .lk')].every(a => a.offsetParent !== null)))) bad.push(tag + ': menu not reachable on mobile'); }
      } else {
        const f0 = await p.evaluate(() => document.body.classList.contains('noflag')); await p.click('#tFlags');
        if (f0 === (await p.evaluate(() => document.body.classList.contains('noflag')))) bad.push(tag + ': Flags toggle has no effect');
        await p.click('#tFlags'); await p.click('#tSeo');
        if ((await p.evaluate(() => getComputedStyle(document.querySelector('.seob')).display)) === 'none') bad.push(tag + ': SEO toggle has no effect');
        const t = (pg.title || '').replace(/\{\{ASSUMED: (.*?)\}\}/g, '$1').length, m = (pg.meta || '').replace(/\{\{ASSUMED: (.*?)\}\}/g, '$1').length;
        if (!LEGAL_RE.test(pid) && (t < 50 || t > 60 || m < 140 || m > 160)) bad.push(tag + ': SEO title ' + t + ' / meta ' + m + ' characters (50-60 / 140-160)');
        ok.push(tag + ': ' + pg.sections.map(s => s.type).join(',') + ' | primary buttons ' + prim + ' | title ' + t + ' meta ' + m);
        await p.click('#tSeo');
      }
    }
  }
  if (navSig.size !== 1) bad.push('menu differs between pages or languages (' + navSig.size + ' versions)');
  for (const pid in seq) if (seq[pid].size > 1) bad.push(pid + ': section order differs between languages');
  for (const l of D.LANGS) {
    await p.setViewportSize({ width: 1440, height: 900 });
    await go('#sm/' + l);
    const cols = await p.$$eval('.col', c => c.length);
    if (cols !== D.ORDER.length) bad.push('sitemap/' + l + ': ' + cols + ' columns for ' + D.ORDER.length + ' pages');
    if (!(await p.$$eval('#lines path', x => x.length))) bad.push('sitemap/' + l + ': connector lines missing');
    if (await p.$$eval('.sc', c => c.filter(x => !x.textContent.trim()).length)) bad.push('sitemap/' + l + ': empty cards');
    for (const pid of written) {
      const pg = D.PAGES[pid][l]; if (pg.stub) continue;
      const n = await p.$$eval('.col[data-p="' + pid + '"] .sc[data-sec]', c => c.length);
      if (n !== pg.sections.length) bad.push('sitemap/' + l + '/' + pid + ': ' + n + ' cards for ' + pg.sections.length + ' sections');
    }
    ok.push('sitemap/' + l + ': ' + cols + ' columns');
    if (SHOTS) await p.screenshot({ path: path.join(SHOTS, 'sitemap-' + l + '.png') });
  }
  const pid0 = written[0], l0 = D.LANGS.find(l => !D.PAGES[pid0][l].stub), last = D.PAGES[pid0][l0].sections.length - 1;
  await go('#sm/' + l0); await p.click('.col[data-p="' + pid0 + '"] .sc[data-sec="' + last + '"]'); await p.waitForTimeout(150);
  const top = await p.evaluate(id => { const e = document.getElementById(id); return e ? e.getBoundingClientRect().top : 9999; }, 's-' + pid0 + '-' + last);
  if (top > 250 || top < -50) bad.push('sitemap card click does not land on its section');
  await go('#wf/' + l0 + '/' + pid0); await p.click('#mAll');
  if ((await p.$$eval('.thumb', t => t.length)) !== D.ORDER.length) bad.push('All pages view does not show every page');
  const stub = D.ORDER.find(pid => D.PAGES[pid][l0].stub);
  if (stub) { await go('#wf/' + l0 + '/' + pid0); await p.evaluate(s => go(s), stub); if (!(await p.innerText('#note')).trim()) bad.push('link to an unwritten page shows no note'); }
  await go('#wf/' + l0 + '/' + pid0);
  const other = D.LANGS.find(l => l !== l0);
  if (other) { await p.selectOption('#langSel', other); if (!(await p.evaluate(() => location.hash)).includes('/' + other)) bad.push('language dropdown does not switch language'); }
  if (SHOTS) { await go('#wf/' + l0 + '/' + pid0); await p.screenshot({ path: path.join(SHOTS, 'wireframe-' + l0 + '-' + pid0 + '.png') }); }
  ok.forEach(x => console.log('ok  ' + x));
  console.log('console errors: ' + (errs.length ? errs.join(' | ') : 'none'));
  console.log('external requests: ' + (reqs.length ? reqs.join(' | ') : 'none'));
  if (errs.length || reqs.length) bad.push('console errors or external requests');
  bad.forEach(x => console.log('FAIL ' + x));
  console.log(bad.length ? 'RESULT: ' + bad.length + ' failure(s)' : 'RESULT: all checks passed');
  await b.close(); process.exit(bad.length ? 1 : 0);
})();
