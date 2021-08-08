"""
Palindrome

Implement a function to check if a linked list is a palindrome.
"""
from linked_list import LinkedList
from stack import Stack


# Time: O(n)
# Space: O(n) for stack
class Solution:
    def is_palindrome(self, lst: LinkedList) -> bool:
        half = Stack()
        head = runner = lst.head
        while runner != None and runner.next != None:
            half.push(head.data)
            head = head.next
            runner = runner.next.next
        if runner != None:
            head = head.next
        
        while head != None:
            if half.pop() != head.data:
                return False
            head = head.next
        return True