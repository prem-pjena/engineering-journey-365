# CV — Month 2 (Day 60): ₹60-80k/mo FT Level

---

**PREM PRAKASH JENA**
Bengaluru, India | prem.pjena@email.com | +91-XXXXX-XXXXX
[GitHub: prem-pjena](https://github.com/prem-pjena) | [LinkedIn: premprakashj](https://linkedin.com/in/premprakashj)

---

## PROFESSIONAL SUMMARY

Agentic AI Engineer with expertise in LangGraph orchestration, Model Context Protocol (MCP), and production RAG systems. Combines 6 months of DevOps experience (Docker, AWS) with deep specialization in multi-agent architectures, automated evaluation, and cost-optimized LLM deployment. Built and deployed two production-grade AI systems — a RAG knowledge assistant and an MCP-connected multi-agent orchestrator. Seeking AI Engineer role where I can design and ship agentic systems at scale.

---

## SKILLS

**Core AI/ML:**
LangChain, LangGraph (StateGraph, reducers, conditional routing, human-in-the-loop, multi-agent), MCP (stdio and HTTP SSE transports, Tools/Resources/Prompts), RAG (naive, hybrid, agentic), Prompt Engineering (few-shot, CoT), Ragas Evaluation (faithfulness, context precision/recall, LLM-as-a-judge), LangSmith Tracing

**LLM & APIs:**
OpenAI API (GPT-4o, embeddings), Gemini API, Structured Outputs (with_structured_output, Pydantic), Function/Tool Calling, Streaming SSE, Token Management

**Programming:**
Python (OOP, Async/Await, Generators, Context Managers, Type Hints), SQL (JOINs, aggregations, indexing)

**Infrastructure:**
Docker, docker-compose, AWS EC2, GitHub Actions CI/CD, OpenTelemetry

**Vector & Data:**
pgvector (HNSW/IVFFlat indexing), ChromaDB, Cosine Similarity, Hybrid Search (BM25 + dense), Cross-encoder Reranking (BGE)

**Interview Knowledge:**
Transformer Architecture (Q, K, V, Self-Attention), ML Concepts (bias-variance, precision/recall/F1, cross-validation), NLP (BPE/WordPiece tokenization, BERT vs GPT), System Design for AI (RAG at scale, multi-tenant isolation, latency optimization, LLM gateway)

---

## PROJECTS

### 1. Enterprise Orchestrator — MCP-Connected Multi-Agent System
*Technologies: LangGraph, MCP, FastAPI, pgvector, Docker, AWS EC2, Ragas, OpenTelemetry*

- Built a multi-agent LangGraph system using Supervisor pattern: Planner agent decomposes tasks → routes to specialized Worker agents (Researcher, Writer) via conditional edges
- Implemented dual-channel memory architecture — persistent conversation history + ephemeral reasoning scratchpad — preventing O(n²) token leaks during reflection loops
- Created custom MCP Server (Streamable HTTP transport) exposing SQLite database as Resource and external API as Tool, enabling secure enterprise tool integration
- Integrated Ragas CI pipeline: automated Faithfulness and Context Precision evaluation on every deployment, blocking merges if scores drop below threshold
- Added cost-tracking middleware: extracts token usage from API responses, calculates USD cost per session, emits structured logs for billing analytics
- Instrumented with OpenTelemetry + LangSmith for full agent chain-of-thought tracing and latency monitoring
- Deployed with docker-compose (Agent + VectorDB + MCP Server) on AWS EC2
- [Live Demo](http://ec2-xx-xx-xx-xx.ap-south-1.compute.amazonaws.com) | [GitHub Repository](https://github.com/prem-pjena/agent-orchestrator)

### 2. Enterprise RAG System with Automated Evaluation
*Technologies: LangChain, pgvector, OpenAI, Docker, AWS EC2, Ragas*

- Built production RAG pipeline: PDF ingestion → semantic chunking → embedding → hybrid search (BM25 + dense) → cross-encoder reranking → LLM generation with citations
- Achieved Faithfulness score of 0.92 and Context Precision of 0.88 via Ragas evaluation framework
- Containerized with Docker, deployed on AWS EC2 with GitHub Actions CI/CD
- [GitHub Repository](https://github.com/prem-pjena/rag-system)

---

## EXPERIENCE

### AI Engineering Intern — SkillVeda (May 2026 – Jul 2026)
*3 months* | *Remote*

- Developed backend features for interview process automation agents using Python
- Gained practical exposure to production AI systems and feature development

*Transitioned to focus on Agentic AI specialization — the role's backend focus was misaligned with my career trajectory in AI orchestration.*

---

### Jr. DevOps Engineer — [Company] (May 2025 – Oct 2025)
*6 months*

- Containerized services using Docker, ensuring parity across dev/production environments
- Configured CI/CD pipelines (GitHub Actions) for automated testing and deployments
- Managed Linux-based infrastructure, monitoring, and release management

---

## EDUCATION

**B.Tech in Computer Science Engineering** — Lovely Professional University (2020–2024)

---

## OPEN SOURCE CONTRIBUTIONS

- [LangChain](https://github.com/langchain-ai/langchain) — Documentation improvements and bug fix for document loader edge case
- [FastMCP](https://github.com/fastmcp/fastmcp) — Example MCP server implementation for SQLite database access
- [Ragas](https://github.com/explodinggradients/ragas) — Test case contributions for faithfulness evaluation metric

---

## KEY ACHIEVEMENTS

- Built two production-grade AI systems: RAG assistant + MCP-connected multi-agent orchestrator
- Achieved Faithfulness 0.92, Context Precision 0.88 on RAG evaluation
- Solved 50+ DSA problems (Arrays, Strings, Hash Maps, Two Pointers, Sliding Window, Trees, Graphs, DP basics)
- 3 merged open-source PRs in LangChain, FastMCP, and Ragas repositories
- 6 months production DevOps experience (Docker, AWS, CI/CD)
