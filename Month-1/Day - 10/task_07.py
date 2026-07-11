# Task 7: Two Sum — Optimized (O(n) with hash map)

def two_sum_optimized(nums, target):
    seen = {}  # number -> index
    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed], i]
        seen[num] = i
    return []

# Test
nums = [2, 7, 11, 15]
target = 9
print(f"nums={nums}, target={target}")
print(f"Result: {two_sum_optimized(nums, target)}")  # [0, 1]

# Edge case
nums2 = [3, 2, 4]
target2 = 6
print(f"nums={nums2}, target={target2}")
print(f"Result: {two_sum_optimized(nums2, target2)}")  # [1, 2]
