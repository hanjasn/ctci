from typing import TypeVar


T = TypeVar('T')


class Queue:
  def __init__(self) -> None:
    self.first = None
    self.last = None
  
  def add(self, data: T) -> None:
    node = _Node(data)
    if self.last:
      self.last.next = node
    self.last = node
    if self.first == None:
      self.first = self.last

  def remove(self) -> T:
    if self.empty():
      return None
    
    data = self.first.data
    self.first = self.first.next
    if self.first == None:
      self.last = None

    return data

  def peek(self) -> T:
    if self.empty():
      return None
    
    return self.first.data

  def empty(self) -> bool:
    return self.first == None


class _Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None