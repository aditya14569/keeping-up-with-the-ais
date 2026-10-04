#!/usr/bin/env python3
"""Email subject + HTML body for an issue of a settings-driven newsletter.

Usage (from the repo root): python3 tools/email_body.py java/issues/<file>.pdf
Writes email.html and prints `subject=...`, `name=...` and `key=...` lines for $GITHUB_OUTPUT.
Standard library only (runs on a bare GitHub runner).
"""
import html
import re
import sys
from datetime import date
from pathlib import Path

pdf = Path(sys.argv[1])
folder = pdf.parent.parent                      # java/issues/x.pdf -> java/
settings = (folder / "settings.yml").read_text(encoding="utf-8")


def setting(key, default=""):
    m = re.search(rf'^{key}:\s*"?(.*?)"?\s*(#.*)?$', settings, re.M)
    return m.group(1).strip() if m else default


name = setting("name", folder.name)
accent = setting("email_accent", "#5b3df5")
md = pdf.with_suffix(".md").read_text(encoding="utf-8")
meta = dict(re.findall(r"^(\w+):\s*(.+)$", md.split("---")[1], re.M)) if md.startswith("---") else {}
issue = meta.get("issue", "?").strip()
d = date.fromisoformat(meta.get("date", date.today().isoformat()).strip())
title = meta.get("title", "").strip().strip('"')

tldr = re.search(r'<div class="tldr"[^>]*>(.*?)</div>', md, re.S)
items = re.findall(r"^\d+\.\s+(.+)$", tldr.group(1), re.M) if tldr else []


def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


lis = "".join(f"<li style='margin:0 0 8px'>{inline(i)}</li>" for i in items)
mins = setting("read_time_minutes", "20")
body = f"""<div style="font-family:Segoe UI,Helvetica,Arial,sans-serif;max-width:600px;color:#16181d;line-height:1.5">
<p style="font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:{accent};font-weight:700;margin:0">{html.escape(name)} · Issue #{issue}</p>
<h2 style="font-family:Georgia,serif;margin:4px 0 12px">{html.escape(title)}</h2>
<p style="margin:0 0 6px"><b>Today:</b></p>
<ol style="padding-left:20px;margin:0 0 14px">{lis}</ol>
<p>The full issue, with both stories explained in depth and the rest of the news "on the radar", is attached as a PDF.</p>
<p style="color:#8a8f9c;font-size:12px">{d.strftime('%A, %d %B %Y')} · Researched and written by Claude.</p>
</div>"""
Path("email.html").write_text(body, encoding="utf-8")
print(f"subject={name} #{issue}: {title}")
print(f"name={name}")
print(f"key={folder.name}")
