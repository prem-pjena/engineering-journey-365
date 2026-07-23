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
| 11 | Jul 14-21 | **OOP: classes, objects, __init__, self, object attributes, instance methods, inheritance, method overriding, super(), @staticmethod, @classmethod. Built VectorStore** ⏳ Pending: @property, dunder, Mini OOP Project | Two Sum | 1 |
| 12 | Jul 21-23 | **Terminal Basics** (pwd, ls, cd, mkdir, touch) + **Git** (init, status, add, commit, log, HEAD) + **Context Managers** (basic with, __enter__, __exit__) + **Modules/Packages** (import, __init__.py) + **venv/pip** | Two Sum (review) + Valid Anagram (LeetCode #242) | 2 |

---

## 🔄 Current Day

| Day | Date | Status | Topics | DSA |
|-----|------|--------|--------|-----|
| 13 | Jul 23 | 🔴 IN PROGRESS | pip/venv + HTTP Protocol + Type Hinting + FastAPI intro | Contains Duplicate + Valid Anagram (review) |

---

## 📅 Upcoming (v4 — Final Audit Optimized)

### Phase 1: API & Async Core (Days 13-22)
| Day | Morning | Afternoon | DSA (30 min only) |
|-----|---------|-----------|-----------------------------------|
| 13 | **pip/venv** + **HTTP Protocol** + **Type Hinting** + **FastAPI intro** | Setup venv. Build strictly-typed GET/POST endpoint | Contains Duplicate #217 |
| 14 | Generators, Tuples, enumerate, zip | Custom text stream simulator | Valid Anagram #242 (review) |
| 15 | Markdown + regex/JSON + Defensive Parsing | Error-resilient JSON parser from markdown | Intersection of Two Arrays #349 |
| 16 | .env + LLM APIs (tokens, logits, softmax, streaming) | Multi-turn Chat CLI with streaming | First Unique Character #387 |
| 17 | **Asyncio deep dive** + Prompt Engineering | Async Chat CLI with concurrent API calls | Range Sum Query #303 |
| 18 | Pydantic + FastAPI SSE + Generative Parameters | Streaming endpoint with token controls | Binary Search #704 |
| 19 | 🔁 REVIEW DAY | 🔁 REVIEW DAY | 🔁 REVIEW DAY |
| 20 | LangChain (PromptTemplate, LCEL, loaders, splitters) | Document Loaders + Text Splitter | Search Insert Position #35 |
| 21 | Basic RAG (chunk → embed → retrieve → generate) | Single-hop Q&A over local doc | First Bad Version #278 |
| 22 | SQL + ACID + sqlite3 + pgvector intro | SQLite database. Document metadata queries | Valid Parentheses #20 |

### Phase 2: RAG & Orchestration (Days 23-32)
| Day | Morning | Afternoon | DSA (30 min only) |
|-----|---------|-----------|-----------------------------------|
| 23 | LangGraph (StateGraph, Nodes, Edges, Reducers) | Build deterministic LangGraph agent | Longest Common Prefix #14 |
| 24 | Docker + Hybrid Search (BM25 + RRF) + pgvector | Run pgvector. BM25 + dense + RRF | Index of Occurrence #28 |
| 25 | Advanced LangGraph (conditional, cycles, checkpointing) | Weather agent with retry + PostgresSaver | Majority Element #169 |
| 26-32 | LangGraph + pgvector + LangSmith + WebSockets + A2A | Build + evaluate RAG agent, stream execution | Trees + Graphs (see study_plan.md) |

### Phase 3: MCP & Integration (Days 34-40)
| Day | Morning | Afternoon | DSA (30 min only) |
|-----|---------|-----------|-----------------------------------|
| 34-36 | MCP Theory + Advanced + LangGraph Integration | Build MCP server, connect to agent | Intervals + Heaps |
| 37-39 | FastAPI Advanced + Redis + Docker Compose | Production-grade stack | Graphs + Topological Sort |
| 40 | 🔁 REVIEW DAY | 🔁 REVIEW DAY | 🔁 REVIEW DAY |

### Phase 4: MVP Project 1 — Voice/Chat Agent Backend (Days 41-50)
| Day | Morning | Afternoon | DSA (30 min only) |
|-----|---------|-----------|-----------------------------------|
| 41-46 | MCP Server + LangGraph Agent + Streaming + Tests + Deploy | Enterprise tool endpoints, WebSocket streaming | Design + Caching problems |
| 47 | 🔁 REVIEW DAY | 🔁 REVIEW DAY | 🔁 REVIEW DAY |
| 48-50 | Polish + Loom Demo + Apply Batch 1 | Proof of Work to Top 10 companies | Tries + DP + Backtracking |

### Phase 5: MVP Project 2 + Apply Blitz (Days 51-60)
| Day | Morning | Afternoon | DSA (30 min only) |
|-----|---------|-----------|-----------------------------------|
| 51-53 | Financial Data Analyst Agent + SQL Agent + Frontend | LangGraph + PostgreSQL + WebSocket streaming | Heap + Design problems |
| 54 | 🔁 REVIEW DAY | 🔁 REVIEW DAY | 🔁 REVIEW DAY |
| 55-56 | Polish + Loom + Apply Batch 2 | Both projects live | No new DSA |
| 57-58 | Mock Interviews (Verbal + Pair + System Design + Behavioral) | Practice rounds | No new DSA |
| 59-60 | Apply Batch 3 + Final Review | Close loops | 🔁 FINAL REVIEW |

### Phase 4: Advanced DSA & Enterprise RAG Architectures (Days 32-39)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 32 | **CRAG + Adaptive RAG + RAGFlow DeepDoc** for enterprise docs | Evaluator + layout-aware parsing | Course Schedule |
| 33 | **Conversational + Agentic RAG**. Study: NirDiamant/rag_techniques | Chat history + agent re-queries | Climbing Stairs |
| 34 | **Agentic RAG + Cross-Session Memory**: Mem0 + Graphiti. Study: NirDiamant/Agent_Memory_Techniques | Agent rewrites queries + integrate Mem0 | Coin Change |
| 35 | **Eval + Advanced Prompting**: LLM-as-a-judge, Ragas, AIBOM. DSPy, Tree of Thoughts, loss functions (cross-entropy, contrastive) | Build auto-eval + compiled prompts | Longest Increasing Subsequence |
| 36 | **PROJECT 1 BUILD**: Multi-Tenant Enterprise Knowledge Agent (continued) | FastAPI + pgvector RLS + LangGraph + Cross-encoder | LRU Cache |
| 37 | **PROJECT 1**: Docker + AWS ECS deploy | Deploy + test | Task Scheduler |
| 38 | **PROJECT 1 DONE**: Ragas eval + LLM-as-a-judge + APPLY | Wellfound + YC apps | Min Stack |
| 39 | **PROJECT 1 FOLLOW-UP**: Buffer for callbacks, weak area review | Respond to recruiters | Merge + Insert Interval |

### Phase 5: Database Architecture & Advanced SQL (Days 40-46)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 40 | **Vector Compression**: FP32/FP16/Int8, sub-space clustering + **FAISS** (Flat, IVFFlat, PQ) | Compress index with Int8 PQ. Measure recall vs memory | Kth Largest in Stream |
| 41 | **Late-Interaction Theory** (ColBERT vs Bi/Cross-Encoders) + **Vespa** (phased ranking, Docker config) | Phased ranking token-level interactions via Vespa Docker | K Closest Points to Origin |
| 42 | **Storage Engines** (row vs columnar) + **Cache Eviction** (LRU, LFU, TTL) + **LanceDB** + Multi-Tenant scaling | Multi-tenant store + TTL eviction. Contrast RAM vs S3 | Best Time to Buy/Sell Stock |
| 43 | **Hybrid Search**: pgvector + tsvector + RRF + **Elasticsearch ELSER** (~30K dims) | Build hybrid search. Compare 4 retrieval types | Trapping Rain Water |
| 44 | **Redis VSET + FT.HYBRID**: VSIM, COMBINE RRF vs LINEAR | Implement VSIM + FT.HYBRID. Measure latency | Add Two Numbers + Remove Nth Node + Search Rotated (R1), Find Min (R3) |
| 45 | **System Metrics**: latency, throughput, QPS, p50/p95 + **CAP Theorem** + **Milvus** architecture | Deploy clustered Milvus. Measure consistency vs latency trade-offs | Product Except Self + Group Anagrams + Add Two Numbers (R1), Remove Nth (R3) |
| 46 | **AI Security** (prompt injection, jailbreaks) + **NeMo Guardrails** + **Agno dual-schema** + **Ollama** | Semantic routing firewall + guarded local LLM | Validate BST + Kth Smallest BST + Product Except Self (R1), Group Anagrams (R3) |

### Phase 6: AI Infrastructure & Production MLOps (Days 47-56)
| Day | Morning | Afternoon | DSA (See agent/dsa/study_plan.md) |
|-----|---------|-----------|-----------------------------------|
| 47 | **Networking** (sockets, TCP/UDP) + **Concurrency vs Parallelism** + **WebSockets/protobuf/gRPC** | Build bi-directional streaming. Compare sync vs async throughput | 🔁 REVIEW ONLY: Merge Intervals, Number of Islands, Course Schedule, Search Rotated, Product Except Self, Validate BST |
| 48 | **Git** (branch, merge) + **DVC** + **MLflow** + **Feast/Tecton** + DSPy compilation | Git branches + DVC dataset + MLflow tracker + feature pipeline | Subsets + Permutations + Add Two Numbers (R7), Group Anagrams (R7) |
| 49 | **JSON-RPC 2.0** + **Webhooks** + **PKI/TLS** + **OAuth 2.1** + **MCP** (server, security) | Build MCP server with mTLS + OAuth 2.1 + monitoring | Combination Sum + Letter Combo + Subsets (R1), Permutations (R3) |
| 50 | **OS Memory** (paging, virtual) + **Process Scheduling** (preemption) + **GPU Arch** + **vLLM** + rate limiting + caching | Deploy vLLM. Implement Sliding Window Log. Tenant cache | Climbing Stairs + House Robber + Combo Sum (R1), Letter Combo (R3) |
| 51 | **Ontology Design** (POLE+O) + **Ebbinghaus Decay** + **Tripartite Memory** (Cognee, Neo4j, Graphiti, AgentMemory) | POLE+O extraction → Long-Term graph with temporal decay | Coin Change + LIS + Climbing Stairs (R1), House Robber (R3) |
| 52-56 | **System Design Crash Course** + **Mock Week** (Verbal, Pair, Whiteboarding, Behavioral+Take-Home, Apply) | Practice all formats | Word Break + LCS + Coin Change (R1), LIS (R3) → Trie + Design Word Search + Monotonic Stack → Final Review |

### Phase 7: Agentic Orchestration, MCP & Advanced Tools (Days 57-60)
| Day | Morning | Afternoon | DSA (See agent/dsa/study_plan.md) |
|-----|---------|-----------|-----------------------------------|
| 57 | **Advanced Agent Patterns** + **LangGraph vs CrewAI vs AutoGen** + **A2A vs MCP** | Self-reflecting agent + A2A card + MCP tool call | Word Search + Palindromic Substrings + Largest Rect (R1), Top K Revisited (R7) |
| 58 | **Infra Integrations** (Blackboard, Daytona, Firecrawl, Headroom) — individual practice modules | Practice each tool separately | Time Based KV + LRU Cache + Word Search (R1), Palindromic Substr (R3) |
| 59 | **PROJECT 2 BUILD**: Assemble Autonomous Swarm (all components) | Integrate + deploy | Longest Consecutive Seq + Container With Most Water + Time KV (R1), LRU Cache (R3) |
| 60 | **PROJECT 2 DONE**: Eval + Deploy + README + **APPLY BLITZ** | Production-grade docs. Apply to 40+ roles | 🔁 FINAL REVIEW: Two Sum, Contains Dup, Valid Paren, Max Depth, Number of Islands, Merge Intervals, Coin Change, Subsets |

### Phase 8: Scalable Agentic System Design (Post-60-Day — Interview Deep Dive)
| Topic | Morning | Afternoon | Deliverable |
|-------|---------|-----------|-------------|
| Distributed Systems for AI | CAP Theorem, Eventual Consistency, Message Queues (Kafka/RabbitMQ) | Circuit Breakers, Idempotency in Agent Actions | distributed_systems_ai.md |
| Advanced Rate Limiting | Token Bucket vs Leaky Bucket vs Sliding Window Log | Model Routing vs Single Frontier Model | rate_limiting_models.md |
| Protocol Architecture | A2A: Agent Cards, discovery, JSON-RPC 2.0, stateful tasks. MCP: Roots, Sampling | Blended A2A+MCP architectures, security (mTLS, sender-constrained tokens) | protocol_architecture.md |
| Multi-Tenant Design | Silo/Pool/Bridge isolation, tenant-aware caching, RLS, LoRA adapters | Capacity planning: HNSW memory, peak QPS, back-of-envelope | multi_tenant_design.md |
| Disaster Recovery | Multi-region, DB replication, agent state recovery, LLM provider fallback | Graceful degradation: cache fallbacks, model chains | dr_failover.md |
| System Design Mock I | Design RAG for 10M QPD with multi-modal data | Design secure multi-agent with A2A + MCP | system_design_mock_1.md |
| System Design Mock II | Design LLM inference for 500 concurrent users | Design feature store for real-time recs (50ms p99) | system_design_mock_2.md |

---

## 📚 Repository & Reference Integration Matrix
| Days | Focus | Primary Repository |
|------|-------|-------------------|
| 11-24, 32-46 | DSA Pattern Families | labuladong/fucking-algorithm — state-space reduction for BFS and Backtracking |
| 25-31 | ML Theory | alirezadir/machine-learning-interviews, KalyanKS-NLP/LLM-Interview-Questions — top 30 concepts |
| 47-51 | System Design | binhnguyennus/awesome-scalability, chiphuyen/dmls-book Chapters 8-11 |
| 49-51 | Agentic Implementation | modelcontextprotocol/servers, NirDiamant/GenAI_Agents |
| Day 30 | Paper Reading | mli/paper-reading — DeepSeek-V3 Technical Report + Attention Is All You Need |

### Phase 8: Scalable Agentic System Design (Post-60-Day — Interview Deep Dive)
| Topic | Morning | Afternoon | Deliverable |
|-------|---------|-----------|-------------|
| Distributed Systems for AI | CAP Theorem, Eventual Consistency, Message Queues (Kafka/RabbitMQ) | Circuit Breakers, Idempotency in Agent Actions | distributed_systems_ai.md |
| Advanced Rate Limiting | Token Bucket vs Leaky Bucket vs Sliding Window Log | Model Routing vs Single Frontier Model | rate_limiting_models.md |
| Protocol Architecture | A2A: Agent Cards, discovery, JSON-RPC 2.0, stateful tasks. MCP: Roots, Sampling | Blended A2A+MCP architectures, security (mTLS, sender-constrained tokens) | protocol_architecture.md |
| Multi-Tenant Design | Silo/Pool/Bridge isolation, tenant-aware caching, RLS, LoRA adapters | Capacity planning: HNSW memory, peak QPS, back-of-envelope | multi_tenant_design.md |
| Disaster Recovery | Multi-region, DB replication, agent state recovery, LLM provider fallback | Graceful degradation: cache fallbacks, model chains | dr_failover.md |
| System Design Mock I | Design RAG for 10M QPD with multi-modal data | Design secure multi-agent with A2A + MCP | system_design_mock_1.md |
| System Design Mock II | Design LLM inference for 500 concurrent users | Design feature store for real-time recs (50ms p99) | system_design_mock_2.md |


---

## ⚠️ Rules for Updating

1. After each day completes, append the actual topics covered to the Completed table.
2. Update Current Day status to ✅ COMPLETED.
3. Add the next day to Current Day with 🔴 IN PROGRESS.
4. If topics shift (faster or slower), update Upcoming table accordingly.
5. Never plan more than 3 days ahead — let actual pace dictate.
