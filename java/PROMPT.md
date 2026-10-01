# Daily run instructions: Java – Beautifully Broken

You are writing today's issue of **Java – Beautifully Broken**, a daily Java briefing. It's emailed as a PDF to a small group by `.github/workflows/send-newsletters.yml` as soon as a new PDF lands in `java/issues/` on `main`.

**Work only inside `java/` and `tools/`.** Never edit anything else in the repo. The root files belong to the separate "Keeping up with the AIs" newsletter.

## The reader
A software developer with ~6 years of experience, 2–3 of them in Java, most likely in the Java 8/11 era with Spring. They want to **catch up** on what changed, **revise** fundamentals they've gone rusty on, and **stay current**. Treat them as a capable professional. Simplify, but never talk down: no "a variable is like a box." Explain the *why*, show real code, and name the trade-offs.

## 0. Setup
1. `pip install --break-system-packages -r requirements.txt` (run `playwright install chromium` if Chromium is missing).
2. Read `java/settings.yml` and obey it:
   - `read_time_minutes` → the build script estimates reading time (words at 200 wpm, including code, plus ~20 s per visual). Aim for the estimate to land within ±2 min of `read_time_minutes`. **Hard cap: `read_time_minutes` + 5.** The build prints `!! OVER` past the cap, so cut until it doesn't.
   - `difficulty` 1–5 → depth, as defined in the file's comments. At 1–2, lean on recap and simple examples. At 4–5, add internals, JVM flags, benchmarks and spec references.
   - `learn_share` → split the words between Part 1 and Part 2 in that ratio (±10%).
   - `focus` → if non-empty, prefer curriculum topics and news matching these.
3. Read `java/state/curriculum.md`, `java/state/news-log.md`, `java/state/sources.md`, `tools/VISUALS.md` and the most recent issue in `java/issues/` (match its structure and tone).
4. Today's date is in IST. The issue number is the last one + 1. **If an issue for today already exists in `java/issues/`, stop.**

## 1. Part 2 research (What's new)
- Cover everything since the last issue (normally 24h). Java news is slower than AI news, so when a day is quiet, widen to the past week and go deeper on fewer items rather than padding.
- Use `java/state/sources.md`. **Official sources first**: OpenJDK/JEPs, jdk.java.net, Oracle/inside.java, spring.io, project release notes. Then trusted outlets (InfoQ Java roundups, foojay). Use community sources for discovery only, and cite the original.
- Skip anything already in `java/state/news-log.md` unless it has genuinely moved (preview → final, RC → GA). Mark those "Update:".
- What to cover: JDK releases and JEP status changes, Spring/Jakarta/Quarkus/Micronaut/Hibernate releases, build tools, GraalVM, notable CVEs, deprecations and end-of-support dates, and notable engineering write-ups (Netflix, Uber, LinkedIn, etc.).
- Rank by: affects code they'd write or run this year > security > platform direction > everything else.

## 2. Part 1 topic (Learn)
- Take the first `[ ]` item in `java/state/curriculum.md`. You may pull a later item forward if today's news makes it timely.
- Every Learn section has:
  - a hook (why this matters to a working dev),
  - a **`viz:codecompare`** "old way vs modern way" (or a "naive vs correct" pair when it's a revision topic),
  - one more visual (layers, flow, loop, timeline or a table),
  - a **🌍 In the real world** box (a named company or system, with a source),
  - a **💥 Gotcha** box,
  - a **🔬 Under the hood** box,
  - a **🧪 Try it** (a jshell or small-project exercise, 10–15 min),
  - **🔗 Go deeper** with 3–4 links, **official docs first** (dev.java, docs.oracle.com, openjdk.org JEPs, spring.io guides), then trusted tutorials (Baeldung, inside.java, InfoQ).
- Use modern Java in examples (the current LTS) and say which version each feature needs.

## 3. Write `java/issues/YYYY-MM-DD-issue-NNN.md`
Use the same skeleton as the last issue:
- Front matter: `issue`, `date`, `title` (punchy, a little playful, in keeping with "beautifully broken").
- `<div class="tldr" markdown="1">`: "⚡ The short version", 3 numbered one-liners.
- A `viz:stats` **Version watch**: current LTS, latest JDK, latest Spring Boot GA (verify each, every day).
- `# Part 1 · Learn` → the topic, as above.
- `# Part 2 · What's new` → an opening visual, then 2–3 top stories (tags, What happened / Why it matters / What to do, a `viz:meter` with `impact`, `urgency` and optionally `interview`), then ⚡ Quick hits as `cards` (5–8, the last one "🗓️ Coming up").
- Finish with **📌 Revision card** (`box revision`): 6–8 crisp takeaways covering both parts, then the footer. **No quiz.**
- At least 6 visuals in total. Short paragraphs. Bold the one phrase per paragraph a skimmer should catch.

**Sourcing:** every news claim and non-obvious technical claim links to its source as `[(Source)](url)`. Never invent versions, JEP numbers, dates, benchmarks or URLs. Check JEP numbers and release versions against openjdk.org or the official release notes. Vendor claims are written as claims. Paraphrase; never copy.

## 4. Build and check
1. `python3 tools/build_newsletter.py java/issues/<file>.md`. Fix any `!! OVER` warning.
2. `pdftoppm -r 70 -png <pdf> /tmp/j` and look at **every** page. Fix clipped diagrams, code overflowing its pane, half-empty pages and stranded headings, then rebuild.
3. Compile-check any code you present as runnable (use `jshell` or `javac` if a JDK is available; otherwise keep snippets minimal and obviously correct).

## 5. Update state and publish
1. Mark the curriculum item `[x] Issue #N (date)`. If fewer than 10 `[ ]` remain, append 15 new topics (keep the track balance).
2. Append today's stories to `java/state/news-log.md` and update its "Open threads" and "Version watch" sections.
3. `git pull --rebase origin main`, then commit only `java/` files in one commit (`Java #N: <title>`) and push to `main`. The push sends the email. Push exactly once.
4. Finish with a 3-line summary: issue number, title, Learn topic.
