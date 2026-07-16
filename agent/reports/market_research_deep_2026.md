# 📊 Deep Market Research — Agentic AI Engineer (India + Global Remote) 2025-2026

**Source:** Gemini Deep Research (Jul 17, 2026)
**Researched For:** Prem — Agentic AI Engineer, ₹10-12 LPA target

---

## 🎯 Updated Target Validations

| Target | Research Says | Verdict |
|--------|---------------|---------|
| ₹30k-50k/mo internship | ✅ Confirmed — multiple companies pay this range | ✅ ON TRACK |
| ₹10-12 LPA FT (₹80k-₹1L/mo) | ✅ Confirmed as baseline for proven agentic skills | ✅ ON TRACK |
| US/global remote ($24k-$40k/yr) | ✅ Realistic — YC startups actively hire India remote | ✅ ADDED TARGET |
| Skip service-based companies | ✅ Confirmed — TCS/Infosys max out at ₹7-9 LPA | ✅ CONFIRMED |

---

## 🏢 EXACT Company Mapping

### Indian AI-First Startups (₹30k-50k Intern / ₹10-12 LPA FT)

| Company | Role | Type | Stipend/Salary | Tech Stack | Location | Evidence |
|---------|------|------|----------------|------------|----------|----------|
| **Aight (Ashva Intelligence)** | Backend Engineering Intern | Intern → FT | ₹25k-₹50k/mo | Python, FastAPI, LiteLLM, PostgreSQL, Redis | Gurgaon | Wellfound: "Stipend ₹25,000–50,000/month... Strong performers get FT offer" |
| **Fluexy** | Full-Stack AI Engineering Intern | Intern | ₹15k-₹20k/mo + 1-3% ESOP | Python, Next.js, LangChain, LangGraph, AWS/GCP | Remote | Wellfound: "₹15,000 – ₹20,000 • 1.0% – 3.0% ESOP... 2025/26 batch passouts only" |
| **Gravity AI** | AI Intern | Intern | ₹15k-₹20k/mo (₹1.8L-2.4L/yr) | Python, LangChain, RAG, MLOps, CI/CD, Agentic Workflow | Remote | Wellfound: "₹1.8L – ₹2.4L • No equity... Remote (India)" |
| **SuperKalam** | AI/ML Research Intern | Intern | ₹25k-₹40k/mo | Python, Node.js, RAG, Agentic Workflows, STT/TTS | Remote/Bengaluru | YC Jobs: "Stipend: INR 25 - 40k per month... Remote / Bengaluru" |
| **RIOM Ventures** | AI Engineering Intern | Intern | ₹10k-₹25k/mo (₹1.2L-3L/yr) | Python, LLM APIs, LangChain, Vector DBs, Flutter | Remote | Wellfound: "₹1.2L – ₹3L • No equity... Remote (Everywhere)" |
| **Hungama Digital** | AI & GenAI Engineer Intern | Intern → FT | ₹50k/mo (FT PPO: ₹12-15 LPA) | Python, PyTorch, Scikit-learn, GenAI Pipelines | Remote | TechGig: "Stipend: ₹50,000/month... PPOs ₹12–15 LPA" |
| **Teal India (Tealbox)** | AI/ML Engineer Intern | Intern → FT | ₹30k/mo | Python, Elasticsearch, NLP, vLLMs, Vector Search | Bengaluru | thejobcompany: "30,000/Month [Stipend]... Internship + FTE" |

### Global Remote / US-EU Startups Hiring from India ($24k-$40k/yr)

| Company | Role | Type | Salary | Tech Stack | Location | Evidence |
|---------|------|------|--------|------------|----------|----------|
| **Peakflo (YC)** | ML Engineer Intern | Intern → FT | ₹40k-₹50k/mo ($5.7k-$7.2k/yr) | Python, LLM Fine-tuning, RAG, Agentic Architecture | Singapore/Remote | YC Jobs: "₹480K - ₹600K INR... Performance based full-time role conversion" |
| **Lamatic.ai** | Applied AI Engineer Intern | Intern | $6k-$10k total | JavaScript, GenAI, GraphQL, AI Workflows | Miami/Remote | Wellfound: "$6k – $10k • No equity... Remote (India)" |
| **Great Question (YC)** | AI Engineer Intern | Intern | Competitive hourly | AI Agents, MCP Tool Structuring, Evals, Semantic Search | SF/Remote PST | YC Jobs: "Duration: 3 months... Compensation: Competitive hourly rate" |
| **Smart Audit** | AI Engineer | FT | $25k-$50k/yr | GenAI, LLMs, Automation, Python | Remote/Bengaluru | Wellfound: "$25k – $50k... Remote • Bengaluru" |

---

## 🔧 Tech Stack Requirements — Exact JD Keywords

### Backend & API Layer
| Technology | Demand | Why |
|-----------|--------|-----|
| **FastAPI** | 🟢 Dominant | Async native → handles streaming LLM responses. Django/Flask rarely mentioned |
| **Pydantic** | 🟢 Critical | Structured outputs, data validation for LLM JSON responses |
| **Asynchronous Python** | 🟢 Must-have | asyncio, async/await for concurrent API calls |

### AI/LLM Orchestration
| Technology | Demand | Why |
|-----------|--------|-----|
| **LangChain** | 🟢 Foundational | Base abstraction layer, but alone is NOT enough |
| **LangGraph** | 🟢 Must-have | Stateful, cyclic orchestration for agents. Basic chains considered obsolete |
| **MCP (Model Context Protocol)** | 🟢 Emerging critical | "MCP tool structuring" explicitly demanded by companies like Great Question |
| **CrewAI** | 🟡 Alternative | Multi-agent framework, less common than LangGraph |
| **LlamaIndex** | 🟡 Nice-to-have | Some JDs mention it alongside LangChain |

### Vector Databases & Retrieval
| Technology | Demand | Why |
|-----------|--------|-----|
| **pgvector** | 🟢 Enterprise standard | Co-locate relational data + vectors in single PostgreSQL. Simplifies deployment |
| **Pinecone** | 🟡 Popular for prototyping | Managed, but adds network latency + compliance overhead |
| **ChromaDB** | 🟡 Hackathon favorite | Lightweight, local. Rarely in production JDs |
| **Hybrid Search (BM25 + Vector)** | 🟢 Must-have | Sparse + dense retrieval for exact keyword matches + semantic meaning |

### Evaluation & MLOps
| Technology | Demand | Why |
|-----------|--------|-----|
| **LangSmith** | 🟢 Critical hiring filter | "Vibes-based testing is a terminal red flag" — hiring managers |
| **Ragas** | 🟢 Important | Faithfulness, answer relevance, context precision metrics |
| **Langfuse** | 🟡 Alternative | Open-source observability |
| **CI/CD for Prompts** | 🟢 Differentiator | Automated eval pipelines in GitHub Actions |

### Cloud & Deployment
| Technology | Demand | Why |
|-----------|--------|-----|
| **AWS (ECS, EC2)** | 🟢 Dominant | Containerized FastAPI + Docker + ECS = standard deploy pattern |
| **Docker** | 🟢 Must-have | Containerization for reproducible deployments |
| **GitHub Actions** | 🟢 Expected | CI/CD pipeline automation |
| **GCP** | 🟡 Acceptable | Some startups use GCP, but AWS is more common |

### Full-Stack Bonus
| Technology | Demand | Why |
|-----------|--------|-----|
| **Next.js + TypeScript** | 🟢 High ROI | "Full Stack AI Engineer" roles pay premium. End-to-end feature delivery |
| **React** | 🟡 Acceptable | Next.js preferred over plain React |

---

## 🏗️ Projects That Signal Seniority

### Project 1: Multi-Tenant Enterprise RAG System
**What to build:**
- Row-level security in PostgreSQL (pgvector) for data isolation
- LangGraph supervisor agent that routes queries:
  - Internal vector DB for proprietary docs
  - MCP-integrated web search tool
  - Conversational summary from history
- **Advanced retrieval techniques (differentiators):**
  - Document Hierarchies: small chunks for search, parent chunks for LLM context
  - Query Routing: cheap local model (Llama 3 8B) routes → expensive frontier model (GPT-4o)
- **Must document in README:**
  - Time to First Token (TTFT)
  - End-to-end inference latency
  - Cost per query

### Project 2: Asynchronous Multi-Agent Workflow
**What to build:**
- CrewAI or LangGraph multi-agent network:
  - Research Agent → data aggregation
  - Analysis Agent → synthesis
  - Review Agent → critique against rubrics
- Apply to high-value domain: financial analysis, market intelligence, code review
- **Critical differentiator:**
  - Error handling when APIs rate-limit
  - Fallback when LLM outputs malformed JSON
  - Pydantic-enforced structured outputs
- Containerized with Docker, deployed to live cloud with authenticated API endpoint

---

## 📝 Resume Optimization

### Keywords That Pass ATS
| Instead of | Use |
|-----------|-----|
| Python | Asynchronous Python, FastAPI, Pydantic |
| Machine Learning | LLM Orchestration, LangGraph, RAG |
| Databases | PostgreSQL, pgvector, Vector Similarity Search |
| Testing | Programmatic LLM Evaluation, LangSmith, Prompt Versioning |

### Bullet Point Formula (STAR)
```
Weak: "Built an AI chatbot using LangChain"
Strong: "Architected a multi-agent orchestration pipeline using LangGraph and FastAPI,
reducing manual data extraction time by 85% while maintaining 94% factual accuracy
measured via Ragas evaluation frameworks"
```

### Headline
```
❌ "Fresher Software Engineer"
✅ "Agentic AI Engineer | LangGraph & FastAPI | Building Autonomous Workflows"
```

### Non-Negotiable Resume Requirements
- GitHub link AND deployed URL for EVERY project
- OR Loom video demo if hosting is cost-prohibitive
- Every bullet must have: Action verb + Technology used + Quantified impact

---

## 📋 Platform Execution Strategy

| Platform | Strategy | Expected Conversion |
|----------|----------|-------------------|
| **Wellfound** | Search exact: "LangGraph", "Agentic", "MCP". Filter by India/Remote | Direct founder chat |
| **YC Work at a Startup** | Filter: Remote + Engineering. Highlight independent building | Premium YC startups |
| **X (Twitter) DMs** | Find CTOs of funded AI startups. Send deployed project link | Bypasses HR entirely |
| **LinkedIn DMs** | Same as X — personalized message + proof of work | Inbound recruiter pull |

---

## ⚡ Skill Gap Analysis — ROI Prioritization

### Must-Have (Highest ROI — Add Immediately)
| Skill | Why | Time to Learn |
|-------|-----|---------------|
| **LangGraph** | Stateful agent orchestration. Basic LangChain chains are obsolete | 3-4 days |
| **MCP (Model Context Protocol)** | Explicitly demanded by top companies (Great Question etc.) | 2-3 days |
| **FastAPI + Async Python** | Required for streaming LLM responses in production | 2 days |
| **Programmatic LLM Evaluation (LangSmith, Ragas)** | "Vibes-based testing is a terminal red flag" | 2-3 days |
| **pgvector + Hybrid Search (BM25 + Vector)** | Enterprise standard for scalable retrieval | 2-3 days |

### Good-to-Have (High ROI — Add if time permits)
| Skill | Why | Time to Learn |
|-------|-----|---------------|
| **Next.js + TypeScript** | Unlocks "Full Stack AI Engineer" roles (higher pay) | 4-5 days |
| **Docker + AWS ECS + GitHub Actions** | Deploy pipeline — separates deployable engineers from theorists | 2-3 days |

### Nice-to-Have (Lower ROI — Skip if short on time)
| Skill | Why |
|-------|-----|
| **LoRA / PEFT Fine-tuning** | Advanced prompting + RAG solves 90% of business problems |
| **LlamaIndex** | Some JDs mention it, but LangChain + LangGraph covers same ground |

### 🚫 DO NOT SPEND TIME ON (for this sprint)
| Skill | Why to Skip |
|-------|-------------|
| Training CNNs/RNNs from scratch | Modern GenAI roles use pre-trained models via APIs. Zero JD mentions |
| Django / Flask | FastAPI has near-total dominance in AI engineering JDs |
| Deep ML theory (backpropagation math) | Not tested in interviews — applied engineering is what matters |

---

## 🧠 Interview Dynamics

### What They Actually Test
1. **AI System Design** — The defining technical hurdle
   - "Design a scalable LLM-powered enterprise search for 1M queries/day"
   - Must discuss: caching (Redis), query routing (cheap vs expensive models), latency optimization

2. **The Latency/Cost/Accuracy Trilemma**
   - Interviewers probe: "How do you optimize for all three?"
   - Answer: semantic caching + local model routing + frontier model only for complex reasoning

3. **Portfolio Deep-Dive**
   - They will break your deployed project. Edge cases matter.
   - "What happens when the API rate-limits you?"
   - "What if the LLM returns malformed JSON?"
   - "Walk me through your error handling"

### Common Rejection Reasons
- 🔴 "Demo-Driven Development" — app works in ideal conditions, breaks on edge cases
- 🔴 Can't explain engineering trade-offs (using GPT-4o for trivial classification)
- 🔴 Tutorial projects (signals inability to build independently)

### Compensation Reality Check
- **Indian startups:** ₹10-12 LPA may include ESOPs. Ask: "What's the fixed cash component?"
- **Global remote:** $24k-$40k is ALL cash. Higher immediate utility in India
- Always calculate: monthly in-hand = (CTC - tax - PF - PT) / 12

---

## 📊 Updated Target Map

| Milestone | Target | Timeline | Strategy |
|-----------|--------|----------|----------|
| Internship | ₹30k-₹50k/mo | Day 28 (Aug ~10) | Apply Wellfound+YC, showcase deployed RAG project |
| Full-Time (India) | ₹10-12 LPA (₹80k-₹1L/mo) | Day 56 (Sep ~10) | Convert internship → PPO OR apply with 2 projects deployed |
| Full-Time (Global) | $24k-$40k/yr (₹20L-₹34L/yr) | Day 60+ | Target YC startups, async communication, full-stack capability |
