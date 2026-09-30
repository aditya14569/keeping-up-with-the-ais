#!/usr/bin/env python3
"""Make the email subject and HTML body for an issue PDF.

Reads the matching .md file, writes email.html, and prints
`subject=...` for $GITHUB_OUTPUT. Uses only the standard library.
"""
import html
import re
import sys
from datetime import date
from pathlib import Path

pdf = Path(sys.argv[1])
md = pdf.with_suffix(".md").read_text(encoding="utf-8")

meta = dict(re.findall(r"^(\w+):\s*(.+)$", md.split("---")[1], re.M)) if md.startswith("---") else {}
issue = meta.get("issue", "?")
d = date.fromisoformat(meta.get("date", date.today().isoformat()))
title = meta.get("title", "")

tldr = re.search(r'<div class="tldr"[^>]*>(.*?)</div>', md, re.S)
items = re.findall(r"^\d+\.\s+(.+)$", tldr.group(1), re.M) if tldr else []


def inline(s: str) -> str:
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    return s


lis = "".join(f"<li style='margin:0 0 8px'>{inline(i)}</li>" for i in items)
body = f"""<div style="font-family:Segoe UI,Helvetica,Arial,sans-serif;max-width:600px;color:#16181d;line-height:1.5">
<p style="font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#5b3df5;font-weight:700;margin:0">Keeping up with the AIs · Issue #{issue}</p>
<h2 style="font-family:Georgia,serif;margin:4px 0 12px">{html.escape(title)}</h2>
<p style="margin:0 0 6px"><b>If you only have one minute:</b></p>
<ol style="padding-left:20px;margin:0 0 14px">{lis}</ol>
<p>The full issue (Learn one thing + What moved) is attached as a PDF, about 10 minutes to read.</p>
<p style="color:#8a8f9c;font-size:12px">{d.strftime('%A, %d %B %Y')} · Written and researched by Claude.</p>
</div>"""
Path("email.html").write_text(body, encoding="utf-8")
print(f"subject=Keeping up with the AIs #{issue}: {title}")
