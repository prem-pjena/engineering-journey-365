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
| 11 | Jul 14-21 | **OOP: classes, objects, __init__, self, object attributes, instance methods, inheritance, method overriding, super(), @staticmethod, @classmethod. Built VectorStore** ⏳ Pending: @property, dunder, Mini OOP Project | Two Sum (moved to Day 12) | 1 |

---

## 🔄 Current Day

| Day | Date | Status | Topics | DSA |
|-----|------|--------|--------|-----|
| 12 | Jul 21 | 🔴 IN PROGRESS | Terminal, Git, Context Managers, Modules, __init__.py, venv/pip | Two Sum (pending from D11) + Valid Anagram |

---

## 📅 Upcoming (Market-Validated v4 — 2026 Enterprise)

### Phase 1-2: Core DSA Mastery & Algorithmic Optimization (Days 11-24)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 11 | **Python Decorators** (first-class functions, @syntax) + **OOP deep dive** (@property, @staticmethod, @classmethod, dunder) | Build DocumentStore with dunder methods for exact lookup | Two Sum |
| 12 | **Terminal Basics** (cd, ls, mkdir) + **Git** (init, add, commit) + **Context Managers** + **venv/pip** | Init Git repo. Python package. First commit | Two Sum (pending from D11) + Valid Anagram |
| 13 | **pip/venv** + **HTTP Protocol** (GET/POST, headers, status codes) + **Type Hinting** + **FastAPI intro** | Setup venv. Build strictly-typed GET/POST endpoint | Group Anagrams |
| 14 | Generators (yield), Tuples, enumerate, zip | Custom text stream simulator with configurable delays | Top K Frequent |
| 15 | **Markdown Syntax** (fences, headings) + **regex/JSON** + **Defensive Parsing** (truncated brackets, fences) | Error-resilient parser extracting JSON from markdown | Product of Array |
| 16 | **Environment Variables** (.env, os.environ) + **LLM APIs** (tokens, logits, softmax, temperature, streaming) | .env setup. Multi-turn Chat CLI with streaming | Valid Palindrome |
| 17 | **Prompt Engineering**: System prompts, few-shot, CoT | Manual prompt template router | 3Sum |
| 18 | **Async Python** + **Data Serialization** (schema, Pydantic) + FastAPI SSE + **Generative Parameters** | Streaming endpoint with Pydantic validation + token controls | Container With Most Water + Two Sum II |
| 19 | **Data Pipeline Theory** + **LangChain** (PromptTemplate, LCEL, parsers) | Document Loaders + RecursiveCharacterTextSplitter | Longest Substring w/o Repeat |
| 20 | **Vector Math** (dot product, cosine similarity) + **Embeddings API** | Pure-Python cosine similarity search | Valid Parentheses |
| 21 | **Basic RAG**: chunk → embed → store → cosine retrieve → LLM generate | Single-hop Q&A over local doc | Binary Search |
| 22 | **Relational DB** + **ACID** (transactions, commit, rollback) + **SQL** (SELECT, JOIN) + **sqlite3** | SQLite database. Practice transactions | Search 2D Matrix |
| 23 | **IR Theory** (TF-IDF, inverted index) + **Parent-Child Chunking** + **Cross-Encoder Reranking** | Two-stage: TF-IDF + reranking | Reverse Linked List |
| 24 | **Docker Basics** (images, containers, Dockerfiles) + **Hybrid Search** (BM25, RRF) + **pgvector via Docker** | Run pgvector in Docker. BM25 + dense + RRF fusion | Merge Two Sorted Lists |

### Phase 3: Classical ML, NLP Theory & Transformer Internals (Days 25-31)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 25 | **Linear Algebra for AI**: vectors, dot products, matrices, eigenvectors | Solve linear algebra problems. Visualize transformations | Reorder List |
| 25B | **Calculus**: Derivatives, Chain Rule + **Gradient Descent** | Build gradient descent optimizer. Visualize loss landscape | — |
| 26 | **Pandas/NumPy** basics + **Classical ML Intro**: Logistic Regression + K-Means | Implement Logistic Regression + K-Means on toy datasets | Max Depth Tree |
| 27 | **Classical NLP**: BoW, N-grams, Tokenization + **Word2Vec**/GloVe | Build BoW vectors. Train Word2Vec. Visualize with PCA | Validate BST |
| 27B | **Sequential Models**: RNN theory, vanishing gradient + **LSTM** (gates, cell state) | Compare RNN vs feedforward on sequential data | — |
| 28 | **NN Lifecycle**: Training vs Inference + **Transformer Internals** (QKV, RoPE, layer norm, residual) | Implement transformer block. Compare with RNN | Invert Tree |
| 29 | **Standard KV Cache** + **Mixture-of-Experts** + **DeepSeek-V3** (MLA, MoE, MTP) | Diagram KV cache vs MLA. Calculate savings | LCA of BST |
| 30 | **Eval Theory**: BLEU, ROUGE, MAP, MRR, NDCG + **LangSmith** + **Ragas** | LangSmith project + Ragas eval pipeline | Level Order Traversal |
| 31 | **LangGraph**: StateGraph, TypedDict, Nodes, Edges, Reducers. DAG/cyclic theory | Build simple cyclic agent (weather-checker with retry) | Longest Consecutive Sequence |

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
| 44 | **Redis VSET + FT.HYBRID**: VSIM, COMBINE RRF vs LINEAR | Implement VSIM + FT.HYBRID. Measure latency | Largest Rectangle in Histogram |
| 45 | **System Metrics**: latency, throughput, QPS, p50/p95 + **CAP Theorem** + **Milvus** architecture | Deploy clustered Milvus. Measure consistency vs latency trade-offs | Course Schedule II |
| 46 | **AI Security** (prompt injection, jailbreaks) + **NeMo Guardrails** + **Agno dual-schema** + **Ollama** | Semantic routing firewall + guarded local LLM | Trapping Rain Water review |

### Phase 6: AI Infrastructure & Production MLOps (Days 47-56)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 47 | **Networking** (sockets, TCP/UDP) + **Concurrency vs Parallelism** + **WebSockets/protobuf/gRPC** | Build bi-directional streaming. Compare sync vs async throughput | Find Min Rotated + Search in Rotated Array |
| 48 | **Git** (branch, merge) + **DVC** + **MLflow** + **Feast/Tecton** + DSPy compilation | Git branches + DVC dataset + MLflow tracker + feature pipeline | Subsets |
| 49 | **JSON-RPC 2.0** + **Webhooks** + **PKI/TLS** + **OAuth 2.1** + **MCP** (server, security) | Build MCP server with mTLS + OAuth 2.1 + monitoring | Serialize/Deserialize Tree |
| 50 | **OS Memory** (paging, virtual) + **Process Scheduling** (preemption) + **GPU Arch** + **vLLM** + rate limiting + caching | Deploy vLLM. Implement Sliding Window Log. Tenant cache | Word Ladder |
| 51 | **Ontology Design** (POLE+O) + **Ebbinghaus Decay** + **Tripartite Memory** (Cognee, Neo4j, Graphiti, AgentMemory) | POLE+O extraction → Long-Term graph with temporal decay | Permutations |
| 52-56 | **System Design Crash Course** + **Mock Week** (Verbal, Pair, Whiteboarding, Behavioral+Take-Home, Apply) | Practice all formats | Combination Sum → Eval RPN |

### Phase 7: Agentic Orchestration, MCP & Advanced Tools (Days 57-60)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 57 | **Advanced Agent Patterns** + **LangGraph vs CrewAI vs AutoGen** + **A2A vs MCP** | Self-reflecting agent + A2A card + MCP tool call | Implement Trie |
| 58 | **Infra Integrations** (Blackboard, Daytona, Firecrawl, Headroom) — individual practice modules | Practice each tool separately | Time Based KV Store |
| 59 | **PROJECT 2 BUILD**: Assemble Autonomous Swarm (all components) | Integrate + deploy | Largest Rectangle |
| 60 | **PROJECT 2 DONE**: Eval + Deploy + README + **APPLY BLITZ** | Production-grade docs. Apply to 40+ roles | Course Schedule II review |

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
