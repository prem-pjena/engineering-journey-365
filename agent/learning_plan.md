# 📚 60-Day Agentic AI Engineer Sprint: Complete Curriculum (Market-Validated v2)

**Target Role:** Agentic AI Engineer | AI Engineer | SDE AI
**Target Compensation:** ₹30-50k/mo intern (Day 28) → ₹10-12 LPA FT / $24-40k/yr global remote (Day 60)
**Investment:** 5-6 hours daily. Zero days off.

---

## 📊 Complete Tech Stack (Market-Validated Priority Matrix)

| Priority | Category | Technologies |
|----------|----------|-------------|
| 🔴 Must-Know | Python Architecture | OOP (classes, inheritance, dunder, @property, static/classmethod), Context Managers, Async (asyncio, await, gather), Generators (yield), Tuples, enumerate, zip, String methods, JSON, Comprehensions, Type hints, Modules |
| 🔴 Must-Know | Backend API | **FastAPI**, Pydantic v2 strict validation, **Asynchronous Python**, **Server-Sent Events (SSE)** for streaming (market standard — Django/Flask are obsolete for AI roles) |
| 🔴 Must-Know | LLM & Orchestration | LangChain (prompt templates, loaders, splitters, with_structured_output), **Algorithmic Prompt Optimization (DSPy + GEPA)**, LLM APIs (OpenAI, Gemini) — **LCEL deep dive deprioritized, use LangGraph for orchestration** |
| 🔴 Must-Know | Agent Frameworks | **LangGraph** (StateGraph, nodes, edges, reducers, routing, checkpointing via **PostgresSaver**, HITL, multi-agent, parallel **Send API**, hash-based idempotent recompute) — industry standard for production agents. **OpenAI Agents SDK** for lightweight handoffs/voice. **CrewAI** for rapid role-based agent assembly (complementary to LangGraph) |
| 🔴 Must-Know | RAG & Search | Corrective → Adaptive → Agentic RAG, **Proposition Generation**, **Step-back Prompting**, **Semantic Chunking**, **Parent-Child Chunking**, **Cross-encoder Reranking**, **Hybrid Search (BM25 + Dense + tsvector + RRF)**, **GraphRAG**, pgvector, **RAGFlow DeepDoc** for enterprise document parsing — **Naive RAG deprioritized** |
| 🔴 Must-Know | Agent Memory | **Mem0** (semantic fact extraction, automated deduplication, contradiction resolution), **Graphiti** (temporal knowledge graphs), **Procedural Memory** (parameterized workflow templates from execution traces), **Blackboard System** (multi-agent shared memory with optimistic locking) |
| 🔴 Must-Know | Agentic Web Interaction | **browser-use** (Playwright-based visual DOM understanding, tab/multi-tab navigation), **Firecrawl** (LLM-ready markdown extraction, anti-bot bypass, batch crawling) |
| 🔴 Must-Know | Sandboxed Execution | **Daytona SDK** (isolated, ephemeral sandboxes with dedicated kernel, network isolation, vCPU/RAM allocation for AI-generated code) |
| 🔴 Must-Know | Evaluation & Observability | **LangSmith**, **Langfuse/OpenLLMetry** (observability + tracing), **Ragas** (Faithfulness, Context Precision/Recall, Answer Relevancy), **LLM-as-a-judge** regression testing, **AIBOM** (AI Bill of Materials for supply chain security) |
| 🔴 Must-Know | Constrained Decoding | **XGrammar / Outlines** — finite-state machine token masking for guaranteed JSON output. Prevents agent crashes from malformed tool calls |
| 🔴 Must-Know | Inference Optimization | **vLLM** (PagedAttention, continuous batching, Tensor Parallelism), KV cache management, Quantization (INT8/INT4) — essential for open-source model serving |
| 🔴 Must-Know | Semantic Caching | **Redis** (LangCache) with vector embedding + cosine similarity threshold tuning (0.85-0.95) + hybrid metadata filtering for tenant isolation. **Redis for agent session state storage** |
| 🔴 Must-Know | Agent Security | **Dual Schema Enforcement** (Agno pattern — read-only transaction scopes for data agents), **JWT-based RBAC**, **AgentShield** (config scanning, adversarial red-teaming), **NeMo Guardrails** (topical bounding, jailbreak detection), **OAuth 2.1** for MCP (token exchange, no token passthrough, per-client consent registries) |
| 🔴 Must-Know | SQL & Vectors | PostgreSQL, pgvector, **pgvectorscale (DiskANN)** for SSD-optimized billion-scale vectors, HNSW vs IVFFlat vs DiskANN vs **PQ vs IVF+PQ** indexing, vector similarity search, **read-only transaction scopes**, **Recursive CTEs** for tree traversal, **tsvector full-text search + Reciprocal Rank Fusion** for hybrid retrieval |
| 🔴 Must-Know | Tensor-Native Search | **Vespa** — unified tensor framework for dense, sparse, lexical, and multi-modal retrieval in single engine. Phased ranking (BM25 + HNSW + ONNX reranking) |
| 🔴 Must-Know | Serverless Vector Storage | **LanceDB** — Arrow-native columnar format, memory-mapped S3-backed zero-copy access, compute-storage decoupling |
| 🔴 Must-Know | Distributed Vector DB | **Milvus** — Knowhere engine, Proxy/QueryNode/IndexNode decoupling, GuaranteeTs consistency, consistency_level tuning (Strong/Bounded/Eventual) |
| 🔴 Must-Know | Agent Memory Databases | **Cognee** (graph-native memory control plane), **Neo4j** (tripartite Short/Long/Reasoning memory), **Graphiti** (bi-temporal knowledge graphs), **AgentMemory** (MCP-integrated procedural memory with Ebbinghaus decay) |
| 🔴 Must-Know | DSA | **Pareto 50+** — Arrays & Hashing, Two Pointers, Sliding Window, Stack & Queue, Binary Search, Linked Lists, Trees (BFS/DFS), Graphs (BFS/DFS/Topo Sort/Cycle Detection), Intervals, Backtracking, Heaps, Design (LRU Cache, Trie, Time-Based KV), **DP (Coin Change, LIS, Climbing Stairs)**, **Monotonic Stack (Largest Rectangle, Trapping Rain Water)**, **BFS Shortest Path (Word Ladder)**. **Probabilistic Data Structures**: Bloom filters, HyperLogLog. **Dimensionality Reduction**: matrix multiplication complexity for attention |
| 🔴 Must-Know | Local LLM Deployment | **Ollama** — run LLMs locally for development, privacy-preserving deployment, data sovereignty compliance (critical for Indian enterprise/fintech) |
| 🔴 Must-Know | Enterprise RAG Engine | **RAGFlow** — DeepDoc module for layout-aware document parsing (tables, headers, multi-column, OCR), visual RAG pipeline builder |
| 🔴 Must-Know | Token Optimization | **Headroom** — content-aware compression (JSON, AST, prose) reducing token overhead 60-95% before LLM processing |
| 🔴 Must-Know | Local Agent Gateway | **OpenClaw** — multi-channel agent gateway, AGENTS.md/SOUL.md workspace state management, local-first orchestration |
| 🔴 Must-Know | Agentic Coding | **Claude Code** — agentic coding tool, CLAUDE.md workspace context injection, automated three-phase loop (gather → act → verify) |
| 🟡 Good-to-Have | Visual Workflow Builders | **n8n**, **Langflow**, **Dify** — rapid prototyping and stakeholder demonstrations; not for production agent workflows |
| 🟡 Good-to-Have | Self-Hosted Chat UI | **Open WebUI** — offline-capable ChatGPT alternative for local testing |
| 🟡 Good-to-Have | Sparse Vector Search | **Elasticsearch ELSER** — learned sparse retrieval (~30K dimensions), exact-match precision + deep semantic matching without fine-tuning |
| 🟡 Good-to-Have | Enterprise RAG Reference | **Bisheng** — study production document extraction pipelines, hybrid orchestration engines (theory only) |
| 🟡 Good-to-Have | Full-Stack | **Next.js + TypeScript** (unlocks Full Stack AI Engineer roles — premium pay for end-to-end delivery) |
| 🟡 Good-to-Have | Data | Pandas, NumPy basics |
| 🟡 Good-to-Have | Interview Theory | Transformer architecture (Q, K, V, self-attention, RoPE), BERT vs GPT, tokenization (BPE/WordPiece/Unigram/SentencePiece), LLM inference architecture (vLLM, KV cache), **MCP OWASP Top 10**, **Procedural vs Episodic vs Semantic Memory**, **Blackboard Architecture**, **DeepSeek-V3 (MLA, MoE) internals**, **Classical ML (Logistic Regression, Random Forest, XGBoost, K-Means, PCA)** |
| ⚪ Nice-to-Have | Fine-tuning | LoRA / PEFT — 8.5% JD mention vs RAG 35.9%. Read 1 article for concept only |
| 🟡 Good-to-Have | Prototype-Only | **CrewAI** — rapid role-based assembly, not for stateful production. **n8n/Langflow/Dify** — visual prototyping only |
| 🚫 Skip | CNNs/RNNs/Classical ML | Zero JD mentions for GenAI Engineer roles. Skip bias-variance, cross-validation, gradient descent entirely |

---

## 📅 60-Day Complete Curriculum (Market-Validated)

### Phase 1-2: Core DSA Mastery & Algorithmic Optimization (Days 11-24)
*Goal: Arrays, hashing, two pointers, linked lists, binary search. Python + FastAPI + DSPy/GEPA*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 11 | **Python Decorators**: Functions as first-class objects, wrapper functions, @syntax + **OOP deep dive**: @property, @staticmethod, @classmethod, dunder methods (`__len__`, `__getitem__`, `__setitem__`, `__repr__`, `__iter__`) | Build DocumentStore class with custom dunder methods for string-based exact document lookup | Two Sum | vector_store_oop.py |
| 12 | **Terminal Basics**: cd, ls, mkdir, touch, pwd + **Git Fundamentals**: init, add, commit, status, log + **Context Managers** (`__enter__`, `__exit__`), Modules, `__init__.py` + **IDE Setup**: virtual environment (venv), pip install | Init Git repo. Create Python package with `__init__.py`. Safe File I/O Manager. First commit | Valid Anagram | context_logger.py |
| 13 | **pip + venv**: Installing packages, requirements.txt, virtual environments + **HTTP Protocol** (GET/POST/PUT/DELETE, headers, status codes, MIME types, request-response lifecycle) + **Python Type Hinting** (Union, Optional, List, Dict) + **FastAPI intro** | Setup venv. Install FastAPI/uvicorn. Build strictly-typed GET/POST endpoint. Understanding what an API endpoint is | Group Anagrams | fastapi_hello.py |
| 14 | Generators (yield), Tuples, enumerate, zip | Build a custom text stream simulator that mimics sequential token generation of a document with configurable delays using generators | Top K Frequent | token_streamer.py |
| 15 | **Markdown Syntax Basics**: headings, code fences, bold/italic, lists + **String methods, regex module** (re.search, re.findall, re.sub), JSON module + **Defensive Parsing**: handling truncated brackets, unescaped quotes, extracting JSON from markdown-wrapped LLM outputs | Build an error-resilient parser that strips markdown fences, extracts JSON blocks, handles malformed strings | Product of Array | defensive_json_parser.py |
| 16 | **Environment Variables**: .env files, os.environ, python-dotenv, API key security + **LLM APIs**: What is a token? Logit? Softmax? Autoregressive generation? Model lifecycle (training vs inference). Temperature, top-k, top-p, streaming | Setup .env with API keys. Build multi-turn Chat CLI with real-time streaming and conversation history | Valid Palindrome | basic_llm_api.py |
| 17 | **Prompt Engineering Fundamentals**: System prompts, Role prompting, Zero-shot vs Few-shot, Chain-of-Thought conceptually | Build a manual prompt template router that generates specialized outputs based on few-shot examples | 3Sum | prompt_engineering.py |
| 18 | **Async Python** (asyncio, event loop, gather, async/await, concurrency vs parallelism) + **Data Serialization**: What is a schema? JSON Schema, Pydantic models, serialization/deserialization + FastAPI SSE Streaming + **Generative Parameters**: Logit bias, Softmax, Temperature scaling | Build streaming REST endpoint with Pydantic schema validation. Force specific token constraints | Container With Most Water + Two Sum II | fastapi_streaming.py |
| 19 | **Data Pipeline Theory**: What is a pipeline? Stages, I/O flow, transformations + **LangChain Fundamentals**: What is LangChain? PromptTemplate, ChatPromptTemplate, Messages (System/Human/AI), output parsers (StrOutputParser, PydanticOutputParser), **LCEL basics** (pipe operator), simple chains | **Apply to Documents**: Document Loaders, RecursiveCharacterTextSplitter, Regex-based chunking. Parse first PDF | Longest Substring w/o Repeat | langchain_fundamentals.py |
| 20 | **Vector Mathematics**: Linear algebra basics (vector spaces, dot product, cosine similarity, dimensions) + **Embeddings API** (OpenAI text-embedding-3-small) | Manually embed text chunks. Write a pure-Python cosine similarity search function (no databases yet) | Valid Parentheses | vector_math_embeddings.py |
| 21 | **Basic RAG Pipeline**: What is RAG? Full loop: chunk → embed → store in simple Python list → retrieve via cosine similarity → generate answer with LLM. Build functional single-hop Q&A over local document | Binary Search | basic_rag.py |
| 22 | **Relational Database Fundamentals**: Tables, Rows, Primary/Foreign Keys, Data Types + **ACID Properties**: Atomicity, Consistency, Isolation, Durability, Transactions, Commit, Rollback + **SQL Basics**: SELECT, INSERT, WHERE, JOIN + **Python DB connections** (sqlite3) | Build a basic SQLite database. Insert and query document metadata. Practice transactions and rollback | Search 2D Matrix | sql_fundamentals.py |
| 23 | **Information Retrieval Theory**: TF-IDF, sparse vs dense vectors, inverted index architecture + **Parent-Child Chunking** + **Cross-Encoder Reranking** (Bi-encoder vs Cross-encoder theory) | Implement a two-stage retrieval pipeline: TF-IDF for candidate retrieval + local reranking model for re-scoring | Reverse Linked List | ir_reranking.py |
| 24 | **Docker Basics**: What is Docker? Images vs Containers, Dockerfiles, docker pull/run/ps, port mapping, volumes + **Hybrid Search Theory**: BM25 algorithm, sparse vs dense fusion, **Reciprocal Rank Fusion (RRF)** formula + pgvector HNSW vs IVFFlat tuning via Docker container | Run pgvector in Docker. Implement BM25 keyword search alongside dense search. Fuse results using RRF. Benchmark recall | Merge Two Sorted Lists | docker_hybrid_search.py |

### Phase 3: Classical ML, NLP Theory & Transformer Internals (Days 25-31)
*Goal: Math/statistics foundations, classical ML, transformer internals, DeepSeek-V3 (MLA, MoE), RAG evaluation metrics. No new DSA — this phase builds theory*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 25 | **Linear Algebra for AI**: Vector spaces, dot products, matrix multiplication, eigenvectors, geometric intuition of high-dimensional spaces | Solve linear algebra practice problems. Visualize vectors and matrix transformations | Reorder List | linear_algebra.py |
| 25B | **Calculus for Deep Learning**: Derivatives, Partial Derivatives, Chain Rule + **Optimization Theory**: Gradient Descent, Learning Rates, convex vs non-convex optimization | Build a simple gradient descent optimizer in pure Python. Visualize loss landscape | — | gradient_descent.py |
| 26 | **Data Science Tooling**: Pandas DataFrames (head, describe, groupby), NumPy arrays (broadcasting, reshape) + **Classical ML Intro**: Supervised vs Unsupervised learning. **Logistic Regression** (classification basics). **K-Means** (clustering basics). Probability & Statistics (Bayes, distributions) integrated | Implement Logistic Regression on toy dataset. Implement K-Means clustering. Compare results | Max Depth Tree | classical_ml_intro.py |
| 27 | **Classical NLP**: Bag of Words, N-grams, Tokenization, Stop words + **Word Embeddings**: Word2Vec (CBOW vs Skip-gram), GloVe, loading pre-trained embeddings | Build BoW and TF-IDF vectors. Train a basic Word2Vec embedding. Visualize embedding space with PCA | Validate BST | classical_nlp.py |
| 27B | **Sequential Models**: Why sequences? RNN theory, hidden states, vanishing/exploding gradients + **LSTM theory**: gates (forget, input, output), cell state vs hidden state | Compare RNN forward pass with feedforward network on sequential data | — | sequential_models.py |
| 28 | **Neural Network Lifecycle**: Training vs Inference, forward pass, backward pass (conceptual), loss calculation + **Transformer Internals**: Why transformers? Seq2Seq bottlenecks. Multi-head attention math (QKV, scaled dot-product, why divide by sqrt(d_k)), positional encoding (RoPE), layer norm, residual connections, FFN | Implement a minimal transformer block (conceptual math first, then code). Compare with RNN forward pass | Invert Tree | transformer_block.py |
| 29 | **Standard KV Cache Mechanics**: Inference-time memory management, Key-Value tensors, cache size scaling with sequence length + **Mixture-of-Experts**: Sparse vs dense networks, routing gates, expert allocation + **DeepSeek-V3** (MLA, MoE, MTP) | Diagram standard KV cache vs MLA compression. Calculate memory savings for different sequence lengths | LCA of BST | kv_cache_moe.py |
| 30 | **Evaluation Theory**: N-gram overlap (BLEU, ROUGE), Ranking metrics (MAP, MRR, NDCG) + **LangSmith Platform**: Projects, traces, spans, datasets + **Ragas**: Faithfulness, Context Precision, Answer Relevancy | Setup LangSmith project. Build automated evaluation pipeline for local RAG system. Measure and log metrics | Level Order Traversal | langsmith_eval.py |
| 31 | **LangGraph Foundations**: What is LangGraph? StateGraph vs plain Chain. Defining state (TypedDict), Nodes (functions that modify state), Edges (conditional routing based on state values), Reducers (add_messages). **State Machine Theory**: DAGs, cyclic execution, checkpointing | Build a simple deterministic cyclic LangGraph agent (e.g., weather-checking agent with tool retry loop) | Longest Consecutive Sequence | langgraph_foundations.py |

### Phase 4: Advanced DSA & Enterprise RAG Architectures (Days 32-39)
*Goal: Graph algorithms, DP, intervals alongside RAGFlow deep document parsing, agentic RAG, advanced memory*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 32 | **Corrective RAG (CRAG)** + **Adaptive RAG** + **Multimodal AI Intro**: What is OCR? Bounding boxes, Vision-Language Models, layout-aware document parsing vs naive text extraction | Process a complex PDF using layout-aware chunking. Extract tables and charts using OCR concepts. Build evaluator → web search fallback | Course Schedule | corrective_adaptive_rag.py |
| 33 | **Conversational RAG + Agentic RAG**. Study Ref: NirDiamant/rag_techniques | Chat history injection + agent re-queries + Step-back prompting | Climbing Stairs | conversational_rag.py |
| 34 | **Knowledge Graph Foundations**: What is a knowledge graph? Nodes, edges, properties, Ontology (schema design), Entity Resolution (deduplication), Semantic Relationships + **Temporal Knowledge Graphs**: Bi-temporal data modeling (valid time vs ingestion time) + **Cross-Session Memory**: Mem0 (semantic dedup) + Graphiti (temporal KGs) | Build a simple knowledge graph. Add temporal tracking. Build cross-session memory that tracks preference changes over time | Coin Change | knowledge_graph_memory.py |
| 35 | **DSPy Framework Deep Dive**: What is DSPy? Signatures (input/output contracts), Modules (ChainOfThought, ReAct), optimizers (BootstrapFewShot, MIPROv2). DSPy treats prompts as compiled weights, not handcrafted strings. Wiring LM calls programmatically | Convert a manual prompt chain into DSPy programmatic signatures. Run optimizer to auto-improve prompts | Longest Increasing Subsequence | dspy_deep_dive.py |
| 35B | **LLM-as-a-judge** + Advanced Prompting (Tree of Thoughts, self-consistency) | Build a self-evaluating LLM pipeline that grades own outputs | — | llm_judge.py |
| 36 | **PROJECT 1 BUILD**: Multi-Tenant RAG Agent (using only taught tools — FastAPI, SQLite, LangChain, LangGraph, pgvector via Docker, basic CRAG, Mem0, hybrid search) | FastAPI + SQLite metadata + LangGraph supervisor routing + pgvector hybrid search + CRAG evaluator. Local test | LRU Cache | project1_build/ |
| 37 | **Docker Compose + Cloud Infrastructure**: docker-compose.yml for multi-container setup (app + pgvector + Redis). AWS ECS (ECR, task definitions, IAM roles, Fargate launch type) | Write docker-compose.yml for full stack. Deploy containerized app to AWS ECS Fargate | Task Scheduler | project1_deploy/ |
| 38 | **PROJECT 1 DONE**: Ragas eval report + LLM-as-a-judge regression + **APPLY blitz** (Wellfound + YC applications) | Project 1 as proof. Personalized applications | Min Stack | project1_done/ |
| 39 | **PROJECT 1 FOLLOW-UP**: Buffer day. What are callbacks? Event-driven programming, async hooks + SDLC fundamentals (requirements, architecture, testing types: unit/integration/system). Re-visit weak DSA areas | Respond to recruiter messages. Practice Two Pointers, Sliding Window patterns | Merge Intervals + Insert Interval | interview_followup/ |

### Phase 5: Database Architecture & Advanced SQL (Days 40-46)
*Goal: Master vector index algorithms (FAISS PQ/IVF), tensor-native search (Vespa), serverless vector stores (LanceDB), Redis VSET, Milvus distributed architecture, hybrid search with Elasticsearch ELSER, and multi-tenant vector scaling*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 40 | **Vector Compression Theory**: Sub-space clustering, centroids, hardware datatypes (FP32, FP16, Int8), memory bandwidth + **FAISS**: IndexFlatL2, IndexIVFFlat, Product Quantization (IVF4096,PQ16) | Compress a vector index using Int8 PQ. Measure recall degradation vs memory savings | Kth Largest in Stream | faiss_compression.py |
| 41 | **Late-Interaction Architecture Theory**: ColBERT vs Bi-Encoders vs Cross-Encoders (speed vs recall trade-offs). Token-level embeddings, MaxSim operations + **Vespa**: Tensor-native search, phased ranking profiles | Implement a phased ranking pipeline using token-level interactions for higher recall | K Closest Points to Origin | vespa_colbert.py |
| 42 | **Storage Engine Fundamentals**: Row-oriented vs Columnar memory layouts, Apache Arrow architecture, zero-copy reads + **Cache Eviction Policies**: LRU (Least Recently Used), LFU (Least Frequently Used), TTL (Time-To-Live) + **LanceDB**: S3-backed columnar scaling + **Multi-Tenant Vector Scaling**: Pre-filtering vs post-filtering recall collapse, hnsw.max_scan_tuples | Build a multi-tenant vector store using columnar caching. Implement TTL-based cache eviction. Contrast RAM scaling vs S3-backed | Best Time to Buy/Sell Stock | lancedb_multitenant.py |
| 43 | **Hybrid Search Architectures**: PostgreSQL pgvector + tsvector + RRF + **Elasticsearch ELSER**: Sparse vector retrieval (~30K dims), semantic_text field type, Retriever API fusion | Build hybrid search with pgvector RRF. Implement ELSER. Compare BM25 vs dense vs sparse vs hybrid recall | Trapping Rain Water | hybrid_search_arch.py |
| 44 | **Redis VSET & FT.HYBRID**: Native VSET data type + VSIM for sub-ms similarity. FT.HYBRID with COMBINE RRF vs COMBINE LINEAR. Multi-tier caching strategy. Study Ref: redis/redis, redis-developer/sql-redis | Implement VSIM search. Build FT.HYBRID with RRF and LINEAR. Measure vs two-phase | Largest Rectangle in Histogram | redis_vset.py |
| 45 | **System Performance Metrics**: What is latency? throughput? QPS (queries per second)? RPS (requests per second)? p50/p95/p99 percentiles. How to measure and baseline + **Distributed Systems Architecture**: CAP Theorem, Consistency Levels (Strong/Bounded/Eventual), Sharding, Replication + **Milvus**: Knowhere, Proxy/QueryNode/IndexNode, GuaranteeTs, Clustering Compaction | Deploy and configure clustered Milvus. Measure read latency and throughput under different consistency settings. Record p50/p95 | Course Schedule II | milvus_distributed.py |
| 46 | **AI Security Fundamentals**: Adversarial prompt injection, Jailbreaks, Prompt leaking + **NeMo Guardrails**: Colang for topical bounding, jailbreak detection + **Agno dual-schema** + **Ollama** local deployment | Implement semantic routing firewall. Block malicious prompts before reaching LLM. Deploy guarded agent | Trapping Rain Water review | security_guardrails.py |

### Phase 6: AI Infrastructure & Production MLOps (Days 47-56)
*Goal: Master inference optimization, caching, feature stores, model registries, CI/CD for AI, observability, streaming architectures, and mock interviews*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 47 | **Networking Fundamentals**: Network sockets, TCP vs UDP, connection lifecycle + **Concurrency vs Parallelism**: Threading, multiprocessing, async IO, GIL limitations + **Advanced Protocols**: WebSockets (persistent bi-directional TCP), Protocol Buffers (protobuf schema definitions), HTTP/2 multiplexing + **gRPC Streaming**: bidirectional streaming for token delivery | Build a high-throughput persistent bi-directional streaming connection for real-time token delivery. Compare sync vs async throughput | Find Min Rotated + Search in Rotated Array | streaming_protocols.py |
| 48 | **Version Control Fundamentals**: Git (commits, branches, remotes) + **Data Versioning**: DVC (tracking datasets alongside code) + **Model Registries**: MLflow (experiment tracking, artifact storage) + **Feature Stores**: Feast/Tecton (offline batch + online streaming, point-in-time joins) + **Prompt Management**: DSPy compilation, Vellum | Initialize Git repo. Track dataset with DVC. Log model hyperparameters via MLflow. Build feature store dual-pipeline | Subsets | mlops_git_dvc.py |
| 49 | **JSON-RPC 2.0 Fundamentals**: Request/Response structure, method calls, params + **Webhooks**: What is a webhook? Event payloads, reverse API, push vs pull + **Cybersecurity Basics**: PKI, TLS handshakes, Symmetric vs Asymmetric encryption, Certificate Authorities + **OAuth 2.1**: Grant flows, JWTs, scopes + **MCP**: Host/Client/Server, Tools/Resources/Prompts, Threat models (Confused Deputy, mTLS, tool output sanitization) | Build first MCP server exposing one tool. Add mTLS + OAuth 2.1 token exchange. Design monitoring dashboard | Serialize/Deserialize Tree | mcp_security.py |
| 50 | **OS Memory Management**: Virtual vs Physical memory, paging, non-contiguous block allocation + **Process Management**: Preemption, Scheduling (context switching, time slices, priority queues) + **GPU Architecture**: VRAM, memory bandwidth, Streaming Multiprocessors, fragmentation + **vLLM**: PagedAttention (logical KV → physical GPU pages), Continuous batching, Token-aware rate limiting (Sliding Window Log, Token Bucket) + **Multi-Tenant Caching**: Silo/Pool/Bridge models, tenant-aware Redis | Deploy vLLM. Analyze KV cache fragmentation reduction. Implement Sliding Window Log rate limiter. Build tenant-aware cache | Word Ladder | vllm_inference.py |
| 51 | **Ontology Design**: POLE+O (Person, Org, Location, Event, Object) architecture, data modeling for Knowledge Graphs + **Memory Decay Theory**: Ebbinghaus forgetting curve, temporal weighting formulas + **Tripartite Agent Memory**: Cognee (graph-native), Neo4j (Short/Long/Reasoning), Graphiti (bi-temporal), AgentMemory (MCP-integrated procedural memory) | Build extraction pipeline: observations → POLE+O graph → Long-Term memory with temporal decay provenance. Implement forgetting curve | Permutations | tripartite_memory.py |
| 52-56 | **System Design Crash Course**: Load Balancing, Reverse Proxies, Horizontal vs Vertical Scaling, Message Queues (Kafka/RabbitMQ), Event-driven design + **Mock Interviews** (Verbal Theory, Pair Programming, Whiteboarding, Behavioral, Take-Home) | Practice designing scalable, high-availability agentic architectures. 5 mock days covering all formats | Combination Sum → Course Schedule II review | mock_week/ |

### Phase 7: Agentic Orchestration, MCP & Advanced Tools (Days 57-60)
*Goal: Final capstone polish, apply blitz, offer evaluation*

### Phase 7: Agentic Orchestration, MCP & Advanced Tools (Days 57-60)
*Goal: Master advanced agent patterns, infrastructure integrations, then build capstone. Final apply blitz.*

| Day | Morning (2hr) | Afternoon (2hr) | Evening DSA (1hr) | Deliverable |
|-----|--------------|-----------------|-------------------|------------|
| 57 | **Advanced Agent Patterns**: Self-reflection loops, multi-tool use, hierarchical planning, multi-agent debate. **Multi-Agent Orchestration Comparison**: LangGraph (stateful production) vs CrewAI (rapid role-based) vs AutoGen (conversational debate). **Protocol Design — A2A vs MCP**: Horizontal agent delegation (A2A — JSON-RPC 2.0, Agent Cards, capability discovery) vs vertical tool integration (MCP). Blended architectures | Build self-reflecting agent. Compare framework topologies. Implement A2A card discovery + MCP tool call in same system | Implement Trie (Prefix Tree) | agent_patterns_a2a.py |
| 58 | **Advanced Infrastructure Integrations**: **Blackboard Architecture** (shared-memory event loops, knowledge source triggers, conflict resolution for multi-agent coordination). **MicroVM Sandboxing via Daytona** (SDK lifecycle management, warm starts, snapshots). **Web Scraping Theory** (DOM elements, headless browsers, markdown extraction) via Firecrawl. **Context Compression via Headroom** (CCR pattern, local proxy interception, token reduction) | Build individual practice modules: (1) Blackboard namespace with two agents writing/reading. (2) Daytona sandbox executing safe Python. (3) Firecrawl scrape → markdown. (4) Headroom compression pipeline | Time Based Key-Value Store | infra_integrations.py |
| 59 | **PROJECT 2 BUILD**: Autonomous Code & Web Intelligence Swarm — Assemble all infra components: Blackboard + Researcher (browser-use + Firecrawl) + Coder (Daytona) + Tripartite Memory (Neo4j/Cognee POLE+O) + MCP OAuth 2.1 + Headroom compression + Docker + CI/CD | Build and integrate the full swarm. Implement MCP Sampling + Claude Code acceleration | Largest Rectangle in Histogram | project2_build/ |
| 60 | **PROJECT 2 DONE**: LLM-as-a-judge regression + Deploy + README with architecture diagrams + **APPLY BLITZ**: Wellfound (20) + YC (10) + LinkedIn DMs (10) | Production-grade project with docs. Personalized messages with both projects | Course Schedule II review | project2_done/ |

---

### Phase 8: Scalable Agentic System Design (Post-60-Day — Interview Deep Dive)
*Goal: Master distributed systems for AI, advanced rate limiting, A2A/MCP protocol architectures, disaster recovery, and system design interview frameworks. Study these topics after securing interviews.*

| Topic | Morning (2hr) | Afternoon (2hr) | Key Deliverable |
|-------|--------------|-----------------|-----------------|
| **Distributed Systems Fundamentals for AI** | CAP Theorem and Eventual Consistency for distributed agent memory and vector replication. Message Queues (Kafka/RabbitMQ) for background inference tasks and document ingestion | Circuit Breakers and Retry Logic for fault-tolerant LLM API gateways. Idempotency in Agent Actions (preventing double-execution of tool calls during retries) | distributed_systems_ai.md |
| **Advanced Rate Limiting & Load Balancing** | Token Bucket vs Leaky Bucket vs Sliding Window Log (memory cost, fairness, burst tolerance). Load balancing for inference servers (round-robin, least connections, request routing) | Model Routing vs Single Frontier Model — latency vs cost trade-offs. Token-aware rate limiting for GPU concurrency | rate_limiting_models.md |
| **Protocol Architecture Deep Dive** | A2A Protocol: Agent Cards, capability discovery, JSON-RPC 2.0, multi-part modal messages, stateful long-running tasks. MCP: Roots, Sampling, streaming tools, subscriptions | Blended architectures: orchestrator uses A2A for horizontal delegation, workers use MCP for vertical tool access. Security: mTLS, sender-constrained tokens | protocol_architecture.md |
| **Multi-Tenant AI Platform Design** | Silo/Pool/Bridge isolation models. Tenant-aware caching (namespace isolation, prevent cross-tenant leakage). Row-level security in pgvector. Tenant-specific LoRA adapters | Capacity planning: memory footprint for HNSW at scale, peak QPS calculations, back-of-envelope estimations for interviews | multi_tenant_design.md |
| **Disaster Recovery & Failover** | Multi-region deployment for AI systems. Database replication strategies. Agent state recovery after crashes. Handling LLM API provider outages (fallback models) | Designing for graceful degradation: cache fallbacks, model fallback chains, degraded response strategies | dr_failover.md |
| **System Design Mock I** | Full mock: "Design a RAG system for 10M QPD with multi-modal data" | Full mock: "Design a secure multi-agent system with A2A + MCP" | system_design_mock_1.md |
| **System Design Mock II** | Full mock: "Design an LLM inference serving platform for 500 concurrent users" | Full mock: "Design a feature store for real-time recommendations (50ms p99)" | system_design_mock_2.md |

---

## 📋 2 Projects to Build (Market-Aligned) — Architecture Documentation Requirements

### Project 1 (Days 29-31): Multi-Tenant Enterprise Knowledge Agent
**Tech Stack:** FastAPI + pgvector (RLS) + **pgvectorscale (DiskANN)** + LangGraph + MCP + Mem0 + Graphiti + Cross-encoder + Hybrid Search + Docker + AWS ECS + LangSmith/Ragas
**Features:**
- Agno-style dual-schema architecture: read-only transaction scopes for data-analyst agents, isolated schema for engineer agents
- JWT-based RBAC for strict multi-tenant isolation
- **pgvectorscale StreamingDiskANN** for handling 10M+ document chunks on SSDs without RAM exhaustion
- **Hybrid Search with RRF**: BM25 + pgvector + tsvector fused via Reciprocal Rank Fusion
- **Metadata pre-filtering**: iterative index scans (hnsw.max_scan_tuples) to prevent recall collapse under multi-tenant constraints
- Temporal Knowledge Graphs (Graphiti) for relational entity tracking over time
- Mem0 for user-scoped semantic memory with automated fact deduplication and contradiction resolution
- Corrective RAG (CRAG) with evaluator → web search fallback
- Comprehensive Ragas evaluation + LLM-as-a-judge regression testing
- **Interview signal:** "Hire me" — shows architectural maturity, security awareness, and production thinking at billion-vector scale

### Project 2 (Days 54-56): Autonomous Code & Web Intelligence Swarm
**Tech Stack:** FastAPI + LangGraph (Blackboard pattern) + browser-use + Firecrawl + Daytona + MCP (OAuth 2.1) + Next.js/TypeScript + **Neo4j/Cognee tripartite memory** + Docker + AWS ECS + GitHub Actions
**Features:**
- **Blackboard shared-memory architecture** with optimistic locking — agents write to namespaces (research/, code/) with thread-safe locks, maintain private scratchpads
- **Researcher Agent**: browser-use + Playwright for visual DOM understanding, multi-tab SPA navigation; Firecrawl for LLM-ready markdown extraction and anti-bot bypass
- **Coder Agent**: executes Python data-transformation workflows strictly inside isolated, ephemeral Daytona sandboxes (dedicated kernel, network isolation)
- **Tripartite Agent Memory via Neo4j/Cognee**: Short-Term (conversational state), Long-Term (POLE+O knowledge graph with bi-temporal provenance), Reasoning (decision trace history)
- **Temporal decay function** applied to short-term conversations; Ebbinghaus forgetting curves via AgentMemory MCP hooks
- **MCP servers secured via OAuth 2.1** — token exchange, no token passthrough, per-client consent registries
- **LLM-as-a-judge regression testing** — catches infinite tool-calling loops, context drift, silent failures
- Full CI/CD pipeline (push → test → eval → deploy) + cost tracking middleware
- **Interview signal:** "Full-stack AI Engineer" — end-to-end delivery with enterprise security, tripartite memory, and temporal decay

### 📐 Project 1 — Architecture Documentation Requirements
The README MUST include:
- **Component Diagram**: Visually mapping ingestion pipeline (parsers, embedding models), storage layer (vector DB, object storage), and serving layer (API gateway, LLM)
- **Data Flow Definition**: Point-in-time consistency strategies, handling late-arriving events
- **Capacity Planning**: Back-of-envelope calculations for memory footprint (RAM for 1M vectors in HNSW) and peak QPS throughput
- **Tenant Isolation Strategy**: Row-level security implementation, tenant-aware cache key design

### 📐 Project 2 — Architecture Documentation Requirements
The README MUST include:
- **State Machine Diagram**: Node transitions, conditional edges, HITL checkpoints using standard flowchart notation
- **Protocol Specifications**: Which interactions use A2A (horizontal negotiation) vs MCP (vertical tool execution)
- **Security Threat Model**: Mitigations for prompt injection, ambient authority escalation, cross-tenant data leakage in agent logs
- **CI/CD Pipeline Design**: Token-budget regression tests, deterministic evaluation gates for automated deployment

---

## 🎯 Application Strategy

| Milestone | When | Where | What to Show |
|-----------|------|-------|-------------|
| **Internship apply blitz** | Day 31 | Wellfound + YC Work at a Startup | Project 1 deployed + GitHub profile |
| Ongoing applications | Days 32-56 | LinkedIn DMs + X (Twitter) DMs | Projects + technical content |
| **FT apply blitz** | Day 57 | Wellfound + YC + LinkedIn | Both projects deployed + full tech stack |
| Offer evaluation | Day 59-60 | Compare CTC vs cash vs equity | Market research benchmarks |

---

## 🚫 What We're Skipping (Research-Validated)

| 🚫 Skip / Reinstated | What Changed |
|--------------|----------------|
| Training CNNs/RNNs from scratch | Still skip — zero JD mentions. Pre-trained models via APIs is the standard |
| Deep ML math (backpropagation derivation) | Still skip — not tested in AI Engineer interviews |
| Django / Flask | Still skip — FastAPI has near-total dominance in AI engineering |
| Pandas/NumPy as full week | Still skip — moved to 1-day Good-to-Have |
| Apna.co as primary platform | Still skip — low signal, legacy IT, fake AI listings |
| **Coin Change, LIS, Word Ladder, Trapping Rain Water, Largest Rectangle** | **REINSTATED** — per Noida tech hub interview data (Adobe, Microsoft). DP for RL state-space, monotonic stack for production optimization, BFS for graph routing |
| **Naive RAG (fixed-size chunking)** | Still skip — replaced by Proposition Generation, Step-back, GraphRAG |
| **InMemorySaver for LangGraph** | Still skip — restricted to testing only. PostgresSaver mandatory |
| **Static API keys for MCP** | Still skip — OWASP MCP Top 10 vulnerability. OAuth 2.1 mandatory |
| **Manual prompt engineering as primary skill** | Still skip — replaced by DSPy + GEPA |
| **ChromaDB for production** | Downgraded to prototype-only. Use pgvector/DiskANN for production |

---

## 📊 Compensation Targets (Research-Validated)

| Milestone | Target | Evidence |
|-----------|--------|----------|
| Internship | ₹30-50k/mo | Hungama (₹50k), Aight (₹25-50k), SuperKalam (₹25-40k), Peakflo (₹40-50k) |
| India FT | ₹10-12 LPA (₹80k-₹1L/mo in-hand) | Hungama PPO ₹12-15 LPA, market median ₹9-11 LPA |
| Global Remote FT | $24k-$40k/yr (₹20L-₹34L/yr) | Smart Audit ($25-50k/yr), Great Question, Peakflo |


---

## 🏗️ Portfolio Spec: ₹30k vs ₹80k Level

### ₹30k Intern Level (Day 28)
- Basic RAG pipeline with LangChain + basic vector DB
- Manual testing, basic error handling
- Simple README with install + run instructions

### ₹80k FT Level (Day 60) — "Enterprise Orchestrator"
- **LangGraph** with dual-channel memory, **PostgresSaver**, **Send API**, **interrupt()** HITL pattern
- **MCP Server** with **OAuth 2.1**, **Sampling**, **Roots**
- **CrewAI** for rapid role-based prototyping
- **CI/CD pipeline** with LLM-as-a-judge: fail build if infinite loops, faithfulness < 0.85, context drift > 15%
- **Tripartite Agent Memory**: Neo4j/Cognee (Short/Long/Reasoning), POLE+O extraction, Ebbinghaus temporal decay
- **browser-use** + **Firecrawl** for web automation
- **Daytona sandbox** for safe code execution
- **RAGFlow DeepDoc** for enterprise document parsing
- **Ollama** for privacy-preserving local LLM
- **Claude Code** agentic coding acceleration
- **OpenClaw** local agent gateway
- **Headroom** token compression (60-95%)
- **Guardrails** + **NeMo** + **AgentShield** for security
- **Redis VSET/FT.HYBRID** semantic caching + agent state
- **pgvectorscale DiskANN** for billion-scale vector search
- **tsvector + pgvector + RRF** hybrid search
- **README** with: Mermaid.js architecture diagram, documented trade-offs ("Why pgvector over Pinecone"), quantitative metrics (p50/p95 latency, Faithfulness/Context Precision via Ragas)

### 📖 Narrative Architecture: "Tell Me About Yourself"
**Optimal Structure:** "I am an AI Engineer focused on bridging the gap between raw LLM capabilities and production-grade applications. While my foundation is in full-stack engineering, I've spent the last year specializing in Agentic workflows — specifically building stateful applications using LangGraph and standardizing external tool integrations via the Model Context Protocol. I thrive in high-velocity startup environments where I can own the entire architecture, from the data ingestion pipeline to the final streaming inference endpoint."

### 📖 Termination Narrative
**Optimal Structure:** "My previous role provided an excellent foundation in robust backend systems, but the company's trajectory moved away from deep AI integration. I am targeting seed-to-Series-B startups because I want to be closer to the architectural decision-making process, specifically involving generative AI, multi-agent infrastructure, and RAG optimization."

### 📖 Wellfound Profile Optimization
- **Headline:** "AI Engineer | LangGraph, MCP, & RAG Architecture | Building Stateful AI Systems"
- **Skills:** Python, FastAPI, LangGraph, Model Context Protocol, Vector Databases (Qdrant/Milvus), PostgreSQL, TypeScript
- **Project Descriptions:** Quantifiable metrics — "Reduced context latency by 40% via Redis semantic caching"

---

## 🎯 AI-Specific DSA Strategy

### Mock Interview Framework (1-Hour Structure)
| Time | Phase | Objective |
|------|-------|-----------|
| 00:00-05:00 | Constraint Identification | Clarify boundaries: data types, edge cases, memory limits ("Are edges guaranteed to form a DAG?") |
| 05:00-15:00 | Architectural Proposal | Propose brute-force baseline Big-O, immediately pivot to optimized approach (e.g., identify overlapping subproblems → memoization) |
| 15:00-45:00 | Implementation | Write code with continuous vocalization. Silence = failure. Explain each block's logic as written |
| 45:00-60:00 | Validation & Optimization | Manual dry-run on edge-case input. Discuss space complexity optimizations |

### Handling Unseen Problems (Communication Protocol)
**Script:** "I haven't encountered this exact formulation, but the structural constraints map closely to [Pattern X — e.g., Topological Sort or BFS]. Let me outline the base case for the recursion tree, and we can identify how to prune the state space efficiently."

### Top 10 High-Frequency DSA Problems for AI Engineering
| Problem | Pattern | AI Engineering Relevance |
|---------|---------|--------------------------|
| Serialize/Deserialize N-ary Tree | Tree Traversal | State checkpoints, saving agent execution graphs to databases |
| LRU Cache | Linked List + Hash | KV caching in Transformer architectures |
| Course Schedule I/II | Topological Sort (Graph) | Dependency resolution in multi-agent workflows |
| Design Add and Search Words | Trie | Prompt prefix matching, structured decoding |
| Merge Intervals | Array / Sorting | Time-series log analysis, token boundary alignment |
| Find Median from Data Stream | Heap / Priority Queue | Dynamic latency calculations in concurrent API gateways |
| Word Ladder | BFS | Optimal pathfinding, state-space search in multi-step AI planning |
| Clone Graph | Graph Traversal | Deep-copying complex state objects without reference mutation |
| K Closest Points to Origin | Heap / Sorting | Exact and approximate nearest neighbor (ANN) vector search |
| Design Hit Counter | Sliding Window / Queue | API rate limiters and token bucket algorithms in LLM gateways |

### Spaced Repetition Protocol
- Starting Day 25: Mandatory **15-minute daily flashcard review** of the Interview Question Bank (see vs_code_context.md)
- Continue indefinitely through Day 60

---

## 🎯 Advanced Theory Focus Areas (Phase 3 Supplement)

### Chip Huyen's DMLS Integration
- Skip chapters on basic tabular feature engineering
- Concentrate on: Data Distribution Shifts, Evaluation Protocols (Offline vs Online metrics), Model Deployment Strategies (Canary vs Shadow)

### Autograd & Deep Learning Fundamentals
- Deep learning frameworks = 3 operation types: elementwise, reductions (aggregations like SUM), movement (tensor reshaping)
- Master: reverse-mode automatic differentiation — computation graphs traversed backward to compute gradients via chain rule ($\frac{\partial L}{\partial x} = \frac{\partial L}{\partial y} \cdot \frac{\partial y}{\partial x}$)

### Essential Research Papers for Interview Defense
- **Attention Is All You Need**: Exact matrix operations for self-attention. Why scores are scaled by $\sqrt{d_k}$ (pushes softmax out of near-zero gradient regions)
- **DeepSeek-V3 Technical Report**: FP8 mixed precision training, MTP for speculative decoding, MLA for KV cache bottleneck
- **InstructGPT / RLHF**: SFT → Reward Model → PPO pipeline

### Hands-On Translation
- LoRA/QLoRA exercises → link to VRAM constraint interview answers. Articulate how PEFT drastically reduces optimizer state memory

---

## 📚 Study References (Curated Repos — Integrated into Daily Plan)

---

## 📚 Study References (Curated Repos — Integrated into Daily Plan)

| Repository | Phase/Day | What to Study |
|-----------|-----------|---------------|
| facebookresearch/faiss | Phase 5 Day 43 | Index algorithm comparison: IVF, HNSW, PQ, IVF+HNSW hybrid |
| nmslib/nmslib | Phase 5 Day 43 | Non-metric space library, HNSW variants, benchmark comparisons |
| deepseek-ai/DeepSeek-V3 | Phase 3 Day 29 | MLA architecture, MoE routing, Multi-Token Prediction internals |
| trekhleb/homemade-machine-learning | Phase 3 Day 25 | Math foundations, classical ML implementations from scratch |
| scikit-learn/scikit-learn | Phase 3 Day 26 | Classical ML: Logistic Regression, Random Forest, XGBoost, K-Means, PCA |
| karpathy/minGPT | Phase 3 Day 28 | Minimal transformer implementation, attention mechanics |
| infiniflow/ragflow | Phase 4 Day 32 | DeepDoc layout-aware parsing, visual RAG pipeline |
| crewAIInc/crewAI | Phase 7 Day 54 | Role-based agent assembly, task delegation, process flows |
| ollama/ollama | Phase 5 Day 45 | Local LLM deployment, API serving, model management |
| anthropics/claude-code | Phase 7 Day 56 | Agentic coding, CLAUDE.md context injection, MCP connectivity |
| openclaw/openclaw | Phase 7 Day 57 | Local agent gateway, AGENTS.md/SOUL.md workspace state management |
| headroomlabs-ai/headroom | Phase 7 Day 58 | ContentRouter/SmartCrusher token compression algorithms |
| addyosmani/agent-skills | Phase 7 Day 57 | Reusable agent skill patterns, workflow packaging |
| n8n-io/n8n | Phase 7 Day 55 | Visual AI workflow automation, rapid prototyping |
| langflow-ai/langflow | Phase 7 Day 55 | Drag-and-drop agent builder for stakeholder demos |
| langgenius/dify | Phase 7 Day 55 | Full-stack AI app platform, rapid prototyping |
| open-webui/open-webui | Phase 7 Day 54 | Self-hosted ChatGPT alternative for local testing |
| google-gemini/gemini-cli | Phase 7 Day 54 | CLI-based agent interaction for DevTools workflows |
| williamfiset/Algorithms | Phase 1-2 | Foundational DSA implementations, graph algorithms |
| jwasham/coding-interview-university | Phase 1-2 | Comprehensive DSA study roadmap |
| ed-donner/agents | Phase 7 Day 54 | Week 4: LangGraph multi-agent routing templates |
| NirDiamant/Agent_Memory_Techniques | Phase 4 Day 34 | Notebooks 24-27: Mem0, Graphiti, Procedural Memory |
| NirDiamant/rag_techniques | Phase 4 Day 33 | Proposition Generation, Step-back Prompting patterns |
| NirDiamant/GenAI_Agents | Phase 7 Day 54 | Agent architectures, tool-use patterns, multi-agent patterns |
| punkpeye/awesome-mcp-servers | Phase 7 Day 56 | Real-world MCP server implementations, OAuth 2.1 integrations |
| modelcontextprotocol/servers | Phase 7 Day 56 | Canonical MCP reference implementations |
| OpenBMB/ToolBench | Phase 7 Day 54 | DFSDT algorithm, ToolEval metrics |
| firecrawl/firecrawl-workflows | Phase 7 Day 55 | Outcome-focused business skills for agents |
| EthicalML/awesome-production-agentic-systems | Phase 6 Day 48 | CI/CD, AIBOM, observability tooling |
| openai/openai-agents-python | Phase 7 Day 54 | Agent handoffs, manager pattern, voice streaming |
| browser-use/browser-use | Phase 7 Day 55 | Visual DOM, multi-tab navigation, Playwright |
| daytonaio/daytona | Phase 7 Day 55 | Python SDK for sandbox creation, ephemeral execution |
| guardrails-ai/guardrails | Phase 5 Day 46 | Input/output validators, PII detection, schema compliance |
| agno-agi/agno | Phase 5 Day 45 | Dual schema enforcement, JWT-based RBAC patterns |
| ashishps1/learn-ai-engineering | Phase 6 | System design interview prep, architecture blueprints |
| Shubhamsaboo/awesome-llm-apps | Phase 4 | Real-world LLM application patterns, RAG variants |
| NousResearch/hermes-agent | Phase 1 Day 17 | DSPy + GEPA integration patterns for prompt evolution |
| **donnemartin/system-design-primer** | **Phase 8** | Rate limiting algorithms, load balancing, cache eviction policies — map to vLLM/Semantic Caching |
| **a2aproject/A2A** | **Phase 7 Day 54** | Agent-to-Agent protocol: Agent Cards, capability discovery, JSON-RPC 2.0 |
| **FareedKhan-dev/all-agentic-architectures** | **Phase 7 Day 54** | 35 agent patterns (Reflexion, LATS, Meta-Controller). Implement deterministic-picker pattern |
| **alirezadir/Agentic-AI-Systems** | **Phase 7 Day 54** | Multi-agent state management and reasoning loops chapter mapping |
| **iusztinpaul/designing-real-world-ai-agents-workshop** | **Phase 7 Day 57** | End-to-end Deep Research Agent as MCP server using FastMCP + Opik evaluations |
| **NirDiamant/agents-towards-production** | **Phase 7 Day 58** | Docker deployment, PII sanitization pipelines, security guardrails for capstone |
| **omBharatiya/ai-system-design-guide** | **Phase 6, Phase 8** | AI system design interview questions and architecture blueprints |
| **labuladong/fucking-algorithm** | **Phase 1-2** | DSA problem-solving frameworks, pattern-based algorithm mastery |
| **binhnguyennus/awesome-scalability** | **Phase 8** | Scalability patterns, system design interview prep for high-throughput systems |
| **KalyanKS-NLP/LLM-Interview-Questions** | **Phase 3, Phase 6** | LLM interview questions with answers, theory deep dives |
| **ombharatiya/AI-Engineer-Interview-Questions** | **Phase 6** | AI Engineer specific interview questions compilation |
| **chiphuyen/dmls-book** | **Phase 3** | Designing Machine Learning Systems — production ML patterns |
| **HandsOnLLM/Hands-On-Large-Language-Models** | **Phase 3, Phase 4** | Practical LLM exercises that translate to interview answers |
| **mli/paper-reading** | **Phase 3 Day 28-29** | Key papers to study: Attention Is All You Need, DeepSeek-V3, etc. |

---

## 🏛️ Design Patterns for AI Engineers

| Pattern | When to Use |
|---------|-------------|
| **ReAct** (Reason + Act) | Exploratory tasks with dynamic API interaction |
| **Plan-and-Execute** | Complex long-horizon tasks needing decomposition |
| **Evaluator-Optimizer** | Code generation, data extraction requiring high accuracy |
| **Tool-Use** | Structured data extraction with function calling |
| **Multi-Agent (Supervisor)** | Multiple specialized agents routed by a central LLM |
| **MCP Integration** | Secure enterprise tool access via OAuth 2.1, no hardcoded APIs |
| **Agentic RAG** | Dynamic retrieval where agent rewrites queries if results poor |
| **Blackboard System** | Multi-agent shared memory with namespaces, optimistic locking, private scratchpads |
| **Dual Schema Enforcement** | Read-only transaction scopes for data agents, isolated schemas for engineer agents |
| **Send API Fan-out** | Parallel dispatch to multiple specialist agents from a single supervisor |
| **Hash-based Idempotent Recompute** | Skip redundant LLM calls by caching outputs keyed by input hash |
| **Procedural Memory** | Extract parameterized workflow templates from successful execution traces |

---

## 🛡️ Post-2-Month Roadmap

| Phase | Months | Salary Target | Focus |
|-------|--------|---------------|-------|
| Months 3-6 | Jul-Oct | ₹1-1.5L/mo | Open source (LangChain, MCP), fine-tuning (LoRA/QLoRA), advanced MLOps |
| Months 6-12 | Oct-Mar | ₹2L+/mo | Distributed systems, Kafka, multi-modal AI, vLLM/TensorRT-LLM inference serving |

---

## 📚 Interview Q Bank (25 questions)
[Included in full plan — LLM/RAG, LangGraph, MCP, System Design, ML/NLP, Production Patterns]

## 🚨 Risk Mitigation
| Risk | Mitigation |
|------|-----------|
| DSA deficit | 1hr/day every single day. 30-50 targeted problems. |
| Terminated internship | Frame as "backend vs AI misalignment." Control narrative early. |
| Tutorial Hell | Unique problem + live deploy + eval scores + architecture docs. |
| Application black holes | Apna (chat), Wellfound (founder DMs). Skip traditional portals. |

---

*Based on Gemini Deep Research: Architecting the Agentic AI Engineer (Jul 2026)*
