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

---

## 🔄 Current Day

| Day | Date | Status | Topics | DSA |
|-----|------|--------|--------|-----|
| 11 | Jul 14 | 🔴 IN PROGRESS | OOP: classes, inheritance, dunder, @property, Context Managers, Modules | Two Sum, Valid Anagram |

---

## 📅 Upcoming (Complete 60-Day Curriculum — All Concepts, No Skipping)

### Week 1 (Days 1-7): Python Foundations + LLM Basics
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 11 | OOP: classes, inheritance, dunder, @property | Build mock Vector Store class | Two Sum |
| 12 | Context Managers, Modules, __init__.py | LLM wrapper with static methods | Valid Anagram |
| 13 | Async: asyncio, event loop, gather | Fetch 5 mock APIs concurrently | Group Anagrams |
| 14 | Generators (yield), Tuples, enumerate, zip | Build streaming token generator | Top K Frequent |
| 15 | String methods, JSON module | Parse nested JSON LLM outputs | Product of Array |
| 16 | **Pandas + NumPy** (DataFrames, arrays, broadcasting, cleaning) | Data analysis script on mock CSV | Valid Palindrome |
| 17 | LLM APIs: OpenAI/Gemini, streaming | Chat + streaming responses | 3Sum |

### Week 2 (Days 8-14): LangChain + RAG + SQL
| Day | Topics | DSA |
|-----|--------|-----|
| 18 | Prompt Engineering: few-shot, CoT, system prompts | Container With Most Water |
| 19 | LangChain LCEL, Prompt Templates | Longest Substring |
| 20 | with_structured_output, Pydantic schemas | Valid Parentheses |
| 21 | Document Loaders, Text Splitters | Binary Search |
| 22 | Vector DBs, Cosine similarity, Embeddings, ChromaDB | Search 2D Matrix |
| 23 | Naive RAG: chunk → embed → store → retrieve | Reverse Linked List |
| 24 | **SQL + data validation** (SELECT, INSERT, JOINs, aggregations, cleaning) | Merge Two Sorted |

### Week 3 (Days 15-21): Advanced RAG + pgvector + ML/NLP
| Day | Topics | DSA |
|-----|--------|-----|
| 25 | Multi-query, MMR retrieval | Reorder List |
| 26 | Metadata filtering, hybrid search | Max Depth Tree |
| 27 | Cross-encoder reranking (BGE) + **RNN/CNN basics** | Same Tree |
| 28 | pgvector setup, vector queries, HNSW vs IVFFlat | Invert Tree |
| 29 | **Agentic RAG** + **Transformer architecture (Q, K, V, self-attention)** | Level Order Traversal |
| 30 | **PROJECT 1: RAG System** + Ragas evaluation + **NLP (BERT vs GPT, embeddings)** | LCA of BST |

### Week 4 (Days 22-28): Apply ₹30k + Interview Prep
| Day | Topics | DSA |
|-----|--------|-----|
| 22-24 | Docker + AWS EC2 deploy, **ML basics (bias-variance, precision/recall/F1, cross-validation)**, **NLP concepts (BERT vs GPT, embeddings, tokenization)** | Trie, Kth Largest |
| 25-28 | Apply on Apna + Wellfound, mock interviews, **Transformer architecture review (Q, K, V, self-attention)**, **RNN/CNN refresher** | Review all patterns |

### Weeks 5-8 (Days 29-56): LangGraph → MCP → Project 2 → Apply FT
| Week | Focus | Target |
|------|-------|--------|
| 5 | LangGraph (StateGraph, reducers, routing, HITL, multi-agent, LangSmith) | Agent mastery |
| 6 | MCP (stdio, HTTP SSE, Tools/Resources/Prompts, LangGraph+MCP) | Protocol mastery |
| 7 | Cost tracking, System Design (RAG scale, multi-tenant, latency), CI/CD | Interview prep |
| 8 | **Project 2** + Apply blitz (50+ roles) | ₹60-80k FT offer |

| Day | Planned Topics | DSA |
|-----|---------------|-----|
| 11 | **LangChain LCEL, prompt templates, ChatOpenAI** + Pydantic BaseModel + with_structured_output() | Contains Duplicate |
| 12 | **LLM APIs (OpenAI, Gemini)** — chat, streaming, embeddings, json_mode vs json_schema | Valid Anagram |
| 13 | **OOP deep dive** — classes, inheritance, dunder, @property, Context Managers, Modules | Two Sum II |
| 14 | **Async Python** (asyncio, async/await, gather, event loop) + Tuples, enumerate(), zip() | Group Anagrams |
| 15 | **Vector DBs** — pgvector setup, embeddings, cosine similarity, SQL queries for RAG | Top K Frequent |
| 16 | **Naive RAG** — chunk → embed → store → retrieve → generate + chunking strategies | Product of Array |
| 17 | **LangGraph basics** — StateGraph, nodes, edges, state, Reducers, add_messages | Valid Palindrome |
| 18 | **ReAct pattern** — agent with tool calling, conditional routing, state persistence | 3Sum |
| 19 | **Ragas evaluation** — faithfulness, context precision, recall + prompt engineering | Container With Most Water |
| 20 | **MCP basics** — Host/Client/Server, Tools vs Resources vs Prompts, stdio transport | Best Time to Buy/Sell |
| 21 | **Project 1** — Build RAG Agent with LangGraph + MCP | Longest Substring |
| 22-28 | **Apply for ₹30k internship** — Apna, Wellfound. Interview prep. | Targeted DSA + Review |
| 29-35 | **LangGraph advanced** — multi-agent, parallel execution, human-in-the-loop, LangSmith | Review + mock |
| 36-42 | **MCP advanced** — Streamable HTTP, security, auth + Advanced RAG (hybrid search, reranking) | Review + mock |
| 43-49 | **Interview prep** — ML concepts, NLP, system design, behavioral (termination narrative) | Targeted practice |
| 50-56 | **Project 2** — Multi-Agent MCP Orchestrator + **Apply FT** ₹60-80k | DSA review |

**All previous concepts included:** OOP, Context Managers, Async, Tuples, Generators, String methods, JSON, Type hints — integrated into LangChain/agent projects during Weeks 1-2.
|-------------|-----------|----------|
| Naive RAG intro | **Semantic Chunking** — statistical rolling-window cosine distance, agentic chunking for tables/headers | 🔴 |
| Prompt Engineering | **Constrained Decoding** — Native Structured Outputs, Pydantic response_format, no regex parsing | 🔴 |
| LangGraph intro | **Graph State Persistence** — PostgresSaver, checkpointer, thread_id, resume across restarts | 🔴 |
| LangGraph intro | **Topological Sorting + Deadlock Prevention** — cycles, recursion_limit, Kahn's Algorithm | 🔴 |
| Before deployment | **MCP Integration** — MCP server exposing DB, tool discovery, JSON-RPC transport | 🔴 |
| UI/Deployment | **SSE + Token Streaming** — StreamingResponse, async generators, real-time output | 🟡 |
| Alongside Ragas | **Observability** — LangSmith tracing, execution tree debugging, token cost tracking | 🟡 |
| DSA Month 1 | **Vector Math** — Cosine similarity from scratch with NumPy, L2 vs L1 vs Cosine | 🟡 |
| DSA Month 2 | **Graph Traversal Algorithms** — BFS, DFS, topological sort (Kahn's Algorithm) | 🔴 |

---

## ⚠️ Rules for Updating

1. After each day completes, append the actual topics covered to the Completed table.
2. Update Current Day status to ✅ COMPLETED.
3. Add the next day to Current Day with 🔴 IN PROGRESS.
4. If topics shift (faster or slower), update Upcoming table accordingly.
5. Never plan more than 3 days ahead — let actual pace dictate.
