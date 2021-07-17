"""
Remove Dups

Write code to remove duplicates from an unsorted linked list. How would you solve this problem if a temporary buffer is not
allowed?
"""
from linked_list import *

# Time: O(n)
# Space: O(n - m) where m represents all duplicates
# Iterate through list while using set to check for duplicates
class Solution1:
  def remove_dups(self, head: Node) -> None:
    if head == None:
      return

    s = set()
    node = Node(0)
    node.next = head
    while node.next != None:
      if node.next.data in s:
        node.next = node.next.next
      else:
        s.add(node.next.data)
        node = node.next

# Time: O(n*logn)
# Space: O(n)
# Sort, then check adjacent elements for duplicates
class Solution2:
  def remove_dups(self, head: Node) -> None:
    if head == None:
      return

    self.merge_sort(head)
    while head.next != None:
      if head.next.data == head.data:
        head.next = head.next.next
      else:
        head = head.next

  def merge_sort(self, head: Node) -> None:
    arr = []
    node = head
    while node != None:
      arr.append(node.data)
      node = node.next
    self._merge_sort(arr, 0, len(arr) - 1)

    node = head
    i = 0
    while node != None:
      node.data = arr[i]
      node = node.next
      i += 1

  def _merge_sort(self, arr: list, low: int, high: int) -> None:
    if low < high:
      mid = int((low + high)/2)
      self._merge_sort(arr, low, mid)
      self._merge_sort(arr, mid + 1, high)
      self._merge(arr, low, mid, high)

  def _merge(self, arr: list, low: int, mid: int, high: int) -> None:
    temp = []
    for i in range(len(arr)):
      temp.append(arr[i])
    current, left, right = low, low, mid + 1

    while left <= mid and right <= high:
      if temp[left] <= temp[right]:
        arr[current] = temp[left]
        left += 1
      else:
        arr[current] = temp[right]
        right += 1
      current += 1
    while left <= mid:
      arr[current] = temp[left]
      left += 1
      current += 1


# Time: O(n^2)
# Space: O(1)
# Runner technique
class Solution3:
  def remove_dups(self, head: Node) -> None:
    while head != None:
      runner = head
      while runner.next != None:
        if runner.next.data == head.data:
          runner.next = runner.next.next
        else:
          runner = runner.next
      head = head.next