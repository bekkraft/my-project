# РАСКАДРОВКА — БЛОК 3: ШАТЁР АМИРА ТЕМУРА (кадры 54–64, 2:42–3:12)
# 21 панель

## ГЛАВНАЯ ТРУДНОСТЬ ЭТОЙ СЦЕНЫ

Здесь почти ничего не происходит физически. Тридцать секунд на одиннадцать
кадров, восемь из них — абсолютная статика. Вся сцена держится на ДВУХ
движениях за всё время:

1. **Темур поднимает глаза** (кадр 58)
2. **Уголок его рта дёргается в улыбку** (кадр 64)

Всё остальное — неподвижность. Поэтому панели здесь фазируют не действие,
а МИКРОМИМИКУ. Если разбить их как обычные подкадры движения, сцена
рассыплется.

## ТРИ ПРАВИЛА, БЕЗ КОТОРЫХ СЦЕНА НЕ РАБОТАЕТ

1. **Поза Темура ИДЕНТИЧНА во всех панелях.** Сидит на подушках, опирается
   на левую руку, правая неподвижно лежит на колене. Меняются только глаза
   и рот. Ни одна панель не должна показать его в другой позе.
2. **Камера на уровне глаз СИДЯЩЕГО Темура.** Не снизу — он не тиран.
   Не сверху — он не жертва. Прямо в глаза: зритель на месте Шохруха.
3. **Корона даёт ОДИН горящий блик** в темноте, при половине лица в тени.
   Власть читается раньше лица.

## ПОРЯДОК ГЕНЕРАЦИИ
Сначала **58c** — взгляд Темура в камеру. Это лицо всей сцены. Как получится —
подставлять её как image reference во ВСЕ остальные панели с Темуром, чтобы
поза и свет не поплыли.

---

# ТОКЕНЫ

### [SUFFIX]
```
cinematic film still, 35mm film grain, natural motivated lighting, shallow depth of field, subtle halation, 16:9
```

### [TEMUR]
```
a Central Asian ruler of about 60 with a broad strong-jawed weathered face, heavy dark eyebrows, dark deep-set eyes with a heavy gaze from beneath the brows, tanned skin, deep lines on the forehead and around the eyes, a short wedge beard dark and heavily streaked with grey, wearing a golden domed crown set with dark red gemstones and topped with a white feather plume, a white fur-trimmed robe with gold floral embroidery over a patterned blue and deep red brocade tunic, a massive tarnished silver ring with a dark red carnelian on his right ring finger, seated cross-legged on low cushions leaning on his left arm with his right arm resting motionless on his knee
```

### [SHOHRUH]
```
a 30-year-old Uzbek man, oval face with moderately defined cheekbones, dark brown almond-shaped eyes with tired shadows beneath them, thick straight dark eyebrows set low, a thin white scar through his left eyebrow, uneven three-day stubble, very dark almost black short hair tousled on one side, wearing a white shirt damp on the chest and collar with the top button undone and the second button missing, dark blue jeans, a dark grey bomber jacket hanging crookedly off one shoulder, dark brown leather boots, a steel watch on his left wrist
```

### [WARRIORS]
```
late-14th-century Timurid warriors, Central Asian and Turkic men with dark almond eyes and thin beards, quilted ochre and dark green knee-length robes belted with cloth sashes, lamellar plate armour, leather bracers, pointed steel helmets with mail aventails, curved sabres
```

### [TENT]
```
the interior of an enormous 14th century Timurid military command tent, layered Persian carpets covering the floor, low cushions, a brazier of glowing coals, oil lamps and candles as the only light sources, fabric walls, a high roof lost in shadow
```

### [LOWKEY]
```
low-key lighting from candles and oil lamps below and to the side, amber and deep red palette with black shadows and one burning gold highlight
```

## НЕГАТИВНЫЙ ПРОМПТ ДЛЯ ВСЕГО БЛОКА
```
no crusaders, no red crosses, no christian symbols, no european knights, no chainmail hauberks, no surcoats, no tabards, no straight swords, no european faces, no medieval european armour, no heraldry, no throne, no wooden chair, no tiled walls, no palace interior, no standing Temur, no modern objects, no electric light, no text overlay, no subtitles, no captions, no lettering, no watermark, no logo, no extra fingers, no distorted faces, no cartoon, no anime, no illustration
```

---

# КАДР 54. Вход в шатёр (2 панели)
Прикреплять: эталон шатра #14

**54a**
```
Cinematic film still, wide shot, backlit, [TENT], the entrance flap at the far end being drawn aside from outside, a hard wedge of white daylight cutting into the amber darkness across the carpets, no one yet standing in it, [LOWKEY], 35mm lens, [SUFFIX]
```

**54b**
```
Cinematic film still, wide shot, backlit, identical framing, [TENT], [SHOHRUH] standing inside the wedge of hard white daylight at the far end of the tent, reduced almost to a black silhouette by the backlight, his modern jacket and jeans unmistakable in outline against the daylight, amber darkness all around him, [LOWKEY], 35mm lens, [SUFFIX]
```

# КАДР 55. Интерьер: воины-стены (1 панель) — СТАТИКА
Прикреплять: эталон шатра #14

**55a**
```
Cinematic film still, wide shot, perfectly centred symmetrical composition, [TENT], two rows of [WARRIORS] standing motionless along both side walls like human walls, a brazier of glowing coals in the centre, low cushions beyond it, the high fabric roof lost in shadow above, the wedge of daylight from the entrance behind, [LOWKEY], 24mm lens, [SUFFIX]
```

# КАДР 56. Темур не поднимает глаз (1 панель)
Прикреплять: эталон Темура в шатре #4a + карта Темура #C4

**56a**
```
Cinematic film still, medium shot, camera exactly at the eye level of a seated man, [TEMUR], [TENT], his gaze cast down at his own hands, face angled slightly downward, half his face in deep shadow, a single burning highlight on the gold of the crown, [LOWKEY], 50mm lens, [SUFFIX]
```

# КАДР 57. Темур говорит, не глядя (2 панели)
Реплика: «Менга айтишди… юз етти от кучи бор эмиш»

**57a**
```
Cinematic film still, close-up, camera at the eye level of a seated man, [TEMUR], [TENT], mouth closed, eyes still cast down, absolutely still, candle light from below and the side, half the face in shadow, one gold highlight on the crown, [LOWKEY], 85mm lens, [SUFFIX]
```

**57b**
```
Cinematic film still, close-up, identical framing and identical pose, [TEMUR], [TENT], mouth now open mid-sentence speaking slowly, eyes STILL cast down and not lifted, nothing else in the face or body changed, candle light from below and the side, [LOWKEY], 85mm lens, [SUFFIX]
```

# КАДР 58. ТЕМУР ПОДНИМАЕТ ГЛАЗА (3 панели) ★ ГЛАВНЫЙ КАДР СЦЕНЫ
Генерировать ПЕРВЫМ. Три панели — одна голова, одно освещение, меняются
ТОЛЬКО веки и направление взгляда. Ничего больше.

**58a**
```
Cinematic film still, close-up, camera at the eye level of a seated man, [TEMUR], [TENT], eyes cast fully down, heavy lids lowered, face motionless, candle light from below and the side, half the face in shadow, one gold highlight on the crown, [LOWKEY], 85mm lens, [SUFFIX]
```

**58b**
```
Cinematic film still, close-up, identical framing and identical pose, [TEMUR], [TENT], heavy eyelids risen halfway, the eyes just beginning to come up from beneath the brows, the head itself not moved at all, candle light from below and the side, [LOWKEY], 85mm lens, [SUFFIX]
```

**58c**
```
Cinematic film still, close-up, identical framing and identical pose, [TEMUR], [TENT], eyes now fully lifted and fixed directly into the lens with an immovable weighing gaze from beneath heavy brows, a small candle flame reflected in each dark iris, the head still not moved, half the face in shadow, one gold highlight on the crown, [LOWKEY], 85mm lens, [SUFFIX]
```

# КАДР 59. Шохрух отвечает (2 панели)
Реплика: «Мен… Шоҳруҳ. Тошкентданман.»
Прикреплять: карта Шохруха #C1 + эталон лица #1

**59a**
```
Cinematic film still, medium shot over the shoulder of [TEMUR] seated in the foreground, [SHOHRUH] in the middle ground bowing awkwardly and off balance, one foot shifted to catch himself, lit by the wedge of daylight from the entrance behind him against the amber darkness, [LOWKEY], 50mm lens, [SUFFIX]
```

**59b**
```
Cinematic film still, medium shot over the shoulder of [TEMUR] seated in the foreground, identical framing, [SHOHRUH] now upright and speaking, throat working as he swallows, shoulders drawn in, lit by the wedge of daylight from behind, [LOWKEY], 50mm lens, [SUFFIX]
```

# КАДР 60. «Бундай шаҳар йўқ» (2 панели)

**60a**
```
Cinematic film still, close-up, identical framing and identical pose to the earlier Temur shots, [TEMUR], [TENT], eyes fixed forward, mouth open speaking a short flat sentence, no emphasis in the face, [LOWKEY], 85mm lens, [SUFFIX]
```

**60b**
```
Cinematic film still, close-up, identical framing and identical pose, [TEMUR], [TENT], mouth closed again, eyes still fixed forward, holding a long silence, absolutely nothing moving, [LOWKEY], 85mm lens, [SUFFIX]
```

# КАДР 61. ШОХРУХ ПОНИМАЕТ, ГДЕ ОН (3 панели) ★
Сабли его не сломали. Степь не сломала. Ломает фраза «такого города нет».
Прикреплять: карта Шохруха #C1 + expression sheet #C2

**61a**
```
Cinematic film still, close-up, eye level, [SHOHRUH] listening with a neutral attentive face, eyebrows slightly raised, still expecting an ordinary answer, warm candle light on one side of his face, deep shadow on the other, [LOWKEY], 85mm lens, [SUFFIX]
```

**61b**
```
Cinematic film still, close-up, identical framing, [SHOHRUH] with the understanding arriving, eyes widening fractionally, lips parting, the attentive expression falling away, warm candle light on one side of his face, [LOWKEY], 85mm lens, [SUFFIX]
```

**61c**
```
Cinematic film still, close-up, identical framing, [SHOHRUH] with the floor gone from under him, eyes unfocused and staring past the camera, face gone slack, all colour and light draining away from his side of the frame, [LOWKEY], 85mm lens, [SUFFIX]
```

# КАДР 62. Задача: чопар, пистирма, «жанг эртага» (1 панель)

**62a**
```
Cinematic film still, close-up, identical framing and identical pose, [TEMUR], [TENT], speaking with grim weight, eyes fixed forward, the shadows on his face deeper than before as if the lamps had burned lower, [LOWKEY], 85mm lens, [SUFFIX]
```

# КАДР 63. «Лекин…» · воины напрягаются (2 панели)

**63a**
```
Cinematic film still, medium shot with three layers of depth, [TENT], [SHOHRUH] in the middle ground with one hand half raised, mouth open having just interrupted, [TEMUR] seated in the near foreground out of focus, [WARRIORS] along the walls behind, everyone still, [LOWKEY], 35mm lens, [SUFFIX]
```

**63b**
```
Cinematic film still, medium shot with three layers of depth, identical framing, [TENT], [SHOHRUH] frozen mid-gesture, and behind him the [WARRIORS] along the walls all shifted a fraction toward him, hands moved to sabre grips, heads turned, the stillness broken only in the background, [LOWKEY], 35mm lens, [SUFFIX]
```

# КАДР 64. УЛЫБКА УГОЛКОМ РТА (2 панели) ★ единственная за фильм

**64a**
```
Cinematic film still, tight close-up, identical framing and identical pose, [TEMUR], [TENT], face completely still and unreadable like carved stone, mouth a flat line, eyes fixed forward, one gold highlight on the crown, [LOWKEY], 100mm lens, [SUFFIX]
```

**64b**
```
Cinematic film still, tight close-up, identical framing and identical pose, [TEMUR], [TENT], ONE CORNER of his mouth lifted a few millimetres into the faintest possible smile, like a crack opening in stone, the eyes warming very slightly, everything else in the face unchanged, one gold highlight on the crown, [LOWKEY], 100mm lens, [SUFFIX]
```

---

# ИТОГИ БЛОКА 3

- **21 панель** на 11 кадров
- **Оптических переходов нет** — вся сцена на жёстких склейках
- **Три панели решают сцену:** 58c (взгляд), 61c (осознание), 64b (улыбка)

## ПОЧЕМУ ПАНЕЛИ ЗДЕСЬ ТАК ПОХОЖИ ДРУГ НА ДРУГА

Это не ошибка и не лень. Сцена построена на том, что **ничего не меняется**.
Если в 57b, 60a, 62a и 64a Темур будет сидеть чуть иначе — власть, которая
держится на его неподвижности, исчезнет, и получится обычный разговор
двух людей. Поэтому в промптах везде стоит `identical framing and identical
pose`, и поэтому все панели с Темуром генерируются с 58c как референсом.

## ЧЕК-ЛИСТ ПРИЁМКИ
- [ ] Темур СИДИТ во всех 12 панелях с ним, ни одной стоящей
- [ ] Поза идентична: опора на левую руку, правая неподвижна на колене
- [ ] Корона на месте во всех панелях, перо не меняет форму
- [ ] Камера на уровне глаз СИДЯЩЕГО, не сверху и не снизу
- [ ] 58a → 58b → 58c: меняются ТОЛЬКО веки, голова не двигается
- [ ] 64a → 64b: меняется ТОЛЬКО один уголок рта
- [ ] Ни одного крестоносца, красного креста, трона, изразца
- [ ] Шохрух в той же одежде, что весь фильм
- [ ] Клин дневного света из входа виден в 54a, 54b, 55a, 59a, 59b
