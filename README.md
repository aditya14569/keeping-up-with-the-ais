# Keeping up with the AIs

A daily AI briefing, written by Claude and emailed as a PDF every morning.

- **Part 1 · Learn one thing:** one AI concept a day, following `state/curriculum.md`, with links to go deeper.
- **Part 2 · What moved:** the last 24 hours in AI, explained so vibe coders get it and developers find it useful.

## How it works

```
6:45 AM IST  Claude scheduled task  ──►  researches + writes issues/<date>.md + .pdf
                                         updates state/ files, pushes to main
                                                   │
                                                   ▼
             GitHub Actions (send-issue.yml)  ──►  emails the new PDF (BCC) to everyone
```

- `PROMPT.md` holds the instructions the daily run follows. Edit it to change tone, length or sections.
- `state/curriculum.md` is the learning path. Reorder or add topics any time.
- `state/news-log.md` holds stories already covered (to avoid repeats) and open threads to follow up.
- `state/sources.md` lists where to look.
- `VISUALS.md` documents the diagram and chart blocks (stats, loop, flow, bars, timeline, versus, meter, quiz) that every issue uses.
- `scripts/build_pdf.py` turns Markdown into the PDF, drawing the visual blocks. `fonts/` holds the open-licensed fonts it uses. `scripts/email_body.py` builds the email text.

## One-time email setup (about 10 minutes)

Use a **spare Gmail account** (for example `keepingupwiththeais@gmail.com`), not your personal one. Its password lives only in GitHub secrets.

1. On that account, turn on **2-Step Verification**, then create an **App password** at <https://myaccount.google.com/apppasswords>. Copy the 16-character password.
2. In this repo: **Settings → Secrets and variables → Actions → New repository secret**. Add:

| Secret | Value |
|---|---|
| `SMTP_SERVER` | `smtp.gmail.com` |
| `SMTP_PORT` | `465` |
| `SMTP_USERNAME` | the spare Gmail address |
| `SMTP_PASSWORD` | the 16-character app password |
| `RECIPIENTS` | comma-separated emails, e.g. `you@gmail.com,friend1@gmail.com` |

3. Test it: **Actions → Email new issue → Run workflow** with `issues/2026-09-30-issue-001.pdf`.

Friends are BCC'd, so they don't see each other's addresses. To add or remove someone, edit the `RECIPIENTS` secret.

Any SMTP provider works (Outlook, Zoho, Brevo, etc.). Just change the four SMTP secrets.

## Build a PDF locally

```bash
pip install -r requirements.txt && playwright install chromium
python3 scripts/build_pdf.py issues/2026-09-30-issue-001.md
```
