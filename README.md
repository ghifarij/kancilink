# Kancilink

A URL shortener that I containerized, automated, deployed and broke on purpose to learn how it fails.

> **Status:** in progress (started November 2026). This README grows as each part is built.

## What it does

- Create a short link (`POST /links`, API token required)
- Redirect (`GET /<code>`): Redis cache first, Postgres fallback
- Click stats, health check (`/health`), metrics (`/metrics`)

## Stack

| Tool | Why it's here |
|---|---|
| Python (Flask + gunicorn) | The service. A new language for me |
| Postgres | Stores the links: the source of truth |
| Redis | Links are written once and read many times, so lookups are cached. Redis going down is the main failure demo |
| Docker (multi-stage) | One image that runs the same on my laptop, in CI and on the server |
| Docker Compose | The whole stack starts with one command |
| nginx | Single public entry point, rate limiting, access logs, clean error page |
| GitHub Actions + Trivy + GHCR | Lint, test, scan, build and publish a versioned image on every merge |
| Prometheus + Grafana | Traffic, error and latency graphs, so incidents are measured |
| AWS EC2 + Cloudflare | One Linux server, HTTPS through Cloudflare |

## Run it locally

So far the app is a skeleton with one endpoint, `/health`. It needs Python 3.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

pytest                              # run the tests
flask --app app run --port 5001     # development server
curl http://127.0.0.1:5001/health   # {"status":"ok"}
```

Port 5001 because macOS uses 5000 for AirPlay Receiver.

## How this was built

I used Claude (AI) as a coding partner. The split is strict:

| Part | Written by |
|---|---|
| App code (Python/Flask) and app tests | Claude, reviewed by me. I passed a review quiz on every pull request before merging |
| 3–5 app changes (listed in `docs/DECISIONS.md`) | Me |
| Dockerfile, Compose, nginx, CI/CD workflows, Makefile, server setup, monitoring config | **Me.** Claude explained concepts and reviewed my work, but did not write these files |
| Decisions, incident runbooks and postmortems | Me |

Commits containing Claude's code end with `Co-Authored-By: Claude`, and my commits don't. To see the split: `git log --format='%h %s%n%b' | grep -B1 Co-Authored-By`.

## Docs

- [Decisions](docs/DECISIONS.md): every choice and why
- [Learning log](docs/LEARNING.md): what broke and how I fixed it
- [Incidents](docs/incidents/): runbooks and postmortems
- [Progress](docs/PROGRESS.md)
