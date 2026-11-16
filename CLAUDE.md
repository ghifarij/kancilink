# Kancilink

A URL shortener that I containerize, automate, deploy and break on purpose to learn how it fails. It's my DevOps headline project for the ADI application. The shared rules in `../CLAUDE.md` apply here, especially **Who writes what** and **Commits**.

- Repo: `github.com/ghifarij/kancilink` (public)
- Image: `ghcr.io/ghifarij/kancilink`
- Live address (from Phase 9): `s.ghifarij.my.id`

## The app

- One Flask service run by gunicorn.
- Postgres stores the links (the source of truth).
- Redis caches lookups: Redis first, falling back to Postgres when Redis is down.
- Endpoints:
  - `POST /links` (needs an API token)
  - `GET /<code>` (the redirect)
  - click stats
  - `/health`
  - `/metrics`
- Only `http` and `https` targets are accepted.

## How Claude builds the app: 6 slices

Claude writes each slice as **one pull request**. Every slice goes through these steps:

1. **Learn.** About 30 minutes on the Python/Flask ideas this slice uses. Explain them with the slice's own code.
2. **Build.** Small, readable code with tests. Plain Flask, no extra frameworks unless I approve.
3. **Review quiz.** Ask me about 5 questions about this slice: what a line does, what happens when X fails, why it's built this way. Merge only after I answer all of them correctly. If I can't, explain and ask again.
4. **Record.** Add the slice's code notes to `docs/LEARNING.md`, in plain words, with what I struggled with.

| Slice | Content | Phase |
|---|---|---|
| 1 | Skeleton + `/health` | 0 |
| 2 | Create link + Postgres | 4 |
| 3 | Redirect + Redis cache with Postgres fallback | 4 |
| 4 | Click stats | 5 |
| 5 | API token check | 5 |
| 6 | `/metrics` | 7 |

I also make 3–5 app changes **myself** in Phase 4. Each one gets a DECISIONS entry.

## DevOps files are mine

Dockerfile, `compose.yaml`, nginx config, `.github/workflows/*`, Makefile, scripts, server setup and Prometheus/Grafana config are written by me. Claude coaches me through them as described in `../CLAUDE.md`.

## Git workflow

1. Branch from `main`.
2. Open a pull request.
3. CI must pass (once Phase 5 exists).
4. Squash-merge.

Never push to `main` directly. Branch names: `slice/N-name`, `devops/topic`, `fix/topic`.

## Records

| File | What goes in it |
|---|---|
| `docs/PROGRESS.md` | This repo's tasks, by phase |
| `docs/DECISIONS.md` | Numbered decisions with my reasons. My answer to "why X?" |
| `docs/LEARNING.md` | Dated log: slice code notes, what broke, how I fixed it. My answer to "what was hard?" |
| `docs/incidents/` | One runbook + postmortem per incident |
