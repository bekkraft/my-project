# -*- coding: utf-8 -*-
"""Собирает storyboard.html — рабочий стол раскадровки.

Данные — из RASKADROVKA/sheets.json, разметка и скрипт — из tools/page-app.html.
Запускать после build_sheets.py, из корня репозитория.
"""
import io, json, os, re

BASE = 'shahruhiya'
SHEETS = os.path.join(BASE, 'RASKADROVKA', 'sheets.json')
TPL = os.path.join(BASE, 'tools', 'page-app.html')

ACTS = {
    u'АКТ 1 — Ташкент и туннель':    ('#7E94AC', u'Акт 1 · Ташкент и туннель'),
    u'АКТ 2 — Степь и лагерь':       ('#C9954A', u'Акт 2 · Степь и лагерь'),
    u'Шатёр Темура':                 ('#A8552E', u'Шатёр · Амир Темур'),
    u'АКТ 3 — Гонка':                ('#D9682F', u'Акт 3 · Гонка'),
    u'АКТ 3 — Имя, перстень, финал': ('#C3A551', u'Финал · Имя, перстень, возвращение'),
}


def timecodes():
    out = {}
    for ln in io.open(os.path.join(BASE, 'SCENARIY.md'), encoding='utf-8'):
        m = re.match(r'^\|\s*(\d+)\s*\|\s*(\d+:\d+)\s*\|', ln)
        if m:
            out.setdefault(int(m.group(1)), m.group(2))
    return out


TC = timecodes()
sheets = json.load(io.open(SHEETS, encoding='utf-8'))

batches = []
for sh in sheets:
    ps = sh['panels']
    acc, label = ACTS[ps[0]['block']]
    tcs = [TC[p['shot']] for p in ps if p['shot'] in TC]
    tc = (tcs[0] + u' – ' + tcs[-1]) if len(tcs) > 1 else (tcs[0] if tcs else u'')
    refs = []
    for p in ps:
        for r in [x.strip() for x in (p.get('ref') or u'').split(';') if x.strip()]:
            if r not in refs:
                refs.append(r)
    k = len(ps)
    batches.append({
        'n': sh['n'], 'acc': acc, 'label': label, 'tc': tc,
        'neg': sh['neg'], 'refs': u'; '.join(refs),
        'instr': (u'Generate %d SEPARATE images, one for each numbered prompt below. '
                  u'Each image must be 16:9. Do NOT merge them into a grid, collage or '
                  u'contact sheet. Keep the visual style identical across all %d.' % (k, k)),
        'panels': [{'id': p['id'], 'shot': p['shot'], 'title': p['title'],
                    'prompt': p['prompt'], 'note': p.get('note', u''),
                    'label': label, 'key': p['id'].endswith('a')} for p in ps],
    })

total = sum(len(b['panels']) for b in batches)
six = sum(1 for b in batches if len(b['panels']) == 6)
keys = sum(1 for b in batches for p in b['panels'] if p['key'])

data = {
    'batches': batches,
    'lede': (u'%d панелей на %d %s — %d ровно по шесть. Панели одного кадра никогда '
             u'не разнесены по разным партиям: у них общая рамка, врозь они разъезжаются. '
             u'Токены развёрнуты, промпты готовы к вставке. %d панелей с точкой в углу — '
             u'стартовые кадры видео, из них собирается фильм.'
             % (total, len(batches),
                (u'партию' if len(batches) % 10 == 1 and len(batches) % 100 != 11 else
                 u'партии' if len(batches) % 10 in (2, 3, 4) and len(batches) // 10 % 10 != 1
                 else u'партий'),
                six, keys)),
}

tpl = io.open(TPL, encoding='utf-8').read()
payload = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
out = tpl.replace('/*__DATA__*/', payload)

io.open(os.path.join(BASE, 'storyboard.html'), 'w', encoding='utf-8').write(out)

# автономный файл: артефакт оборачивает страницу сам, скачанному нужна обёртка
SHELL = (u'<!doctype html>\n<html lang="ru"><head><meta charset="utf-8">\n'
         u'<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
         u'<style>:root{color-scheme:light dark}html,body{margin:0}'
         u'img{max-width:100%}[hidden]{display:none!important}</style>\n'
         u'%s\n</head><body>\n%s\n</body></html>\n')
head_end = out.index('</style>') + len('</style>')
standalone = SHELL.replace(u'%s', u'\x00', 1).replace(u'%s', u'\x01', 1)\
    .replace(u'\x00', out[:head_end]).replace(u'\x01', out[head_end:])
exp = os.path.join(BASE, 'export', 'SHAHRUHIYA-raskadrovka.html')
io.open(exp, 'w', encoding='utf-8').write(standalone)
print(u'партий: %d, панелей: %d, стартовых: %d, размер: %.0f КБ'
      % (len(batches), total, keys, len(out.encode('utf-8')) / 1024.0))
