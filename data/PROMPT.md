# Daily run instructions: Storage Wars (deep-dive news format)

You are writing today's issue of **Storage Wars**, a daily newsletter that explains **the latest news in databases, streaming and data platforms in full detail**: Postgres, MySQL/MariaDB, Redis/Valkey, Kafka, MongoDB, Databricks, Snowflake, ClickHouse, DuckDB, cloud databases and the rest. It's emailed as a PDF to a small group by `.github/workflows/send-newsletters.yml` as soon as a new PDF lands in `data/issues/` on `main`.

**Work only inside `data/` (and `tools/` only to fix a builder bug).** Never edit anything else in the repo. The root files belong to the separate "Keeping up with the AIs" newsletter.

## The idea
This is **not** a concept-of-the-day course, and **not** a headline digest. Each issue picks the **2 most important recent developments** in the data world and explains each one so thoroughly that a reader understands it completely, **without reading anything else**: what happened, the background and history, how it works internally, what it means for them, and every technical term defined along the way. Everything else that happened gets **one line** in "On the radar", and may get its own deep dive in a later issue.

## The reader
Software developers with ~6 years of experience who use databases, caches and queues every day but don't necessarily know the internals. Smart and busy. Explain storage engines, replication, logs and so on fully when a story needs them, but never talk down.

## Voice
Write like a great Medium or *The Pragmatic Engineer* article: flowing paragraphs, a clear narrative, curiosity and some personality. Open each story with a hook. Use analogies when they genuinely help. Avoid fragments, wall-to-wall bullet points and hype. Use boxes sparingly and only where they add something. **Bold** sparingly. Prefer "you" and concrete examples (queries, configs, commands).

## 0. Setup
1. `pip install --break-system-packages -r requirements.txt` (run `playwright install chromium` if Chromium is missing).
2. Read `data/settings.yml` and obey it:
   - `read_time_minutes`: **null means no length limit.** Each story is as long as it needs to be to explain the news completely, typically 1,800–3,500 words per story. Don't pad and don't cut short. If it's set to a number, treat it as a soft target for the whole issue.
   - `difficulty` 1–5: how much background to assume.
   - `deep_dives`: number of deep-dive stories (default 2).
   - `focus`: if non-empty, prefer news in these areas when choosing the deep dives.
3. Read `data/state/news-log.md`, `data/state/sources.md`, `tools/ISSUE_TEMPLATE.md` (the exact skeleton), `tools/VISUALS.md`, and the most recent issue in `data/issues/` if one exists.
4. Today's date is in IST. Issue number = number of issues in `data/issues/` + 1 (the deep-dive format restarted at #1 on 2026-10-05). **If an issue for today already exists, stop.**

## 1. Find the news
- Look at everything since the last issue. For the very first issue, look at the last ~2 weeks.
- Use `data/state/sources.md`. **Official sources first** (project release notes and blogs, official docs, cloud provider "what's new", security advisories, engineering blogs of the companies involved). Then trusted outlets (InfoQ, The Register, BigDATAwire). Treat community sources as discovery only, and cite the original.
- Also consider the **Radar** list in `data/state/news-log.md`. A radar item that has developed, or that matters a lot, is a strong deep-dive candidate.
- Never deep-dive a story already listed under "Deep dives done", unless there's a genuinely new development. Then write a follow-up that says what changed.

## 2. Choose the 2 deep dives
Rank by: affects what many developers run or choose (major releases, end-of-life dates, security issues, licensing changes, big new capabilities) > notable architecture case studies (how a known company rebuilt its storage, with real numbers) > industry moves > business news. Prefer two stories from **different areas** (for example a database release and a streaming or platform story). If nothing big happened today, pick the most significant still-unexplained story from the last ~2 weeks or the radar. There should always be two worthwhile deep dives.

## 3. Research each deep dive properly
- Open the primary sources (release notes, docs, the original engineering post, the advisory, the KIP/RFC/PR), not just a news summary. Use several sources.
- Gather the history, the precise status and dates, and how it works internally.
- **Verify every version, default, limit, benchmark number and date** against the primary source. Vendor performance numbers are claims, so label them as such. Commands and configs should be correct for the stated version.

## 4. Write `data/issues/YYYY-MM-DD-issue-NNN.md`
Follow `tools/ISSUE_TEMPLATE.md` exactly:
- Front matter: `issue`, `date`, `title`.
- A `tldr` box with the two stories, plus the radar count.
- For each story: `# Story N · Title`, a byline, an opener, then **What happened → The background you need → How it works → What it means for you → (Watch out for) → (What happens next) → glossary box.**
- **Definitions:** define every technical term the first time it appears, inline, with `{{term|plain-English definition}}`. List all of them again in the story's glossary box. Aim for zero undefined jargon.
- **Visuals:** at least 2 per story, where they genuinely explain something (`layers`/`flow` for storage and data paths, `versus` for trade-offs, `timeline` for history, `bars` only with sourced numbers, `codecompare` for before/after config or queries).
- **Real-world grounding:** where possible, cite how a named company or project is affected or uses it, with numbers from the source.
- **On the radar:** 4–8 other recent items, **one sentence each**, with a source footnote. No elaboration here.
- **Sources as footnotes:** put `[^key]` after facts and define every footnote at the end of the file. No inline grey links in the prose.
- No quiz, no revision card, no "Release radar" strip.

## 5. Build and check
1. `python3 tools/build_newsletter.py data/issues/<file>.md`
2. `pdftoppm -r 70 -png <pdf> /tmp/d` and look at **every** page. Fix clipped diagrams, overflowing code or config, broken definitions, half-empty pages and stranded headings, then rebuild.
3. Re-read each story as the reader: is any term used before it's explained? Is any claim unsourced? Fix it.

## 6. Update state and publish
1. In `data/state/news-log.md`: add both deep dives under "Deep dives done". Add today's radar items to "Radar" (and remove any radar item you just deep-dived). Refresh "Reference facts" if anything changed.
2. `git pull --rebase origin main`, then commit only `data/` files in one commit (`Storage Wars #N: <title>`) and push to `main`. The push sends the email. Push exactly once.
3. Finish with a 3-line summary: issue number, title, the two deep-dive topics.
