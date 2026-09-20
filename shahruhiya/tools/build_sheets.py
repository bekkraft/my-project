# -*- coding: utf-8 -*-
"""Пересобирает раскадровки в листы ровно по 6 панелей.

Источник — STORYBOARD-01..05. Токены разворачиваются, каждый лист
самодостаточен: 6 промптов + негатив + блок для копирования в Flow.
Запускать из корня репозитория.
"""
import io, os, re, json

SRC = [
    ('STORYBOARD-01-ACT1.md',   u'АКТ 1 — Ташкент и туннель'),
    ('STORYBOARD-02-ACT2A.md',  u'АКТ 2 — Степь и лагерь'),
    ('STORYBOARD-03-TENT.md',   u'Шатёр Темура'),
    ('STORYBOARD-04-RACE.md',   u'АКТ 3 — Гонка'),
    ('STORYBOARD-05-FINALE.md', u'АКТ 3 — Имя, перстень, финал'),
]
BASE = 'shahruhiya'
OUT = os.path.join(BASE, 'RASKADROVKA')

NEG = (u'no rings on fingers, no wedding ring, no jewellery on hands, no text overlay, '
       u'no subtitles, no captions, no lettering, no watermark, no logo, no extra fingers, '
       u'no distorted faces, no cartoon, no anime, no illustration')

FENCE = re.compile(r'```\n(.*?)\n```', re.S)

# кадр → эталоны, которые надо приложить к панели.
# В исходных файлах строка «Эталон:» стояла у двух кадров из 124 — карта ниже
# закрывает все остальные. Три якоря на панель (карта героя + лицо + локация)
# требует мастер-промпт, раздел 1.5.
REFS = [
    ((1, 8),     u'#8 спальня'),
    ((9, 11),    u'ванная (отдельный эталон)'),
    ((12, 14),   u'#9 двор с тандыром, #2 Шохрух в рост, #6 Нексия'),
    ((15, 20),   u'#6 Нексия, #10 улицы Ташкента утром'),
    ((21, 21),   u'#11c въезд в туннель снаружи, #6 Нексия'),
    ((22, 23),   u'#11a туннель бетонный'),
    ((24, 24),   u'#11a туннель бетонный + #11 туннель каменный — оба, это морф'),
    ((25, 27),   u'#11 туннель каменный'),
    ((28, 32),   u'#12 степь, #6 Нексия'),
    ((33, 49),   u'#13 военный лагерь, #5 командир отряда, #6 Нексия'),
    ((50, 53),   u'#3 Бобур, #13 лагерь, #6 Нексия'),
    ((54, 64),   u'#14 шатёр, #4a Темур в шатре (корона!), #3 Бобур'),
    ((65, 67),   u'#13 лагерь, #6 Нексия, #3 Бобур'),
    ((68, 75),   u'#15 горная дорога и ущелье, #6 Нексия, #3 Бобур'),
    ((76, 83),   u'#15 ущелье, #5 командир отряда'),
    ((84, 87),   u'#15 ущелье, #5 командир отряда, #3 Бобур'),
    ((88, 101),  u'#4b Темур перед войском (корона!), #7 перстень, #5 командир, #3 Бобур'),
    ((102, 105), u'#12 степь, #6 Нексия, #7 перстень'),
    ((106, 108), u'#11 туннель каменный, #11a туннель бетонный'),
    ((109, 113), u'#16 Ташкент финал, #6 Нексия, #7 перстень'),
    ((114, 117), u'#16 Ташкент финал, #9 двор с тандыром'),
    ((118, 121), u'#17 сквер Амира Темура сверху, #16 Ташкент финал'),
    ((122, 124), u'#16 Ташкент финал, #17 сквер сверху'),
]


def refs_for(shot):
    for (a, b), r in REFS:
        if a <= shot <= b:
            return r
    return u''




def parse(path):
    """→ (токены, список панелей)."""
    text = io.open(path, encoding='utf-8').read()
    lines = text.split('\n')

    tokens, panels = {}, []
    shot_no, shot_title, ref = None, u'', u''
    i = 0
    while i < len(lines):
        ln = lines[i]

        m = re.match(r'^### \[([A-Z0-9\-]+)\]', ln)
        if m:
            blk = FENCE.search('\n'.join(lines[i:i + 14]))
            if blk:
                tokens[m.group(1)] = blk.group(1).strip()
            i += 1
            continue

        m = re.match(r'^#+\s*КАДР\s+(\d+)\.\s*(.*)$', ln)
        if m:
            shot_no = int(m.group(1))
            shot_title = re.sub(r'\s*\(\d+\s*панел.*?\)', '', m.group(2)).strip()
            ref = u''
            i += 1
            continue

        m = re.match(r'^Эталон[ы]?:\s*(.+)$', ln)
        if m and shot_no:
            ref = m.group(1).strip()
            i += 1
            continue

        m = re.match(r'^\*\*(S\d+[a-z])\*\*\s*$', ln)
        if m:
            blk = FENCE.search('\n'.join(lines[i:i + 12]))
            if blk:
                panels.append(dict(id=m.group(1), shot=shot_no, title=shot_title,
                                   ref=ref, prompt=blk.group(1).strip()))
            i += 1
            continue
        i += 1
    return tokens, panels


def expand(prompt, tokens):
    out = prompt
    for _ in range(4):
        def sub(m):
            return tokens.get(m.group(1), m.group(0))
        new = re.sub(r'\[([A-Z0-9\-]+)\]', sub, out)
        if new == out:
            break
        out = new
    left = sorted(set(re.findall(r'\[([A-Z0-9\-]+)\]', out)))
    return out, left


all_panels = []
for fn, block_name in SRC:
    tokens, panels = parse(os.path.join(BASE, fn))
    for p in panels:
        p['prompt'], p['unresolved'] = expand(p['prompt'], tokens)
        p['block'] = block_name
        p['src'] = fn
        all_panels.append(p)

bad = [(p['id'], p['unresolved']) for p in all_panels if p['unresolved']]
if bad:
    print('!! неразвёрнутые токены:', bad[:10])

if not os.path.isdir(OUT):
    os.makedirs(OUT)

SIZE = 6
LOOKAHEAD = 4


def pack(block_panels):
    """Группы ровно по 6, кадр не разрывается.

    Панели кадра держатся вместе всегда: у соседних панелей одного кадра
    общая рамка и масштаб, врозь они разъезжаются. Чтобы при этом попадать
    в 6, разрешён локальный обгон — кадр из ближайших десяти может встать
    раньше по очереди, если он ровно добивает лист до шести.
    """
    shots = []
    for p in block_panels:
        if shots and shots[-1][0] == p['shot']:
            shots[-1][1].append(p)
        else:
            shots.append([p['shot'], [p]])

    rest = list(shots)
    out = []
    cur = []
    while rest:
        room = SIZE - sum(len(x[1]) for x in cur)
        window = rest[:LOOKAHEAD]
        pick = None
        for c in window:                      # ровно добивает до шести
            if len(c[1]) == room:
                pick = c
                break
        if pick is None:                      # иначе — первый влезающий
            for c in window:
                if len(c[1]) <= room:
                    pick = c
                    break
        if pick is None:                      # кадр длиннее листа
            if cur:
                out.append(cur)
                cur = []
                continue
            big = rest.pop(0)[1]
            for i in range(0, len(big), SIZE):
                out.append([[big[i]['shot'], big[i:i + SIZE]]])
            continue
        rest.remove(pick)
        cur.append(pick)
        if sum(len(x[1]) for x in cur) == SIZE:
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)

    # огрызок в один-два кадра подклеиваем к предыдущему листу
    i = len(out) - 1
    while i > 0:
        a = sum(len(x[1]) for x in out[i - 1])
        b = sum(len(x[1]) for x in out[i])
        if b < 3 and a + b <= SIZE:
            out[i - 1] += out.pop(i)
        i -= 1

    sheets = []
    for grp in out:
        grp.sort(key=lambda x: x[0])
        sheets.append([p for _, panels in grp for p in panels])
    return sheets


sheets = pack(all_panels)   # окно в десять кадров само держит листы внутри блока

index = []
for n, sheet in enumerate(sheets, 1):
    ids = [p['id'] for p in sheet]
    shots = sorted(set(p['shot'] for p in sheet))
    blocks = []
    for p in sheet:
        if p['block'] not in blocks:
            blocks.append(p['block'])
    refs = []
    for p in sheet:
        src = p['ref'] or refs_for(p['shot'])
        for r in [x.strip() for x in src.split(',') if x.strip()]:
            if r not in refs:
                refs.append(r)

    # панели кадра, оставшиеся за пределами листа
    carry = []
    for p in sheet:
        sibs = [q['id'] for q in all_panels if q['shot'] == p['shot'] and q['src'] == p['src']]
        outside = [s for s in sibs if s not in ids]
        if outside:
            carry.append((p['shot'], p['id'], outside))

    L = []
    A = L.append
    A(u'# РАСКАДРОВКА %02d — %d панел%s' % (n, len(sheet),
      u'ь' if len(sheet) == 1 else (u'и' if len(sheet) < 5 else u'ей')))
    A(u'')
    A(u'**Панели:** `%s`' % u'`, `'.join(ids))
    A(u'**Кадры:** %s · **Блок:** %s' % (u', '.join(str(s) for s in shots), u' / '.join(blocks)))
    A(u'**Эталоны прикрепить:** %s' % (u'; '.join(refs) if refs else u'—'))
    if any(u'Шохрух' in p['prompt'] or u'30-year-old Uzbek man' in p['prompt'] for p in sheet):
        A(u'**Плюс всегда:** карта персонажа #C1 + эталон лица #1 — в каждой панели с Шохрухом.')
    A(u'')
    if carry:
        A(u'> **Внимание — кадр разрезан между листами.**')
        for shot, pid, outside in carry:
            A(u'> Кадр %d: здесь `%s`, остальные панели `%s` — в соседнем листе.'
              % (shot, pid, u'`, `'.join(outside)))
        A(u'> Прикрепи уже сгенерированную соседнюю панель как референс, '
          u'иначе рамка и масштаб уедут.')
        A(u'')
    A(u'---')
    A(u'')
    A(u'## ПАНЕЛИ')
    A(u'')
    for k, p in enumerate(sheet, 1):
        A(u'### %d) %s — кадр %d. %s' % (k, p['id'], p['shot'], p['title']))
        A(u'```')
        A(p['prompt'])
        A(u'```')
        A(u'')
    A(u'### НЕГАТИВ (на все шесть)')
    A(u'```')
    A(NEG)
    A(u'```')
    A(u'')
    A(u'---')
    A(u'')
    A(u'## БЛОК ДЛЯ FLOW — скопировать целиком')
    A(u'')
    A(u'```text')
    A(u'Generate 6 SEPARATE images, one for each numbered prompt below. '
      u'Each image must be 16:9. Do NOT merge them into a grid, collage or contact sheet. '
      u'Keep the visual style identical across all six.')
    A(u'')
    for k, p in enumerate(sheet, 1):
        A(u'%d) %s' % (k, p['id']))
        A(p['prompt'])
        A(u'')
    A(u'NEGATIVE PROMPT (apply to all six):')
    A(NEG)
    A(u'```')
    A(u'')
    A(u'---')
    A(u'')
    A(u'## ПРОВЕРКА ПЕРЕД СЛЕДУЮЩИМ ЛИСТОМ')
    A(u'')
    A(u'- [ ] Пришло ровно 6 картинок, не коллаж')
    A(u'- [ ] Все 16:9')
    A(u'- [ ] Лицо Шохруха то же, что в принятых панелях')
    A(u'- [ ] Нет перстня на пальце (до кадра 105)')
    A(u'- [ ] Нет текста и подписей в кадре')
    A(u'- [ ] Файлы сохранены как %s' % u', '.join(u'`%s.png`' % i for i in ids))
    A(u'')
    io.open(os.path.join(OUT, 'RASKADROVKA-%02d.md' % n), 'w', encoding='utf-8').write(u'\n'.join(L))
    index.append(dict(n=n, ids=ids, shots=shots, block=blocks[0], split=bool(carry)))

# индекс
import collections as _c
sz = _c.Counter(len(x) for x in sheets)
L = [u'# РАСКАДРОВКИ — ИНДЕКС',
     u'',
     u'**%d панелей · %d %s.** %s' %
     (len(all_panels), len(sheets),
      (u'лист' if len(sheets) % 10 == 1 and len(sheets) % 100 != 11 else
       u'листа' if len(sheets) % 10 in (2, 3, 4) and len(sheets) // 10 % 10 != 1 else u'листов'),
      u', '.join(u'%d по %d' % (sz[k], k) for k in sorted(sz, reverse=True))),
     u'',
     u'Один лист = одна отправка в Flow. Блок для копирования — внизу каждого файла.',
     u'Панели одного кадра никогда не разнесены по разным листам: у них общая',
     u'рамка и масштаб, врозь они разъезжаются. Ради этого кадры внутри листа',
     u'иногда идут не подряд — на результат это не влияет, каждая панель',
     u'сохраняется под своим ID и собирается по `MANIFEST.md`.',
     u'',
     u'| Лист | Панели | Кадры | Блок |',
     u'|---|---|---|---|']
for it in index:
    L.append(u'| [%02d](RASKADROVKA-%02d.md) | `%s` | %s | %s |' %
             (it['n'], it['n'], u'` `'.join(it['ids']),
              u', '.join(str(x) for x in it['shots']), it['block']))
L.append(u'')
io.open(os.path.join(OUT, 'INDEX.md'), 'w', encoding='utf-8').write(u'\n'.join(L))

io.open(os.path.join(OUT, 'sheets.json'), 'w', encoding='utf-8').write(
    json.dumps([{'n': n, 'panels': [{'id': p['id'], 'shot': p['shot'], 'title': p['title'],
                                     'prompt': p['prompt'], 'block': p['block'],
                                     'ref': p['ref']} for p in s]}
                for n, s in enumerate(sheets, 1)], ensure_ascii=False, indent=1))

print(u'панелей: %d, листов: %d, последний: %d' % (len(all_panels), len(sheets), len(sheets[-1])))
print(u'разрезанных кадров на границах листов: %d' % sum(1 for i in index if i['split']))
