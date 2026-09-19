# -*- coding: utf-8 -*-
import io, markdown

src = io.open('shahruhiya/SCENARIY.md', encoding='utf-8').read()
body = markdown.markdown(src, extensions=['tables', 'sane_lists', 'nl2br'])

css = """
@page { size: A4; margin: 2cm 2.2cm; }
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 11.5pt; line-height: 1.45; color: #111; }
h1 { font-size: 22pt; text-align: center; letter-spacing: 2px; margin: 24pt 0 6pt; page-break-before: always; }
h1:first-of-type { page-break-before: avoid; }
h2 { font-size: 12.5pt; text-transform: uppercase; letter-spacing: 1px; margin: 22pt 0 6pt; border-bottom: 1px solid #999; padding-bottom: 3pt; page-break-after: avoid; }
h3 { font-size: 11.5pt; margin: 16pt 0 4pt; page-break-after: avoid; }
p { margin: 5pt 0; text-align: left; }
blockquote { margin: 6pt 0 6pt 3.2cm; padding: 0; border: none; font-family: "DejaVu Sans Mono", "Courier New", monospace; font-size: 11pt; }
blockquote strong { display: block; margin-left: -1.2cm; letter-spacing: 1px; }
blockquote em { color: #555; font-size: 9.5pt; }
table { border-collapse: collapse; width: 100%; font-size: 8.5pt; margin: 8pt 0; }
th, td { border: 1px solid #bbb; padding: 3pt 4pt; vertical-align: top; text-align: left; }
th { background: #eee; }
hr { border: none; border-top: 1px solid #ccc; margin: 14pt 0; }
li { margin: 2pt 0; }
"""

html = u'<!DOCTYPE html>\n<html><head><meta charset="utf-8"><title>ШАҲРУҲИЯ — сценарий</title><style>%s</style></head><body>\n%s\n</body></html>' % (css, body)
io.open('shahruhiya/export/SHAHRUHIYA-scenariy.html', 'w', encoding='utf-8').write(html)
print('ok', len(html))

try:
    from weasyprint import HTML as _H
    _H(filename='shahruhiya/export/SHAHRUHIYA-scenariy.html').write_pdf(
        'shahruhiya/export/SHAHRUHIYA-scenariy.pdf')
    print('pdf ok')
except ImportError:
    print('weasyprint not installed — pip install weasyprint')
