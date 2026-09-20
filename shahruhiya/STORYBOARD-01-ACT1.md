# РАСКАДРОВКА — БЛОК 1: АКТ 1 (кадры 1–27, 0:00–1:25)
# 57 панелей

## КАК ЭТИМ ПОЛЬЗОВАТЬСЯ

Промпты написаны с ТОКЕНАМИ в квадратных скобках. Перед генерацией сделай
автозамену — токен разворачивается в один и тот же текст во ВСЕХ панелях.
Это и есть механизм консистентности: описание героя должно быть ДОСЛОВНО
одинаковым везде, иначе лицо поплывёт.

### [SUFFIX]
```
cinematic film still, 35mm film grain, natural motivated lighting, shallow depth of field, subtle halation, 16:9
```

### [SHOHRUH]
```
a 30-year-old Uzbek man, oval face with moderately defined cheekbones, dark brown almond-shaped eyes with tired shadows beneath them, thick straight dark eyebrows set low, a thin white scar through his left eyebrow, uneven three-day stubble, very dark almost black short hair tousled on one side, wearing a white shirt damp on the chest and collar with the top button undone and the second button missing, dark blue jeans, a dark grey bomber jacket hanging crookedly off one shoulder, dark brown leather boots, a steel watch on his left wrist
```

### [SHOHRUH-DRY] — кадры 1–9b, до ванной
Рубашка становится мокрой только в S9c, когда он плещет воду в лицо.
До этого она СУХАЯ. В кадрах 1–8 использовать этот токен, дальше — обычный.
```
a 30-year-old Uzbek man, oval face with moderately defined cheekbones, dark brown almond-shaped eyes with tired shadows beneath them, thick straight dark eyebrows set low, a thin white scar through his left eyebrow, uneven three-day stubble, very dark almost black short hair tousled on one side, wearing a DRY white cotton shirt with the top button undone and the second button missing, dark blue jeans, a dark grey bomber jacket, dark brown leather boots, a steel watch on his left wrist
```

### [COLD]
```
desaturated cold steel-grey palette
```

### [CAR] — снаружи
НИКОГДА не писать «Nexia R3» или «Daewoo Nexia»: генератор не знает эту
региональную модель и подставляет обобщённый старый седан. Работает только
ОПИСАНИЕ КУЗОВА — базу Chevrolet Aveo T250 модель знает хорошо.
```
a grey compact four-door saloon of the late-S2000s Chevrolet Aveo T250 body style, rounded bonnet, large swept-back teardrop headlamps wrapping up into the front wings, a small two-part front grille with a thin chrome bar, tall narrow vertical tail lamps at the rear corners, fifteen-inch five-spoke alloy wheels, faded grey paint
```

### [CAR-INT] — салон
```
the interior of a small grey saloon, a dark grey moulded dashboard with two round instrument dials and a small digital display between them, a worn three-spoke steering wheel, a thin film of dust on the plastic
```

## ПРАВИЛА БЛОКА

1. **Движение камеры НЕ входит в промпты.** Панель — застывший момент.
   Push-in, handheld, crash zoom уйдут в Фазу 6 (видео).
2. **Прикреплять к каждой панели:** карта Шохруха (#C1) + эталон #1 (лицо) +
   эталон локации. Три якоря.
3. **Акт 1 весь холодный и десатурированный** — кроме туннеля (янтарь) и
   кадра 16 (фары — единственное тёплое пятно акта).
4. **Негативный промпт для всего блока:**
   `no rings on fingers, no wedding ring, no jewellery on hands, no text overlay, no subtitles, no captions, no lettering, no watermark, no logo, no extra fingers, no distorted faces, no cartoon, no anime, no illustration`

   Панель S14b в первой генерации вышла с подписью «Bismillah» прямо в кадре —
   отсюда `no subtitles, no captions, no lettering`.

---

# КАДР 1. Будильник, первый свайп (2 панели)
Эталон: спальня (#8)
Первая генерация дала два РАЗНЫХ телефона и две разные руки — склейка бы
развалилась. Аппарат и рука теперь описаны дословно в обеих панелях.
Сгенерировать S1a, принять, и подставить её как image reference в S1b.

**S1a**
```
Cinematic film still, extreme close-up, top-down directly above, a modern black glass-backed smartphone with a narrow notch and rounded corners in a plain matte black case, lying face up at a slight angle on a crumpled white pillow, the screen showing only the large numerals 7:47 and a single glowing alarm indicator with NO words and no interface labels of any kind, the smooth unlined hand of a man of thirty entering frame from the right with the index finger extended toward the screen, screen glow the only light source, cold blue light on the fingers, [COLD], 50mm macro lens, [SUFFIX]
```

**S1b**
```
Cinematic film still, extreme close-up, top-down directly above, IDENTICAL framing, scale and camera position to the previous panel, the very same modern black glass-backed smartphone with a narrow notch and rounded corners in the same plain matte black case, lying in exactly the same place and at exactly the same angle on the same crumpled white pillow, the screen now dark and blank, the same smooth unlined hand of a man of thirty completing a swipe across the glass and lifting away, only weak grey window light remaining on the pillow, [COLD], 50mm macro lens, [SUFFIX]
```

# КАДР 2. Лицо в подушке (1 панель)

**S2a**
```
Cinematic film still, close-up at pillow level, [SHOHRUH-DRY] asleep face down into a white pillow, only the jacket absent and the shirt visible, eyes shut, mouth slightly open, hair flattened on one side, one arm thrown over the pillow, soft flat grey overcast window light from the left with almost no shadows, [COLD], 35mm lens, [SUFFIX]
```

# КАДР 3. Второй свайп (1 панель, повтор композиции S1a)

**S3a**
```
Cinematic film still, extreme close-up, top-down directly above, the same smartphone screen on the same crumpled white pillow showing the alarm active again, the same male index finger pressed flat against the glass mid-swipe, identical framing to the earlier swipe, screen glow the only light, [COLD], 50mm macro lens, [SUFFIX]
```

# КАДР 4. Глаза открываются (3 панели)
Три панели — ОДНА макро-рамка, меняются только веки. В первой генерации S4c
отъехала на общий план с курткой и комнатой, и движение не прочиталось.
Сгенерировать S4a, принять, и подставить её как image reference в S4b и S4c.

**S4a**
```
Cinematic film still, extreme close-up of the closed eyes of [SHOHRUH-DRY], eyelids shut, dark lashes, tired shadows beneath, the thin white scar through the left eyebrow clearly visible, soft cold grey window light from the left, [COLD], 85mm lens, [SUFFIX]
```

**S4b**
```
Cinematic film still, extreme close-up of the eyes of [SHOHRUH-DRY], eyelids cracked half open and unfocused, pupils still adjusting, the thin white scar through the left eyebrow visible, soft cold grey window light from the left, [COLD], 85mm lens, [SUFFIX]
```

**S4c**
```
Cinematic film still, extreme close-up of the eyes of [SHOHRUH-DRY], IDENTICAL framing, scale and camera distance to the two previous panels, the crop holding only the brows, the eyes and the bridge of the nose with no shoulders, no clothing and no room behind, a plain out-of-focus pale grey wall filling the background, both eyes fully open and fixed straight ahead, a small window reflection caught in the dark brown iris, the thin white scar through the left eyebrow visible, soft cold grey window light from the left, [COLD], 85mm lens, [SUFFIX]
```

# КАДР 5. Потолок (1 панель)

**S5a**
```
Cinematic film still, medium wide shot from a low point of view looking straight up at a plain white ceiling of a small ordinary apartment bedroom, a simple round ceiling light fixture slightly off centre, the top edge of a curtained window at the frame edge, completely flat even overcast light, no shadows, [COLD], 24mm lens, [SUFFIX]
```

# КАДР 6. Мозг складывает цифры (2 панели)

**S6a**
```
Cinematic film still, close-up, eye level, [SHOHRUH-DRY] lying on his back on an unmade bed, eyes open and blank, face still calm, lips parted, soft flat grey window light from the left, [COLD], 35mm lens, [SUFFIX]
```

**S6b**
```
Cinematic film still, close-up, eye level, [SHOHRUH-DRY] lying on his back on an unmade bed, eyes suddenly wide, eyebrows raised high, jaw tensed in a flash of panic, head beginning to lift off the pillow, soft flat grey window light from the left, [COLD], 35mm lens, [SUFFIX]
```

# КАДР 7. Рывок с кровати, удар бедром (4 панели)
Активное действие — детальная фазировка.

**S7a**
```
Cinematic film still, medium shot, low eye level, [SHOHRUH-DRY] lying on an unmade bed in a small bedroom, torso beginning to lift, one hand pressed into the mattress, sheets tangled around his legs, soft grey window light from the left, [COLD], 24mm lens, [SUFFIX]
```

**S7b**
```
Cinematic film still, medium shot, low eye level, [SHOHRUH-DRY] in a small bedroom, torso fully upright and twisted toward the edge of the bed, sheets thrown aside, one bare foot already reaching the floor, soft grey window light from the left, [COLD], 24mm lens, [SUFFIX]
```

**S7c**
```
Cinematic film still, medium shot, low eye level, [SHOHRUH-DRY] in a small bedroom mid-lunge off the bed, both feet on the floor, body pitched forward off balance, arms swinging, slight motion blur on the hands, soft grey window light from the left, [COLD], 24mm lens, [SUFFIX]
```

**S7d**
```
Cinematic film still, medium shot, low eye level, [SHOHRUH-DRY] in a small bedroom jolting to a halt, his right hip struck against the sharp wooden corner of the bed frame, body folded slightly sideways, face contorted, soft grey window light from the left, [COLD], 24mm lens, [SUFFIX]
```

# КАДР 8. Угол и гримаса (2 панели)

**S8a**
```
Cinematic film still, insert close-up, the sharp bare wooden corner of a bed frame in a small bedroom with a man's hip pressed against it and beginning to pull away, worn varnish on the wood, soft grey window light, [COLD], 50mm lens, [SUFFIX]
```

**S8b**
```
Cinematic film still, close-up, eye level, [SHOHRUH-DRY] with his face screwed up in pain, eyes squeezed shut, teeth bared, one hand clamped on his right hip, standing beside an unmade bed, soft grey window light from the left, [COLD], 50mm lens, [SUFFIX]
```

# КАДР 9. Вода в лицо (3 панели)
Эталон локации: ванная — генерируется отдельно, палитра бирюзового кафеля

**S9a**
```
Cinematic film still, medium close-up at sink level, [SHOHRUH-DRY] leaning over a small bathroom sink, both hands cupped under a running tap and filling with water, head still up, hard cold lamp light from directly above carving shadows under his eyes, white and turquoise tile, [COLD], 35mm lens, [SUFFIX]
```

**S9b**
```
Cinematic film still, medium close-up at sink level, [SHOHRUH-DRY] driving both cupped hands of water into his own face, water bursting outward in droplets, eyes shut tight, hard cold lamp light from directly above, white and turquoise tile, [COLD], 35mm lens, [SUFFIX]
```

**S9c**
```
Cinematic film still, medium close-up at sink level, [SHOHRUH] lifting his dripping face, water running down his cheeks and jaw and soaking the collar and chest of his white shirt, eyes open and stinging, hard cold lamp light from directly above, white and turquoise tile, [COLD], 35mm lens, [SUFFIX]
```

# КАДР 10. Зеркало в брызгах (1 панель) — СОЗНАТЕЛЬНАЯ СТАТИКА

**S10a**
```
Cinematic film still, close-up of a bathroom mirror covered in scattered water droplets, the reflected face of [SHOHRUH] broken and fragmented by the drops, only one eye and part of the scarred left eyebrow clearly readable through the water, hard cold lamp light from above, white and turquoise tile behind, [COLD], 50mm lens, [SUFFIX]
```

# КАДР 11. Пуговица (3 панели)

**S11a**
```
Cinematic film still, extreme close-up, wet male fingers pinching a small white shirt button against damp white cotton fabric, the buttonhole just below, water beaded on the cloth, hard cold lamp light from above, [COLD], 50mm macro lens, [SUFFIX]
```

**S11b**
```
Cinematic film still, extreme close-up, wet male fingers slipping off a small white shirt button, the button twisting free, fingertips sliding across damp white cotton, hard cold lamp light from above, [COLD], 50mm macro lens, [SUFFIX]
```

**S11c**
```
Cinematic film still, extreme close-up, a male hand dropping away from an unbuttoned damp white shirt front, the collar hanging open, a bare thread where the second button is missing, hard cold lamp light from above, [COLD], 50mm macro lens, [SUFFIX]
```

# КАДР 12. Двор (2 панели) — СОЗНАТЕЛЬНАЯ СТАТИКА
Прикреплять: эталон двора #9

**S12a**
```
Cinematic film still, wide shot, eye level, the courtyard of a Soviet-era five-storey brick apartment block in Tashkent early morning, wet asphalt after night rain with puddles reflecting the sky, an elderly Uzbek man in a tubeteika cap and striped robe sweeping slowly with a long broom in the middle distance, a tandoor bakery in an open garage to the right with live fire inside and smoke drifting under the awning, laundry lines strung between trees, [CAR] parked by an entrance, soft overcast morning light, grey asphalt and green foliage with warm ochre smoke, 35mm lens, [SUFFIX]
```

**S12b**
```
Cinematic film still, wide shot, eye level, the same Tashkent courtyard with the old man still sweeping unchanged in the middle distance and the same parked car untouched, [SHOHRUH] crossing the very foreground close to the lens and heavily out of focus, only a blurred dark shape in motion, the sharp world behind him unchanged, soft overcast morning light, grey asphalt and green foliage with warm ochre smoke, 35mm lens, [SUFFIX]
```

# КАДР 13. Ключи в лужу (3 панели)
Прикреплять: эталон двора #9

**S13a**
```
Cinematic film still, insert shot, top-down, a bunch of car keys falling through the air a hand's width above a puddle on wet courtyard asphalt, the sky and green tree branches mirrored in the still water below, soft overcast morning light, [COLD], 50mm lens, [SUFFIX]
```

**S13b**
```
Cinematic film still, insert shot, top-down, a bunch of car keys striking the same puddle on wet courtyard asphalt, a crown of water bursting upward, the mirrored sky and green branches shattered into ripples, soft overcast morning light, [COLD], 50mm lens, [SUFFIX]
```

**S13c**
```
Cinematic film still, insert shot, top-down, a male hand plunging into the same puddle on wet courtyard asphalt and closing around the bunch of car keys, water running off the knuckles, the reflection still broken, soft overcast morning light, [COLD], 50mm lens, [SUFFIX]
```

# КАДР 14. Ключ и «Бисмиллоҳ» (2 панели)
Прикреплять: карта Шохруха #C1 + эталон лица #1

**S14a**
```
Cinematic film still, medium close-up from the passenger side, profile, [SHOHRUH] sitting in the driver's seat, [CAR-INT], one hand pushing the key into the ignition, eyes down on his hand, the grey courtyard visible through the windscreen, flat grey daylight through glass, [COLD], 35mm lens, [SUFFIX]
```

**S14b**
```
Cinematic film still, medium close-up from the passenger side, profile, identical framing, [SHOHRUH] in the driver's seat, [CAR-INT], lips parted mid-word speaking quietly to no one, gaze already forward through the windscreen, hand still on the key, flat grey daylight through glass, [COLD], 35mm lens, [SUFFIX]
```

# КАДР 15. Приборка и лампа бензина (2 панели) — ПОСЕВ
СНАЧАЛА сгенерировать S15b, довести до нужного вида, ПОТОМ подставлять её
как image reference в S15a, S19a и позже в 112. Иначе получатся четыре разные
приборки и рифма через весь фильм не прочитается.

**S15a**
```
Cinematic film still, insert close-up of a car instrument cluster, [CAR-INT], two round dials framed by the top of the steering wheel, needles resting at zero, every warning lamp dark, the display blank, a fine layer of dust on the plastic, flat grey daylight through the windscreen, [COLD], 50mm lens, [SUFFIX]
```

**S15b**
```
Cinematic film still, insert close-up of the same car instrument cluster in identical framing and scale, [CAR-INT], the dials now lit with cool green backlighting, both needles swung up, and a single ORANGE LOW-FUEL WARNING LAMP burning bright among them, the only warm colour in the frame, flat grey daylight through the windscreen, [COLD], 50mm lens, [SUFFIX]
```

# КАДР 16. Фары на луже (2 панели)
Прикреплять: ПРИНЯТЫЙ ЭТАЛОН МАШИНЫ #6 — обязательно, иначе кузов уедет

**S16a**
```
Cinematic film still, wide shot, very low angle near the ground, a large still puddle on wet courtyard asphalt directly in front of [CAR] parked facing the camera, the headlights dark, the water holding only a dull grey sky, overcast morning, [COLD], 24mm lens, [SUFFIX]
```

**S16b**
```
Cinematic film still, wide shot, very low angle near the ground, identical framing, the headlights of the same [CAR] now lit and falling across the puddle, the water holding a warm inverted reflection of the apartment block and trees, a small city upside down inside the water, warm light spilling across an otherwise cold grey courtyard, 24mm lens, [SUFFIX]
```

# КАДР 17. Пробка (1 панель)
Прикреплять: эталон улиц #10

**S17a**
```
Cinematic film still, medium shot from the rear seat over the driver's shoulder, [CAR-INT], looking through the windscreen at three lanes of Tashkent traffic packed bumper to bumper, mostly white and grey Uzbek-market sedans, wipers mid-stroke, rain beads on the glass, red brake lights, trolleybus wires overhead, billboards and high-rises beyond, overcast daylight, [COLD] with red brake lights as the only accents, 35mm lens, [SUFFIX]
```

# КАДР 18. Телефон за рулём (3 панели)
Прикреплять: карта Шохруха #C1 + эталон лица #1

**S18a**
```
Cinematic film still, close-up, eye level, [SHOHRUH] in the driver's seat holding a smartphone low near the wheel, eyes cast down at the screen, the screen glow lighting his face from below, blurred traffic beyond the windscreen, [COLD], 50mm lens, [SUFFIX]
```

**S18b**
```
Cinematic film still, close-up, eye level, identical framing, [SHOHRUH] in the driver's seat with his chin lifted and eyes snapped forward onto the road, the phone still held low in his hand, screen glow gone from his face, blurred traffic beyond the windscreen, [COLD], 50mm lens, [SUFFIX]
```

**S18c**
```
Cinematic film still, close-up, eye level, identical framing, [SHOHRUH] in the driver's seat with his eyes cast down at the phone screen again, the same downward glow on his face, blurred traffic beyond the windscreen, [COLD], 50mm lens, [SUFFIX]
```

# КАДР 19. 8:02 (1 панель)
Прикреплять: утверждённую панель S15b как image reference

**S19a**
```
Cinematic film still, insert close-up of the same car instrument cluster in identical framing and scale, [CAR-INT], the dials lit with the same cool green backlighting, the ORANGE LOW-FUEL WARNING LAMP still burning exactly as before, the small digital display reading 8:02, dust on the plastic, flat grey daylight, [COLD], 50mm lens, [SUFFIX]
```

# КАДР 20. Заправка мимо (2 панели) — ВЫСТРЕЛ ПОСЕВА

**S20a**
```
Cinematic film still, medium shot from inside a car looking out through the side window, a petrol station with its canopy and pumps entering frame at the near edge of the glass, rain beads on the window, wet road, overcast daylight, [COLD], 35mm lens, [SUFFIX]
```

**S20b**
```
Cinematic film still, medium shot from inside a car looking out through the side window, identical framing, the same petrol station now sliding off the far edge of the frame and almost gone, only the end of its canopy left, rain beads on the glass, overcast daylight, [COLD], 35mm lens, [SUFFIX]
```

# КАДР 21. Поворот к туннелю (2 панели)
Прикреплять: эталон въезда в туннель #S11b

**S21a**
```
Cinematic film still, medium shot from behind the driver, [CAR-INT], both male hands turning the worn three-spoke steering wheel hard to the right, wet road swinging across the windscreen, overcast daylight, [COLD], 24mm lens, [SUFFIX]
```

**S21b**
```
Cinematic film still, insert shot through a rain-beaded windscreen, a road sign and the concrete mouth of a city underpass ahead with orange light glowing inside it, wet asphalt, overcast daylight above, [COLD] outside against warm amber inside the tunnel, 24mm lens, [SUFFIX]
```

# КАДР 22. Лампы бегут по лицу (2 панели)
Прикреплять: карта Шохруха #C1 + эталон лица #1

**S22a**
```
Cinematic film still, medium close-up, profile from the passenger side, [SHOHRUH] driving, his face in shadow between tunnel lamps, only a faint amber edge along his cheekbone, dark concrete beyond the side window, amber and black palette, 35mm lens, [SUFFIX]
```

**S22b**
```
Cinematic film still, medium close-up, profile from the passenger side, identical framing, [SHOHRUH] driving with a hard band of orange sodium light laid across his eyes and cheekbone, the rest of the frame black, dark concrete beyond the side window, amber and black palette, 35mm lens, [SUFFIX]
```

# КАДР 23. Лампы гаснут (3 панели)
Прикреплять: эталон туннеля изнутри #11. Три панели — ОДНА И ТА ЖЕ геометрия,
меняются только лампы. Сгенерировать S23a, потом её как reference в S23b и S23c.

**S23a**
```
Cinematic film still, wide shot from the driver's point of view, perfectly centred symmetrical composition looking down the interior of a road tunnel, a long receding row of orange sodium ceiling lamps all lit, lane markings running away from the camera, bare concrete walls, no other cars, amber orange palette, 24mm lens, [SUFFIX]
```

**S23b**
```
Cinematic film still, wide shot from the driver's point of view, the same centred symmetrical tunnel interior in identical framing, roughly half the ceiling lamps now dark and breaking the rhythm of the row, the far end swallowed in blackness, lane markings running away, amber orange fading into coal black, 24mm lens, [SUFFIX]
```

**S23c**
```
Cinematic film still, wide shot from the driver's point of view, the same centred symmetrical tunnel interior in identical framing with only two or three lamps still burning close to the camera, the tunnel stretching impossibly far into total darkness with no end visible, headlights raking the near walls, amber orange against coal black, 24mm lens, [SUFFIX]
```

# КАДР 24. БЕТОН → КАМЕНЬ (3 панели) — ОПТИЧЕСКИЙ ПЕРЕХОД, МОРФ БЕЗ СКЛЕЙКИ

**S24a**
```
Cinematic film still, extreme close-up of a bare poured-concrete tunnel wall, form-work seams and grey aggregate texture, raking car headlight skimming across the surface from the left, deep black beyond, 50mm lens, [SUFFIX]
```

**S24b**
```
Cinematic film still, extreme close-up of a tunnel wall caught halfway between two materials, smooth poured concrete on the left of frame dissolving into rough ancient hewn stone on the right with deep veins like old animal hide, one continuous unbroken surface, raking headlight from the left, deep black beyond, 50mm lens, [SUFFIX]
```

**S24c**
```
Cinematic film still, extreme close-up of a rough ancient hewn stone wall with deep veins and pitted grain like the hide of an old animal, all trace of concrete gone, raking headlight skimming from the left, deep black beyond, 50mm lens, [SUFFIX]
```

# КАДР 25. Руки и педаль (2 панели)

**S25a**
```
Cinematic film still, close-up, [SHOHRUH] gripping a worn steering wheel with both hands, knuckles white with strain, tendons raised on the backs of his hands, almost total darkness with only a faint dashboard glow, near-black palette, 50mm lens, [SUFFIX]
```

**S25b**
```
Cinematic film still, extreme close-up in the footwell of a car, a man's boot pressing a brake pedal all the way flat to the floor with no resistance left, rubber pad crushed against the metal, almost total darkness with a faint edge of light, near-black palette, 50mm lens, [SUFFIX]
```

# КАДР 26. Белый свет (3 панели)

**S26a**
```
Cinematic film still, wide shot from the driver's point of view down the frontal centre of a dark ancient stone tunnel, a small hard point of pure white light far ahead in the blackness, stone walls barely readable at the edges, black palette with one white point, 24mm lens, [SUFFIX]
```

**S26b**
```
Cinematic film still, wide shot from the driver's point of view, the pure white light now swollen to fill the lower half of the windscreen, the stone walls burning out at their edges, all colour draining, white and black only, 24mm lens, [SUFFIX]
```

**S26c**
```
Cinematic film still, wide shot from the driver's point of view, blinding pure white light filling the entire windscreen and spilling past its frame, only a faint ghost of the dashboard silhouette remaining at the bottom edge, everything else burned out, 24mm lens, [SUFFIX]
```

# КАДР 27. Тишина (1 панель)

**S27a**
```
Cinematic film still, a completely blank pure white frame with the faintest possible warm grain, no subject, no horizon, no object, total emptiness, [SUFFIX]
```

---

# ИТОГИ БЛОКА 1

- **57 панелей** на 27 кадров
- **Одна панель-TRANSITION по существу:** S24b (морф бетона в камень).
  Остальные переходы — жёсткие склейки, панели не нужны
- **Три сознательные статики:** S10a (зеркало), S12a–S12b (двор), S23a–S23c (туннель)
- **Тёплые пятна в холодном акте, их всего два:** S12a (огонь тандыра) и S16b (фары на луже)
- **Посевы, которые обязаны читаться:** S12a (старик), S13b (ключи в луже),
  S14b (Бисмиллоҳ), S15b (лампа бензина), S20b (заправка уходит)

## ЧЕК-ЛИСТ ПРИЁМКИ БЛОКА
- [ ] Лицо Шохруха одинаковое во всех 30 панелях с ним
- [ ] Шрам на ЛЕВОЙ брови виден в S4a, S4b, S4c, S10a
- [ ] Рубашка СУХАЯ в S1a–S9b (токен [SHOHRUH-DRY]), мокрая с S9c и до конца фильма
- [ ] Оранжевая лампа бензина в S15b и S19a — один и тот же огонёк
- [ ] Двор в S12a и S12b — идентичный фон, меняется только передний план
- [ ] Туннель S23a→S23b→S23c — одна и та же геометрия, гаснут только лампы
- [ ] S24a→S24b→S24c — одна и та же стена, меняется только материал
- [ ] Весь блок холодный и десатурированный, кроме S16b и туннеля
