"""
Queue via Stacks

Implement a MyQueue class which implements a queue using two stacks.
"""
from typing import TypeVar
from stack import Stack


T = TypeVar('T')


# The end stack continuously adds elements and only moves everything to the front stack once the front stack becomes empty.
class Queue:
  def __init__(self) -> None:
    self.front = Stack()
    self.end = Stack()
  
  def add(self, data: T) -> None:
    self.end.push(data)

  def remove(self) -> T:
    self.shift()
    return self.front.pop()

  def peek(self) -> T:
    self.shift()
    return self.front.peek()
  
  def shift(self) -> bool:
    if self.empty() or not self.front.empty():
      return False
    
    while not self.end.empty():
      self.front.push(self.end.pop())
    return True

  def empty(self) -> bool:
    return self.front.empty() and self.end.empty()
  
  def print_values(self) -> str:
    result = ""
    node = self.front.top
    if self.end.empty():
      while node:
        if node.next == None:
          result += str(node.data)
        else:
          result += str(node.data) + ", "
        node = node.next
      return result
    else:
      while node:
        result += str(node.data) + ", "
        node = node.next
    
    reverse = Stack()
    node = self.end.top
    while node:
      reverse.push(node.data)
      node = node.next
    
    node = reverse.top
    while node:
      if node.next == None:
        result += str(node.data)
      else:
        result += str(node.data) + ", "
      node = node.next

    return result