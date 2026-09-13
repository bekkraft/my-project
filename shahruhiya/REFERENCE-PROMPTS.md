# ШАҲРУҲИЯ — ЭТАЛОННЫЕ ИЗОБРАЖЕНИЯ (Фаза 1.5.4)

## ПОРЯДОК ГЕНЕРАЦИИ — ВАЖНО

1. Сначала **#1 (лицо Шохруха)**. Это референс-панель героя. Пока она не
   устроит — дальше не идти.
2. Затем **#2** (Шохрух в полный рост), подставив #1 как image reference.
3. Затем остальные персонажи (#3–#5) и объекты (#6–#7).
4. Локации (#8–#16) — в любом порядке, они друг от друга не зависят.
5. Все утверждённые эталоны потом подставляются как image reference
   в соответствующие панели раскадровки (Фаза 5).

## ЕДИНЫЙ СТИЛЕВОЙ СУФФИКС

Повторяется в КАЖДОМ промпте без изменений:

```
cinematic film still, 35mm film grain, natural motivated lighting,
shallow depth of field, subtle halation, 16:9
```

## ОБЩИЕ ЗАПРЕТЫ (negative prompt, если генератор поддерживает)

Для сцен прошлого: `no modern objects, no electric light, no plastic,
no wristwatch, no eyeglasses, no printed text, no power lines, no contrails`

Для всех: `no text overlay, no watermark, no logo, no extra fingers,
no distorted faces, no cartoon, no anime, no illustration`

---

# ПЕРСОНАЖИ

## #1. ШОХРУХ — ЛИЦО КРУПНО (референс-панель героя)

```
Cinematic film still, extreme close-up portrait, eye level, a 30-year-old
Uzbek man with an oval face and moderately defined cheekbones, dark brown
almond-shaped eyes with tired shadows beneath them, thick straight eyebrows
set low over the eyes, a thin white 1.5cm scar through his left eyebrow,
straight medium nose, medium-full lips with a slightly fuller lower lip,
uneven three-day stubble, very dark brown almost black short hair 3-4cm long
tousled on one side, wearing a white shirt with the collar wet, neutral
expression, looking directly into the lens, plain soft grey background,
soft diffused overcast window light from the left, cool neutral palette,
85mm lens, cinematic film still, 35mm film grain, natural motivated lighting,
shallow depth of field, subtle halation, 16:9
```

## #2. ШОХРУХ — В ПОЛНЫЙ РОСТ (одежда начала сцены)

```
Cinematic film still, full body shot, eye level, the same 30-year-old Uzbek
man, 178cm, ordinary non-athletic build, slightly stooped posture, dark brown
almond eyes, thick straight eyebrows, thin white scar on the left eyebrow,
three-day stubble, short dark tousled hair, wearing a white shirt wet on the
chest and collar with the top button undone and the second button missing,
dark blue jeans, a dark grey bomber jacket thrown on hastily with one sleeve
sitting crooked, dark boots, a metal-band watch on his left wrist, standing
in a plain empty room, soft diffused overcast light from a window on the left,
desaturated cool grey palette, 50mm lens, cinematic film still, 35mm film
grain, natural motivated lighting, shallow depth of field, subtle halation, 16:9
```

## #3. БОБУР — молодой воин XIV века

```
Cinematic film still, medium shot, eye level, a 22-year-old Central Asian
warrior of the late 14th century, 172cm, stocky with broad shoulders and a
short neck, broad face with round cheekbones, dark narrow lively curious eyes,
short eyebrows, slightly flattened nose, sparse youthful moustache and no
beard, black hair pulled back with a thin braid at his left temple, a
triangular leather amulet on a cord around his neck, wearing a quilted ochre
robe belted with a cloth sash over a plain undershirt, leather bracers,
knee-high leather boots, a sabre in a scabbard on his left hip, holding a felt
cap in one hand, standing in an open steppe camp, hard clear daylight,
ochre and dusty brown palette with steel accents, 50mm lens, cinematic film
still, 35mm film grain, natural motivated lighting, shallow depth of field,
subtle halation, 16:9
```

## #4a. АМИР ТЕМУР — В ШАТРЕ  [v4, канонический портрет + корона]

КЛИЕНТ ПРЕДОСТАВИЛ КАНОНИЧЕСКИЙ ПОРТРЕТ. Подставлять его как IMAGE
REFERENCE — тогда лицо совпадёт точно, а не «примерно».
РЕШЕНИЕ КЛИЕНТА: КОРОНА ВО ВСЕХ СЦЕНАХ, включая шатёр. Темур один и тот же
в каждом кадре, канонический образ не размывается. В лоу-кее шатра золото
короны даёт один горящий блик при половине лица в тени — власть читается
раньше лица.

```
Cinematic film still, medium shot, camera at the eye level of a seated man,
a Central Asian ruler of about 60 with a broad strong-jawed weathered face,
heavy dark eyebrows, DARK DEEP-SET EYES with a heavy gaze from beneath the
brows, tanned skin, lines on the forehead and around the eyes, a SHORT WEDGE
BEARD dark and heavily streaked with grey, moustache, wearing a GOLDEN DOMED
CROWN SET WITH DARK RED GEMSTONES AND TOPPED WITH A WHITE FEATHER PLUME,
dressed in a white fur-trimmed robe with GOLD FLORAL EMBROIDERY over a
patterned blue and deep red brocade tunic and a white undershirt, seated
cross-legged on LOW CUSHIONS directly on layered Persian carpets, leaning on
his left arm, his right arm resting motionless on his knee, a massive
tarnished silver ring with a dark red carnelian on his right ring finger,
inside a large 14th century TIMURID military command TENT, fabric walls and
carpets, oil lamps and candles as the only light, ONE BURNING HIGHLIGHT ON
THE GOLD OF THE CROWN, half his face in shadow, amber and deep red palette
with black shadows, 85mm lens, cinematic film still, 35mm film grain, natural
motivated lighting, shallow depth of field, subtle halation, 16:9
```

НЕГАТИВНЫЙ ПРОМПТ:
```
no throne, no wooden chair, no tiled walls, no palace interior, no long white
beard, no grey eyes, no turban, no crusaders, no red crosses, no european
armour, no modern objects
```

## #4b. АМИР ТЕМУР — ПЕРЕД ВОЙСКОМ (полный канон, кадры 87–100)

```
Cinematic film still, medium shot, low angle, the same Central Asian ruler of
about 60, broad strong-jawed weathered face, heavy dark eyebrows, DARK
DEEP-SET EYES, short wedge beard dark and heavily streaked with grey,
wearing a GOLDEN DOMED CROWN SET WITH DARK RED GEMSTONES AND TOPPED WITH A
WHITE FEATHER PLUME, a white fur-trimmed cloak with gold floral embroidery
over a patterned blue and deep red brocade robe, standing before an army on
an open steppe field at sunset, thousands of warriors and banners behind him
out of focus, horizontal golden hour light almost level with the ground,
dust burning in the air, bronze skin tones, red and gold palette, 50mm lens,
cinematic film still, 35mm film grain, natural motivated lighting, shallow
depth of field, subtle halation, 16:9
```

## #5. КОМАНДИР ОТРЯДА

```
Cinematic film still, medium shot, eye level, a 45-year-old Central Asian
warrior of the late 14th century, 175cm, thickset with a powerful neck,
weather-beaten sun-darkened face with deep vertical creases in the cheeks,
dark narrowed eyes, greying medium-length beard, a scar running through his
right eyebrow and cheekbone, wearing a dark green robe under lamellar plate
armour, leather bracers, boots, a sabre at his hip and a round shield on his
back, a pointed helmet held under his arm, standing in a military camp,
dark red banners bearing ONLY a three-circle emblem behind him,
hard clear daylight with sharp shadows, ochre and steel palette, 50mm lens, cinematic film still, 35mm film grain, natural
motivated lighting, shallow depth of field, subtle halation, 16:9
```

---

# ОБЪЕКТЫ-СИМВОЛЫ

## #6. НЕКСИЯ («ТЕМИР ОТ»)

```
Cinematic film still, three-quarter rear view, low angle, a grey Daewoo Nexia
III sedan with faded sun-worn paint, a deep unrepaired scratch down to the
primer on the right side of the rear bumper, a slightly clouded right wing
mirror, parked on wet asphalt in a Soviet-era apartment courtyard after night
rain, puddles reflecting the sky, bare trees behind, soft overcast morning
light, grey asphalt and green foliage palette, 35mm lens, cinematic film still,
35mm film grain, natural motivated lighting, shallow depth of field, subtle
halation, 16:9
```

## #7. ПЕРСТЕНЬ

```
Cinematic film still, extreme close-up macro, a massive ring of tarnished
blackened silver set with a large dark red carnelian stone, worn almost
illegible Arabic calligraphy engraved in the metal around the stone, resting
on a dark leather surface, a single warm low light source raking across the
metal, deep shadows, amber and dark red palette, 100mm macro lens, cinematic
film still, 35mm film grain, natural motivated lighting, shallow depth of
field, subtle halation, 16:9
```

---

# ЛОКАЦИИ

## #8. Л1 — СПАЛЬНЯ ШОХРУХА

```
Cinematic film still, wide shot, eye level, a small 3x4 metre bedroom in an
ordinary Tashkent apartment, an unmade bed against the wall with a sharp
exposed corner, a smartphone lying on the pillow, a white ceiling, a wardrobe
with one door ajar, a single window with a thin curtain on the left, empty of
people, soft diffused cool white morning light after rain from the left window,
almost no shadows, white and pale grey palette with warm wood, 24mm lens,
cinematic film still, 35mm film grain, natural motivated lighting, shallow
depth of field, subtle halation, 16:9
```

## #9. Л3 — ДВОР С ТАНДЫРОМ

```
Cinematic film still, wide shot, eye level, the courtyard of a Soviet-era
five-storey apartment block in Tashkent early morning, wet asphalt after night
rain with puddles reflecting the sky, an elderly Uzbek man in a tubeteika cap
sweeping with a long broom in the middle distance, smoke rising from a tandoor
oven catching slanted light, laundry lines between trees, a grey sedan parked
by an entrance, soft overcast morning light, grey asphalt and green foliage
with warm ochre smoke, 35mm lens, cinematic film still, 35mm film grain,
natural motivated lighting, shallow depth of field, subtle halation, 16:9
```

## #10. Л5 — УЛИЦЫ ТАШКЕНТА, УТРО (до туннеля)

```
Cinematic film still, wide shot from inside a car through the windscreen,
a three-lane Tashkent avenue in morning traffic, cars packed bumper to bumper,
traffic lights, wet asphalt reflecting red brake lights, trolleybus wires
overhead, high-rise buildings and billboards, overcast daylight, desaturated
cold steel-grey palette with red brake lights and a yellow traffic light as
the only colour accents, claustrophobic composition, 35mm lens, cinematic film
still, 35mm film grain, natural motivated lighting, shallow depth of field,
subtle halation, 16:9
```

## #11. Л6 — ТУННЕЛЬ, ИНТЕРЬЕР (ПОРТАЛ)  [v2, после первой генерации]

ПРОВАЛ ПЕРВОЙ ПОПЫТКИ: генератор снял въезд в туннель СНАРУЖИ, с моста,
с городом и машинами. Тот кадр сохранён отдельно как эталон для кадра 21
(поворот к туннелю), но главный эталон — вид ИЗНУТРИ — нужен заново.

```
Cinematic film still, wide shot from the driver's point of view inside a car,
looking straight down the INTERIOR of a road tunnel, perfectly centred
symmetrical composition, the tunnel stretching impossibly far into darkness
with no end visible, a long receding row of orange sodium lamps along the
ceiling, SEVERAL LAMPS ALREADY DARK breaking the rhythm, lane markings
running away from the camera, bare concrete walls close on both sides that
give way further in to ROUGH ANCIENT STONE WITH VEINS LIKE OLD ANIMAL HIDE,
no other cars, only headlights raking the walls in the foreground, amber
orange fading into coal black, claustrophobic, 24mm lens, cinematic film
still, 35mm film grain, natural motivated lighting, shallow depth of field,
subtle halation, 16:9
```

НЕГАТИВНЫЙ ПРОМПТ (обязателен):
```
no exterior view, no bridge, no sky, no daylight, no city skyline,
no other vehicles, no people, no street lamps outside
```

## #11b. Л6 — ВЪЕЗД В ТУННЕЛЬ, СНАРУЖИ (для кадра 21)

ПОЛУЧЕН с первой попытки — сохранить. Вид с эстакады на въезд в туннель
у цирка, оранжевое свечение внутри, сумеречный город. Используется в
кадре 21 («поворот к туннелю»), но НЕ как эталон локации Л6.

## #12. Л7 — СТЕПЬ (ТОЧКА ПРИБЫТИЯ)

```
Cinematic film still, extreme wide shot, low horizon, an endless Central Asian
steppe of green-brown grass with rolling hills breathing under the wind, wet
dark earth in the foreground after rain, thin campfire smoke rising far away
on the horizon, an enormous pale blue sky with fast-moving clouds, absolutely
no power lines, no buildings, no modern object anywhere, clear golden morning
light after rain, green-brown earth and ochre against pale blue, 24mm lens,
cinematic film still, 35mm film grain, natural motivated lighting, shallow
depth of field, subtle halation, 16:9
```

## #13. Л8 — ВОЕННЫЙ ЛАГЕРЬ

```
Cinematic film still, wide shot, slightly elevated angle, a vast late-14th
century Central Asian military camp of hundreds of tents and yurts stretching
to the horizon, banners bearing a three-circle emblem, campfires, horse lines,
large cooking cauldrons, stacked spears and round shields, dust hanging in the
air, warriors in quilted robes and lamellar armour in the middle distance,
hard clear daylight casting sharp shadows, campfire smoke scattering the light
in layers, ochre and dusty brown and leather with steel and dark red banners,
24mm lens, cinematic film still, 35mm film grain, natural motivated lighting,
shallow depth of field, subtle halation, 16:9
```

## #14. Л9 — ШАТЁР АМИРА ТЕМУРА (интерьер)  [v2, после первой генерации]

ПРОВАЛ ПЕРВОЙ ПОПЫТКИ — САМЫЙ ОПАСНЫЙ ИЗ ТРЁХ. Композиция, свет и
пространство вышли идеально: клин дневного света из входа, подушки на
коврах, жаровня с углями, центральная симметрия, лоу-кей от ламп. Но воины
по бокам оказались ЕВРОПЕЙСКИМИ КРЕСТОНОСЦАМИ — кольчуги, сюрко с красными
крестами, европейские лица. Генератор соединил «tent» + «14th century» и
выдал лагерь крестового похода. В фильме про Амира Темура это разрушение
мира, а не погрешность стиля.

```
Cinematic film still, wide shot, centred symmetrical composition, the interior
of an enormous 14th century CENTRAL ASIAN TIMURID military command tent,
layered Persian carpets covering the entire floor, low cushions arranged in
the centre, a brazier of glowing coals, oil lamps and candles as the only
light sources, a high fabric roof lost in shadow, a wedge of hard daylight
falling through the entrance flap at the far end, TWO ROWS OF TIMURID WARRIORS
standing along both sides like walls, Central Asian and Turkic men with dark
almond eyes and thin beards, wearing QUILTED ROBES in ochre and dark green
belted with cloth sashes, LAMELLAR PLATE ARMOUR, leather bracers, CURVED
SABRES at the hip, POINTED HELMETS with mail aventails, low-key lighting from
below and the side, amber and deep red with black shadows and golden
highlights, 24mm lens, cinematic film still, 35mm film grain, natural
motivated lighting, shallow depth of field, subtle halation, 16:9
```

НЕГАТИВНЫЙ ПРОМПТ (без него повторится):
```
no crusaders, no red crosses, no christian symbols, no european knights,
no chainmail hauberks, no surcoats, no tabards, no straight swords,
no european faces, no medieval european armour, no heraldry
```

## #15. Л10 — ГОРНАЯ ДОРОГА / УЩЕЛЬЕ

```
Cinematic film still, wide shot, low angle, a broken track through rocky
highland terrain like a wound in the earth, loose stones, deep mud, ruts and
boulders, a narrow gorge between two steep slopes visible in the distance,
late afternoon sun very low and backlit, long shadows reaching across the
frame, dust in the air, maximum contrast between orange-gold light and cold
blue shadows, 35mm lens, cinematic film still, 35mm film grain, natural
motivated lighting, shallow depth of field, subtle halation, 16:9
```

## #16. Л12 — ТАШКЕНТ, ФИНАЛ

```
Cinematic film still, wide shot, eye level, the same Tashkent avenue as before
but now in risen morning sun, warm low light breaking between the buildings
and playing on drying wet asphalt, puddles shrinking, trees lining the road,
a woman carrying flatbread from a tandoor, a child running after a bus,
the Amir Temur monument with the horseman's arm pointing east visible down the
street, unhurried composition with air around everything, warm golden and green
and ochre palette, the exact opposite of the earlier cold steel grey,
35mm lens, cinematic film still, 35mm film grain, natural motivated lighting,
shallow depth of field, subtle halation, 16:9
```

---

## #17. СКВЕР АМИРА ТЕМУРА, ВИД СВЕРХУ (кадр 121, финальный подъём камеры)

Референс предоставлен клиентом. Решает финальный кадр: город раскрывается
как КОЛЕСО, а в центре — тот, кто дал герою имя. Рифма к полю, где тысячи
воинов стояли кольцом вокруг Темура.

```
Cinematic film still, extreme wide aerial shot rising above a city square,
a large CIRCULAR PARK with radial tree-lined paths converging on an
equestrian monument at the exact centre on a round pedestal, the rider's arm
raised pointing east, a ring road encircling the park, dense green trees,
neoclassical buildings around the perimeter, a modern Central Asian city
skyline beyond, early morning sun low and warm, wet asphalt still drying on
the ring road, warm golden and green palette, 24mm lens, cinematic film still,
35mm film grain, natural motivated lighting, shallow depth of field, subtle
halation, 16:9
```

---

# СТАТУС ГЕНЕРАЦИИ

| # | Эталон | Статус | Комментарий |
|---|---|---|---|
| 1 | Шохрух, лицо | ПРИНЯТ — РЕФЕРЕНС-ПАНЕЛЬ ГЕРОЯ | шрам на левой брови виден, тени под глазами, неровная щетина, миндалевидные тёмно-карие. Подставляется во ВСЕ панели с героем |
| 2 | Шохрух, полный рост | ПРИНЯТ | бомбер криво, мокрая рубашка, джинсы, часы на левом запястье, сутулость. Мелочь: обувь вышла как резиновые сапоги — в раскадровке заменить на ботинки |
| 3 | Бобур | ПРИНЯТ | тумор, косичка, халат, сабля, наручи, шапка. Открыт вопрос об этнических чертах |
| 4a | Темур в шатре | ПЕРЕДЕЛАТЬ по каноническому портрету | клиент дал канонический референс — подставлять как image reference. КОРОНА (решение клиента: во всех сценах), подушки в шатре вместо трона |
| 4b | Темур перед войском | НОВЫЙ | полный канон с золотой короной и белым пером, закат, войско за спиной |
| 5 | Командир отряда | ПРИНЯТ с правкой | убрать знамя со львом на заднем плане |
| 6 | Нексия | ПРИНЯТ | серая выцветшая, потёртость до грунта на правой задней части, мокрый двор с лужами. СОХРАНИТЬ РАКУРС: кадр 111 (бампер со следом сабли) снимается с того же угла |
| 7 | Перстень | ПРИНЯТ | потемневшее серебро, тёмно-красный камень, арабская вязь по ободку, кожа, тёплый рейкинг-свет |
| 8 | Л1 спальня | ПРИНЯТ | белая обычная, незастеленная, телефон на подушке, шкаф, окно слева, холодный плоский свет |
| 9 | Л3 двор | ПРИНЯТ | лучше задуманного: тандыр как пекарня в гараже. При раскадровке поставить у подъезда серую Нексию |
| 10 | Л5 улицы Ташкента | ПРИНЯТ | вид из салона, дворники и капли, пробка, красные стоп-сигналы на сером, провода, реальные узбекские бренды на билбордах |
| 11 | Л6 туннель, интерьер | ПЕРЕДЕЛАТЬ | снят снаружи с моста вместо вида изнутри |
| 11b | Л6 въезд снаружи | ПРИНЯТ как бонус | используется в кадре 21, не как эталон локации |
| 12 | Л7 степь | ПРИНЯТ | дышащие холмы, мокрая земля с лужами на переднем плане, дымы на горизонте, огромное небо, ни одного провода |
| 13 | Л8 лагерь | ПРИНЯТ | ЗНАМЁНА С ТРЕМЯ КОЛЬЦАМИ, сотни юрт до горизонта, копья, круглые щиты, котлы, костры, пыль слоями |
| 14 | Л9 шатёр | ПЕРЕДЕЛАТЬ — КРИТИЧНО | композиция, свет и пространство идеальны, но воины оказались ЕВРОПЕЙСКИМИ КРЕСТОНОСЦАМИ в сюрко с красными крестами |
| 15 | Л10 горная дорога | ПРИНЯТ | разбитая колея, грязь и лужи, валуны, ущелье вдали, контровой закат, оранжевое против синих теней |
| 16 | Л12 Ташкент финал | ПРИНЯТ | памятник с рукой на восток, женщина с лепёшками, ребёнок за автобусом, тёплый золотой, мокрый асфальт |
| 17 | Сквер сверху (кадр 121) | НОВЫЙ | референс от клиента: круглый парк, радиальные аллеи, памятник в центре, кольцевая дорога |

**Итого: 13 принято. Осталось 5: Темур в шатре (4a), Темур перед войском (4b), шатёр (14), туннель изнутри (11), сквер сверху (17).**

---

# ЧЕК-ЛИСТ ПРИЁМКИ ЭТАЛОНОВ

- [ ] #1 и #2 — ОДНО И ТО ЖЕ ЛИЦО (шрам на левой брови, щетина, тени под глазами)
- [ ] Темур СИДИТ, правая рука неподвижна на колене, глаза СВЕТЛО-СЕРЫЕ
- [ ] На перстне читается тёмно-красный камень и стёртая вязь
- [ ] На Нексии видна царапина на правой стороне заднего бампера
- [ ] В степи и лагере НЕТ проводов, высоток, следов самолётов
- [ ] Туннель: лампы уходят вдаль, часть уже погасла, бетон переходит в камень
- [ ] Ташкент начальный — холодный серо-стальной; Ташкент финальный — тёплый золотой
- [ ] Во всех 16 виден один и тот же характер плёнки и зерна
