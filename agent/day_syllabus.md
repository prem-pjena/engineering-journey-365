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
| 15 | String methods, JSON module + **Constrained Decoding (XGrammar/Outlines)** | Parse nested JSON LLM outputs + FSM token masking | Product of Array |
| 16 | LLM APIs: OpenAI/Gemini, temperature, tokens, streaming | Chat + streaming response | Valid Palindrome |
| 17 | **Algorithmic Prompt Optimization**: DSPy + GEPA — self-improving prompt signatures from execution traces | Replace manual prompting with compiled, optimized prompts | 3Sum |

### Phase 2: LangChain + Advanced RAG Foundation (Days 18-24)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 18 | FastAPI SSE Streaming + Pydantic + Constrained Decoding | Build streaming endpoint + FSM-guaranteed JSON | Container With Most Water + Two Sum II |
| 19 | LangChain: Document Loaders, Text Splitters, **Semantic Chunking** | Parse PDF, compare chunk strategies | Longest Substring |
| 20 | Vector DBs, Embeddings, ChromaDB, HNSW vs IVFFlat | Store chunks + index tuning | Valid Parentheses |
| 21 | **Advanced Retrieval**: Proposition Generation + Step-back Prompting | Decompose docs into atomic propositions, generate broader queries | Binary Search |
| 22 | **SQL + pgvector**: SELECT, INSERT, JOINs, vector columns, read-only scopes | Store embeddings with read-only transaction scopes | Search 2D Matrix |
| 23 | **Parent-Child Chunking + Cross-Encoder Reranking + GraphRAG** | Rerank top-20 → top-3, introduce GraphRAG via Milvus | Reverse Linked List |
| 24 | **Hybrid Search**: BM25 + Dense, pgvector HNSW vs IVFFlat tuning | Implement hybrid search + benchmark index configs | Merge Two Sorted |

### Phase 3: Adaptive RAG + Agentic Memory + Evaluation (Days 25-31)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 25 | **Corrective RAG (CRAG)** + **Adaptive RAG** | Evaluator → web fallback + router | Reorder List |
| 26 | **Conversational RAG + Agentic RAG**. Study: NirDiamant/rag_techniques | Chat history + agent re-queries. Analyze Proposition Gen patterns | Max Depth Tree |
| 27 | **Agentic RAG with Contextual AI**: instruction-following rerankers, grounded models | Agent rewrites queries if results poor | Validate BST |
| 28 | **Cross-Session Agent Memory**: Mem0 (semantic dedup) + Graphiti (temporal KGs). Study: NirDiamant/Agent_Memory_Techniques Notebooks 24-27 | Integrate Mem0 into LangGraph + build temporal KG | Invert Tree |
| 29 | **Evaluation**: LLM-as-a-judge regression, Ragas, failure-mode reporting, AIBOM tracking | Golden dataset + auto-eval pipeline (catch infinite loops, context drift) | LCA of BST |
| 30 | **PROJECT 1 BUILD**: Multi-Tenant Enterprise Knowledge Agent (Agno dual-schema, Graphiti, Mem0, CRAG, JWT RBAC) | FastAPI + pgvector RLS + LangGraph + Cross-encoder + Hybrid Search | Level Order Traversal |
| 31 | **Project 1 DONE + APPLY BLITZ**: Deploy AWS ECS, Ragas report | Wellfound + YC apps with Project 1 as proof | Longest Consecutive Sequence |

### Phase 4: LangGraph + Web Automation + MCP (Days 32-39)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 32 | LangGraph: StateGraph, Nodes, Edges, State, Reducers. Study: ed-donner/agents Week 4 | Linear 3-node state + chatbot with memory | Course Schedule |
| 33 | LangGraph: Conditional Routing + **DFSDT** + **PostgresSaver checkpointing** | Intent router with durable checkpointing (not InMemorySaver) | Climbing Stairs |
| 34 | **Advanced LangGraph**: HITL, **Send API** (parallel fan-out), hash-based idempotent recompute. Study: OpenBMB/ToolBench | Approval interrupts + parallel dispatch to analysts | LRU Cache |
| 35 | MCP Core: Host/Client/Server, stdio/HTTP SSE, Tools/Resources. **OAuth 2.1 for MCP** | Python MCP server + token exchange (no passthrough) | Task Scheduler |
| 36 | **Agentic Web Interaction**: browser-use (Playwright, visual DOM) + Firecrawl (markdown extraction). Study: firecrawl/firecrawl-workflows | Research agent navigates SPAs + extracts structured data | Min Stack |
| 37 | MCP Integrations: Explore punkpeye/awesome-mcp-servers | OAuth 2.1 integrations, schema definitions | Merge Intervals |
| 38 | **Lightweight Orchestration**: OpenAI Agents SDK (handoffs, manager pattern, voice streaming) | Manager agent delegates to specialized sub-agents | Insert Interval |
| 39 | **LangGraph + MCP + Web Agent Integration** | Agent discovers MCP tools + browser-use for web research | Course Schedule II |

### Phase 5: Production Security + Sandboxed Execution + Cloud Deploy (Days 40-46)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 40 | **Agent Security & RBAC**: Agno dual-schema (read-only transactions) + JWT-based multi-tenant isolation | PostgreSQL read_only scopes for analyst agents | Kth Largest in a Stream |
| 41 | **Threat Modeling**: AgentShield config scanning + NeMo Guardrails (Colang, topical bounding, jailbreak detection) | Scan agent configs for vulns, implement safety guards | K Closest Points to Origin |
| 42 | **Sandboxed Code Execution**: Daytona SDK (isolated ephemeral sandboxes, dedicated kernel) | Build secure Python REPL via Daytona | Best Time to Buy/Sell Stock |
| 43 | **vLLM Inference**: PagedAttention, continuous batching, TP, KV cache. Study: EthicalML/awesome-production-agentic-systems | Deploy model, measure TTFT | Longest Repeating Char Replacement |
| 44 | **Redis Semantic Caching** + **Next.js UI** basics with SSE streaming | Semantic cache + chat UI | Linked List Cycle |
| 45 | **AWS ECS Fargate + Docker**: Deploy full stack (Fargate + RDS + Load Balancer) | Cloud deployment + CloudWatch | 3Sum review |
| 46 | **GitHub Actions CI/CD**: Auto-test, auto-eval (LLM-as-a-judge), auto-deploy + Cost tracking | Push → test → deploy + token cost middleware | Min Window Substring |

### Phase 6: System Design + Interview Mastery (Days 47-53)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 47 | System Design: RAG at scale + LangGraph scaling (PostgresSaver, Send API, hash-based idempotent recompute) | 1M QPD architecture + parallel fan-out design | Find Min Rotated + Search in Rotated Array |
| 48 | System Design: Multi-tenant, LLM Gateway, vLLM inference architecture, PagedAttention | Gateway design + inference trade-offs | Subsets |
| 49 | **MCP Security Paradigms**: OAuth 2.1, mTLS, OWASP MCP Top 10 (Confused Deputy, Tool Poisoning), per-client consent | Design secure MCP proxy with token exchange | Serialize/Deserialize Tree |
| 50 | **NLP Concepts**: Transformer QKV, RoPE, BERT vs GPT, tokenization, MoE, speculative decoding | tiktoken + attention viz | Permutations |
| 51 | **Advanced Memory Theory**: Procedural Memory (workflow templates), Blackboard System (namespaces, optimistic locking) | Design memory architecture with access control | Word Search |
| 52 | System Design Mock + Behavioral | Termination narrative + why AI + architecture trade-offs | Combination Sum |
| 53 | Live Coding Mock (FastAPI + LangGraph + MCP) | Build mini agent under time pressure | Clone Graph |

### Phase 7: Capstone Project + Apply FT (Days 54-60)
| Day | Morning | Afternoon | DSA |
|-----|---------|-----------|-----|
| 54 | **PROJECT 2**: Autonomous Code & Web Intelligence Swarm — Blackboard pattern + Researcher (browser-use/Firecrawl) + Coder (Daytona) | Build Blackboard with namespaces, initiate agents | Implement Trie (Prefix Tree) |
| 55 | Project 2: MCP with OAuth 2.1 + Docker + GitHub Actions + AWS ECS | CI/CD pipeline + token exchange | Time Based Key-Value Store |
| 56 | **Project 2 DONE**: LLM-as-a-judge regression (catch infinite loops, context drift) + Deploy + README | Production-grade with architecture diagrams | Number of Islands + Max Area of Island |
| 57 | **APPLY BLITZ**: Wellfound (20) + YC (10) + LinkedIn DMs (10) | Personalized messages with both projects | Redundant Connection |
| 58 | Follow-ups + Mock interviews | Respond to callbacks, practice behavioral, negotiate | Evaluate Reverse Polish Notation |
| 59 | Buffer / Offer evaluation | Compare offers, negotiate | Rest |
| 60 | **🎯 ₹10-12 LPA OFFER** | Celebrate + plan next | — |


---

## ⚠️ Rules for Updating

1. After each day completes, append the actual topics covered to the Completed table.
2. Update Current Day status to ✅ COMPLETED.
3. Add the next day to Current Day with 🔴 IN PROGRESS.
4. If topics shift (faster or slower), update Upcoming table accordingly.
5. Never plan more than 3 days ahead — let actual pace dictate.
