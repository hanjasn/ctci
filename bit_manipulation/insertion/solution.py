"""
Insertion

You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to insert M into N such that M starts
at bit i and ends at bit j. You can assume that the bits i through j have enough space to fit all of M. That is, if M = 10011,
you can assume that there are at least 5 bits between i and j. You would not, for example, have j = 3 and i = 2, because M could
not fully fit between bit 3 and bit 2.

Input:  N = 100 0000 0000, M = 10011, i = 2, j = 6
Output: N = 100 0100 1100
"""


class Solution:
  def update_bits(self, n: int, m: int, i: int, j: int) -> int:
    left = ~0 << (j + 1)
    right = (1 << i) - 1
    mask = left | right

    n_cleared = n & mask
    m_shifted = m << i
    return n_cleared | m_shifted