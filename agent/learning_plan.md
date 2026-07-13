# 📚 Complete AI Engineer Roadmap (12 Months)

**Target Role:** AI Engineer / Agentic AI Engineer
**Focus:** LLMs, RAG, agents, NLP, applied ML. NO research, NO heavy math.
**Phase 1 (30 days):** Quick job to stop financial bleed.
**Phases 2-4:** Deepen AI skills, fill interview knowledge gaps.

---

## 🎯 Target Roles

| Role | Salary (India) | Fit |
|------|----------------|-----|
| **AI Engineer** | ₹8-25 LPA | ✅ Primary target |
| **Agentic AI Engineer** | ₹10-30 LPA | ✅ Primary target |
| **GenAI Engineer** | ₹8-22 LPA | ✅ Strong fit |
| **AI/ML Developer** | ₹7-18 LPA | ✅ Strong fit |
| Backend AI Engineer | ₹8-18 LPA | ⚠️ Fallback |
| ML Engineer | ₹7-20 LPA | ⚠️ Possible but less interest |
| Data Scientist | ₹6-18 LPA | ❌ Not interested |

---

## 🧠 Complete AI Engineer Tech Stack

| Domain | Technologies | Depth |
|--------|-------------|-------|
| **Languages** | Python, SQL | Deep |
| **Data Manipulation** | Pandas, NumPy | Practical — enough for interviews |
| **ML Fundamentals** | Scikit-learn (regression, classification, clustering basics) | Conceptual — explain algorithms, not implement from scratch |
| **NLP** | Tokenization, embeddings, BERT vs GPT, transformers concept | Interview-ready — explain architecture, not math |
| **LLMs & Gen AI** | OpenAI API, LangChain, RAG, LangGraph, MCP, prompt engineering | Deep — core skill |
| **AI Agents** | LangGraph (StateGraph, multi-agent), tool calling, MCP servers | Deep — core skill |
| **Model Serving** | FastAPI, Docker, AWS EC2 | Practical — deploy models, not build infra |
| **Evaluation** | Ragas, LLM-as-a-judge, basic ML metrics | Practical |
| **DSA** | 60 problems (arrays, strings, hash maps, trees, graphs) | Interview-ready |
| **System Design** | AI system design basics (RAG scaling, caching, routing) | Conceptual |

## Phase 1 NOT in Scope (Postpone to Phases 3-4)
- ⏳ PyTorch / TensorFlow → Phase 3
- ⏳ MLOps (Kubeflow, model monitoring) → Phase 4
- ⏳ Model training/fine-tuning → Phase 3
- ⏳ Research papers → Phase 4
- ❌ Computer Vision (not relevant to target roles)
- ❌ Statistical ML theory (hypothesis testing, Bayesian)

---

## 🧭 4-Phase Roadmap

### Phase 1 (30 Days — Jul 11 to Aug 10): QUICK JOB
**Goal:** ₹15-40k/mo role. Stop financial bleed.
**Stack:** FastAPI + PostgreSQL + LLM APIs + RAG + Docker + AWS + 30 DSA
**Interview prep:** Transformer architecture, RNN vs CNN vs Transformer (basic), NLP basics (tokenization, embeddings), ML fundamentals (overfitting, cross-validation)
**Portfolio:** 1 deployed RAG API with Ragas eval
**Eligible for:** AI Intern, Jr GenAI Engineer, AI Developer

### Phase 2 (Months 2-3 — Aug-Sep): ML FUNDAMENTALS + DEEPER NLP
**Goal:** Fill interview knowledge gaps. Be credible in any AI interview.
**Applied skills:** Scikit-learn end-to-end pipelines, Pandas/NumPy advanced, feature engineering
**Interview knowledge:**
- ML: Regression, classification, clustering, decision trees, ensembles (Random Forest, XGBoost), regularization, cross-validation, confusion matrix, precision/recall/F1, ROC-AUC
- NLP: Tokenization (BPE, WordPiece), Word2Vec/GloVe, sequence length, padding, BERT vs GPT in depth, fine-tuning vs RAG, prompt engineering vs fine-tuning
- Deep learning concepts (NOT implementation): What are neural networks? What is backpropagation conceptually? What are activation functions? What is attention?
**Portfolio:** Upgrade RAG system with better retrieval + evaluation
**Eligible for:** AI Engineer, GenAI Engineer, NLP-focused AI roles

### Phase 3 (Months 4-6 — Oct-Dec): AGENTIC AI + DEEP LEARNING
**Goal:** Be a strong Agentic AI Engineer. Also learn DL fundamentals.
**Agentic AI skills:** LangGraph advanced (multi-agent, human-in-the-loop, checkpointing), MCP servers (2-3 custom), open-source contributions, advanced RAG (hybrid search, reranking)
**Deep Learning (PyTorch):**
- Tensors, autograd, nn.Module, datasets/dataloaders
- Build: simple NN for classification, CNN for image tasks
- Fine-tune: BERT/GPT with HuggingFace Transformers
- Concept: backpropagation, gradient descent optimizers, loss functions
**Interview knowledge:**
- Agent patterns: ReAct, Plan-Execute, Reflection, Tool use, Multi-agent
- Memory systems: Short-term, episodic, semantic memory in agents
- Evaluation: Task completion rate, latency/cost tradeoffs
- DL: What are neural networks? How does backpropagation work? What are CNNs/RNNs/Transformers?
**Open source:** 2-3 merged PRs in LangChain, Ragas, or FastMCP repos
**Portfolio:** 1 fine-tuned model (BERT sentiment or similar) deployed + agent system
**Eligible for:** Agentic AI Engineer, AI Engineer (with DL knowledge)

### Phase 4 (Months 7-12 — Jan-Jun): BROADEN + MLOps + SPECIALIZE
**Goal:** Eligible for all AI Engineer roles up to mid-senior + MLOps knowledge.
**MLOps:**
- MLflow: experiment tracking, model registry, deployment
- Model monitoring: data drift, concept drift, performance decay
- CI/CD for ML: automated retraining pipelines, A/B testing
- Feature stores, model versioning, canary deployments
- Model serving: vLLM, Ollama, Triton Inference Server basics
**Deepen:** LangGraph at scale, production MCP, multi-modal LLMs, cost optimization, semantic caching
**Observe:** Langfuse, Helicone — LLM tracing, P95 latency, token cost dashboards
**DSA:** 60 problems total (add graphs, DP basics)
**System design:** AI system design for interviews (RAG at scale, agent architecture, LLM gateway)
**Eligible for:** ALL AI Engineer roles + MLOps-aware roles up to mid-senior

---

## 🚫 Not in Scope (Even Long Term)

| Topic | Why Skip |
|-------|----------|
| **Computer Vision deep dive** | Not relevant to target roles |
| **Statistical theory** (hypothesis testing, p-values, Bayesian) | Data Scientist territory |
| **Research paper implementation** | Unless working in research lab |
| **Kubernetes deep dive** | Docker + AWS ECS is sufficient |

---

## 📅 Phase 1 Detail — First 30 Days

### Week 1: Python + Data Basics + FastAPI Foundation

| Day | Morning | Afternoon | Evening (DSA) |
|-----|---------|-----------|---------------|
| **11** | Pandas (DataFrames, read_csv, groupby) | NumPy (arrays, broadcasting) | Contains Duplicate |
| **12** | Scikit-learn basics (regression, classification) | Tuples, enumerate(), zip() | Valid Anagram |
| **13** | OOP (classes, inheritance, @property) | Context Managers, Modules | Two Sum II |
| **14** | Async Python (asyncio, async/await) | FastAPI basics (routes, Pydantic) | Group Anagrams |
| **15** | FastAPI CRUD + JWT auth | Docker + PostgreSQL setup | Top K Frequent |
| **16** | Dockerize FastAPI app | LLM APIs (OpenAI, streaming) | Product of Array |
| **17** | **First AI prototype** (LLM + FastAPI + Docker) | Valid Palindrome |

### Week 2: RAG Foundation

| Day | Topics | DSA |
|-----|--------|-----|
| 18 | PostgreSQL queries, pgvector setup | 3Sum |
| 19 | LangChain (loaders, splitters, chains) | Container With Most Water |
| 20 | Naive RAG + embeddings + cosine search | Best Time to Buy/Sell |
| 21 | LangGraph basics (StateGraph, nodes, edges) | Valid Parentheses |
| 22 | ReAct pattern, tool calling | Min Stack |
| 23 | Advanced RAG (hybrid search, reranking) | Binary Search |
| 24 | Ragas evaluation (faithfulness, precision) | Search 2D Matrix |

### Week 3: Project + LangGraph + MCP

| Day | Topics | DSA |
|-----|--------|-----|
| 25 | **Build RAG API** (upload → chunk → embed → query) | Reverse Linked List |
| 26 | LangGraph state persistence + conditional routing | Merge Two Sorted |
| 27 | **MCP server** (FastMCP, expose DB as tool) | Max Depth Tree |
| 28 | **Deploy on AWS** (Docker + EC2 + CI/CD) | Same Tree |
| 29 | Resume + LinkedIn + applications start | Level Order Traversal |
| 30 | Applications + DSA revision | Review |

### Week 4: Interview Prep + Applications

| Day | Topics | DSA |
|-----|--------|-----|
| 31 | Mock interview — Transformer architecture, RNN vs CNN vs Transformer | Review Arrays |
| 32 | Mock interview — NLP basics, BERT vs GPT, embeddings | Review Pointers |
| 33 | Mock interview — ML fundamentals, overfitting, regularization | Review Stack |
| 34 | Mock interview — Agent patterns, ReAct, tool calling | Review Trees |
| 35-40 | Applications + take-homes + offers | DSA review |

---

## 🛡️ Backup

| If... | Then... |
|-------|---------|
| No FT offer by Day 40 | Take ₹15-25k internship. Keep building evenings. |
| Interview asks math-heavy ML | Admit "I focus on applied AI, not research. But conceptually I understand X." |
| Role requires PyTorch | Learn basics in 1 week — enough for interview. |

---

*Target: AI Engineer / Agentic AI Engineer. Not researcher, not backend-only, not data scientist.*
