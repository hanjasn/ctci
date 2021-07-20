"""
Validate BST

Implement a function to check if a binary tree is a binary search tree.
"""
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
  
  # Time: O(n)
  # Space: O(logn) for a balanced tree
  def is_BST_with_dup(self) -> bool:
    return self._is_BST_with_dup(self, None, None)

  def _is_BST_with_dup(self, node: 'BinaryTreeNode', min: T, max: T) -> bool:
    if node == None:
      return True
    
    if (min != None and node.data <= min) or (max != None and node.data > max):
      return False
    
    if self._is_BST_with_dup(node.left, min, node.data) == False or self._is_BST_with_dup(node.right, node.data, max) == False:
      return False
    return True

  # def is_BST_with_dup(self) -> bool:
  #   return self._is_BST_with_dup(self)[0]
  
  # def _is_BST_with_dup(self, node: 'BinaryTreeNode') -> list:
  #   if node == None:
  #     return [True, None]
    
  #   left = self._is_BST_with_dup(node.left)
  #   if left[0] == False:
  #     return [False, None]
  #   right = self._is_BST_with_dup(node.right)
  #   if right[0] == False:
  #     return [False, None]
    
  #   if left[1] == None:
  #     left[1] = node.data
  #   if right[1] == None:
  #     right[1] = node.data
  #   if left[1] > node.data or right[1] < node.data:
  #     return [False, None]
  #   return [True, max(node.data, left[1], right[1])]

  # Time: O(n)
  # Space: O(logn) for a balanced tree
  def is_BST(self) -> bool:
    in_order = self.copy_BST(self)
    for i in range(1, len(in_order)):
      if in_order[i] < in_order[i - 1]:
        return False
    return True
   
  def copy_BST(self, node: 'BinaryTreeNode') -> list:
    in_order = []
    self._copy_BST(self, in_order)
    return in_order

  def _copy_BST(self, node: 'BinaryTreeNode', in_order: list) -> None:
    if node == None:
      return
    
    self._copy_BST(node.left, in_order)
    in_order.append(node.data)
    self._copy_BST(node.right, in_order)

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