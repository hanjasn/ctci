"""
Magic Index

A magic index in an array A[0...n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
"""
from typing import List


# Time: O(n)
# Space: O(logn)
# Binary search algorithm for non distinct integers
class Solution1:
    def find_magic_index(self, arr: List[int]) -> int:
        return self._find_magic_index(arr, 0, len(arr) - 1)
    
    def _find_magic_index(self, arr: List[int], left: int, right: int) -> int:
        if right < left:
            return -1
        
        mid = (left + right)//2
        if arr[mid] == mid:
            return mid
        
        index = self._find_magic_index(arr, left, min(arr[mid], mid - 1))
        if index != -1:
            return index
        return self._find_magic_index(arr, max(arr[mid], mid + 1), right)


# Time: O(logn)
# Space: O(logn)
# Binary search algorithm for distinct integers
class Solution2:
    def find_magic_index(self, arr: List[int]) -> int:
        return self._find_magic_index(arr, 0, len(arr) - 1)

    def _find_magic_index(self, arr: List[int], left: int, right: int) -> int:
        if right < left:
            return -1
        
        mid = (left + right)//2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            return self._find_magic_index(arr, left, mid - 1)
        return self._find_magic_index(arr, mid + 1, right)


# Time: O(n)
# Space: O(1)
# Brute-force algorithm
class Solution3:
    def find_magic_index(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if arr[i] == i:
                return i
        return -1