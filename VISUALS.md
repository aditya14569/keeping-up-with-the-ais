# Visual toolkit

`scripts/build_pdf.py` turns fenced ```` ```viz:<type> ```` blocks (YAML inside) into diagrams and charts. Issue #1 uses every one of them, so copy from it when in doubt.

## Blocks

**stats**: big-number cards (put one right after the TL;DR)
```yaml
title: Today in three numbers
items:
  - value: "13%"
    label: of Vercel's paid teams tried **Jev** in 24h
```

**loop**: a cycle diagram (processes that repeat: agent loops, training loops, RAG flow)
```yaml
title: …
center: Your goal
steps:
  - {label: "1 · Think", sub: decide the next step}
note: optional caption
```

**flow**: left-to-right architecture/process diagram. Columns hold 1–3 boxes each. Keep labels ≤ 16 characters.
```yaml
title: How X works
headers: [Input, Model, Output]
columns:
  - [{label: ChatGPT, sub: web · mobile}]
  - [{label: Your dot, sub: GPT-6 Astra, style: accent}]   # styles: accent | soft | warn
```

**bars**: horizontal bar chart. Use it only with sourced numbers. Mark derived numbers in `note`.
```yaml
title: …
bars:
  - {label: Standard, value: 9.3, display: "~9 sec"}
  - {label: Ultrafast, value: 0.67, display: "~0.7 sec", highlight: true}
note: Source + how any number was derived
```

**timeline**: 3–7 dated events, evenly spaced. Keep labels ≤ 40 characters.
```yaml
title: …
events:
  - {date: Sep 15, label: TypeSafe launches Jev, highlight: true}
```

**versus**: two-card comparison (old vs new, A vs B)
```yaml
left:  {emoji: 💬, title: Chat model, points: [...], example: "optional mono snippet"}
right: {emoji: 🎯, title: Decision model, points: [...], example: "..."}
note: say if the example is illustrative
```

**meter**: "Who should care" dots, 0–5. Keys: `everyone`, `vibe`, `dev`, `hype`.
```yaml
vibe: 4
dev: 3
```

**quiz**: three multiple-choice questions at the end. Answers print upside down.
```yaml
title: "Pop quiz: 30 seconds, no Googling"
questions:
  - {q: …, options: [A, B, C], answer: B, why: short reason}
```

## HTML boxes and tags (write them straight in Markdown)

- `<div class="box jargon" markdown="1">`: 📖 Jargon buster (3–4 terms)
- `<div class="box tryit" markdown="1">`: 🧪 Try it / 🎯 One thing to try today
- `<div class="box devs" markdown="1">`: 🛠️ For devs
- `<div class="box care" markdown="1">`: 👀 Should you care?
- `<div class="cards" markdown="1">` wrapping a bullet list: two-column quick-hit cards. Start each item with an emoji and a **bold title.**
- Tags under a story heading: `<span class="tag hot">BIG DEAL</span>`. Classes: `hot`, `try`, `dev`, `watch`, `learn`.

## Rules
- Every issue has **at least 5 visuals**: the stats strip, 1–2 in Learn, 2+ in What moved, a meter per top story, and the quiz.
- Visuals must **explain**, not decorate. A diagram shows how something works. A chart compares real numbers.
- Never invent data for a chart. If a number is derived or illustrative, the `note` says so.
- For anything the blocks can't draw, you may write a small inline `<svg>` (width 640, Poppins/Body fonts, the palette in build_pdf.py). Keep it simple.
- After building, **look at every page image** and fix clipped labels, overflowing boxes or awkward page breaks.
