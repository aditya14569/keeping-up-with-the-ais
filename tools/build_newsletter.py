#!/usr/bin/env python3
"""Build an issue PDF for any newsletter folder that has a settings.yml
(java/, data/ ...). Separate from scripts/build_pdf.py, which stays dedicated
to "Keeping up with the AIs".

Usage: python3 tools/build_newsletter.py java/issues/2026-10-01-issue-001.md
Reads <folder>/settings.yml for the name, theme and reading-speed settings.

Visual blocks: fenced ```viz:<type> blocks containing YAML.
Types: stats, bars, timeline, loop, flow, versus, layers, codecompare, meter.
See tools/VISUALS.md.

Needs: pip install markdown pyyaml playwright && playwright install chromium
"""
import html as H
import math
import re
import sys
from datetime import date
from pathlib import Path

import markdown
import yaml
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
NAME = ""
KICKER = ""
WPM = 200
FONTS = (ROOT / "fonts").as_uri()

PALETTE = ["#5b3df5", "#ff6b4a", "#0f9d8a", "#f5a524", "#2f80ed", "#d63384"]  # replaced by theme at build time
SOFT = "#f1eefe"
SOFT_LINE = "#cfc6fd"
INK, MUTED, LINE = "#16181d", "#5b6170", "#e3e5ea"


def esc(s):
    return H.escape(str(s))


def inline_md(s):
    s = esc(s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a class="src" href="\2">\1</a>', s)
    return s


def wrap(text, width):
    words, lines, cur = str(text).split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines or [""]


def tspans(lines, x, y0, lh):
    return "".join(f'<tspan x="{x}" y="{y0 + i * lh:.1f}">{esc(l)}</tspan>' for i, l in enumerate(lines))


def figure(title, svg_or_html, note=None, kind="fig"):
    t = f'<div class="fig-title">{inline_md(title)}</div>' if title else ""
    n = f'<div class="fig-note">{inline_md(note)}</div>' if note else ""
    return f'<div class="{kind}">{t}{svg_or_html}{n}</div>'


ARROW_DEFS = f"""<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M0,0 L10,5 L0,10 z" fill="{MUTED}"/></marker></defs>"""


# ---------- components ----------

def viz_stats(d):
    cards = []
    for i, it in enumerate(d.get("items", [])):
        c = PALETTE[i % len(PALETTE)]
        cards.append(f'<div class="stat" style="--c:{c}"><div class="v">{esc(it["value"])}</div>'
                     f'<div class="l">{inline_md(it["label"])}</div></div>')
    return figure(d.get("title"), f'<div class="stats">{"".join(cards)}</div>', d.get("note"))


def viz_bars(d):
    bars = d["bars"]
    W, lab, row = 640, 190, 38
    area = W - lab - 110
    mx = max(float(b["value"]) for b in bars) or 1
    h = row * len(bars) + 8
    out = [f'<svg viewBox="0 0 {W} {h}" width="100%">']
    for i, b in enumerate(bars):
        y = 6 + i * row
        v = float(b["value"])
        bw = max(4, area * v / mx)
        c = PALETTE[0] if b.get("highlight") else "#b9bdc8"
        out.append(f'<text x="{lab - 12}" y="{y + 20}" text-anchor="end" class="svg-l">{esc(b["label"])}</text>')
        out.append(f'<rect x="{lab}" y="{y + 4}" width="{bw:.1f}" height="24" rx="5" fill="{c}"/>')
        out.append(f'<text x="{lab + bw + 8:.1f}" y="{y + 21}" class="svg-v" fill="{c if b.get("highlight") else MUTED}">'
                   f'{esc(b.get("display", b["value"]))}</text>')
    out.append("</svg>")
    return figure(d.get("title"), "".join(out), d.get("note"))


def viz_timeline(d):
    ev = d["events"]
    n = len(ev)
    W, Hh = 640, 190
    y = 95
    x0, x1 = 80, W - 80
    step = (x1 - x0) / max(1, n - 1)
    out = [f'<svg viewBox="0 0 {W} {Hh}" width="100%">',
           f'<line x1="{x0 - 20}" y1="{y}" x2="{x1 + 20}" y2="{y}" stroke="{LINE}" stroke-width="4" stroke-linecap="round"/>']
    for i, e in enumerate(ev):
        x = x0 + i * step
        hi = e.get("highlight")
        c = PALETTE[1] if hi else PALETTE[0]
        up = i % 2 == 0
        lines = wrap(e["label"], 18)[:3]
        out.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y - 26 if up else y + 26}" stroke="{c}" stroke-width="1.5"/>')
        out.append(f'<circle cx="{x}" cy="{y}" r="{9 if hi else 7}" fill="{c}" stroke="#fff" stroke-width="3"/>')
        if up:
            ty = y - 34 - 14 * (len(lines))
            out.append(f'<text x="{x}" y="{ty}" text-anchor="middle" class="svg-date" fill="{c}">{esc(e["date"])}</text>')
            out.append(f'<text text-anchor="middle" class="svg-s">{tspans(lines, x, ty + 15, 14)}</text>')
        else:
            ty = y + 44
            out.append(f'<text x="{x}" y="{ty}" text-anchor="middle" class="svg-date" fill="{c}">{esc(e["date"])}</text>')
            out.append(f'<text text-anchor="middle" class="svg-s">{tspans(lines, x, ty + 15, 14)}</text>')
    out.append("</svg>")
    return figure(d.get("title"), "".join(out), d.get("note"))


def viz_loop(d):
    steps = d["steps"]
    n = len(steps)
    W, Hh = 640, 300
    cx, cy, rx, ry = W / 2, Hh / 2, 215, 105
    bw, bh = 160, 52
    out = [f'<svg viewBox="0 0 {W} {Hh}" width="100%">', ARROW_DEFS]
    out.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{LINE}" stroke-width="3" stroke-dasharray="2 7" stroke-linecap="round"/>')
    pts = []
    for i in range(n):
        a = -math.pi / 2 + 2 * math.pi * i / n
        pts.append((cx + rx * math.cos(a), cy + ry * math.sin(a), a))
    # arrows along the ellipse between nodes (clockwise)
    for i in range(n):
        a0 = pts[i][2]
        a1 = a0 + 2 * math.pi / n
        am = (a0 + a1) / 2
        p0 = (cx + rx * math.cos(am - 0.18), cy + ry * math.sin(am - 0.18))
        p1 = (cx + rx * math.cos(am + 0.18), cy + ry * math.sin(am + 0.18))
        out.append(f'<path d="M{p0[0]:.1f},{p0[1]:.1f} A{rx},{ry} 0 0 1 {p1[0]:.1f},{p1[1]:.1f}" fill="none" stroke="{MUTED}" stroke-width="2.5" marker-end="url(#ah)"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="48" fill="{INK}"/>')
    cl = wrap(d.get("center", ""), 11)[:3]
    out.append(f'<text text-anchor="middle" class="svg-center">{tspans(cl, cx, cy + 5 - 8 * (len(cl) - 1), 16)}</text>')
    for i, (x, y, _) in enumerate(pts):
        s = steps[i]
        c = PALETTE[i % len(PALETTE)]
        out.append(f'<rect x="{x - bw / 2:.1f}" y="{y - bh / 2:.1f}" width="{bw}" height="{bh}" rx="12" fill="#fff" stroke="{c}" stroke-width="2.5"/>')
        out.append(f'<text x="{x:.1f}" y="{y - 3:.1f}" text-anchor="middle" class="svg-h" fill="{c}">{esc(s["label"])}</text>')
        if s.get("sub"):
            out.append(f'<text x="{x:.1f}" y="{y + 14:.1f}" text-anchor="middle" class="svg-s">{esc(s["sub"])}</text>')
    out.append("</svg>")
    return figure(d.get("title"), "".join(out), d.get("note"))


def viz_flow(d):
    cols = d["columns"]
    n = len(cols)
    W, gap = 640, 34
    cw = (W - gap * (n - 1)) / n
    bh, sp = 50, 10
    tallest = max(len(c) for c in cols)
    Hh = tallest * bh + (tallest - 1) * sp + 34
    out = [f'<svg viewBox="0 0 {W} {Hh}" width="100%">', ARROW_DEFS]
    heads = d.get("headers", [])
    for ci, col in enumerate(cols):
        x = ci * (cw + gap)
        if ci < len(heads) and heads[ci]:
            out.append(f'<text x="{x + cw / 2:.1f}" y="13" text-anchor="middle" class="svg-cap">{esc(heads[ci]).upper()}</text>')
        total = len(col) * bh + (len(col) - 1) * sp
        y0 = 24 + (Hh - 24 - total) / 2
        for bi, b in enumerate(col):
            b = b if isinstance(b, dict) else {"label": b}
            y = y0 + bi * (bh + sp)
            style = b.get("style", "")
            fill, stroke, tc = "#fff", "#c9ccd6", INK
            if style == "accent":
                fill, stroke, tc = PALETTE[0], PALETTE[0], "#fff"
            elif style == "warn":
                fill, stroke, tc = "#fff4e0", PALETTE[3], INK
            elif style == "soft":
                fill, stroke = SOFT, SOFT_LINE
            out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cw:.1f}" height="{bh}" rx="11" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
            has_sub = bool(b.get("sub"))
            fs = min(13, (cw - 14) / max(1, len(b["label"])) * 1.75)
            out.append(f'<text x="{x + cw / 2:.1f}" y="{y + (21 if has_sub else 30):.1f}" text-anchor="middle" class="svg-h" style="fill:{tc};font-size:{fs:.1f}px">{esc(b["label"])}</text>')
            if has_sub:
                out.append(f'<text x="{x + cw / 2:.1f}" y="{y + 38:.1f}" text-anchor="middle" class="svg-s" style="fill:{tc};opacity:.85">{esc(b["sub"])}</text>')
        if ci < n - 1:
            ym = 24 + (Hh - 24) / 2
            out.append(f'<line x1="{x + cw + 4:.1f}" y1="{ym:.1f}" x2="{x + cw + gap - 6:.1f}" y2="{ym:.1f}" stroke="{MUTED}" stroke-width="2.5" marker-end="url(#ah)"/>')
    out.append("</svg>")
    return figure(d.get("title"), "".join(out), d.get("note"))


def viz_versus(d):
    def card(side, c):
        lines = "".join(f"<li>{inline_md(l)}</li>" for l in side.get("points", []))
        ex = f'<div class="vs-ex">{inline_md(side["example"])}</div>' if side.get("example") else ""
        return (f'<div class="vs-card" style="--c:{c}"><div class="vs-h">{esc(side.get("emoji", ""))} {inline_md(side["title"])}</div>'
                f'<ul>{lines}</ul>{ex}</div>')
    body = f'<div class="vs">{card(d["left"], "#8a8f9c")}<div class="vs-mid">VS</div>{card(d["right"], PALETTE[0])}</div>'
    return figure(d.get("title"), body, d.get("note"))


def viz_meter(d):
    rows = []
    labels = {"impact": "🏗️ Day-to-day impact", "interview": "🎯 Interview value", "urgency": "⏰ Act-now urgency",
              "depth": "🧠 Depth", "prod": "🚨 Production risk", "everyone": "🙋 Everyone", "hype": "🔥 Hype level"}
    for k, v in d.items():
        if k in ("title", "note"):
            continue
        v = int(v)
        dots = "".join(f'<span class="dot{" on" if i < v else ""}"></span>' for i in range(5))
        rows.append(f'<span class="m-row"><span class="m-l">{esc(labels.get(k, k))}</span>{dots}</span>')
    return f'<div class="meter"><span class="m-t">{esc(d.get("title", "Why it matters to you"))}</span>{"".join(rows)}</div>'


def viz_layers(d):
    """Stacked layers, top to bottom (e.g. app -> JVM -> OS, or query -> buffer pool -> disk pages)."""
    rows = d["layers"]
    W, lh, gap = 640, 46, 8
    Hh = len(rows) * (lh + gap) + 4
    out = [f'<svg viewBox="0 0 {W} {Hh}" width="100%">']
    for i, r in enumerate(rows):
        r = r if isinstance(r, dict) else {"label": r}
        y = 2 + i * (lh + gap)
        inset = i * float(d.get("taper", 0))
        x, w = inset, W - 2 * inset
        hi = r.get("highlight")
        c = PALETTE[0] if hi else PALETTE[(i % (len(PALETTE) - 1)) + 1]
        fill = c if hi else mix(c, 0.12)
        tc = "#fff" if hi else INK
        out.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{lh}" rx="10" fill="{fill}" stroke="{c}" stroke-width="2"/>')
        out.append(f'<text x="{x + 16:.1f}" y="{y + 28}" class="svg-h" style="fill:{tc}">{esc(r["label"])}</text>')
        if r.get("sub"):
            out.append(f'<text x="{x + w - 16:.1f}" y="{y + 28}" text-anchor="end" class="svg-s" style="fill:{tc};opacity:.9">{esc(r["sub"])}</text>')
    out.append("</svg>")
    return figure(d.get("title"), "".join(out), d.get("note"))


def viz_codecompare(d):
    """Two code panes side by side: old way vs modern way."""
    def pane(side, cls):
        cap = f'<div class="cc-h">{inline_md(side.get("title", ""))}</div>'
        code = f'<pre class="cc-code"><code>{esc(side["code"].rstrip())}</code></pre>'
        return f'<div class="cc-pane {cls}">{cap}{code}</div>'
    body = f'<div class="cc">{pane(d["left"], "old")}{pane(d["right"], "new")}</div>'
    return figure(d.get("title"), body, d.get("note"))


VIZ = {"stats": viz_stats, "bars": viz_bars, "timeline": viz_timeline, "loop": viz_loop,
       "flow": viz_flow, "versus": viz_versus, "meter": viz_meter, "layers": viz_layers,
       "codecompare": viz_codecompare}


def mix(hex_color, amount):
    """Blend a colour with white (amount = share of the colour)."""
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    r, g, b = (round(255 - (255 - c) * amount) for c in (r, g, b))
    return f"#{r:02x}{g:02x}{b:02x}"


CSS = r"""
@font-face { font-family: "Poppins"; font-weight: 400; src: url("FONTS/Poppins-Regular.ttf"); }
@font-face { font-family: "Poppins"; font-weight: 500; src: url("FONTS/Poppins-Medium.ttf"); }
@font-face { font-family: "Poppins"; font-weight: 700; src: url("FONTS/Poppins-Bold.ttf"); }
@font-face { font-family: "Body"; font-weight: 400; src: url("FONTS/Carlito-Regular.ttf"); }
@font-face { font-family: "Body"; font-weight: 700; src: url("FONTS/Carlito-Bold.ttf"); }
@font-face { font-family: "Body"; font-style: italic; src: url("FONTS/Carlito-Italic.ttf"); }
@font-face { font-family: "Body"; font-weight: 700; font-style: italic; src: url("FONTS/Carlito-BoldItalic.ttf"); }
@font-face { font-family: "Mono"; src: url("FONTS/DejaVuSansMono.ttf"); }
:root { --ink:#16181d; --muted:#5b6170; --line:#e3e5ea; --v:THEME_ACCENT; --coral:THEME_ACCENT2; --vsoft:THEME_SOFT; --teal:#0f9d8a; --amber:#f5a524; --blue:#2f80ed; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Body", "Noto Color Emoji", sans-serif; color: var(--ink); font-size: 11.6pt; line-height: 1.55; margin: 0; }
b, strong { color: #000; }
a { color: var(--v); text-decoration: none; font-weight: 700; }
a.src { font-size: 8.3pt; color: #9aa0ad; font-weight: 400; }

/* masthead */
.mast { background: THEME_GRADIENT; color: #fff; border-radius: 16px; padding: 18px 22px 16px; position: relative; overflow: hidden; }
.mast:after { content: ""; position: absolute; right: -40px; top: -60px; width: 220px; height: 220px; border-radius: 50%; background: rgba(255,255,255,.08); }
.mast .kicker { font-family: Poppins; font-size: 8pt; letter-spacing: .18em; text-transform: uppercase; opacity: .85; font-weight: 500; }
.mast .name { font-family: Poppins; font-weight: 700; font-size: 30pt; line-height: 1.05; margin: 4px 0 8px; letter-spacing: -.02em; }
.mast .headline { font-family: Poppins; font-weight: 500; font-size: 13.5pt; line-height: 1.3; max-width: 88%; }
.mast .meta { display: flex; gap: 8px; margin-top: 12px; font-family: Poppins; font-size: 8.5pt; }
.mast .meta span { background: rgba(255,255,255,.16); padding: 3px 10px; border-radius: 99px; }

/* tldr */
.tldr { margin: 14px 0 6px; background: #fff8ec; border: 1.5px solid #f7d9a0; border-radius: 14px; padding: 10px 16px 6px; break-inside: avoid; }
.tldr > p:first-child { font-family: Poppins; font-weight: 700; font-size: 10.5pt; margin: 0 0 4px; }
.tldr ol { margin: 0 0 4px; padding-left: 20px; }
.tldr li { margin: 3px 0; }

/* headings */
h1 { font-family: Poppins; font-weight: 700; font-size: 20pt; margin: 24px 0 6px; line-height: 1.1; break-after: avoid; letter-spacing: -.01em; }
h1 .pill { display: inline-block; font-size: 8.5pt; letter-spacing: .14em; vertical-align: middle; background: var(--v); color: #fff; border-radius: 99px; padding: 3px 11px; margin-right: 8px; position: relative; top: -3px; }
h1.part2 .pill { background: var(--coral); }
h1.part2, h1.part3 { break-before: page; margin-top: 0; }
h1.part3 .pill { background: var(--ink); }
h1 + p.lede { color: var(--muted); margin-top: 0; }
h2 { font-family: Poppins; font-weight: 700; font-size: 15pt; margin: 20px 0 6px; line-height: 1.25; break-after: avoid; padding-left: 12px; border-left: 5px solid var(--v); }
h3 { font-family: Poppins; font-weight: 500; font-size: 10.5pt; text-transform: uppercase; letter-spacing: .08em; color: var(--v); margin: 16px 0 3px; break-after: avoid; }
p { margin: 5px 0 8px; }
ul, ol { margin: 4px 0 9px; padding-left: 20px; }
li { margin: 3px 0; }

/* labels inside story text */
.tag { display: inline-block; font-family: Poppins; font-weight: 700; font-size: 7.3pt; letter-spacing: .1em; padding: 2px 8px; border-radius: 99px; vertical-align: middle; position: relative; top: -2px; margin-right: 4px; }
.tag.hot { background: #ffe4dd; color: #c2410c; } .tag.try { background: #dcf5ef; color: #0f766e; }
.tag.dev { background: #e5efff; color: #1d4ed8; } .tag.watch { background: #fff1d6; color: #a16207; } .tag.learn { background: var(--vsoft); color: var(--v); }

/* figures */
.fig { margin: 12px 0 14px; padding: 12px 14px 8px; border: 1px solid var(--line); border-radius: 14px; background: #fcfcfe; break-inside: avoid; }
.fig-title { font-family: Poppins; font-weight: 700; font-size: 10pt; margin-bottom: 6px; }
.fig-note { font-size: 8.5pt; color: var(--muted); margin-top: 4px; }
svg text { font-family: Poppins, sans-serif; }
.svg-l { font-family: Body, sans-serif; font-size: 13px; fill: var(--ink); font-weight: 700; }
.svg-v { font-size: 13px; font-weight: 700; }
.svg-h { font-size: 13px; font-weight: 700; }
.svg-s { font-family: Body, sans-serif; font-size: 11.5px; fill: var(--muted); }
.svg-date { font-size: 11.5px; font-weight: 700; }
.svg-cap { font-size: 9.5px; letter-spacing: .12em; fill: #9aa0ad; font-weight: 500; }
.svg-center { font-size: 13px; font-weight: 700; fill: #fff; }

.stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(0, 1fr)); gap: 10px; }
.stat { border-radius: 12px; padding: 10px 12px; background: color-mix(in srgb, var(--c) 10%, white); border-top: 4px solid var(--c); }
.stat .v { font-family: Poppins; font-weight: 700; font-size: 19pt; color: var(--c); line-height: 1.1; }
.stat .l { font-size: 9.5pt; color: var(--ink); line-height: 1.3; margin-top: 3px; }

.vs { display: flex; gap: 10px; align-items: stretch; }
.vs-card { flex: 1; border-radius: 12px; padding: 10px 12px; border: 2px solid var(--c); background: #fff; }
.vs-h { font-family: Poppins; font-weight: 700; font-size: 10.5pt; color: var(--c); margin-bottom: 3px; }
.vs-card ul { margin: 0; padding-left: 16px; font-size: 10pt; }
.vs-ex { margin-top: 6px; font-family: Mono; font-size: 8pt; background: #f3f4f7; border-radius: 7px; padding: 6px 8px; white-space: pre-wrap; }
.vs-mid { align-self: center; font-family: Poppins; font-weight: 700; font-size: 9pt; color: #fff; background: var(--ink); border-radius: 99px; padding: 6px 7px; }

.meter { display: flex; flex-wrap: wrap; align-items: center; gap: 6px 16px; margin: 8px 0 10px; padding: 7px 12px; border-radius: 99px; background: #f4f5f8; font-size: 9.5pt; break-inside: avoid; }
.m-t { font-family: Poppins; font-weight: 700; font-size: 8pt; letter-spacing: .1em; text-transform: uppercase; color: var(--muted); }
.m-row { display: inline-flex; align-items: center; gap: 3px; }
.m-l { margin-right: 5px; font-weight: 700; }
.dot { width: 9px; height: 9px; border-radius: 50%; background: #d6d9e0; display: inline-block; }
.dot.on { background: var(--coral); }

/* boxes */
.box { border-radius: 12px; padding: 9px 14px 6px; margin: 10px 0 12px; }
.box > p:first-child { margin-top: 0; }
.box.devs { background: #eef4ff; border-left: 5px solid var(--blue); }
.box.devs > p:first-child strong:first-child { color: #1d4ed8; }
.box.jargon { background: var(--vsoft); border: 1.5px dashed var(--v); break-inside: avoid; }
.box.jargon > p:first-child strong:first-child { color: var(--v); }
.box.tryit { background: #e9f8f4; border-left: 5px solid var(--teal); break-inside: avoid; }
.box.tryit > p:first-child strong:first-child { color: #0f766e; }
.box.care { background: #fff6f3; border-left: 5px solid var(--coral); break-inside: avoid; }

table { width: 100%; border-collapse: separate; border-spacing: 0; margin: 8px 0 12px; font-size: 10pt; break-inside: auto; border: 1px solid var(--line); border-radius: 12px; }
th { text-align: left; background: var(--ink); color: #fff; padding: 6px 9px; font-family: Poppins; font-weight: 500; font-size: 9pt; }
td { padding: 6px 9px; border-top: 1px solid var(--line); vertical-align: top; }
tr:nth-child(even) td { background: #f8f8fb; }
tr { break-inside: avoid; }
code { font-family: Mono; font-size: 8.6pt; background: #f1f2f5; padding: 1px 4px; border-radius: 4px; }
pre { background: #12131a; color: #e6e6e6; padding: 10px 12px; border-radius: 10px; white-space: pre-wrap; margin: 6px 0 8px; break-inside: avoid; }
pre code { font-size: 8.2pt; line-height: 1.32; background: none; padding: 0; color: inherit; }

/* quick hit cards */
.cards ul { list-style: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 9px; }
.cards li { border: 1px solid var(--line); border-radius: 12px; padding: 9px 12px; margin: 0; font-size: 10.2pt; line-height: 1.45; break-inside: avoid; background: #fff; }
.cards li strong:first-child { display: block; font-family: Poppins; font-size: 10pt; line-height: 1.3; margin-bottom: 3px; }

/* revision card: replaces the quiz in these newsletters */
.box.revision { background: #16181d; color: #eceef3; border-radius: 14px; padding: 12px 16px 8px; break-inside: avoid; margin-top: 16px; }
.box.revision b, .box.revision strong { color: #fff; }
.box.revision > p:first-child strong:first-child { font-family: Poppins; font-size: 12pt; color: #fff; }
.box.revision ul { columns: 2; column-gap: 22px; padding-left: 16px; }
.box.revision li { break-inside: avoid; font-size: 10pt; }
.box.revision code { background: rgba(255,255,255,.12); color: #fff; }
.box.realworld { background: #fffaf0; border-left: 5px solid var(--amber); break-inside: avoid; }
.box.realworld > p:first-child strong:first-child { color: #a16207; }
.box.gotcha { background: #fff1f1; border-left: 5px solid #e5484d; break-inside: avoid; }
.box.gotcha > p:first-child strong:first-child { color: #b42318; }
.cc { display: flex; gap: 10px; }
.cc-pane { flex: 1; min-width: 0; }
.cc-h { font-family: Poppins; font-weight: 700; font-size: 9pt; margin-bottom: 4px; }
.cc-pane.old .cc-h { color: #8a8f9c; } .cc-pane.new .cc-h { color: var(--v); }
.cc-code { margin: 0; height: calc(100% - 22px); }
.cc-code code { font-size: 7.8pt; line-height: 1.28; }
.cc-pane.old .cc-code { background: #2a2c35; }
.cc-pane.new .cc-code { box-shadow: inset 4px 0 0 var(--v); }
.keep { break-inside: avoid; }
/* learning-format additions */
.dt { font-weight: 700; color: var(--v); border-bottom: 1.5px dotted var(--v); }
.dd { font-size: 9.6pt; color: #4b5161; font-style: italic; background: var(--vsoft); border-radius: 5px; padding: 0 5px; margin-left: 4px; }
.dd:before { content: "≈ "; font-style: normal; color: var(--v); font-weight: 700; }
.box.glossary { background: #fbfaf7; border: 1px solid var(--line); border-top: 4px solid var(--v); break-inside: avoid; }
.box.glossary > p:first-child strong:first-child { color: var(--v); font-family: Poppins; }
.box.glossary ul { list-style: none; padding: 0; columns: 2; column-gap: 20px; font-size: 9.6pt; }
.box.glossary li { break-inside: avoid; margin: 0 0 5px; }
.box.aside { background: #f7f7fa; border-left: 4px solid #9aa0ad; font-size: 10.6pt; break-inside: avoid; }
.box.aside > p:first-child strong:first-child { color: #3b4050; }
.box.casefile { background: #16181d; color: #e9eaee; border-radius: 12px; padding: 12px 16px 8px; break-inside: avoid; font-family: Mono; font-size: 9pt; line-height: 1.5; }
.box.casefile b, .box.casefile strong { color: #fff; }
.box.casefile > p:first-child strong:first-child { color: #fbbf24; font-family: Poppins; font-size: 10pt; letter-spacing: .08em; }
.box.casefile code { background: rgba(255,255,255,.1); color: #fff; }
.box.steps { background: #fff; border: 1px solid var(--line); border-left: 5px solid var(--v); break-inside: avoid; }
.box.recap { background: var(--vsoft); border-radius: 12px; break-inside: avoid; }
.box.recap > p:first-child strong:first-child { color: var(--v); font-family: Poppins; }
.box.brief { background: #f4f5f8; border-radius: 12px; font-size: 10pt; break-inside: avoid; }
.box.brief > p:first-child strong:first-child { font-family: Poppins; }
p.opener { font-size: 12.4pt; line-height: 1.6; color: #22252c; }
p.opener:first-letter { font-family: Poppins; font-weight: 700; font-size: 34pt; float: left; line-height: .9; margin: 4px 8px 0 0; color: var(--v); }
.byline { font-family: Poppins; font-size: 8.5pt; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); margin: -2px 0 10px; }
.footnote { font-size: 8.4pt; color: var(--muted); margin-top: 18px; border-top: 1px solid var(--line); padding-top: 6px; }
.footnote ol { padding-left: 18px; } .footnote li { margin: 1px 0; } .footnote hr { display: none; }
.footnote a.footnote-backref { display: none; }
sup a.footnote-ref, a.footnote-ref { font-size: 7.5pt; color: var(--v); font-weight: 700; }
.footer { margin-top: 18px; padding: 10px 14px; border-radius: 12px; background: #f4f5f8; font-size: 8.8pt; color: var(--muted); }
"""


def parse(md_text):
    meta = {}
    m = re.match(r"^---\n(.*?)\n---\n", md_text, re.S)
    if m:
        meta = yaml.safe_load(m.group(1)) or {}
        md_text = md_text[m.end():]
    return meta, md_text


def render_body(body_md):
    blocks = []

    def stash(m):
        kind, src = m.group(1), m.group(2)
        try:
            blocks.append(VIZ[kind](yaml.safe_load(src)))
        except Exception as e:  # show the problem in the PDF rather than failing silently
            blocks.append(f'<pre>viz:{esc(kind)} error: {esc(e)}</pre>')
        return f"\n\nKVIZ{len(blocks) - 1}KVIZ\n\n"

    body_md = re.sub(r"```viz:(\w+)\n(.*?)```", stash, body_md, flags=re.S)
    # Inline definitions: {{term|plain-English definition}} -> term + a small definition right after it
    body_md = re.sub(r"\{\{([^|{}]+)\|([^{}]+)\}\}",
                     r'<span class="dt">\1</span><span class="dd">\2</span>', body_md)
    html = markdown.markdown(body_md, extensions=["tables", "fenced_code", "md_in_html", "sane_lists", "footnotes"])
    html = re.sub(r'<a href="([^"]+)">\(', r'<a class="src" href="\1">(', html)
    for i, b in enumerate(blocks):
        html = html.replace(f"<p>KVIZ{i}KVIZ</p>", b).replace(f"KVIZ{i}KVIZ", b)
    # Keep a heading together with its tag line and first paragraph (no orphaned headings at page bottoms).
    html = re.sub(r'(<h([23])[^>]*>(?:(?!</h[23]>).)*</h\2>\s*(?:<p><span class="tag(?:(?!</p>).)*</p>\s*)?<p>(?:(?!</p>).)*</p>)',
                  r'<div class="keep">\1</div>', html, flags=re.S)
    # "# Part 1 · Learn" -> pill + title
    count = {"n": 0}

    def pill(m):
        count["n"] += 1
        label, title = m.group(1), m.group(2)
        if re.fullmatch(r"Part \d", label):
            label = label.upper()
        return f'<h1 class="part{count["n"]}"><span class="pill">{label.upper()}</span>{title}</h1>'
    html = re.sub(r"<h1>([^<·]{1,30}) · (.*?)</h1>", pill, html)
    return html


def find_settings(md_path: Path) -> dict:
    for folder in [md_path.parent, *md_path.parents]:
        f = folder / "settings.yml"
        if f.exists():
            return yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        if folder == ROOT:
            break
    raise SystemExit(f"No settings.yml found above {md_path}")


def apply_theme(cfg: dict) -> str:
    global NAME, KICKER, WPM, PALETTE, SOFT, SOFT_LINE
    t = cfg.get("theme", {})
    NAME = cfg["name"]
    KICKER = cfg.get("kicker", "Daily briefing · Learn + What's new")
    WPM = int(cfg.get("words_per_minute", 200))
    a1, a2 = t.get("accent", "#5b3df5"), t.get("accent2", "#ff6b4a")
    PALETTE = [a1, a2, "#0f9d8a", "#f5a524", "#2f80ed", "#d63384"]
    SOFT, SOFT_LINE = mix(a1, 0.1), mix(a1, 0.35)
    grad = t.get("gradient", [a1, a2])
    stops = ", ".join(f"{c} {round(i * 100 / max(1, len(grad) - 1))}%" for i, c in enumerate(grad))
    return (CSS.replace("THEME_ACCENT2", a2).replace("THEME_ACCENT", a1).replace("THEME_SOFT", SOFT)
               .replace("THEME_GRADIENT", f"linear-gradient(120deg, {stops})"))


def build(md_path: Path) -> Path:
    cfg = find_settings(md_path)
    css = apply_theme(cfg)
    meta, body_md = parse(md_path.read_text(encoding="utf-8"))
    # Count prose + code + the text inside visuals (labels, code panes, notes), minus URLs, tags and YAML keys.
    text = re.sub(r"\(https?://[^)]+\)|</?[a-zA-Z][^>]*>|```viz:\w+", " ", body_md)
    text = re.sub(r"^\s*-?\s*\w+:\s", " ", text, flags=re.M)
    words = len([w for w in text.split() if re.search(r"\w", w)])
    visuals = len(re.findall(r"```viz:", body_md))
    # Reading model: prose/code at WPM, plus ~20 seconds to take in each diagram or chart.
    minutes = max(1, round(words / WPM + visuals / 3))
    d = meta.get("date") or date.today()
    d = d if isinstance(d, date) else date.fromisoformat(str(d))
    body = render_body(body_md)
    issue = meta.get("issue", "?")
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{css.replace("FONTS", FONTS)}</style></head><body>
<div class="mast">
  <div class="kicker">{esc(meta.get("kicker", KICKER))}</div>
  <div class="name">{NAME}</div>
  <div class="headline">{esc(meta.get('title', ''))}</div>
  <div class="meta"><span>{("Issue #" + str(issue)) if str(issue).isdigit() else ("Sample " + str(issue))}</span><span>{d.strftime('%a, %d %b %Y')}</span><span>⏱️ ~{minutes} min read</span><span>Level {cfg.get("difficulty", 3)}/5</span></div>
</div>
{body}
</body></html>"""
    out = md_path.with_suffix(".pdf")
    tmp = md_path.with_suffix(".render.html")
    tmp.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(tmp.resolve().as_uri(), wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        page.pdf(path=str(out), format="A4", print_background=True, display_header_footer=True,
                 header_template="<span></span>",
                 footer_template=f'<div style="font-size:7.5pt;color:#9aa0ad;width:100%;text-align:center;font-family:sans-serif">'
                                 f'{NAME} · Issue #{issue} · <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
                 margin={"top": "13mm", "bottom": "15mm", "left": "14mm", "right": "14mm"})
        browser.close()
    tmp.unlink(missing_ok=True)
    target = cfg.get("read_time_minutes")
    if target:
        cap = int(target) + 5
        flag = "" if minutes <= cap else f"  !! OVER the {cap}-min cap, cut it down"
        print(f"Built {out} ({words} words + {visuals} visuals, ~{minutes} min; target {target}, cap {cap}){flag}")
    else:
        print(f"Built {out} ({words} words + {visuals} visuals, ~{minutes} min; no length cap)")
    return out


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        build(Path(arg))
