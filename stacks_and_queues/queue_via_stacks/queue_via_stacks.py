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

  def add(self, data) -> None:
    self.end.push(data)

  def remove(self) -> T:
    if self.front.is_empty():
      self.move_to_front()
    return self.front.pop()

  def peek(self) -> T:
    if self.front.is_empty():
      self.move_to_front()
    return self.front.peek()

  def is_empty(self) -> bool:
    return self.front.is_empty() and self.end.is_empty()
  
  def move_to_front(self) -> None:
    while self.end.peek():
      self.front.push(self.end.pop())

  def print_values(self) -> str:
    result = ""
    node = self.front.top
    if self.end.is_empty():
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