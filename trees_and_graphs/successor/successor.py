"""
Successor

Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. You may assume that
each node has a link to its parent.
"""
from typing import TypeVar


T = TypeVar('T')


# Time: O(logn) when balanced
# Space: O(1)
# Iterative solution
# 
# Time: O(logn) when balanced
# Space: O(logn) when balanced
# Recursive solution
class BinaryTreeNode:
  def __init__(self, data: T) -> None:
    self.data = data
    self.left = None
    self.right = None
    self.parent = None
    self.size = 1
  
  def insert_in_order(self, data: T) -> None:
    if data <= self.data:
      if self.left == None:
        self.set_left(BinaryTreeNode(data))
      else:
        self.left.insert_in_order(data)
    else:
      if self.right == None:
        self.set_right(BinaryTreeNode(data))
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
  
  def successor(self) -> 'BinaryTreeNode':
    if self.right != None:
      return self.right.find_min()

    node = self
    while node.parent != None:
      if node == node.parent.left:
        return node.parent
      node = node.parent
    return None

  # Recursive solution
  # def _successor(self) -> 'BinaryTreeNode':
  #   if self.parent != None:
  #     if self == self.parent.left:
  #       return self.parent
  #     return self.parent._successor()
  #   return None
  
  def find_min(self) -> 'BinaryTreeNode':
    node = self
    while node.left != None:
      node = node.left
    return node

  # Recursive solution
  # def find_min(self) -> 'BinaryTreeNode':
  #   return self._find_min(self)
  
  # def _find_min(self, node: 'BinaryTreeNode') -> 'BinaryTreeNode':
  #   if node.left == None:
  #     return node
    
  #   return self._find_min(node.left)
  
  def get_size(self):
    return self.size
  
  def set_left(self, node: 'BinaryTreeNode') -> None:
    self.left = node
    if node != None:
      node.parent = self
  
  def set_right(self, node: 'BinaryTreeNode') -> None:
    self.right = node
    if node != None:
      node.parent = self

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