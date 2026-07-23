# Task 2: Valid Anagram — Frequency Counter Pattern

"""
Problem: Given two strings s and t, return True if t is an anagram of s.

Approach 1: Two Dictionaries
- Count characters in s, count characters in t
- Compare both dictionaries

Approach 2: One Dictionary (Optimized)
- Count characters in s (increment)
- Decrement for characters in t
- If any count != 0, not an anagram
"""

# Approach 1: Two Dictionaries
def is_anagram_two_dict(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count_s, count_t = {}, {}
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    
    return count_s == count_t


# Approach 2: One Dictionary (Optimized)
def is_anagram_one_dict(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        count[char] = count.get(char, 0) - 1
        if count[char] < 0:
            return False
    
    return all(v == 0 for v in count.values())


# Edge cases tested
if __name__ == "__main__":
    # Normal case
    assert is_anagram_one_dict("listen", "silent") == True
    # Length mismatch
    assert is_anagram_one_dict("ab", "abc") == False
    # Missing character
    assert is_anagram_one_dict("ab", "ac") == False
    # Negative frequency
    assert is_anagram_one_dict("ab", "aa") == False
    # Remaining positive
    assert is_anagram_one_dict("abc", "abb") == False
    print("All test cases passed!")
