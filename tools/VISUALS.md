# Visual & text toolkit: Java – Beautifully Broken & Storage Wars

`tools/build_newsletter.py` turns fenced ```` ```viz:<type> ```` blocks (with YAML inside) into diagrams and charts. Colours come from the folder's `settings.yml` theme, so never hard-code colours. Each folder's Issue #1 uses most of these blocks, so copy from it when in doubt.

## Blocks

**stats**: big-number cards. Good for "Version watch" (current LTS, latest JDK, latest Spring Boot) or "Today in numbers".
```yaml
title: Version watch
items:
  - {value: "25", label: current **LTS** JDK}
```

**codecompare**: two code panes side by side, **old way** (left, dimmed) vs **modern way** (right). Keep each pane ≤ 14 lines and ≤ 48 characters wide.
```yaml
title: "Data carrier: then vs now"
left:
  title: "Java 8: a POJO"
  code: |
    public final class Point { ... }
right:
  title: "Java 16+: a record"
  code: |
    record Point(int x, int y) {}
note: optional caption
```

**layers**: a stack drawn top to bottom (app → JVM → OS, query → buffer pool → pages → disk). `taper: 10` narrows each lower layer. `highlight: true` marks the focus layer. Keep labels ≤ 30 characters and `sub` ≤ 40.
```yaml
title: …
layers:
  - {label: Your SQL query, sub: "SELECT * FROM users WHERE id = 42"}
  - {label: Buffer pool, sub: hot pages cached in RAM, highlight: true}
```

**flow**: left-to-right architecture or process diagram, with 2–4 columns of 1–3 boxes each. Keep labels ≤ 16 characters. Styles: `accent`, `soft`, `warn`.
```yaml
title: How X works
headers: [Producer, Broker, Consumer]
columns:
  - [{label: Order service, sub: writes events}]
  - [{label: Kafka topic, sub: 6 partitions, style: accent}]
```

**loop**: a cycle (event loop, GC cycle, consumer poll loop, checkpointing).
```yaml
title: …
center: One poll()
steps:
  - {label: "1 · Fetch", sub: get a batch}
```

**bars**: horizontal bar chart, using **sourced numbers only**. If a number is derived or illustrative, the `note` says so.
```yaml
title: …
bars:
  - {label: Platform threads, value: 4000, display: "~4k"}
  - {label: Virtual threads, value: 1000000, display: "1M+", highlight: true}
note: Source + how the numbers were derived
```

**timeline**: 3–7 dated events (release history, the road from Java 8 to 25, Kafka's ZooKeeper removal). Keep labels ≤ 40 characters.
```yaml
title: …
events:
  - {date: "2014", label: "Java 8: lambdas & streams"}
  - {date: "2025", label: "Java 25 LTS", highlight: true}
```

**versus**: two-card conceptual comparison (B-tree vs LSM-tree, Redis vs Memcached). Use it for ideas. Use `codecompare` for code.
```yaml
left:  {emoji: 🌳, title: B-tree, points: [...], example: "optional mono snippet"}
right: {emoji: 🪵, title: LSM-tree, points: [...]}
```

**meter**: a 0–5 dot rating. Keys: `impact` (day-to-day impact), `interview` (interview value), `urgency` (act-now urgency), `depth`, `prod` (production risk). Optional `title`.
```yaml
impact: 4
interview: 5
urgency: 2
```

## Text components (write them straight in Markdown)

- **Inline definition:** `{{term|plain-English definition}}` renders the term highlighted with its definition right beside it. Use it on the **first** use of every technical term.
- **Footnotes for sources:** `fact.[^key]`, with `[^key]: [Title](url), publisher, date.` at the end of the file. They render as small superscript numbers and a sources list. Don't use inline `[(Source)](url)` links in the deep-dive format.
- **Opener paragraph** (with drop cap): `<p class="opener" markdown="1">…</p>`, the first paragraph of each story.
- **Byline** under a story heading: `<div class="byline">JDK 28 · OpenJDK · Announced 2 Oct · ~12 min read</div>`
- **Story headings:** `# Story 1 · Title` renders as a pill "STORY 1" and starts a new page for story 2+.

## Boxes (use sparingly, where they add something)

- `<div class="box glossary" markdown="1">`: **📖 Words from this story**. Required at the end of each story; lists every term defined inline.
- `<div class="box gotcha" markdown="1">`: **💥 Watch out for**, for caveats, preview status and common misunderstandings.
- `<div class="box realworld" markdown="1">`: **🌍 In the real world**, a named company or project, with a source.
- `<div class="box tryit" markdown="1">`: **🧪 Try it**, an optional hands-on snippet.
- `<div class="box aside" markdown="1">`: a short side note or bit of history.
- `<div class="box casefile" markdown="1">`: a dark, monospace "incident log", for stories that start from an outage or CVE.
- `<div class="box brief" markdown="1">`: the **On the radar** list at the end of the issue.
- `<div class="tldr" markdown="1">`: the opening summary box.
- `meter` and `stats` blocks still work, but they're optional in this format.

## Rules
- **At least 2 visuals per deep-dive story**, each explaining something (a mechanism, a before/after, history, sourced numbers). Never decorative.
- Never invent data. Label illustrative examples as illustrative. Vendor numbers are claims.
- No quiz, no revision card.
- After building, look at **every** page image. Fix clipped labels, overflowing code, half-empty pages and stranded headings.
