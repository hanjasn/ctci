"""
Check Permutation

Given two strings, write a method to decide if one is a permutation of the other.
"""


# Time: O(n)
# Space: O(1)
# Assume case sensitive, and whitespace counts
# Assuming ASCII encoding
class Solution1:
  def check_permutation(self, s1, s2):
    if len(s1) != len(s2):
      return False
    
    chars = [0] * 128
    for c in s1:
      chars[ord(c)] += 1
    for c in s2:
      chars[ord(c)] -= 1
      if chars[ord(c)] < 0:
        return False
    return True


# Time: O(n*logn)
# Space: O(logn)
# Assume case sensitive, and white space counts
# If the strings are not the same length, return false. Sort the strings and then compare them to determine if one is a
# permutation of the other.
class Solution2:
  def check_permutation(self, s1, s2):
    if len(s1) != len(s2):
      return False
    s1_sorted = self.quick_sort(s1)
    s2_sorted = self.quick_sort(s2)
    if s1_sorted != s2_sorted:
      return False
    else:
      return True

  def quick_sort(self, s):
    s_list = list(s)
    self._quick_sort(s_list, 0, len(s_list) - 1)
    return ''.join(s_list)

  def _quick_sort(self, arr, left, right):
    if left < right:
      index = self._partition(arr, left, right)
      self._quick_sort(arr, left, index - 1)
      self._quick_sort(arr, index, right)

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