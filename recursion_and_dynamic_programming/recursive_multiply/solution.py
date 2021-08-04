"""
Recursive Multiply

Write a recursive function to multiply two numbers without using the * operator. You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.
"""


# Time: O(log(n)) where n is the smaller of the two numbers
# Space: O(log(n))
# Using bit-shifting
# 3 * 11
# 3 + (3 * 10)
# 3 + (6 * 5)
# 3 + (6 + (6 * 4))
# 3 + (6 + (12 * 2))
# 3 + (6 + (24 * 1))
#
# 8 * 8
# 16 * 4
# 32 * 2
# 64 * 1
# 64 * 0
class Solution1:
    def recursive_multiply(self, n1: int, n2: int) -> int:
        return self._recursive_multiply(max(n1, n2), min(n1, n2))
    
    def _recursive_multiply(self, n1: int, n2: int) -> int:
        if n2 == 0:
            return 0
        elif n2 % 2 == 1:
            return n1 + self._recursive_multiply(n1, n2 - 1)
        return self._recursive_multiply(n1 << 1, n2 >> 1)


# Time: O(n) where n is the smaller of the two numbers
# Space: O(n)
# Brute-force solution
class Solution2:
    def recursive_multiply(self, n1: int, n2: int) -> int:
        return self._recursive_multiply(max(n1, n2), min(n1, n2))
    
    def _recursive_multiply(self, val: int, repeat: int) -> int:
        if repeat == 0:
            return 0
        return val + self._recursive_multiply(val, repeat - 1)