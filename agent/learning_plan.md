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
| 🔴 Must-Know | SQL & Vectors | PostgreSQL, pgvector, **pgvectorscale (DiskANN)** for SSD-optimized billion-scale vectors, HNSW vs IVFFlat vs DiskANN indexing, vector similarity search, **read-only transaction scopes**, **Recursive CTEs** for tree traversal, **tsvector full-text search + Reciprocal Rank Fusion** for hybrid retrieval |
| 🔴 Must-Know | DSA | **Pareto 50+** — Arrays & Hashing, Two Pointers, Sliding Window, Stack & Queue, Binary Search, Linked Lists, Trees (BFS/DFS), Graphs (BFS/DFS/Topo Sort/Cycle Detection), Intervals, Backtracking, Heaps, Design (LRU Cache, Trie, Time-Based KV), **DP (Coin Change, LIS, Climbing Stairs)**, **Monotonic Stack (Largest Rectangle, Trapping Rain Water)**, **BFS Shortest Path (Word Ladder)**. **Probabilistic Data Structures**: Bloom filters, HyperLogLog. **Dimensionality Reduction**: matrix multiplication complexity for attention |
| 🔴 Must-Know | Local LLM Deployment | **Ollama** — run LLMs locally for development, privacy-preserving deployment, data sovereignty compliance (critical for Indian enterprise/fintech) |
| 🔴 Must-Know | Enterprise RAG Engine | **RAGFlow** — DeepDoc module for layout-aware document parsing (tables, headers, multi-column, OCR), visual RAG pipeline builder |
| 🔴 Must-Know | Token Optimization | **Headroom** — content-aware compression (JSON, AST, prose) reducing token overhead 60-95% before LLM processing |
| 🔴 Must-Know | Local Agent Gateway | **OpenClaw** — multi-channel agent gateway, AGENTS.md/SOUL.md workspace state management, local-first orchestration |
| 🔴 Must-Know | Agentic Coding | **Claude Code** — agentic coding tool, CLAUDE.md workspace context injection, automated three-phase loop (gather → act → verify) |
| 🟡 Good-to-Have | Visual Workflow Builders | **n8n**, **Langflow**, **Dify** — rapid prototyping and stakeholder demonstrations; not for production agent workflows |
| 🟡 Good-to-Have | Self-Hosted Chat UI | **Open WebUI** — offline-capable ChatGPT alternative for local testing |
| 🟡 Good-to-Have | Full-Stack | **Next.js + TypeScript** (unlocks Full Stack AI Engineer roles — premium pay for end-to-end delivery) |
| 🟡 Good-to-Have | Data | Pandas, NumPy basics |
| 🟡 Good-to-Have | Interview Theory | Transformer architecture (Q, K, V, self-attention, RoPE), BERT vs GPT, tokenization (BPE/WordPiece/Unigram/SentencePiece), LLM inference architecture (vLLM, KV cache), **MCP OWASP Top 10**, **Procedural vs Episodic vs Semantic Memory**, **Blackboard Architecture**, **DeepSeek-V3 (MLA, MoE) internals**, **Classical ML (Logistic Regression, Random Forest, XGBoost, K-Means, PCA)** |
| ⚪ Nice-to-Have | Fine-tuning | LoRA / PEFT — 8.5% JD mention vs RAG 35.9%. Read 1 article for concept only |
| 🟡 Good-to-Have | Prototype-Only | **ChromaDB** — excellent for rapid local prototyping. NOT for production. **CrewAI** — rapid role-based assembly, not for stateful production. **n8n/Langflow/Dify** — visual prototyping only |
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
| 20 | Vector DBs, Embeddings, ChromaDB (prototype-only), HNSW vs IVFFlat | Store chunks + similarity search + index tuning | Valid Parentheses | chroma_ingestion.py |
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
*Goal: Master vector indexing strategies, hybrid search, recursive CTEs, Redis caching, and production database comparisons*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 40 | **Vector Indexing Deep Dive**: HNSW tuning (m, ef_construction, ef_search) for <10M vectors + active writes. IVFFlat tuning (lists, probes) for memory constraints. **DiskANN via pgvectorscale** for SSD-optimized Vamana graph — billion-scale | Benchmark HNSW vs IVFFlat vs DiskANN on same dataset. Measure recall vs QPS vs memory | Kth Largest in Stream | vector_indexing.py |
| 41 | **Vector DB Production Comparison**: pgvector vs Pinecone vs Qdrant vs Milvus vs Weaviate — deployment cost, infra overhead, latency benchmarks. When to choose what | Decision tree analysis + cost projection for different scale scenarios | K Closest Points to Origin | vector_db_comparison.md |
| 42 | **SQL Optimization for AI**: Recursive CTEs (WITH RECURSIVE) for traversing semantic hierarchies and document chunk trees. Partition pruning for multi-tenant RAG | Write recursive queries on hierarchical data. Set up table partitioning | Best Time to Buy/Sell Stock | sql_optimization.sql |
| 43 | **PostgreSQL Hybrid Search**: Fusing pgvector semantic similarity (cosine/L2) with tsvector full-text search via Reciprocal Rank Fusion (RRF). Study Ref: facebookresearch/faiss, nmslib/nmslib | Build hybrid search endpoint. Compare recall vs pure semantic | Trapping Rain Water (monotonic stack mastery) | hybrid_search_rrf.py |
| 44 | **Redis for AI**: Semantic caching (LangCache) with cosine threshold 0.85-0.95. Agent session state storage. Vector search with redis-py. Multi-tier caching strategy | Implement Redis LangCache. Measure TTFT improvement | Largest Rectangle in Histogram (monotonic stack) | redis_caching.py |
| 45 | **Agent Security & RBAC**: Agno dual-schema (read-only transactions) + JWT isolation + **Ollama local deployment** for privacy-preserving dev | PostgreSQL read_only scopes. Deploy local LLM with Ollama. Study Ref: ollama/ollama | Course Schedule II | agent_security_ollama.py |
| 46 | **Agentic Threat Modeling**: AgentShield config scanning + NeMo Guardrails (Colang, topical bounding, jailbreak detection) + **AWS ECS Fargate** deploy | Scan configs for vulns. Deploy guarded agent to cloud | Trapping Rain Water review | threat_model_deploy.py |

### Phase 6: System Design & Production MLOps (Days 47-53)
*Goal: Feature stores, model registries, drift detection, load balancing, inference optimization, MCP security, memory architectures*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 47 | **High-Throughput RAG Architecture**: Scaling to 1M QPD — load balancing inference servers, rate limiting at AI gateway, CDN for static prompt assets/embeddings. **LangGraph scaling**: PostgresSaver, Send API, hash-based idempotent recompute | Architecture diagram for 1M QPD + parallel fan-out design | Find Min Rotated + Search in Rotated Array | rag_architecture.md |
| 48 | **MLOps & Production ML Infrastructure**: Feature Stores (prevent training-serving skew), Model Registries via MLflow/DVC, A/B Testing Infrastructure for LLM outputs | Design feature store schema. Build MLflow experiment tracker | Subsets | mlops_infra.md |
| 49 | **AI Observability & Drift Detection**: Monitoring latency p50/p95/p99, distributed tracing. Detecting concept/data drift via Prometheus + Grafana. **MCP Security**: OAuth 2.1, mTLS, OWASP MCP Top 10, per-client consent | Design monitoring dashboard. Build secure MCP proxy with token exchange | Serialize/Deserialize Tree | observability_mcp.md |
| 50 | **Semantic Caching & Data Layers**: Redis LangCache (cosine threshold 0.85-0.95) for LLM cost reduction. **Inference Optimization & Hardware Topology**: vLLM continuous batching, PagedAttention, KV cache, CUDA/GPU kernel constraints | Implement multi-tier cache. Diagram GPU memory hierarchy | Word Ladder (BFS shortest path) | caching_inference.md |
| 51 | **Agent Memory Architectures**: Procedural Memory (parameterized workflow templates from execution traces), Blackboard System (namespaces, optimistic locking, thread-safe locks). **NLP Concepts**: Transformer QKV, RoPE, BERT vs GPT, tokenization (BPE/WordPiece/Unigram/SentencePiece), MoE, speculative decoding | Design memory architecture + tiktoken counter + attention viz | Permutations | memory_nlp.py |
| 52 | **Live Coding Mock (FastAPI + LangGraph + MCP)** + Behavioral | Build mini agent under time pressure. Practice "termination narrative" + architecture trade-offs | Combination Sum | live_coding_mock/ |
| 53 | **DSA Mock + Portfolio Review + Apply Follow-ups** | Solve problems under time pressure. Polish GitHub. Respond to callbacks | Clone Graph | mock_interview_log |

### Phase 7: Agentic Orchestration, MCP & Advanced Tools (Days 54-60)
*Goal: Build Autonomous Code & Web Intelligence Swarm, master CrewAI/LangGraph complementarity, Ollama, Claude Code, OpenClaw, Headroom, MCP advanced features*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 54 | **Advanced Agent Patterns**: Self-reflection loops, multi-tool use, hierarchical planning, multi-agent debate. **Multi-Agent Orchestration Comparison**: LangGraph (stateful production) vs CrewAI (rapid role-based assembly) vs AutoGen (conversational debate). Study Ref: crewAIInc/crewAI, NirDiamant/GenAI_Agents | Build self-reflecting agent + compare framework topologies. **Open WebUI** for local testing | Implement Trie (Prefix Tree) | agent_patterns.py |
| 55 | **PROJECT 2 BUILD**: Autonomous Code & Web Intelligence Swarm — Blackboard pattern + Researcher (browser-use + Playwright + Firecrawl) + Coder (Daytona sandbox). **Visual Workflow Builders**: n8n, Langflow, Dify for rapid prototyping. **Ollama** for local LLM serving | Build Blackboard with namespaces. Initiate agents. Prototype workflow visually in n8n | Time Based Key-Value Store | project2_start/ |
| 56 | **PROJECT 2 continued**: MCP servers with OAuth 2.1 + **Advanced MCP** (streaming tools, resource subscriptions, Sampling for server-initiated LLM calls, Roots for directory boundaries). **Claude Code** integration for agentic coding acceleration | Docker + GitHub Actions + AWS ECS. Implement MCP Sampling. Study Ref: anthropics/claude-code | Largest Rectangle in Histogram | project2_continue/ |
| 57 | **PROJECT 2 DONE**: LLM-as-a-judge regression (catch infinite loops, context drift) + Deploy + README with architecture diagrams. **OpenClaw** local gateway (AGENTS.md, SOUL.md configs). **Agent Skills Ecosystem**: addyosmani/agent-skills patterns | Production-grade project with docs. Set up OpenClaw gateway. Package agent skills | Number of Islands + Max Area of Island | project2_done/ |
| 58 | **Token Compression & Optimization**: Headroom ContentRouter + SmartCrusher — compress JSON/AST/prose tool outputs by 60-95% before LLM processing. **Agent Observability**: tracing, logging, debugging loops. Track completion rate, cost/task, steps/task via LangSmith. **Memory Architectures**: Mem0, Graphiti, Redis for procedural state. AgentShield + NeMo for safety | Implement Headroom compression. Build LangSmith dashboard. Run AgentShield scan | Redundant Connection | optimization_observability.py |
| 59 | **APPLY BLITZ**: Wellfound (20 apps) + YC (10) + LinkedIn DMs (10). **Claude Code** MCP server connectivity for dev workflow | Personalized messages with both projects. Set up CLAUDE.md workspace context | Evaluate Reverse Polish Notation | apply_blitz_log.md |
| 60 | Follow-ups + Mock interviews + Offer evaluation | Respond to callbacks, negotiate offers. Compare CTC vs cash vs equity | Course Schedule II review | interview_tracker.md |

---

## 📋 2 Projects to Build (Market-Aligned)

### Project 1 (Days 29-31): Multi-Tenant Enterprise Knowledge Agent
**Tech Stack:** FastAPI + pgvector (RLS) + LangGraph + MCP + Mem0 + Graphiti + Cross-encoder + Hybrid Search + Docker + AWS ECS + LangSmith/Ragas
**Features:**
- Agno-style dual-schema architecture: read-only transaction scopes for data-analyst agents, isolated schema for engineer agents
- JWT-based RBAC for strict multi-tenant isolation
- Temporal Knowledge Graphs (Graphiti) for relational entity tracking over time
- Mem0 for user-scoped semantic memory with automated fact deduplication and contradiction resolution
- Corrective RAG (CRAG) with evaluator → web search fallback
- Parent-child chunking + cross-encoder reranking + Hybrid Search (BM25 + dense)
- Comprehensive Ragas evaluation + LLM-as-a-judge regression testing
- **Interview signal:** "Hire me" — shows architectural maturity, security awareness, and production thinking

### Project 2 (Days 54-56): Autonomous Code & Web Intelligence Swarm
**Tech Stack:** FastAPI + LangGraph (Blackboard pattern) + browser-use + Firecrawl + Daytona + MCP (OAuth 2.1) + Next.js/TypeScript + Docker + AWS ECS + GitHub Actions
**Features:**
- **Blackboard shared-memory architecture** with optimistic locking — agents write to namespaces (research/, code/) with thread-safe locks, maintain private scratchpads
- **Researcher Agent**: browser-use + Playwright for visual DOM understanding, multi-tab SPA navigation; Firecrawl for LLM-ready markdown extraction and anti-bot bypass
- **Coder Agent**: executes Python data-transformation workflows strictly inside isolated, ephemeral Daytona sandboxes (dedicated kernel, network isolation)
- **MCP servers secured via OAuth 2.1** — token exchange, no token passthrough, per-client consent registries
- **LLM-as-a-judge regression testing** — catches infinite tool-calling loops, context drift, silent failures
- Full CI/CD pipeline (push → test → eval → deploy) + cost tracking middleware
- **Interview signal:** "Full-stack AI Engineer" — end-to-end delivery with enterprise security and sandboxing

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
- Basic RAG pipeline with LangChain + ChromaDB
- Manual testing, basic error handling
- Simple README with install + run instructions

### ₹80k FT Level (Day 60) — "Enterprise Orchestrator"
- **LangGraph** with dual-channel memory (persistent + ephemeral scratchpad), **PostgresSaver** for durable checkpoints, **Send API** for parallel operations
- **MCP Server** with **OAuth 2.1 token exchange**, **Sampling** for server-initiated LLM calls, **Roots** for directory boundaries
- **CrewAI** for rapid role-based agent assembly (complementary to LangGraph for prototyping)
- **CI/CD pipeline** with LLM-as-a-judge: fail build if infinite loops detected, faithfulness < 0.85, or context drift > 15%
- **Agent memory** with Mem0 (semantic deduplication) + Graphiti (temporal knowledge graphs)
- **browser-use** for visual web automation, **Firecrawl** for structured data extraction
- **Daytona sandbox** for safe agent code execution (isolated kernel, network egress restricted)
- **RAGFlow DeepDoc** for enterprise document parsing with layout awareness
- **Ollama** local LLM deployment for privacy-preserving development
- **Claude Code** agentic coding acceleration with CLAUDE.md context injection
- **OpenClaw** local agent gateway with AGENTS.md/SOUL.md workspace management
- **Headroom** token compression (60-95% reduction before LLM processing)
- **Guardrails** + **NeMo Guardrails** + **AgentShield** for security
- **Redis LangCache** semantic caching + agent session state storage
- **pgvectorscale DiskANN** for SSD-optimized billion-scale vector search
- **tsvector + pgvector + RRF** hybrid search
- **Cost tracking** middleware — exact USD cost per session
- **OpenTelemetry** traces for agent chain-of-thought
- **README** with: architecture diagram, design tradeoffs (DiskANN vs HNSW, OAuth 2.1 vs API keys, PostgresSaver vs InMemorySaver), Ragas metrics table, docker-compose instructions

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
