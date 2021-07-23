"""
Successor

Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. You may assume that
each node has a link to its parent.
"""
from typing import TypeVar


T = TypeVar('T')


# Time: O(logn) when balanced, O(n) otherwise
# Space: O(1)
# Iterative solution
# 
# Time: O(logn) when balanced, O(n) otherwise
# Space: O(logn) when balanced, O(n) otherwise
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

  def find_min(self) -> 'BinaryTreeNode':
    node = self
    while node.left != None:
      node = node.left
    return node

  # Recursive solution
  # def successor(self) -> 'BinaryTreeNode':
  #   if self.right != None:
  #     return self.right.find_min()
    
  #   return self._successor(self)

  # def _successor(self, node: 'BinaryTreeNode') -> 'BinaryTreeNode':
  #   if node.parent == None:
  #     return None
    
  #   if node == node.parent.left:
  #     return node.parent
  #   return self._successor(node.parent)

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

  def copy_tree(self) -> list:
    in_order = []
    self._copy_tree(self, in_order)
    return in_order

  def _copy_tree(self, node: 'BinaryTreeNode', in_order: list) -> None:
    if node == None:
      return
    
    self._copy_tree(node.left, in_order)
    in_order.append(node.data)
    self._copy_tree(node.right, in_order)

  def print_tree(self) -> str:
    return str(self.copy_tree())