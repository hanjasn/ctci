"""
Sort Stack

Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you
may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push,
pop, peek, and isEmpty.
"""
from typing import TypeVar


T = TypeVar('T')
# Time: O(n^2) for sort()
# Space: O(n) for sort()
class Stack:
  def __init__(self) -> None:
    self.top = None
    self.size = 0
  
  def push(self, data: T) -> None:
    self.size += 1
    node = _Node(data)
    node.next = self.top
    self.top = node

  def pop(self) -> T:
    if self.is_empty():
      return None
    
    self.size -= 1
    data = self.peek()
    self.top = self.top.next
    return data
    
  def sort(self) -> None:
    if self.size <= 1:
      return
    
    sorted = Stack()
    while not self.is_empty():
      temp = self.pop()
      while not sorted.is_empty() and temp < sorted.peek():
        self.push(sorted.pop())
      sorted.push(temp)
    
    while not sorted.is_empty():
      self.push(sorted.pop())

  def peek(self) -> T:
    if self.is_empty():
      return None
    
    return self.top.data
  
  def get_size(self) -> int:
    return self.size

  def is_empty(self) -> bool:
    return self.top == None
  
  def print_values(self) -> str:
    result = ""
    node = self.top
    while node:
      if node.next == None:
        result += str(node.data)
      else:
        result += str(node.data) + ", "
      node = node.next
    return result


class _Node:
  def __init__(self, data: T) -> None:
    self.data = data
    self.next = None