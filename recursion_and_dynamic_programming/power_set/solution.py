"""
Power Set

Write a method to return all subsets of a set.
"""
from typing import List


# Time: O(n*2^n)
# Space: O(n*2^n)
# Bit manipulation solution
class Solution1:
    def power_set(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range(1 << n):
            result.append([nums[j] for j in range(n) if i & (1 << j) != 0])
        return result


# Time: O(n*2^n)
# Space: O(n*2^n)
# Iterative solution
class Solution2:
    def power_set(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
        return result