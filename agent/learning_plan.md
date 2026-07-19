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
| 🔴 Must-Know | Agent Frameworks | **LangGraph** (StateGraph, nodes, edges, reducers, routing, checkpointing via **PostgresSaver**, HITL, multi-agent, parallel **Send API**, hash-based idempotent recompute) — industry standard for production agents. **OpenAI Agents SDK** for lightweight handoffs/voice |
| 🔴 Must-Know | RAG & Search | Corrective → Adaptive → Agentic RAG, **Proposition Generation**, **Step-back Prompting**, **Semantic Chunking**, **Parent-Child Chunking**, **Cross-encoder Reranking**, **Hybrid Search (BM25 + Dense)**, **GraphRAG**, pgvector, ChromaDB — **Naive RAG deprioritized** |
| 🔴 Must-Know | Agent Memory | **Mem0** (semantic fact extraction, automated deduplication, contradiction resolution), **Graphiti** (temporal knowledge graphs), **Procedural Memory** (parameterized workflow templates from execution traces), **Blackboard System** (multi-agent shared memory with optimistic locking) |
| 🔴 Must-Know | Agentic Web Interaction | **browser-use** (Playwright-based visual DOM understanding, tab/multi-tab navigation), **Firecrawl** (LLM-ready markdown extraction, anti-bot bypass, batch crawling) |
| 🔴 Must-Know | Sandboxed Execution | **Daytona SDK** (isolated, ephemeral sandboxes with dedicated kernel, network isolation, vCPU/RAM allocation for AI-generated code) |
| 🔴 Must-Know | Evaluation & Observability | **LangSmith**, **Langfuse/OpenLLMetry** (observability + tracing), **Ragas** (Faithfulness, Context Precision/Recall, Answer Relevancy), **LLM-as-a-judge** regression testing, **AIBOM** (AI Bill of Materials for supply chain security) |
| 🔴 Must-Know | Constrained Decoding | **XGrammar / Outlines** — finite-state machine token masking for guaranteed JSON output. Prevents agent crashes from malformed tool calls |
| 🔴 Must-Know | Inference Optimization | **vLLM** (PagedAttention, continuous batching, Tensor Parallelism), KV cache management, Quantization (INT8/INT4) — essential for open-source model serving |
| 🔴 Must-Know | Semantic Caching | **Redis** with vector embedding + cosine similarity threshold tuning (0.85-0.95) + hybrid metadata filtering for tenant isolation |
| 🔴 Must-Know | Agent Security | **Dual Schema Enforcement** (Agno pattern — read-only transaction scopes for data agents), **JWT-based RBAC**, **AgentShield** (config scanning, adversarial red-teaming), **NeMo Guardrails** (topical bounding, jailbreak detection), **OAuth 2.1** for MCP (token exchange, no token passthrough, per-client consent registries) |
| 🔴 Must-Know | SQL & Vectors | PostgreSQL, pgvector, HNSW vs IVFFlat indexing, vector similarity search, **read-only transaction scopes** |
| 🔴 Must-Know | DSA | **Pareto 50** — Arrays & Hashing, Two Pointers, Sliding Window, Stack & Queue, Binary Search, Linked Lists, Trees (BFS/DFS), Graphs (BFS/DFS/Topo Sort/Cycle Detection), Intervals, Backtracking, Heaps, Design (LRU Cache, Trie, Time-Based KV), DP Basics. **Explicitly skip**: Coin Change, LIS, Word Ladder, Trapping Rain Water, Largest Rectangle — zero ROI for Agentic AI startup interviews |
| 🟡 Good-to-Have | Full-Stack | **Next.js + TypeScript** (unlocks Full Stack AI Engineer roles — premium pay for end-to-end delivery) |
| 🟡 Good-to-Have | Data | Pandas, NumPy basics |
| 🟡 Good-to-Have | Interview Theory | Transformer architecture (Q, K, V, self-attention, RoPE), BERT vs GPT, tokenization high-level concept, LLM inference architecture (vLLM, KV cache), **MCP OWASP Top 10**, **Procedural vs Episodic vs Semantic Memory**, **Blackboard Architecture** |
| ⚪ Nice-to-Have | Fine-tuning | LoRA / PEFT — 8.5% JD mention vs RAG 35.9%. Read 1 article for concept only |
| 🚫 Skip | CNNs/RNNs/Classical ML | Zero JD mentions for GenAI Engineer roles. Skip bias-variance, cross-validation, gradient descent entirely |

---

## 📅 60-Day Complete Curriculum (Market-Validated)

### Phase 1: Python, APIs, and Algorithmic Prompting (Days 11-17)
*Goal: Complete Python foundation, FastAPI backend, algorithmic prompts via DSPy/GEPA*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 11 | OOP: classes, inheritance, dunder, @property, @staticmethod, @classmethod | Build mock VectorStore class | Two Sum | vector_store_oop.py |
| 12 | Context Managers (`__enter__`, `__exit__`), Modules, `__init__.py` | Safe File I/O Manager + Package refactor | Valid Anagram | context_logger.py |
| 13 | Async Python: asyncio, event loop, gather + **FastAPI intro** | Build first FastAPI endpoint (GET/POST) | Group Anagrams | fastapi_hello.py |
| 14 | Generators (yield), Tuples, enumerate, zip | Build streaming token generator | Top K Frequent | token_streamer.py |
| 15 | String methods, JSON module + **Constrained Decoding (XGrammar/Outlines)** | Parse nested JSON LLM outputs + FSM token masking | Product of Array | json_parser.py |
| 16 | LLM APIs: OpenAI/Gemini, temperature, tokens, streaming | Chat + streaming response | Valid Palindrome | basic_llm_api.py |
| 17 | **Algorithmic Prompt Optimization**: DSPy + GEPA (Genetic-Pareto Evolution). Compiling self-improving prompt signatures from execution traces | Replace manual prompt engineering with compiled, optimized prompts | 3Sum | dspy_optimizer.py |

### Phase 2: LangChain + Advanced RAG Foundation (Days 18-24)
*Goal: Master LangChain, Advanced Retrieval (Proposition Gen, Step-back, GraphRAG), SQL + pgvector*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 18 | FastAPI SSE Streaming + Pydantic + Constrained Decoding | Build streaming endpoint + FSM-guaranteed JSON | **Container With Most Water + Two Sum II** | fastapi_streaming.py |
| 19 | LangChain: Document Loaders, Text Splitters, **Semantic Chunking** | Parse PDF, split by semantic boundaries, compare chunk strategies | Longest Substring | semantic_chunker.py |
| 20 | Vector DBs, Embeddings, ChromaDB, HNSW vs IVFFlat | Store chunks + similarity search + index tuning | Valid Parentheses | chroma_ingestion.py |
| 21 | **Advanced Retrieval**: Proposition Generation + Step-back Prompting | Decompose documents into atomic propositions, generate broader queries | Binary Search | advanced_retrieval.py |
| 22 | **SQL + pgvector**: SELECT, INSERT, JOINs, vector columns, read-only scopes | Store embeddings with read-only transaction scopes for safety | Search 2D Matrix | pgvector_setup.sql |
| 23 | **Parent-Child Chunking + Cross-Encoder Reranking + GraphRAG** | Rerank top-20 to top-3 with BGE, introduce GraphRAG via Milvus | Reverse Linked List | reranked_rag.py |
| 24 | **Hybrid Search**: BM25 + Dense Vector, pgvector HNSW vs IVFFlat tuning | Implement hybrid search + benchmark index configs | Merge Two Sorted | hybrid_search.py |

### Phase 3: Adaptive RAG + Agentic Memory + Evaluation (Days 25-31)
*Goal: Master advanced RAG, cross-session memory, LLM-as-a-judge eval, build & deploy Project 1*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 25 | **Corrective RAG (CRAG)** + **Adaptive RAG** | Evaluator → web search fallback + router | Reorder List | corrective_adaptive_rag.py |
| 26 | **Conversational RAG + Agentic RAG**. Study Ref: NirDiamant/rag_techniques | Chat history injection + agent re-queries. Analyze Proposition Gen patterns | Max Depth Tree | conversational_rag.py |
| 27 | **Agentic RAG with Contextual AI**: instruction-following rerankers, grounded language models | Build agent that rewrites queries if results poor | **Validate BST** | agentic_rag.py |
| 28 | **Cross-Session Agent Memory**: Mem0 (semantic fact extraction, dedup, contradiction resolution) + Graphiti (temporal knowledge graphs). Study Ref: NirDiamant/Agent_Memory_Techniques Notebooks 24-27 | Integrate Mem0 into LangGraph state schema + build temporal KG | Invert Tree | agent_memory.py |
| 29 | **Evaluation**: LLM-as-a-judge regression testing, Ragas (Faithfulness, Context Precision), failure-mode reporting, AIBOM tracking | Build golden dataset + auto-eval pipeline that catches infinite loops, context drift | LCA of BST | comprehensive_eval.py |
| 30 | **PROJECT 1 BUILD**: Multi-Tenant Enterprise Knowledge Agent (Agno dual-schema, Graphiti KG, Mem0, CRAG, JWT RBAC) | FastAPI + pgvector RLS + LangGraph + Cross-encoder + Hybrid Search. Local test | Level Order Traversal | project1_start/ |
| 31 | **PROJECT 1 DONE**: Docker containerize + Deploy to AWS ECS + Ragas eval report + **APPLY blitz** | Wellfound + YC applications with Project 1 as proof | **Longest Consecutive Sequence** | project1_deployed/ |

### Phase 4: LangGraph + Web Automation + MCP (Days 32-39)
*Goal: Master stateful agents, agentic web interaction, MCP protocol, lightweight orchestration*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 32 | LangGraph: StateGraph, Nodes, Edges, State, Reducers, add_messages. Study Ref: ed-donner/agents Week 4 | Linear 3-node state machine + chatbot with memory | Course Schedule | basic_state_graph.py |
| 33 | LangGraph: Conditional Routing + **DFSDT Concept** + **PostgresSaver checkpointing** | Chatbot with intent router. Implement durable checkpointing (not InMemorySaver) | Climbing Stairs | stateful_chatbot.py |
| 34 | **Advanced LangGraph**: HITL, Parallel execution (**Send API**), hash-based idempotent recompute. Study Ref: OpenBMB/ToolBench | Approval interrupts + parallel fan-out to multiple analysts | **LRU Cache** | advanced_langgraph.py |
| 35 | MCP Core: Host/Client/Server, stdio/HTTP SSE, Tools/Resources/Prompts. **OAuth 2.1 for MCP** | Python MCP server with tools. Enforce token exchange (no passthrough) | **Task Scheduler** | mcp_core.py |
| 36 | **Agentic Web Interaction**: browser-use with Playwright (visual DOM, multi-tab nav) + Firecrawl (markdown extraction, anti-bot bypass). Study Ref: firecrawl/firecrawl-workflows | Build research agent that navigates SPAs + extracts structured data | **Min Stack** | web_agent.py |
| 37 | MCP Integrations: Explore real-world MCP servers on punkpeye/awesome-mcp-servers | Study OAuth 2.1 integrations, tool schema definitions | Merge Intervals | mcp_integrations.py |
| 38 | **Lightweight Orchestration**: OpenAI Agents SDK (agent handoffs, manager pattern, real-time voice streaming) | Build manager agent that delegates to specialized sub-agents | Insert Interval | openai_sdk_agent.py |
| 39 | **LangGraph + MCP + Web Agent Integration** | Agent discovers and calls MCP tools + browser-use for web research | **Course Schedule II** | full_integration.py |

### Phase 5: Production Security + Sandboxed Execution + Cloud Deploy (Days 40-46)
*Goal: Build secure, sandboxed AI apps, deploy with CI/CD, add UI layer*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 40 | **Agent Security & RBAC**: Agno-style Dual Schema Enforcement (read-only transactions for data agents) + JWT-based multi-tenant isolation | PostgreSQL with default_transaction_read_only=on for analyst agents | **Kth Largest in Stream** | agent_security.py |
| 41 | **Agentic Threat Modeling**: AgentShield config scanning (agents.json, .cursorrules) + **NeMo Guardrails** (Colang for topical bounding, jailbreak detection, output sanitization) | Scan agent configs for vulns, implement safety guardrails | **K Closest Points to Origin** | threat_model.py |
| 42 | **Sandboxed Code Execution**: Daytona SDK — isolated ephemeral sandboxes, dedicated kernel, network isolation, vCPU/RAM allocation | Build secure Python REPL tool that routes agent code to Daytona sandbox | **Best Time to Buy/Sell Stock** | daytona_sandbox.py |
| 43 | **vLLM Inference**: PagedAttention, continuous batching, TP, KV cache | Deploy model with vLLM, measure TTFT. Study Ref: EthicalML/awesome-production-agentic-systems | **Longest Repeating Char Replacement** | vllm_basics.py |
| 44 | **Redis Semantic Caching**: embeddings, cosine threshold (0.85-0.95), hybrid metadata filters + **Next.js UI** basics | Build semantic cache layer + chat UI with SSE streaming | **Linked List Cycle** | semantic_cache.py |
| 45 | **AWS ECS Fargate + Docker**: Deploy full stack to cloud | Fargate + RDS + Load Balancer + CloudWatch logging | 3Sum review | aws_deploy_logs/ |
| 46 | **GitHub Actions CI/CD**: Auto-test, auto-eval (LLM-as-a-judge), auto-deploy + Cost tracking per query | Push → test → deploy pipeline + token cost middleware | Min Window Substring | .github/workflows/ci.yml |

### Phase 6: System Design + Interview Mastery (Days 47-53)
*Goal: Ace AI System Design, MCP Security, Advanced Memory Theory, and ML/NLP interview rounds*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 47 | **System Design**: RAG at scale, semantic caching (Redis), query routing, hybrid metadata filtering + **LangGraph scaling** (PostgresSaver, Send API, hash-based idempotent recompute) | Architecture diagram for 1M QPD + parallel fan-out design | **Find Min Rotated + Search in Rotated Array** | rag_architecture.md |
| 48 | **System Design**: Multi-tenant isolation, LLM Gateway, vLLM inference architecture, PagedAttention, continuous batching | Gateway design + inference optimization trade-offs | **Subsets** — generate all combinations of prompt options or tool params | inference_architecture.md |
| 49 | **MCP Security Paradigms**: OAuth 2.1 token exchange, mTLS, OWASP MCP Top 10 (Confused Deputy, Tool Poisoning, Scope Creep, Context Injection), per-client consent registries | Design secure MCP proxy with token exchange + consent registry | Serialize/Deserialize Tree | mcp_security.md |
| 50 | **NLP Concepts**: Transformer (QKV, self-attention, RoPE), BERT vs GPT, tokenization (high-level), MoE, speculative decoding | tiktoken counter + attention visualization | **Permutations** — reorder tool execution sequences to evaluate optimal logic paths | nlp_concepts.md |
| 51 | **Advanced Memory Theory**: Procedural Memory (parameterized workflow templates from execution traces), Blackboard System (multi-agent shared memory with namespaces, optimistic locking, thread-safe locks) | Design memory architecture: namespaces, access control, version checking for concurrent writes | Word Search | memory_architecture.md |
| 52 | System Design Mock + Behavioral | Practice "termination narrative" + why AI + architecture trade-offs | **Combination Sum** | behavioral_prep.md |
| 53 | Live Coding Mock (FastAPI + LangGraph + MCP) | Build a mini agent under time pressure | **Clone Graph** | live_coding_mock/ |

### Phase 7: Capstone Project + Apply FT (Days 54-60)
*Goal: Build standout Autonomous Code & Web Intelligence Swarm, apply aggressively, secure offers*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 54 | **PROJECT 2 BUILD**: Autonomous Code & Web Intelligence Swarm — Blackboard shared-memory pattern with optimistic locking | Researcher agent (browser-use + Playwright for SPA nav, Firecrawl for extraction). Coder agent (Daytona sandbox for safe execution). Build Blackboard with namespaces | **Implement Trie (Prefix Tree)** | project2_start/ |
| 55 | Project 2 continued: MCP servers with OAuth 2.1 (token exchange, per-client consent) + LangGraph supervisor routing | Docker + GitHub Actions CI/CD + AWS ECS deploy | **Time Based Key-Value Store** | project2_continue/ |
| 56 | **PROJECT 2 DONE**: LLM-as-a-judge regression testing (catch infinite loops, context drift) + Deploy + README with architecture diagrams | Production-grade project with docs. Eval report showing safety + performance | **Number of Islands + Max Area of Island** | project2_deployed/ |
| 57 | **APPLY BLITZ**: Wellfound (20 apps) + YC (10) + LinkedIn DMs (10) | Personalized messages with project links | **Redundant Connection** | application_log.md |
| 58 | Follow-ups + Mock interviews | Respond to callbacks, practice behavioral, negotiate | **Evaluate Reverse Polish Notation** | interview_tracker.md |
| 59 | Buffer / Offer evaluation | Compare CTC vs cash vs equity | Rest | offer_evaluation.md |
| 60 | **CELEBRATE + PLAN NEXT** | ₹10-12 LPA offer in hand | — | done.md |

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

| Old Plan Item | Reason to Skip |
|--------------|----------------|
| Training CNNs/RNNs from scratch | Zero JD mentions. Pre-trained models via APIs is the standard |
| Deep ML math (backpropagation derivation) | Not tested in AI Engineer interviews |
| Django / Flask | FastAPI has near-total dominance in AI engineering |
| Pandas/NumPy as full week | Moved to 1-day Good-to-Have |
| Apna.co as primary platform | Low signal, legacy IT, fake AI listings |
| **Naive RAG (fixed-size chunking)** | Replaced by Proposition Generation, Step-back Prompting, Semantic Chunking, GraphRAG |
| **InMemorySaver for LangGraph** | Restricted to testing only. PostgresSaver mandatory for production HITL workflows |
| **Static API keys for MCP** | OWASP MCP Top 10 vulnerability. OAuth 2.1 token exchange is mandatory |
| **Manual prompt engineering as primary skill** | Replaced by DSPy + GEPA algorithmic prompt optimization |

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

### ₹80k FT Level (Day 56) — "Enterprise Orchestrator"
- **LangGraph** with dual-channel memory (persistent + ephemeral scratchpad), **PostgresSaver** for durable checkpoints, **Send API** for parallel operations
- **MCP Server** exposing mock enterprise APIs via stdio transport, secured with **OAuth 2.1 token exchange**
- **CI/CD pipeline** with LLM-as-a-judge: fail build if infinite loops detected, faithfulness < 0.85, or context drift > 15%
- **Agent memory** with Mem0 (semantic deduplication) + Graphiti (temporal knowledge graphs)
- **browser-use** for visual web automation, **Firecrawl** for structured data extraction
- **Daytona sandbox** for safe agent code execution (isolated kernel, network egress restricted)
- **Guardrails** + **NeMo Guardrails** for jailbreak detection and output safety
- **Cost tracking** middleware — exact USD cost per session
- **OpenTelemetry** traces for agent chain-of-thought
- **README** with: architecture diagram, design tradeoffs (OAuth 2.1 vs API keys, PostgresSaver vs InMemorySaver), Ragas metrics table, docker-compose instructions

---

## 📚 Study References (Curated Repos — Integrated into Daily Plan)

| Repository | Phase/Day | What to Study |
|-----------|-----------|---------------|
| ed-donner/agents | Phase 4 Day 32 | Week 4: LangGraph multi-agent routing templates and supervisor architectures |
| NirDiamant/Agent_Memory_Techniques | Phase 3 Day 28 | Notebooks 24-27: Mem0, Graphiti, Procedural Memory implementations |
| NirDiamant/rag_techniques | Phase 3 Day 26 | Proposition Generation, Step-back Prompting, Adaptive Retrieval patterns |
| NirDiamant/GenAI_Agents | Phase 3-4 | Agent architectures, tool-use patterns, multi-agent patterns |
| punkpeye/awesome-mcp-servers | Phase 4 Day 37 | Real-world MCP server implementations, OAuth 2.1 integrations, tool schema definitions |
| modelcontextprotocol/servers | Phase 4 Day 35 | Canonical MCP reference implementations (Filesystem, Everything servers) |
| OpenBMB/ToolBench | Phase 4 Day 34 | DFSDT algorithm, ToolEval metrics for multi-tool reasoning |
| firecrawl/firecrawl-workflows | Phase 4 Day 36 | Outcome-focused business skills (SEO audits, QA reports) for coding agents |
| EthicalML/awesome-production-agentic-systems | Phase 5 Day 43 | Standard CI/CD, AIBOM, observability tooling for agentic apps |
| openai/openai-agents-python | Phase 4 Day 38 | Agent handoffs, manager pattern, real-time voice streaming |
| browser-use/browser-use | Phase 4 Day 36 | Visual DOM understanding, multi-tab navigation, Playwright integration |
| daytonaio/daytona | Phase 5 Day 42 | Python SDK for sandbox creation, network isolation, ephemeral execution |
| guardrails-ai/guardrails | Phase 5 Day 41 | Input/output validators, PII detection, schema compliance |
| agno-agi/agno | Phase 5 Day 40 | Dual schema enforcement, JWT-based RBAC patterns |
| ashishps1/learn-ai-engineering | Phase 6 | System design interview prep, architecture blueprints |
| microsoft/ai-agents-for-beginners | Phase 4 | Beginner-friendly agent patterns, multi-agent design |
| Shubhamsaboo/awesome-llm-apps | Phase 2-3 | Real-world LLM application patterns, RAG variants |
| coleam00/ai-agents-masterclass | Phase 4 | Production agent patterns, tool-use architectures |
| e2b-dev/awesome-ai-agents | Phase 4 | Curated agent frameworks, tools, and evaluation platforms |
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
