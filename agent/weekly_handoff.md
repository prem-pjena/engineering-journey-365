# 🧠 Prem's Learning Handbook — SkillVeda Internship

**Purpose:** This is a weekly journal of everything I built, fixed, and learned.  
I feed this to my mentor AI every week so it can teach me the concepts behind what I implemented.

**How to use:** After each week's work, update this file with the new section. Then paste the entire file to your mentor AI and say: *"Here's what I did this week. Teach me the concepts behind all of this."*

---

## Week 1-2: June 12-14, 2026 — Bug Fixes & Performance

### What I Built

#### 1. PDL Retry Logic
**File:** `apps/api/src/lib/pdl.ts`

**What I did:** PDL (People Data Labs) is an external API we call to search for candidates. When PDL returns errors (rate limited or server errors), the search just failed. I added retry logic that waits 1 second, tries again, waits 2 seconds, tries again, then gives up.

**Code I wrote:**
```typescript
const RETRYABLE_STATUSES = new Set([429, 500, 502, 503]);

async function pdlFetchWithRetry<T>(path, init, maxRetries = 2) {
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await pdlFetch<T>(path, init);
    } catch (err) {
      if (err instanceof HttpError && RETRYABLE_STATUSES.has(err.status)) {
        if (attempt < maxRetries) {
          const backoffMs = Math.pow(2, attempt) * 1000; // 1s, 2s
          await new Promise(r => setTimeout(r, backoffMs));
          continue;
        }
      }
      throw err;
    }
  }
}
```

**Concepts to learn:** ⬅️ Mentor AI, teach me these
- What is exponential backoff? Why 1s then 2s?
- What are HTTP status codes 429, 500, 502, 503?
- What's the difference between retryable and non-retryable errors?
- What is an API rate limit?

#### 2. Outreach Worker Interval
**File:** `apps/api/src/lib/outreachWorker.ts`

**What I did:** Changed `60 * 1000` (1 minute) to `5 * 60 * 1000` (5 minutes). The worker was checking the database for follow-up emails every 60 seconds even though follow-ups are 1-2 days apart.

**Concepts to learn:**
- What is a background worker?
- What is polling vs event-driven architecture?
- Why is checking every 60s wasteful when nothing is due?
- What is "database load" and why does it matter?

#### 3. Database Index
**File:** `supabase/migrations/20260614000001_add_outreach_sends_followup_index.sql`

**What I did:** Added a database index on the `next_followup_at` column. Without an index, the database reads every row to find what it needs (full table scan). With an index, it goes directly to the right rows.

```sql
CREATE INDEX outreach_sends_next_followup_idx 
  ON outreach_sends (next_followup_at) 
  WHERE status = 'sent';
```

**Concepts to learn:**
- What is a database index? How is it like a book's index?
- What is a full table scan?
- What's a partial index (the `WHERE status = 'sent'` part)?
- Why does an index make queries faster?

#### 4. Async Scoring
**Files:** `searches.router.ts`, `SearchResults.tsx`, `queries.ts`

**What I did:** Before my fix, when a recruiter clicked "Score candidates," the website froze for 30-60 seconds while Gemini (our AI) scored all candidates. I changed it so:
1. Clicking "Score" returns immediately (no waiting)
2. The AI scores in the background
3. The frontend checks every 3 seconds for results
4. When scores arrive, the page updates automatically

**Concepts to learn:**
- What is synchronous vs asynchronous code?
- What is a Promise? What does `await` do?
- What is polling? How is it different from WebSockets?
- What is `Promise.allSettled` vs `Promise.all`?

#### 5. Score Caching
**Files:** `candidateScorer.ts`, `searches.router.ts`, new database migration

**What I did:** Every time someone scored a search, we paid Gemini to score the same candidates again. I created a `candidate_scores` table that stores scores. Before calling Gemini, we check if we already have a score for this candidate. If yes, we reuse it for free.

**Code concept:**
```typescript
// Check cache first
const cached = await loadCachedScores(projectId, candidateIds);
const uncached = candidates.filter(c => !cached.has(c.id));

// Only call Gemini for new candidates
if (uncached.length > 0) {
  const fresh = await scoreCandidates(requirement, uncached);
}

// Save scores to cache for next time
await persistScores(searchId, allScores, projectId);
```

**Concepts to learn:**
- What is caching? Why does it save money?
- What is a cache table vs the main table?
- What is upsert (`onConflictDoUpdate`)?

---

## Week 2: June 19-21, 2026 — Candidate Side Portal

### What I Built

#### 1. Standout.work Research
I researched Standout.work (a YC-backed AI talent agent) by:
- Visiting their website and signing up with LinkedIn
- Scanning a QR code to connect on WhatsApp
- Chatting with their AI agent on WhatsApp
- Taking an AI voice call from their system
- Reading a Gemini Deep Search technical report about their architecture

**What I learned about Standout:**
- It uses `npx standout` CLI to analyze developer's actual coding skills
- Connects via WhatsApp with AI agent conversations
- AI can make voice calls to candidates
- Uses dual AI agents (one for candidate, one for company) that negotiate
- Privacy-first: company sees skills, not identity
- Viral growth via "AI Wrapped" (Spotify Wrapped for developers)

**Their tech stack:** Next.js 16, React 19, Tailwind, TypeScript, Clerk Auth, Anthropic Claude, Vercel AI SDK, LangGraph, Supabase/PostgreSQL, Prisma, OpenSearch, pg-boss

#### 2. LinkedIn Signup Page
**Files created:**
- `apps/web/src/routes/CandidateSignup.tsx` — UI page with LinkedIn + Google buttons
- `apps/web/src/routes/CandidateOnboarding.tsx` — 2-step form for role/location/salary
- `apps/web/src/routes/CandidateDashboard.tsx` — Shows profile summary
- `apps/api/src/routes/candidate.router.ts` — Backend API for profile CRUD
- `apps/web/src/lib/candidate.ts` — Frontend API client

**How LinkedIn OAuth works:**
```typescript
// This opens LinkedIn's permission screen
const { error } = await supabase.auth.signInWithOAuth({
  provider: 'linkedin_oidc',
  options: { redirectTo: '/candidate/onboarding' }
});
```

**Database table I designed:**
```sql
CREATE TABLE candidate_profiles (
  id          UUID PRIMARY KEY,
  email       TEXT UNIQUE NOT NULL,
  full_name   TEXT,
  headline    TEXT,          -- from LinkedIn
  desired_role TEXT,         -- CSM, AE, SDR, etc.
  desired_location TEXT,     -- Bangalore, Remote, etc.
  experience_years NUMERIC,
  salary_min  INTEGER,       -- in LPA
  resume_url  TEXT,
  skills      TEXT[],
  -- plus timestamps, RLS policies
);
```

**Concepts to learn:**
- What is OAuth? How does "Sign in with LinkedIn" work?
- What is a redirect URL? Why does LinkedIn need one?
- What are access tokens and refresh tokens?
- What is Row Level Security (RLS) in PostgreSQL?
- Why use UUID as primary key instead of auto-increment?
- What is a JSONB column?

#### 3. Migration Runner
**File:** `apps/api/src/db/migrate.ts`

**What I learned:** Simply creating a `.sql` file isn't enough. You have to:
1. Write the migration file
2. Add it to the `migrate.ts` runner script
3. Run the migration against the database

**Concepts to learn:**
- What is a database migration?
- Why do we need migration files instead of just running SQL directly?
- What is the migration runner pattern?

#### 4. Drizzle Schema Addition
**File:** `apps/api/src/db/schema.ts`

I added the `candidateScores` and `candidateProfiles` Drizzle table definitions to match the SQL migrations. This is how the TypeScript code knows the database structure.

**Concepts to learn:**
- What is an ORM (Object Relational Mapper)?
- Why do we need `schema.ts` when we already have SQL migrations?
- What does `pgTable` do?

---

## Current Project Structure

```
Skillveda-app-main/
├── apps/
│   ├── api/
│   │   └── src/
│   │       ├── db/
│   │       │   ├── schema.ts          ← Drizzle table definitions
│   │       │   ├── client.ts           ← Database connection
│   │       │   └── migrate.ts          ← Migration runner
│   │       ├── lib/
│   │       │   ├── pdl.ts              ← PDL API client (added retry)
│   │       │   ├── outreachWorker.ts   ← Background worker (changed interval)
│   │       │   ├── candidateScorer.ts  ← Gemini scoring (added caching)
│   │       │   ├── candidateScorer.ts  ← Also added allSettled fix
│   │       │   ├── resumeParser.ts     ← PDF resume parsing
│   │       │   └── ... 
│   │       ├── routes/
│   │       │   ├── searches.router.ts  ← Search + scoring (made async)
│   │       │   ├── candidate.router.ts ← NEW: Candidate profile API
│   │       │   └── ...
│   │       └── server.ts               ← Express server (mounted candidate routes)
│   └── web/
│       └── src/
│           ├── routes/
│           │   ├── SearchResults.tsx    ← Added async polling + progress text
│           │   ├── CandidateSignup.tsx  ← NEW: LinkedIn/Google signup
│           │   ├── CandidateOnboarding.tsx ← NEW: Preferences form
│           │   ├── CandidateDashboard.tsx  ← NEW: Dashboard
│           │   └── ...
│           ├── lib/
│           │   ├── queries.ts           ← Added refetchInterval option
│           │   ├── candidate.ts         ← NEW: Candidate API client
│           │   └── ...
│           └── App.tsx                  ← Added candidate routes
├── supabase/migrations/
│   ├── 20260614000001_*.sql            ← NEW: next_followup_at index
│   ├── 20260614000002_*.sql            ← NEW: candidate_scores table
│   └── 20260621000001_*.sql            ← NEW: candidate_profiles table
├── agent/                              ← All gitignored
│   ├── TASKS.md
│   ├── DISCOVERIES.md
│   ├── CANDIDATE_SIDE.md
│   ├── DOCUMENTATION.md
│   ├── LEARNINGS.md
│   ├── MESSAGES.md
│   ├── README.md
│   └── HANDOFF_CONTEXT.md              ← This file
├── env/                                ← Gitignored
│   ├── api.env                         ← All API credentials
│   └── web.env.local
└── .gitignore
```

---

## Week 3-4: June 25-28, 2026 — Candidate Portal Finalization

### What I Built

#### 12. Sales-Optimized Profile Editor
**File:** `apps/web/src/routes/CandidateEditProfile.tsx`

Added sales-specific fields (quota attainment %, ACV, sales cycle, methodology, notice period, work type). Backend Zod schema + handler updated. Profile strength bar with ROI messaging ("3x more intros").

#### 13. Kanban Pipeline Dashboard
**File:** `apps/web/src/routes/CandidateDashboard.tsx`

4-column Kanban board: Applied → Shortlisted → Assessment → Interview. Auto-refreshes every 30s.

#### 14. Market Value Modal & AI Agent Coming Soon
**File:** `apps/web/src/routes/CandidateDashboard.tsx`

Modal overlay showing AI-estimated salary range + coming-soon agent explainer.

#### 15. Smart Profile Suggestions
**File:** `apps/web/src/routes/CandidateDashboard.tsx`

Yellow notification bar with contextual CTAs: add quota (3x more intros), set notice period (80% filter by this), upload resume (40% better matches), etc.

#### 16. Saved Jobs (Bookmarking)
**Files:** `apps/web/src/lib/savedJobs.ts`, `apps/web/src/routes/CandidateSaved.tsx`

localStorage-based bookmarking with ♡ icon. Count in nav. Dedicated `/candidate/saved` page.

#### 17. Applied State Detection
**File:** `apps/web/src/routes/PublicJobDetail.tsx`

Fetches applications on page load, checks if jobId matches — shows "Applied" instead of "Apply Now".

#### 18. Backend Caching
**File:** `apps/api/src/routes/publicJobs.router.ts`

In-memory cache for jobs list with 60s TTL. `invalidateJobsCache()` export.

#### 19. Theme Consistency
All candidate pages converted to white/forest theme (`bg-sage-bg` / `bg-forest`).

### What's Still Pending
- LinkedIn OAuth credentials
- WhatsApp AI agent integration
- Voice call AI agent
- Public talent page
- Recruiter dashboard widget

---

## Environment Details

- **Node.js:** v22.22.3 (managed via nvm)
- **Package manager:** pnpm v10.15.0
- **Git branch:** `feature/pp/initial/bugs`
- **GitHub repo:** `https://github.com/Aastha-skill/Skillveda-app`
- **Supabase project:** `ekpgmfggwsbjpflrhykp`
- **Local URLs:** API at `http://localhost:3000`, Frontend at `http://localhost:5173`
- **Start commands:** `cd apps/api && pnpm dev` and `cd apps/web && pnpm dev`

---

## Things I Need My Mentor AI to Explain

1. How does OAuth work in detail? (access tokens, refresh tokens, scopes)
2. What is Row Level Security in Postgres? Why do I need policies?
3. How does caching work? What are different caching strategies?
4. What's the difference between `Promise.all` and `Promise.allSettled`?
5. How does a database index actually work under the hood?
6. What is polling vs WebSockets vs Server-Sent Events?
7. How do background workers work? (cron jobs, message queues)
8. What is TypeScript's type system? Why strict mode?

---

## Week 3: June 22, 2026 — Public Jobs Page & Apply Flow

### What I Built

#### 1. Public Jobs Page
**Files created:**
- `apps/web/src/routes/PublicJobs.tsx` — Job listing page at `/jobs` (no login needed)
- `apps/web/src/routes/PublicJobDetail.tsx` — Job detail page at `/jobs/:id`
- `apps/web/src/lib/publicJobs.ts` — API client for jobs

**What I built:** A browsable job board where anyone can see all published jobs. Each job card shows title, company, location, seniority level, and experience range. Clicking a job shows the full description.

**Apply flow:**
```
Anyone visits /jobs → sees all jobs ✅
    → Clicks a job → sees full JD ✅
        → Clicks "Apply Now"
            → ✅ Logged in → instant apply
            → ❌ Not logged in → redirected to signup
```

**Key decision:** No guest apply — everyone must sign up. But LinkedIn makes it fast (1 click, 5 seconds).

**Code pattern:**
```typescript
// PublicJobs.tsx — fetches and lists jobs
useEffect(() => {
  const load = async () => {
    const data = await publicJobsApi.list();
    setJobs(data);
  };
  void load();
}, []);

// PublicJobDetail.tsx — checks auth before apply
const handleApply = async () => {
  const { data: { session } } = await supabase.auth.getSession();
  if (session) {
    // Logged in → apply
    await publicJobsApi.apply(jobId, { name, email });
  } else {
    // Not logged in → redirect to signup with return URL
    navigate('/candidate/signup', { state: { returnTo: `/jobs/${jobId}` } });
  }
};
```

**Concepts to learn:**
- What is a "public" route vs authenticated route?
- What is `useEffect` and why is it used for data fetching?
- What is the difference between client-side and server-side routing?
- How does conditional rendering work in React?

#### 2. API Client Pattern
**File:** `apps/web/src/lib/publicJobs.ts`

**What I built:** A typed API client that wraps fetch calls with proper TypeScript interfaces. Shows the pattern for adding new API endpoints.

**Concepts to learn:**
- What is an API client? Why not just use fetch directly?
- What is TypeScript interface for API responses?
- What is the difference between `api.get`, `api.post`?

---

## Week 4: June 23, 2026 — Architecture Hardening (Production Readiness)

### What I Built

#### 1. Fixed Vite Proxy Rewrite Bug
**File:** `apps/web/vite.config.ts`

**Problem:** The Vite dev server proxy had `rewrite: (path) => path.replace(/^\/api/, '')` which stripped the `/api` prefix from proxied requests. But the backend Express routes all expect `/api/*` (e.g., `app.use('/api/me', ...)`). So requests through the proxy would go to `/me` on the backend, which didn't match `/api/me`.

**Why it worked anyway:** The env var `VITE_API_URL=http://localhost:3000` made the frontend bypass the proxy entirely and call `localhost:3000` directly.

**Fix:** Removed the `rewrite` line so the proxy passes paths through unchanged.

**Concepts to learn:**
- What is a dev server proxy? Why is it needed?
- What is CORS and why does the proxy help avoid it in development?

#### 2. Added Global Rate Limiting
**File:** `apps/api/src/server.ts`
**Package:** `express-rate-limit`

**Problem:** The server had NO rate limiting at all. The public job apply endpoint was completely unprotected. Anyone could write a script to submit thousands of fake applications, wasting Gemini credits and filling the database with spam.

**Fix:** Added a global rate limiter: 200 requests per minute per IP. This protects all endpoints from basic abuse.

```typescript
const globalLimiter = rateLimit({
  windowMs: 60 * 1000,  // 1 minute window
  max: 200,              // 200 requests per minute
  standardHeaders: true,
  legacyHeaders: false,
});
app.use(globalLimiter);
```

**Concepts to learn:**
- What is rate limiting? Why is it important?
- What's a good rate limit for an API?
- What is IP-based rate limiting vs user-based?

#### 3. Added Request/Correlation ID
**File:** `apps/api/src/middleware/requestLogger.ts`

**Problem:** Every log entry was isolated. If a search failed, you couldn't link the error log to the request that caused it. Debugging was like reading a book with no page numbers.

**Fix:** Each request now gets a unique ID (UUID) that appears in all log entries for that request.

```typescript
const requestId = crypto.randomUUID();
(req as any).requestId = requestId;
// Every log for this request includes: { requestId, method, path, status, durationMs }
```

**Concepts to learn:**
- What is a correlation ID? Why does it matter?
- What is distributed tracing?
- How does logging work in production vs development?

#### 4. Fixed console.error → Structured Logger
**File:** `apps/api/src/routes/publicJobs.router.ts`

**Problem:** One error handler was using `console.error()` instead of the pino logger that everything else uses.

**Fix:** Changed to `logger.error()` so all errors go to the same structured logging pipeline.

**Concepts to learn:**
- Why use structured logging (JSON) instead of console.log?
- What is pino and why is it fast?

#### 5. Added Security Headers
**File:** `apps/api/src/server.ts`
**Package:** `helmet`

**Problem:** The app sent no security headers. This made it vulnerable to clickjacking (a malicious site could embed SkillVeda in an iframe), XSS attacks, and MIME-type sniffing attacks.

**Fix:** Added `helmet()` middleware which sets 15+ security headers automatically:
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Content-Security-Policy` (restricts what scripts can run)
- And many more

```typescript
app.use(helmet());
```

**Concepts to learn:**
- What are security headers? Why do they matter?
- What is clickjacking?
- What is CSP (Content Security Policy)?
- How does HTTPS help with security?

### Architecture Issues NOT Yet Fixed (Future)

| Issue | Reason Not Fixed |
|-------|----------------|
| Webhook idempotency keys | Requires design decision on idempotency model |
| Automated migration discovery | Nice-to-have; manual approach works for now |
| Migration tracking table | Nice-to-have; current approach is idempotent with IF NOT EXISTS |


---

## Week 5: June 24, 2026 — Candidate Experience & Lead Magnet

### What I Built

#### 1. Resume Upload in Onboarding
Added Step 0 to onboarding wizard. Candidates upload PDF/DOCX resume → stored in Supabase storage → URL saved to profile.

#### 2. Job Matching on Dashboard
New endpoint `GET /api/candidate/matches` — scores candidate preferences against all published jobs. Shows matches on dashboard with color-coded percentages.

#### 3. Candidate Pool as Lead Magnet (Strategy)
Ideas to convert the candidate database into recruiter signups:
- "X candidates available" badge on public jobs page
- Recruiter dashboard widget showing match counts
- Weekly email digest to recruiters
- Public talent page at /talent
- Referral program for candidates
