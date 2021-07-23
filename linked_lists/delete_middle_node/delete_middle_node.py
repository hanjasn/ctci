"""
Delete Middle Node

Implement an algorithm to delete a node in the middle of a singly linked list, given only access to
that node.

Example:
Input: the node c from the linked list a->b->c->d->e
Output: nothing is returned, but the new linked list looks like a->b->d->e
"""
from linked_list import *


# Time: O(n)
# Space: O(1)
# Copy the data over from the next node to the current node until the second last node is reached, and then delete the last node.
class Solution:
  def delete(self, node: LinkedListNode) -> bool:
    if node == None or node.next == None:
      return False
    
    while node.next != None:
      node.data = node.next.data
      if node.next.next == None:
        node.next = None
      else:
        node = node.next
    return True