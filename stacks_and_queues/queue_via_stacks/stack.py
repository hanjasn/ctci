from typing import TypeVar


T = TypeVar('T')


class Stack:
  def __init__(self) -> None:
    self.top = None
  
  def push(self, data: T) -> None:
    node = _Node(data)
    node.next = self.top
    self.top = node

  def pop(self) -> T:
    if self.is_empty():
      return None

    data = self.peek()
    self.top = self.top.next
    return data

  def peek(self) -> T:
    if self.is_empty():
      return None
    
    return self.top.data

  def is_empty(self) -> bool:
    return self.top == None


class _Node:
  def __init__(self, data: T) -> None:
    self.data = data
    self.next = None