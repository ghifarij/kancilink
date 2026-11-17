# Kancilink: decisions

Every decision and my reason for it. This is my answer to "why did you use X?"
Change a decision only on purpose: add a new ID that says which one it revises.

Decisions K1–K17 were made in the planning sessions on 2026-11-11.

## Scope

| ID | Decision | Why | Rejected |
|---|---|---|---|
| K1 | **One DevOps project** (Kancilink) that covers build, ship, run and break | Starting from zero DevOps, one project I can fully defend beats two I can't | Two projects (app + a Kubernetes reliability lab) |
| K2 | **One Flask service** that both creates links and redirects | Less to wire, so I can explain every part | 3 services (api, redirector, worker) |
| K3 | **No Kubernetes, k6, SLOs or 12 postmortems** | Too much to learn and defend before January. Kubernetes is taught in the program | The original Reliability Lab plan |
| K4 | **Only tools I built and drilled go on my CV** | The interview tests live whatever the portfolio shows | Listing tools I only saw |

## App

| ID | Decision | Why | Rejected |
|---|---|---|---|
| K5 | **Python + Flask** (gunicorn in production) | I want to learn a new language; Python is common in DevOps | TypeScript/Express (I already know it) |
| K6 | **Postgres** stores the links | Durable, relational, and what I'd use in a real backend | SQLite (a file inside the container, lost on rebuild) |
| K7 | **Redis cache first, Postgres fallback** | A link is written once and read many times. Gives a real failure demo: Redis dies, the app slows but stays up | No cache |
| K8 | **API token for creating links; only http/https targets; robots.txt blocks indexing** | Stops strangers using it to spread spam links | Open link creation |
| K9 | **Claude writes the app in 6 small pull requests; I pass a review quiz before each merge** | I must understand code I didn't write, as if I'd reviewed a teammate's PR | One big scaffold |

## Delivery and operations

| ID | Decision | Why | Rejected |
|---|---|---|---|
| K10 | **Docker multi-stage image** | Same image on laptop, CI and server; multi-stage keeps it small | Running Python straight on the server |
| K11 | **Docker Compose** for the whole stack, locally and on the server | One file, one command, same everywhere | Separate `docker run` commands |
| K12 | **nginx** in front of the app | Single public entry point (app, DB and Grafana stay private), rate limiting, access logs, clean error page when the app is down | Exposing gunicorn directly |
| K13 | **GitHub Actions + Trivy + GHCR, image tag `sha-<commit>`** | Every merge is tested, scanned and published. A unique tag per commit makes rollback a redeploy of an older tag | `latest` tag only (can't roll back) |
| K14 | **Prometheus + Grafana** (first to cut if late) | Incidents get measured, not guessed | No monitoring |

## Hosting

| ID | Decision | Why | Rejected |
|---|---|---|---|
| K15 | **AWS only for deployment: one EC2 VM (x86, t3.small) + security group.** Postgres and Redis run as containers on it. Free plan credits; $1 budget alert | A plain Linux server makes me do the work the interview tests: SSH, firewall, nginx, deploy. A small, true claim ("one EC2 instance"). Fallbacks: Oracle Always Free, then Hetzner | Railway, Render, Fly.io: platforms that hide the server; no reliable free 24/7 tier. RDS/ElastiCache: cost, and claims I couldn't defend |
| K16 | **x86 server** | GitHub's default CI runners build x86 images, so nothing extra to learn (an image built for one CPU family fails on the other with "exec format error") | ARM (Oracle free tier, my Mac) |
| K17 | **Cloudflare proxy + Origin Certificate on nginx, SSL "Full (strict)"; domain `s.ghifarij.my.id`** | My domain's DNS is already on Cloudflare; traffic is encrypted end to end | Let's Encrypt/certbot (more moving parts); plain HTTP |

## Process

| ID | Decision | Why | Rejected |
|---|---|---|---|
| K18 | **First commits split by author** (2026-11-16): Claude's docs in `46a85b8` (with the `Co-Authored-By` trailer), my `.gitignore` in `1ac17a1` (no trailer) | I write the `.gitignore` myself, so my first commit is done by me | One first commit holding both |
