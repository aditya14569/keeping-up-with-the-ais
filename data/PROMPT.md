# Daily run instructions: Storage Wars

You are writing today's issue of **Storage Wars**, a daily briefing on databases, streaming and data platforms: how data is stored and moved, plus what's new across Postgres, MySQL, Redis, Kafka, Databricks, Snowflake and the rest. It's emailed as a PDF to a small group by `.github/workflows/send-newsletters.yml` as soon as a new PDF lands in `data/issues/` on `main`.

**Work only inside `data/` and `tools/`.** Never edit anything else in the repo. The root files belong to the separate "Keeping up with the AIs" newsletter.

## The reader
Software developers with ~6 years of experience. They use databases, caches and queues daily but want to really understand **how they work underneath**, revise the fundamentals, and keep up with a fast-moving ecosystem. Treat them as capable professionals. Simplify, but never talk down. Explain the *why*, show real commands and configs, and name the trade-offs.

## 0. Setup
1. `pip install --break-system-packages -r requirements.txt` (run `playwright install chromium` if Chromium is missing).
2. Read `data/settings.yml` and obey it:
   - `read_time_minutes` → the build script estimates reading time (words at 200 wpm, including code, plus ~20 s per visual). Aim for the estimate to land within ±2 min of `read_time_minutes`. **Hard cap: `read_time_minutes` + 5.** The build prints `!! OVER` past the cap, so cut until it doesn't.
   - `difficulty` 1–5 → depth, as defined in the file's comments.
   - `learn_share` → split the words between Part 1 and Part 2 in that ratio (±10%).
   - `focus` → if non-empty, prefer curriculum topics and news matching these.
3. Read `data/state/curriculum.md`, `data/state/news-log.md`, `data/state/sources.md`, `tools/VISUALS.md` and the most recent issue in `data/issues/` (match its structure and tone).
4. Today's date is in IST. The issue number is the last one + 1. **If an issue for today already exists in `data/issues/`, stop.**

## 1. Part 2 research (What's new)
- Cover everything since the last issue. On quiet days, widen to the week and go deeper on fewer items.
- Use `data/state/sources.md`. **Official sources first**: project release notes and blogs (postgresql.org, kafka.apache.org, redis.io, docs.databricks.com release notes, Snowflake/MongoDB/ClickHouse/DuckDB blogs, AWS/GCP/Azure "what's new"). Then trusted outlets and engineering blogs. Use community sources for discovery only, and cite the original.
- Skip anything already in `data/state/news-log.md` unless it moved (beta → RC → GA, preview → GA). Mark those "Update:".
- What to cover: releases and end-of-life dates, new cloud database features, licensing changes, company moves that affect users, security issues, and engineering case studies (how Discord, Uber, Netflix, Shopify, etc. store and move data).
- Rank by: affects what they run or choose this year > security and end-of-life dates > architecture trends > business news.

## 2. Part 1 topic (Learn)
- Take the first `[ ]` item in `data/state/curriculum.md`. You may pull a later item forward if the news makes it timely.
- Every Learn section has:
  - a hook,
  - a **`viz:layers` or `viz:flow`** showing the mechanism,
  - one more visual (versus, loop, bars with sourced numbers, or a table),
  - a **🌍 In the real world** box (a named company, system or incident, with a source),
  - a **💥 Gotcha** box,
  - a **🔬 Under the hood** box,
  - a **🧪 Try it** (`docker run` + psql/redis-cli/kafka CLI, 10–15 min),
  - **🔗 Go deeper** with 3–4 links, **official docs first**, then trusted resources (Use The Index, Luke; well-known engineering blogs; the original papers).
- Concrete numbers (page sizes, defaults, limits) must come from official docs, with the link.

## 3. Write `data/issues/YYYY-MM-DD-issue-NNN.md`
Use the same skeleton as the last issue:
- Front matter: `issue`, `date`, `title` (punchy, with a little Storage Wars attitude).
- `<div class="tldr" markdown="1">`: "⚡ The short version", 3 numbered one-liners.
- A `viz:stats` **Release radar**: 3 current version facts relevant today (e.g. latest Postgres major, latest Kafka, a notable end-of-life date). Verify each, every day.
- `# Part 1 · Learn` → the topic, as above.
- `# Part 2 · What's new` → an opening visual, then 2–3 top stories (tags, What happened / Why it matters / What to do, a `viz:meter` with `impact`, `urgency` and optionally `prod`), then ⚡ Quick hits as `cards` (5–8, the last one "🗓️ Coming up").
- Finish with **📌 Revision card** (`box revision`): 6–8 crisp takeaways, then the footer. **No quiz.**
- At least 6 visuals in total. Short paragraphs. Bold the one phrase per paragraph a skimmer should catch.

**Sourcing:** every news claim and non-obvious technical claim links to its source as `[(Source)](url)`. Never invent versions, defaults, benchmarks, dates or URLs. Vendor performance numbers are written as claims. Paraphrase; never copy.

## 4. Build and check
1. `python3 tools/build_newsletter.py data/issues/<file>.md`. Fix any `!! OVER` warning.
2. `pdftoppm -r 70 -png <pdf> /tmp/d` and look at **every** page. Fix clipped diagrams, overflowing code, half-empty pages and stranded headings, then rebuild.

## 5. Update state and publish
1. Mark the curriculum item `[x] Issue #N (date)`. If fewer than 10 `[ ]` remain, append 15 new topics (keep the track balance).
2. Append today's stories to `data/state/news-log.md` and update its "Open threads" and "Release radar" sections.
3. `git pull --rebase origin main`, then commit only `data/` files in one commit (`Storage Wars #N: <title>`) and push to `main`. The push sends the email. Push exactly once.
4. Finish with a 3-line summary: issue number, title, Learn topic.
