# Экспорт сценария

`SCENARIY.md` — источник. Всё остальное собирается из него.

```bash
pip install markdown weasyprint python-docx
python3 shahruhiya/tools/export_html_pdf.py   # → export/…html и …pdf
python3 shahruhiya/tools/export_docx.py       # → export/…docx
```

Запускать из корня репозитория. Шрифты — DejaVu Serif / DejaVu Sans Mono
(полное покрытие узбекской кириллицы: ғ ҳ қ ў).

| файл | для чего |
|---|---|
| `export/SHAHRUHIYA-scenariy.pdf` | читать и печатать, 27 страниц |
| `export/SHAHRUHIYA-scenariy.docx` | править в Word / Google Docs |
| `export/SHAHRUHIYA-scenariy.html` | открыть в браузере, «Печать → Сохранить как PDF» |
