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
| 11 | Jul 14 | 🔴 IN PROGRESS | OOP: classes, inheritance, dunder, @property, @staticmethod, @classmethod | Two Sum, Valid Anagram |

---

## 📅 Upcoming (Market-Validated — All Concepts, No Skipping)

### Phase 1: Python Completion + LLM APIs (Days 11-17)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 11 | OOP: classes, inheritance, dunder, @property, @staticmethod, @classmethod | Build mock VectorStore class | Two Sum |
| 12 | Context Managers, Modules, __init__.py | Safe File I/O Manager + Package | Valid Anagram |
| 13 | Async: asyncio, event loop, gather + **FastAPI intro** | Build first FastAPI endpoint | Group Anagrams |
| 14 | Generators (yield), Tuples, enumerate, zip | Streaming token generator | Top K Frequent |
| 15 | String methods, JSON module | Parse nested JSON LLM outputs | Product of Array |
| 16 | LLM APIs: OpenAI/Gemini, temperature, tokens, streaming | Chat + streaming response | Valid Palindrome |
| 17 | Prompt Engineering: few-shot, CoT, system prompts | Test personas | 3Sum |

### Phase 2: LangChain + RAG Core (Days 18-24)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 18 | LangChain LCEL, Prompt Templates | Rewrite Day 16 with LangChain | Container With Most Water |
| 19 | with_structured_output, Pydantic schemas | Structured JSON entity extraction | Longest Substring |
| 20 | Document Loaders, Text Splitters, **Semantic Chunking** | Parse PDF by semantic boundaries | Valid Parentheses |
| 21 | Vector DBs, Embeddings, ChromaDB | Store chunks + similarity search | Binary Search |
| 22 | **Naive RAG**: chunk → embed → store → retrieve → generate | End-to-end RAG script | Search 2D Matrix |
| 23 | **SQL + pgvector basics**: SELECT, INSERT, JOINs, vector columns | Store embeddings in PostgreSQL | Reverse Linked List |
| 24 | **Parent-Child Chunking + Cross-Encoder Reranking** | Rerank top-20 → top-3 with BGE | Merge Two Sorted |

### Phase 3: Advanced RAG + Evaluation + Project 1 (Days 25-31)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 25 | **Hybrid Search**: BM25 + Dense, pgvector HNSW vs IVFFlat | Implement hybrid search + index tuning | Reorder List |
| 26 | **Corrective RAG (CRAG)** + **Adaptive RAG** | Evaluator → web fallback + router | Max Depth Tree |
| 27 | **Conversational RAG + Agentic RAG** | Chat history + agent re-queries | Same Tree |
| 28 | **LangSmith + Ragas Eval**: Faithfulness, Context Precision, Answer Relevancy | Golden dataset + eval pipeline | Invert Tree |
| 29 | **PROJECT 1**: Multi-Tenant RAG System (FastAPI + pgvector + LangGraph + MCP) | Build core features | LCA of BST |
| 30 | Project 1: Docker containerize + Cross-encoder + Hybrid Search | Complete features + eval | Level Order Traversal |
| 31 | **Project 1 DONE**: Deploy to AWS ECS + Ragas eval + **APPLY BLITZ** | Wellfound + YC apps | Review all |

### Phase 4: LangGraph Mastery + MCP (Days 32-39)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 32 | LangGraph: StateGraph, Nodes, Edges, State | Linear 3-node state machine | Course Schedule |
| 33 | LangGraph: Reducers, add_messages, Conditional Routing | Chatbot with memory + router | Climbing Stairs |
| 34 | LangGraph: Checkpointing, Human-in-the-loop | Approval interrupt before tools | Coin Change |
| 35 | LangGraph: Multi-agent Supervisor Pattern | Supervisor → 2 workers | Longest Increasing Subseq |
| 36 | LangSmith Tracing for LangGraph | Instrument multi-agent | Word Break |
| 37 | MCP: Host/Client/Server, stdio transport | Python MCP server with tools | Merge Intervals |
| 38 | MCP: HTTP SSE, JSON-RPC 2.0, Tools vs Resources vs Prompts | DB schema as MCP Resource | Insert Interval |
| 39 | **LangGraph + MCP Integration** | Agent discovers MCP tools | Non-overlapping Intervals |

### Phase 5: Full-Stack + Production Patterns (Days 40-46)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 40 | FastAPI Deep Dive: error handling, middleware, streaming, background tasks | Production FastAPI app | Rotate Image |
| 41 | **Next.js + TypeScript basics** | Build chat UI component | Spiral Matrix |
| 42 | Connect Next.js UI → FastAPI backend (streaming) | End-to-end chat app | Number of 1 Bits |
| 43 | Docker compose: Agent + pgvector + MCP Server + Next.js | Multi-container orchestration | Counting Bits |
| 44 | **AWS ECS**: Deploy full stack (Fargate + RDS + Load Balancer) | Cloud deployment | Missing Number |
| 45 | **GitHub Actions CI/CD**: Auto-test, auto-eval, auto-deploy | Push → test → deploy pipeline | 3Sum review |
| 46 | Cost tracking + Prompt versioning + A/B testing | Metadata wrapper + toggle | Min Window Substring |

### Phase 6: System Design + Interview Prep (Days 47-53)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 47 | System Design: RAG at scale, semantic caching (Redis), query routing | 1M QPD architecture | Find Min Rotated review |
| 48 | System Design: Multi-tenant, latency optimization, LLM Gateway | Gateway design | Merge k Sorted Lists |
| 49 | ML Concepts: bias-variance, precision/recall/F1, cross-validation | Metrics calculator | Serialize/Deserialize Tree |
| 50 | NLP Concepts: BPE/WordPiece, BERT vs GPT, Transformer QKV | tiktoken + attention viz | Alien Dictionary |
| 51 | DSA Mock + Portfolio Review | Polish GitHub | Word Search |
| 52 | System Design Mock + Behavioral | Termination narrative + why AI | LCS |
| 53 | Live Coding Mock (FastAPI + LangGraph) | Build mini agent under time | Word Ladder |

### Phase 7: Project 2 + Apply FT (Days 54-60)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 54 | **PROJECT 2**: Multi-Agent MCP Orchestrator (FastAPI + LangGraph + MCP + Next.js) | Build core | Trapping Rain Water |
| 55 | Project 2: Docker + GitHub Actions + AWS ECS | CI/CD pipeline | Largest Rectangle |
| 56 | **Project 2 DONE**: Ragas eval + Deploy + README | Production-grade | Review patterns |
| 57 | **APPLY BLITZ**: Wellfound (20) + YC (10) + LinkedIn DMs (10) | Personalized messages | Review weak areas |
| 58 | Follow-ups + Mock interviews | Respond to callbacks | Targeted DSA |
| 59 | Buffer / Offer evaluation | Compare offers, negotiate | Rest |
| 60 | **🎯 ₹10-12 LPA OFFER** | Celebrate + plan next | — |


---

## ⚠️ Rules for Updating

1. After each day completes, append the actual topics covered to the Completed table.
2. Update Current Day status to ✅ COMPLETED.
3. Add the next day to Current Day with 🔴 IN PROGRESS.
4. If topics shift (faster or slower), update Upcoming table accordingly.
5. Never plan more than 3 days ahead — let actual pace dictate.
