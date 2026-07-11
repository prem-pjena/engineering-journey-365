# 📋 Day Syllabus — Live Tracker

**Purpose:** Tracks what was actually taught each day. Always check this before generating a prompt. Never assume. Never guess.

---

## ✅ Completed Days

| Day | Date | Topics Covered | DSA Problems | Total DSA |
|-----|------|---------------|-------------|-----------|
| 1 | Jun 22 | Variables, data types, input(), print(), arithmetic, calculator | Algorithm, O(1), O(n) | 0 |
| 2 | Jun 22 | Comparisons, if/elif/else, booleans, login checker | Decision trees | 0 |
| 3 | Jun 24 | Logical operators (and/or/not), nested conditions, login validation | — | 0 |
| 4 | Jun 25 | while loops, break, continue, retry logic, menu-driven app | — | 0 |
| 5 | Jun 30 | for loops, range(), string iteration, accumulator pattern | — | 0 |
| 6 | Jun 30 | Functions (def, params, return, default params) | — | 0 |
| 7 | Jul 1 | Lists (indexing, append, pop, remove, insert, len, iteration, sum manually, max manually, Todo app) | — | 0 |
| 8 | Jul 1 | List slicing, list comprehensions, membership (in/not in), dicts (get, keys, values, items, update), list of dicts, linear search, Contact Book | Linear Search (O(n), O(1)) | 0 |
| 9 | Jul 4 | Exception handling (try/except/else/finally, ValueError, ZeroDivisionError, KeyError), *args, **kwargs, lambda, map(), filter(), program organization, dispatch table, Calculator 2.0 | Big O review (O(1), O(n), O(n²)) | 0 |
| 10 | Jul 11 | File I/O (open, read, write, with, readlines, append, modes, FileNotFoundError), Sets (add, remove, discard, union, intersection, membership), Two Sum (brute O(n²) + optimized O(n) with hash map) | Two Sum (LeetCode #1) | 1 |

---

## 🔄 Current Day

| Day | Date | Status | Topics | DSA |
|-----|------|--------|--------|-----|
| 11 | Jul 11 | 🔴 IN PROGRESS | Tuples, enumerate(), zip(), type conversions | Contains Duplicate, Valid Anagram |

---

## 📅 Upcoming (Flexible)

| Day | Planned Topics | DSA |
|-----|---------------|-----|
| 11 | Tuples, Set operations, type conversions + enumerate(), zip() | Arrays: Contains Duplicate, Valid Anagram |
| 12 | String methods (.split, .join, .strip, .replace, .find) + JSON module (dumps/loads) + dict/set comprehensions + **Generators (yield, generator expressions, lazy evaluation)** | Strings: Valid Palindrome, Reverse String |
| 13 | **OOP** — Classes, objects, `__init__`, self, methods, `__str__` | Arrays: Two Sum II |
| 14 | **OOP** — Inheritance, `super()`, dunder methods, `@property`, staticmethod, classmethod + **Context Managers (`__enter__`, `__exit__`, `with` statement, contextlib)** | Trees: Max Depth of Binary Tree |
| 15 | **OOP mini-project** (Bank Account / Library system) | Trees: Invert Tree |
| 16 | **Modules & imports** — `import`, `from`, `as`, `__init__.py`, `if __name__ == "__main__"`, package structure | Two Pointers |
| 17 | **Modern env: uv** (instead of pip/venv), pyproject.toml, lockfiles + **Type hints** (`def func(x: int) -> str:`) + **Env vars** (`os.getenv`, `python-dotenv`) + **Async Concurrency** (asyncio, async/await, asyncio.gather, event loop, I/O vs CPU-bound) | Valid Parentheses |
| 18 | **FastAPI starts** — Routes, Pydantic v2, async endpoints + **ORM (SQLModel/SQLAlchemy)** + **Alembic migrations** + pgvector setup | Min Stack |
| 19 | FastAPI — CRUD, query/body params, error handling + **Rate Limiting** (Redis sliding window, FastAPI dependency, 429 responses) | Container With Most Water |
| 20 | FastAPI — Dependency injection, middleware, file upload + **API Security (JWT, OAuth2)** + **Testing (pytest, openai-responses mocking)** | 3Sum |

## 📅 Month 2 Additions (from Deep Research audit)

These topics must be inserted into the existing Month 2 plan:

| Insert After | New Topic | Priority |
|-------------|-----------|----------|
| Naive RAG intro | **Semantic Chunking** — statistical rolling-window cosine distance, agentic chunking for tables/headers | 🔴 |
| Prompt Engineering | **Constrained Decoding** — Native Structured Outputs, Pydantic response_format, no regex parsing | 🔴 |
| LangGraph intro | **Graph State Persistence** — PostgresSaver, checkpointer, thread_id, resume across restarts | 🔴 |
| LangGraph intro | **Topological Sorting + Deadlock Prevention** — cycles, recursion_limit, Kahn's Algorithm | 🔴 |
| Before deployment | **MCP Integration** — MCP server exposing DB, tool discovery, JSON-RPC transport | 🔴 |
| UI/Deployment | **SSE + Token Streaming** — StreamingResponse, async generators, real-time output | 🟡 |
| Alongside Ragas | **Observability** — LangSmith tracing, execution tree debugging, token cost tracking | 🟡 |
| DSA Month 1 | **Vector Math** — Cosine similarity from scratch with NumPy, L2 vs L1 vs Cosine | 🟡 |
| DSA Month 2 | **Graph Traversal Algorithms** — BFS, DFS, topological sort (Kahn's Algorithm) | 🔴 |

---

## ⚠️ Rules for Updating

1. After each day completes, append the actual topics covered to the Completed table.
2. Update Current Day status to ✅ COMPLETED.
3. Add the next day to Current Day with 🔴 IN PROGRESS.
4. If topics shift (faster or slower), update Upcoming table accordingly.
5. Never plan more than 3 days ahead — let actual pace dictate.
