# Task 3: Two Sum — Hash Map Pattern (Review)

"""
Problem: Given an array of integers nums and an integer target, return indices
of the two numbers that add up to target.

Approach 1: Brute Force O(n²)
- Check every pair

Approach 2: Hash Map O(n)
- For each number, check if (target - num) already seen
- Store seen numbers with their indices
"""

def two_sum_brute(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_optimal(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    assert two_sum_optimal([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_optimal([3, 2, 4], 6) == [1, 2]
    assert two_sum_optimal([3, 3], 6) == [0, 1]
    print("All Two Sum test cases passed!")
