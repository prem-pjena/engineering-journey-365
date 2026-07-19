# 📚 60-Day Agentic AI Engineer Sprint: Complete Curriculum (Market-Validated v2)

**Target Role:** Agentic AI Engineer | AI Engineer | SDE AI
**Target Compensation:** ₹30-50k/mo intern (Day 28) → ₹10-12 LPA FT / $24-40k/yr global remote (Day 60)
**Investment:** 5-6 hours daily. Zero days off.

---

## 📊 Complete Tech Stack (Market-Validated Priority Matrix)

| Priority | Category | Technologies |
|----------|----------|-------------|
| 🔴 Must-Know | Python Architecture | OOP (classes, inheritance, dunder, @property, static/classmethod), Context Managers, Async (asyncio, await, gather), Generators (yield), Tuples, enumerate, zip, String methods, JSON, Comprehensions, Type hints, Modules |
| 🔴 Must-Know | Backend API | **FastAPI**, Pydantic, **Asynchronous Python**, **Server-Sent Events (SSE)** for streaming (market standard — Django/Flask are obsolete for AI roles) |
| 🔴 Must-Know | LLM & Orchestration | LangChain (prompt templates, loaders, splitters, with_structured_output), Prompt Engineering (few-shot, CoT, system), LLM APIs (OpenAI, Gemini) — **LCEL deep dive deprioritized, use LangGraph for orchestration** |
| 🔴 Must-Know | Agent Frameworks | **LangGraph** (StateGraph, nodes, edges, reducers, routing, checkpointing, HITL, multi-agent, parallel) — industry standard for production agents |
| 🔴 Must-Know | RAG & Search | Naive → Advanced → Corrective → Adaptive → Agentic RAG, **Parent-Child Chunking**, **Semantic Chunking**, **Cross-encoder Reranking**, **Hybrid Search (BM25 + Dense)**, pgvector, ChromaDB |
| 🔴 Must-Know | Evaluation & Observability | **LangSmith**, **Langfuse/OpenLLMetry** (observability + tracing), **Ragas** (Faithfulness, Context Precision/Recall, Answer Relevancy) |
| 🔴 Must-Know | Constrained Decoding | **XGrammar / Outlines** — finite-state machine token masking for guaranteed JSON output. Prevents agent crashes from malformed tool calls |
| 🔴 Must-Know | Inference Optimization | **vLLM** (PagedAttention, continuous batching, Tensor Parallelism), KV cache management, Quantization (INT8/INT4) — essential for open-source model serving |
| 🔴 Must-Know | Semantic Caching | **Redis** with vector embedding + cosine similarity threshold tuning (0.85-0.95) + hybrid metadata filtering for tenant isolation |
| 🔴 Must-Know | SQL & Vectors | PostgreSQL, pgvector, HNSW vs IVFFlat indexing, vector similarity search |
| 🔴 Must-Know | DSA | **Pareto 50** — Arrays & Hashing, Two Pointers, Sliding Window, Stack & Queue, Binary Search, Linked Lists, Trees (BFS/DFS), Graphs (BFS/DFS/Topo Sort/Cycle Detection), Intervals, Backtracking, Heaps, Design (LRU Cache, Trie, Time-Based KV), DP Basics. **Explicitly skip**: Coin Change, LIS, Word Ladder, Trapping Rain Water, Largest Rectangle — zero ROI for Agentic AI startup interviews |
| 🟡 Good-to-Have | Full-Stack | **Next.js + TypeScript** (unlocks Full Stack AI Engineer roles — premium pay for end-to-end delivery) |
| 🟡 Good-to-Have | Data | Pandas, NumPy basics |
| 🟡 Good-to-Have | Interview Theory | Transformer architecture (Q, K, V, self-attention, RoPE), BERT vs GPT, tokenization high-level concept, LLM inference architecture (vLLM, KV cache) |
| ⚪ Nice-to-Have | Fine-tuning | LoRA / PEFT — 8.5% JD mention vs RAG 35.9%. Read 1 article for concept only |
| 🚫 Skip | CNNs/RNNs/Classical ML | Zero JD mentions for GenAI Engineer roles. Skip bias-variance, cross-validation, gradient descent entirely |

---

## 📅 60-Day Complete Curriculum (Market-Validated)

### Phase 1: Python Completion + LLM APIs (Days 11-17)
*Goal: Complete Python foundation, learn FastAPI, start using LLM APIs*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 11 | OOP: classes, inheritance, dunder, @property, @staticmethod, @classmethod | Build mock VectorStore class | Two Sum | vector_store_oop.py |
| 12 | Context Managers (`__enter__`, `__exit__`), Modules, `__init__.py` | Safe File I/O Manager + Package refactor | Valid Anagram | context_logger.py |
| 13 | Async Python: asyncio, event loop, gather + **FastAPI intro** | Build first FastAPI endpoint (GET/POST) | Group Anagrams | fastapi_hello.py |
| 14 | Generators (yield), Tuples, enumerate, zip | Build streaming token generator | Top K Frequent | token_streamer.py |
| 15 | String methods, JSON module | Parse nested JSON LLM outputs | Product of Array | json_parser.py |
| 16 | LLM APIs: OpenAI/Gemini, temperature, tokens, streaming | Chat + streaming response | Valid Palindrome | basic_llm_api.py |
| 17 | Prompt Engineering: few-shot, CoT, system prompts | Test prompts for different personas | 3Sum | prompt_engineering.py |

### Phase 2: LangChain + RAG Core (Days 18-24)
*Goal: Master LangChain, build RAG pipelines, learn SQL + pgvector*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 18 | FastAPI SSE Streaming + Pydantic | Build streaming endpoint, understand Server-Sent Events | **Container With Most Water + Two Sum II** — optimization bounds + sorted pointer matching | fastapi_streaming.py |
| 19 | **Constrained Decoding (XGrammar/Outlines)** | Compile Pydantic schema → FSM → guaranteed JSON output | Longest Substring | constrained_decoding.py |
| 20 | Document Loaders, Text Splitters, **Semantic Chunking** | Parse PDF, split by semantic boundaries | Valid Parentheses | semantic_chunker.py |
| 21 | Vector DBs, Embeddings, ChromaDB | Store chunks + similarity search | Binary Search | chroma_ingestion.py |
| 22 | **Naive RAG**: chunk → embed → store → retrieve → generate | End-to-end RAG script | Search 2D Matrix | naive_rag.py |
| 23 | **SQL + pgvector basics**: SELECT, INSERT, JOINs, vector columns | Store embeddings in PostgreSQL | Reverse Linked List | pgvector_setup.sql |
| 24 | **Parent-Child Chunking + Cross-Encoder Reranking** | Rerank top-20 to top-3 with BGE | Merge Two Sorted | reranked_rag.py |

### Phase 3: Advanced RAG + Evaluation + Project 1 (Days 25-31)
*Goal: Master advanced RAG patterns, programmatic evaluation, build & deploy Project 1*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 25 | **Hybrid Search**: BM25 + Dense Vector, pgvector HNSW vs IVFFlat | Implement hybrid search + index tuning | Reorder List | hybrid_search.py |
| 26 | **Corrective RAG (CRAG)** + **Adaptive RAG** | Evaluator → web search fallback + router | Max Depth Tree | corrective_adaptive_rag.py |
| 27 | **Conversational RAG + Agentic RAG** | Chat history injection + agent re-queries | **Validate BST** | conversational_rag.py |
| 28 | **LangSmith + Ragas Evaluation**: Faithfulness, Context Precision, Answer Relevancy | Build golden dataset + eval pipeline | Invert Tree | ragas_evaluation.py |
| 29 | **PROJECT 1 BUILD**: Multi-Tenant RAG System | FastAPI + pgvector + LangGraph supervisor + MCP tools | LCA of BST | project1_start/ |
| 30 | PROJECT 1 continued: Docker containerize + Cross-encoder + Hybrid Search | Complete all features + eval | Level Order Traversal | project1_continue/ |
| 31 | **PROJECT 1 DONE**: Deploy to AWS ECS + Ragas eval report + **APPLY blitz** | Wellfound + YC applications with Project 1 as proof | **Longest Consecutive Sequence** | project1_deployed/ |

### Phase 4: LangGraph Mastery + MCP (Days 32-39)
*Goal: Master stateful agents, MCP protocol, LangSmith tracing*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 32 | LangGraph: StateGraph, Nodes, Edges, State | Linear 3-node state machine. Reference: ed-donner/agents Week 4 labs | Course Schedule | basic_state_graph.py |
| 33 | LangGraph: Reducers, add_messages, Conditional Routing + **DFSDT Concept** | Chatbot with memory + intent router. **DFSDT**: Depth-First Search Decision Tree — explores multiple tool paths and backtracks on failure (beats linear ReAct for complex multi-tool tasks) | Climbing Stairs | stateful_chatbot.py |
| 34 | LangGraph: Checkpointing, Human-in-the-loop | Approval interrupt before tool execution | **LRU Cache** | hitl_agent.py |
| 35 | LangGraph: Multi-agent Supervisor Pattern | Supervisor → 2 worker agents | **Task Scheduler** — rate-limit emulation for agent API calls | supervisor_agent.py |
| 36 | LangSmith Tracing for LangGraph | Instrument multi-agent system | **Min Stack** — state history snapshots | langsmith_tracing.py |
| 37 | MCP: Host/Client/Server, stdio transport | Python MCP server with tools. **Study**: modelcontextprotocol/servers Filesystem server as reference pattern | Merge Intervals | mcp_stdio_server.py |
| 38 | MCP: HTTP SSE, JSON-RPC 2.0, Tools vs Resources vs Prompts | DB schema as MCP Resource. **Study**: modelcontextprotocol/servers Everything server (exercises ALL MCP features) | Insert Interval | mcp_http_server.py |
| 39 | **LangGraph + MCP Integration** | Agent discovers and calls MCP tools. **Study**: ed-donner/agents Week 6 MCP labs | **Course Schedule II** — extract exact execution sequence for dependent agents | langgraph_mcp_agent.py |

### Phase 5: Full-Stack + Production Patterns (Days 40-46)
*Goal: Build end-to-end AI apps, deploy with CI/CD, add UI layer*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 40 | FastAPI Deep Dive: error handling, middleware, streaming, background tasks, SSE. **Add Guardrails** for LLM output validation (PII, toxicity, schema compliance) | Production-grade FastAPI app with Guard input/output validation | **Kth Largest in Stream** — real-time ranking of telemetry logs | fastapi_production.py |
| 41 | **vLLM Inference**: PagedAttention, continuous batching, TP, KV cache | Deploy model with vLLM, measure TTFT | **K Closest Points to Origin** — mimics vector distance retrieval | vllm_basics.py |
| 42 | **Redis Semantic Caching**: embeddings, cosine threshold (0.85-0.95), hybrid metadata filters | Build semantic cache layer | **Best Time to Buy/Sell Stock** — time-series max delta extraction in telemetry | semantic_cache.py |
| 43 | **Next.js + TypeScript basics** + SSE streaming from FastAPI | Chat UI with real-time streaming | **Longest Repeating Char Replacement** — noise/error tolerance in prompt parsing | fullstack_chat_app/ |
| 44 | **AWS ECS**: Deploy full stack to cloud | Fargate + RDS + Load Balancer | **Linked List Cycle** — infinite loop detection in linear agent state nodes | aws_deploy_logs/ |
| 45 | **GitHub Actions CI/CD**: Auto-test, auto-eval, auto-deploy | Push → test → deploy pipeline | 3Sum review | .github/workflows/ci.yml |
| 46 | Cost tracking per query + Prompt versioning + A/B testing | Metadata wrapper + toggle prompts | Min Window Substring | cost_tracker.py |

### Phase 6: System Design + Interview Prep (Days 47-53)
*Goal: Ace AI System Design and ML/NLP interview rounds*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 47 | **System Design**: RAG at scale, semantic caching (Redis), query routing, hybrid metadata filtering | Architecture diagram for 1M QPD | **Find Min Rotated + Search in Rotated Array** — offset pivot detection + disjoint partition search | rag_architecture.md |
| 48 | **System Design**: Multi-tenant isolation, latency optimization, LLM Gateway, vLLM inference architecture | Gateway design + PagedAttention explanation | **Subsets** — generate all combinations of prompt options or tool params | inference_architecture.md |
| 49 | **LLM Inference Concepts**: vLLM, PagedAttention, continuous batching, KV cache, quantization (INT8/INT4), constrained decoding deep dive | Explain each concept with real examples | Serialize/Deserialize Tree | llm_inference_interview.md |
| 50 | **NLP Concepts**: Transformer (QKV, self-attention, RoPE), BERT vs GPT, tokenization (high-level), MoE, speculative decoding | tiktoken counter + attention visualization | **Permutations** — reorder tool execution sequences to evaluate optimal logic paths | nlp_concepts.md |
| 51 | DSA Mock + Portfolio Review | Solve problems + polish GitHub | Word Search | mock_interview_log |
| 52 | System Design Mock + Behavioral | Practice "termination narrative" + why AI | **Combination Sum** — aggregate params to meet a computational threshold | behavioral_prep.md |
| 53 | Live Coding Mock (FastAPI + LangGraph) | Build a mini agent under time pressure | **Clone Graph** — duplicate agent states for parallel processing | live_coding_mock/ |

### Phase 7: Project 2 + Apply FT (Days 54-60)
*Goal: Build standout capstone, apply aggressively, secure offers*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 54 | **PROJECT 2 BUILD**: Multi-Agent MCP Orchestrator | FastAPI + LangGraph + MCP + Next.js UI | **Implement Trie (Prefix Tree)** — autocomplete for token search, foundational for LLM tokenizers | project2_start/ |
| 55 | PROJECT 2 continued: Docker + GitHub Actions + AWS ECS | Full CI/CD pipeline | **Time Based Key-Value Store** — manage temporal states across long-running agents | project2_continue/ |
| 56 | **PROJECT 2 DONE**: Ragas eval + Deploy + README | Production-grade project with docs | **Number of Islands + Max Area of Island** — graph clustering, quantifying connected tasks | project2_deployed/ |
| 57 | **APPLY BLITZ**: Wellfound (20 apps) + YC (10) + LinkedIn DMs (10) | Personalized messages with project links | **Redundant Connection** — cycle detection in undirected graphs to prevent execution loops | application_log.md |
| 58 | Follow-ups + Mock interviews | Respond to callbacks, practice behavioral | **Evaluate Reverse Polish Notation** — parsing dynamic calculator agent commands | interview_tracker.md |
| 59 | Buffer / Offer evaluation | Compare offers, negotiate | Rest | offer_evaluation.md |
| 60 | **CELEBRATE + PLAN NEXT** | ₹10-12 LPA offer in hand | — | done.md |

---

## 📋 2 Projects to Build (Market-Aligned)

### Project 1: Multi-Tenant Enterprise RAG System (Days 29-31)
**Tech Stack:** FastAPI + pgvector + LangGraph + MCP + Docker + AWS ECS + LangSmith/Ragas
**Features:**
- Row-level security in pgvector for data isolation
- LangGraph supervisor agent → routes queries to vector DB / MCP web search / conversation memory
- Parent-child chunking + cross-encoder reranking
- Hybrid search (BM25 + dense vector)
- Ragas evaluation in CI/CD
- **Interview signal:** "Hire me" — shows architectural maturity

### Project 2: Multi-Agent MCP Orchestrator (Days 54-56)
**Tech Stack:** FastAPI + LangGraph + MCP + Next.js/TypeScript + Docker + AWS ECS + GitHub Actions
**Features:**
- Multiple specialized agents (Research → Analysis → Review)
- MCP servers for each tool category (DB, search, computation)
- Next.js chat UI with streaming responses
- Full CI/CD pipeline (push → test → eval → deploy)
- Error handling + fallback logic for every edge case
- **Interview signal:** "Full-stack AI Engineer" — end-to-end delivery capability

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
| Pandas/NumPy as full week | Moved to 1-day Good-to-Have (Day 16 replaced with LLM APIs) |
| Apna.co as primary platform | Low signal, legacy IT, fake AI listings |

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
- **LangGraph** with dual-channel memory (persistent + ephemeral scratchpad)
- **MCP Server** exposing mock enterprise APIs via stdio transport
- **CI/CD pipeline** with Ragas: fail build if faithfulness < 0.85 or context precision < 0.90
- **Cost tracking** middleware — exact USD cost per session
- **OpenTelemetry** traces for agent chain-of-thought
- **README** with: architecture diagram, design tradeoffs (HNSW vs IVFFlat), Ragas metrics table, docker-compose instructions

---

## 🏛️ Design Patterns for AI Engineers

| Pattern | When to Use |
|---------|-------------|
| **ReAct** (Reason + Act) | Exploratory tasks with dynamic API interaction |
| **Plan-and-Execute** | Complex long-horizon tasks needing decomposition |
| **Evaluator-Optimizer** | Code generation, data extraction requiring high accuracy |
| **Tool-Use** | Structured data extraction with function calling |
| **Multi-Agent (Supervisor)** | Multiple specialized agents routed by a central LLM |
| **MCP Integration** | Secure enterprise tool access without hardcoded APIs |
| **Agentic RAG** | Dynamic retrieval where agent rewrites queries if results poor |

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
