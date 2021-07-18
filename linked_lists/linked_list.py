from typing import TypeVar


T = TypeVar('T')


class LinkedList:
  def __init__(self) -> None:
    self.head = None
  
  def push(self, data: T) -> None:
    node = Node(data)
    node.next = self.head
    self.head = node

  def __str__(self) -> str:
    result = ""
    node = self.head
    while node:
      if node.next == None:
        result += str(node.data)
      else:
        result += f'{str(node.data)}, '
      node = node.next
    
    return result
  

class Node:
  def __init__(self, data: T) -> None:
    self.data = data
    self.next = None