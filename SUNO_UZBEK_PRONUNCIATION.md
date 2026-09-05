# Инструкция для Suno: правильное произношение узбекских слов

Suno лучше понимает подсказки на английском. Вставляйте блок ниже в поле
**Style of Music** (или в начало текста песни в квадратных скобках).

## Короткая версия (вставить в Style)

```
Uzbek language vocals, sung in Uzbek (Latin script). Pronounce every word as
Uzbek, NOT English or Turkish. Letter guide: "o'" = deep "o" (like Russian ў/о),
"g'" = soft throaty "gh" (like French r), "q" = deep "k" from the throat,
"x" = "kh" (like German "ch" in Bach), never "ks", "j" = "dj" as in "jam",
"sh" = "sh", "ch" = "ch", "ng" = single nasal sound, "h" = light breathy "h",
"y" = "y" as in "yes", "e" = "e" as in "bed", "o" = "o" as in "bore" (not "ow"),
"u" = "oo" as in "moon", "i" = "ee" as in "see". Apostrophe ' after a vowel
= short pause / glottal stop (a'lo, san'at). Stress on the last syllable.
```

## Подробная таблица букв

| Буква (латиница) | Кириллица | Как объяснить Suno                          |
|------------------|-----------|---------------------------------------------|
| oʻ / o'          | ў         | deep "o", like "bore"; NOT "oh-apostrophe"  |
| gʻ / g'          | ғ         | throaty "gh", like French "r"               |
| q                | қ         | deep "k" from the throat                    |
| x                | х         | "kh" like German "Bach"; never "ks"         |
| h                | ҳ         | light breathy "h"                           |
| j                | ж / дж    | "dj" as in "jam"                            |
| sh               | ш         | "sh" as in "ship"                           |
| ch               | ч         | "ch" as in "chair"                          |
| ng               | нг        | one nasal sound as in "sing"                |
| y                | й         | "y" as in "yes"                             |
| o                | о         | "o" as in "bore", not "ow"                  |
| u                | у         | "oo" as in "moon"                           |
| i                | и         | "ee" as in "see"                            |
| e                | э         | "e" as in "bed"                             |
| a                | а         | open "a" as in "father"                     |
| ʼ (tutuq)        | ъ         | short pause / glottal stop                  |

## Практические советы

1. **Пишите текст на узбекской латинице** и укажите `[Uzbek]` в начале текста.
2. **Сложные слова разбивайте на слоги** через дефис: `Toshkent → Tosh-kent`,
   `o'zbek → o'z-bek`, `g'alaba → gha-la-ba`.
3. **Апостроф** Suno часто читает как английское сокращение. Если слово
   звучит неправильно, замените `o'` на `ō` или `o`, а `g'` на `gh`:
   `ko'z → kōz`, `bog' → bogh`.
4. **Буква x**: если Suno читает как «кс», пишите `kh`: `xalq → khalq`.
5. **Ударение** в узбекском почти всегда на последний слог — укажите это
   в Style: `stress on the last syllable`.
6. Добавьте в Style жанр и регион: `Uzbek pop`, `Central Asian folk`,
   `doira, rubab, tanbur` — это тоже улавливает акцент модели.

## Пример готового промпта

**Style:**
```
Uzbek pop ballad, male vocals, sung in Uzbek (Latin script), clear Uzbek
pronunciation: "o'"=deep o, "g'"=throaty gh, "q"=deep k, "x"=kh, "j"=dj,
"sh"=sh, "ch"=ch. Stress on last syllable. Doira and rubab, modern beat.
```

**Lyrics:**
```
[Uzbek]
[Verse]
Sen-siz ko'n-gil o'r-tan-a-di
Yul-duz-lar ham so'r-a-di
Qay-da-san, ey ja-nim me-ning
Qal-bim se-ni kut-a-di
```
