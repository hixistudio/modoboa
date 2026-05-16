# PurpleToad Fork Changes

This document tracks all modifications made to the Modoboa codebase for the PurpleToad project.

## Baseline

- **Upstream:** Modoboa (public fork)
- **Fork Date:** 2026-05-16
- **Purpose:** Extend Modoboa with plan-tier awareness, quotas, and custom API endpoints for PurpleToad integration

## Planned Modifications

### 1. Plan Tier Support
- Add `plan_tier` field to User/Domain models
- Enforce domain and mailbox quotas based on plan tier

### 2. Custom API Endpoints
- `GET /api/v1/plan-usage/` — Return plan limits and current usage
- `GET /api/v1/account-quota/` — Return account-level quota data

### 3. Quota Extensions
- Extend domain quota model with custom fields
- Add storage tracking per mailbox

## Integration Notes

- Modoboa API base URL: `http://modoboa:8000/api/v1`
- Auth token: `f08124c0459b97a4398ce6d52f16821484612765`
- PurpleToad API communicates with Modoboa via REST API

## How to Stay in Sync with Upstream

1. Add upstream remote: `git remote add upstream https://github.com/modoboa/modoboa.git`
2. Fetch upstream: `git fetch upstream`
3. Rebase: `git rebase upstream/main`
4. Resolve conflicts in our modified files
5. Run Modoboa test suite to verify
