# Task 6: Two Sum — Brute Force

def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Test
nums = [2, 7, 11, 15]
target = 9
print(f"nums={nums}, target={target}")
print(f"Result: {two_sum_brute(nums, target)}")  # [0, 1]
