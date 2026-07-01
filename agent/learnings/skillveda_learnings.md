# 🏢 SkillVeda — Office Work to Concepts Mapping

**Purpose:** Every task I build at SkillVeda gets mapped to engineering fundamentals. This helps me explain my work in interviews and connect office experience to learning.

---

## Week 1-2: Bug Fixes & Performance

### 1. PDL Retry Logic

| Aspect | Detail |
|--------|--------|
| **What I built** | Exponential backoff retry for PDL API calls |
| **Python equivalent** | `while` loop + `try/except` + `time.sleep()` |
| **Concepts** | HTTP status codes, rate limiting, exponential backoff, idempotency |
| **Why it matters** | Every production system needs retry logic. FAANG interviews ask about resilience patterns. |

### 2. Outreach Worker Interval

| Aspect | Detail |
|--------|--------|
| **What I built** | Changed polling interval from 1min → 5min |
| **Python equivalent** | `while` loop + `time.sleep()`, cron jobs |
| **Concepts** | Background workers, polling vs event-driven, database load optimization |
| **Why it matters** | System design interviews test your understanding of async processing patterns. |

### 3. Database Index

| Aspect | Detail |
|--------|--------|
| **What I built** | Partial index on `next_followup_at WHERE status = 'sent'` |
| **Python equivalent** | DSA: Binary search vs linear search |
| **Concepts** | Full table scan, B-tree index, partial index, query performance |
| **Why it matters** | DB indexing is a core system design concept. Every backend interview covers this. |

### 4. Async Scoring

| Aspect | Detail |
|--------|--------|
| **What I built** | Made Gemini scoring async with frontend polling |
| **Python equivalent** | `asyncio`, `await`, `Promise.allSettled` |
| **Concepts** | Synchronous vs asynchronous, Promises, polling, WebSockets vs polling |
| **Why it matters** | Async patterns are central to modern backend architecture and AI systems. |

### 5. Score Caching

| Aspect | Detail |
|--------|--------|
| **What I built** | `candidate_scores` cache table to avoid redundant Gemini calls |
| **Python equivalent** | Dictionary cache, `functools.lru_cache` |
| **Concepts** | Caching strategies (write-through, write-behind), cache invalidation, upsert |
| **Why it matters** | Caching is one of the most frequently asked system design topics. |

---

## Week 2: Candidate Side Portal

### 6. LinkedIn OAuth

| Aspect | Detail |
|--------|--------|
| **What I built** | Sign-in with LinkedIn using Supabase OAuth |
| **Concepts** | OAuth 2.0 flow, access tokens, refresh tokens, redirect URIs, scopes |
| **Python equivalent** | `authlib`, `requests-oauthlib` in FastAPI |
| **Why it matters** | OAuth is everywhere. Every interview expects you to explain it. |

### 7. Candidate Profiles CRUD

| Aspect | Detail |
|--------|--------|
| **What I built** | Full CRUD API with PostgreSQL, Drizzle ORM, RLS policies |
| **Concepts** | REST API design, CRUD, Row Level Security, UUID vs auto-increment, JSONB |
| **Python equivalent** | FastAPI + SQLAlchemy + PostgreSQL |
| **Why it matters** | CRUD is the foundation of 90% of backend work. |

### 8. Migration Runner

| Aspect | Detail |
|--------|--------|
| **What I built** | SQL migration files + runner script in migrate.ts |
| **Concepts** | Database migrations, schema versioning, rollbacks |
| **Python equivalent** | Alembic (FastAPI migrations) |
| **Why it matters** | Migration patterns are universal across all backend stacks. |

---

## Week 3-4: Candidate Portal Finalization + Architecture Hardening

### 9. Public Jobs Page & Apply Flow

| Aspect | Detail |
|--------|--------|
| **What I built** | Public job listing page at `/jobs` with apply flow (signup gate for non-logged-in users) |
| **Concepts** | Public vs authenticated routes, client-side routing, conditional rendering, auth gating patterns |
| **Python equivalent** | FastAPI route guards, dependency injection for auth, middleware for session checking |
| **Why it matters** | Auth gating is a universal pattern. Every app has public pages + protected pages. |

### 10. Rate Limiting

| Aspect | Detail |
|--------|--------|
| **What I built** | Global rate limiter (200 req/min per IP) using `express-rate-limit` |
| **Python equivalent** | `slowapi` or FastAPI middleware with Redis for distributed rate limiting |
| **Concepts** | Rate limiting algorithms (token bucket, leaky bucket), IP-based vs user-based limits, DDoS protection |
| **Why it matters** | Rate limiting is one of the most common system design interview topics. Every production API needs it. |

### 11. Correlation ID / Request Logging

| Aspect | Detail |
|--------|--------|
| **What I built** | UUID per request attached to all log entries for traceability |
| **Python equivalent** | `structlog` or `loguru` with request ID middleware in FastAPI |
| **Concepts** | Distributed tracing, correlation IDs, structured logging, observability |
| **Why it matters** | Debugging in production without tracing is impossible. Observability is a core SRE skill. |

### 12. Kanban Pipeline Dashboard

| Aspect | Detail |
|--------|--------|
| **What I built** | 4-column Kanban board (Applied → Shortlisted → Assessment → Interview) with auto-refresh |
| **Concepts** | State management, polling for updates, visual pipeline design |
| **Python equivalent** | FastAPI + WebSocket for real-time updates instead of polling |
| **Why it matters** | Real-time UI patterns (polling vs WebSockets) are a common system design tradeoff. |

### 13. In-Memory Backend Caching

| Aspect | Detail |
|--------|--------|
| **What I built** | In-memory cache for jobs list with 60s TTL and invalidation export |
| **Python equivalent** | `functools.lru_cache` or `cachetools` with TTL in FastAPI |
| **Concepts** | Cache-aside pattern, TTL-based invalidation, write-through vs write-behind, stale data tradeoffs |
| **Why it matters** | Caching is the #1 performance optimization in backend systems. |

### 14. Saved Jobs (localStorage Bookmarking)

| Aspect | Detail |
|--------|--------|
| **What I built** | Bookmarking with ♡ icon using localStorage, persisted across sessions |
| **Concepts** | Client-side storage (localStorage vs sessionStorage vs cookies), offline-first patterns |
| **Python equivalent** | Server-side saved jobs with PostgreSQL table for cross-device sync |
| **Why it matters** | Understanding storage tradeoffs (client vs server) is fundamental to web architecture. |

### 15. Vite Proxy Rewrite Bug Fix

| Aspect | Detail |
|--------|--------|
| **What I built** | Fixed proxy path rewrite that was stripping `/api` prefix |
| **Concepts** | Dev server proxy, CORS, reverse proxy patterns, how API gateways work |
| **Why it matters** | Understanding how proxies work is essential for deployment and microservices architecture. |

### 16. Applied State Detection

| Aspect | Detail |
|--------|--------|
| **What I built** | Fetch applications on page load, check if jobId matches → show "Applied" instead of "Apply Now" |
| **Concepts** | Optimistic UI, state derivation from data, idempotent operations |
| **Why it matters** | Preventing duplicate actions (double-apply) is a universal backend concern. |

---

## Concepts to Study Next (Updated Priority Order)

1. **OAuth 2.0** — full flow: access tokens, refresh tokens, scopes, redirect URIs
2. **Rate Limiting** — token bucket, leaky bucket, sliding window, distributed rate limiting
3. **Caching Strategies** — cache-aside, write-through, write-behind, TTL, invalidation
4. **Async Programming** — Promises, async/await, event loop, `Promise.all` vs `allSettled`
5. **Database Indexing** — B-tree, partial, composite, GIN/GiST for vectors
6. **Polling vs WebSockets vs SSE** — when to use which, tradeoffs
7. **Background Workers** — cron, message queues, event-driven architecture
8. **Correlation IDs & Observability** — structured logging, distributed tracing
9. **RLS in PostgreSQL** — row-level security policies, multi-tenancy
10. **TypeScript → Python Translation** — interfaces ↔ Pydantic, ORM ↔ SQLAlchemy
