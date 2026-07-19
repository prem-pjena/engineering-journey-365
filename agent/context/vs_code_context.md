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
| 1 | 11-17 | Python Completion + FastAPI + LLM APIs | CLI chat + FastAPI endpoint |
| 2 | 18-24 | LangChain + RAG Core + pgvector | RAG pipeline |
| 3 | 25-31 | Advanced RAG + LangSmith/Ragas + **Project 1 + DEPLOY + APPLY** | Multi-Tenant RAG deployed |
| 4 | 32-39 | LangGraph Mastery + MCP | Stateful agents + MCP integration |
| 5 | 40-46 | Full-Stack (Next.js UI) + Production (Docker, AWS ECS, Bedrock, CI/CD) | End-to-end deployed app |
| 6 | 47-53 | System Design (RAG at scale, Redis caching, KV cache) + ML/NLP Interview Prep | Interview ready |
| 7 | 54-60 | **Project 2 + DEPLOY + APPLY FT** | Multi-Agent MCP Orchestrator |

## ALL Concepts (Market-Validated)
### 🔴 Must-Know
- **Python:** OOP (classes, inheritance, dunder, @property, static/classmethod), Context Managers, Async (asyncio, gather), Generators, Tuples, enumerate, zip, String methods, JSON, Type hints, Modules
- **Backend:** FastAPI, Pydantic, Asynchronous Python, Constrained Decoding (Outlines/XGrammar for guaranteed JSON output)
- **LLM:** LangChain (LCEL, templates, loaders, splitters, structured output), Prompt Engineering (few-shot, CoT, system), LLM APIs (OpenAI, Gemini)
- **Sampling params:** Temperature (0-2), top-k, top-p, max_tokens, frequency penalty — used on EVERY API call
- **Agents:** LangGraph (StateGraph, nodes, edges, reducers, routing, checkpointing, HITL, multi-agent supervisor, parallel)
- **RAG:** Naive → Advanced → Corrective (CRAG) → Adaptive → Conversational → Agentic RAG
- **Search:** Hybrid Search (BM25 + Dense), pgvector, ChromaDB, Parent-Child Chunking, Semantic Chunking, Cross-encoder Reranking, HNSW vs IVFFlat
- **Evaluation:** LangSmith, Ragas (Faithfulness, Context Precision, Answer Relevancy)
- **MCP:** Model Context Protocol (Host/Client/Server, stdio vs HTTP SSE, Tools/Resources/Prompts, JSON-RPC 2.0). **Study**: modelcontextprotocol/servers repo — canonical reference implementations. ed-donner/agents Week 6 for hands-on labs.
- **Tool Planning:** **DFSDT** (Depth-First Search Decision Tree) — explores multiple tool paths and backtracks on failure. Beats linear ReAct for complex multi-tool scenarios. From OpenBMB/ToolBench research.
- **LLM Safety:** **Guardrails** (guardrails-ai/guardrails) — input/output validators for PII, toxic language, schema compliance, competitor checking. Add to Phase 5 FastAPI backend.
- **Deployment:** Docker, AWS ECS Fargate, AWS Bedrock, GitHub Actions CI/CD
- **SQL:** PostgreSQL, pgvector, vector similarity search, HNSW index tuning (ef_search, m)
- **DSA:** **Pareto 50** — Arrays & Hashing, Two Pointers, Sliding Window, Stack & Queue, Binary Search, Linked Lists, Trees (BFS/DFS), Graphs (BFS/DFS/Topo Sort/Cycle Detection), Intervals, Backtracking, Heaps, Design (LRU Cache, Trie, Time-Based KV), DP Basics. **Explicitly skip**: Coin Change, LIS, Word Ladder, Trapping Rain Water, Largest Rectangle — zero ROI for Agentic AI startup interviews

### 🟡 Good-to-Have
- **Full-Stack:** Next.js + TypeScript (chat UI components, streaming responses)
- **Data:** Pandas, NumPy, Scikit-learn basics
- **Inference:** vLLM engine (PagedAttention, continuous batching), KV cache management, VRAM capacity planning
- **Cost Optimization:** Quantization (INT8/INT4 — AWQ, GPTQ), Redis Semantic Caching
- **Interview Theory:** Transformer (QKV, self-attention, RoPE), BERT vs GPT, BPE/WordPiece tokenization, bias-variance, precision/recall/F1
- **AWS:** Bedrock API, ECS Fargate, CloudWatch logging

### 🚫 Skipped (Research-Validated)
- Training CNNs/RNNs from scratch, Django/Flask, deep ML math (gradient descent), Apna.co
- Fine-tuning (LoRA/PEFT): Read 1 article only. Only 8.5% of JDs mention it.
- Classical ML pipelines: AI Engineers build LLM pipelines, not training pipelines

## 2 Key Projects
### Project 1 (Days 29-31): Multi-Tenant Enterprise RAG System
- FastAPI + pgvector (row-level security) + LangGraph supervisor + MCP tools + Cross-encoder reranking + Hybrid Search + Docker + AWS ECS + Ragas eval
- Apply signal: "Hire me" — architectural maturity

### Project 2 (Days 54-56): Multi-Agent MCP Orchestrator
- FastAPI + LangGraph (supervisor → workers) + MCP servers + Next.js UI + Docker + AWS ECS + GitHub Actions CI/CD + Error handling + Fallback logic
- **Optional enhancement:** Integrate browser-use as a tool for web UI interaction
- Apply signal: "Full-stack AI Engineer" — end-to-end delivery

## Key Interview Answers (From Deep Research)
1. "Why RAG over Fine-tuning?": RAG solves knowledge, fine-tuning solves behavior. Start with RAG + prompting.
2. "Transformer architecture?": Self-attention is O(n²). Place critical instructions at end of prompt for highest attention weight.
3. "How to ensure JSON output?": Constrained decoding with Outlines/XGrammar — logit masks guarantee schema compliance.
4. "How to optimize costs?": Compound AI systems — cheap SLM router + expensive frontier model only for complex tasks.
5. "AWS for AI?": Bedrock for serverless, ECS Fargate for persistent backends, Aurora pgvector for RAG.

## Key Files
- agent/learning_plan.md — market-validated v2 curriculum (MOST UPDATED)
- agent/day_syllabus.md — live day tracker with 7-phase structure
- agent/skill_tracker.md — scores with new skills (FastAPI, LangGraph, MCP, LangSmith, Next.js)
- agent/reports/current_status.md — full status with research-backed targets
- agent/reports/market_research_2026.md — salary validation data
- agent/reports/market_research_deep_2026.md — company mapping, tech stack, skill gaps
- agent/learnings/rag_architecture_14_types.md — all RAG types with 12 LPA interview answers
- agent/learnings/gold_mines_repo_analysis.md — deep analysis of 7 key repos: Guardrails (production safety with validators), ed-donner/agents (6-week agent curriculum matching Phases 1-4), agno-agi/agno (full-stack agent framework, LangGraph alternative), modelcontextprotocol/servers (official MCP reference implementations — study for Phase 4), browser-use/browser-use (AI browser agent with MCP server/client — use in Project 2), OpenBMB/ToolBench (DFSDT algorithm that beats ReAct for multi-tool scenarios, ToolEval metrics), EthicalML/awesome-production-agentic-systems (master index of production agentic tools)
