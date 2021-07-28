"""
Next Number

Given a positive integer, print the next smallest and the next largest number that have the same
number of 1 bits in their binary representation.
"""


# Time: O(n) where n is the bit length
# Space: O(n)
# Arithmetic solution
class Solution1:
  def get_prev(self, num: int) -> int:
    temp, c0, c1 = num, 0, 0
    while temp & 1 == 1:
      c1 += 1
      temp >>= 1
    
    if temp == 0:
      return None
    
    while temp & 1 == 0:
      c0 += 1
      temp >>= 1
    
    return num - (1 << c1) - (1 << (c0 - 1)) + 1

  def get_next(self, num: int) -> int:
    temp, c0, c1 = num, 0, 0
    while temp & 1 == 0:
      c0 += 1
      temp >>= 1
    while temp & 1 == 1:
      c1 += 1
      temp >>= 1
    
    return num + (1 << c0) + (1 << (c1 - 1)) - 1


# Time: O(n) where n is the bit length
# Space: O(n)
# Bit manipulation solution
class Solution2:
  def get_prev(self, num: int) -> int:
    temp, c0, c1 = num,  0, 0
    while temp & 1 == 1:
      c1 += 1
      temp >>= 1
    
    if temp == 0:
      return None
    
    while temp & 1 == 0:
      c0 += 1
      temp >>= 1
    p = c0 + c1

    num &= ~0 << (p + 1)
    num |= ((1 << (c1 + 1)) - 1) << (c0 - 1)
    return num

  def get_next(self, num: int) -> int:
    temp, c0, c1 = num, 0, 0
    while temp & 1 == 0:
      c0 += 1
      temp >>= 1
    while temp & 1 == 1:
      c1 += 1
      temp >>= 1
    p = c0 + c1

    num |= (1 << p)
    num &= (~0 << p)
    num |= (1 << (c1 - 1)) - 1
    return num


# Brute force solution
class Solution3:
  def get_prev(self, num: int) -> int:
    count_num = self.count_ones(num)
    i = num - 1
    while self.count_ones(i) != count_num:
      if i == 0:
        return None
      i -= 1
    return i

  def get_next(self, num: int) -> int:
    count_num = self.count_ones(num)
    i = num + 1
    while self.count_ones(i) != count_num:
      i += 1
    return i

  def count_ones(self, num: int) -> int:
    count = 0
    while num > 0:
      if num & 1 == 1:
        count += 1
      num >>= 1
    return count