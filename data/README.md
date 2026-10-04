# Storage Wars

A daily newsletter that explains **the latest news in full detail**, researched and written by Claude and emailed as a PDF.

**Format (since 5 Oct 2026, numbering restarted at #1):** every issue has **2 deep-dive stories** on the most important recent developments. Each one is explained end to end (what happened, background and history, how it works, what it means for you), with every technical term defined inline and in a glossary, and sources as footnotes. Everything else gets **one line** in "On the radar", and may get its own deep dive later. There's no length cap.

Earlier issues in the old learning format (1–4 Oct 2026) are in `archive/v1-learning-format/`.

## Change it (no coding needed)
Open [`settings.yml`](settings.yml) on GitHub, click the ✏️ pencil, edit, and **Commit changes**. The next morning's issue follows it.

| Setting | What it does | Default |
|---|---|---|
| `read_time_minutes` | `null` = no length limit. A number = soft target | `null` |
| `difficulty` | 1 = explain everything … 3 = working dev … 5 = expert | `3` |
| `deep_dives` | Deep-dive stories per issue | `2` |
| `focus` | Areas to prefer, e.g. `[kafka, postgres]` | `[]` |

## Files
- `PROMPT.md`: the full instructions the daily run follows (how stories are chosen, structure, voice, sourcing).
- `state/news-log.md`: deep dives already done, plus the **radar** of mentioned-but-not-yet-explained items (future deep-dive candidates).
- `state/sources.md`: where the news comes from (official sources first).
- `../tools/ISSUE_TEMPLATE.md`: the exact issue skeleton. `../tools/VISUALS.md`: diagrams and text components.

## How it's sent
A scheduled Claude task writes `issues/<date>-issue-NNN.md`, builds the PDF with `tools/build_newsletter.py`, and pushes it. `.github/workflows/send-newsletters.yml` then emails it, BCC, to `RECIPIENTS` (or to `DATA_RECIPIENTS` if that secret exists). To re-send: **Actions → Email new issue (Java & Storage Wars) → Run workflow**, then enter the PDF path.
