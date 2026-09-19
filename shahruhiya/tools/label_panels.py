#!/usr/bin/env python3
"""
ШАҲРУҲИЯ — разметка панелей сториборда.

Берёт ЧИСТЫЕ панели (S12a.png) и делает две вещи:

1. label  — дорисовывает полосу с ID под каждой панелью -> S12a_L.png
            Чистый оригинал НЕ трогается: он идёт в видео как start frame.
2. sheet  — собирает размеченные панели в контактные листы по N штук.

Номер рисуется ПРОГРАММНО, а не генератором: шрифт один и тот же,
положение одно и то же, прочитается всегда.

ИСПОЛЬЗОВАНИЕ
    python3 label_panels.py label ./panels
    python3 label_panels.py sheet ./panels/labeled --cols 4 --rows 3
    python3 label_panels.py all   ./panels

СТРУКТУРА ПОСЛЕ ЗАПУСКА
    panels/            S12a.png        чистые -> в видео
    panels/labeled/    S12a_L.png      с номером -> в сториборд
    panels/sheets/     sheet_01.png    контактные листы
"""

import argparse, os, re, sys
from PIL import Image, ImageDraw, ImageFont

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "C:/Windows/Fonts/arialbd.ttf",
]

BAR_RATIO   = 0.075   # высота полосы = 7.5% от высоты панели
BAR_COLOR   = (16, 16, 18)
TEXT_COLOR  = (255, 255, 255)
DIM_COLOR   = (150, 150, 155)


def load_font(size):
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                pass
    return ImageFont.load_default()


def panel_id(filename):
    """S12a.png -> S12a ; 12a.png -> S12a (доклеиваем префикс)"""
    stem = os.path.splitext(os.path.basename(filename))[0]
    stem = re.sub(r'_L$', '', stem)
    m = re.match(r'^S?(\d+)([a-z])$', stem, re.I)
    if not m:
        return None
    return f"S{m.group(1)}{m.group(2).lower()}"


def sort_key(pid):
    m = re.match(r'^S(\d+)([a-z])$', pid)
    return (int(m.group(1)), m.group(2)) if m else (9999, 'z')


def label_one(src, dst, pid, note=""):
    img = Image.open(src).convert("RGB")
    w, h = img.size
    bar = max(28, int(h * BAR_RATIO))

    out = Image.new("RGB", (w, h + bar), BAR_COLOR)
    out.paste(img, (0, 0))
    draw = ImageDraw.Draw(out)

    f_id = load_font(int(bar * 0.62))
    pad = int(bar * 0.3)
    ty = h + (bar - int(bar * 0.62)) // 2 - int(bar * 0.06)
    draw.text((pad, ty), pid, font=f_id, fill=TEXT_COLOR)

    if note:
        f_note = load_font(int(bar * 0.38))
        nx = pad + int(draw.textlength(pid, font=f_id)) + pad
        ny = h + (bar - int(bar * 0.38)) // 2 - int(bar * 0.04)
        draw.text((nx, ny), note, font=f_note, fill=DIM_COLOR)

    out.save(dst, quality=95)


def cmd_label(folder):
    outdir = os.path.join(folder, "labeled")
    os.makedirs(outdir, exist_ok=True)
    n = 0
    for name in sorted(os.listdir(folder)):
        if not name.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            continue
        pid = panel_id(name)
        if not pid:
            print(f"  пропуск (имя не похоже на ID): {name}")
            continue
        label_one(os.path.join(folder, name),
                  os.path.join(outdir, f"{pid}_L.png"), pid)
        n += 1
    print(f"размечено панелей: {n} -> {outdir}")
    return n


def cmd_sheet(folder, cols, rows, gap=14):
    files = [f for f in os.listdir(folder)
             if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))]
    items = sorted(((panel_id(f), f) for f in files if panel_id(f)),
                   key=lambda t: sort_key(t[0]))
    if not items:
        print("нет размеченных панелей"); return 0

    outdir = os.path.join(os.path.dirname(folder.rstrip("/")) or ".", "sheets")
    os.makedirs(outdir, exist_ok=True)

    per = cols * rows
    made = 0
    for i in range(0, len(items), per):
        chunk = items[i:i + per]
        thumbs = [Image.open(os.path.join(folder, f)).convert("RGB") for _, f in chunk]
        tw, th = thumbs[0].size
        sheet = Image.new("RGB",
                          (cols * tw + (cols + 1) * gap,
                           rows * th + (rows + 1) * gap), (28, 28, 30))
        for k, t in enumerate(thumbs):
            if t.size != (tw, th):
                t = t.resize((tw, th))
            r, c = divmod(k, cols)
            sheet.paste(t, (gap + c * (tw + gap), gap + r * (th + gap)))
        made += 1
        path = os.path.join(outdir, f"sheet_{made:02d}_{chunk[0][0]}-{chunk[-1][0]}.png")
        sheet.save(path, quality=92)
        print(f"  лист {made}: {chunk[0][0]}…{chunk[-1][0]} -> {path}")
    print(f"контактных листов: {made}")
    return made


def main():
    ap = argparse.ArgumentParser(description="Разметка панелей сториборда ID")
    ap.add_argument("cmd", choices=["label", "sheet", "all"])
    ap.add_argument("folder")
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--rows", type=int, default=3)
    a = ap.parse_args()

    if not os.path.isdir(a.folder):
        sys.exit(f"нет такой папки: {a.folder}")

    if a.cmd in ("label", "all"):
        cmd_label(a.folder)
    if a.cmd == "sheet":
        cmd_sheet(a.folder, a.cols, a.rows)
    if a.cmd == "all":
        cmd_sheet(os.path.join(a.folder, "labeled"), a.cols, a.rows)


if __name__ == "__main__":
    main()
