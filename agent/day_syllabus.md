# 📋 Day Syllabus — Live Tracker

**Purpose:** Tracks what was actually taught each day. Always check this before generating a prompt. Never assume. Never guess.

---

## ✅ Completed Days

| Day | Date | Topics Covered | DSA Problems | Total DSA |
|-----|------|---------------|-------------|-----------|
| 1 | Jun 22 | Variables, data types, input(), print(), arithmetic, calculator | Algorithm, O(1), O(n) | 0 |
| 2 | Jun 22 | Comparisons, if/elif/else, booleans, login checker | Decision trees | 0 |
| 3 | Jun 24 | Logical operators (and/or/not), nested conditions, login validation | — | 0 |
| 4 | Jun 25 | while loops, break, continue, retry logic, menu-driven app | — | 0 |
| 5 | Jun 30 | for loops, range(), string iteration, accumulator pattern | — | 0 |
| 6 | Jun 30 | Functions (def, params, return, default params) | — | 0 |
| 7 | Jul 1 | Lists (indexing, append, pop, remove, insert, len, iteration, sum manually, max manually, Todo app) | — | 0 |
| 8 | Jul 1 | List slicing, list comprehensions, membership (in/not in), dicts (get, keys, values, items, update), list of dicts, linear search, Contact Book | Linear Search (O(n), O(1)) | 0 |
| 9 | Jul 4 | Exception handling (try/except/else/finally, ValueError, ZeroDivisionError, KeyError), *args, **kwargs, lambda, map(), filter(), program organization, dispatch table, Calculator 2.0 | Big O review (O(1), O(n), O(n²)) | 0 |
| 10 | Jul 11 | File I/O (open, read, write, with, readlines, append, modes, FileNotFoundError), Sets (add, remove, discard, union, intersection, membership), Two Sum (brute O(n²) + optimized O(n) with hash map) | Two Sum (LeetCode #1) | 1 |
| 11 | Jul 14 | **OOP: classes, objects, __init__, self, object attributes, methods, inheritance, pass, method overriding** | Two Sum (review) | 1 |

---

## 🔄 Current Day

| Day | Date | Status | Topics | DSA |
|-----|------|--------|--------|-----|
| 12 | Jul 17 | 🔴 IN PROGRESS | Context Managers, Modules, `__init__.py` | Valid Anagram |

---

## 📅 Upcoming (Market-Validated — All Concepts, No Skipping)

### Phase 1: Python Completion + LLM APIs (Days 11-17)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 11 | OOP: classes, inheritance, dunder, @property, @staticmethod, @classmethod | Build mock VectorStore class | Two Sum |
| 12 | Context Managers, Modules, __init__.py | Safe File I/O Manager + Package | Valid Anagram |
| 13 | Async: asyncio, event loop, gather + **FastAPI intro** | Build first FastAPI endpoint | Group Anagrams |
| 14 | Generators (yield), Tuples, enumerate, zip | Streaming token generator | Top K Frequent |
| 15 | String methods, JSON module | Parse nested JSON LLM outputs | Product of Array |
| 16 | LLM APIs: OpenAI/Gemini, temperature, tokens, streaming | Chat + streaming response | Valid Palindrome |
| 17 | Prompt Engineering: few-shot, CoT, system prompts | Test personas | 3Sum |

### Phase 2: LangChain + RAG Core (Days 18-24)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 18 | FastAPI SSE Streaming + Pydantic, Constrained Decoding (XGrammar) | Build streaming endpoint + guaranteed JSON | Container With Most Water + Two Sum II |
| 19 | Document Loaders, Text Splitters, **Semantic Chunking** | Parse PDF by semantic boundaries | Longest Substring |
| 20 | Vector DBs, Embeddings, ChromaDB | Store chunks + similarity search | Valid Parentheses |
| 21 | **Naive RAG**: chunk → embed → store → retrieve → generate | End-to-end RAG script | Binary Search |
| 22 | **SQL + pgvector basics**: SELECT, INSERT, JOINs, vector columns | Store embeddings in PostgreSQL | Search 2D Matrix |
| 23 | **Parent-Child Chunking + Cross-Encoder Reranking** | Rerank top-20 → top-3 with BGE | Reverse Linked List |
| 24 | **Hybrid Search**: BM25 + Dense, pgvector HNSW vs IVFFlat | Implement hybrid search + index tuning | Merge Two Sorted |

### Phase 3: Advanced RAG + Evaluation + Project 1 (Days 25-31)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 25 | **Corrective RAG (CRAG)** + **Adaptive RAG** | Evaluator → web fallback + router | Reorder List |
| 26 | **Conversational RAG + Agentic RAG** | Chat history + agent re-queries | Max Depth Tree |
| 27 | **LangSmith + Langfuse + Ragas Eval**: Faithfulness, Context Precision, Answer Relevancy | Golden dataset + eval pipeline + observability | Validate BST |
| 28 | **PROJECT 1**: Multi-Tenant RAG System (FastAPI + pgvector + LangGraph + MCP) | Build core features | Invert Tree |
| 29 | Project 1: Docker containerize + Cross-encoder + Hybrid Search + Constrained Decoding | Complete features + eval | LCA of BST |
| 30 | Project 1: Deploy to AWS ECS + Ragas eval + SSE streaming | Deploy + apply ready | Level Order Traversal |
| 31 | **Project 1 DONE + APPLY BLITZ** | Wellfound + YC apps | Longest Consecutive Sequence |

### Phase 4: LangGraph Mastery + MCP (Days 32-39)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 32 | LangGraph: StateGraph, Nodes, Edges, State | Linear 3-node state machine | Course Schedule |
| 33 | LangGraph: Reducers, add_messages, Conditional Routing + **DFSDT Concept** | Chatbot with memory + DFSDT tool planning | Climbing Stairs |
| 34 | LangGraph: Checkpointing, Human-in-the-loop | Approval interrupt before tools | LRU Cache |
| 35 | LangGraph: Multi-agent Supervisor Pattern | Supervisor → 2 workers | Task Scheduler |
| 36 | LangSmith Tracing for LangGraph | Instrument multi-agent | Min Stack |
| 37 | MCP: Host/Client/Server, stdio transport | Python MCP server with tools | Merge Intervals |
| 38 | MCP: HTTP SSE, JSON-RPC 2.0, Tools vs Resources vs Prompts | DB schema as MCP Resource | Insert Interval |
| 39 | **LangGraph + MCP Integration** | Agent discovers MCP tools | Course Schedule II |

### Phase 5: Full-Stack + Production Patterns (Days 40-46)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 40 | FastAPI Deep Dive: error handling, middleware, streaming, SSE, **Guardrails** for LLM output safety (PII, toxicity, schema) | Production FastAPI app with safety guards | Kth Largest in a Stream |
| 41 | **vLLM Inference**: PagedAttention, continuous batching, TP, KV cache | Deploy model with vLLM | K Closest Points to Origin |
| 42 | **Redis Semantic Caching**: embeddings, cosine threshold 0.85-0.95, hybrid metadata filters | Build semantic cache layer | Best Time to Buy/Sell Stock |
| 43 | **Next.js + TypeScript** with SSE streaming from FastAPI | Chat UI with real-time streaming | Longest Repeating Char Replacement |
| 44 | **AWS ECS**: Deploy full stack (Fargate + RDS + Load Balancer) | Cloud deployment | Linked List Cycle |
| 45 | **GitHub Actions CI/CD**: Auto-test, auto-eval, auto-deploy | Push → test → deploy pipeline | 3Sum review |
| 46 | Cost tracking + Prompt versioning + A/B testing | Metadata wrapper + toggle | Min Window Substring |

### Phase 6: System Design + Interview Prep (Days 47-53)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 47 | System Design: RAG at scale, semantic caching, hybrid metadata filtering, Redis tuning | 1M QPD architecture | Find Min Rotated + Search in Rotated Array |
| 48 | System Design: Multi-tenant, vLLM inference architecture, PagedAttention, continuous batching | Inference architecture design | Subsets |
| 49 | **LLM Inference Interview Prep**: vLLM, KV cache, quantization, constrained decoding deep dive | Explain concepts with examples | Serialize/Deserialize Tree |
| 50 | **NLP Concepts**: Transformer QKV, RoPE, BERT vs GPT, tokenization, MoE, speculative decoding | tiktoken + attention viz | Permutations |
| 51 | DSA Mock + Portfolio Review | Polish GitHub | Word Search |
| 52 | System Design Mock + Behavioral | Termination narrative + why AI | Combination Sum |
| 53 | Live Coding Mock (FastAPI + LangGraph) | Build mini agent under time | Clone Graph |

### Phase 7: Project 2 + Apply FT (Days 54-60)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 54 | **PROJECT 2**: Multi-Agent MCP Orchestrator (FastAPI + LangGraph + MCP + Next.js) | Build core | Implement Trie (Prefix Tree) |
| 55 | Project 2: Docker + GitHub Actions + AWS ECS | CI/CD pipeline | Time Based Key-Value Store |
| 56 | **Project 2 DONE**: Ragas eval + Deploy + README | Production-grade | Number of Islands + Max Area of Island |
| 57 | **APPLY BLITZ**: Wellfound (20) + YC (10) + LinkedIn DMs (10) | Personalized messages | Redundant Connection |
| 58 | Follow-ups + Mock interviews | Respond to callbacks, practice behavioral | Evaluate Reverse Polish Notation |
| 59 | Buffer / Offer evaluation | Compare offers, negotiate | Rest |
| 60 | **🎯 ₹10-12 LPA OFFER** | Celebrate + plan next | — |


---

## ⚠️ Rules for Updating

1. After each day completes, append the actual topics covered to the Completed table.
2. Update Current Day status to ✅ COMPLETED.
3. Add the next day to Current Day with 🔴 IN PROGRESS.
4. If topics shift (faster or slower), update Upcoming table accordingly.
5. Never plan more than 3 days ahead — let actual pace dictate.
