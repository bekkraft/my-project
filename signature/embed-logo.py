#!/usr/bin/env python3
"""Вшить свой файл логотипа в signature.html.

Использование:  python3 embed-logo.py путь/к/logo.png [ширина_в_подписи]
По умолчанию ширина — 160 px.
"""
import base64, mimetypes, pathlib, re, sys

if len(sys.argv) < 2:
    sys.exit(__doc__)

src = pathlib.Path(sys.argv[1])
width = sys.argv[2] if len(sys.argv) > 2 else "160"
mime = mimetypes.guess_type(src.name)[0] or "image/png"
b64 = base64.b64encode(src.read_bytes()).decode()

sig = pathlib.Path(__file__).with_name("signature.html")
html = sig.read_text(encoding="utf-8")
html, n = re.subn(
    r'<img src="[^"]*" alt="[^"]*" width="\d+" style="[^"]*"',
    f'<img src="data:{mime};base64,{b64}" alt="Алмалыкский горно-металлургический комбинат" '
    f'width="{width}" style="display:block; width:{width}px; height:auto; border:0;"',
    html, count=1)
if not n:
    sys.exit("Не найден тег <img> в signature.html")
sig.write_text(html, encoding="utf-8")
print(f"Готово: {src.name} вшит в signature.html (ширина {width} px)")
