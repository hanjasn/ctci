"""
Return Kth to Last

Implement an algorithm to find the kth to last element of a singly linked list.
"""
from linked_list import *


# Time: O(n)
# Space: O(1)
# Using the runner technique, start one pointer from the head and one k elements ahead of the head, and terminate once the
# runner reaches the last element
class Solution1:
  def find_kth_last_element(self, head: LinkedListNode, k: int) -> LinkedListNode:
    runner = head
    for i in range(k):
      runner = runner.next
    
    while runner.next != None:
      head = head.next
      runner = runner.next
    return head


# Time: O(n)
# Space: O(1)
# Find the size, and then calculate the index of the element using the size and k, and the find the corresponding element.
class Solution2:
  def find_kth_last_element(self, head: LinkedListNode, k: int) -> LinkedListNode:
    node = head
    size = 0
    while node != None:
      size += 1
      node = node.next
    
    index = (size - 1) - k
    node = head
    for i in range(index):
      node = node.next
    return node


# Time: O(n)
# Space: O(n) due to recursion
class Solution3:
  def print_kth_last_element(self, head: LinkedListNode, k: int) -> int:
    if head == None:
      return -1
    index = self.print_kth_last_element(head.next, k) + 1
    if index == k:
      print("kth element:", head.data)
    return index