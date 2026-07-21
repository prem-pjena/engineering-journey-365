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
| 13 | **Type Hinting** (Union, Optional, List, Dict) + **HTTP Protocol** (GET/POST, headers, status codes) + FastAPI intro | Strictly-typed FastAPI GET/POST with JSON validation | Group Anagrams |
| 14 | Generators (yield), Tuples, enumerate, zip | Custom text stream simulator with configurable delays | Top K Frequent |
| 15 | **String methods, regex** (re.search, re.findall) + JSON + **Defensive Parsing** (markdown fences, truncated brackets) | Error-resilient parser that strips fences and extracts JSON | Product of Array |
| 16 | **LLM APIs**: OpenAI/Gemini, tokens, logits, softmax, autoregressive generation, temperature, streaming | Multi-turn Chat CLI with streaming + conversation history | Valid Palindrome |
| 17 | **Prompt Engineering**: System prompts, Role prompting, Zero-shot vs Few-shot, Chain-of-Thought | Manual prompt template router with few-shot examples | 3Sum |
| 18 | **Async Python** (asyncio, gather) + FastAPI SSE + Pydantic v2 + **Generative Parameters** (logit bias, softmax, temperature) | Streaming REST endpoint with token parameter control | Container With Most Water + Two Sum II |
| 19 | **LangChain Fundamentals**: PromptTemplate, ChatPromptTemplate, Messages, output parsers, LCEL pipe | Document Loaders + RecursiveCharacterTextSplitter + Regex chunking | Longest Substring w/o Repeat |
| 20 | **Vector Math**: dot product, cosine similarity, dimensions + **Embeddings API** (text-embedding-3-small) | Pure-Python cosine similarity search (no databases) | Valid Parentheses |
| 21 | **Basic RAG**: chunk → embed → store in Python list → cosine retrieve → LLM generate. Single-hop Q&A over local doc | Binary Search |
| 22 | **SQL Fundamentals**: Tables, rows, keys, SELECT, INSERT, JOIN + sqlite3 in Python | SQLite database for document metadata storage | Search 2D Matrix |
| 23 | **IR Theory**: TF-IDF, sparse vs dense vectors, inverted index + **Parent-Child Chunking** + **Cross-Encoder Reranking** | Two-stage: TF-IDF retrieval + local reranking model | Reverse Linked List |
| 24 | **Hybrid Search Theory**: BM25, RRF formula, sparse-dense fusion + pgvector HNSW vs IVFFlat tuning | BM25 keyword + dense vector search fused via RRF | Merge Two Sorted Lists |

### Phase 3: Classical ML, NLP Theory & Transformer Internals (Days 25-31)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 25 | **Calculus**: Derivatives, Chain Rule + **Optimization**: Gradient Descent, Learning Rates + **Linear Algebra**: vectors, dot products, matrices | Build gradient descent optimizer in pure Python | Reorder List |
| 26 | **Classical ML**: Logistic Regression, Random Forest, XGBoost, K-Means, PCA + Probability & Statistics integrated | Implement on toy datasets | Max Depth Tree |
| 27 | **Classical NLP**: Bag of Words, N-grams + **Word Embeddings**: Word2Vec, GloVe + **Sequential Models**: RNN/LSTM, vanishing gradient | Train Word2Vec. Visualize embedding space | Validate BST |
| 28 | **Transformer Internals**: Seq2Seq bottlenecks, multi-head attention math, RoPE, layer norm, residual, FFN. Study: karpathy/minGPT | Implement transformer block. Compare with RNN | Invert Tree |
| 29 | **Standard KV Cache** + **Mixture-of-Experts** (routing gates, sparse vs dense) + **DeepSeek-V3** (MLA, MoE, MTP) | Diagram KV cache vs MLA. Calculate savings | LCA of BST |
| 30 | **Eval Theory**: BLEU, ROUGE, MAP, MRR, NDCG + **LangSmith** (traces, projects, datasets) + **Ragas** (Faithfulness, Precision) | LangSmith project + Ragas eval pipeline | Level Order Traversal |
| 31 | **LangGraph Foundations**: StateGraph, TypedDict, Nodes, Edges, Reducers, conditional routing. DAG/cyclic theory | Build simple cyclic LangGraph agent (weather-checker with retry) | Longest Consecutive Sequence |

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
| 40 | **Vector Compression Theory**: Sub-space clustering, centroids, FP32/FP16/Int8 + **FAISS** (Flat, IVFFlat, PQ) | Compress index with Int8 PQ. Measure recall vs memory | Kth Largest in Stream |
| 41 | **Late-Interaction Theory**: ColBERT vs Bi-Encoders vs Cross-Encoders, MaxSim + **Vespa** (phased ranking) | Phased ranking with token-level interactions | K Closest Points to Origin |
| 42 | **Storage Engines**: Row vs Columnar, Apache Arrow, zero-copy + **LanceDB** S3-backed + Multi-Tenant vector scaling | Multi-tenant store with columnar caching. Contrast RAM vs S3 | Best Time to Buy/Sell Stock |
| 43 | **Hybrid Search**: pgvector + tsvector + RRF + **Elasticsearch ELSER** sparse vectors (~30K dims) | Build hybrid search. Compare 4 retrieval types | Trapping Rain Water |
| 44 | **Redis VSET + FT.HYBRID**: VSIM for sub-ms similarity, COMBINE RRF vs LINEAR | Implement VSIM + FT.HYBRID. Measure latency | Largest Rectangle in Histogram |
| 45 | **Distributed Systems**: CAP Theorem, Consistency Levels, Sharding + **Milvus** (Knowhere, Proxy/QueryNode/IndexNode) | Deploy clustered Milvus. Tune consistency vs latency | Course Schedule II |
| 46 | **AI Security**: Prompt injection, Jailbreaks + **NeMo Guardrails** + **Agno dual-schema** + **Ollama** | Semantic routing firewall + guarded local LLM deploy | Trapping Rain Water review |

### Phase 6: AI Infrastructure & Production MLOps (Days 47-56)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 47 | **Advanced Networking**: WebSockets, Protocol Buffers, HTTP/2, gRPC bidirectional streaming | Build persistent bi-directional streaming for token delivery | Find Min Rotated + Search in Rotated Array |
| 48 | **Git + DVC** (version control, data versioning) + **MLflow** (experiment tracking) + **Feast/Tecton** (feature stores, point-in-time joins) + DSPy compilation | Git repo + DVC dataset + MLflow tracker + feature pipeline | Subsets |
| 49 | **JSON-RPC 2.0** + **PKI/TLS/Certificates** + **OAuth 2.1** (JWTs, scopes, grants) + **MCP** (Host/Client/Server, Tools/Resources, threat models) | Build MCP server with mTLS + OAuth 2.1 + monitoring | Serialize/Deserialize Tree |
| 50 | **OS Memory**: Virtual vs Physical, paging + **GPU Arch**: VRAM, bandwidth, fragmentation + **vLLM** PagedAttention, continuous batching + rate limiting + multi-tenant caching | Deploy vLLM. Analyze fragmentation reduction. Tenant cache | Word Ladder |
| 51 | **Ontology Design**: POLE+O, Knowledge Graph modeling + **Ebbinghaus Decay** theory + **Tripartite Memory**: Cognee, Neo4j, Graphiti, AgentMemory | Build POLE+O extraction → Long-Term graph with temporal decay | Permutations |
| 52-56 | **System Design Crash Course**: Load Balancing, Scaling, Message Queues + **Mock Week**: Verbal, Pair Programming, Whiteboarding, Behavioral + Take-Home, Apply Blitz | Practice all interview formats | Combination Sum → Eval RPN |

### Phase 7: Agentic Orchestration, MCP & Advanced Tools (Days 57-60)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 57 | **Advanced Agent Patterns + A2A vs MCP**: Self-reflection, multi-tool, hierarchical, debate. LangGraph vs CrewAI vs AutoGen. A2A vs MCP blended | Build self-reflecting agent + A2A card discovery + MCP tool call | Implement Trie (Prefix Tree) |
| 58 | **Infra Integrations**: Blackboard shared-memory, Daytona sandbox, Firecrawl scraping, Headroom compression — individual practice modules | Build each infra module separately before assembling | Time Based Key-Value Store |
| 59 | **PROJECT 2 BUILD**: Assemble Autonomous Swarm — Blackboard + Researcher + Coder + Tripartite Memory + MCP + Headroom + CI/CD | Integrate all components. Deploy | Largest Rectangle in Histogram |
| 60 | **PROJECT 2 DONE**: LLM-as-a-judge + Deploy + README + **APPLY BLITZ** | Production-grade docs. Apply to 40+ roles | Course Schedule II review |

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
