"""
Minimal Tree

Given a sorted (increasing order) array with unique integer elements, write an algorithm to create
a binary search tree with minimal height.
"""


class Node:
  def __init__(self, data: int) -> None:
    self.data = data
    self.left = None
    self.right = None


# Time: O(n)
# Space: O(logn)
# Recursively split the array in half on each side until you reach the end, and then set the current node's left and right
# children to the return values (nodes) of the recursive calls.
class Solution:
  def build_BST(self, arr: list) -> Node:
    return self._build_BST(arr, 0, len(arr) - 1)
  
  def _build_BST(self, arr: list, left: int, right: int) -> Node:
    if left == right:
      return Node(arr[left])
    elif right < left:
      return None
    
    mid = (left + right)//2
    node = Node(arr[mid])
    node.left = self._build_BST(arr, left, mid - 1)
    node.right = self._build_BST(arr, mid + 1, right)
    return node
  
  def print_in_order(self, node) -> str:
    if node == None:
      return "[]"
    
    result = "[" + self._print_in_order(node)
    result = result[0:-2] + "]"
    return result

  def _print_in_order(self, node) -> str:
    if node == None:
      return ""

    result = ""
    result += self._print_in_order(node.left)
    result += str(node.data) + ", "
    result += self._print_in_order(node.right)
    return result
