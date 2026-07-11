# Day 9 — Exception Handling, Advanced Functions, Program Organization

**Status:** ✅ Completed — 2026-07-04

## Topics Covered
- Exception Handling: try/except/else/finally, ValueError, ZeroDivisionError, KeyError
- *args — variable positional arguments
- **kwargs — variable keyword arguments
- Lambda functions (single and multiple params)
- map() — transform every element
- filter() — keep elements by condition
- Program Organization — modular function-based structure
- Function Dispatch Table — functions as first-class objects stored in dict
- Calculator 2.0 — reusable functions + dispatch table
- Big O Review: O(1), O(n), O(n²) with real examples

## Programs Built
1. Exception handling for invalid integer input
2. Division calculator with ValueError + ZeroDivisionError
3. `sum_all(*args)` with accumulator pattern
4. `show_info(**kwargs)` with .items() iteration
5. Lambda functions (double, multiply)
6. map() and filter() on lists
7. Contact Book refactored with separate functions + main()
8. Calculator 2.0 with function dispatch table

## Biggest Breakthrough
**Function dispatch table** — storing functions in a dictionary:
```python
operations = {1: add, 2: subtract, 3: multiply, 4: divide}
operations[choice](a, b)
```
This was the hardest concept. Understood after working through confusion about `add` vs `add()`.

## Mistakes Fixed
- `false` → `False` (case sensitivity)
- `dict` as variable name (built-in shadowing)
- Function with print() returns None (non-obvious)
- Dictionary KeyError vs ValueError confusion
- Function reference `add` vs execution `add()` distinction

## Scores
- Python: 8.4/10 · DSA: 4.5/10 · Functions: 9.2/10
- Exception Handling: 9.2/10 · Lambda: 9.5/10
- Program Organization: 9.3/10 · Problem Solving: 7.4/10
- Coding Confidence: 10/10 · Independent Builder: 9.5/10

## Readiness
✅ **9.5/10 — Ready for Day 10 (File I/O + Sets)**
