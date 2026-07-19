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
| 1 | 11-17 | Python + FastAPI + Algorithmic Prompting (DSPy/GEPA) | CLI chat + FastAPI endpoint + compiled prompts |
| 2 | 18-24 | LangChain + Advanced RAG (Proposition Gen, Step-back, GraphRAG) + pgvector | Advanced RAG pipeline |
| 3 | 25-31 | Adaptive RAG + Agentic Memory (Mem0/Graphiti) + LLM-as-a-judge Eval + **Project 1 + DEPLOY + APPLY** | Multi-Tenant Knowledge Agent deployed |
| 4 | 32-39 | LangGraph (PostgresSaver, Send API) + Web Automation (browser-use/Firecrawl) + MCP (OAuth 2.1) + OpenAI Agents SDK | Stateful agents + web + MCP integration |
| 5 | 40-46 | Security (Agno RBAC, AgentShield, NeMo) + Sandboxed Execution (Daytona) + vLLM + Redis + Next.js + CI/CD | Secure, sandboxed deployed app |
| 6 | 47-53 | System Design (RAG scale, LangGraph scaling) + MCP Security (OWASP Top 10) + Advanced Memory Theory (Procedural, Blackboard) | Interview ready |
| 7 | 54-60 | **Project 2 + DEPLOY + APPLY FT** | Autonomous Code & Web Intelligence Swarm |

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
- **Search:** Hybrid Search (BM25 + Dense), pgvector, ChromaDB, HNSW vs IVFFlat
- **Evaluation:** LangSmith, Langfuse/OpenLLMetry, Ragas (Faithfulness, Context Precision, Answer Relevancy), **LLM-as-a-judge** regression testing, **AIBOM** supply chain tracking
- **MCP:** Model Context Protocol (Host/Client/Server, stdio vs HTTP SSE, Tools/Resources/Prompts, JSON-RPC 2.0). **OAuth 2.1 mandatory** (token exchange, no passthrough, per-client consent). Study: modelcontextprotocol/servers, punkpeye/awesome-mcp-servers
- **Agent Security:** **Dual Schema Enforcement** (Agno — read-only scopes for data agents), **JWT-based RBAC**, **AgentShield** (config vuln scanning), **NeMo Guardrails** (Colang for topical bounding, jailbreak detection)
- **Tool Planning:** **DFSDT** (Depth-First Search Decision Tree) — explores multiple tool paths and backtracks on failure. From OpenBMB/ToolBench
- **LLM Safety:** **Guardrails** (guardrails-ai/guardrails) — input/output validators for PII, toxic language, schema compliance
- **Deployment:** Docker, AWS ECS Fargate, AWS Bedrock, GitHub Actions CI/CD
- **SQL:** PostgreSQL, pgvector, vector similarity search, HNSW index tuning (ef_search, m), **read-only transaction scopes**
- **DSA:** **Pareto 50** — Arrays & Hashing, Two Pointers, Sliding Window, Stack & Queue, Binary Search, Linked Lists, Trees (BFS/DFS), Graphs (BFS/DFS/Topo Sort/Cycle Detection), Intervals, Backtracking, Heaps, Design (LRU Cache, Trie, Time-Based KV), DP Basics. **Explicitly skip**: Coin Change, LIS, Word Ladder, Trapping Rain Water, Largest Rectangle

### 🟡 Good-to-Have
- **Full-Stack:** Next.js + TypeScript (chat UI components, streaming responses)
- **Data:** Pandas, NumPy, Scikit-learn basics
- **Inference:** vLLM engine (PagedAttention, continuous batching), KV cache management, VRAM capacity planning
- **Cost Optimization:** Quantization (INT8/INT4 — AWQ, GPTQ), Redis Semantic Caching
- **Interview Theory:** Transformer (QKV, self-attention, RoPE), BERT vs GPT, BPE/WordPiece tokenization, bias-variance, precision/recall/F1, **MCP OWASP Top 10**, **Procedural vs Episodic vs Semantic Memory**
- **AWS:** Bedrock API, ECS Fargate, CloudWatch logging

### 🚫 Skipped (Research-Validated)
- Training CNNs/RNNs from scratch, Django/Flask, deep ML math (gradient descent), Apna.co
- Fine-tuning (LoRA/PEFT): Read 1 article only. Only 8.5% of JDs mention it.
- Classical ML pipelines: AI Engineers build LLM pipelines, not training pipelines
- **Naive RAG:** Deprioritized in favor of Proposition Generation, Step-back Prompting, and GraphRAG
- **InMemorySaver:** Restricted to testing only. Use PostgresSaver for production
- **Static API keys for MCP:** Deprecated. OAuth 2.1 token exchange is mandatory

## 2 Key Projects
### Project 1 (Days 29-31): Multi-Tenant Enterprise Knowledge Agent
- FastAPI + pgvector (RLS) + LangGraph + MCP + Mem0 + Graphiti + Cross-encoder reranking + Hybrid Search + Docker + AWS ECS + Ragas eval + LLM-as-a-judge
- **Agno dual-schema:** read-only transaction scopes for data agents, isolated schema for engineer agents
- **JWT-based RBAC** for multi-tenant isolation
- Apply signal: "Hire me" — architectural maturity with security awareness

### Project 2 (Days 54-56): Autonomous Code & Web Intelligence Swarm
- FastAPI + LangGraph (Blackboard pattern with optimistic locking) + browser-use + Firecrawl + Daytona + MCP (OAuth 2.1) + Next.js UI + Docker + AWS ECS + GitHub Actions CI/CD
- **Researcher Agent:** browser-use + Playwright for visual DOM, multi-tab SPA navigation
- **Coder Agent:** Python workflows inside isolated Daytona sandboxes
- **MCP servers secured via OAuth 2.1** token exchange, per-client consent registries
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
- agent/learnings/rag_architecture_14_types.md — all RAG types with 12 LPA interview answers
- agent/learnings/gold_mines_repo_analysis.md — deep analysis of 7 key repos: Guardrails (production safety with validators), ed-donner/agents (6-week agent curriculum matching Phases 1-4), agno-agi/agno (full-stack agent framework, LangGraph alternative), modelcontextprotocol/servers (official MCP reference implementations — study for Phase 4), browser-use/browser-use (AI browser agent with MCP server/client — use in Project 2), OpenBMB/ToolBench (DFSDT algorithm that beats ReAct for multi-tool scenarios, ToolEval metrics), EthicalML/awesome-production-agentic-systems (master index of production agentic tools)
