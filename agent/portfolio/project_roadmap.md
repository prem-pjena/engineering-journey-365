# 🗺️ Portfolio Project Roadmap — Top 1% Strategy

**Core Philosophy:** 2 projects. 4 phases. 12 months. Each evolves.

| Project | Phase 1 (Months 1-3) | Phase 2 (Months 4-6) | Phase 3 (Months 7-9) | Phase 4 (Months 10-12) |
|---------|----------------------|----------------------|----------------------|-----------------------|
| **P1: RAG System** | v1.0 — Basic RAG + RBAC | v2.0 — Semantic Cache + Ragas CI | v3.0 — Hybrid Search + Reranking | vFinal — Multi-tenant + Token Budgeting |
| **P2: MCP Agent** | v1.0 — Basic MCP + LangGraph | v2.0 — Multi-Agent Orchestrator | v3.0 — Enterprise with Human-in-loop | vFinal — Unified Platform |

---

## 📋 Project 1: RAG System (Evolving)

### Phase 1 (Months 1-3) — v1.0: Enterprise RAG with RBAC 🔐
**For:** Domestic interviews (₹50k+/mo)

| Aspect | Detail |
|--------|--------|
| **What** | RAG over documents with role-based access control |
| **Stack** | FastAPI + PostgreSQL/pgvector + OpenAI + LangChain + Docker |
| **Features** | PDF upload → chunk → embed → store → query with citations |
| **Eval** | Basic Ragas scoring (faithfulness, answer relevance) |
| **Deployment** | Dockerized on AWS EC2 |
| **UI** | Streamlit or Gradio |
| **READ ME Must Have** | Architecture diagram, Ragas scores, setup instructions |

### Phase 2 (Months 4-6) — v2.0: Cost-Optimized Cache + Eval CI
**For:** Global remote interviews ($80-110k USD)

| Upgrade | Why It Matters |
|---------|----------------|
| **Semantic Caching** (Redis + SentenceTransformers) | Proves cost consciousness — 30% cost reduction |
| **Model Routing** (LiteLLM cascade) | Shows understanding of quality/cost tradeoff — 68% savings |
| **Prompt Compression** | 20-40% token reduction, zero quality loss |
| **Ragas CI Pipeline** | Auto-eval on every git push — block merge if faithfulness drops |
| **Langfuse Observability** | P95 latency, token cost dashboard |

### Phase 3 (Months 7-9) — v3.0: Advanced RAG
**For:** Top 5% differentiation

| Upgrade | Why It Matters |
|---------|----------------|
| **Hybrid Search** (BM25 + dense vectors) | Beats naive vector search |
| **Cross-Encoder Reranking** (Cohere/BGE) | Filters low-signal chunks → smaller context → cheaper + better |
| **Temporal Graph RAG** (Neo4j) | Timestamped facts, recency prioritization |

### Phase 4 (Months 10-12) — vFinal: Enterprise Multi-Tenant
**For:** Top 1% / staff-level

| Upgrade | Why It Matters |
|---------|----------------|
| **Multi-Tenant Token Budgeting** | Tiered budgets per customer |
| **Cost Dashboard** | Real-time USD savings visualization |
| **Circuit Breakers** | Auto-protect against abuse |
| **Enterprise Security** | RBAC, audit logging, prompt injection prevention |

---

## 📋 Project 2: MCP Multi-Agent System (Evolving)

### Phase 1 (Months 1-3) — v1.0: Basic MCP Server + LangGraph Agent 🔌
**For:** Domestic interviews (₹50k+/mo)

| Aspect | Detail |
|--------|--------|
| **What** | LangGraph agent that uses MCP server to query a database |
| **Stack** | LangGraph + FastMCP + FastAPI + SQLite/PostgreSQL + Docker |
| **Features** | MCP server exposing read-only SQL, agent as MCP client, Planner→Search→Synthesizer |
| **Deployment** | Dockerized on AWS EC2 |
| **READ ME Must Have** | MCP architecture diagram, example query flow |

### Phase 2 (Months 4-6) — v2.0: Multi-Agent Orchestrator
**For:** Global remote interviews

| Upgrade | Why It Matters |
|---------|----------------|
| **3 Agents** (Planner/Searcher/Synthesizer) | Shows multi-agent orchestration |
| **Dynamic MCP Discovery** | Agent finds available servers at runtime |
| **Checkpointing** | State persistence across nodes |
| **Error Recovery** | Circuit breaker for agent loops |

### Phase 3 (Months 7-9) — v3.0: Enterprise MCP
**For:** Top 5% differentiation

| Upgrade | Why It Matters |
|---------|----------------|
| **2-3 Custom MCP Servers** (DB, filesystem, web search) | MCP is the #1 diff in 2026 |
| **Human-in-the-loop** | Approval gates for sensitive operations |
| **Self-Healing Code** (Pydantic + Instructor) | Auto-repair malformed JSON |
| **Ragas Agent Eval** | Tool call accuracy metrics in README |

### Phase 4 (Months 10-12) — vFinal: Unified Platform
**For:** Top 1% / founder-ready

| Upgrade | Why It Matters |
|---------|----------------|
| **Combine P1 + P2** | RAG pipeline feeds agent's knowledge |
| **Enterprise Security** | RBAC, audit logging, compliance |
| **AWS Enterprise** | ECS, Bedrock, API Gateway |
| **Deployed + Documented** | Live demo, video walkthrough, technical blog |

---

## 🏆 BONUS: Open Source Strategy (Months 4-12)

| Month | Target | Contribution Type |
|-------|--------|-------------------|
| 4-5 | LiteLLM | Bug fixes, docs |
| 5-6 | Ragas | Test cases, edge cases |
| 7-8 | FastMCP | Integration examples |
| 8-9 | LangChain | Documentation, bug fixes |
| 9-10 | DSPy or LangGraph | Feature contributions |

**Target:** 5+ merged PRs by Month 12. Each PR = top 1% signal.

---

## 📊 Global Hiring Requirements Checklist

| Requirement | Domestic (Oct 1) | Global (Dec 2027) |
|-------------|-----------------|-------------------|
| 2 deployed projects | ✅ Live on AWS | ✅ Live on AWS |
| Ragas eval scores | ✅ In README | ✅ In README + CI gate |
| Architecture diagrams | ✅ Mermaid/Excalidraw | ✅ Mermaid/Excalidraw |
| Live demo URL | ✅ | ✅ |
| Video walkthrough | Optional | ✅ Recommended |
| LLM observability | ❌ | ✅ Langfuse dashboard |
| Cost optimization | ❌ | ✅ Semantic cache + routing |
| MCP servers | 1 basic | ✅ 2-3 custom |
| Open source PRs | 0 | ✅ 5+ merged |
| Technical blog posts | 0 | ✅ 3+ articles |
| Personal website | ❌ | ✅ Next.js portfolio |
| TypeScript/Next.js UI | ❌ | ✅ Basic frontend |
| Unit tests | ✅ | ✅ Comprehensive |
| CI/CD pipeline | ✅ GitHub Actions | ✅ + Ragas eval gate |

---

## 💰 Salary Targets

| Target | Timeline | Monthly In-Hand |
|--------|----------|-----------------|
| Domestic (₹6-9 LPA) | Month 3 (Oct 1) | ~₹50-65k |
| Global Remote ($60-80k USD) | Month 6-9 | ~₹4.4-5.8L/mo (44ADA) |
| Global Remote ($80-120k USD) | Month 12 | ~₹5.8-8.7L/mo (44ADA) |
| Indian Product (₹18-30 LPA) | Month 12 (backup) | ~₹1.2-2L/mo |

---

*Based on "The Elite AI Engineer Blueprint" — Gemini Deep Research (Jul 2026)*
