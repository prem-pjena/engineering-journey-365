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
| 11 | Jul 14 | **OOP: classes, objects, __init__, self, object attributes, methods, inheritance, pass, method overriding** | Two Sum (review) | 1 |

---

## 🔄 Current Day

| Day | Date | Status | Topics | DSA |
|-----|------|--------|--------|-----|
| 12 | Jul 17 | 🔴 IN PROGRESS | Context Managers, Modules, `__init__.py` | Valid Anagram |

---

## 📅 Upcoming (Market-Validated v4 — 2026 Enterprise)

### Phase 1-2: Core DSA Mastery & Algorithmic Optimization (Days 11-24)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 11 | OOP: classes, inheritance, dunder, @property, @staticmethod, @classmethod | Build mock VectorStore class | Two Sum |
| 12 | Context Managers, Modules, __init__.py | Safe File I/O Manager + Package | Valid Anagram |
| 13 | Async: asyncio, event loop, gather + **FastAPI intro** | Build first FastAPI endpoint | Group Anagrams |
| 14 | Generators (yield), Tuples, enumerate, zip + **Constrained Decoding (XGrammar/Outlines)** | Streaming token generator + FSM masking | Top K Frequent |
| 15 | String methods, JSON module | Parse nested JSON LLM outputs | Product of Array |
| 16 | LLM APIs: OpenAI/Gemini, temperature, tokens, streaming + **Probabilistic Data Structures** (Bloom filters, HyperLogLog) | Chat + streaming + set membership | Valid Palindrome |
| 17 | **Algorithmic Prompt Optimization**: DSPy + GEPA — self-improving prompt signatures | Replace manual prompting with compiled, optimized prompts | 3Sum |
| 18 | FastAPI SSE Streaming + Pydantic v2 + Constrained Decoding | Streaming endpoint + FSM-guaranteed JSON | Container With Most Water + Two Sum II |
| 19 | LangChain: Document Loaders, Text Splitters, **Semantic Chunking** | Parse PDF, compare chunk strategies | Longest Substring w/o Repeat |
| 20 | Vector DBs, Embeddings, ChromaDB (prototype-only), HNSW vs IVFFlat | Store chunks + index tuning | Valid Parentheses |
| 21 | **Advanced Retrieval**: Proposition Generation + Step-back Prompting | Decompose docs into atomic propositions | Binary Search |
| 22 | **SQL + pgvector**: SELECT, INSERT, JOINs, vector columns, read-only scopes | Store embeddings with read-only scopes | Search 2D Matrix |
| 23 | **Parent-Child Chunking + Cross-Encoder Reranking + GraphRAG** | Rerank top-20 → top-3, introduce GraphRAG | Reverse Linked List |
| 24 | **Hybrid Search**: BM25 + Dense + tsvector + RRF, pgvector HNSW vs IVFFlat tuning | Implement hybrid search + benchmark | Merge Two Sorted Lists |

### Phase 3: Classical ML, NLP Theory & Transformer Internals (Days 25-31)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 25 | **Math & Statistics**: Linear algebra (dot products, matrix multiplication, eigenvectors), Probability (Bayes, conditional), Distributions | Solve math foundations problems | Reorder List |
| 26 | **Classical ML**: Logistic Regression, Random Forest, XGBoost, K-Means, PCA | Implement on toy datasets | Max Depth Tree |
| 27 | **NLP & Embeddings**: Word2Vec, GloVe, LSTM vs Transformer, cross-attention vs causal vs bidirectional | Build embeddings + attention viz | Validate BST |
| 28 | **Transformer Internals**: Multi-head attention math, RoPE, layer norm, residual connections, FFN. Study: karpathy/minGPT | Implement minimal transformer block | Invert Tree |
| 29 | **DeepSeek-V3**: MLA (KV compression), MoE (auxiliary-loss-free), Multi-Token Prediction | Diagram MLA vs MHA, calculate savings | LCA of BST |
| 30 | **Inference Optimization + RAG Eval**: KV cache, PagedAttention, speculative decoding, quantization. Ragas metrics + traditional (F1, MAP, MRR, NDCG) | Build Ragas eval pipeline | Level Order Traversal |
| 31 | **PROJECT 1 BUILD**: Multi-Tenant Enterprise Knowledge Agent (Agno dual-schema, Graphiti, Mem0, CRAG, JWT RBAC, tsvector) | FastAPI + pgvector RLS + LangGraph + Hybrid Search | Longest Consecutive Sequence |

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
| 40 | **Vector Indexing Deep Dive**: HNSW tuning, IVFFlat, DiskANN via pgvectorscale | Benchmark HNSW vs IVFFlat vs DiskANN | Kth Largest in Stream |
| 41 | **Vector DB Comparison**: pgvector vs Pinecone vs Qdrant vs Milvus vs Weaviate | Decision tree + cost projection | K Closest Points to Origin |
| 42 | **SQL Optimization for AI**: Recursive CTEs, partition pruning | Write recursive queries, set up partitioning | Best Time to Buy/Sell Stock |
| 43 | **PostgreSQL Hybrid Search**: pgvector + tsvector + RRF. Study: faiss, nmslib | Build hybrid search endpoint | Trapping Rain Water |
| 44 | **Redis for AI**: LangCache semantic caching, agent session state, multi-tier caching | Implement Redis LangCache | Largest Rectangle in Histogram |
| 45 | **Agent Security + Ollama**: Agno dual-schema, JWT RBAC + local LLM deployment | PostgreSQL read_only scopes + Ollama | Course Schedule II |
| 46 | **AgentShield + NeMo Guardrails + AWS ECS deploy** | Config scanning + guarded cloud deploy | Trapping Rain Water review |

### Phase 6: AI Infrastructure & Production MLOps (Days 47-53)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 47 | **Real-Time Streaming Agent Architectures**: SSE/WebSockets, state management in streams, gateway strategies (connection pooling, gRPC, drop handling) | Build real-time streaming agent endpoint | Find Min Rotated + Search in Rotated Array |
| 48 | **MLOps + Prompt Management**: Feature stores (Feast/Tecton, point-in-time joins), MLflow/DVC. DSPy compilation, Vellum/Promptfoo A/B testing | Feature store dual-pipeline + DSPy compiled prompts + shadow deployments | Subsets |
| 49 | **AI Observability + MCP Security**: Langfuse/LangSmith tracing, Prometheus/Grafana drift detection. MCP threat models (Confused Deputy, mTLS, tool output sanitization, container isolation) | Monitoring dashboard + secure MCP proxy with mTLS + output sanitization | Serialize/Deserialize Tree |
| 50 | **Inference Optimization + Multi-Tenant Caching**: vLLM PagedAttention (logical KV → physical GPU pages, <8 tokens/seq fragmentation). Continuous batching. Token-aware rate limiting. Silo/Pool/Bridge isolation. Tenant-aware Redis caching | Diagram PagedAttention scheduler + Sliding Window Log + tenant-aware cache | Word Ladder |
| 51 | **CI/CD for AI Agents**: PR-time checks, token-budget regression gates, canary deployments, automated rollback | GitHub Actions pipeline with eval gates + canary deploy | Permutations |
| 52 | Live Coding Mock (FastAPI + LangGraph + MCP + Streaming) + Behavioral | Build mini streaming agent. Practice trade-off articulation | Combination Sum |
| 53 | DSA Mock + Portfolio Review + Apply Follow-ups | Solve problems + polish GitHub README with architecture diagrams | Clone Graph |

### Phase 7: Agentic Orchestration, MCP & Advanced Tools (Days 54-60)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 54 | **Advanced Agent Patterns + A2A vs MCP**: Self-reflection, multi-tool, hierarchical, debate. LangGraph vs CrewAI vs AutoGen. A2A (horizontal delegation, Agent Cards, JSON-RPC 2.0) vs MCP (vertical tools). Study: a2aproject/A2A, FareedKhan-dev/all-agentic-architectures | Build self-reflecting agent + A2A card discovery + MCP tool call in same system | Implement Trie (Prefix Tree) |
| 55 | **PROJECT 2 BUILD**: Autonomous Code & Web Intelligence Swarm — Blackboard + Researcher (browser-use/Firecrawl) + Coder (Daytona). n8n/Langflow/Dify prototyping. Ollama local | Build Blackboard with namespaces. Visual workflow in n8n | Time Based Key-Value Store |
| 56 | **PROJECT 2**: MCP with OAuth 2.1 + Advanced MCP (streaming tools, Sampling, Roots). Claude Code integration | Docker + GitHub Actions + AWS ECS. MCP Sampling | Largest Rectangle in Histogram |
| 57 | **PROJECT 2 DONE**: LLM-as-a-judge + Deploy + README. OpenClaw gateway (AGENTS.md, SOUL.md). Study: iusztinpaul/designing-real-world-ai-agents-workshop | Production-grade docs + OpenClaw + Deep Research Agent pattern | Number of Islands + Max Area of Island |
| 58 | **Token Compression**: Headroom (60-95% reduction). Agent observability (LangSmith: cost/task, steps/task). Mem0 + Graphiti + AgentShield + NeMo | Headroom compression + LangSmith dashboard + security scan | Redundant Connection |
| 59 | **APPLY BLITZ**: Wellfound (20) + YC (10) + LinkedIn DMs (10). Claude Code MCP connectivity | Personalized messages with both projects | Evaluate Reverse Polish Notation |
| 60 | Follow-ups + Mock interviews + Offer evaluation | Negotiate, compare CTC vs cash vs equity | Course Schedule II review |

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
