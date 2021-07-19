from typing import TypeVar


T = TypeVar('T')


class BinaryTreeNode:
  def __init__(self, data: T) -> None:
    self.data = data
    self.left = None
    self.right = None
  
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
  
  def print_in_order(self) -> str:
    result = "[" + self._print_in_order(self)
    result = result[0:-2] + "]"
    return result

  def _print_in_order(self, node: 'BinaryTreeNode') -> str:
    if node == None:
      return ""

    result = ""
    result += self._print_in_order(node.left)
    result += str(node.data) + ", "
    result += self._print_in_order(node.right)
    return result