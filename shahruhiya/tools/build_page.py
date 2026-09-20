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


# Компактная ДНК персонажей: на листе она объявляется один раз, а не в каждой панели.
DNA = [
    (u'SHOHRUH', u'SHOHRUH — a 30-year-old Uzbek man, oval face, tired dark brown eyes, '
                 u'thick low eyebrows, a thin white scar through the left eyebrow, three-day '
                 u'stubble, very dark hair tousled on one side, a white shirt damp on the chest '
                 u'with the second button missing, dark blue jeans, a grey bomber jacket off one '
                 u'shoulder, a steel watch on the left wrist.'),
    (u'AMIR TEMUR', u'AMIR TEMUR — a Central Asian ruler of about 60, broad strong-jawed '
                    u'weathered face, heavy brows, deep-set dark eyes, a short wedge beard '
                    u'heavily streaked with grey, a golden domed crown set with dark red gems '
                    u'and topped with a white feather plume, a white fur-trimmed robe with gold '
                    u'embroidery over blue and deep red brocade, a stiff right leg. The crown '
                    u'is on his head in every panel where he appears.'),
    (u'BOBUR', u'BOBUR — a 22-year-old warrior, broad face, lively narrow dark eyes, a sparse '
               u'moustache and no beard, black hair with a thin braid at the left temple, a '
               u'triangular leather amulet at the neck, a quilted ochre robe with a braided '
               u'sash, leather bracers, a curved sabre on the left hip.'),
    (u'THE COMMANDER', u'THE COMMANDER — a 45-year-old warrior, thickset, weather-beaten face, '
                       u'a scar through the right eyebrow and cheekbone, a greying beard, a dark '
                       u'green robe under a lamellar steel cuirass.'),
    (u'Timurid warriors', u'TIMURID WARRIORS — late-14th-century Central Asian and Turkic men, '
                          u'quilted ochre and dark green knee-length robes, lamellar plate '
                          u'armour, pointed steel helmets with mail aventails, curved sabres.'),
    (u'the grey saloon', u'THE CAR — a faded grey compact four-door saloon of late-2000s '
                         u'Chevrolet Aveo T250 proportions, rounded bonnet, large swept-back '
                         u'teardrop headlamps, tall narrow vertical tail lamps.'),
    (u'the silver ring', u'THE RING — massive tarnished blackened silver set with a large dark '
                         u'red carnelian, worn Arabic calligraphy around the stone.'),
]

# Генераторы рисуют кириллицу как набор закорючек — шапка листа идёт латиницей.
LAT = {
    u'АКТ 1 — Ташкент и туннель':      u'ACT 1 - TASHKENT AND THE TUNNEL',
    u'АКТ 2 — Степь и лагерь':         u'ACT 2 - THE STEPPE AND THE CAMP',
    u'Шатёр Темура':                   u'THE TENT OF AMIR TEMUR',
    u'АКТ 3 — Гонка':                  u'ACT 3 - THE RACE',
    u'АКТ 3 — Имя, перстень, финал':   u'ACT 3 - THE NAME, THE RING, THE RETURN',
}

STYLE = {
    u'АКТ 1 — Ташкент и туннель':
        u'desaturated cold steel-grey palette, flat overcast Tashkent morning, wet asphalt',
    u'АКТ 2 — Степь и лагерь':
        u'warm golden morning light, ochre and dusty brown against a huge pale blue sky',
    u'Шатёр Темура':
        u'low-key candle and oil-lamp light from below and the side, amber and deep red with '
        u'black shadows and one burning gold highlight',
    u'АКТ 3 — Гонка':
        u'late afternoon sun very low and backlit, long shadows, orange-gold against cold blue '
        u'shadows, dust hanging in the air',
    u'АКТ 3 — Имя, перстень, финал':
        u'golden hour, horizontal sunlight almost level with the ground, dust burning in the '
        u'air, bronze skin tones, red and gold',
}

# На листе номера ДОЛЖНЫ быть напечатаны, поэтому запреты на текст снимаются.
TEXT_BANS = ('no text overlay', 'no subtitles', 'no captions', 'no lettering')


def sheet_negative(neg):
    keep = [t.strip() for t in neg.split(',')
            if t.strip() and t.strip().lower() not in TEXT_BANS]
    return u', '.join(keep + [u'no speech bubbles', u'no comic book styling',
                              u'no handwriting', u'no misspelled labels'])


def sheet_prompt(b, panels):
    cols = 3
    rows = -(-len(panels) // cols)
    who = [line for key, line in DNA
           if any(key in p['short'] for p in panels)]
    beats = []
    for i, p in enumerate(panels, 1):
        beats.append(u'Panel %d, labelled %s, timecode %s — %s'
                     % (i, p['id'], p.get('tc') or u'--:--', p['short'].rstrip('.') + u'.'))
    return (
        u'A professional storyboard sheet for the short film "Shahrukhiya", a magical-realism '
        u'drama set between present-day Tashkent and the steppe of Amir Temur in the 14th '
        u'century. One single composite presentation page holding %d sequential cinematic '
        u'panels in a clean %d\u00d7%d grid, read left to right, top to bottom.\n\n'
        u'STYLE. Photoreal cinematic film stills, 35mm film grain, natural motivated lighting, '
        u'shallow depth of field, subtle halation. Every panel is a 16:9 frame from the same '
        u'film, graded the same way: %s. No illustration, no comic art — each panel looks like '
        u'a frame of photographed film pasted onto the board.\n\n'
        u'CHARACTERS. %s\n\n'
        u'SHEET LAYOUT. A dark charcoal production board. The panels sit in the grid with even '
        u'thin gutters between them and a white hairline border around each frame. Beneath '
        u'every panel runs a narrow caption strip in clean sans-serif type carrying that '
        u'panel\u2019s label and timecode exactly as written below, plus its short shot note. '
        u'A single header line across the top of the board reads "SHAHRUKHIYA \u2014 BATCH %d '
        u'\u2014 %s". Typography is small, quiet and legible; it never overlaps the images.\n\n'
        u'PANELS.\n%s\n\n'
        u'ART DIRECTION. Vary the shot sizes exactly as described — do not flatten everything to '
        u'medium shots. Faces stay identical from panel to panel. Keep the light direction and '
        u'colour consistent across the whole sheet. Composition inside each frame is centred on '
        u'what the note names, with real depth and atmosphere.\n\n'
        u'RENDER. Masterpiece quality, production-ready storyboard sheet, sharp legible '
        u'captions, 16:9 board.'
        % (len(panels), cols, rows, STYLE.get(b['block'], u'cinematic natural light'),
           u' '.join(who) if who else u'No named characters in this batch.',
           b['n'], LAT.get(b['block'], u'SHAHRUKHIYA'), u'\n'.join(beats))
    )


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
    for p in ps:
        p['tc'] = TC.get(p['shot'], u'')
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
    batches[-1]['sheetPrompt'] = sheet_prompt(
        {'n': sh['n'], 'label': label, 'block': ps[0]['block']}, ps)
    batches[-1]['sheetNeg'] = sheet_negative(sh['neg'])

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
