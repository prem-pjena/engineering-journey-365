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
[16 existing interview answers remain above — see file for full content]

## INTERVIEW QUESTION BANK: CORE TECHNICAL DOMAINS

### Category 1: LLM Theory
**Q1.1: Explain Multi-Head Latent Attention (MLA) and how it resolves the memory bandwidth bottleneck of standard MHA.**
A: Standard MHA caches K/V vectors for every token across all heads — cache scales as 2 × n_h × d_h per token. MLA compresses input hidden state into a single low-dimensional latent vector via joint compression. During inference, only compressed latent vectors are cached, drastically reducing memory overhead while maintaining mathematical equivalence to full attention quality. (Phase 3 Day 28 | Hard | High Frequency)

**Q1.2: Describe auxiliary-loss-free load balancing in MoE.**
A: Traditional MoE uses auxiliary loss to prevent all tokens routing to one expert, degrading primary training objective. Auxiliary-loss-free strategy dynamically adjusts a bias term per expert based on real-time load, ensuring balanced utilization without performance trade-offs. (Phase 3 Day 29 | Hard | Medium Frequency)

**Q1.3: What is Multi-Token Prediction (MTP) and how does it impact inference?**
A: MTP uses a shared trunk with dedicated output heads to predict multiple future tokens simultaneously during training. This provides denser training signal for better representation planning and naturally facilitates speculative decoding during inference — significant acceleration without separate draft model. (Phase 3 Day 30 | Medium | High Frequency)

### Category 2: RAG Architecture
**Q2.1: Design an advanced chunking and two-stage retrieval pipeline.**
A: Fixed-size chunking breaks semantic boundaries. Use semantic chunking — split based on embedding distance shifts. Two-stage retrieval: Stage 1 = fast dense retrieval (HNSW index) to fetch top-100 broad candidates. Stage 2 = cross-encoder reranking to re-score top-10 by modeling deep query-document interaction, resolving out-of-vocabulary and semantic mismatch. (Phase 6 Day 47 | Medium | High Frequency)

**Q2.2: How do you evaluate a RAG system in production to prevent hallucination?**
A: Adopt the RAG Triad: Groundedness (Faithfulness) — is answer strictly derived from retrieved context? Context Relevance — does retrieved context actually contain the answer? Answer Relevance — does final response address the user's prompt? Calculated via LLM-as-a-judge with NDCG and MRR for retrieval ranking. (Phase 3 Day 31 | Hard | High Frequency)

### Category 3: LangGraph / Agent Frameworks
**Q3.1: Explain architectural difference between a sequential chain and a StateGraph. When is StateGraph strictly required?**
A: Sequential chain executes operations linearly — brittle for dynamic edge cases. StateGraph models execution as cyclic state machine: nodes modify a strictly typed shared state object, conditional edges route based on state values. Required for: loops (tool retry), conditional branching, multi-agent orchestration, and pause-resume (HITL) mechanics. (Phase 6 Day 47 | Easy | High Frequency)

**Q3.2: Implement a Human-in-the-Loop approval gate for a high-risk tool call.**
A: Use interrupt() pattern paired with persistent checkpointer (PostgresSaver). Before executing the high-risk tool, call interrupt() — halts execution, serializes state snapshot to DB, yields control to client. Human reviews state, applies corrections via state update, issues Command(resume=...) to resume from exact interruption point. (Phase 6 Day 48 | Medium | High Frequency)

### Category 4: MCP Protocol
**Q4.1: How does MCP resolve the N×M integration problem?**
A: Connecting N AI models to M tools historically required N×M custom implementations. MCP collapses this into hub-and-spoke over JSON-RPC 2.0: build one MCP Server exposing tools/resources/prompts; any MCP-compliant client dynamically discovers and invokes them without bespoke integration logic. (Phase 6 Day 49 | Medium | High Frequency)

**Q4.2: Explain MCP sampling capability and its security implications.**
A: Sampling reverses the flow — MCP Server can request LLM completions from Client. Enables server to execute autonomous agentic loops without its own LLM API keys. Security: Client retains full authority over authorization, user-approval gates, rate limiting, and final model selection (guided by server's costPriority/speedPriority hints). (Phase 6 Day 49 | Hard | Medium Frequency)

### Category 5: Vector Databases
**Q5.1: Compare HNSW, IVF, and DiskANN trade-offs for semantic search.**
A: HNSW — multi-layer proximity graph, lowest latency + highest recall, but massive RAM (entire graph in-memory), expensive at scale. IVF — k-means cluster partitioning, searches only nearest centroids (nprobe parameter), memory efficient but needs index training, slight recall loss. DiskANN — on-disk graph, minimal RAM metadata, fetches vectors from SSDs, only viable solution for billion-scale cost-efficient deployments. (Phase 6 Day 50 | Hard | High Frequency)

**Q5.2: Explain Product Quantization (PQ) and its role in vector storage.**
A: PQ compresses dense vector embeddings by splitting high-dim vectors into sub-vectors, clustering each subspace, and replacing sub-vectors with nearest centroid IDs from a learned codebook. Asymmetric distance computation enables efficient ANN search while compressing memory 10-50x. (Phase 6 Day 50 | Medium | Medium Frequency)

### Category 6: System Design
**Q6.1: Architect a high-throughput multi-tenant LLM inference gateway with billing enforcement.**
A: Core = async reverse proxy (FastAPI). Authenticates tenant via JWT, verifies prepaid wallet balance in PostgreSQL. Before routing to upstream LLM, queries Redis semantic cache to intercept redundant queries (sub-100ms). On cache miss, forward request. On response, async message queue (Celery/Kafka) processes token usage and debits ledger — billing logic does not block critical inference path. (Phase 6 Day 51 | Hard | High Frequency)

### Category 7: Production Patterns
**Q7.1: How to implement AI observability and guardrails in production?**
A: Tracing via OpenTelemetry/Langfuse — log every execution trace (prompt, token usage, latency, intermediate tool calls). Guardrails as distinct pipeline phase: Input guardrails (Presidio for PII, small classifiers for prompt injection). Output guardrails (Pydantic JSON validation, safety heuristics before returning to client). (Phase 6 Day 49 | Medium | High Frequency)

### Category 8: Classical ML
**Q8.1: Why is accuracy invalid for fraud detection? How should evaluation be structured?**
A: Extreme class imbalance (legitimate:fraud = 10,000:1). Model predicting "not fraud" always achieves 99.99% accuracy while failing entirely. Use Precision, Recall, PR-AUC. Calibrate decision threshold based on asymmetric business costs: financial damage of FN vs customer friction of FP. (Phase 3 Day 25 | Easy | High Frequency)

### Category 9: Python / FastAPI
**Q9.1: Implement a token-streaming endpoint with FastAPI. Why is synchronous execution fatal?**
A: Synchronous blocks worker thread for entire 2-10s generation window — thread pool exhaustion + timeout errors. Use async/await: async generator function iterates over upstream LLM stream chunks, yields instantly. Pass to StreamingResponse for SSE, allowing frontend to render tokens in real-time without blocking. (Phase 6 Day 52 | Medium | High Frequency)

### Category 10: Behavioral
**Q10.1: Describe a scenario where you sacrificed ideal architecture for a business constraint.**
A: [Template] "In a recent deployment, we designed an optimized linear processing pipeline. Compliance mandated human sign-off before downstream propagation. Rather than building an external state machine, I pivoted to LangGraph — slight latency overhead and stateful model required, but native interrupt() pattern enabled deterministic HITL approvals, passing the compliance audit while shipping on schedule." (Phase 6 Day 52 | Easy | High Frequency)

## AI System Design Interview Strategy

### Core Divergences: FAANG vs AI Startups
- **Latency Paradigm**: Traditional microservices <50ms. LLM inference = 2-10s. Reject synchronous blocking — use async task queues (Celery/RabbitMQ) or SSE.
- **Statefulness**: REST APIs are stateless. Agentic AI is inherently stateful — incorporate PostgreSQL JSONB for thread persistence, Vector DBs for semantic recall.
- **Cost Factor**: LLM generation has direct per-token costs. Incomplete without billing layers, Token Bucket rate limiters, and Redis semantic caching.

### Optimal Answer Structure (5-Step Flow)
1. **Requirements Extraction**: QPS, max tokens, latency budgets, cost ceilings. Clarify business objective (engagement vs accuracy).
2. **Data & Memory Schema**: Define schema for conversation threads, vector embeddings, tool-call receipts.
3. **High-Level Architecture**: Client → API Gateway (Auth/Rate Limiting) → Orchestrator (LangGraph) → [Cache / Vector DB / LLM Provider / MCP Servers]
4. **Deep Dive — The Bottleneck**: Zero in on most complex component (semantic chunking, embedding latency, KV cache optimization).
5. **Trade-offs Analysis**: Open-source local model vs proprietary API (latency, privacy, hosting overhead).

### Architectural Template: RAG at Scale
- **Ingestion Pipeline**: Async workers parsing raw docs, OCR extraction, semantic chunking. Batch embedding generation to circumvent rate limits.
- **Storage Layer**: Hybrid vector DB (Qdrant/Weaviate). HNSW for rapid recall vs DiskANN for cost efficiency at billion-scale. Discuss pre-filtering (precise, potentially slow) vs post-filtering (fast, risks <K results).
- **Retrieval & Generation**: Two-stage: dense + sparse (BM25), fused via RRF. Stage 2: lightweight cross-encoder reranking before final context injection.

## Target Company Dossiers

| Company | Location | Domain | Technical Focus |
|---------|----------|--------|-----------------|
| Aight | Gurgaon | AI Spend Gateway | FastAPI, Async Python, LLM APIs, SQL — prepaid wallet metering system |
| Peakflo | Remote | Fintech AI | Deep DB triage (Postgres/MongoDB), AI coding agent transcript |
| SuperKalam | Bengaluru | AI EdTech | JS, OOP, NextJS, React Native, full-stack, 2-4 day take-home |
| Gravity AI | Noida | Healthcare AI | React, JavaScript, Python, FHIR healthcare data, SLM/LLM/RAG pipelines |
| Smart Audit | Bengaluru | Audit Workflow | MERN, PyTorch, LoRA, vLLM, Qdrant/Milvus, OCR, ISO 27001 |
| Great Question | Remote | UX Research | Rails, React, pair programming, TDD, 90-min live coding |
| Fluexy | Bangalore | AI Decision Intelligence | Product execution, multi-agent simulations, portfolio > LeetCode |

### Specific Interview Pipeline Intelligence
- **Aight**: No classic DSA. Build a prepaid wallet metering system — real-time token accounting, billing correctness, hard balance cutoffs.
- **Peakflo**: Level-2 DB investigations (anomaly detection, lock contention, slow query logs). Submit AI coding agent transcript (Claude Code/Cursor) showing prompt engineering, iterative debugging, architectural planning.
- **SuperKalam**: 2-4 day take-home (NextJS, Node.js, Postgres, Redis). Prioritize execution speed + pixel-perfect UI. Submit Loom walkthrough.
- **Gravity AI**: React/ES6+ heavy + AI integration. Prepare SLM vs LLM vs RAG architecture discussions + FHIR data standards.
- **Smart Audit**: Full-stack MERN + PEFT/LoRA + vLLM/Triton + vector DB scalability + custom OCR. ISO 27001 compliance knowledge.
- **Great Question**: 90-min pair programming. Master "thinking out loud" protocol, TDD, clean Rails/React code.

## Negotiation Strategy

### Market Calibration
- India: ₹10-15 LPA base for 1-3 yr experience Agentic AI Engineer
- Global Remote: $24k-$40k/yr USD

### Evaluating Startup Viability
- Seed-stage must have 18-24 months runway. Ask: "What is current financial runway and what milestones unlock Series A?"

### Equity vs Cash
- ESOPs are highly illiquid. Negotiate base salary covering all expenses. View equity as asymmetric upside, not wage substitute. Standard vest: 4-year with 1-year cliff.

### Establishing Leverage
- Generate bespoke architecture diagram or mini POC specific to company domain during final interview stages.
- Signal strength: ask deep questions about burn rates, technical debt, product roadmaps. Demonstrate willingness to walk away from red flags.

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
