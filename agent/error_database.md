# ❌ Error Database

**Purpose:** Every mistake logged once. Never repeated.

---

## Error #1
| Field | Detail |
|-------|--------|
| **Topic** | `input()` |
| **Mistake** | Assumed user input automatically becomes an integer |
| **Correction** | `input()` returns a string. Use `int(input())` when an integer is required |
| **Status** | ✅ Resolved |

---

## Error #2
| Field | Detail |
|-------|--------|
| **Topic** | `print()` |
| **Mistake** | Used `print("Name": name)` — wrong syntax. Also used `\n` incorrectly |
| **Correction** | Use `print("Name:", name)` with a comma. Use multiple `print()` statements when needed |
| **Status** | ✅ Resolved |

---

## Error #3
| Field | Detail |
|-------|--------|
| **Topic** | O(1) |
| **Mistake** | Thought O(1) = one operation |
| **Correction** | O(1) = amount of work stays CONSTANT regardless of input size |
| **Status** | ✅ Resolved |

---

## Error #4
| Field | Detail |
|-------|--------|
| **Topic** | Comparison Operators |
| **Mistake** | Used `>=` when requirement said `>` |
| **Correction** | `>` = Greater Than. `>=` = Greater Than Or Equal To. Different operators. |
| **Status** | ✅ Resolved |

---

## Error #5
| Field | Detail |
|-------|--------|
| **Topic** | String Comparison |
| **Mistake** | Used `if id == yes:` without quotes around the string |
| **Correction** | Strings must be enclosed in quotation marks: `if id == "yes":` |
| **Status** | ✅ Resolved |

## Error #6
| Field | Detail |
|-------|--------|
| **Topic** | `continue` in `while` loops |
| **Mistake** | Placed `continue` before updating the loop variable, causing an infinite loop |
| **Correction** | Update the loop variable before `continue`, or structure the loop so the update always occurs |
| **Status** | ✅ Resolved |

## Error #7
| Field | Detail |
|-------|--------|
| **Topic** | String methods |
| **Mistake** | Wrote `lower.name` instead of `name.lower()` |
| **Correction** | String methods use dot notation: `variable.method()` not `method.variable` |
| **Status** | ✅ Resolved |

---

## Error #8
| Field | Detail |
|-------|--------|
| **Topic** | Function parameters |
| **Mistake** | Called `even_odd()` without passing required argument |
| **Correction** | All parameters must be passed: `even_odd(number)` |
| **Status** | ✅ Resolved |

## Error #9
| Field | Detail |
|-------|--------|
| **Topic** | Building lists manually |
| **Mistake** | Repeated code 3× instead of using a `for` loop |
| **Correction** | Use `for i in range(n):` to avoid repetition |
| **Status** | ✅ Resolved |

## Error #10
| Field | Detail |
|-------|--------|
| **Topic** | Largest number algorithm |
| **Mistake** | Reset max inside the loop + used `i` instead of `num` |
| **Correction** | Initialize max before loop, compare each element, update only when larger |
| **Status** | ✅ Resolved |

## Error #11
| Field | Detail |
|-------|--------|
| **Topic** | remove() vs pop() |
| **Mistake** | Used `remove()` when `pop()` was needed |
| **Correction** | `remove(value)` removes by value. `pop(index)` removes by index/index-1 position |
| **Status** | ✅ Resolved |

## Error #12
| Field | Detail |
|-------|--------|
| **Topic** | Index off-by-one |
| **Mistake** | Used `pop(index)` instead of `pop(index-1)` for user-facing menu |
| **Correction** | User numbering starts at 1, list indexing starts at 0. Always convert: `pop(index-1)` |
| **Status** | ✅ Resolved |

## Error #13
| Field | Detail |
|-------|--------|
| **Topic** | Todo app program flow |
| **Mistake** | Forgot menu logic — always added task instead of showing options |
| **Correction** | Structure menu-driven apps as: loop → show options → get choice → act |
| **Status** | ✅ Resolved |


## Error #14
| Field | Detail |
|-------|--------|
| **Topic** | Variable naming (typo) |
| **Mistake** | Typo: `menue` vs `menu` |
| **Correction** | Always double-check variable name spelling. Python treats `menue` as a new undefined variable. |
| **Status** | ✅ Resolved |

## Error #15
| Field | Detail |
|-------|--------|
| **Topic** | Loop variable vs list element |
| **Mistake** | Confused index `i` with the actual dict `contacts[i]` |
| **Correction** | `for i` gives the index. Use `contacts[i]` to access the dict at that index. OR use `for contact in contacts` to get dicts directly. |
| **Status** | ✅ Resolved |

## Error #16
| Field | Detail |
|-------|--------|
| **Topic** | Search logic placement |
| **Mistake** | Printed "Not found" inside the loop instead of after searching the whole list |
| **Correction** | Only declare "not found" AFTER the loop completes without a match. Use a `found` flag. |
| **Status** | ✅ Resolved |

## Error #17
| Field | Detail |
|-------|--------|
| **Topic** | `=` vs `==` in conditions |
| **Mistake** | Used single `=` (assignment) instead of `==` (comparison) inside `if` |
| **Correction** | `=` assigns a value. `==` compares two values. Use `==` in conditions. |
| **Status** | ✅ Resolved |

---

*New errors will be appended here as they occur.*
