# PurpleToad Fork Changes

This document tracks all modifications made to the Modoboa codebase for the PurpleToad project.

## Baseline

- **Upstream:** Modoboa (public fork)
- **Fork Date:** 2026-05-16
- **Purpose:** Extend Modoboa with plan-tier awareness, quotas, and custom API endpoints for PurpleToad integration
- **Current Commit:** `44540b6a1` — "feat: add development Docker configuration and core test project scaffolding"
- **Docker Image:** `python:3.12-alpine` base, builds from `docker/Dockerfile.dev`
- **API Base:** `https://localhost:8080/api/v1/`
- **Auth Token:** `f08124c0459b97a4398ce6d52f16821484612765`

## Baseline Verification (2026-05-16)

- [x] Container builds successfully from `docker/Dockerfile.dev`
- [x] Container starts with `docker compose up -d modoboa`
- [x] Port mapping `8080:8000` active
- [x] HTTPS server responds (self-signed cert via `runserver_plus`)
- [ ] API `/api/v1/core/` returns 500 — needs database initialization (expected for dev setup)

## Changes Made

### 1. ALLOWED_HOSTS
- Expanded `ALLOWED_HOSTS` in `test_project/test_project/settings.py` to include Docker network IPs (`172.20.0.10`–`172.20.0.20`) and service names (`api`, `api-unsecured`, `modoboa`) for inter-service communication.

## Integration Notes

- Modoboa API base URL: `https://modoboa:8000/api/v1`
- Auth token: `f08124c0459b97a4398ce6d52f16821484612765`
- PurpleToad API communicates with Modoboa via REST API

## How to Stay in Sync with Upstream

1. Add upstream remote: `git remote add upstream https://github.com/modoboa/modoboa.git`
2. Fetch upstream: `git fetch upstream`
3. Rebase: `git rebase upstream/main`
4. Resolve conflicts in our modified files
5. Run Modoboa test suite to verify
