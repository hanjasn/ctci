"""
Partition

Write code to partition a linked list around a value x, such that all nodes less than x come before
all nodes greater than or equal to x. If x is contained within the list, the values of x only need to
be after the elements less than x.

Example:
Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
from linked_list import *


# Time: O(n)
# Space: O(1)
# Stable solution
# Create two new linked lists with the smaller and larger nodes, and then merge them together, making sure to remove any loops
# and dummy nodes.
class Solution1:
  def partition(self, head: LinkedListNode, partition: int) -> LinkedListNode:
    before = before_head = LinkedListNode(0)
    after = after_head = LinkedListNode(0)
    while head != None:
      if head.data < partition:
        before.next = head
        before = before.next
      else:
        after.next = head
        after = after.next
      head = head.next
    
    after.next = None
    before.next = after_head.next
    return before_head.next


# Time: O(n)
# Space: O(1)
# Unstable solution
# Copy the data of nodes lower than partition to array and then reappend them as new nodes to the head of the list in reverse
# order.
class Solution2:
  def partition(self, head: LinkedListNode, partition: int) -> LinkedListNode:
    arr = []
    node = LinkedListNode(0)
    node.next = head
    while node.next != None:
      if node.next.data < partition:
        if node.next == head:
          arr.append(head.data)
          head = head.next
          node.next = head
        else:
          arr.append(node.next.data)
          node.next = node.next.next
      else:
        node = node.next
    
    for i in range(len(arr) - 1, -1, -1):
      node = LinkedListNode(arr[i])
      node.next = head
      head = node
    return head


# Time: O(n)
# Space: O(1)
# Failed solution
# class Solution3:
#   def partition(self, head: Node, partition: int) -> None:
#     while head.next != None:
#       if head.next.data >= partition:
#         break
#       head = head.next
#     runner = head
#     while runner.next != None:
#       if runner.next.data < partition:
#         break
#       runner = runner.next

#     while head.next != None:
#       if head.next.data >= partition:
#         while runner.next != None:
#           if runner.next.data < partition:
#             self.swap(head, runner)
#             runner = runner.next
#             break
#           runner = runner.next
#         if runner.next == None:
#           break
#       head = head.next
  
#   def swap(self, first: Node, second: Node) -> None:
#     temp = first.next.next
#     first.next.next = second.next.next
#     second.next.next = temp

#     temp = second.next
#     second.next = first.next
#     first.next = temp