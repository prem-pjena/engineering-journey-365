# 🗺️ Portfolio Project Roadmap (Dual Goal)

**Short-term Goal:** 2 deployed projects that land a ₹50k+/mo domestic AI role by Oct 1
**Long-term Goal:** Same projects upgraded → land $80-110k USD remote role by Dec 2027

---

## Project 1: Enterprise RAG System with RBAC 🔐
**Timeline:** Weeks 5-6 (Jul 29 - Aug 11) — For domestic interviews
**Upgraded By:** Month 6 (Jan 2027) — For global interviews

### Phase 1 (Domestic — Jul/Aug)
| Aspect | Detail |
|--------|--------|
| **What** | RAG over documents with role-based access control |
| **Skills shown** | FastAPI, pgvector, LangChain, OpenAI, Docker, AWS EC2 |
| **Stack** | FastAPI + PostgreSQL/pgvector + OpenAI + Docker + AWS |
| **Features** | PDF upload → chunk → embed → store → query with citations |
| **Eval** | Basic Ragas scoring (faithfulness, answer relevance) |
| **Deployment** | Dockerized on AWS EC2 |
| **UI** | Streamlit or Gradio |
| **LinkedIn angle** | "Built RAG system with automated evaluation achieving 92% faithfulness" |

### Phase 2 (Global Upgrade — Dec/Jan)
| Addition | Why It Matters for Global Hiring |
|----------|----------------------------------|
| Hybrid search (BM25 + dense) | Filters out "naive RAG" candidates |
| Cross-encoder reranking | Shows understanding of precision |
| Ragas eval scores in README | Proves quantitative thinking |
| LLM observability (Langfuse) | Proves production readiness |
| Architecture diagram (Mermaid) | Shows system design capability |

---

## Project 2: MCP-Enabled Multi-Agent System 🔌
**Timeline:** Weeks 7-8 (Aug 12-25) — For domestic interviews
**Upgraded By:** Month 6-7 (Jan/Feb 2027) — For global interviews

### Phase 1 (Domestic — Aug)
| Aspect | Detail |
|--------|--------|
| **What** | LangGraph agent that uses MCP server to query a database |
| **Skills shown** | LangGraph, FastMCP, AI Agents, tool calling, state management |
| **Stack** | LangGraph + FastMCP + FastAPI + SQLite/PostgreSQL + Docker |
| **Features** | Planner → Search → Synthesizer pattern, state persistence |
| **Deployment** | Dockerized on AWS EC2 |
| **LinkedIn angle** | "Built MCP-enabled autonomous agent for database querying" |

### Phase 2 (Global Upgrade — Dec/Jan)
| Addition | Why It Matters |
|----------|----------------|
| 2-3 custom MCP servers (DB, filesystem, web search) | MCP is the #1 hiring differentiator in 2026 |
| Agent tool call accuracy eval (Ragas) | Proves agent evaluation maturity |
| Human-in-the-loop checkpointing | Shows production agent design |
| Langfuse tracing dashboard | Proves observability skills |
| Live deployed URL + video demo | Non-negotiable for remote global roles |

---

## 🏆 Bonus: Open Source Contribution (Months 7-9)
**This is the highest-signal item for global hiring.**

Submit and merge a PR to one of:
- LangChain / LangGraph
- LlamaIndex
- DSPy
- FastMCP
- vLLM

Merged PR in a major AI repo = instantly top 1% of global applicants.

---

## 📊 Global Hiring Portfolio Requirements

| Requirement | Domestic (Oct 1) | Global (Dec 2027) |
|-------------|-----------------|-------------------|
| GitHub repos | 2 projects | 2 projects + open-source PR |
| Live URLs | Not required | ✅ Mandatory |
| Ragas eval scores | Nice to have | ✅ Required in README |
| Architecture diagrams | Nice to have | ✅ Required in README |
| LLM observability | Not required | ✅ Required |
| MCP servers | 1 basic | ✅ 2-3 custom |
| Video demo | Not required | ✅ Recommended |
| Technical blog posts | Not required | ✅ 2-3 articles |
| TypeScript/Next.js UI | Not required | ✅ Recommended |
| Unit tests | Nice to have | ✅ Required |
| Docker + docker-compose | ✅ Required | ✅ Required |
| Deployed on cloud | ✅ Recommended | ✅ Required (AWS) |

---

## Deployment Strategy

| Aspect | Project 1 | Project 2 |
|--------|-----------|-----------|
| **GitHub** | Detailed README + architecture diagram | Detailed README + architecture diagram |
| **Live Demo** | Deployed on AWS EC2 (public URL) | Deployed on AWS EC2 (video demo) |
| **Documentation** | API docs (Swagger) + Ragas scores | MCP architecture + eval scores |
| **Code Quality** | Type hints, tests, clean structure | Type hints, tests, clean structure |
| **Observability** | Langfuse/Helicone tracing | Langfuse tracing for agent calls |
