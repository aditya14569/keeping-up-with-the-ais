#!/usr/bin/env python3
"""Build a newsletter issue PDF from Markdown.

Usage: python3 scripts/build_pdf.py issues/2026-09-30-issue-001.md
Writes the PDF next to the Markdown file (same name, .pdf).

Needs: pip install markdown playwright && playwright install chromium
"""
import re
import sys
from datetime import date
from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

NAME = "Keeping up with the AIs"

CSS = r"""
@page { size: A4; margin: 16mm 17mm 18mm 17mm; }
:root { --ink:#16181d; --muted:#5b6170; --line:#e3e5ea; --accent:#5b3df5; --accent-soft:#f1eefe;
        --dev:#0f766e; --dev-soft:#ecf8f6; --warm:#fff7e8; --warm-line:#f3d9a4; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Carlito", "DejaVu Sans", sans-serif; color: var(--ink); font-size: 11pt; line-height: 1.5; margin: 0; }
.mast { border-bottom: 3px solid var(--ink); padding-bottom: 8px; margin-bottom: 14px; }
.mast .kicker { font-size: 8.5pt; letter-spacing: .14em; text-transform: uppercase; color: var(--accent); font-weight: 700; }
.mast .name { font-family: "Bitstream Charter", "DejaVu Serif", serif; font-size: 27pt; font-weight: 700; line-height: 1.05; margin: 2px 0 6px; letter-spacing: -.01em; }
.mast .meta { display: flex; justify-content: space-between; font-size: 9pt; color: var(--muted); }
.mast .headline { font-family: "Bitstream Charter", "DejaVu Serif", serif; font-style: italic; font-size: 13pt; margin-top: 6px; }
h1 { font-family: "Bitstream Charter", "DejaVu Serif", serif; font-size: 17pt; margin: 22px 0 6px; padding: 5px 10px; background: var(--ink); color: #fff; border-radius: 3px; break-after: avoid; }
h2 { font-family: "Bitstream Charter", "DejaVu Serif", serif; font-size: 14pt; margin: 16px 0 4px; line-height: 1.25; break-after: avoid; }
h3 { font-size: 11.5pt; text-transform: uppercase; letter-spacing: .06em; color: var(--accent); margin: 14px 0 3px; break-after: avoid; }
p { margin: 5px 0 7px; }
ul, ol { margin: 4px 0 8px; padding-left: 20px; }
li { margin: 2px 0; }
a { color: var(--accent); text-decoration: none; }
a.src { font-size: 8.5pt; color: var(--muted); }
strong { color: #000; }
table { width: 100%; border-collapse: collapse; margin: 6px 0 10px; font-size: 10pt; break-inside: avoid; }
th { text-align: left; background: var(--accent-soft); padding: 5px 7px; border-bottom: 2px solid var(--accent); }
td { padding: 5px 7px; border-bottom: 1px solid var(--line); vertical-align: top; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.6pt; }
pre { background: #0f1117; color: #e6e6e6; padding: 9px 11px; border-radius: 5px; overflow: hidden; white-space: pre-wrap; margin: 6px 0; break-inside: avoid; }
pre code { font-size: 8.4pt; line-height: 1.45; }
.tldr { background: var(--warm); border: 1px solid var(--warm-line); border-radius: 6px; padding: 8px 14px 6px; margin: 4px 0 8px; break-inside: avoid; }
.tldr ol { margin-top: 2px; }
.box { border-radius: 6px; padding: 8px 13px 5px; margin: 9px 0 11px; }
.box.devs { background: var(--dev-soft); border-left: 4px solid var(--dev); }
.box.devs > p:first-child strong { color: var(--dev); }
.footer { margin-top: 18px; padding-top: 8px; border-top: 1px solid var(--line); font-size: 8.8pt; color: var(--muted); }
"""


def parse(md_text: str):
    meta = {}
    m = re.match(r"^---\n(.*?)\n---\n", md_text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        md_text = md_text[m.end():]
    return meta, md_text


def build(md_path: Path) -> Path:
    meta, body_md = parse(md_path.read_text(encoding="utf-8"))
    words = len(re.sub(r"\(https?://[^)]+\)", "", body_md).split())
    minutes = max(1, round(words / 220))
    d = date.fromisoformat(meta.get("date", date.today().isoformat()))
    body = markdown.markdown(body_md, extensions=["tables", "fenced_code", "md_in_html", "sane_lists"])
    body = re.sub(r'<a href="([^"]+)">\(', r'<a class="src" href="\1">(', body)  # source citations
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="mast">
  <div class="kicker">Daily AI briefing · Learn one thing + What moved</div>
  <div class="name">{NAME}</div>
  <div class="meta"><span>Issue #{meta.get('issue','?')} · {d.strftime('%A, %d %B %Y')}</span><span>~{minutes} min read</span></div>
  <div class="headline">{meta.get('title','')}</div>
</div>
{body}
</body></html>"""
    out = md_path.with_suffix(".pdf")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html, wait_until="load")
        page.pdf(path=str(out), format="A4", print_background=True, display_header_footer=True,
                 header_template="<span></span>",
                 footer_template=f'<div style="font-size:7.5pt;color:#8a8f9c;width:100%;text-align:center;font-family:sans-serif">'
                                 f'{NAME} · Issue #{meta.get("issue","?")} · page <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
                 margin={"top": "15mm", "bottom": "17mm", "left": "16mm", "right": "16mm"})
        browser.close()
    print(f"Built {out} ({words} words, ~{minutes} min)")
    return out


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        build(Path(arg))
