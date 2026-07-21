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
| 19 | **LangChain Fundamentals**: PromptTemplate, ChatPromptTemplate, Messages, output parsers, LCEL pipe chaining | **Apply to Docs**: Document Loaders, Text Splitters, Semantic Chunking. Parse first PDF | Longest Substring w/o Repeat |
| 20 | Vector DBs, Embeddings, HNSW vs IVFFlat (prototyping with FAISS or local pgvector) | Store chunks + index tuning | Valid Parentheses |
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
| 30 | **LangSmith Platform + RAG Eval**: Projects, traces, spans, datasets. KV cache, PagedAttention, speculative decoding. Ragas (Faithfulness, Context Precision/Recall). F1, MAP, MRR, NDCG | Setup LangSmith project + build Ragas eval pipeline | Level Order Traversal |
| 31 | **LangGraph Foundations + PROJECT 1 START**: StateGraph vs Chain, TypedDict state, Nodes, Edges, Reducers, conditional routing. Build supervisor LangGraph for RAG | FastAPI + pgvector RLS + LangGraph + Hybrid Search | Longest Consecutive Sequence |

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
| 40 | **FAISS Vector Primitives Lab**: IndexFlatL2, IndexIVFFlat (Voronoi), Product Quantization (IVF4096,PQ16), HNSW vs IVFFlat vs PQ trade-offs. Scalar Int8 quantization (<1.5% recall loss, 64% storage reduction) | Build FAISS index benchmark. Measure recall vs QPS vs memory | Kth Largest in Stream |
| 41 | **Vespa: Tensor-Native Search**: Tensor math (mapped vs indexed dimensions), ColBERT multi-vector, phased ranking (BM25 + HNSW + ONNX reranking) | Build hybrid search schema with nearestNeighbor + bm25. Define rank-profile | K Closest Points to Origin |
| 42 | **LanceDB + Multi-Tenant Scaling**: In-memory vs SSD vs object-storage. LanceDB Arrow columnar S3-backed. Pre-filtering vs post-filtering recall collapse. pgvector hnsw.max_scan_tuples | RAM scaling calc. Tenant isolation with physical partitions. Contrast with LanceDB | Best Time to Buy/Sell Stock |
| 43 | **Hybrid Search Architectures**: pgvector + tsvector + RRF. Elasticsearch ELSER sparse vectors (~30K dims), semantic_text, Retriever API | Build hybrid search (pgvector RRF). Implement ELSER. Compare recall | Trapping Rain Water |
| 44 | **Redis VSET & FT.HYBRID**: Native VSET + VSIM for sub-ms similarity. FT.HYBRID with COMBINE RRF vs COMBINE LINEAR. Multi-tier caching | Implement VSIM + FT.HYBRID. Measure vs two-phase approach | Largest Rectangle in Histogram |
| 45 | **Milvus Distributed Architecture**: Knowhere, Proxy/QueryNode/IndexNode, GuaranteeTs consistency, consistency_level tuning, Clustering Compaction | Deploy Milvus. Configure consistency levels. Trigger compaction | Course Schedule II |
| 46 | **Agent Security + Ollama + AWS ECS Deploy**: Agno dual-schema, JWT RBAC, Ollama local, Guardrails + NeMo | PostgreSQL read_only scopes + guarded cloud deploy | Trapping Rain Water review |

### Phase 6: AI Infrastructure & Production MLOps (Days 47-56)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 47 | **Real-Time Streaming Agent Architectures**: SSE/WebSockets, state management in streams, gateway strategies (connection pooling, gRPC, drop handling) | Build real-time streaming agent endpoint | Find Min Rotated + Search in Rotated Array |
| 48 | **MLOps + Prompt Management**: Feature stores (Feast/Tecton, point-in-time joins), MLflow/DVC. DSPy compilation, Vellum/Promptfoo A/B testing | Feature store dual-pipeline + DSPy compiled prompts + shadow deployments | Subsets |
| 49 | **MCP Fundamentals + AI Observability**: What is MCP? Host/Client/Server, JSON-RPC 2.0, Tools/Resources/Prompts, transports. Build first MCP server. **Then**: tracing + drift detection + MCP threat models | Build MCP server → add mTLS + monitoring dashboard | Serialize/Deserialize Tree |
| 50 | **Inference Optimization + Multi-Tenant Caching**: vLLM PagedAttention (logical KV → physical GPU pages, <8 tokens/seq fragmentation). Continuous batching. Token-aware rate limiting. Silo/Pool/Bridge isolation. Tenant-aware Redis caching | Diagram PagedAttention scheduler + Sliding Window Log + tenant-aware cache | Word Ladder |
| 51 | **Tripartite Agent Memory & Temporal Graphs**: Cognee (graph-native), Neo4j (Short/Long/Reasoning), Graphiti (bi-temporal), AgentMemory (Ebbinghaus decay). POLE+O extraction. Study: topoteretes/cognee, rohitg00/agentmemory | Design memory loop: observations → POLE+O → Long-Term graph → reasoning traces. Implement temporal decay | Permutations |
| 52 | **MOCK: LLM Theory & RAG Architecture** (Verbal) + **Behavioral Integration** | Practice Q&A from interview bank. Record and refine | Combination Sum |
| 53 | **MOCK: Pair Programming** (Live coding — enforce "thinking out loud") | Build mini streaming agent with continuous vocalization | Clone Graph |
| 54 | **MOCK: System Design** (Whiteboarding RAG pipelines + LLM Gateways) | Draw 5-step flow. Practice trade-offs | Number of Islands + Max Area |
| 55 | **MOCK: Behavioral + Portfolio Defense + Take-Home Simulation** (6-hr block) | Build full MVP: FastAPI + LangGraph + MCP server | Redundant Connection |
| 56 | **APPLY BLITZ + Mock Review**: Wellfound (20) + YC (10) + LinkedIn DMs (10) | Review mock recordings. Iterate based on feedback | Evaluate Reverse Polish Notation |

### Phase 7: Agentic Orchestration, MCP & Advanced Tools (Days 57-60)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 57 | **Advanced Agent Patterns + A2A vs MCP**: Self-reflection, multi-tool, hierarchical, debate. LangGraph vs CrewAI vs AutoGen. A2A (horizontal delegation, Agent Cards, JSON-RPC 2.0) vs MCP (vertical tools). Study: a2aproject/A2A, FareedKhan-dev/all-agentic-architectures | Build self-reflecting agent + A2A card discovery + MCP tool call in same system | Implement Trie (Prefix Tree) |
| 58 | **PROJECT 2 BUILD**: Autonomous Code & Web Intelligence Swarm — Blackboard + Researcher (browser-use/Firecrawl) + Coder (Daytona). **Tripartite Memory**: Neo4j/Cognee (POLE+O). n8n/Langflow/Dify. Ollama | Build Blackboard with tripartite memory. Visual workflow in n8n | Time Based Key-Value Store |
| 59 | **PROJECT 2**: MCP with OAuth 2.1 + Advanced MCP (Sampling, Roots, streaming). Claude Code + Headroom compression + Docker + AWS ECS | Implement MCP Sampling + Headroom + CI/CD | Largest Rectangle in Histogram |
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
