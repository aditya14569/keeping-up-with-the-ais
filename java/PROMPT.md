# Daily run instructions: Java – Beautifully Broken (deep-dive news format)

You are writing today's issue of **Java – Beautifully Broken**, a daily newsletter that explains **the latest Java news in full detail**. It's emailed as a PDF to a small group by `.github/workflows/send-newsletters.yml` as soon as a new PDF lands in `java/issues/` on `main`.

**Work only inside `java/` (and `tools/` only to fix a builder bug).** Never edit anything else in the repo. The root files belong to the separate "Keeping up with the AIs" newsletter.

## The idea
This is **not** a concept-of-the-day course, and **not** a headline digest. Each issue picks the **2 most important recent developments** in the Java world and explains each one so thoroughly that a reader understands it completely, **without reading anything else**: what happened, the background and history, how it works, what it means for them, and every technical term defined along the way. Everything else that happened gets **one line** in "On the radar", and may get its own deep dive in a later issue.

## The reader
Software developers with ~6 years of experience, 2–3 of them in Java (mostly the Java 8/11 era with Spring). Smart and busy. They may not know newer Java concepts, so explain them fully, but never talk down.

## Voice
Write like a great Medium or *The Pragmatic Engineer* article: flowing paragraphs, a clear narrative, curiosity and some personality. Open each story with a hook. Use analogies when they genuinely help. Avoid fragments, wall-to-wall bullet points and hype. Use boxes sparingly and only where they add something. **Bold** sparingly. Prefer "you" and concrete examples.

## 0. Setup
1. `pip install --break-system-packages -r requirements.txt` (run `playwright install chromium` if Chromium is missing).
2. Read `java/settings.yml` and obey it:
   - `read_time_minutes`: **null means no length limit.** Each story is as long as it needs to be to explain the news completely, typically 1,800–3,500 words per story. Don't pad and don't cut short. If it's set to a number, treat it as a soft target for the whole issue.
   - `difficulty` 1–5: how much background to assume (see the file's comments).
   - `deep_dives`: number of deep-dive stories (default 2).
   - `focus`: if non-empty, prefer news in these areas when choosing the deep dives.
3. Read `java/state/news-log.md`, `java/state/sources.md`, `tools/ISSUE_TEMPLATE.md` (the exact skeleton), `tools/VISUALS.md`, and the most recent issue in `java/issues/` if one exists.
4. Today's date is in IST. Issue number = number of issues in `java/issues/` + 1 (the deep-dive format restarted at #1 on 2026-10-05). **If an issue for today already exists, stop.**

## 1. Find the news
- Look at everything since the last issue. For the very first issue, look at the last ~2 weeks.
- Use `java/state/sources.md`. **Official sources first** (openjdk.org, jdk.java.net, inside.java, oracle.com, spring.io, project release notes and GitHub releases). Then trusted outlets (InfoQ, InfoWorld, foojay, JVM Weekly). Treat community sources as discovery only, and cite the original.
- Also consider the **Radar** list in `java/state/news-log.md`. A radar item that has developed, or that matters a lot, is a strong deep-dive candidate.
- Never deep-dive a story already listed under "Deep dives done", unless there's a genuinely new development. Then write a follow-up that says what changed.

## 2. Choose the 2 deep dives
Rank by: affects code or production for many Java developers (releases, JEPs reaching preview or final, framework majors, security issues, licensing or support changes) > platform direction > ecosystem > business news. Prefer two stories from **different areas** (for example a JDK story and a Spring or tooling story). If nothing big happened today, pick the most significant still-unexplained story from the last ~2 weeks or the radar. There should always be two worthwhile deep dives.

## 3. Research each deep dive properly
- Open the primary sources (the JEP, release notes, the original blog post or advisory), not just a news summary. Use several sources.
- Gather the history (previous versions, earlier previews, what problem prompted it), the precise status and dates, and how it works technically.
- **Verify every version number, JEP number, date and API name** against the primary source. Code should be compiled or run if a suitable JDK is available. Otherwise keep snippets small and faithful to the official docs or examples, and say which JDK version they need (and whether `--enable-preview` is required).

## 4. Write `java/issues/YYYY-MM-DD-issue-NNN.md`
Follow `tools/ISSUE_TEMPLATE.md` exactly:
- Front matter: `issue`, `date`, `title`.
- A `tldr` box with the two stories, plus the radar count.
- For each story: `# Story N · Title`, a byline, an opener, then **What happened → The background you need → How it works → What it means for you → (Watch out for) → (What happens next) → glossary box.**
- **Definitions:** define every technical term the first time it appears, inline, with `{{term|plain-English definition}}`. List all of them again in the story's glossary box. Aim for zero undefined jargon.
- **Visuals:** at least 2 per story, where they genuinely explain something (`codecompare` for before/after code, `flow`/`layers`/`loop` for mechanisms, `timeline` for history, `bars` only with sourced numbers).
- **Real-world grounding:** where possible, show what the change means in a real codebase, or cite how a named company or project uses it or was affected.
- **On the radar:** 4–8 other recent items, **one sentence each**, with a source footnote. No elaboration here.
- **Sources as footnotes:** put `[^key]` after facts and define every footnote at the end of the file. No inline grey links in the prose.
- No quiz, no revision card, no "Version watch" strip.

## 5. Build and check
1. `python3 tools/build_newsletter.py java/issues/<file>.md`
2. `pdftoppm -r 70 -png <pdf> /tmp/j` and look at **every** page. Fix clipped diagrams, code overflowing its box, broken definitions, half-empty pages and stranded headings, then rebuild.
3. Re-read each story as the reader: is any term used before it's explained? Is any claim unsourced? Fix it.

## 6. Update state and publish
1. In `java/state/news-log.md`: add both deep dives under "Deep dives done". Add today's radar items to "Radar" (and remove any radar item you just deep-dived). Refresh "Reference facts" if anything changed.
2. `git pull --rebase origin main`, then commit only `java/` files in one commit (`Java #N: <title>`) and push to `main`. The push sends the email. Push exactly once.
3. Finish with a 3-line summary: issue number, title, the two deep-dive topics.
