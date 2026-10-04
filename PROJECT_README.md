# Project context: three daily newsletters (compact handoff)

> Paste this file into any new AI chat to pick up exactly where we left off. It summarises everything decided and built so far (Sept 30 – Oct 4, 2026; last updated 4 Oct, evening).

## 1. What this is
Three daily PDF newsletters, **researched and written by Claude**, built in this repo, and **emailed by GitHub Actions** to a small group of friends.
- **AI newsletter:** **Learn** (one curriculum topic) + **What moved** (latest news). Unchanged since launch.
- **Java and Storage Wars (deep-dive news format since 5 Oct 2026):** each issue explains the **2 most important recent news stories in full detail** (what happened, background and history, how it works, what it means for you), with **every technical term defined inline** and in a glossary, and sources as footnotes. Everything else gets **one line** in "On the radar", and may get a deep dive later. **No length cap.** Numbering restarted at **#1 on 5 Oct 2026**. The old learning-format issues (1–4 Oct) are archived in `java/archive/` and `data/archive/`.

| Newsletter | Folder | Reader & length | Theme | Daily run (IST) | Ends with |
|---|---|---|---|---|---|
| **Keeping up with the AIs** | repo root (`issues/`, `state/`, `PROMPT.md`, `scripts/`) | Vibe coders → developers, 10–12 min | purple/coral | **6:45 AM** | Pop quiz |
| **Java – Beautifully Broken** | `java/` | Dev with ~6 yrs experience, 2–3 in Java (8/11 era). Latest Java news, explained in depth. No length cap | orange | **7:40 AM** | On the radar (one-liners) |
| **Storage Wars** | `data/` | Same reader. Latest news in databases, Kafka, Redis, Databricks etc., explained in depth. No length cap | teal | **8:20 AM** | On the radar (one-liners) |

Issue #1 dates: AI 2026-09-30. Java and Storage Wars: first launched 2026-10-01 in a learning format (4 issues, now archived), then **relaunched as #1 on 2026-10-05** in the deep-dive news format.

## 2. How it works
```
Scheduled Claude task (cloud, auto-approve)
  → clones aditya14569/keeping-up-with-the-ais
  → follows <folder>/PROMPT.md: research → write issues/<date>-issue-NNN.md → build PDF → check every page → update state/
  → git pull --rebase, commit, push to main (only that newsletter's files)
GitHub Actions (on a new PDF)
  → AI:        .github/workflows/send-issue.yml        (issues/*.pdf)
  → Java/Data: .github/workflows/send-newsletters.yml  (java/issues/*.pdf, data/issues/*.pdf)
  → emails the PDF via Gmail SMTP, BCC to recipients, with a short summary in the body
```
- **Scheduled tasks** (claude.ai): "Keeping up with the AIs: daily issue", "Java – Beautifully Broken: daily issue", "Storage Wars: daily issue". Each run starts fresh and has no memory, so all memory lives in the repo's `state/` files.
- **Per-newsletter memory:** AI: `state/curriculum.md` (topics ticked off as `[x] Issue #N`), `state/news-log.md`, `state/sources.md`. Java/Data: `state/news-log.md` ("Deep dives done", plus a **Radar** of mentioned-but-not-yet-explained items that are candidates for future deep dives, plus reference facts) and `state/sources.md`. There's no curriculum any more.
- **Issue skeleton for Java/Data:** `tools/ISSUE_TEMPLATE.md`. Two `# Story N · Title` sections, each running What happened → Background → How it works → What it means for you → (Watch out for) → (What happens next) → Glossary, then "On the radar" and footnotes.
- **Builders:** `scripts/build_pdf.py` (AI only) and `tools/build_newsletter.py` (Java/Data, driven by `settings.yml`). HTML → PDF via Playwright/Chromium. Fonts are bundled in `fonts/` because npm font downloads are blocked in the sandbox.
- **Visual blocks**, written as fenced ```` ```viz:<type> ```` YAML in the Markdown: stats, bars, timeline, loop, flow, versus, meter (+ quiz for AI; layers and codecompare for Java/Data). Docs: `VISUALS.md` (AI) and `tools/VISUALS.md` (Java/Data).
- **Java/Data text components:** inline definitions `{{term|definition}}`, `[^footnotes]` for sources, an opener paragraph with a drop cap, a byline, and boxes (glossary, gotcha, realworld, tryit, aside, casefile, brief). At least 2 visuals per story.

## 3. Settings you can change (no coding)
- **Java / Storage Wars:** edit `java/settings.yml` or `data/settings.yml` on GitHub (pencil icon → Commit). The next run follows it:
  `read_time_minutes` (`null` = no limit, the default; a number = soft target) · `difficulty` 1–5 (how much background to assume) · `deep_dives` (stories per issue, default 2) · `focus` (areas to prefer, e.g. `[kafka, postgres]`).
- **AI newsletter:** edit `PROMPT.md` (length rule: 1,700–2,300 words, max 2,500).
- **Topics:** AI: reorder or add lines in `state/curriculum.md`. Java/Data: add items to the Radar in `state/news-log.md` to suggest future deep dives.

## 4. Email setup (already done)
GitHub repo → **Settings → Secrets and variables → Actions → Repository secrets**:
`SMTP_SERVER` = smtp.gmail.com · `SMTP_PORT` = 465 · `SMTP_USERNAME` = the sender Gmail · `SMTP_PASSWORD` = that account's 16-character **app password** (needs 2-Step Verification) · `RECIPIENTS` = comma-separated emails, **no quotes, no spaces**.
Optional: `JAVA_RECIPIENTS` / `DATA_RECIPIENTS` give a newsletter its own list (otherwise it falls back to `RECIPIENTS`). Recipients are BCC'd. Email addresses are kept **only in secrets**, never in this public repo.

**Add or remove a reader:** Settings → Secrets and variables → Actions → click `RECIPIENTS` → **Update secret** → paste the full list again (GitHub never shows the old value) → Save. It takes effect on the next send.

**Re-send or test an issue:** Actions → "Email new issue" (AI) or "Email new issue (Java & Storage Wars)" → **Run workflow** → enter the PDF path, e.g. `java/issues/2026-10-04-issue-004.pdf`. Use a laptop; the Run button is hidden on GitHub mobile.

## 5. Ground rules (keep these in any future change)
- **Never change the AI newsletter's files** when working on Java/Data (root `PROMPT.md`, `VISUALS.md`, `scripts/`, `state/`, `issues/`, `send-issue.yml`, `README.md`).
- Every news claim links to a source actually opened. **Official docs and release notes first**, then trusted outlets. Vendor numbers are labelled as claims. Never invent versions, JEP numbers, defaults or URLs.
- Real-world examples wherever possible (named companies, incidents), each with a source.
- Simplify, but not for babies: explain the *why* and show real code and commands.
- Java/Data voice: flowing, Medium-style articles with a hook, a narrative and personality. Not fragmented bullet lists. Every story must be understandable without reading anything else.
- Each run checks every rendered page image (no clipped diagrams, stranded headings or half-empty pages) before pushing, and pushes **once**. The push is what sends the email.

## 6. Lessons learned / gotchas
- **GitHub access:** Claude needed the **Claude GitHub App installed** on the repo (github.com/apps/claude) for push access. The repo was made **public** so the connection could see it.
- **First emails land in spam:** mark "Not spam" and add the sender to contacts (each reader does this once).
- An email sent from your own Gmail to yourself shows up in **Sent**, not the inbox.
- PDF layout: big figures avoid splitting across pages, which can leave gaps. The builder keeps headings with their first paragraph and lets tables split by row.
- A run is skipped if today's issue already exists. For an ad-hoc extra issue, fire the scheduled task with a note telling it to ignore that rule (that's what happened on Oct 1, which made Issue #2 for Java/Data).

## 7. History of format decisions
- 30 Sep: AI newsletter launched (Learn + What moved, quiz at the end). 1 Oct: Java and Storage Wars launched in the same Learn + What's new format (~20 min, revision card instead of quiz).
- 4 Oct: three Java formats were tried as samples (Long Read essays, textbook chapters, case files) to make it more of a learning source.
- 4 Oct (final decision): Java and Storage Wars became **deep dives into the latest news**. 2 big stories per issue, fully explained with context and definitions, one-line radar for the rest, no length cap, numbering restarted at #1 from 5 Oct.

## 8. Ideas not yet done
- Weekend lighter "weekly recap" format (currently full issues every day).
- Per-reader interest tags; a web archive page of past issues; per-newsletter recipient lists.
