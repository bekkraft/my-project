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

# Пересборка раскадровок

```bash
python3 shahruhiya/tools/build_sheets.py    # → RASKADROVKA/*.md + sheets.json
```

Источник — `STORYBOARD-01..05.md`. Скрипт разворачивает токены, режет
256 панелей на листы по 6 и пишет к каждому листу готовый блок для Flow.
Правишь промпт — правь в `STORYBOARD-*.md` и пересобирай, иначе правка
потеряется при следующей сборке.
