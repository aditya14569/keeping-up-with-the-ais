# Daily run instructions: Keeping up with the AIs

You are writing today's issue of **Keeping up with the AIs**, a daily AI briefing for a small group of friends: vibe coders and developers in India. The issue is emailed as a PDF every morning by the GitHub Actions workflow in this repo. It sends automatically when a new PDF is pushed to `main`.

## 0. Setup
1. Clone the repo, then `pip install --break-system-packages -r requirements.txt` (add `playwright install chromium` if Chromium is missing).
2. Read `state/curriculum.md`, `state/news-log.md`, `state/sources.md`, and the most recent issue in `issues/` to match tone and format.
3. Work out today's date in IST and the next issue number (last issue + 1). If an issue for today's date already exists, stop: don't send twice.

## 1. Research (What moved)
- Cover the last 24 hours. On a Monday, or if the last issue is older than a day, cover everything since the last issue.
- Search every layer in `state/sources.md`. Search each major lab separately rather than in one combined query. Fetch the actual pages for anything you'll feature.
- Skip stories already in `state/news-log.md`, unless there's a real new development. Mark those "Update:".
- Check the "Open threads" list in the news log and follow up on anything that has resolved.
- Rank by: impact on what readers can build or use > big-lab launches > money/policy > everything else.

## 2. Pick the Learn topic
- Take the first `[ ]` topic in `state/curriculum.md`. If a later topic is the centre of today's news, you may pull it forward.
- Find 3–4 real, high-quality tutorials, docs or articles for it. Open each link to confirm it works and fits. Prefer official docs, free courses and well-known engineering blogs.

## 3. Write `issues/YYYY-MM-DD-issue-NNN.md`
Copy the exact structure of the last issue, and read `VISUALS.md` first. **The issue should be fun to read, not a chore.** It should feel like a good magazine: visual, punchy and scannable.
- Front matter: `issue`, `date`, `title` (a short, punchy headline for the day).
- `<div class="tldr" markdown="1">`: "⚡ If you only have one minute", 3 numbered one-liners.
- A `viz:stats` strip: "Today in three numbers", using real, sourced numbers only.
- `# Part 1 · Learn one thing` (~4 min): an H2 with an emoji, tag pills, a bold one-line hook, the plain-English version, an **analogy**, at least one **diagram** (`viz:loop`, `viz:flow`, `viz:versus` or a table), a 📖 Jargon buster box, "Why now?" if relevant, a 🧪 Try it in 10 minutes box (no-code + some-code), a 🛠️ For devs box (code + gotchas), and 🔗 Go deeper with 3–4 links.
- `# Part 2 · What moved in AI` (~7 min): open with a visual (a `viz:timeline` when there's a multi-day arc, otherwise a flow or bars chart). Then 2–3 top stories, each with: tag pills, What happened, a diagram or chart where one genuinely helps, The details that matter, Why it matters, a `viz:meter`, a 👀 Should you care? box, and a 🛠️ For devs box where useful. Then ⚡ Quick hits as `cards` (6–8 items, emoji + bold title, the last one "🗓️ Coming up"), a 🎯 One thing to try today box, a `viz:quiz` (3 questions), and the footer.
- Short paragraphs (≤ 4 lines). Bold the one phrase per paragraph that someone skimming should see.

**Length:** 1,700–2,300 words of text plus the visuals (the build script prints the count), which is 10–12 minutes. **Hard maximum 2,500 words.**

**Voice:** a vibe coder must understand every sentence, and a developer must find something useful in every item. Explain jargon the first time you use it. No hype words. Company numbers are "claims." Use Indian context (₹, IST, Indian availability) where natural.

**Sourcing:** every news claim links to its source as `[(Outlet)](url)`. Never invent facts, numbers, quotes or URLs. If you can't verify something, leave it out. Paraphrase; never copy sentences from articles.

## 4. Build and check
1. `python3 scripts/build_pdf.py issues/<file>.md`
2. Render the pages to PNG (`pdftoppm -r 70 -png <pdf> /tmp/p`) and look at **every** page. Fix clipped diagram labels, overflowing boxes, half-empty pages and headings stranded at the bottom of a page, then rebuild.
3. Re-check every number and date against its source.

## 5. Update state and publish
1. In `state/curriculum.md`, mark the topic `[x] Issue #N (date)`. If fewer than 10 topics remain, append 15 new ones.
2. Append today's stories to `state/news-log.md` and update "Open threads."
3. Commit the .md, the .pdf and the state files together in one commit: `Issue #N: <title>`. Push to `main`. The push triggers the email.
4. Finish with a 3-line summary: issue number, title, and the Learn topic.
