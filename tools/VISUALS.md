# Visual toolkit: Java – Beautifully Broken & Storage Wars

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

## HTML boxes and tags (write them straight in Markdown)

- `<div class="box realworld" markdown="1">`: **🌍 In the real world**, how a named company or a well-known system uses this, with a source link.
- `<div class="box gotcha" markdown="1">`: **💥 Gotcha**, what breaks in production or trips people up.
- `<div class="box devs" markdown="1">`: **🔬 Under the hood**, the deeper internals for when you want more.
- `<div class="box jargon" markdown="1">`: **📖 Jargon buster**
- `<div class="box tryit" markdown="1">`: **🧪 Try it**, a 10–15 minute hands-on exercise (jshell, docker run, psql, redis-cli…)
- `<div class="box care" markdown="1">`: **👀 Should you care?**
- `<div class="box revision" markdown="1">`: **📌 Revision card**, closes every issue: 6–8 crisp takeaways from the whole issue, shown in two columns.
- `<div class="cards" markdown="1">` wrapping a bullet list: two-column quick-hit cards. Start each item with an emoji and a **bold title.**
- Tags under a heading: `<span class="tag hot">BIG DEAL</span>`. Classes: `hot`, `try`, `dev`, `watch`, `learn`.

## Rules
- **No quiz** in these newsletters.
- **At least 6 visuals per issue.** Include at least one `codecompare` (Java) or one `layers`/`flow` (Storage Wars) in Learn, a visual in What's new, and a meter on each top story.
- Visuals must explain, not decorate. Never invent data. Label illustrative examples as illustrative.
- For anything the blocks can't draw, you may write a small inline `<svg>` (width 640, fonts Poppins/Body).
- After building, look at **every** page image. Fix clipped labels, overflowing code, half-empty pages and stranded headings.
