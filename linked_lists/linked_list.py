from typing import TypeVar


T = TypeVar('T')


class LinkedList:
  def __init__(self) -> None:
    self.head = None
    self.tail = None
    self.size = 0
  
  def add(self, data: T) -> None:
    self.size += 1
    
    node = LinkedListNode(data)
    if self.tail != None:
      self.tail.next = node
    self.tail = node

    if self.head == None:
      self.head = self.tail
  
  def get_size(self) -> int:
    return self.size

  def __str__(self) -> str:
    result = ""
    node = self.head
    while node != None:
      result += str(node.data)
      if node.next != None:
        result += ", "
      node = node.next
    return result
  

class LinkedListNode:
  def __init__(self, data: T) -> None:
    self.data = data
    self.next = None