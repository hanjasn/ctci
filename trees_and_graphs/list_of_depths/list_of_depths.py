"""
List of Depths

Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with
depth D, you'll have D linked lists).
"""
from typing import TypeVar
from linked_list import *
from binary_tree import *


T = TypeVar('T')


# Time: O(n)
# Space: O(n)
class SolutionDFS:  
  def list_of_depths(self, node: BinaryTreeNode) -> list:
    depth_list = []
    self._list_of_depths(node, depth_list, 0)
    return depth_list

  def _list_of_depths(self, node: BinaryTreeNode, depth_list: list, depth: int) -> None:
    if node == None:
      return
    
    if len(depth_list) == depth:
      depth_list.append(LinkedList())
    depth_list[depth].add(node)
    self._list_of_depths(node.left, depth_list, depth + 1)
    self._list_of_depths(node.right, depth_list, depth + 1)
  

# Time: O(n)
# Space: O(n)
class SolutionBFS:
  def list_of_depths(self, node: BinaryTreeNode) -> list:
    if node == None:
      return []
    
    depth_list = []
    current = LinkedList()
    current.add(node)
    while current.get_size() > 0:
      depth_list.append(current)

      parents = current
      current = LinkedList()
      parent = parents.head
      while parent != None:
        if parent.data.left != None:
          current.add(parent.data.left)
        if parent.data.right != None:
          current.add(parent.data.right)
        parent = parent.next
    return depth_list