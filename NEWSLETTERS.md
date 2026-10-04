# Newsletters in this repo

| Newsletter | Folder | Sent (IST) | Settings |
|---|---|---|---|
| Keeping up with the AIs | repo root (`issues/`, `state/`, `PROMPT.md`) | ~6:45 AM | edit `PROMPT.md` |
| Java – Beautifully Broken (latest Java news, 2 deep dives/day) | [`java/`](java/) | ~7:40 AM | [`java/settings.yml`](java/settings.yml) |
| Storage Wars (latest data/DB news, 2 deep dives/day) | [`data/`](data/) | ~8:20 AM | [`data/settings.yml`](data/settings.yml) |

All three use the same email secrets. The Java and Storage Wars newsletters share `tools/` (PDF builder, visuals, email body) and the `send-newsletters.yml` workflow. The AI newsletter keeps its own `scripts/` and `send-issue.yml`, untouched.
