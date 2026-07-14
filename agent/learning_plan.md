# 📚 12-Month AI Engineer / SDE AI Roadmap

**Target Role:** AI Engineer | SDE AI | Agentic AI Engineer
**Core Stack:** LLMs, Agents, LangChain, LangGraph, LangSmith, Prompting, RAG, MCP
**NOT Targeting:** AI Backend Engineer, ML Engineer (math), Data Scientist

---

## 🎯 Target Roles & Salary

| Role | 6-month target | 12-month target |
|------|---------------|----------------|
| AI Engineer (GenAI/LLM focus) | ₹40-60k/mo | ₹80k-1.2L/mo |
| Agentic AI Engineer | ₹50-70k/mo | ₹1-1.5L/mo |
| SDE AI (AI features) | ₹50-70k/mo | ₹1-1.5L/mo |

---

## 🧠 Core Tech Stack

| Domain | Tech | Depth |
|--------|------|-------|
| **LLMs & APIs** | OpenAI, Anthropic, Gemini, open-source models (Ollama) | Deep |
| **Orchestration** | LangChain, LangGraph, LangSmith | Deep — core skill |
| **Agents** | ReAct, multi-agent, tool calling, state machines | Deep — core skill |
| **RAG** | Vector DBs, chunking, hybrid search, reranking | Deep |
| **MCP** | Model Context Protocol, FastMCP servers | Deep |
| **Prompting** | Few-shot, chain-of-thought, structured outputs | Deep |
| **Model Serving** | FastAPI (minimal), Docker (basic), cloud deploy | Practical |
| **DSA** | 60-80 problems (arrays, strings, hash maps, trees, graphs) | Interview-ready |
| **NLP Concepts** | Tokenization, embeddings, BERT vs GPT, transformers | Conceptual |
| **ML Concepts** | Basic algorithms conceptually, evaluation metrics | Conceptual |

---

## 🚫 What We SKIP

| Topic | Reason |
|-------|--------|
| **Backend engineering** (deep FastAPI, PostgreSQL optimization, API scaling) | Not your role. AI Engineer uses APIs, doesn't build backend infra. |
| **Hardcore ML math** (backpropagation derivations, calculus, linear algebra) | Not needed for AI Engineer using pre-trained models. |
| **DevOps deep dive** (Kubernetes, CI/CD pipelines, infra monitoring) | Basic Docker + deploy is enough. |
| **Data Science** (statistics, hypothesis testing, A/B testing deep) | Not your target. |
| **Computer Vision** | Not relevant to LLM/agent focus. |

---

## 📅 4-Phase Roadmap

### Phase 1 (Months 1-2): AI FOUNDATION

**Goal:** Get first AI Engineer role. ₹30-40k/mo.
**Core focus:** LangChain, RAG, basic agents, prompting

**Week 1-2:** Python review → LangChain basics (LCEL, chains, prompt templates) → LLM APIs (OpenAI, Gemini) → embeddings → vector DBs → basic RAG
**Week 3-4:** LangGraph basics (StateGraph, nodes, edges) → ReAct pattern → tool calling → Ragas evaluation → MCP basics
**Week 5-6:** **Project 1: RAG Agent** — Build + deploy. Apply for roles.
**Week 7-8:** Interview prep + applications

**By end of Month 2:** Can build RAG agents, use LangChain/LangGraph, deploy basic apps. ₹30-40k/mo role.

### Phase 2 (Months 3-5): AGENT MASTERY

**Goal:** Master agentic AI. ₹50-70k/mo.
**Core focus:** LangGraph advanced, multi-agent, MCP, LangSmith

**LangGraph deep:** State persistence, checkpointing, human-in-the-loop, conditional routing, complex state graphs
**Multi-agent:** Planner → Executor → Synthesizer patterns, agent communication, task decomposition
**MCP advanced:** Custom MCP servers (DB, API, file system tools), MCP security, discovery
**LangSmith:** Tracing, evaluation, debugging agent workflows
**NLP concepts:** Tokenization, BERT vs GPT, embeddings, transformers architecture (conceptual)

**By end of Month 5:** Can build production multi-agent systems, MCP servers. ₹50-70k/mo role.

### Phase 3 (Months 6-9): DEEPEN + BROADEN

**Goal:** Be strong for ₹80k-1L/mo roles.
**Core focus:** Advanced RAG, open-source models, evaluation, system design

**Advanced RAG:** Hybrid search, cross-encoder reranking, query transformation, multi-hop RAG
**Open-source models:** Ollama, vLLM basics, model quantization, local deployment
**Evaluation:** Ragas advanced, LLM-as-a-judge, regression testing, prompt versioning
**DSA:** 60-80 problems (add graphs, DP basics)
**System design (AI-specific):** RAG at scale, agent architecture, LLM gateway, caching strategies

### Phase 4 (Months 10-12): EXPERT LEVEL

**Goal:** ₹1-1.5L/mo. Senior AI Engineer.
**Core focus:** Production agents, fine-tuning concepts, cost optimization, mentoring

**Production agents:** Error recovery, audit trails, multi-modal agents, long-running workflows
**Fine-tuning concepts:** LoRA, QLoRA, when to fine-tune vs RAG vs prompting (conceptual, not implementation)
**Cost optimization:** Semantic caching, model routing, prompt compression, token budgeting
**Open source:** 3-5 merged PRs in LangChain, LangGraph, FastMCP, or Ragas

---

## 🏗️ The 2 Portfolio Projects

### Project 1 (Month 1-2): RAG Agent
- LangChain + LangGraph + OpenAI + ChromaDB/pgvector
- Agent that retrieves documents and answers with citations
- ReAct pattern with tool calling
- Ragas evaluation scores in README
- Basic Docker deployment

### Project 2 (Month 3-5): Multi-Agent MCP System
- LangGraph multi-agent (Planner → Searcher → Synthesizer)
- Custom MCP server exposing DB + API tools
- LangSmith tracing and evaluation
- Human-in-the-loop guardrails
- Dockerized + deployed

---

## 📚 Interview Prep (Conceptual Only — No Math)

### LLM & RAG (know these)
- Transformer architecture concept (Q, K, V, self-attention — no math)
- Tokenization, context windows, token limits
- RAG evaluation: faithfulness, precision, recall
- Chunking strategies, embedding models
- When to use RAG vs fine-tuning vs prompting

### Agents (know these)
- ReAct pattern (Reason + Act)
- LangGraph StateGraph concept (nodes, edges, state)
- Tool calling, function calling
- Multi-agent orchestration patterns
- Memory types (short-term, episodic, semantic)
- Infinite loop prevention

### MCP (know these)
- Host vs Client vs Server architecture
- Tools vs Resources vs Prompts
- Why MCP over custom API integrations

### NLP Concepts (conceptual)
- BERT (encoder-only) vs GPT (decoder-only)
- Embeddings: what they represent
- Tokenization methods (BPE, WordPiece)

---

## 📊 Weekly Progress Tracker

| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | LangChain basics, LLM APIs, embeddings | Chat script with memory |
| 2 | RAG pipeline, vector DBs, basic agents | RAG query system |
| 3 | LangGraph, ReAct, tool calling | Agent with tools |
| 4 | Ragas eval, MCP basics | Project 1 starts |
| 5-6 | **Project 1** + applications | Deployed RAG Agent |
| 7-8 | Interview prep + apply | ₹30-40k/mo role |

---

*Target: AI Engineer working with agents, models, LLMs. No backend. No math ML.*
