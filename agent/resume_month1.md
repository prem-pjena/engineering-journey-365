# CV — Month 1 (Day 31): ₹30k-₹50k Internship Level (Market-Validated)

---

**PREM PRAKASH JENA**
Bengaluru, India | prem.pjena@email.com | +91-XXXXX-XXXXX
[GitHub: prem-pjena](https://github.com/prem-pjena) | [LinkedIn: premprakashj](https://linkedin.com/in/premprakashj)

---

## PROFESSIONAL SUMMARY

AI Engineer with 6 months of DevOps infrastructure experience (Docker, AWS, CI/CD) transitioning into Agentic AI. Built and deployed a production-grade multi-tenant RAG system with LangGraph orchestration, pgvector hybrid search, cross-encoder reranking, and automated Ragas evaluation. Seeking AI Engineer internship where I can apply agentic orchestration, LLM APIs, and vector database skills.

---

## SKILLS

**Languages:** Python, SQL
**AI/ML:** LangChain, LangGraph (StateGraph, routing), Prompt Engineering, LLM APIs (OpenAI, Gemini), RAG (naive → agentic), MCP basics
**Vector & Search:** pgvector (HNSW indexing), ChromaDB, Hybrid Search (BM25 + Dense), Cross-encoder Reranking, Semantic Chunking, Parent-Child Chunking
**Backend:** FastAPI, Pydantic, REST APIs, Asynchronous Python
**Evaluation:** Ragas (Faithfulness, Context Precision, Answer Relevancy), LangSmith
**DevOps:** Docker, docker-compose, AWS ECS/EC2, GitHub Actions CI/CD
**Data:** SQL (SELECT, JOINs, aggregations, indexing), Pandas, NumPy
**Tools:** uv, Git, pyproject.toml
**Concepts:** OOP, Async/Await, Context Managers, Transformers (QKV), Tokenization (BPE), Sampling (temp, top-k, top-p)

---

## PROJECT

### Multi-Tenant RAG System with LangGraph Orchestration
*Technologies: Python, FastAPI, LangChain, LangGraph, pgvector, ChromaDB, MCP, OpenAI API, Cross-encoder, Docker, AWS ECS, Ragas, LangSmith*

- Built production-grade RAG pipeline with parent-child semantic chunking, hybrid search (BM25 + dense vector), and cross-encoder reranking (BGE) — dropping top-20 results to top-3 relevant
- Implemented LangGraph supervisor agent that dynamically routes queries: internal pgvector for proprietary docs, MCP-integrated web search tool, or conversation memory
- Added structured output extraction using Pydantic schemas with constrained decoding concepts for guaranteed JSON compliance
- Integrated automated Ragas evaluation pipeline (Faithfulness ≥ 0.9, Context Precision ≥ 0.85) in CI/CD, blocking deployments on regression
- Applied row-level security in pgvector for multi-tenant data isolation
- Containerized with Docker, deployed on AWS ECS Fargate with CloudWatch monitoring and GitHub Actions CI/CD
- [Live Demo](http://ec2-xx-xx-xx-xx.ap-south-1.compute.amazonaws.com) | [GitHub Repository](https://github.com/prem-pjena/rag-system)

---

## EXPERIENCE

### AI Engineering Intern — SkillVeda (May 2026 – Jul 2026)
*3 months* | *Remote*

- Developed backend features for interview process automation agents using Python and TypeScript
- Built exponential backoff retry logic for external API calls, improving reliability under rate limits
- Optimized background worker interval 1min→5min, reducing database load by 80%
- Implemented async scoring pipeline with frontend polling, eliminating 30-60 second UI freezes
- Designed score caching system, reducing redundant Gemini AI API calls

### Jr. DevOps Engineer — [Company Name] (May 2025 – Oct 2025)
*6 months* | *Remote*

- Containerized backend services using Docker for dev/prod parity
- Configured CI/CD pipelines automating testing and deployment
- Managed Linux-based infrastructure, production monitoring, and release management

*Note: Role was backend-focused; transitioned to pursue Agentic AI specialization.*

---

### Jr. DevOps Engineer — [Company] (May 2025 – Oct 2025)
*6 months*

- Containerized backend services using Docker, ensuring parity between development and production environments
- Configured CI/CD pipelines (GitHub Actions) for automated testing and deployment
- Managed Linux-based infrastructure for production systems

---

## EDUCATION

**B.Tech in Computer Science Engineering** — Lovely Professional University (2020–2024)

---

## CERTIFICATIONS & COURSEWORK

- LangChain for LLM Application Development (DeepLearning.AI)
- Building Systems with ChatGPT API (DeepLearning.AI)
- AWS Cloud Practitioner Essentials

---

## KEY ACHIEVEMENTS

- Built and deployed a production RAG system with automated evaluation metrics
- Solved 30+ DSA problems (Two Pointers, Sliding Window, Binary Search, BFS/DFS)
- 6 months hands-on DevOps experience with Docker, AWS, and CI/CD
