# -*- coding: utf-8 -*-
"""Собирает storyboard.html из RASKADROVKA/sheets.json.

Шапка и скрипт — из tools/page-head.html и tools/page-tail.html.
Запускать после build_sheets.py, из корня репозитория.
"""
import io, json, os, re

BASE = 'shahruhiya'
SHEETS = os.path.join(BASE, 'RASKADROVKA', 'sheets.json')

ACTS = {
    u'АКТ 1 — Ташкент и туннель':      ('act1', '#7E94AC', u'Акт 1 · Ташкент и туннель'),
    u'АКТ 2 — Степь и лагерь':         ('act2', '#C9954A', u'Акт 2 · Степь и лагерь'),
    u'Шатёр Темура':                   ('tent', '#A8552E', u'Шатёр Темура'),
    u'АКТ 3 — Гонка':                  ('race', '#D9682F', u'Акт 3 · Гонка'),
    u'АКТ 3 — Имя, перстень, финал':   ('fin',  '#C3A551', u'Акт 3 · Имя, перстень, финал'),
}


def timecodes():
    """кадр → тайм-код из покадровой таблицы сценария."""
    out = {}
    for ln in io.open(os.path.join(BASE, 'SCENARIY.md'), encoding='utf-8'):
        m = re.match(r'^\|\s*(\d+)\s*\|\s*(\d+:\d+)\s*\|', ln)
        if m:
            out.setdefault(int(m.group(1)), m.group(2))
    return out


def esc(t):
    return (t.replace(u'&', u'&amp;').replace(u'<', u'&lt;')
             .replace(u'>', u'&gt;').replace(u"'", u'&#x27;'))


TC = timecodes()
sheets = json.load(io.open(SHEETS, encoding='utf-8'))
head = io.open(os.path.join(BASE, 'tools', 'page-head.html'), encoding='utf-8').read()
tail = io.open(os.path.join(BASE, 'tools', 'page-tail.html'), encoding='utf-8').read()

total = sum(len(s['panels']) for s in sheets)
six = sum(1 for s in sheets if len(s['panels']) == 6)
head = re.sub(r'<span class="bno">.*?</span>', '', head)   # на всякий случай
head = re.sub(r'\d+ панелей раскадровки, разложенных на \d+ партий по шесть\.',
              u'%d панелей раскадровки, разложенных на %d парти%s: %d ровно по шесть, '
              u'остальные меньше — панели одного кадра никогда не разносятся по разным '
              u'партиям, иначе у них разъедется рамка.'
              % (total, len(sheets),
                 u'ю' if len(sheets) % 10 == 1 and len(sheets) % 100 != 11 else
                 (u'и' if len(sheets) % 10 in (2, 3, 4) and len(sheets) // 10 % 10 != 1 else u'й'),
                 six), head)

def instr(k):
    return (u'Generate %d SEPARATE images, one for each numbered prompt below. '
            u'Each image must be 16:9. Do NOT merge them into a grid, collage or '
            u'contact sheet. Keep the visual style identical across all %d.' % (k, k))

parts = []
for sh in sheets:
    ps = sh['panels']
    block = ps[0]['block']
    key, acc, label = ACTS[block]
    shots = []
    for p in ps:
        if not shots or shots[-1][0] != p['shot']:
            shots.append((p['shot'], p['title']))
    tcs = [TC.get(s) for s, _ in shots if TC.get(s)]
    tc = (tcs[0] + u' – ' + tcs[-1]) if len(tcs) > 1 else (tcs[0] if tcs else u'')
    refs = []
    for p in ps:
        for r in [x.strip() for x in (p['ref'] or u'').split(',') if x.strip()]:
            if r not in refs:
                refs.append(r)

    A = parts.append
    A(u'<section class="batch" data-act="%s" data-ids="%s" style="--acc:%s">'
      % (key, u' '.join(p['id'] for p in ps), acc))
    A(u'<header class="bh">')
    A(u'  <span class="bno">%d<i>/%d</i></span>' % (sh['n'], len(sheets)))
    A(u'  <div class="bmeta"><span class="blab">%s</span>' % esc(label))
    A(u'  <span class="btc">%s</span></div>' % esc(tc))
    A(u'  <span class="bn">%d панел%s</span>'
      % (len(ps), u'ь' if len(ps) == 1 else (u'и' if len(ps) < 5 else u'ей')))
    A(u'  <button class="cpy" type="button">копировать партию</button>')
    A(u'</header>')
    A(u'<p class="shots">%s</p>'
      % u' · '.join(u'<b>%d</b> %s' % (n, esc(t)) for n, t in shots))
    if refs:
        A(u'<p class="note">Прикрепить эталоны: %s</p>' % esc(u'; '.join(refs)))
    notes = []
    for p in ps:
        if p.get('note') and (p['shot'], p['note']) not in notes:
            notes.append((p['shot'], p['note']))
    for shot, txt in notes:
        A(u'<p class="note"><b>Кадр %d.</b> %s</p>' % (shot, esc(txt)))
    A(u'<div class="slots">%s</div>'
      % u''.join(u'<div class="slot"><span>%s</span></div>' % p['id'] for p in ps))
    A(u'<p class="refs"><span>плюс:</span> карта Шохруха #C1 · эталон лица #1 — '
      u'в каждой панели, где он в кадре</p>')
    A(u'<details class="det"><summary>показать промпты</summary>')
    A(u'<div class="prs">%s</div>'
      % u''.join(u'<div class="pr"><div class="prid">%s</div><pre class="prompt">%s</pre></div>'
                 % (p['id'], esc(p['prompt'])) for p in ps))
    A(u'<div class="neg"><div class="negh">негативный промпт — на всю партию'
      u'<button class="cpyn" type="button">копировать</button></div>'
      u'<pre class="negp">%s</pre></div>' % esc(sh['neg']))
    A(u'</details>')
    A(u'<p class="instr" hidden>%s</p>' % esc(instr(len(ps))))
    A(u'</section>')

out = head + u'\n'.join(parts) + tail
io.open(os.path.join(BASE, 'storyboard.html'), 'w', encoding='utf-8').write(out)
print(u'партий: %d, панелей: %d, размер: %.0f КБ'
      % (len(sheets), total, len(out.encode('utf-8')) / 1024.0))
