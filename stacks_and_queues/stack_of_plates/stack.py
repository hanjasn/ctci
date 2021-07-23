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
    if self.top != None:
      self.top.above = node
    self.top = node

    if self.bottom == None:
      self.bottom = self.top
  
  def pop(self) -> T:
    if self.empty():
      return None
    
    self.size -= 1

    data = self.peek()
    self.top = self.top.below

    if self.top == None:
      self.bottom = None
    else:
      self.top.above = None
    return data
  
  def remove_bottom(self) -> T:
    if self.empty():
      return None
    
    self.size -= 1

    data = self.bottom.data
    self.bottom = self.bottom.above
    if self.bottom == None:
      self.top = None
    else:
      self.bottom.below = None
    return data

  def peek(self) -> T:
    if self.empty():
      return None
    
    return self.top.data
  
  def get_size(self) -> int:
    return self.size
  
  def empty(self) -> bool:
    return self.top == None
  
  def print_values(self) -> str:
    result = ""
    node = self.top
    while node != None:
      result += str(node.data)
      if node.below != None:
        result += ", "
      node = node.below
    return result


class _Node:
  def __init__(self, data: T) -> None:
    self.data = data
    self.above = None
    self.below = None