"""
Flip Bit to Win

You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the length of the longest sequence of 1s
you could create.

Input: 1775 (or: 11011101111)
Output: 8
"""


# Time: O(n) where n is the length of the sequence
# Space: O(1)
class Solution1:
  def length_longest_sequence(self, num: int) -> int:
    curr_length, prev_length, max_length = 0, 0, 1
    while num > 0:
      if (num & 1) == 1:
        curr_length += 1
      else:
        prev_length = 0 if (num & 2 == 0) else curr_length + 1
        curr_length = 0
      max_length = max(max_length, prev_length + curr_length)
      num >>= 1
    return max_length


# Time: O(n) where n is the length of the sequence
# Space: O(n)
class Solution2:
  def length_longest_sequence(self, num: int) -> int:
    binary = self.to_binary_str(num)
    max_ones = 1
    count_ones = 0
    flip = False
    next_ = 0
    i = 0
    while i <= len(binary):
      if i == len(binary):
        max_ones = max(max_ones, count_ones)
      elif binary[i] == "0":
        if flip == True:
          max_ones = max(max_ones, count_ones)
          flip = False
          count_ones = 0
          i = next_
          continue
        else:
          flip = True
          next_ = i + 1
      count_ones += 1
      i += 1
    return max_ones
  
  # def length_longest_sequence(self, num: int) -> int:
  #   binary = self.to_binary_str(num)
  #   zero_indices = [-1]
  #   for i in range(len(binary)):
  #     if binary[i] == "0":
  #       zero_indices.append(i)
  #   if len(zero_indices) < 2:
  #     return len(binary)

  #   max_ones = 1
  #   for index in zero_indices:
  #     flip = False
  #     count_ones = 0
  #     for i in range(index + 1, len(binary)):
  #       if binary[i] == "0":
  #         if flip == True:
  #           break
  #         flip = True
  #       count_ones += 1
      
  #     max_ones = max(max_ones, count_ones)
  #   return max_ones
  
  def to_binary_str(self, num: int) -> str:
    if num == 0:
      return "0"

    result = ""
    while num > 0:
      result = str(num % 2) + result
      num //= 2
    return result