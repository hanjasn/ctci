"""
Is Unique

Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""

# Time: O(n)
# Space: O(1)
# Assuming an ASCII string
class Solution1:
  def is_unique(self, s):
    if len(s) > 128:
      return False
    unique_chars = [False] * 128
    for c in s:
      c = ord(c)
      if unique_chars[c]:
        return False
      unique_chars[c] = True
    return True

# Time: O(n*logn)
# Space: O(logn)
# Sort the string and then compare adjacent pairs of characters
class Solution2:
  def is_unique(self, s):
    if len(s) < 2:
      return True
    s_list = list(s)
    self.quick_sort(s_list, 0, len(s_list) - 1)
    for i in range(1, len(s_list)):
      if s_list[i] == s_list[i-1]:
        return False
    return True

  def quick_sort(self, arr, left, right):
    index = self._partition(arr, left, right)
    if left < index - 1:
      self.quick_sort(arr, left, index - 1)
    if index < right:
      self.quick_sort(arr, index, right)

  def _partition(self, arr, left, right):
    pivot = arr[int((left + right)/2)]
    while left <= right:
      while arr[left] < pivot:
        left += 1
      while arr[right] > pivot:
        right -= 1
      if left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return left

# Time: O(n^2)
# Space: O(1)
# Brute-force method
class Solution3:
  def is_unique(self, s):
    for i in range(len(s)):
      for j in range(len(s)):
        if i == j:
          continue
        if s[i] == s[j]:
          return False
    return True