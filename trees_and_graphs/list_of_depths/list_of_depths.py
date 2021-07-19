"""
List of Depths

Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g. if you have a tree with
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
    lists = []
    self._list_of_depths(node, lists, 0)
    return lists

  def _list_of_depths(self, node: BinaryTreeNode, lists: list, depth: int) -> None:
    if node == None:
      return
    
    if len(lists) <= depth:
      lists.append(LinkedList())
    lists[depth].add(node.data)
    self._list_of_depths(node.left, lists, depth + 1)
    self._list_of_depths(node.right, lists, depth + 1)


# Time: O(n)
# Space: O(n)
class SolutionBFS:
  def list_of_depths(self, node: BinaryTreeNode) -> list:    
    lists = []
    if node != None:
      current = LinkedList()
      current.add(node)
      while current.get_size() > 0:
        data_list = LinkedList()
        c = current.head
        while c != None:
          data_list.add(c.data.data)
          c = c.next
        lists.append(data_list)

        parents = current
        current = LinkedList()
        parent = parents.head
        while parent != None:
          if parent.data.left != None:
            current.add(parent.data.left)
          if parent.data.right != None:
            current.add(parent.data.right)
          parent = parent.next
    return lists