# ФАЗА 6 — ВИДЕО-ПРОМПТЫ (124 сцены)
## Протокол «Сториборд → фильм», раздел 5.6

## ПРАВИЛО «ОСНОВА = ПАНЕЛЬ» (жёсткое)

Панель сториборда — это БАЗА сцены. Композиция, ракурс, объекты, персонаж,
свет, цвет и одежда **сохраняются в видео без изменений**. Видео-промпт
описывает ТОЛЬКО движение камеры, движение объектов и действие во времени
поверх этой основы.

**Запрещено** менять ракурс, композицию, объекты, свет или одежду персонажа
относительно панели. Любое отличие — согласуется с клиентом отдельно.

Поэтому промпты здесь КОРОТКИЕ. Всё, что описано в панели, повторно не
пишется: оно приходит со стартовым кадром.

## ФОРМАТ КАЖДОЙ СЦЕНЫ
```
[SCENE <ID>]
Base frame: storyboard panel <ID>. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: <что движется и что происходит во времени>
Camera: <движение камеры или static>
```

## КАК ОТПРАВЛЯТЬ В ГЕНЕРАЦИЮ
1. Найти панель по ID в пакете-манифесте (`MANIFEST.md`)
2. Подставить её как **start frame / image reference**
3. Отправить промпт с тем же ID
4. Отправлять ВЕСЬ пакет целиком: картинки панелей + промпты с ID

## ЕСЛИ ГЕНЕРАТОР НЕ ПОДДЕРЖИВАЕТ СТАРТОВЫЙ КАДР
Только тогда — и только тогда — дописать в конец промпта стилевой хвост:
```
35mm film grain, natural motivated lighting, shallow depth of field, subtle halation, cinematic, 16:9
```
При работающем стартовом кадре этот хвост НЕ НУЖЕН: стиль приходит с панелью.

---

# АКТ 1 — ТАШКЕНТ И ТУННЕЛЬ

### [SCENE S1a] · 3 сек
```
[SCENE S1a]
Base frame: storyboard panel S1a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: a male finger enters frame, swipes across the phone screen, the alarm display goes dark, the hand withdraws.
Camera: static.
```

### [SCENE S2a] · 2 сек
```
[SCENE S2a]
Base frame: storyboard panel S2a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the sleeping man does not wake as the alarm rings again offscreen, only his brow tightening and one hand twitching.
Camera: very slight handheld drift.
```

### [SCENE S3a] · 2 сек
```
[SCENE S3a]
Base frame: storyboard panel S3a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the same finger swipes the alarm away again and withdraws out of frame.
Camera: static.
```

### [SCENE S4a] · 2 сек
```
[SCENE S4a]
Base frame: storyboard panel S4a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the closed eyelids crack open unfocused, then snap fully open and fix straight ahead.
Camera: almost imperceptible push-in.
```

### [SCENE S5a] · 2 сек
```
[SCENE S5a]
Base frame: storyboard panel S5a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: nothing moves at all. One held beat of stillness.
Camera: static.
```

### [SCENE S6a] · 2 сек
```
[SCENE S6a]
Base frame: storyboard panel S6a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the man's blank face snaps into panic, eyebrows flying up, head lifting off the pillow.
Camera: fast crash zoom in.
```

### [SCENE S7a] · 4 сек
```
[SCENE S7a]
Base frame: storyboard panel S7a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he throws off the sheets, twists off the bed, lunges forward and slams his hip into the sharp corner of the bed frame, folding sideways.
Camera: violent handheld following the body.
```

### [SCENE S8a] · 2 сек
```
[SCENE S8a]
Base frame: storyboard panel S8a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: his hand clamps onto the struck hip and his face contorts, teeth bared, eyes squeezed shut.
Camera: handheld.
```

### [SCENE S9a] · 4 сек
```
[SCENE S9a]
Base frame: storyboard panel S9a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he fills his cupped hands under the tap, drives the water into his own face, and lifts his dripping head as water soaks his collar and chest.
Camera: handheld.
```

### [SCENE S10a] · 3 сек
```
[SCENE S10a]
Base frame: storyboard panel S10a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: water droplets run slowly down the mirror glass, the fragmented reflection shifting as the drops travel.
Camera: static.
```

### [SCENE S11a] · 3 сек
```
[SCENE S11a]
Base frame: storyboard panel S11a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: wet fingers pinch the shirt button, slip off it twice, then give up and drop away leaving the shirt hanging open.
Camera: handheld.
```

### [SCENE S12a] · 5 сек
```
[SCENE S12a]
Base frame: storyboard panel S12a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the old man sweeps at his own unhurried pace, tandoor smoke drifts, and a blurred dark figure rushes across the very foreground close to the lens without slowing.
Camera: static.
```

### [SCENE S13a] · 3 сек
```
[SCENE S13a]
Base frame: storyboard panel S13a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the keys fall and strike the puddle, water bursting upward in a crown and shattering the reflection, then a hand plunges in and snatches them out.
Camera: handheld.
```

### [SCENE S14a] · 3 сек
```
[SCENE S14a]
Base frame: storyboard panel S14a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he pushes the key into the ignition and mutters one short word under his breath without meaning it, his eyes already forward.
Camera: static.
```

### [SCENE S15a] · 3 сек
```
[SCENE S15a]
Base frame: storyboard panel S15a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the dials wake, both needles sweep up, and a single orange low-fuel warning lamp lights and stays burning.
Camera: static.
```

### [SCENE S16a] · 4 сек
```
[SCENE S16a]
Base frame: storyboard panel S16a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the headlights switch on and throw a warm inverted reflection of the apartment block into the puddle, a small city appearing upside down in the water.
Camera: slow tilt down toward the water.
```

### [SCENE S17a] · 3 сек
```
[SCENE S17a]
Base frame: storyboard panel S17a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the wipers sweep across the rain-beaded glass, brake lights pulsing in the stalled traffic beyond.
Camera: handheld.
```

### [SCENE S18a] · 4 сек
```
[SCENE S18a]
Base frame: storyboard panel S18a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he looks down at the phone in his hand, snaps his eyes up to the road, then drops them back to the screen again.
Camera: handheld.
```

### [SCENE S19a] · 2 сек
```
[SCENE S19a]
Base frame: storyboard panel S19a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the orange low-fuel lamp burns steadily, the digital display holding at 8:02.
Camera: static.
```

### [SCENE S20a] · 3 сек
```
[SCENE S20a]
Base frame: storyboard panel S20a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the petrol station slides steadily across the window and out of frame as the car passes it without slowing.
Camera: lateral tracking with the moving car.
```

### [SCENE S21a] · 4 сек
```
[SCENE S21a]
Base frame: storyboard panel S21a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: both hands haul the steering wheel hard right and the concrete mouth of the underpass swings into the windscreen.
Camera: handheld.
```

### [SCENE S22a] · 4 сек
```
[SCENE S22a]
Base frame: storyboard panel S22a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: hard bands of orange lamp light sweep rhythmically across the driver's face as the car runs deeper into the tunnel.
Camera: handheld that gradually settles and stops dead.
```

### [SCENE S23a] · 4 сек — КАМЕРА ВПЕРВЫЕ НА ШТАТИВЕ
```
[SCENE S23a]
Base frame: storyboard panel S23a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the receding row of orange ceiling lamps goes out one by one from the far end toward the camera until darkness swallows the tunnel.
Camera: slow steady push-in on a locked tripod.
```

### [SCENE S24a] · 3 сек — МОРФ БЕЗ СКЛЕЙКИ
```
[SCENE S24a]
Base frame: storyboard panel S24a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the poured concrete surface transforms continuously into rough ancient hewn stone as the camera travels along it, with no cut anywhere in the move.
Camera: slow lateral tracking along the wall in one unbroken take.
```

### [SCENE S25a] · 3 сек
```
[SCENE S25a]
Base frame: storyboard panel S25a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the hands tighten on the wheel until the knuckles whiten, then the boot presses the brake pedal flat to the floor meeting no resistance at all.
Camera: static.
```

### [SCENE S26a] · 3 сек
```
[SCENE S26a]
Base frame: storyboard panel S26a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the point of white light ahead swells rapidly until it fills the entire windscreen and burns the frame out completely.
Camera: static.
```

### [SCENE S27a] · 2 сек
```
[SCENE S27a]
Base frame: storyboard panel S27a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: nothing. Only the faintest grain moving in a blank white frame.
Camera: static.
```

---

# АКТ 2 — СТЕПЬ, ЛАГЕРЬ, ШАТЁР

### [SCENE S28a] · 3 сек
```
[SCENE S28a]
Base frame: storyboard panel S28a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the closed eyelids open in exactly the same way as in the bedroom, open sky and grassland now reflected in the iris.
Camera: static.
```

### [SCENE S29a] · 6 сек — САМЫЙ ДЛИННЫЙ КАДР ФИЛЬМА
```
[SCENE S29a]
Base frame: storyboard panel S29a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the steppe grass moves under the wind, clouds travel fast overhead, distant campfire smoke drifts. Nothing else happens for the full duration.
Camera: absolutely static locked-off for the entire shot.
```

### [SCENE S30a] · 4 сек
```
[SCENE S30a]
Base frame: storyboard panel S30a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the car door swings wide, the man climbs out unsteadily, and his knees buckle as he grabs the door frame for support.
Camera: locked tripod.
```

### [SCENE S31a] · 2 сек
```
[SCENE S31a]
Base frame: storyboard panel S31a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the boot presses down into the wet earth and water wells up around the sole.
Camera: static.
```

### [SCENE S32a] · 3 сек
```
[SCENE S32a]
Base frame: storyboard panel S32a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the emptiness opens out to every horizon as the camera rises, the car and the single figure shrinking below.
Camera: slow steady drone ascent.
```

### [SCENE S33a] · 3 сек
```
[SCENE S33a]
Base frame: storyboard panel S33a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the view travels across the horizon from thin smoke columns to scattered tents to a vast camp of hundreds of yurts filling the frame.
Camera: slow horizontal pan.
```

### [SCENE S34a] · 2 сек
```
[SCENE S34a]
Base frame: storyboard panel S34a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the warriors stop mid-task and turn their heads in unison, a hand closes on a sabre grip, and the curved blade rips clear of its scabbard.
Camera: static, then a sharp snap.
```

### [SCENE S35a] · 2 сек
```
[SCENE S35a]
Base frame: storyboard panel S35a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the ring of armed warriors closes tighter around the car, shadows swinging inward.
Camera: static.
```

### [SCENE S36a] · 2 сек
```
[SCENE S36a]
Base frame: storyboard panel S36a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he throws both arms up above his head, palms out, shouting at the armed men around him.
Camera: sudden handheld.
```

### [SCENE S37a] · 2 сек
```
[SCENE S37a]
Base frame: storyboard panel S37a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the warrior's brows draw together in total incomprehension and he says something short and guttural.
Camera: static.
```

### [SCENE S38a] · 2 сек
```
[SCENE S38a]
Base frame: storyboard panel S38a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the three warriors take deliberate steps toward the lens, blades rising higher, dust lifting from their boots.
Camera: static.
```

### [SCENE S39a] · 5 сек ★
```
[SCENE S39a]
Base frame: storyboard panel S39a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he lowers his raised hand to lay the palm flat over his heart, closes his eyes, and speaks clearly and deliberately, his face going calm for the first time.
Camera: very slow push-in.
```

### [SCENE S40a] · 2 сек
```
[SCENE S40a]
Base frame: storyboard panel S40a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the sabre blade stops dead at the top of its arc and hangs motionless in the air.
Camera: static.
```

### [SCENE S41a] · 4 сек
```
[SCENE S41a]
Base frame: storyboard panel S41a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the older scarred warrior looks steadily ahead weighing what he has heard, giving nothing away, barely blinking, for the full duration.
Camera: absolutely static.
```

### [SCENE S42a] · 3 сек
```
[SCENE S42a]
Base frame: storyboard panel S42a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he lowers his sabre until it hangs point-down at his side and answers quietly, and the warriors behind him lower their blades in turn.
Camera: static.
```

### [SCENE S43a] · 3 сек
```
[SCENE S43a]
Base frame: storyboard panel S43a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the hand settles onto the warm bonnet and strokes it slowly the way a man calms a horse.
Camera: static.
```

### [SCENE S44a] · 3 сек
```
[SCENE S44a]
Base frame: storyboard panel S44a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he lifts the bonnet, the watching warriors flinch back a step, then crowd in close behind to stare into the engine bay.
Camera: static.
```

### [SCENE S45a] · 3 сек
```
[SCENE S45a]
Base frame: storyboard panel S45a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: a warrior's bare fingers touch the hot engine, he recoils a full step with his burnt hand snatched to his chest, eyes wide, whispering.
Camera: sharp handheld on the reaction.
```

### [SCENE S46a] · 3 сек
```
[SCENE S46a]
Base frame: storyboard panel S46a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the commander asks a short question across the open engine bay, brows drawn.
Camera: static.
```

### [SCENE S47a] · 3 сек
```
[SCENE S47a]
Base frame: storyboard panel S47a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he pauses, the corner of his mouth lifting, and answers with a precise number.
Camera: static.
```

### [SCENE S48a] · 3 сек
```
[SCENE S48a]
Base frame: storyboard panel S48a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the warriors turn to look at one another, baffled, one shaking his head slowly.
Camera: static.
```

### [SCENE S49a] · 5 сек ★
```
[SCENE S49a]
Base frame: storyboard panel S49a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the old man lays his open palm on the bonnet, closes his eyes, listens to the running engine through the metal, and nods slowly.
Camera: static.
```

### [SCENE S50a] · 4 сек
```
[SCENE S50a]
Base frame: storyboard panel S50a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the young warrior sits rigid gripping the seat edge while the driver reaches over and fastens the seatbelt across him, the buckle clicking home.
Camera: locked to the moving car.
```

### [SCENE S51a] · 6 сек
```
[SCENE S51a]
Base frame: storyboard panel S51a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the warrior points out of the window and names things, the driver taps the wheel and names things back, the warrior fails to repeat a word, and both of them break into laughter.
Camera: locked to the moving car, cut as a series of quick jump cuts.
```

### [SCENE S52a] · 4 сек
```
[SCENE S52a]
Base frame: storyboard panel S52a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the young warrior watches the passing steppe and speaks quietly without turning his head.
Camera: locked to the moving car.
```

### [SCENE S53a] · 4 сек
```
[SCENE S53a]
Base frame: storyboard panel S53a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the car and the four flanking horsemen travel together across the grassland, dust trailing behind them, banners swaying.
Camera: high steady drone tracking alongside.
```

### [SCENE S54a] · 4 сек
```
[SCENE S54a]
Base frame: storyboard panel S54a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the tent flap is drawn aside from outside, the wedge of white daylight widens across the carpets, and a modern man steps into it as a black silhouette.
Camera: static.
```

### [SCENE S55a] · 3 сек
```
[SCENE S55a]
Base frame: storyboard panel S55a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the warriors along the walls stay motionless; only the coals in the brazier shift and the lamp flames move.
Camera: absolutely static.
```

### [SCENE S56a] · 3 сек
```
[SCENE S56a]
Base frame: storyboard panel S56a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the seated ruler studies his own hands and does not look up. Nothing else moves.
Camera: absolutely static.
```

### [SCENE S57a] · 4 сек
```
[SCENE S57a]
Base frame: storyboard panel S57a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he speaks slowly without lifting his eyes; nothing in his body moves at all.
Camera: absolutely static.
```

### [SCENE S58a] · 4 сек ★ ГЛАВНЫЙ КАДР СЦЕНЫ
```
[SCENE S58a]
Base frame: storyboard panel S58a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the heavy eyelids rise slowly and the gaze comes up from beneath the brows to fix directly into the lens. The head does not move at all.
Camera: absolutely static.
```

### [SCENE S59a] · 3 сек
```
[SCENE S59a]
Base frame: storyboard panel S59a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the modern man bows awkwardly, catches his balance, straightens and answers, swallowing hard.
Camera: absolutely static.
```

### [SCENE S60a] · 4 сек
```
[SCENE S60a]
Base frame: storyboard panel S60a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he says one short flat sentence and then holds a long silence, eyes fixed forward, nothing moving.
Camera: absolutely static.
```

### [SCENE S61a] · 4 сек ★ ЕДИНСТВЕННОЕ ДВИЖЕНИЕ КАМЕРЫ В ШАТРЕ
```
[SCENE S61a]
Base frame: storyboard panel S61a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he listens, then the understanding lands, his eyes widen fractionally, his lips part and his face goes slack as the ground leaves him.
Camera: almost imperceptible push-in.
```

### [SCENE S62a] · 4 сек
```
[SCENE S62a]
Base frame: storyboard panel S62a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he speaks with grim weight, eyes fixed forward, nothing else moving.
Camera: absolutely static.
```

### [SCENE S63a] · 3 сек
```
[SCENE S63a]
Base frame: storyboard panel S63a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the man interrupts with one hand half raised, and behind him every warrior along the walls shifts a fraction toward him with hands moving to sabre grips.
Camera: absolutely static.
```

### [SCENE S64a] · 3 сек ★
```
[SCENE S64a]
Base frame: storyboard panel S64a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the stone-still face holds, and then one corner of the mouth lifts a few millimetres into the faintest possible smile.
Camera: absolutely static.
```

---

# АКТ 3 — ГОНКА

### [SCENE S65a] · 3 сек
```
[SCENE S65a]
Base frame: storyboard panel S65a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the hand comes to rest flat on the bonnet, he bows his head and speaks one word slowly and deliberately, looking at the metal.
Camera: static.
```

### [SCENE S66a] · 2 сек
```
[SCENE S66a]
Base frame: storyboard panel S66a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the seatbelt buckle clicks home and the young warrior looks down at it and nods once, his hands no longer gripping the seat.
Camera: static.
```

### [SCENE S67a] · 3 сек
```
[SCENE S67a]
Base frame: storyboard panel S67a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the car threads out through the rows of the camp and pulls away alone onto open grassland with a long plume of dust behind it.
Camera: drone tracking and rising.
```

### [SCENE S68a] · 2 сек
```
[SCENE S68a]
Base frame: storyboard panel S68a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: wind moves loose dust across the broken track. Nothing else.
Camera: static.
```

### [SCENE S69a] · 3 сек
```
[SCENE S69a]
Base frame: storyboard panel S69a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: both men are thrown upward by a rut, the passenger twists and points hard left shouting, and the driver hauls the wheel over.
Camera: rigidly mounted to the car, shaking with the suspension, NOT handheld.
```

### [SCENE S70a] · 2 сек
```
[SCENE S70a]
Base frame: storyboard panel S70a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the sealed scroll shakes violently against the seat fabric under its stone but does not slide.
Camera: mounted to the car, vibrating.
```

### [SCENE S71a] · 2 сек
```
[SCENE S71a]
Base frame: storyboard panel S71a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the jagged rock drags hard against the metal underbody, tearing a bright fresh scrape and throwing grit outward.
Camera: tracking along with the car.
```

### [SCENE S72a] · 2 сек
```
[SCENE S72a]
Base frame: storyboard panel S72a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the wheel spins fast and throws an arc of wet mud backward while the car itself does not move at all.
Camera: static.
```

### [SCENE S73a] · 3 сек ★
```
[SCENE S73a]
Base frame: storyboard panel S73a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: one man pushes the stuck car alone and gets nowhere, then a second walks into frame and sets his hands beside him, and together they force it out of the rut.
Camera: static.
```

### [SCENE S74a] · 2 сек
```
[SCENE S74a]
Base frame: storyboard panel S74a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the two muddy men catch each other's eye, breathing hard, and one nods once.
Camera: static.
```

### [SCENE S75a] · 3 сек
```
[SCENE S75a]
Base frame: storyboard panel S75a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the column marches unhurried into the gorge mouth, the head of it passing into cold shadow while the tail is still in sunlight.
Camera: static.
```

### [SCENE S76a] · 2 сек
```
[SCENE S76a]
Base frame: storyboard panel S76a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the hidden warriors stay crouched and motionless, only one head turning to track the column passing below.
Camera: static.
```

### [SCENE S77a] · 2 сек
```
[SCENE S77a]
Base frame: storyboard panel S77a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he raises his palm above the wheel and slams it down flat, the whole arm locked, mouth open.
Camera: static.
```

### [SCENE S78a] · 2 сек
```
[SCENE S78a]
Base frame: storyboard panel S78a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the whole front of the column stops and wheels around toward the camera, hands going to sabre grips, banners swaying.
Camera: fast pan following the sound.
```

### [SCENE S79a] · 3 сек
```
[SCENE S79a]
Base frame: storyboard panel S79a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the car tears forward trailing a wall of dust, slides sideways to a locked halt on loose stone, and stands silent as the dust settles and warriors close in.
Camera: static.
```

### [SCENE S80a] · 2 сек
```
[SCENE S80a]
Base frame: storyboard panel S80a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: every light on the panel dies at once and both needles drop to their bottom stops, the fuel needle hard against empty.
Camera: static.
```

### [SCENE S81a] · 3 сек
```
[SCENE S81a]
Base frame: storyboard panel S81a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he half falls out of the door, drops to both knees on loose stone and thrusts the sealed scroll up above his head in both hands, shouting.
Camera: static.
```

### [SCENE S82a] · 3 сек
```
[SCENE S82a]
Base frame: storyboard panel S82a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he breaks the wax seal, his eyes race across the writing, then his head snaps up and he throws out an arm shouting an order as the column behind begins to turn.
Camera: static.
```

### [SCENE S83a] · 3 сек
```
[SCENE S83a]
Base frame: storyboard panel S83a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: distant silhouetted figures fight on the slope, almost unreadable through dust, then the movement stops and the dust begins to thin.
Camera: static.
```

### [SCENE S84a] · 3 сек
```
[SCENE S84a]
Base frame: storyboard panel S84a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the man's hands shake visibly, and the young warrior lowers himself down beside him and holds out a round flatbread.
Camera: static.
```

### [SCENE S85a] · 2 сек
```
[SCENE S85a]
Base frame: storyboard panel S85a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he chews and makes a tired wry joke, and the warrior beside him laughs openly without understanding it.
Camera: static.
```

### [SCENE S86a] · 3 сек
```
[SCENE S86a]
Base frame: storyboard panel S86a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the thin smudge of dust on the horizon grows into a broad rolling cloud with the dark shapes of a mounted column emerging beneath it.
Camera: static.
```

### [SCENE S87a] · 4 сек
```
[SCENE S87a]
Base frame: storyboard panel S87a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the long trumpets sound, thousands roar across the field, and every voice stops at once as a single open hand is raised.
Camera: slow crane rising.
```

---

# АКТ 3 — ИМЯ И ПЕРСТЕНЬ

### [SCENE S88a] · 2 сек
```
[SCENE S88a]
Base frame: storyboard panel S88a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he extends an arm to indicate someone aside and speaks loudly to the army, then lowers the arm.
Camera: static.
```

### [SCENE S89a] · 3 сек
```
[SCENE S89a]
Base frame: storyboard panel S89a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he asks a short question, eyes fixed on the man before him.
Camera: static.
```

### [SCENE S90a] · 2 сек
```
[SCENE S90a]
Base frame: storyboard panel S90a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the exhausted man says one short word quietly.
Camera: static.
```

### [SCENE S91a] · 4 сек
```
[SCENE S91a]
Base frame: storyboard panel S91a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he says nothing at all and simply looks, weighing, barely blinking, for the full duration.
Camera: absolutely static.
```

### [SCENE S92a] · 8 сек
```
[SCENE S92a]
Base frame: storyboard panel S92a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he turns away from the man, addresses the massed army at length, and raises one hand chest high as he speaks. The whole field stays silent and listening, banners stirring.
Camera: extremely slow push-in across the full duration.
```

### [SCENE S93a] · 2 сек
```
[SCENE S93a]
Base frame: storyboard panel S93a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the ranks stand utterly still, some mouths falling slightly open as they realise what is coming.
Camera: static.
```

### [SCENE S94a] · 4 сек ★ ПИК ФИЛЬМА
```
[SCENE S94a]
Base frame: storyboard panel S94a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he draws breath, shouts a single word at full volume with the cords of his neck standing out, then raises one arm high above his head as he finishes the proclamation.
Camera: static.
```

### [SCENE S95a] · 4 сек
```
[SCENE S95a]
Base frame: storyboard panel S95a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: thousands thrust weapons and fists up in unison roaring one name, banners shaking, as the camera climbs.
Camera: crane rising steadily.
```

### [SCENE S96a] · 2 сек
```
[SCENE S96a]
Base frame: storyboard panel S96a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he rises from the cushions with visible effort, weight taken entirely on his left side, and comes fully upright. Nobody moves to help him.
Camera: static.
```

### [SCENE S97a] · 8 сек ★★ ОДИН НЕПРЕРЫВНЫЙ ПЛАН, БЕЗ СКЛЕЕК
```
[SCENE S97a]
Base frame: storyboard panel S97a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he walks the full length of the corridor of silent warriors toward the lone modern man, limping heavily on his right leg the whole way and arriving face to face with him. Nobody else moves anywhere in frame.
Camera: absolutely static locked-off for the entire eight seconds, with no cut of any kind.
```

### [SCENE S98a] · 2 сек
```
[SCENE S98a]
Base frame: storyboard panel S98a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the old hands work the heavy ring off over the knuckle, leaving a pale band of untanned skin.
Camera: static.
```

### [SCENE S99a] · 3 сек ★
```
[SCENE S99a]
Base frame: storyboard panel S99a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the old hands slide the ring onto the younger mud-stained finger, seat it at the base, and withdraw.
Camera: almost imperceptible push-in.
```

### [SCENE S100a] · 3 сек
```
[SCENE S100a]
Base frame: storyboard panel S100a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he leans in very slightly and speaks quietly, only to the man in front of him, then falls silent, his expression uncharacteristically soft for a moment.
Camera: static.
```

### [SCENE S101a] · 2 сек
```
[SCENE S101a]
Base frame: storyboard panel S101a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the eyes go glassy with unshed tears and he blinks once slowly.
Camera: static.
```

---

# АКТ 3 — РАСТВОРЕНИЕ И ВОЗВРАТ

### [SCENE S102a] · 3 сек
```
[SCENE S102a]
Base frame: storyboard panel S102a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the car and the four riders travel together along the track, banners swaying under the burning sky.
Camera: slow lateral tracking alongside.
```

### [SCENE S103a] · 3 сек
```
[SCENE S103a]
Base frame: storyboard panel S103a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he raises his hand off the wheel to turn the ring on his finger in the last light, looks at it, then lowers the hand back and smiles privately.
Camera: static.
```

### [SCENE S104a] · 3 сек
```
[SCENE S104a]
Base frame: storyboard panel S104a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the riding warriors lose solidity, the steppe showing through their bodies, until only faint ghost outlines remain and then nothing.
Camera: static.
```

### [SCENE S105a] · 3 сек ★ ЕДИНСТВЕННЫЙ ОПТИЧЕСКИЙ ПЕРЕХОД
```
[SCENE S105a]
Base frame: storyboard panel S105a. Keep its framing, angle, composition and objects exactly as they are. The colour change described below is the ONLY permitted deviation.
Motion: all colour drains continuously out of the skin, the wheel, the dashboard and the world beyond the glass until the entire frame is monochrome grey, while the ring alone keeps full saturated colour and its dark red stone burns against the grey.
Camera: static.
```

### [SCENE S106a] · 2 сек
```
[SCENE S106a]
Base frame: storyboard panel S106a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the boot presses the brake pedal flat to the floor and it meets no resistance at all.
Camera: static.
```

### [SCENE S107a] · 2 сек
```
[SCENE S107a]
Base frame: storyboard panel S107a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the point of white light swells until it fills and burns out the entire frame.
Camera: static.
```

### [SCENE S108a] · 2 сек
```
[SCENE S108a]
Base frame: storyboard panel S108a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the car emerges from the tunnel mouth into an ordinary morning street, the city opening out ahead.
Camera: static.
```

### [SCENE S109a] · 2 сек
```
[SCENE S109a]
Base frame: storyboard panel S109a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the digital display holds steady at 7:48, the dials lit.
Camera: static.
```

---

# ФИНАЛ — ТАШКЕНТ

### [SCENE S110a] · 3 сек
```
[SCENE S110a]
Base frame: storyboard panel S110a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: morning sunlight moves slowly across the ring's metal and stone as the car rolls, the hand relaxed on the wheel.
Camera: static.
```

### [SCENE S111a] · 3 сек
```
[SCENE S111a]
Base frame: storyboard panel S111a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the single dry stalk of steppe grass caught in the wheel arch moves in the breeze beside the fresh blade cut.
Camera: static.
```

### [SCENE S112a] · 2 сек
```
[SCENE S112a]
Base frame: storyboard panel S112a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the orange low-fuel warning lamp burns steadily, exactly as it did at the start of the film.
Camera: static.
```

### [SCENE S113a] · 3 сек
```
[SCENE S113a]
Base frame: storyboard panel S113a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: he looks out and up through the windscreen, then turns his head unhurriedly to the side window. Sunlight moves across his face in bars as trees pass.
Camera: locked to the slowly moving car.
```

### [SCENE S114a] · 3 сек
```
[SCENE S114a]
Base frame: storyboard panel S114a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the old man sweeps, the woman carries her stack of flatbread, the schoolboy runs after the bus — three ordinary lives continuing, seen from the passing car.
Camera: steady mount on the slowly moving car.
```

### [SCENE S115a] · 3 сек
```
[SCENE S115a]
Base frame: storyboard panel S115a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the car slows to the kerb, the window comes down, he leans slightly out with his hand to his chest and greets the old man, then waits without hurry.
Camera: static.
```

### [SCENE S116a] · 2 сек
```
[SCENE S116a]
Base frame: storyboard panel S116a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the old man looks up in mild surprise, lifts one hand from his broom to his chest and answers with a small warm nod.
Camera: static.
```

### [SCENE S117a] · 2 сек
```
[SCENE S117a]
Base frame: storyboard panel S117a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the hand draws the seatbelt across and clicks it home, then withdraws, the ring visible on the finger as it moves away.
Camera: static.
```

### [SCENE S118a] · 4 сек
```
[SCENE S118a]
Base frame: storyboard panel S118a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the monument passes across frame with the parallax of the moving car, the sun flaring behind the raised pointing arm.
Camera: static frame carried by the moving car.
```

### [SCENE S119a] · 3 сек
```
[SCENE S119a]
Base frame: storyboard panel S119a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: a slow quiet smile spreads across his face as he keeps looking up, sunlight crossing his face in bars.
Camera: static.
```

### [SCENE S120a] · 3 сек
```
[SCENE S120a]
Base frame: storyboard panel S120a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the reminder lights the screen, a ringed hand picks the phone up, dismisses it, and sets it face down on the seat.
Camera: static.
```

### [SCENE S121a] · 5 сек ★
```
[SCENE S121a]
Base frame: storyboard panel S121a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the camera rises continuously from just above the avenue until the entire circular park is revealed as a wheel, radial avenues converging on the monument at its centre, the city stretching away beyond.
Camera: continuous steady drone ascent across the full duration.
```

### [SCENE S122a] · 4 сек
```
[SCENE S122a]
Base frame: storyboard panel S122a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the puddle shrinks steadily as dry asphalt spreads in from the edges, the reflection breaking up until only a thin damp stain is left.
Camera: static, gently accelerated time.
```

### [SCENE S123a] · 5 сек ★ ПОСЛЕДНЕЕ, ЧТО ВИДИТ ЗРИТЕЛЬ
```
[SCENE S123a]
Base frame: storyboard panel S123a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: low morning sunlight travels slowly across the engraved band until the worn calligraphy catches the light and becomes clearly legible.
Camera: static.
```

### [SCENE S124a] · 10 сек
```
[SCENE S124a]
Base frame: storyboard panel S124a. Keep its framing, angle, composition, objects, lighting, colour and wardrobe exactly as they are.
Motion: the lit engraving holds steady and the image darkens slightly overall. Title text is overlaid in post, NOT generated.
Camera: static.
```

---

# СВОДКА

- **124 сцены**, каждая с меткой `[SCENE ID]` и привязкой к панели
- **Самые длинные:** S97a (8 сек, один план без склеек), S92a (8 сек),
  S29a (6 сек), S51a (6 сек), S121a (5 сек), S123a (5 сек)
- **Единственное разрешённое отклонение от панели:** S105a — обесцвечивание
  мира при сохранении цвета перстня. Прописано в промпте явно
- **Пакет-манифест:** см. `MANIFEST.md`

## ГДЕ ОЖИДАТЬ ПРОБЛЕМ
- **S97a** — восьмисекундная непрерывная походка с хромотой. Если модель
  не тянет 8 сек, генерировать 2×4 сек с одной статичной рамкой и клеить
  встык так, чтобы склейка не читалась
- **S24a** — морф материала без склейки
- **S105a** — избирательное обесцвечивание. Запасной путь: две версии кадра
  и маска на перстень в посте
- **S104a** — растворение всадников. Тоже может потребовать пост
