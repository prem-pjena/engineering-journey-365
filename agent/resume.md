# Prem Prakash Jena

**Location:** India | **Email:** [your-email] | **LinkedIn:** [premprakashj](https://www.linkedin.com/in/premprakashj/) | **GitHub:** [prem-pjena](https://github.com/prem-pjena)

---

## Summary

Agentic AI Engineer with expertise in LangGraph orchestration, Model Context Protocol (MCP), and production RAG systems. Combines 6 months of DevOps infrastructure experience (Docker, AWS, CI/CD) with deep specialization in multi-agent architectures, programmatic LLM evaluation, and cost-optimized inference deployment. Previously transitioned from infrastructure to applied AI, bringing a unique blend of production deployment expertise and modern LLM orchestration skills. Built and deployed two production-grade AI systems — a multi-tenant RAG assistant and an MCP-connected multi-agent orchestrator with full CI/CD.

**Note for interviews:** The one-year post-graduation gap (2024-2025) was spent on "Independent Technical Upskilling" — intentionally building Linux, Docker, and AWS foundations before entering the industry.

---

## Skills

| Category | Skills |
|----------|--------|
| **Languages** | Python, TypeScript, JavaScript, SQL |
| **AI/ML** | LangChain, LangGraph (StateGraph, routing, HITL, multi-agent), MCP (stdio/HTTP SSE, Tools/Resources/Prompts), RAG (naive→corrective→adaptive→agentic), Prompt Engineering, LLM APIs (OpenAI, Gemini), Constrained Decoding, Ragas, LangSmith |
| **Backend** | FastAPI, Pydantic, Asynchronous Python, REST APIs, Express.js |
| **Vector & Search** | pgvector (HNSW/IVFFlat, hybrid search), ChromaDB, Cross-encoder Reranking, Semantic/Parent-Child Chunking |
| **Cloud (AWS)** | Bedrock, ECS Fargate, RDS pgvector, ElastiCache, S3, Lambda, API Gateway, CloudWatch |
| **DevOps** | Docker, docker-compose, Git, GitHub Actions CI/CD |
| **Database** | PostgreSQL, SQL (JOINs, CTEs, window functions, indexing), database design, pgvector |
| **Concepts** | Transformer Architecture (QKV, RoPE, KV cache), Tokenization (BPE), Sampling (temp, top-k, top-p), Quantization, ML basics, OAuth 2.0, RLS |

---

## Experience

### AI Engineering Intern — SkillVeda
*May 2026 – Jul 2026*

- Built exponential backoff retry logic for external PDL API calls, improving reliability under rate limits
- Optimized background worker interval from 1min → 5min, reducing database load by 80%
- Added database partial indexes, reducing full table scans on 100k+ row queries
- Implemented async scoring pipeline with frontend polling, eliminating 30-60 second UI freezes
- Designed and built score caching system, reducing redundant Gemini AI API calls
- Built LinkedIn OAuth signup flow and candidate profile CRUD (full-stack, TypeScript + React + PostgreSQL)

### Jr. DevOps Engineer → DevOps Intern — [Company Name]
*May 2025 – Oct 2025*

- Containerized backend services using Docker, ensuring consistent parity between local dev and production environments
- Configured CI/CD pipelines to automate testing and deployment workflows, significantly reducing manual deployment friction
- Managed Linux-based infrastructure, gaining hands-on exposure to production environments, monitoring, and release management

---

## Projects

### Multi-Tenant Enterprise RAG System
*FastAPI, LangGraph, pgvector, MCP, Cross-encoder, Docker, AWS ECS, Ragas*

- Built production RAG pipeline with parent-child semantic chunking, hybrid search (BM25 + dense), and cross-encoder reranking
- Implemented LangGraph supervisor agent with conditional routing: internal pgvector → MCP web search → conversation memory, with Corrective RAG fallback
- Applied constrained decoding via Pydantic schemas for guaranteed JSON-structured outputs
- Integrated Ragas CI pipeline (Faithfulness ≥ 0.9, Context Precision ≥ 0.85) blocking merges on regression
- Containerized with Docker, deployed on AWS ECS Fargate with GitHub Actions CI/CD
- [GitHub](https://github.com/prem-pjena/rag-system)

### Multi-Agent MCP Orchestrator
*LangGraph, MCP, FastAPI, Next.js, TypeScript, Docker, AWS ECS, Redis*

- Architected multi-agent system with Supervisor pattern: Planner decomposes → Workers execute → Reviewer validates
- Created custom MCP Server (Streamable HTTP) exposing database as Resource and APIs as Tools
- Built Next.js chat UI with SSE streaming and real-time agent reasoning visualization
- Implemented Redis semantic caching: embed queries → cosine similarity → cached response in <10ms
- Deployed full stack via docker-compose on AWS ECS Fargate with CloudWatch dashboards

*In progress — 2 portfolio projects building toward Jan 2027 job target:*
1. **AI-powered API Backend** — FastAPI + PostgreSQL + OpenAI + Docker + AWS
2. **Multi-Agent Workflow Tool** — LangGraph + LangSmith + LLM Agents + PostgreSQL

---

## Education

**B.Tech Computer Science & Engineering** — 2024

---

## Currently Learning (Month 1-2)

- Python fundamentals + DSA (15-20 min daily)
- Problem-solving and algorithmic thinking
- System design fundamentals (passive exposure)
- Building consistent GitHub presence
