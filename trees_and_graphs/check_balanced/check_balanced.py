"""
Check Balanced

Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a
tree such that the heights of the two subtrees of any node never differ by more than one.
"""
from typing import TypeVar


T = TypeVar('T')


# Time: O(n)
# Space: O(h)
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
  
  def is_balanced(self) -> bool:
    if self._is_balanced(self) == -2:
      return False
    return True

  def _is_balanced(self, node: 'BinaryTreeNode') -> int:
    if node == None:
      return -1
    
    left_height = self._is_balanced(node.left)
    if left_height == -2:
      return -2
    
    right_height = self._is_balanced(node.right)
    if right_height == -2:
      return -2
    
    diff = left_height - right_height
    if diff < -1 or diff > 1:
      return -2
    return max(left_height, right_height) + 1
  
  # def is_balanced(self) -> bool:
  #   return self._is_balanced(self)[0]

  # def _is_balanced(self, node: 'BinaryTreeNode') -> tuple:
  #   if node == None:
  #     return (True, -1)
    
  #   left, right = self._is_balanced(node.left), self._is_balanced(node.right)
  #   balanced = left[0] and right[0]
  #   diff = left[1] - right[1]
  #   if diff < -1 or diff > 1:
  #     balanced = False
  #   return (balanced, max(left[1], right[1]) + 1)

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