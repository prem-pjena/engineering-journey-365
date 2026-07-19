# CV — Month 2 (Day 60): ₹10-12 LPA / $24-40k/yr Global Remote Level

---

**PREM PRAKASH JENA**
Bengaluru, India | prem.pjena@email.com | +91-XXXXX-XXXXX
[GitHub: prem-pjena](https://github.com/prem-pjena) | [LinkedIn: premprakashj](https://linkedin.com/in/premprakashj)

---

## PROFESSIONAL SUMMARY

Agentic AI Engineer with deep expertise in LangGraph orchestration, Model Context Protocol (MCP), and production RAG systems. Combines 6 months of DevOps experience (Docker, AWS) with specialization in multi-agent architectures, programmatic LLM evaluation, constrained decoding, and cost-optimized inference deployment. Built and deployed two production-grade AI systems — a multi-tenant RAG assistant and an MCP-connected multi-agent orchestrator with full CI/CD. Seeking AI Engineer role where I can design and ship agentic systems at scale. Open to global remote opportunities.

---

## SKILLS

**Core AI/ML:**
LangGraph (StateGraph, reducers, conditional routing, HITL, multi-agent supervisor, parallel execution), MCP (stdio and HTTP SSE transports, Tools/Resources/Prompts, JSON-RPC 2.0), LangChain (LCEL, chains, templates, loaders, splitters, structured output), RAG (naive → corrective → adaptive → conversational → agentic), Prompt Engineering (few-shot, CoT, system, DSPy)

**LLM & APIs:**
OpenAI API (GPT-4o, embeddings, structured outputs), Gemini API, Constrained Decoding (Outlines/XGrammar for guaranteed JSON), Function/Tool Calling, Streaming SSE, Token Management

**Evaluation & Observability:**
Ragas (Faithfulness, Context Precision/Recall, Answer Relevancy), LangSmith Tracing, Golden Dataset Construction, CI/CD Eval Pipelines

**Vector & Search:**
pgvector (HNSW/IVFFlat indexing, ef_search/m tuning, row-level security), ChromaDB, Hybrid Search (BM25 + dense), Cross-encoder Reranking (BGE), Parent-Child Chunking, Semantic Chunking, Redis Semantic Caching

**Backend & Infrastructure:**
FastAPI (async, middleware, background tasks, streaming), Pydantic, Python (OOP, Async/Await, Generators, Context Managers), Docker, docker-compose, AWS (ECS Fargate, Bedrock, RDS pgvector, ElastiCache, CloudWatch, API Gateway, S3), GitHub Actions CI/CD

**Interview Knowledge:**
Transformer Architecture (QKV, self-attention, RoPE, KV cache), ML Concepts (bias-variance, precision/recall/F1, cross-validation), NLP (BPE/WordPiece tokenization, BERT vs GPT), System Design for AI (RAG at scale, multi-tenant isolation, latency/cost/accuracy trilemma, LLM gateway), Inference Optimization (vLLM, PagedAttention, continuous batching, quantization INT8/INT4)

---

## PROJECTS

### 1. Multi-Tenant Enterprise RAG System
*Technologies: FastAPI, LangChain, LangGraph, pgvector, MCP, Cross-encoder (BGE), Docker, AWS ECS, Ragas, LangSmith*

- Built production RAG pipeline with parent-child semantic chunking and hybrid search (BM25 + dense vector) for precise retrieval across 10k+ documents
- Implemented LangGraph supervisor agent with conditional routing: internal pgvector → MCP web search → conversation memory, with Corrective RAG fallback when retrieval confidence is low
- Added constrained decoding via Pydantic schemas for guaranteed JSON-structured extraction outputs
- Integrated Ragas CI pipeline evaluating Faithfulness (≥ 0.9), Context Precision (≥ 0.85), and Answer Relevancy, blocking merges on regression
- Applied pgvector row-level security for multi-tenant data isolation with HNSW index tuning (m=16, ef_search=200)
- Containerized with Docker, deployed on AWS ECS Fargate with CloudWatch monitoring and automated CI/CD via GitHub Actions
- [Live Demo](url) | [GitHub](url)

### 2. Multi-Agent MCP Orchestrator
*Technologies: LangGraph, MCP, FastAPI, Next.js, TypeScript, Docker, AWS ECS, GitHub Actions, Redis*

- Architected multi-agent LangGraph system with Supervisor pattern: Planner decomposes tasks → routes to specialized Workers (Research, Analysis, Review) via conditional edges
- Created custom MCP Server (Streamable HTTP transport) exposing PostgreSQL database as Resource and external APIs as Tools, enabling secure enterprise integration
- Built Next.js chat UI with Server-Sent Events streaming, TypeScript type safety, and real-time agent reasoning visualization
- Implemented cost-tracking middleware extracting token usage per step, calculating USD/session for billing analytics
- Added Redis semantic caching: embed incoming queries, cosine similarity check, serve cached responses in <10ms for repeat queries
- Deployed full stack (Agent + pgvector + MCP Server + Next.js UI) via docker-compose on AWS ECS Fargate with CloudWatch dashboards

---

## EXPERIENCE

### AI Engineering Intern — SkillVeda (May 2026 – Jul 2026)
*3 months* | *Remote*

- Built exponential backoff retry logic for external PDL API calls, improving reliability under rate limits
- Optimized background worker interval 1min→5min, reducing database load by 80%
- Added database partial indexes, reducing full table scans on 100k+ row queries
- Implemented async scoring pipeline with frontend polling, eliminating 30-60 second UI freezes
- Designed score caching system, reducing redundant Gemini AI API calls
- Built LinkedIn OAuth signup flow and candidate profile CRUD (full-stack, TypeScript + React + PostgreSQL)

### Jr. DevOps Engineer — [Company Name] (May 2025 – Oct 2025)
*6 months* | *Remote*

- Containerized backend services using Docker, ensuring consistent dev/prod environment parity
- Configured CI/CD pipelines automating testing and deployment, reducing manual deployment friction
- Managed Linux-based infrastructure with production monitoring and release management
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
