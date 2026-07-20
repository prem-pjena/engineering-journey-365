# 📚 60-Day Agentic AI Engineer Sprint: Complete Curriculum (Market-Validated v2)

**Target Role:** Agentic AI Engineer | AI Engineer | SDE AI
**Target Compensation:** ₹30-50k/mo intern (Day 28) → ₹10-12 LPA FT / $24-40k/yr global remote (Day 60)
**Investment:** 5-6 hours daily. Zero days off.

---

## 📊 Complete Tech Stack (Market-Validated Priority Matrix)

| Priority | Category | Technologies |
|----------|----------|-------------|
| 🔴 Must-Know | Python Architecture | OOP (classes, inheritance, dunder, @property, static/classmethod), Context Managers, Async (asyncio, await, gather), Generators (yield), Tuples, enumerate, zip, String methods, JSON, Comprehensions, Type hints, Modules |
| 🔴 Must-Know | Backend API | **FastAPI**, Pydantic v2 strict validation, **Asynchronous Python**, **Server-Sent Events (SSE)** for streaming (market standard — Django/Flask are obsolete for AI roles) |
| 🔴 Must-Know | LLM & Orchestration | LangChain (prompt templates, loaders, splitters, with_structured_output), **Algorithmic Prompt Optimization (DSPy + GEPA)**, LLM APIs (OpenAI, Gemini) — **LCEL deep dive deprioritized, use LangGraph for orchestration** |
| 🔴 Must-Know | Agent Frameworks | **LangGraph** (StateGraph, nodes, edges, reducers, routing, checkpointing via **PostgresSaver**, HITL, multi-agent, parallel **Send API**, hash-based idempotent recompute) — industry standard for production agents. **OpenAI Agents SDK** for lightweight handoffs/voice. **CrewAI** for rapid role-based agent assembly (complementary to LangGraph) |
| 🔴 Must-Know | RAG & Search | Corrective → Adaptive → Agentic RAG, **Proposition Generation**, **Step-back Prompting**, **Semantic Chunking**, **Parent-Child Chunking**, **Cross-encoder Reranking**, **Hybrid Search (BM25 + Dense + tsvector + RRF)**, **GraphRAG**, pgvector, **RAGFlow DeepDoc** for enterprise document parsing — **Naive RAG deprioritized** |
| 🔴 Must-Know | Agent Memory | **Mem0** (semantic fact extraction, automated deduplication, contradiction resolution), **Graphiti** (temporal knowledge graphs), **Procedural Memory** (parameterized workflow templates from execution traces), **Blackboard System** (multi-agent shared memory with optimistic locking) |
| 🔴 Must-Know | Agentic Web Interaction | **browser-use** (Playwright-based visual DOM understanding, tab/multi-tab navigation), **Firecrawl** (LLM-ready markdown extraction, anti-bot bypass, batch crawling) |
| 🔴 Must-Know | Sandboxed Execution | **Daytona SDK** (isolated, ephemeral sandboxes with dedicated kernel, network isolation, vCPU/RAM allocation for AI-generated code) |
| 🔴 Must-Know | Evaluation & Observability | **LangSmith**, **Langfuse/OpenLLMetry** (observability + tracing), **Ragas** (Faithfulness, Context Precision/Recall, Answer Relevancy), **LLM-as-a-judge** regression testing, **AIBOM** (AI Bill of Materials for supply chain security) |
| 🔴 Must-Know | Constrained Decoding | **XGrammar / Outlines** — finite-state machine token masking for guaranteed JSON output. Prevents agent crashes from malformed tool calls |
| 🔴 Must-Know | Inference Optimization | **vLLM** (PagedAttention, continuous batching, Tensor Parallelism), KV cache management, Quantization (INT8/INT4) — essential for open-source model serving |
| 🔴 Must-Know | Semantic Caching | **Redis** (LangCache) with vector embedding + cosine similarity threshold tuning (0.85-0.95) + hybrid metadata filtering for tenant isolation. **Redis for agent session state storage** |
| 🔴 Must-Know | Agent Security | **Dual Schema Enforcement** (Agno pattern — read-only transaction scopes for data agents), **JWT-based RBAC**, **AgentShield** (config scanning, adversarial red-teaming), **NeMo Guardrails** (topical bounding, jailbreak detection), **OAuth 2.1** for MCP (token exchange, no token passthrough, per-client consent registries) |
| 🔴 Must-Know | SQL & Vectors | PostgreSQL, pgvector, **pgvectorscale (DiskANN)** for SSD-optimized billion-scale vectors, HNSW vs IVFFlat vs DiskANN vs **PQ vs IVF+PQ** indexing, vector similarity search, **read-only transaction scopes**, **Recursive CTEs** for tree traversal, **tsvector full-text search + Reciprocal Rank Fusion** for hybrid retrieval |
| 🔴 Must-Know | Tensor-Native Search | **Vespa** — unified tensor framework for dense, sparse, lexical, and multi-modal retrieval in single engine. Phased ranking (BM25 + HNSW + ONNX reranking) |
| 🔴 Must-Know | Serverless Vector Storage | **LanceDB** — Arrow-native columnar format, memory-mapped S3-backed zero-copy access, compute-storage decoupling |
| 🔴 Must-Know | Distributed Vector DB | **Milvus** — Knowhere engine, Proxy/QueryNode/IndexNode decoupling, GuaranteeTs consistency, consistency_level tuning (Strong/Bounded/Eventual) |
| 🔴 Must-Know | Agent Memory Databases | **Cognee** (graph-native memory control plane), **Neo4j** (tripartite Short/Long/Reasoning memory), **Graphiti** (bi-temporal knowledge graphs), **AgentMemory** (MCP-integrated procedural memory with Ebbinghaus decay) |
| 🔴 Must-Know | DSA | **Pareto 50+** — Arrays & Hashing, Two Pointers, Sliding Window, Stack & Queue, Binary Search, Linked Lists, Trees (BFS/DFS), Graphs (BFS/DFS/Topo Sort/Cycle Detection), Intervals, Backtracking, Heaps, Design (LRU Cache, Trie, Time-Based KV), **DP (Coin Change, LIS, Climbing Stairs)**, **Monotonic Stack (Largest Rectangle, Trapping Rain Water)**, **BFS Shortest Path (Word Ladder)**. **Probabilistic Data Structures**: Bloom filters, HyperLogLog. **Dimensionality Reduction**: matrix multiplication complexity for attention |
| 🔴 Must-Know | Local LLM Deployment | **Ollama** — run LLMs locally for development, privacy-preserving deployment, data sovereignty compliance (critical for Indian enterprise/fintech) |
| 🔴 Must-Know | Enterprise RAG Engine | **RAGFlow** — DeepDoc module for layout-aware document parsing (tables, headers, multi-column, OCR), visual RAG pipeline builder |
| 🔴 Must-Know | Token Optimization | **Headroom** — content-aware compression (JSON, AST, prose) reducing token overhead 60-95% before LLM processing |
| 🔴 Must-Know | Local Agent Gateway | **OpenClaw** — multi-channel agent gateway, AGENTS.md/SOUL.md workspace state management, local-first orchestration |
| 🔴 Must-Know | Agentic Coding | **Claude Code** — agentic coding tool, CLAUDE.md workspace context injection, automated three-phase loop (gather → act → verify) |
| 🟡 Good-to-Have | Visual Workflow Builders | **n8n**, **Langflow**, **Dify** — rapid prototyping and stakeholder demonstrations; not for production agent workflows |
| 🟡 Good-to-Have | Self-Hosted Chat UI | **Open WebUI** — offline-capable ChatGPT alternative for local testing |
| 🟡 Good-to-Have | Sparse Vector Search | **Elasticsearch ELSER** — learned sparse retrieval (~30K dimensions), exact-match precision + deep semantic matching without fine-tuning |
| 🟡 Good-to-Have | Enterprise RAG Reference | **Bisheng** — study production document extraction pipelines, hybrid orchestration engines (theory only) |
| 🟡 Good-to-Have | Full-Stack | **Next.js + TypeScript** (unlocks Full Stack AI Engineer roles — premium pay for end-to-end delivery) |
| 🟡 Good-to-Have | Data | Pandas, NumPy basics |
| 🟡 Good-to-Have | Interview Theory | Transformer architecture (Q, K, V, self-attention, RoPE), BERT vs GPT, tokenization (BPE/WordPiece/Unigram/SentencePiece), LLM inference architecture (vLLM, KV cache), **MCP OWASP Top 10**, **Procedural vs Episodic vs Semantic Memory**, **Blackboard Architecture**, **DeepSeek-V3 (MLA, MoE) internals**, **Classical ML (Logistic Regression, Random Forest, XGBoost, K-Means, PCA)** |
| ⚪ Nice-to-Have | Fine-tuning | LoRA / PEFT — 8.5% JD mention vs RAG 35.9%. Read 1 article for concept only |
| 🟡 Good-to-Have | Prototype-Only | **CrewAI** — rapid role-based assembly, not for stateful production. **n8n/Langflow/Dify** — visual prototyping only |
| 🚫 Skip | CNNs/RNNs/Classical ML | Zero JD mentions for GenAI Engineer roles. Skip bias-variance, cross-validation, gradient descent entirely |

---

## 📅 60-Day Complete Curriculum (Market-Validated)

### Phase 1-2: Core DSA Mastery & Algorithmic Optimization (Days 11-24)
*Goal: Arrays, hashing, two pointers, linked lists, binary search. Python + FastAPI + DSPy/GEPA*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 11 | OOP: classes, inheritance, dunder, @property, @staticmethod, @classmethod | Build mock VectorStore class | Two Sum | vector_store_oop.py |
| 12 | Context Managers (`__enter__`, `__exit__`), Modules, `__init__.py` | Safe File I/O Manager + Package refactor | Valid Anagram | context_logger.py |
| 13 | Async Python: asyncio, event loop, gather + **FastAPI intro** | Build first FastAPI endpoint (GET/POST) | Group Anagrams | fastapi_hello.py |
| 14 | Generators (yield), Tuples, enumerate, zip + **Constrained Decoding (XGrammar/Outlines)** | Build streaming token generator + FSM token masking | Top K Frequent | token_streamer.py |
| 15 | String methods, JSON module | Parse nested JSON LLM outputs | Product of Array | json_parser.py |
| 16 | LLM APIs: OpenAI/Gemini, temperature, tokens, streaming | Chat + streaming response + **Probabilistic Data Structures** (Bloom filters, HyperLogLog) | Valid Palindrome | basic_llm_api.py |
| 17 | **Algorithmic Prompt Optimization**: DSPy + GEPA (Genetic-Pareto Evolution) | Replace manual prompt engineering with compiled, optimized prompts | 3Sum | dspy_optimizer.py |
| 18 | FastAPI SSE Streaming + Pydantic v2 + Constrained Decoding | Build streaming endpoint + FSM-guaranteed JSON | Container With Most Water + Two Sum II | fastapi_streaming.py |
| 19 | LangChain: Document Loaders, Text Splitters, **Semantic Chunking** | Parse PDF, split by semantic boundaries, compare chunk strategies | Longest Substring w/o Repeat | semantic_chunker.py |
| 20 | Vector DBs, Embeddings, HNSW vs IVFFlat (prototyping with FAISS or local pgvector) | Store chunks + similarity search + index tuning | Valid Parentheses | vector_index_basics.py |
| 21 | **Advanced Retrieval**: Proposition Generation + Step-back Prompting | Decompose docs into atomic propositions, generate broader queries | Binary Search | advanced_retrieval.py |
| 22 | **SQL + pgvector**: SELECT, INSERT, JOINs, vector columns, read-only scopes | Store embeddings with read-only transaction scopes for safety | Search 2D Matrix | pgvector_setup.sql |
| 23 | **Parent-Child Chunking + Cross-Encoder Reranking + GraphRAG** | Rerank top-20 to top-3 with BGE, introduce GraphRAG via Milvus | Reverse Linked List | reranked_rag.py |
| 24 | **Hybrid Search**: BM25 + Dense Vector + tsvector + RRF, pgvector HNSW vs IVFFlat tuning | Implement hybrid search + benchmark index configs | Merge Two Sorted Lists | hybrid_search.py |

### Phase 3: Classical ML, NLP Theory & Transformer Internals (Days 25-31)
*Goal: Math/statistics foundations, classical ML, transformer internals, DeepSeek-V3 (MLA, MoE), RAG evaluation metrics. No new DSA — this phase builds theory*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 25 | **Math & Statistics Foundations**: Linear algebra (dot products, matrix multiplication, eigenvectors for attention). Probability (Bayes theorem, conditional). Distributions | Solve probability + linear algebra problems. Study Ref: trekhleb/homemade-machine-learning | Reorder List | math_foundations.py |
| 26 | **Classical ML Fundamentals**: Logistic Regression, Random Forest, Gradient Boosting (XGBoost), K-Means, PCA. Study Ref: scikit-learn/scikit-learn | Implement each algorithm on toy datasets, compare performance | Max Depth Tree | classical_ml.py |
| 27 | **NLP & Embedding Evolution**: Word2Vec, GloVe, sequence models (LSTM vs Transformer), cross-attention vs causal attention vs bidirectional | Build simple embeddings + attention visualization | Validate BST | nlp_embeddings.py |
| 28 | **Transformer Internals Deep Dive**: Multi-head attention math, positional encoding (RoPE), layer norm, residual connections, feed-forward networks. Study Ref: karpathy/minGPT | Implement a minimal transformer block from scratch | Invert Tree | transformer_block.py |
| 29 | **Next-Gen Architectures: DeepSeek-V3**: Multi-Head Latent Attention (MLA — KV compression to d_c=512), Mixture of Experts (auxiliary-loss-free load balancing), Multi-Token Prediction. Study Ref: deepseek-ai/DeepSeek-V3 | Diagram MLA vs standard MHA. Calculate memory savings | LCA of BST | deepseek_arch.py |
| 30 | **Inference Optimization + RAG Eval Metrics**: KV cache mechanics, PagedAttention, speculative decoding, INT8/INT4 quantization. Ragas (Faithfulness, Context Precision/Recall, Answer Relevancy). Traditional: F1, MAP, MRR, NDCG@K, BLEU, ROUGE | Build eval pipeline with Ragas. Measure faithfulness + context precision | Level Order Traversal | eval_metrics.py |
| 31 | **PROJECT 1 BUILD**: Multi-Tenant Enterprise Knowledge Agent (Agno dual-schema, Graphiti KG, Mem0, CRAG, JWT RBAC, tsvector hybrid search) | FastAPI + pgvector RLS + LangGraph + Cross-encoder + Hybrid Search. **Dimensionality Reduction & Matrix Ops** theory for attention | Longest Consecutive Sequence | project1_start/ |

### Phase 4: Advanced DSA & Enterprise RAG Architectures (Days 32-39)
*Goal: Graph algorithms, DP, intervals alongside RAGFlow deep document parsing, agentic RAG, advanced memory*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 32 | **Corrective RAG (CRAG)** + **Adaptive RAG** + **RAGFlow DeepDoc** for enterprise docs | Evaluator → web search fallback. Parse PDFs with layout awareness (tables, headers, OCR). Study Ref: infiniflow/ragflow | Course Schedule | corrective_adaptive_rag.py |
| 33 | **Conversational RAG + Agentic RAG**. Study Ref: NirDiamant/rag_techniques | Chat history injection + agent re-queries + Step-back prompting | Climbing Stairs | conversational_rag.py |
| 34 | **Agentic RAG with Contextual AI**: instruction-following rerankers, grounded models + **Cross-Session Memory**: Mem0 + Graphiti. Study Ref: NirDiamant/Agent_Memory_Techniques | Agent rewrites queries if results poor. Integrate Mem0 into LangGraph state | Coin Change (RL state-space fundamentals) | agentic_rag_memory.py |
| 35 | **Evaluation**: LLM-as-a-judge regression, Ragas, failure-mode reporting, AIBOM tracking + **Advanced Prompting & Loss Functions**: cross-entropy, contrastive loss, triplet loss, DSPy, Tree of Thoughts, constrained decoding | Build auto-eval pipeline. Implement DSPy compiled prompts | Longest Increasing Subsequence (sequence alignment concepts) | comprehensive_eval.py |
| 36 | **PROJECT 1 BUILD**: Multi-Tenant Enterprise Knowledge Agent (Agno dual-schema, Graphiti, Mem0, CRAG, JWT RBAC, RAGFlow DeepDoc, tsvector hybrid search) | FastAPI + pgvector RLS + LangGraph + Cross-encoder. Local test | LRU Cache | project1_build/ |
| 37 | **PROJECT 1 continued**: Docker containerize + AWS ECS deploy | Deploy + test. Study Ref: langchain-ai/langchain for core pipeline patterns | Task Scheduler | project1_deploy/ |
| 38 | **PROJECT 1 DONE**: Ragas eval report + LLM-as-a-judge regression + **APPLY blitz** | Wellfound + YC applications with Project 1 as proof | Min Stack | project1_done/ |
| 39 | **PROJECT 1 FOLLOW-UP**: Buffer day for interview callbacks, re-visit weak DSA areas | Respond to recruiter messages, practice weak patterns | Merge Intervals + Insert Interval | interview_followup/ |

### Phase 5: Database Architecture & Advanced SQL (Days 40-46)
*Goal: Master vector index algorithms (FAISS PQ/IVF), tensor-native search (Vespa), serverless vector stores (LanceDB), Redis VSET, Milvus distributed architecture, hybrid search with Elasticsearch ELSER, and multi-tenant vector scaling*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 40 | **FAISS Vector Primitives Lab**: IndexFactory strings — IndexFlatL2 (exhaustive), IndexIVFFlat (Voronoi partitioning), **Product Quantization (IVF4096,PQ16)**. HNSW vs IVFFlat vs PQ trade-offs. Scalar Int8 quantization (<1.5% recall loss, 64% storage reduction). Study Ref: facebookresearch/faiss | Build FAISS index comparison benchmark. Measure recall vs QPS vs memory for Flat vs IVFFlat vs IVF-PQ vs HNSW | Kth Largest in Stream | faiss_primitives.py |
| 41 | **Vespa: Tensor-Native AI Search**: Tensor mathematical structures (mapped vs indexed dimensions). Multi-vector indexing for ColBERT late interaction. Phased ranking profiles (first-phase BM25 + HNSW, second-phase ONNX reranking). Study Ref: vespa-engine/vespa | Build hybrid search schema with nearestNeighbor + bm25(text). Define rank-profile that reranks top-1000 using local content node | K Closest Points to Origin | vespa_search.py |
| 42 | **LanceDB & Storage Architecture Comparison**: In-memory vs SSD-optimized vs object-storage architectures. LanceDB columnar Arrow format, zero-copy memory-mapped S3 access, compute-storage decoupling. **Multi-Tenant Vector Scaling**: Pre-filtering vs post-filtering recall collapse. pgvector iterative index scans (hnsw.max_scan_tuples). Physical partitioning for tenant isolation | Calculate RAM scaling for HNSW. Contrast with LanceDB S3-backed on-demand cache fetches. Implement tenant isolation with physical partitions | Best Time to Buy/Sell Stock | lancedb_multitenant.py |
| 43 | **Hybrid Search Architectures**: PostgreSQL pgvector + tsvector + RRF. **Elasticsearch ELSER** sparse vector retrieval (~30K dims) — semantic_text field type, Retriever API fusion. Study Ref: vespa-engine/vespa wiki.sd ColBERT patterns | Build hybrid search with pgvector RRF. Implement Elasticsearch ELSER. Compare BM25 vs dense vs sparse vs hybrid recall | Trapping Rain Water | hybrid_search_arch.py |
| 44 | **Redis for AI: VSET & FT.HYBRID**: Native VSET data type + VSIM command for sub-millisecond similarity. FT.HYBRID fusing lexical + vector ranking in single pipeline — COMBINE RRF (tunable WINDOW, CONSTANT) vs COMBINE LINEAR. Multi-tier caching strategy. Study Ref: redis/redis, redis-developer/sql-redis | Implement VSIM search. Build FT.HYBRID with RRF and LINEAR fusion. Measure latency improvement vs two-phase approach | Largest Rectangle in Histogram | redis_vset.py |
| 45 | **Distributed Vector Databases: Milvus Architecture**: Component decoupling — Knowhere, Proxy, QueryNode, IndexNode. GuaranteeTs and message queue time ticks for read visibility. Consistency_level tuning (Strong, Bounded Staleness, Session, Eventual). Clustering Compaction to prevent segment fragmentation | Deploy Milvus standalone. Configure consistency levels. Measure read latency under different consistency settings. Trigger compaction | Course Schedule II | milvus_architecture.py |
| 46 | **Agent Security + Ollama + AWS ECS Deploy**: Agno dual-schema (read-only transactions) + JWT isolation + Ollama local deployment. Guardrails + NeMo for safety | PostgreSQL read_only scopes. Deploy local LLM. Guarded cloud deploy | Trapping Rain Water review | security_deploy.py |

### Phase 6: AI Infrastructure & Production MLOps (Days 47-56)
*Goal: Master inference optimization, caching, feature stores, model registries, CI/CD for AI, observability, streaming architectures, and mock interviews*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 47 | **Real-Time Streaming Agent Architectures**: Northbound interface design — SSE and WebSockets for token-by-token streaming. State management in streams (agent reasoning traces, intermediate tool calls). Gateway strategies: connection pooling, bidirectional gRPC, handling drops | Build real-time streaming agent endpoint with SSE. Visualize token-by-token output | Find Min Rotated + Search in Rotated Array | streaming_architecture.py |
| 48 | **MLOps & Production ML Infrastructure**: Feature Stores (Feast/Tecton — offline batch + online streaming pipelines, point-in-time joins to prevent training-serving skew). Model Registries (MLflow lifecycle vs DVC Git-native versioning). A/B Testing for LLM outputs. **Prompt Management**: DSPy compilation, Vellum/Promptfoo for A/B testing prompt variants, shadow deployments | Design feature store dual-pipeline. Build MLflow tracker + DSPy compiled prompt pipeline. Shadow-deploy prompt variants | Subsets | mlops_prompt_mgmt.py |
| 49 | **AI Observability & MCP Security**: Monitoring latency p50/p95/p99, distributed tracing (Langfuse, LangSmith). Concept/data drift detection (Prometheus + Grafana). **MCP Threat Models**: Preventing Confused Deputy attacks, mTLS for server-to-server trust, prompt injection via tool output sanitization, containerized MCP server isolation. OAuth 2.1, OWASP MCP Top 10, per-client consent | Design monitoring dashboard. Build secure MCP proxy with mTLS + token exchange + output sanitization | Serialize/Deserialize Tree | observability_mcp_security.py |
| 50 | **Inference Optimization & Multi-Tenant Caching**: vLLM PagedAttention mechanics (logical KV → physical GPU memory pages, eliminating fragmentation to <8 tokens/seq). Continuous batching at iteration level. Token-aware rate limiting (Sliding Window Log, Token Bucket). **Multi-Tenant Isolation**: Silo/Pool/Bridge models. Row-level security in pgvector. Tenant-aware Redis LangCache (tenant_id namespaces, prevent cross-tenant leakage) | Diagram PagedAttention scheduler. Implement Sliding Window Log rate limiter. Build tenant-aware cache with isolation validation | Word Ladder | inference_multitenant.py |
| 51 | **Tripartite Agent Memory & Temporal Graphs**: Failure of flat vector stores for agent state. **Cognee** (graph-native memory control plane), **Neo4j** (Short-Term/Long-Term/Reasoning memory), **Graphiti** (bi-temporal knowledge graphs — valid time vs ingestion time), **AgentMemory** (MCP-integrated procedural memory with Ebbinghaus temporal decay). POLE+O ontology extraction (Person, Org, Location, Event, Object). Study Ref: topoteretes/cognee, rohitg00/agentmemory, getzep/graphiti | Design agent memory loop: parse observations → POLE+O extraction → Long-Term graph with provenance → Reasoning decision traces. Implement temporal decay pruning | Permutations | tripartite_memory.py |
| 52 | **MOCK: LLM Theory & RAG Architecture** (Strictly Verbal) + **Behavioral Integration**: Practice "Tell Me About Yourself" + Termination narrative | Answer Q&A from interview bank. Record and refine tone/pacing | Combination Sum | mock_verbal.md |
| 53 | **MOCK: Pair Programming** (Live coding — enforce "thinking out loud" protocol) | Build a mini streaming agent under time pressure with continuous vocalization | Clone Graph | mock_pair.md |
| 54 | **MOCK: System Design** (Whiteboarding RAG ingestion pipelines + LLM Gateway architectures) | Draw 5-step flow. Practice trade-off articulation | Number of Islands + Max Area | mock_sysdesign.md |
| 55 | **MOCK: Behavioral Integration & Portfolio Defense** + **Take-Home Simulation** (6-hour continuous block) | Build full MVP: FastAPI + LangGraph + MCP server | Redundant Connection | mock_takehome/ |
| 56 | **APPLY BLITZ + Mock Review**: Wellfound (20 apps) + YC (10) + LinkedIn DMs (10). Review mock recordings | Personalized messages with both projects. Iterate based on mock feedback | Evaluate Reverse Polish Notation | apply_review.md |

### Phase 7: Agentic Orchestration, MCP & Advanced Tools (Days 57-60)
*Goal: Final capstone polish, apply blitz, offer evaluation*

### Phase 7: Agentic Orchestration, MCP & Advanced Tools (Days 57-60)
*Goal: Final capstone polish, apply blitz, offer evaluation. Master LangGraph/CrewAI/AutoGen, A2A vs MCP protocols, Ollama, Claude Code, OpenClaw, Headroom*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 57 | **Advanced Agent Patterns**: Self-reflection loops, multi-tool use, hierarchical planning, multi-agent debate. **Multi-Agent Orchestration Comparison**: LangGraph (stateful production) vs CrewAI (rapid role-based) vs AutoGen (conversational debate). **Protocol Design — A2A vs MCP**: Horizontal agent delegation (A2A — JSON-RPC 2.0, Agent Cards, capability discovery) vs vertical tool integration (MCP). Blended architectures. Study Ref: crewAIInc/crewAI, a2aproject/A2A, FareedKhan-dev/all-agentic-architectures, alirezadir/Agentic-AI-Systems | Build self-reflecting agent. Compare framework topologies. Implement A2A card discovery + MCP tool call in same system | Implement Trie (Prefix Tree) | agent_patterns_a2a.py |
| 58 | **PROJECT 2 BUILD**: Autonomous Code & Web Intelligence Swarm — Blackboard pattern + Researcher (browser-use + Playwright + Firecrawl) + Coder (Daytona sandbox). **Tripartite Agent Memory**: Neo4j/Cognee (Short/Long/Reasoning, POLE+O). **Visual Workflow Builders**: n8n, Langflow, Dify for rapid prototyping. **Ollama** for local LLM serving | Build Blackboard with namespaces. Initiate agents with tripartite memory. Prototype workflow visually in n8n | Time Based Key-Value Store | project2_start/ |
| 59 | **PROJECT 2 continued**: MCP servers with OAuth 2.1 + **Advanced MCP** (streaming tools, resource subscriptions, Sampling for server-initiated LLM calls, Roots for directory boundaries). **Claude Code** integration + **Docker + GitHub Actions + AWS ECS**. **Token Compression**: Headroom (60-95% reduction) | Implement MCP Sampling + Headroom compression + CI/CD. Deploy. Study Ref: anthropics/claude-code | Largest Rectangle in Histogram | project2_continue/ |
| 60 | **PROJECT 2 DONE**: LLM-as-a-judge regression + Deploy + README with architecture diagrams + **APPLY BLITZ**: Wellfound (20) + YC (10) + LinkedIn DMs (10) | Production-grade project with docs. Personalized messages with both projects | Course Schedule II review | project2_done/ |

---

### Phase 8: Scalable Agentic System Design (Post-60-Day — Interview Deep Dive)
*Goal: Master distributed systems for AI, advanced rate limiting, A2A/MCP protocol architectures, disaster recovery, and system design interview frameworks. Study these topics after securing interviews.*

| Topic | Morning (2hr) | Afternoon (2hr) | Key Deliverable |
|-------|--------------|-----------------|-----------------|
| **Distributed Systems Fundamentals for AI** | CAP Theorem and Eventual Consistency for distributed agent memory and vector replication. Message Queues (Kafka/RabbitMQ) for background inference tasks and document ingestion | Circuit Breakers and Retry Logic for fault-tolerant LLM API gateways. Idempotency in Agent Actions (preventing double-execution of tool calls during retries) | distributed_systems_ai.md |
| **Advanced Rate Limiting & Load Balancing** | Token Bucket vs Leaky Bucket vs Sliding Window Log (memory cost, fairness, burst tolerance). Load balancing for inference servers (round-robin, least connections, request routing) | Model Routing vs Single Frontier Model — latency vs cost trade-offs. Token-aware rate limiting for GPU concurrency | rate_limiting_models.md |
| **Protocol Architecture Deep Dive** | A2A Protocol: Agent Cards, capability discovery, JSON-RPC 2.0, multi-part modal messages, stateful long-running tasks. MCP: Roots, Sampling, streaming tools, subscriptions | Blended architectures: orchestrator uses A2A for horizontal delegation, workers use MCP for vertical tool access. Security: mTLS, sender-constrained tokens | protocol_architecture.md |
| **Multi-Tenant AI Platform Design** | Silo/Pool/Bridge isolation models. Tenant-aware caching (namespace isolation, prevent cross-tenant leakage). Row-level security in pgvector. Tenant-specific LoRA adapters | Capacity planning: memory footprint for HNSW at scale, peak QPS calculations, back-of-envelope estimations for interviews | multi_tenant_design.md |
| **Disaster Recovery & Failover** | Multi-region deployment for AI systems. Database replication strategies. Agent state recovery after crashes. Handling LLM API provider outages (fallback models) | Designing for graceful degradation: cache fallbacks, model fallback chains, degraded response strategies | dr_failover.md |
| **System Design Mock I** | Full mock: "Design a RAG system for 10M QPD with multi-modal data" | Full mock: "Design a secure multi-agent system with A2A + MCP" | system_design_mock_1.md |
| **System Design Mock II** | Full mock: "Design an LLM inference serving platform for 500 concurrent users" | Full mock: "Design a feature store for real-time recommendations (50ms p99)" | system_design_mock_2.md |

---

## 📋 2 Projects to Build (Market-Aligned) — Architecture Documentation Requirements

### Project 1 (Days 29-31): Multi-Tenant Enterprise Knowledge Agent
**Tech Stack:** FastAPI + pgvector (RLS) + **pgvectorscale (DiskANN)** + LangGraph + MCP + Mem0 + Graphiti + Cross-encoder + Hybrid Search + Docker + AWS ECS + LangSmith/Ragas
**Features:**
- Agno-style dual-schema architecture: read-only transaction scopes for data-analyst agents, isolated schema for engineer agents
- JWT-based RBAC for strict multi-tenant isolation
- **pgvectorscale StreamingDiskANN** for handling 10M+ document chunks on SSDs without RAM exhaustion
- **Hybrid Search with RRF**: BM25 + pgvector + tsvector fused via Reciprocal Rank Fusion
- **Metadata pre-filtering**: iterative index scans (hnsw.max_scan_tuples) to prevent recall collapse under multi-tenant constraints
- Temporal Knowledge Graphs (Graphiti) for relational entity tracking over time
- Mem0 for user-scoped semantic memory with automated fact deduplication and contradiction resolution
- Corrective RAG (CRAG) with evaluator → web search fallback
- Comprehensive Ragas evaluation + LLM-as-a-judge regression testing
- **Interview signal:** "Hire me" — shows architectural maturity, security awareness, and production thinking at billion-vector scale

### Project 2 (Days 54-56): Autonomous Code & Web Intelligence Swarm
**Tech Stack:** FastAPI + LangGraph (Blackboard pattern) + browser-use + Firecrawl + Daytona + MCP (OAuth 2.1) + Next.js/TypeScript + **Neo4j/Cognee tripartite memory** + Docker + AWS ECS + GitHub Actions
**Features:**
- **Blackboard shared-memory architecture** with optimistic locking — agents write to namespaces (research/, code/) with thread-safe locks, maintain private scratchpads
- **Researcher Agent**: browser-use + Playwright for visual DOM understanding, multi-tab SPA navigation; Firecrawl for LLM-ready markdown extraction and anti-bot bypass
- **Coder Agent**: executes Python data-transformation workflows strictly inside isolated, ephemeral Daytona sandboxes (dedicated kernel, network isolation)
- **Tripartite Agent Memory via Neo4j/Cognee**: Short-Term (conversational state), Long-Term (POLE+O knowledge graph with bi-temporal provenance), Reasoning (decision trace history)
- **Temporal decay function** applied to short-term conversations; Ebbinghaus forgetting curves via AgentMemory MCP hooks
- **MCP servers secured via OAuth 2.1** — token exchange, no token passthrough, per-client consent registries
- **LLM-as-a-judge regression testing** — catches infinite tool-calling loops, context drift, silent failures
- Full CI/CD pipeline (push → test → eval → deploy) + cost tracking middleware
- **Interview signal:** "Full-stack AI Engineer" — end-to-end delivery with enterprise security, tripartite memory, and temporal decay

### 📐 Project 1 — Architecture Documentation Requirements
The README MUST include:
- **Component Diagram**: Visually mapping ingestion pipeline (parsers, embedding models), storage layer (vector DB, object storage), and serving layer (API gateway, LLM)
- **Data Flow Definition**: Point-in-time consistency strategies, handling late-arriving events
- **Capacity Planning**: Back-of-envelope calculations for memory footprint (RAM for 1M vectors in HNSW) and peak QPS throughput
- **Tenant Isolation Strategy**: Row-level security implementation, tenant-aware cache key design

### 📐 Project 2 — Architecture Documentation Requirements
The README MUST include:
- **State Machine Diagram**: Node transitions, conditional edges, HITL checkpoints using standard flowchart notation
- **Protocol Specifications**: Which interactions use A2A (horizontal negotiation) vs MCP (vertical tool execution)
- **Security Threat Model**: Mitigations for prompt injection, ambient authority escalation, cross-tenant data leakage in agent logs
- **CI/CD Pipeline Design**: Token-budget regression tests, deterministic evaluation gates for automated deployment

---

## 🎯 Application Strategy

| Milestone | When | Where | What to Show |
|-----------|------|-------|-------------|
| **Internship apply blitz** | Day 31 | Wellfound + YC Work at a Startup | Project 1 deployed + GitHub profile |
| Ongoing applications | Days 32-56 | LinkedIn DMs + X (Twitter) DMs | Projects + technical content |
| **FT apply blitz** | Day 57 | Wellfound + YC + LinkedIn | Both projects deployed + full tech stack |
| Offer evaluation | Day 59-60 | Compare CTC vs cash vs equity | Market research benchmarks |

---

## 🚫 What We're Skipping (Research-Validated)

| 🚫 Skip / Reinstated | What Changed |
|--------------|----------------|
| Training CNNs/RNNs from scratch | Still skip — zero JD mentions. Pre-trained models via APIs is the standard |
| Deep ML math (backpropagation derivation) | Still skip — not tested in AI Engineer interviews |
| Django / Flask | Still skip — FastAPI has near-total dominance in AI engineering |
| Pandas/NumPy as full week | Still skip — moved to 1-day Good-to-Have |
| Apna.co as primary platform | Still skip — low signal, legacy IT, fake AI listings |
| **Coin Change, LIS, Word Ladder, Trapping Rain Water, Largest Rectangle** | **REINSTATED** — per Noida tech hub interview data (Adobe, Microsoft). DP for RL state-space, monotonic stack for production optimization, BFS for graph routing |
| **Naive RAG (fixed-size chunking)** | Still skip — replaced by Proposition Generation, Step-back, GraphRAG |
| **InMemorySaver for LangGraph** | Still skip — restricted to testing only. PostgresSaver mandatory |
| **Static API keys for MCP** | Still skip — OWASP MCP Top 10 vulnerability. OAuth 2.1 mandatory |
| **Manual prompt engineering as primary skill** | Still skip — replaced by DSPy + GEPA |
| **ChromaDB for production** | Downgraded to prototype-only. Use pgvector/DiskANN for production |

---

## 📊 Compensation Targets (Research-Validated)

| Milestone | Target | Evidence |
|-----------|--------|----------|
| Internship | ₹30-50k/mo | Hungama (₹50k), Aight (₹25-50k), SuperKalam (₹25-40k), Peakflo (₹40-50k) |
| India FT | ₹10-12 LPA (₹80k-₹1L/mo in-hand) | Hungama PPO ₹12-15 LPA, market median ₹9-11 LPA |
| Global Remote FT | $24k-$40k/yr (₹20L-₹34L/yr) | Smart Audit ($25-50k/yr), Great Question, Peakflo |


---

## 🏗️ Portfolio Spec: ₹30k vs ₹80k Level

### ₹30k Intern Level (Day 28)
- Basic RAG pipeline with LangChain + basic vector DB
- Manual testing, basic error handling
- Simple README with install + run instructions

### ₹80k FT Level (Day 60) — "Enterprise Orchestrator"
- **LangGraph** with dual-channel memory, **PostgresSaver**, **Send API**, **interrupt()** HITL pattern
- **MCP Server** with **OAuth 2.1**, **Sampling**, **Roots**
- **CrewAI** for rapid role-based prototyping
- **CI/CD pipeline** with LLM-as-a-judge: fail build if infinite loops, faithfulness < 0.85, context drift > 15%
- **Tripartite Agent Memory**: Neo4j/Cognee (Short/Long/Reasoning), POLE+O extraction, Ebbinghaus temporal decay
- **browser-use** + **Firecrawl** for web automation
- **Daytona sandbox** for safe code execution
- **RAGFlow DeepDoc** for enterprise document parsing
- **Ollama** for privacy-preserving local LLM
- **Claude Code** agentic coding acceleration
- **OpenClaw** local agent gateway
- **Headroom** token compression (60-95%)
- **Guardrails** + **NeMo** + **AgentShield** for security
- **Redis VSET/FT.HYBRID** semantic caching + agent state
- **pgvectorscale DiskANN** for billion-scale vector search
- **tsvector + pgvector + RRF** hybrid search
- **README** with: Mermaid.js architecture diagram, documented trade-offs ("Why pgvector over Pinecone"), quantitative metrics (p50/p95 latency, Faithfulness/Context Precision via Ragas)

### 📖 Narrative Architecture: "Tell Me About Yourself"
**Optimal Structure:** "I am an AI Engineer focused on bridging the gap between raw LLM capabilities and production-grade applications. While my foundation is in full-stack engineering, I've spent the last year specializing in Agentic workflows — specifically building stateful applications using LangGraph and standardizing external tool integrations via the Model Context Protocol. I thrive in high-velocity startup environments where I can own the entire architecture, from the data ingestion pipeline to the final streaming inference endpoint."

### 📖 Termination Narrative
**Optimal Structure:** "My previous role provided an excellent foundation in robust backend systems, but the company's trajectory moved away from deep AI integration. I am targeting seed-to-Series-B startups because I want to be closer to the architectural decision-making process, specifically involving generative AI, multi-agent infrastructure, and RAG optimization."

### 📖 Wellfound Profile Optimization
- **Headline:** "AI Engineer | LangGraph, MCP, & RAG Architecture | Building Stateful AI Systems"
- **Skills:** Python, FastAPI, LangGraph, Model Context Protocol, Vector Databases (Qdrant/Milvus), PostgreSQL, TypeScript
- **Project Descriptions:** Quantifiable metrics — "Reduced context latency by 40% via Redis semantic caching"

---

## 🎯 AI-Specific DSA Strategy

### Mock Interview Framework (1-Hour Structure)
| Time | Phase | Objective |
|------|-------|-----------|
| 00:00-05:00 | Constraint Identification | Clarify boundaries: data types, edge cases, memory limits ("Are edges guaranteed to form a DAG?") |
| 05:00-15:00 | Architectural Proposal | Propose brute-force baseline Big-O, immediately pivot to optimized approach (e.g., identify overlapping subproblems → memoization) |
| 15:00-45:00 | Implementation | Write code with continuous vocalization. Silence = failure. Explain each block's logic as written |
| 45:00-60:00 | Validation & Optimization | Manual dry-run on edge-case input. Discuss space complexity optimizations |

### Handling Unseen Problems (Communication Protocol)
**Script:** "I haven't encountered this exact formulation, but the structural constraints map closely to [Pattern X — e.g., Topological Sort or BFS]. Let me outline the base case for the recursion tree, and we can identify how to prune the state space efficiently."

### Top 10 High-Frequency DSA Problems for AI Engineering
| Problem | Pattern | AI Engineering Relevance |
|---------|---------|--------------------------|
| Serialize/Deserialize N-ary Tree | Tree Traversal | State checkpoints, saving agent execution graphs to databases |
| LRU Cache | Linked List + Hash | KV caching in Transformer architectures |
| Course Schedule I/II | Topological Sort (Graph) | Dependency resolution in multi-agent workflows |
| Design Add and Search Words | Trie | Prompt prefix matching, structured decoding |
| Merge Intervals | Array / Sorting | Time-series log analysis, token boundary alignment |
| Find Median from Data Stream | Heap / Priority Queue | Dynamic latency calculations in concurrent API gateways |
| Word Ladder | BFS | Optimal pathfinding, state-space search in multi-step AI planning |
| Clone Graph | Graph Traversal | Deep-copying complex state objects without reference mutation |
| K Closest Points to Origin | Heap / Sorting | Exact and approximate nearest neighbor (ANN) vector search |
| Design Hit Counter | Sliding Window / Queue | API rate limiters and token bucket algorithms in LLM gateways |

### Spaced Repetition Protocol
- Starting Day 25: Mandatory **15-minute daily flashcard review** of the Interview Question Bank (see vs_code_context.md)
- Continue indefinitely through Day 60

---

## 🎯 Advanced Theory Focus Areas (Phase 3 Supplement)

### Chip Huyen's DMLS Integration
- Skip chapters on basic tabular feature engineering
- Concentrate on: Data Distribution Shifts, Evaluation Protocols (Offline vs Online metrics), Model Deployment Strategies (Canary vs Shadow)

### Autograd & Deep Learning Fundamentals
- Deep learning frameworks = 3 operation types: elementwise, reductions (aggregations like SUM), movement (tensor reshaping)
- Master: reverse-mode automatic differentiation — computation graphs traversed backward to compute gradients via chain rule ($\frac{\partial L}{\partial x} = \frac{\partial L}{\partial y} \cdot \frac{\partial y}{\partial x}$)

### Essential Research Papers for Interview Defense
- **Attention Is All You Need**: Exact matrix operations for self-attention. Why scores are scaled by $\sqrt{d_k}$ (pushes softmax out of near-zero gradient regions)
- **DeepSeek-V3 Technical Report**: FP8 mixed precision training, MTP for speculative decoding, MLA for KV cache bottleneck
- **InstructGPT / RLHF**: SFT → Reward Model → PPO pipeline

### Hands-On Translation
- LoRA/QLoRA exercises → link to VRAM constraint interview answers. Articulate how PEFT drastically reduces optimizer state memory

---

## 📚 Study References (Curated Repos — Integrated into Daily Plan)

---

## 📚 Study References (Curated Repos — Integrated into Daily Plan)

| Repository | Phase/Day | What to Study |
|-----------|-----------|---------------|
| facebookresearch/faiss | Phase 5 Day 43 | Index algorithm comparison: IVF, HNSW, PQ, IVF+HNSW hybrid |
| nmslib/nmslib | Phase 5 Day 43 | Non-metric space library, HNSW variants, benchmark comparisons |
| deepseek-ai/DeepSeek-V3 | Phase 3 Day 29 | MLA architecture, MoE routing, Multi-Token Prediction internals |
| trekhleb/homemade-machine-learning | Phase 3 Day 25 | Math foundations, classical ML implementations from scratch |
| scikit-learn/scikit-learn | Phase 3 Day 26 | Classical ML: Logistic Regression, Random Forest, XGBoost, K-Means, PCA |
| karpathy/minGPT | Phase 3 Day 28 | Minimal transformer implementation, attention mechanics |
| infiniflow/ragflow | Phase 4 Day 32 | DeepDoc layout-aware parsing, visual RAG pipeline |
| crewAIInc/crewAI | Phase 7 Day 54 | Role-based agent assembly, task delegation, process flows |
| ollama/ollama | Phase 5 Day 45 | Local LLM deployment, API serving, model management |
| anthropics/claude-code | Phase 7 Day 56 | Agentic coding, CLAUDE.md context injection, MCP connectivity |
| openclaw/openclaw | Phase 7 Day 57 | Local agent gateway, AGENTS.md/SOUL.md workspace state management |
| headroomlabs-ai/headroom | Phase 7 Day 58 | ContentRouter/SmartCrusher token compression algorithms |
| addyosmani/agent-skills | Phase 7 Day 57 | Reusable agent skill patterns, workflow packaging |
| n8n-io/n8n | Phase 7 Day 55 | Visual AI workflow automation, rapid prototyping |
| langflow-ai/langflow | Phase 7 Day 55 | Drag-and-drop agent builder for stakeholder demos |
| langgenius/dify | Phase 7 Day 55 | Full-stack AI app platform, rapid prototyping |
| open-webui/open-webui | Phase 7 Day 54 | Self-hosted ChatGPT alternative for local testing |
| google-gemini/gemini-cli | Phase 7 Day 54 | CLI-based agent interaction for DevTools workflows |
| williamfiset/Algorithms | Phase 1-2 | Foundational DSA implementations, graph algorithms |
| jwasham/coding-interview-university | Phase 1-2 | Comprehensive DSA study roadmap |
| ed-donner/agents | Phase 7 Day 54 | Week 4: LangGraph multi-agent routing templates |
| NirDiamant/Agent_Memory_Techniques | Phase 4 Day 34 | Notebooks 24-27: Mem0, Graphiti, Procedural Memory |
| NirDiamant/rag_techniques | Phase 4 Day 33 | Proposition Generation, Step-back Prompting patterns |
| NirDiamant/GenAI_Agents | Phase 7 Day 54 | Agent architectures, tool-use patterns, multi-agent patterns |
| punkpeye/awesome-mcp-servers | Phase 7 Day 56 | Real-world MCP server implementations, OAuth 2.1 integrations |
| modelcontextprotocol/servers | Phase 7 Day 56 | Canonical MCP reference implementations |
| OpenBMB/ToolBench | Phase 7 Day 54 | DFSDT algorithm, ToolEval metrics |
| firecrawl/firecrawl-workflows | Phase 7 Day 55 | Outcome-focused business skills for agents |
| EthicalML/awesome-production-agentic-systems | Phase 6 Day 48 | CI/CD, AIBOM, observability tooling |
| openai/openai-agents-python | Phase 7 Day 54 | Agent handoffs, manager pattern, voice streaming |
| browser-use/browser-use | Phase 7 Day 55 | Visual DOM, multi-tab navigation, Playwright |
| daytonaio/daytona | Phase 7 Day 55 | Python SDK for sandbox creation, ephemeral execution |
| guardrails-ai/guardrails | Phase 5 Day 46 | Input/output validators, PII detection, schema compliance |
| agno-agi/agno | Phase 5 Day 45 | Dual schema enforcement, JWT-based RBAC patterns |
| ashishps1/learn-ai-engineering | Phase 6 | System design interview prep, architecture blueprints |
| Shubhamsaboo/awesome-llm-apps | Phase 4 | Real-world LLM application patterns, RAG variants |
| NousResearch/hermes-agent | Phase 1 Day 17 | DSPy + GEPA integration patterns for prompt evolution |
| **donnemartin/system-design-primer** | **Phase 8** | Rate limiting algorithms, load balancing, cache eviction policies — map to vLLM/Semantic Caching |
| **a2aproject/A2A** | **Phase 7 Day 54** | Agent-to-Agent protocol: Agent Cards, capability discovery, JSON-RPC 2.0 |
| **FareedKhan-dev/all-agentic-architectures** | **Phase 7 Day 54** | 35 agent patterns (Reflexion, LATS, Meta-Controller). Implement deterministic-picker pattern |
| **alirezadir/Agentic-AI-Systems** | **Phase 7 Day 54** | Multi-agent state management and reasoning loops chapter mapping |
| **iusztinpaul/designing-real-world-ai-agents-workshop** | **Phase 7 Day 57** | End-to-end Deep Research Agent as MCP server using FastMCP + Opik evaluations |
| **NirDiamant/agents-towards-production** | **Phase 7 Day 58** | Docker deployment, PII sanitization pipelines, security guardrails for capstone |
| **omBharatiya/ai-system-design-guide** | **Phase 6, Phase 8** | AI system design interview questions and architecture blueprints |
| **labuladong/fucking-algorithm** | **Phase 1-2** | DSA problem-solving frameworks, pattern-based algorithm mastery |
| **binhnguyennus/awesome-scalability** | **Phase 8** | Scalability patterns, system design interview prep for high-throughput systems |
| **KalyanKS-NLP/LLM-Interview-Questions** | **Phase 3, Phase 6** | LLM interview questions with answers, theory deep dives |
| **ombharatiya/AI-Engineer-Interview-Questions** | **Phase 6** | AI Engineer specific interview questions compilation |
| **chiphuyen/dmls-book** | **Phase 3** | Designing Machine Learning Systems — production ML patterns |
| **HandsOnLLM/Hands-On-Large-Language-Models** | **Phase 3, Phase 4** | Practical LLM exercises that translate to interview answers |
| **mli/paper-reading** | **Phase 3 Day 28-29** | Key papers to study: Attention Is All You Need, DeepSeek-V3, etc. |

---

## 🏛️ Design Patterns for AI Engineers

| Pattern | When to Use |
|---------|-------------|
| **ReAct** (Reason + Act) | Exploratory tasks with dynamic API interaction |
| **Plan-and-Execute** | Complex long-horizon tasks needing decomposition |
| **Evaluator-Optimizer** | Code generation, data extraction requiring high accuracy |
| **Tool-Use** | Structured data extraction with function calling |
| **Multi-Agent (Supervisor)** | Multiple specialized agents routed by a central LLM |
| **MCP Integration** | Secure enterprise tool access via OAuth 2.1, no hardcoded APIs |
| **Agentic RAG** | Dynamic retrieval where agent rewrites queries if results poor |
| **Blackboard System** | Multi-agent shared memory with namespaces, optimistic locking, private scratchpads |
| **Dual Schema Enforcement** | Read-only transaction scopes for data agents, isolated schemas for engineer agents |
| **Send API Fan-out** | Parallel dispatch to multiple specialist agents from a single supervisor |
| **Hash-based Idempotent Recompute** | Skip redundant LLM calls by caching outputs keyed by input hash |
| **Procedural Memory** | Extract parameterized workflow templates from successful execution traces |

---

## 🛡️ Post-2-Month Roadmap

| Phase | Months | Salary Target | Focus |
|-------|--------|---------------|-------|
| Months 3-6 | Jul-Oct | ₹1-1.5L/mo | Open source (LangChain, MCP), fine-tuning (LoRA/QLoRA), advanced MLOps |
| Months 6-12 | Oct-Mar | ₹2L+/mo | Distributed systems, Kafka, multi-modal AI, vLLM/TensorRT-LLM inference serving |

---

## 📚 Interview Q Bank (25 questions)
[Included in full plan — LLM/RAG, LangGraph, MCP, System Design, ML/NLP, Production Patterns]

## 🚨 Risk Mitigation
| Risk | Mitigation |
|------|-----------|
| DSA deficit | 1hr/day every single day. 30-50 targeted problems. |
| Terminated internship | Frame as "backend vs AI misalignment." Control narrative early. |
| Tutorial Hell | Unique problem + live deploy + eval scores + architecture docs. |
| Application black holes | Apna (chat), Wellfound (founder DMs). Skip traditional portals. |

---

*Based on Gemini Deep Research: Architecting the Agentic AI Engineer (Jul 2026)*
