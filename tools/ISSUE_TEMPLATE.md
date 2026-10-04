---
issue: 1
date: 2026-10-05
title: "A headline that captures both stories, with a little personality"
---

<!--
SKELETON for Java – Beautifully Broken and Storage Wars (deep-dive news format).
Copy this structure. Replace every bracketed instruction. Delete these comments.
Components: {{term|definition}} inline definitions, box classes (see tools/VISUALS.md),
viz blocks, and [^footnotes] for sources. Footnote definitions go at the very end.
-->

<div class="tldr" markdown="1">
☕ Today's two stories

1. **[Story 1 in one sentence: what happened + why a developer should care.]**
2. **[Story 2 in one sentence.]**
3. **On the radar:** [N] more things that happened, listed at the end.
</div>

# Story 1 · [Short title of the news]

<div class="byline">[Area, e.g. JDK 28 · OpenJDK] · Announced [date] · ~[N] min read</div>

<p class="opener" markdown="1">[2–4 sentence hook: a scene, a question or the surprising fact. Make the reader want to keep going.]</p>

### What happened

[The news itself, precisely: who, what, when, which version, current status (proposed / preview / GA), with a footnote on every fact.[^s1]]

### The background you need

[Everything a reader needs to understand the news: the problem it solves, how things worked before, and the history (previous versions, earlier attempts). Define every technical term on first use, e.g. {{G1|the JVM's default garbage collector, which splits the heap into regions}}. No outside reading should be needed.]

### How it works

[The core explanation: the mechanism, step by step. Code, config or commands, plus at least one diagram (viz:flow / layers / loop / codecompare / versus).]

```viz:flow
title: "[What the diagram shows]"
headers: [Before, Change, After]
columns:
  - - label: "[box]"
      sub: "[detail]"
  - - label: "[box]"
      sub: "[detail]"
      style: accent
  - - label: "[box]"
      sub: "[detail]"
```

### What it means for you

[Practical impact: who's affected, what to do now vs later, how to try it, migration or upgrade notes. Concrete, with a real-world example where possible (a named company, project or incident, with a source).]

<div class="box gotcha" markdown="1">
**💥 Watch out for**

- [Caveats, limitations, things still in preview, common misunderstandings.]
</div>

### What happens next

[Timeline, open questions, what to watch. Optional if nothing is pending.]

<div class="box glossary" markdown="1">
**📖 Words from this story**

- **[Term]**: [plain-English definition]
- [Every term defined inline above appears here too.]
</div>

# Story 2 · [Short title]

[Same structure as Story 1.]

## On the radar

<div class="box brief" markdown="1">
**Also happened, in one line each. Some will get a full deep dive in a future issue.**

- **[Item]:** [one sentence: what and why it matters].[^r1]
- [4–8 items in total]
</div>

[^s1]: [Source title](https://example.com), publisher, date.
[^r1]: [Source title](https://example.com).
