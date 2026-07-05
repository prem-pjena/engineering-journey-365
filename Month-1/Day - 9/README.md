# Day 9 — Exception Handling, Advanced Functions, Program Organization

**Status:** ✅ Completed — 2026-07-04

## Topics Learned
- Exception Handling: try/except/else/finally, ValueError, ZeroDivisionError, KeyError
- *args — variable positional arguments
- **kwargs — variable keyword arguments
- Lambda functions (single and multiple params)
- map() and filter() — functional programming
- Program Organization — modular function-based structure
- Function Dispatch Table — functions as first-class objects
- Calculator 2.0 — reusable functions + dispatch table
- Big O Review: O(1), O(n), O(n²)

## Programs Built
1. `task_01.py` — Exception handling for invalid integer input
2. `task_02.py` — Division calculator with ValueError + ZeroDivisionError + else/finally
3. `task_03.py` — sum_all(*args) with accumulator pattern
4. `task_04.py` — show_info(**kwargs) with .items() iteration
5. `task_05.py` — Lambda functions (double, multiply with multiple params)
6. `task_06.py` — map() and filter() on lists
7. `task_07.py` — Contact Book refactored with organized functions + main()
8. `task_08.py` — Calculator 2.0 with function dispatch table

## Key Breakthrough
**Function dispatch table** — storing functions in a dictionary:
```python
operations = {1: add, 2: subtract, 3: multiply, 4: divide}
operations[choice](a, b)
```
Functions are first-class objects in Python — can be stored, passed, and called dynamically.

## Mistakes Fixed
- `false` → `False` (Python case sensitivity)
- `dict` as variable name (built-in shadowing)
- Function with print() returns None
- Dict KeyError vs ValueError confusion
- `add` (reference) vs `add()` (execution) distinction

## Scores
- Python: 8.4/10 · DSA: 4.5/10 · Functions: 9.2/10
- Exception Handling: 9.2/10 · Lambda: 9.5/10 · Program Organization: 9.3/10
- Problem Solving: 7.4/10 · Coding Confidence: 10/10 · Independent Builder: 9.5/10

## Verdict
✅ **9.5/10 — Ready for Day 10 (File I/O + Sets)**
