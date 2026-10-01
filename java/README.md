# Java – Beautifully Broken

A daily briefing, researched and written by Claude, emailed as a PDF to the readers.
**Part 1 · Learn** follows `state/curriculum.md`. **Part 2 · What's new** covers everything since the last issue.

## Change the length or difficulty (no coding needed)

Open [`settings.yml`](settings.yml) on GitHub, click the ✏️ pencil, edit, and **Commit changes**. The next morning's issue follows it.

| Setting | What it does | Default |
|---|---|---|
| `read_time_minutes` | Target reading time; the hard cap is this + 5 | `20` |
| `difficulty` | 1 = refresher · 2 = practical · 3 = working dev · 4 = senior · 5 = deep dive | `3` |
| `learn_share` | % of the issue spent on Learn vs What's new | `50` |
| `focus` | Topics to lean towards for a while, e.g. `[kafka, postgres]` | `[]` |

## Other things you can edit
- `state/curriculum.md`: the learning path. Reorder, add or remove topics any time.
- `PROMPT.md`: the full instructions the daily run follows (tone, structure, sourcing rules).
- `state/sources.md`: where the news comes from.

## How it's sent
A scheduled Claude task writes the issue, builds `issues/<date>-issue-NNN.pdf` with `tools/build_newsletter.py`, and pushes it.
`.github/workflows/send-newsletters.yml` then emails it, BCC, to `RECIPIENTS`. To send this newsletter to a different list,
add an optional secret `JAVA_RECIPIENTS` (comma-separated emails). To re-send an issue: **Actions → Email new issue (Java & Storage Wars) → Run workflow**, then enter the PDF path.
