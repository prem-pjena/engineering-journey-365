# Day 12 — Terminal, Git, Context Managers, Modules

**Status:** ✅ Completed — 2026-07-23
**Priority:** Medium (foundational tools for AI Engineer workflow)

## Topics Covered
- **Hash Map DSA:** Two Sum (review), Valid Anagram (new) — Frequency Counter pattern
- **Terminal Basics:** pwd, ls, cd, cd .., mkdir, touch
- **Git:** init, status, add, commit, log, HEAD
- **Context Managers:** with statement, __enter__, __exit__, resource cleanup (conceptual only)
- **Modules:** Single .py file, import statement
- **Packages:** Folder of modules, __init__.py
- **Virtual Environments:** venv, pip, isolation purpose

## DSA
- Two Sum (LeetCode #1) — Brute force O(n²) + Hash Map O(n) — ✅ Completed
- Valid Anagram (LeetCode #242) — Two Dict + One Dict optimized — ✅ Completed

## Key Learnings
- Hash Map lookups are O(1) average
- Frequency Counter pattern: increment on s, decrement on t
- Git creates checkpoints (commits) in a timeline
- HEAD points to current commit
- Package = folder with __init__.py
- venv isolates project dependencies

## Programs Built
1. `task_01.py` — SafeFileManager custom context manager
2. `task_02.py` — Valid Anagram (Two Dict + One Dict optimized)
3. `task_03.py` — Two Sum (Brute + Hash Map)
4. `task_04.py` — Git workflow simulation
5. `task_05.py` — Calculator module (Module vs Package demo)
6. `task_06.py` — Virtual environment setup script

## Topics Intentionally Skipped
- Advanced context managers (exc_type, exc_value, traceback) — Low ROI for AI Engineer
- @property and dunder methods — Postponed from Day 11

## Next: Day 13 — pip/venv + HTTP Protocol + Type Hinting + FastAPI Intro
