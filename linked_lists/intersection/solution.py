"""
Intersection

Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
"""
from typing import Tuple
from linked_list import LinkedList, LinkedListNode


# Time: O(n + m) where n is the length of list A and m is the length of list B
# Space: O(1)
class Solution:
    def intersection(self, lst1: LinkedList, lst2: LinkedList) -> LinkedListNode:
        if lst1.head == None or lst2.head == None:
            return None
        
        [tail1, size1] = self.get_tail_and_size(lst1)
        [tail2, size2] = self.get_tail_and_size(lst2)
        if tail1 != tail2:
            return None
        
        head1, head2 = lst1.head, lst2.head
        if size1 > size2:
            for _ in range(size1 - size2):
                head1 = head1.next
        else:
            for _ in range(size2 - size1):
                head2 = head2.next
        
        while head1 != None:
            if head1 == head2:
                return head1
            head1 = head1.next
            head2 = head2.next
    
    def get_tail_and_size(self, lst: LinkedList) -> Tuple[LinkedListNode, int]:
        size = 1
        tail = lst.head
        while tail.next != None:
            size += 1
            tail = tail.next
        return (tail, size)