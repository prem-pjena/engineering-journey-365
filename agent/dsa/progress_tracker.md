# 📐 DSA Progress Tracker — AI Engineer Optimized v4 (30 Problems)

**Source:** agent/dsa/study_plan.md (v4 — 30 problems, 30 min/day, no DP/Linked Lists/Hard Graphs)
**Based on:** agent/reports/final_audit_report.md

---

## Complete Problem List (30 Problems)

| # | Problem | LeetCode | Pattern | Phase | Day | Status |
|---|---------|----------|---------|-------|-----|--------|
| 1 | Two Sum | #1 | Frequency Counter | 1 | Day 10 | ✅ Done |
| 2 | Valid Anagram | #242 | Frequency Counter | 1 | Day 12 | ✅ Done |
| 3 | Contains Duplicate | #217 | Hash Set | 1 | Day 13 | ⬜ |
| 4 | Intersection of Two Arrays | #349 | Hash Set | 1 | Day 15 | ⬜ |
| 5 | First Unique Character | #387 | Frequency Counter | 1 | Day 16 | ⬜ |
| 6 | Range Sum Query | #303 | Prefix Sum | 1 | Day 17 | ⬜ |
| 7 | Binary Search | #704 | Binary Search | 1 | Day 18 | ⬜ |
| 8 | Search Insert Position | #35 | Binary Search | 1 | Day 20 | ⬜ |
| 9 | First Bad Version | #278 | Binary Search | 1 | Day 21 | ⬜ |
| 10 | Valid Parentheses | #20 | Stack | 1 | Day 22 | ⬜ |
| 11 | Longest Common Prefix | #14 | String | 2 | Day 23 | ⬜ |
| 12 | Index of First Occurrence | #28 | String | 2 | Day 24 | ⬜ |
| 13 | Majority Element | #169 | Hash Map | 2 | Day 25 | ⬜ |
| 14 | Max Depth of Tree | #104 | Tree DFS | 2 | Day 27 | ⬜ |
| 15 | Same Tree | #100 | Tree DFS | 2 | Day 28 | ⬜ |
| 16 | Level Order Traversal | #102 | Tree BFS | 2 | Day 29 | ⬜ |
| 17 | Validate BST | #98 | Tree DFS | 2 | Day 30 | ⬜ |
| 18 | Two Sum II | #167 | Two Pointers | 2 | Day 31 | ⬜ |
| 19 | Longest Substr w/o Repeat | #3 | Sliding Window | 2 | Day 32 | ⬜ |
| 20 | Merge Intervals | #56 | Intervals | 3 | Day 34 | ⬜ |
| 21 | Kth Largest in Array | #215 | Heap | 3 | Day 35 | ⬜ |
| 22 | Top K Frequent Elements | #347 | Heap | 3 | Day 36 | ⬜ |
| 23 | Number of Islands | #200 | Graph BFS | 3 | Day 37 | ⬜ |
| 24 | Course Schedule | #207 | Topological Sort | 3 | Day 38 | ⬜ |
| 25 | Graph Valid Tree | #261 | Graph DFS | 3 | Day 39 | ⬜ |
| 26 | LRU Cache | #146 | Design | 3 | Day 41 | ⬜ |
| 27 | Logger Rate Limiter | #359 | Hash/Design | 3 | Day 42 | ⬜ |
| 28 | Moving Average | #346 | Queue | 3 | Day 43 | ⬜ |
| 29 | Random Pick with Weight | #528 | Prefix Sum + BS | 3 | Day 44 | ⬜ |
| 30 | Dot Product Sparse Vectors | #1570 | Hash Map | 3 | Day 45 | ⬜ |
| 31 | All Paths Source to Target | #797 | Graph DFS | 3 | Day 46 | ⬜ |
| 32 | Implement Trie | #208 | Trie | 4-5 | Day 48 | ⬜ |
| 33 | Word Break | #139 | DP | 4-5 | Day 49 | ⬜ |
| 34 | Permutations | #46 | Backtracking | 4-5 | Day 50 | ⬜ |
| 35 | Merge k Sorted Lists | #23 | Heap | 4-5 | Day 51 | ⬜ |
| 36 | Time Based KV Store | #981 | Design + BS | 4-5 | Day 52 | ⬜ |
| 37 | Design Hit Counter | #362 | Design | 4-5 | Day 53 | ⬜ |

---

## Patterns Covered

| Pattern | AI Application | Problems | Status |
|---------|---------------|----------|--------|
| Frequency Counter | Token counting, RAG filtering | #1, #242, #217, #349, #387, #169 | ⬜ |
| Binary Search | Log analysis, regression bisecting | #704, #35, #278 | ⬜ |
| Stack | JSON validation, tool-call parsing | #20 | ⬜ |
| String / Prefix | Prompt prefix caching, substring search | #14, #28 | ⬜ |
| Tree BFS/DFS | LangGraph state transitions, taxonomy parsing | #104, #100, #102, #98 | ⬜ |
| Two Pointers | String validation, stream parsing | #167, #3 | ⬜ |
| Intervals | RAG chunk merging, context windows | #56 | ⬜ |
| Heap | Vector search, top-K retrieval | #215, #347, #23 | ⬜ |
| Graph BFS/DFS/Topo | LangGraph DAG orchestration | #200, #207, #261, #797 | ⬜ |
| LRU Cache | KV caching for LLM inference | #146 | ⬜ |
| Rate Limiting | LLM API protection, agent loop prevention | #359, #362, #346 | ⬜ |
| Prefix Sum + BS | Token sampling (temperature, top-p) | #528 | ⬜ |
| Sparse Vector | Cosine similarity for embeddings | #1570 | ⬜ |
| Trie | Radix caching for LLM inference | #208 | ⬜ |
| DP (basic) | BPE tokenization | #139 | ⬜ |
| Backtracking | Tool-call permutations | #46 | ⬜ |
| 13 | Logger Rate Limiter | #359 | Hash + Window | 1 | Day 18 | ⬜ |
| 14 | Longest Common Prefix | #14 | String | 2 | Day 20 | ⬜ |
| 15 | Index of First Occurrence | #28 | String | 2 | Day 20 | ⬜ |
| 16 | Merge Two Sorted Lists | #21 | LL Traversal | 2 | Day 21 | ⬜ |
| 17 | Remove Duplicates from LL | #83 | LL Traversal | 2 | Day 21 | ⬜ |
| 18 | Valid Parentheses | #20 | Stack | 2 | Day 22 | ⬜ |
| 19 | Remove Adjacent Duplicates | #1047 | Stack | 2 | Day 22 | ⬜ |
| 20 | Contains Duplicate II | #219 | Sliding Window | 2 | Day 23 | ⬜ |
| 21 | Majority Element | #169 | Hash Map | 2 | Day 23 | ⬜ |
| 22 | Move Zeroes | #283 | Two Pointers | 2 | Day 24 | ⬜ |
| 23 | Reverse Linked List | #206 | In-Place Reversal | 2 | Day 24 | ⬜ |
| 24 | Queue using Stacks | #232 | Stack/Design | 2 | Day 25 | ⬜ |
| 25 | Stack using Queues | #225 | Queue/Design | 2 | Day 25 | ⬜ |
| 26 | Simplify Path | #71 | Stack | 3 | Day 27 | ⬜ |
| 27 | Decode String | #394 | Stack | 3 | Day 27 | ⬜ |
| 28 | Evaluate Reverse Polish | #150 | Stack | 3 | Day 28 | ⬜ |
| 29 | Max Depth of Tree | #104 | Tree DFS | 3 | Day 28 | ⬜ |
| 30 | Same Tree | #100 | Tree DFS | 3 | Day 29 | ⬜ |
| 31 | Level Order Traversal | #102 | Tree BFS | 3 | Day 29 | ⬜ |
| 32 | LCA of Binary Tree | #236 | Tree DFS | 3 | Day 30 | ⬜ |
| 33 | Validate BST | #98 | Tree DFS | 3 | Day 30 | ⬜ |
| 34 | Two Sum II | #167 | Two Pointers | 3 | Day 31 | ⬜ |
| 35 | Longest Substring w/o Repeat | #3 | Sliding Window | 3 | Day 31 | ⬜ |
| 36 | Design Hit Counter | #362 | Queue/Design | 3 | Day 32 | ⬜ |
| 37 | Path Sum | #112 | Tree DFS | 3 | Day 32 | ⬜ |
| 38 | Merge Intervals | #56 | Intervals | 4-5 | Day 34 | ⬜ |
| 39 | Insert Interval | #57 | Intervals | 4-5 | Day 34 | ⬜ |
| 40 | Non-overlapping Intervals | #435 | Intervals | 4-5 | Day 35 | ⬜ |
| 41 | Meeting Rooms II | #253 | Heap/Interval | 4-5 | Day 35 | ⬜ |
| 42 | Kth Largest in Array | #215 | Heap | 4-5 | Day 36 | ⬜ |
| 43 | Kth Largest in Stream | #703 | Heap | 4-5 | Day 36 | ⬜ |
| 44 | Top K Frequent Elements | #347 | Heap | 4-5 | Day 37 | ⬜ |
| 45 | K Closest Points | #973 | Heap | 4-5 | Day 37 | ⬜ |
| 46 | Number of Islands | #200 | Graph BFS | 4-5 | Day 38 | ⬜ |
| 47 | Max Area of Island | #695 | Graph BFS | 4-5 | Day 38 | ⬜ |
| 48 | Course Schedule | #207 | Topological Sort | 4-5 | Day 39 | ⬜ |
| 49 | Course Schedule II | #210 | Topological Sort | 4-5 | Day 39 | ⬜ |
| 50 | Graph Valid Tree | #261 | Graph DFS | 4-5 | Day 41 | ⬜ |
| 51 | Connected Components | #323 | Graph DFS | 4-5 | Day 41 | ⬜ |
| 52 | All Paths Source to Target | #797 | Graph DFS | 4-5 | Day 42 | ⬜ |
| 53 | Clone Graph | #133 | Graph DFS | 4-5 | Day 42 | ⬜ |
| 54 | Dot Product Sparse Vectors | #1570 | Hash Map | 4-5 | Day 43 | ⬜ |
| 55 | Random Pick with Weight | #528 | Prefix Sum + BS | 4-5 | Day 43 | ⬜ |
| 56 | Time Based KV Store | #981 | Design + BS | 4-5 | Day 44 | ⬜ |
| 57 | LRU Cache | #146 | Design (LL+Map) | 4-5 | Day 44 | ⬜ |
| 58 | Daily Temperatures | #739 | Monotonic Stack | 4-5 | Day 45 | ⬜ |
| 59 | BT Vertical Order Traversal | #314 | Tree BFS | 4-5 | Day 45 | ⬜ |
| 60 | Find Min Rotated | #153 | Binary Search | 4-5 | Day 46 | ⬜ |
| 61 | Search Rotated Array | #33 | Binary Search | 4-5 | Day 46 | ⬜ |
| 62 | Implement Trie | #208 | Trie | 6-7 | Day 48 | ⬜ |
| 63 | Design Add/Search Words | #211 | Trie | 6-7 | Day 48 | ⬜ |
| 64 | Word Break | #139 | DP | 6-7 | Day 49 | ⬜ |
| 65 | Design Search Autocomplete | #642 | Trie | 6-7 | Day 49 | ⬜ |
| 66 | Permutations | #46 | Backtracking | 6-7 | Day 50 | ⬜ |
| 67 | Generate Parentheses | #22 | Backtracking | 6-7 | Day 50 | ⬜ |
| 68 | Letter Combinations | #17 | Backtracking | 6-7 | Day 51 | ⬜ |
| 69 | Word Search | #79 | Backtracking | 6-7 | Day 51 | ⬜ |
| 70 | Merge k Sorted Lists | #23 | Heap | 6-7 | Day 52 | ⬜ |
| 71 | LFU Cache | #460 | Hash + LL | 6-7 | Day 52 | ⬜ |
| 72 | Word Search II | #212 | Trie + Backtrack | 6-7 | Day 53 | ⬜ |
| 73 | Max Frequency Stack | #895 | Stack/Design | 6-7 | Day 53 | ⬜ |
| 74 | BT Max Path Sum | #124 | Tree DFS | 6-7 | Day 55 | ⬜ |
| 75 | Find Median from Stream | #295 | Heap | 6-7 | Day 55 | ⬜ |
| 76 | Alien Dictionary | #269 | Topological Sort | 6-7 | Day 56 | ⬜ |
| 77 | Insert Delete GetRandom | #380 | Hash/Design | 6-7 | Day 56 | ⬜ |
| 78 | All O`one Data Structure | #432 | Hash/Design | 6-7 | Day 57 | ⬜ |
| 79 | Max Stack | #716 | Stack/Design | 6-7 | Day 57 | ⬜ |
| 80 | Basic Calculator | #224 | Stack | 6-7 | Day 58 | ⬜ |
| 81 | Word Ladder | #127 | Graph BFS | 6-7 | Day 58 | ⬜ |
| 12 | Best Time Buy/Sell Stock | #121 | Sliding Window | 1-2 | Day 18 | ⬜ |
| 13 | Longest Substr w/o Repeat | #3 | Sliding Window | 1-2 | Day 18 | ⬜ |
| 14 | Valid Parentheses | #20 | Stack | 1-2 | Day 20 | ⬜ |
| 15 | Decode String | #394 | Stack | 1-2 | Day 20 | ⬜ |
| 16 | Binary Search | #704 | Binary Search | 1-2 | Day 21 | ⬜ |
| 17 | Search Insert Position | #35 | Binary Search | 1-2 | Day 21 | ⬜ |
| 18 | Reverse Linked List | #206 | In-Place Reversal | 1-2 | Day 22 | ⬜ |
| 19 | Merge Two Sorted Lists | #21 | LL Traversal | 1-2 | Day 22 | ⬜ |
| 20 | Linked List Cycle | #141 | Fast & Slow | 1-2 | Day 23 | ⬜ |
| 21 | First Bad Version | #278 | Binary Search | 1-2 | Day 23 | ⬜ |
| 22 | Logger Rate Limiter | #359 | Hash Map + Window | 1-2 | Day 24 | ⬜ |
| 23 | Moving Average from Stream | #346 | Sliding Window | 1-2 | Day 24 | ⬜ |
| 24 | Design Hit Counter | #362 | Design | 1-2 | Day 25 | ⬜ |
| 25 | Group Anagrams | #49 | Frequency Counter | 1-2 | Day 25 | ⬜ |
| 26 | Level Order Traversal | #102 | BFS | 3 | Day 27 | ⬜ |
| 27 | Binary Tree Right Side View | #199 | BFS | 3 | Day 27 | ⬜ |
| 28 | Max Depth of Tree | #104 | DFS | 3 | Day 28 | ⬜ |
| 29 | Path Sum | #112 | DFS | 3 | Day 28 | ⬜ |
| 30 | Validate BST | #98 | DFS | 3 | Day 29 | ⬜ |
| 31 | LCA of BST | #235 | DFS | 3 | Day 29 | ⬜ |
| 32 | Same Tree | #100 | DFS | 3 | Day 30 | ⬜ |
| 33 | Kth Smallest BST | #230 | DFS | 3 | Day 30 | ⬜ |
| 34 | Merge Intervals | #56 | Intervals | 3 | Day 31 | ⬜ |
| 35 | Insert Interval | #57 | Intervals | 3 | Day 31 | ⬜ |
| 36 | Kth Largest in Array | #215 | Heap | 4-5 | Day 34 | ⬜ |
| 37 | Kth Largest in Stream | #703 | Heap | 4-5 | Day 34 | ⬜ |
| 38 | Top K Frequent Elements | #347 | Heap | 4-5 | Day 35 | ⬜ |
| 39 | K Closest Points | #973 | Heap | 4-5 | Day 35 | ⬜ |
| 40 | Implement Trie | #208 | Trie | 4-5 | Day 36 | ⬜ |
| 41 | Design Add/Search Words | #211 | Trie | 4-5 | Day 36 | ⬜ |
| 42 | Word Break | #139 | DP (tokenizer) | 4-5 | Day 37 | ⬜ |
| 43 | Product of Array Except Self | #238 | Prefix | 4-5 | Day 37 | ⬜ |
| 44 | Course Schedule | #207 | Graph BFS (Topo) | 4-5 | Day 38 | ⬜ |
| 45 | Course Schedule II | #210 | Graph BFS (Topo) | 4-5 | Day 38 | ⬜ |
| 46 | Graph Valid Tree | #261 | Graph DFS | 4-5 | Day 39 | ⬜ |
| 47 | Number of Connected Components | #323 | Graph DFS | 4-5 | Day 39 | ⬜ |
| 48 | All Paths Source to Target | #797 | Graph DFS | 4-5 | Day 41 | ⬜ |
| 49 | Dot Product of Sparse Vectors | #1570 | Hash Map | 4-5 | Day 41 | ⬜ |
| 50 | Time Based KV Store | #981 | Design + BS | 4-5 | Day 42 | ⬜ |
| 51 | LRU Cache | #146 | Design (LL+Map) | 4-5 | Day 43 | ⬜ |
| 52 | Merge k Sorted Lists | #23 | Heap | 4-5 | Day 44 | ⬜ |
| 53 | Longest Consecutive Sequence | #128 | Hash Set | 4-5 | Day 45 | ⬜ |

---

## Patterns Learned

| Pattern | AI Application | Problems | Status |
|---------|---------------|----------|--------|
| Frequency Counter | Context dedup, token counting | #1, #242, #217, #49, #349, #128 | ⬜ |
| Two Pointers | Text parsing, sequence matching | #125, #167, #283, #88 | ⬜ |
| Prefix Sum + Weighted Random | LLM token sampling (top-p, temp) | #303, #528, #238 | ⬜ |
| Sliding Window | Context window mgmt, token streams | #121, #3, #346 | ⬜ |
| Stack | JSON validation, nested parsing | #20, #394, #71 | ⬜ |
| Binary Search | Quantization, timestamp lookup | #704, #35, #278 | ⬜ |
| Linked Lists | Pointer manipulation | #206, #21, #141 | ⬜ |
| Rate Limiting | API protection, tenant quotas | #359, #362 | ⬜ |
| Tree BFS | Hierarchical document chunking | #102, #199 | ⬜ |
| Tree DFS | KG traversal, AST parsing | #104, #112, #100, #98, #235, #230 | ⬜ |
| Intervals | Chunk overlap management | #56, #57 | ⬜ |
| Heap / Top-K | Vector search, semantic retrieval | #215, #703, #347, #973, #23 | ⬜ |
| Trie | BPE tokenizer, vocabulary | #208, #211 | ⬜ |
| Graph BFS (Topo) | LangGraph DAG execution | #207, #210 | ⬜ |
| Graph DFS | Entity resolution, clustering | #261, #323, #797 | ⬜ |
| LRU Cache | KV caching for LLM inference | #146 | ⬜ |
| Time-Based KV | Model state versioning | #981 | ⬜ |
| Sparse Vector Math | Cosine similarity for embeddings | #1570 | ⬜ |
