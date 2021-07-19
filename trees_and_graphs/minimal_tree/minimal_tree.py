"""
Minimal Tree

Given a sorted (increasing order) array with unique integer elements, write an algorithm to create
a binary search tree with minimal height.
"""
from binary_tree import BinaryTreeNode


# Time: O(n)
# Space: O(logn)
# Recursively split the array in half on each side until you reach the end, and then set the current node's left and right
# children to the return values (nodes) of the recursive calls.
class Solution:
  def build_BST(self, arr: list) -> BinaryTreeNode:
    return self._build_BST(arr, 0, len(arr) - 1)
  
  def _build_BST(self, arr: list, left: int, right: int) -> BinaryTreeNode:
    if left == right:
      return BinaryTreeNode(arr[left])
    elif right < left:
      return None
    
    mid = (left + right)//2
    node = BinaryTreeNode(arr[mid])
    node.left = self._build_BST(arr, left, mid - 1)
    node.right = self._build_BST(arr, mid + 1, right)
    return node