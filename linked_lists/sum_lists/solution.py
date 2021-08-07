"""
Sum Lists

You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.

EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
"""
from typing import Tuple
from linked_list import *


# Time: O(n) where n is the larger of the two lists
# Space: O(n)
class Solution1:
    def sum_lists(self, lst1: LinkedList, lst2: LinkedList) -> LinkedList:
        lst = LinkedList()
        carry = 0
        head1, head2 = lst1.head, lst2.head
        while head1 != None or head2 != None or carry == 1:
            value = carry
            if head1 != None:
                value += head1.data
                head1 = head1.next
            if head2 != None:
                value += head2.data
                head2 = head2.next

            lst.add(value % 10)
            carry = 1 if value >= 10 else 0
        return lst

    def sum_lists_reversed(self, lst1: LinkedList, lst2: LinkedList) -> LinkedList:
        self.pad_zeros(lst1, lst2)
        [lst, carry] = self._sum_lists_reversed(lst1.head, lst2.head)
        if carry == 1:
            lst.add_left(1)
        return lst

    def _sum_lists_reversed(
        self, head1: LinkedListNode, head2: LinkedListNode
    ) -> Tuple[LinkedList, int]:
        if head1 == None:
            return (LinkedList(), 0)
        
        [lst, carry] = self._sum_lists_reversed(head1.next, head2.next)
        value = carry + head1.data + head2.data
        lst.add_left(value % 10)
        carry = 1 if value >= 10 else 0
        return (lst, carry)

    def pad_zeros(self, lst1: LinkedList, lst2: LinkedList) -> None:
        diff = abs(lst1.get_size() - lst2.get_size())
        if lst1.get_size() > lst2.get_size():
            for _ in range(diff):
                lst2.add_left(0)
        else:
            for _ in range(diff):
                lst1.add_left(0)

    def get_val(self, lst: LinkedList) -> int:
        value = 0
        i = 0
        head = lst.head
        while head != None:
            value += head.data * 10 ** i
            i += 1
            head = head.next
        return value

    def get_val_reversed(self, lst: LinkedList) -> int:
        value = 0
        i = lst.get_size() - 1
        head = lst.head
        while head != None:
            value += head.data * 10 ** i
            i -= 1
            head = head.next
        return value


# Time: O(n)
# Space: O(n)
# Sum each list value representation, add each sum, then convert the summed value back to a list.
class Solution2:
    def sum_lists(self, lst1: LinkedList, lst2: LinkedList) -> LinkedList:
        total = self.get_val(lst1) + self.get_val(lst2)
        return self.convert_to_list(total)

    def sum_lists_reversed(self, lst1: LinkedList, lst2: LinkedList) -> LinkedList:
        total = self.get_val_reversed(lst1) + self.get_val_reversed(lst2)
        return self.convert_to_list_reversed(total)

    def get_val(self, lst: LinkedList) -> int:
        total = 0
        i = 0
        head = lst.head
        while head != None:
            total += head.data * 10 ** i
            i += 1
            head = head.next
        return total

    def get_val_reversed(self, lst: LinkedList) -> int:
        total = 0
        i = lst.get_size() - 1
        head = lst.head
        while head != None:
            total += head.data * 10 ** i
            i -= 1
            head = head.next
        return total

    def convert_to_list(self, total: int) -> LinkedList:
        lst = LinkedList()
        if total != 0:
            while total > 0:
                lst.add(total % 10)
                total //= 10
        return lst

    def convert_to_list_reversed(self, total: int) -> LinkedList:
        lst = self.convert_to_list(total)
        self.reverse_list(lst)
        return lst

    def reverse_list(self, lst: LinkedList) -> None:
        prev = None
        curr = lst.head
        while curr != None:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        lst.head = prev
