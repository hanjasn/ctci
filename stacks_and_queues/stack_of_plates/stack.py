from typing import TypeVar


T = TypeVar('T')


class Stack:
  def __init__(self) -> None:
    self.top = None
    self.bottom = None
    self.size = 0

  def push(self, data: T) -> None:
    self.size += 1
    node = _Node(data)
    node.below = self.top
    if self.top:
      self.top.above = node
    self.top = node

    if self.size == 1:
      self.bottom = self.top

  def pop(self) -> T:
    if self.is_empty():
      return None

    self.size -= 1
    data = self.peek()
    self.top = self.top.below
    if self.top:
      self.top.above = None
    else:
      self.bottom = None
    return data

  def peek(self) -> T:
    if self.is_empty():
      return None
    
    return self.top.data
  
  def remove_bottom(self) -> T:
    if self.is_empty():
      return None
    
    self.size -= 1
    data = self.bottom.data
    self.bottom = self.bottom.above
    if self.bottom:
      self.bottom.below = None
    return data
  
  def get_size(self) -> int:
    return self.size

  def is_empty(self) -> bool:
    return self.top == None

  def print_values(self) -> str:
    result = ""
    top = self.top
    while top:
      if top.below == None:
        result += str(top.data)
      else:
        result += str(top.data) + ", "
      top = top.below
    return result


class _Node:
  def __init__(self, data: T) -> None:
    self.data = data
    self.above = None
    self.below = None