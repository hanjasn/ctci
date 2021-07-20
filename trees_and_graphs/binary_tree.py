from typing import TypeVar


T = TypeVar('T')


class BinaryTreeNode:
  def __init__(self, data: T) -> None:
    self.data = data
    self.left = None
    self.right = None
    self.size = 1
  
  def insert_in_order(self, data: T) -> None:
    if data <= self.data:
      if self.left == None:
        self.left = BinaryTreeNode(data)
      else:
        self.left.insert_in_order(data)
    else:
      if self.right == None:
        self.right = BinaryTreeNode(data)
      else:
        self.right.insert_in_order(data)
    self.size += 1
  
  def find(self, data: T) -> 'BinaryTreeNode':
    return self._find(self, data)
  
  def _find(self, node: 'BinaryTreeNode', data: T) -> 'BinaryTreeNode':
    if node == None:
      return None
    
    if data == node.data:
      return node
    
    found = self._find(node.left, data)
    if found != None:
      return found
    return self._find(node.right, data)
  
  def get_size(self):
    return self.size

  def print_in_order(self) -> str:
    result = "[" + self._print_in_order(self)
    result = result[0:-2] + "]"
    return result

  def _print_in_order(self, node: 'BinaryTreeNode') -> str:
    result = ""
    if node != None:
      result += self._print_in_order(node.left)
      result += str(node.data) + ", "
      result += self._print_in_order(node.right)
    return result