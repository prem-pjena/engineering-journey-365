# VS Code Agent Context — Engineering Journey 365
# Last updated: 2026-07-19 (Final validation research — plan score 82/100, minor adjustments applied)

## Status
- **Plan:** 60-day sprint (Market-Validated v2) — Day 11 COMPLETED, Day 12 next
- **Target Intern:** ₹30k-₹50k/mo by ~Day 31 (mid-Aug)
- **Target FT:** ₹10-12 LPA India OR $24k-$40k/yr global remote by Day 60 (mid-Sep)
- **Role:** Agentic AI Engineer | AI Engineer | SDE AI
- **Positioning:** Agentic AI Engineer — orchestration specialist with full-stack delivery capability
- **Primary platforms:** Wellfound (40%), YC Work at a Startup (30%), LinkedIn DMs (15%), X/Twitter DMs (10%), Naukri (5%)
- **SKIP:** Apna.co, TCS/Infosys/Wipro, training CNNs/RNNs, fine-tuning (8.5% JD mention vs RAG 35.9%)

## Role Confirmation (Research-Validated Jul 19)
- I am an **AI Engineer** — NOT a Data Scientist, NOT an ML Engineer
- I consume pre-trained models via APIs, build RAG pipelines, orchestrate agents with LangGraph
- I do NOT train models from scratch, implement gradient descent, or build custom ML pipelines
- RAG appears in 35.9% of JDs vs Fine-tuning in only 8.5% — focus on orchestration is correct
- Fine-tuning: Read 1 article / Concept level only. ROI of LangGraph/LangSmith >>> LoRA
- Transformer architecture: Concept level needed for KV cache and context window understanding
- Sampling params (temp, top-k, top-p): EXPERT level — used on every single API call
- Inference hardware (VRAM, KV cache, quantization): EXPERT level — cost optimization is key skill

## Skills (Day 11 completed — as of Jul 18)
- Python: 9.2/10 | DSA: 5.5/10 | Problem Solving: 7.8/10
- OOP: 4.5/10 | File I/O: 9.9 | Sets: 9.9 | Exception Handling: 9.6
- CRITICAL GAPS: Async, FastAPI (0), LangChain (0), LangGraph (0), RAG (0), MCP (0), LangSmith/Ragas (0), Next.js (0)

## Current Progress
- Days completed: 11 / 60
- DSA solved: 1 / target 50
- Projects deployed: 0

## Market Research Key Findings (Jul 17-19)
- ₹30-50k internships CONFIRMED: Hungama (₹50k), Aight (₹25-50k), SuperKalam (₹25-40k), Peakflo (₹40-50k)
- ₹10-12 LPA FT CONFIRMED: Market median ₹9-11 LPA for AI freshers. PPO example: Hungama ₹12-15 LPA
- Global remote CONFIRMED: Smart Audit ($25-50k/yr), Lamatic, Great Question, Peakflo
- FastAPI is DOMINANT — Django/Flask obsolete for AI roles
- LangGraph MANDATORY — basic LangChain chains considered obsolete for production
- MCP explicitly demanded — Great Question requires "MCP tool structuring"
- Programmatic eval (LangSmith/Ragas) is #1 missing skill for freshers
- See: agent/reports/market_research_deep_2026.md

## AWS Services for AI/ML (New — from Jul 19 research)
- **Bedrock** — serverless API for foundation models (Claude, Titan). Enterprise compliance. No infra management.
- **ECS Fargate** — standard for hosting FastAPI agent backends (NOT Lambda — agent timeouts > 15min)
- **Aurora pgvector** — vectors + relational data co-located. ACID compliance. Row-level security for multi-tenant.
- **ElastiCache (Redis)** — semantic caching: embed queries, cosine similarity check, serve cached response in ms
- **S3** — raw document storage for RAG ingestion pipeline
- **CloudWatch** — centralized logging, latency tracking, cost monitoring
- **API Gateway** — SSL termination, rate limiting to protect token budget
- **Step Functions** — cloud workflow orchestrator (trigger chunking → embedding → DB write)
- **OpenSearch** — alternative for hybrid search at massive scale (10M+ vectors)
- Interview strategy: Speak in trade-offs ("I chose pgvector over OpenSearch to reduce operational complexity")

## 7-Phase Curriculum (Market-Validated v2)

| Phase | Days | Focus | Milestone |
|-------|------|-------|-----------|
| 1-2 | 11-24 | Core DSA + Python + FastAPI + Algorithmic Prompting (DSPy/GEPA) + LangChain + Advanced RAG | CLI chat + FastAPI endpoint + compiled prompts + hybrid search |
| 3 | 25-31 | Classical ML + NLP Theory + Transformer Internals (DeepSeek-V3 MLA/MoE) + RAG Eval | Math foundations + transformer block + eval pipeline + Project 1 |
| 4 | 32-39 | Advanced DSA + Enterprise RAG (RAGFlow DeepDoc) + Agentic Memory (Mem0/Graphiti) | Multi-Tenant Knowledge Agent deployed |
| 5 | 40-46 | Database Architecture (DiskANN, tsvector, CTEs, Redis) + Security (Agno, AgentShield, NeMo) + Ollama | Vector indexing expertise + secure local LLM |
| 6 | 47-53 | AI Infrastructure & MLOps (Streaming Architectures, Feature Stores, Observability, Inference Optimization, Multi-Tenant Caching, CI/CD for AI) | Production MLOps pipeline + streaming agents |
| 7 | 54-60 | Agentic Orchestration (LangGraph/CrewAI/AutoGen) + A2A vs MCP Protocols + Claude Code + OpenClaw + Headroom + **Project 2** | Autonomous Code & Web Intelligence Swarm |
| 8 | Post-60 | Scalable Agentic System Design (Distributed Systems, Rate Limiting, Protocol Architecture, Multi-Tenant Design, Disaster Recovery, System Design Mocks) | Interview-ready system design depth |

## ALL Concepts (Market-Validated v3 — 2026 Update)
### 🔴 Must-Know
- **Python:** OOP, Context Managers, Async (asyncio, gather), Generators, Tuples, enumerate, zip, String methods, JSON, Type hints, Modules
- **Backend:** FastAPI, Pydantic v2 strict validation, Asynchronous Python, Constrained Decoding (Outlines/XGrammar)
- **LLM:** LangChain (templates, loaders, splitters, structured output), **Algorithmic Prompt Optimization (DSPy + GEPA)**, LLM APIs (OpenAI, Gemini)
- **Sampling params:** Temperature (0-2), top-k, top-p, max_tokens, frequency penalty — used on EVERY API call
- **Agents:** LangGraph (StateGraph, nodes, edges, reducers, routing, **PostgresSaver** checkpointing, HITL, multi-agent, parallel **Send API**, hash-based idempotent recompute). **OpenAI Agents SDK** for lightweight handoffs
- **RAG:** Corrective (CRAG) → Adaptive → Agentic RAG. **Proposition Generation**, **Step-back Prompting**, **Semantic Chunking**, **Parent-Child Chunking**, **Cross-encoder Reranking**, **GraphRAG**. Naive RAG deprioritized
- **Agent Memory:** **Mem0** (semantic fact extraction, automated dedup, contradiction resolution), **Graphiti** (temporal knowledge graphs), **Procedural Memory** (parameterized workflow templates), **Blackboard System** (namespaces, optimistic locking, private scratchpads)
- **Web Automation:** **browser-use** (Playwright, visual DOM, multi-tab navigation), **Firecrawl** (LLM-ready markdown, anti-bot bypass)
- **Sandboxed Execution:** **Daytona SDK** — NEVER run agent code natively. Use isolated ephemeral sandboxes
- **Search:** Hybrid Search (BM25 + Dense + **tsvector** + **RRF**), pgvector, **pgvectorscale (DiskANN)**, ChromaDB (prototype-only), HNSW vs IVFFlat vs DiskANN
- **Evaluation:** LangSmith, Langfuse/OpenLLMetry, Ragas (Faithfulness, Context Precision, Answer Relevancy), **LLM-as-a-judge** regression testing, **AIBOM** supply chain tracking
- **MCP:** Model Context Protocol (Host/Client/Server, stdio vs HTTP SSE, Tools/Resources/Prompts, JSON-RPC 2.0). **OAuth 2.1 mandatory** (token exchange, no passthrough, per-client consent). **Advanced MCP**: streaming tools, resource subscriptions, **Sampling**, **Roots**. Study: modelcontextprotocol/servers, punkpeye/awesome-mcp-servers
- **Agent Security:** **Dual Schema Enforcement** (Agno — read-only scopes for data agents), **JWT-based RBAC**, **AgentShield** (config vuln scanning), **NeMo Guardrails** (Colang for topical bounding, jailbreak detection)
- **Local LLM:** **Ollama** — run LLMs locally for development, privacy compliance (critical for Indian enterprise/fintech)
- **Agentic Coding:** **Claude Code** — agentic coding with CLAUDE.md context injection, three-phase loop (gather → act → verify)
- **Local Gateway:** **OpenClaw** — multi-channel agent gateway, AGENTS.md/SOUL.md workspace management
- **Token Optimization:** **Headroom** — ContentRouter/SmartCrusher, 60-95% token reduction before LLM processing
- **Agent Frameworks (complementary):** **LangGraph** (stateful production) + **CrewAI** (rapid role-based prototyping) + **OpenAI Agents SDK** (lightweight handoffs)
- **Tool Planning:** **DFSDT** (Depth-First Search Decision Tree) — explores multiple tool paths and backtracks on failure. From OpenBMB/ToolBench
- **LLM Safety:** **Guardrails** (guardrails-ai/guardrails) — input/output validators for PII, toxic language, schema compliance
- **Deployment:** Docker, AWS ECS Fargate, AWS Bedrock, GitHub Actions CI/CD
- **SQL:** PostgreSQL, pgvector, **pgvectorscale DiskANN**, **Recursive CTEs**, **tsvector full-text search + RRF**, vector similarity search, HNSW vs IVFFlat vs DiskANN index tuning, **read-only transaction scopes**
- **DSA:** **Pareto 50+** — Arrays & Hashing, Two Pointers, Sliding Window, Stack & Queue, Binary Search, Linked Lists, Trees (BFS/DFS), Graphs (BFS/DFS/Topo Sort/Cycle Detection), Intervals, Backtracking, Heaps, Design (LRU Cache, Trie, Time-Based KV), **DP (Coin Change, LIS, Climbing Stairs)**, **Monotonic Stack (Largest Rectangle, Trapping Rain Water)**, **BFS Shortest Path (Word Ladder)**. **Probabilistic Data Structures**: Bloom filters, HyperLogLog

### 🟡 Good-to-Have
- **Full-Stack:** Next.js + TypeScript (chat UI components, streaming responses)
- **Data:** Pandas, NumPy, Scikit-learn basics
- **Inference:** vLLM engine (PagedAttention, continuous batching), KV cache management, VRAM capacity planning
- **Cost Optimization:** Quantization (INT8/INT4 — AWQ, GPTQ), Redis Semantic Caching
- **Interview Theory:** Transformer (QKV, self-attention, RoPE), BERT vs GPT, BPE/WordPiece/Unigram/SentencePiece, bias-variance, precision/recall/F1, **MCP OWASP Top 10**, **Procedural vs Episodic vs Semantic Memory**, **DeepSeek-V3 (MLA, MoE) internals**, **Classical ML (Logistic Regression, Random Forest, XGBoost, K-Means, PCA)**
- **AWS:** Bedrock API, ECS Fargate, CloudWatch logging
- **Visual Workflow Builders:** **n8n**, **Langflow**, **Dify** — rapid prototyping only; not for production
- **Self-Hosted Chat UI:** **Open WebUI** — offline testing

### 🚫 Skipped / Downgraded (Research-Validated)
- Training CNNs/RNNs from scratch, Django/Flask, deep ML math (gradient descent), Apna.co
- Fine-tuning (LoRA/PEFT): Read 1 article only. Only 8.5% of JDs mention it.
- Classical ML pipelines: AI Engineers build LLM pipelines, not training pipelines
- **Naive RAG:** Deprioritized — use Proposition Generation, Step-back, GraphRAG
- **InMemorySaver:** Restricted to testing only. Use PostgresSaver for production
- **Static API keys for MCP:** Deprecated. OAuth 2.1 token exchange is mandatory
- **ChromaDB for production:** Downgraded to prototype-only. Use pgvector/DiskANN for scale

## 2 Key Projects
### Project 1 (Days 31-38): Multi-Tenant Enterprise Knowledge Agent
- FastAPI + pgvector (RLS) + LangGraph + MCP + Mem0 + Graphiti + Cross-encoder reranking + Hybrid Search (BM25 + tsvector + RRF) + Docker + AWS ECS + Ragas eval + LLM-as-a-judge
- **Agno dual-schema:** read-only transaction scopes for data agents, isolated schema for engineer agents
- **JWT-based RBAC** for multi-tenant isolation
- **RAGFlow DeepDoc** for layout-aware enterprise document parsing
- Apply signal: "Hire me" — architectural maturity with security awareness

### Project 2 (Days 54-57): Autonomous Code & Web Intelligence Swarm
- FastAPI + LangGraph (Blackboard pattern with optimistic locking) + browser-use + Firecrawl + Daytona + MCP (OAuth 2.1, Sampling, Roots) + Next.js UI + Docker + AWS ECS + GitHub Actions CI/CD
- **Researcher Agent:** browser-use + Playwright for visual DOM, multi-tab SPA navigation
- **Coder Agent:** Python workflows inside isolated Daytona sandboxes
- **MCP servers secured via OAuth 2.1** token exchange, per-client consent registries
- **Advanced MCP:** Sampling for server-initiated LLM calls, Roots for directory boundaries
- **Ollama** local LLM for privacy-preserving dev
- **Claude Code** agentic coding acceleration
- **OpenClaw** local agent gateway
- **Headroom** token compression (60-95% reduction)
- **LLM-as-a-judge** regression testing catches infinite loops, context drift
- Apply signal: "Full-stack AI Engineer" — enterprise security + sandboxed execution

## Key Interview Answers (From Deep Research)
1. "Why RAG over Fine-tuning?": RAG solves knowledge, fine-tuning solves behavior. Start with RAG + prompting.
2. "Transformer architecture?": Self-attention is O(n²). Place critical instructions at end of prompt for highest attention weight.
3. "How to ensure JSON output?": Constrained decoding with Outlines/XGrammar — logit masks guarantee schema compliance.
4. "How to optimize costs?": Compound AI systems — cheap SLM router + expensive frontier model only for complex tasks.
5. "AWS for AI?": Bedrock for serverless, ECS Fargate for persistent backends, Aurora pgvector for RAG.
6. "MCP Security?": OAuth 2.1 token exchange mandatory. Token passthrough is forbidden (Confused Deputy). Per-client consent registries prevent rogue MCP servers.
7. "Memory architectures?": Three types — Episodic (conversation history), Semantic (Mem0 — deduplicated facts), Procedural (parameterized workflow templates from traces). Blackboard for multi-agent shared state with optimistic locking.
8. "How to scale LangGraph?": PostgresSaver for durable checkpoints, Send API for parallel fan-out, hash-based idempotent recompute to skip repeated work.
9. "Agent safety?": AgentShield for config vuln scanning, NeMo Guardrails for jailbreak detection, dual-schema DB enforcement for data integrity.
10. "Execution sandboxing?": Daytona SDK — isolated ephemeral sandboxes with dedicated kernel, network isolation. NEVER run agent code natively.
11. "HNSW vs DiskANN?": HNSW is RAM-only — memory cost explodes at scale (~5x vector size). DiskANN (pgvectorscale) uses SSD-optimized Vamana graphs, supports billion-scale with metadata pre-filtering without recall cliff. Choose DiskANN for >10M vectors.
12. "Hybrid Search for RAG?": Pure semantic search misses exact keyword matches (acronyms, serial numbers). Fuse pgvector cosine similarity with PostgreSQL tsvector full-text search via Reciprocal Rank Fusion (RRF) for high recall.
13. "DeepSeek-V3 architecture?": Multi-Head Latent Attention (MLA) compresses KV pairs into shared latent space (d_c=512) — reduces KV cache memory by ~10x. MoE with auxiliary-loss-free load balancing — only ~37B active params per token out of 671B total. Multi-Token Prediction improves training efficiency.
14. "LangGraph vs CrewAI?": Complementary, not competing. LangGraph for deterministic stateful production (96% error recovery). CrewAI for rapid role-based prototyping (content generation, research). Use LangGraph in prod, CrewAI for experiments.
15. "Local LLM deployment?": Ollama for dev and privacy compliance. Critical for Indian fintech where data cannot leave premises. Supports OpenAI-compatible API, making it drop-in replaceable.
16. "How to reduce LLM token costs?": Headroom ContentRouter compresses JSON/AST/prose by 60-95% before LLM processing. Combined with Redis LangCache semantic caching (cosine > 0.85 skip LLM call).

## Architecture Decision Records — Vector Database Selection

### Database Selection by Corpus Scale
| Vector Count | Recommended Infrastructure | Justification |
|-------------|---------------------------|---------------|
| <10K | pgvector (Flat L2/IP) | Sub-ms exhaustive search, no graph overhead, ACID compliance |
| <1M | pgvector (HNSW) | Fits in standard DB RAM. ef_search/m tunable for 99% recall |
| <100M | Qdrant/Milvus (IVF-PQ) | Graph indices too large for RAM. PQ reduces footprint |
| <1B | pgvectorscale/LanceDB | DiskANN/SPANN on NVMe SSDs. LanceDB S3-backed for cost efficiency |
| >1B | Milvus/Vespa | Distributed computing, tensor frameworks, massive parallelization |

### Algorithm Trade-offs
| Algorithm | Strengths | Weaknesses | Best For |
|-----------|-----------|------------|----------|
| HNSW | 95%+ recall, absorbs inserts dynamically | 2-5x raw vector size RAM | Dynamic data <50M records |
| IVFFlat | Fast build, ~1.1x memory overhead | Recall drifts, needs re-clustering | Large static datasets with offline rebuild windows |
| DiskANN | SSD-stored, 1B+ vectors per 64GB node | Needs NVMe, expensive incremental updates | Enterprise data exceeding RAM |
| PQ (Product Quantization) | Extreme compression via sub-vector centroids | Lossy, needs exact reranking stage | Edge devices, memory-constrained |

## Performance Tuning Guide
### HNSW (pgvector/FAISS/Milvus)
- **m (degree)**: 16 standard, up to 48 for high dimensionality
- **ef_construction**: 100-200 — higher = better recall, slower build
- **ef_search**: 10-100 — higher = better recall, slower query

### DiskANN (pgvectorscale)
- **storage_layout**: memory_optimized for SBQ compression
- **num_neighbors**: 50 (typical Vamana graph degree)
- **search_list_size**: 100 high-throughput, 200 RAG
- **max_alpha**: 1.2 (graph pruning threshold)

### IVFFlat
- **lists (centroids)**: sqrt(rows) for <1M, rows/1000 for >1M
- **probes**: 10-100. probes=1 = unacceptable recall, >500 = negates index benefit

### Embedding Quantization
- **Scalar Int8**: 64% storage reduction, <1.5% recall loss
- **Binary (1-bit)**: Up to 17% recall cliff in standard models. OK for MRL models (ModernBERT)

## Advanced Vector & Memory Systems Q&A
Q: How would you choose a vector database for 250M dynamic documents?
A: In-memory HNSW requires ~1TB RAM. Evaluate SSD-oriented: pgvectorscale DiskANN with SBQ compression (if relational integrity needed) or LanceDB S3-backed columnar (if compute separation critical).

Q: How does HNSW work and its physical limitations?
A: Skip-list-like graph — sparse upper layers for long-range jumps, dense bottom for precise routing. 95%+ recall, dynamic inserts. But edges require 2-5x raw vector memory — uneconomical beyond 50-100M vectors.

Q: Design a multi-tenant vector storage system. Pitfalls of metadata filtering?
A: Single global index + post-filtering by tenant_id breaks ANN traversal. Greedy search routes through dense clusters — sparse tenants lose recall. Solutions: physical partitioning, iterative index scans (hnsw.max_scan_tuples), or label-embedded graph nodes.

Q: Hybrid search fusion beyond RRF?
A: RRF is unsupervised baseline. Convex Combination (weighted sum) normalizes BM25 + dense scores onto common scale — often outperforms RRF with enough labeled data to tune alpha/beta weights.

Q: How do temporal knowledge graphs differ from vector stores for agent memory?
A: Vector stores treat facts as independent stateless embeddings — superseded facts retrieved via semantic proximity cause hallucination. Temporal graphs (Graphiti, Neo4j Agent Memory) use bi-temporal edges (valid time vs ingestion time), episode-level provenance, and relational traversal instead of flat vector distances.
- agent/learnings/rag_architecture_14_types.md — all RAG types with 12 LPA interview answers
- agent/learnings/gold_mines_repo_analysis.md — deep analysis of 7 key repos

## New Study References (System Design & Interviews)
- **donnemartin/system-design-primer**: Rate limiting, load balancing, cache eviction — map to vLLM/Semantic Caching
- **a2aproject/A2A**: Agent-to-Agent protocol, Agent Cards, capability discovery, JSON-RPC 2.0
- **FareedKhan-dev/all-agentic-architectures**: 35 agent patterns (Reflexion, LATS, Meta-Controller)
- **alirezadir/Agentic-AI-Systems**: Multi-agent state management and reasoning loops
- **iusztinpaul/designing-real-world-ai-agents-workshop**: Deep Research Agent as MCP server via FastMCP + Opik
- **NirDiamant/agents-towards-production**: Docker deployment, PII sanitization, security guardrails
- **omBharatiya/ai-system-design-guide**: AI system design interview questions
- **labuladong/fucking-algorithm**: DSA problem-solving frameworks and pattern mastery
- **binhnguyennus/awesome-scalability**: Scalability patterns for high-throughput systems
- **KalyanKS-NLP/LLM-Interview-Questions**: LLM interview questions with answers
- **ombharatiya/AI-Engineer-Interview-Questions**: AI Engineer specific interview questions
- **chiphuyen/dmls-book**: Designing Machine Learning Systems — production ML patterns
- **HandsOnLLM/Hands-On-Large-Language-Models**: Practical LLM exercises for interviews
- **mli/paper-reading**: Key papers: Attention Is All You Need, DeepSeek-V3
