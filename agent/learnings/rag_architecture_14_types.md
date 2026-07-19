# 🧠 RAG Architecture Knowledge — 12 LPA+ Level

**Source:** Self-research + Market validation (Jul 17, 2026)
**Context:** What a fresher must know about RAG to command ₹10-12+ LPA

---

## The 14 Types of RAG

### 3 Core Paradigms

| Type | Core Idea | When to Use |
|------|-----------|-------------|
| **Naïve RAG** | Retrieve → Augment → Generate (simple chunk + embed + search) | Baseline. Toy projects only |
| **Advanced RAG** | Adds pre-retrieval (query expansion) + post-retrieval (reranking) | Production systems. 90% of use cases |
| **Modular RAG** | Plug-and-play components (routers, memory, web search swapped dynamically) | When you need flexibility per query type |

### Advanced & Specialized RAG

| Type | Core Idea | 12 LPA Relevance |
|------|-----------|-----------------|
| **Agentic RAG** | LLM-driven agent plans, selects tools, decides when to search or stop | 🔴 Must-Know — primary architecture for agent roles |
| **Graph RAG** | Builds knowledge graph from text to capture entity relationships | 🟡 Good-to-Know — Microsoft's approach |
| **Self-RAG (Reflective)** | LLM critiques own output using special tokens for relevance/quality | 🟡 Good-to-Know — advanced pattern |
| **Corrective RAG (CRAG)** | Lightweight evaluator checks quality; falls back to web search if poor | 🔴 Must-Know — shows error handling maturity |
| **Adaptive RAG** | Router classifies query complexity → simple→Naïve, complex→Agentic | 🔴 Must-Know — cost optimization signal |
| **Conversational RAG** | Injects chat history into retrieval for pronouns/follow-ups | 🔴 Must-Know — every real app needs this |
| **Hybrid RAG** | Dense vector search + sparse keyword search (BM25) | 🔴 Must-Know — enterprise standard (pgvector) |
| **Multi-Modal RAG** | Retrieves across images, audio, video, text | ⚪ Nice-to-Know — specialized use cases |
| **Multi-Hop RAG** | Decomposes complex question → sub-queries, hop 1 feeds hop 2 | 🟡 Good-to-Know — shows architectural depth |
| **Hierarchical RAG** | Summary parent chunks + detailed child chunks for context | 🟡 Good-to-Know — parent-child chunking |
| **Ensemble RAG** | Multiple retrieval strategies blended via Reciprocal Rank Fusion | 🟡 Good-to-Know — advanced optimization |

---

## 🔴 The 4 Areas You MUST Master for 12 LPA+

### 1. Advanced Data Chunking & Pre-Processing

| Technique | Problem It Solves | How It Works |
|-----------|------------------|--------------|
| **Fixed-size chunking** | ❌ Cuts sentences in half, destroys context | Splits every N characters. Never use alone |
| **Semantic Chunking** | ✅ Preserves meaning boundaries | Split text based on embedding distance changes between sentences |
| **Parent-Child Chunking** | ✅ Best of both worlds | Store small chunks for exact search, pass larger parent doc to LLM for context |

**Interview answer:** "I use parent-child chunking — small semantic chunks for retrieval precision, but pass the full parent document to the LLM so it has sufficient context to answer accurately."

### 2. Retrieval Optimization & Reranking

| Problem | Solution | How |
|---------|----------|-----|
| Top 20 docs → "Lost in the Middle" syndrome + high API cost | **Cross-Encoder Reranker** | Cohere Rerank or BGE-Reranker evaluates query-doc relationship → drops 20→3 |
| Poorly phrased user questions | **Query Rewriting** | LLM rewrites ambiguous queries before hitting vector DB |

**Interview answer:** "I use a cross-encoder reranker to compress top-20 results to top-3 relevant ones. This solves 'Lost in the Middle' and reduces LLM context costs by 85%."

### 3. Evaluation Frameworks (The Ultimate Interview Seller)

> *Market research: "Vibes-based testing is a terminal red flag. Programmatic eval separates engineers from hobbyists."*

**The RAG Triad (Ragas / TruLens):**

| Metric | Question It Answers |
|--------|-------------------|
| **Context Relevance** | Did we retrieve the RIGHT data? |
| **Groundedness (Faithfulness)** | Is the answer based ONLY on retrieved data? (No hallucinations) |
| **Answer Relevance** | Did the LLM actually answer the user's question? |

**Interview answer:** "I build golden test datasets and run Ragas evaluation in CI/CD. I track faithfulness ≥ 0.9, answer relevancy ≥ 0.85, and context precision ≥ 0.8 before any prompt change ships to production."

### 4. Vector Databases & Latency Management

| Problem | Solution |
|---------|----------|
| Naïve search slows at millions of vectors | **HNSW** (Hierarchical Navigable Small World) — graph-based index, faster but more memory |
| Memory constraints | **IVF-PQ** (Inverted File with Product Quantization) — compresses vectors, sacrifices some accuracy |

**Interview answer:** "I use HNSW for latency-critical paths (search under 100ms) and IVF-PQ for memory-constrained deployments. The choice depends on the accuracy vs speed tradeoff."

---

## ✅ Market Validation

This knowledge directly maps to what companies paying ₹10-12 LPA ask in **AI System Design** rounds:

> *"Design a scalable LLM-powered enterprise search for 1M queries/day"*

| Interview Question | Your Answer Should Reference |
|-------------------|------------------------------|
| "How do you handle bad queries?" | Query rewriting + Adaptive RAG routing |
| "How do you ensure accuracy?" | Cross-encoder reranking + Parent-child chunking |
| "How do you measure quality?" | Ragas Triad (faithfulness, relevancy, precision) |
| "What happens at scale?" | HNSW vs IVF-PQ tradeoffs, caching layer |
| "How do you control costs?" | Adaptive RAG — cheap model for simple, expensive for complex |
| "What if retrieval fails?" | Corrective RAG (CRAG) — web search fallback |

---

## 📚 Reference Library

### NirDiamant/RAG_Techniques — 42+ Runnable Notebooks
**Link:** https://github.com/NirDiamant/RAG_Techniques

A community-driven repo covering RAG from foundational to cutting-edge. Each notebook has intuition + code + references.

**How to use during your sprint:**
- Phase 2 (Days 20-24): Run their Semantic Chunking + Chunk Size Optimization notebooks
- Phase 3 (Days 25-28): Run their Hybrid Search, CRAG, Adaptive Retrieval, and Ragas Evaluation notebooks
- All notebooks have Colab links — open and run instantly, no setup needed

**3 high-value techniques to quickly reference (15 mins each):**
1. **Proposition Chunking** — Splits text into atomic self-contained facts. Alternative to semantic chunking. Interview answer: *"I use proposition chunking for factual precision in retrieval."*
2. **Fusion Retrieval** — Runs multiple query phrasings in parallel, combines via Reciprocal Rank Fusion. Interview answer: *"Fusion retrieval captures different query interpretations and combines results robustly."*
3. **Explainable Retrieval** — Shows which parts of a document caused the semantic match. Interview answer: *"Explaining WHY a document was retrieved is essential for auditing and debugging RAG pipelines."*
