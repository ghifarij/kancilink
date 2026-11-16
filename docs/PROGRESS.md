# Kancilink: progress

Status legend: ⬜ todo · 🟡 in progress · ✅ done · ⛔ blocked

Phase numbers match the master tracker (`../../PROGRESS.md`).

## Phase 0: Setup (11–14 Nov)
- ✅ `CLAUDE.md`, README, docs files written by Claude (2026-11-11)
- ✅ `docs/DECISIONS.md` pre-filled with the planning decisions (2026-11-11)
- ✅ `git init`, first commit, push to `ghifarij/kancilink` (me) (2026-11-16)
- ✅ Branch protection on `main`: ruleset `protect-main` (no deletion, no force push, pull request required, squash merge only, no bypass). Tested: a direct push is rejected (me) (2026-11-16)
- 🟡 Slice 1: skeleton + `/health` (Claude) → review quiz → merge. Pull request opened 2026-11-16

## Phase 2: Foundations (17–21 Nov)
- ⬜ Python basics (1 day) + Flask basics (1 day)
- ⬜ Linux, Git and networking lessons (in ops-drills)
- ⬜ Read the app; shortlist my 3–5 app changes

## Phase 3: Docker (22–28 Nov)
- ⬜ My Dockerfile: multi-stage, non-root user, small image
- ⬜ Explain every line of it out loud

## Phase 4: Compose (29 Nov–5 Dec)
- ⬜ My `compose.yaml`: app, Postgres, Redis, health checks, volumes, start order
- ⬜ Slice 2: create link + Postgres
- ⬜ Slice 3: redirect + Redis cache, Postgres fallback
- ⬜ My 3–5 app changes
- ⬜ A fresh clone runs with one `docker compose up`

## Phase 5: CI/CD (6–12 Dec)
- ⬜ My GitHub Actions workflow: lint, test, Trivy scan, build, push to GHCR with `sha-<commit>` tags
- ⬜ CI required by branch protection
- ⬜ Slice 4: click stats
- ⬜ Slice 5: API token check

## Phase 6: nginx (13–19 Dec)
- ⬜ My nginx config: reverse proxy, rate limiting on link creation, access logs, error page
- ⬜ Incident 1: Redis down (runbook + postmortem)

## Phase 7: Monitoring (20–26 Dec), first to cut
- ⬜ Slice 6: `/metrics`
- ⬜ My Prometheus + Grafana config: traffic, errors, latency
- ⬜ Incident 2: Postgres down (runbook + postmortem)

## Phase 8: Server rehearsal (27 Dec–2 Jan)
- ⬜ Multipass Ubuntu VM: deploy user, SSH keys only, ufw, unattended upgrades (written as a runbook)
- ⬜ AWS sign-up, check Free plan terms, $1 budget alert, one t3.small x86 EC2 + security group
- ⬜ My deploy workflow over SSH (`docker compose pull && up -d`)

## Phase 9: Go live (3–9 Jan)
- ⬜ Cloudflare DNS for `s.ghifarij.my.id`, Origin Certificate on nginx, SSL mode "Full (strict)"
- ⬜ Rollback workflow (`workflow_dispatch` with an older tag)
- ⬜ Incident 3: bad release + rollback (runbook + postmortem)
- ⬜ README final pass
