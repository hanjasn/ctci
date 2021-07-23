from typing import TypeVar


T = TypeVar('T')


class Queue:
  def __init__(self) -> None:
    self.front = None
    self.end = None
  
  def add(self, data: T) -> None:
    node = _Node(data)
    if self.end:
      self.end.next = node
    self.end = node

    if self.front == None:
      self.front = self.end

  def remove(self) -> T:
    if self.empty():
      return None
    
    data = self.peek()
    self.front = self.front.next
    if self.front == None:
      self.end = None
    return data

  def peek(self) -> T:
    if self.empty():
      return None
    
    return self.front.data

  def empty(self) -> bool:
    return self.front == None


class _Node:
  def __init__(self, data: T) -> None:
    self.data = data
    self.next = None