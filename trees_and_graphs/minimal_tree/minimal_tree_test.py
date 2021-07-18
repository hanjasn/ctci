import unittest
from minimal_tree import *


class BuildBSTTest(unittest.TestCase):
  def setUp(self) -> None:
    self.sol = Solution()
  
  def test_1(self) -> None:
    arr = [1, 2, 3]
    root = self.sol.build_BST(arr)
    self.assertEqual(str(arr), self.sol.print_in_order(root))

  def test_2(self) -> None:
    arr = [1, 2, 3, 5, 7, 8, 9, 11]
    root = self.sol.build_BST(arr)
    self.assertEqual(str(arr), self.sol.print_in_order(root))
  
  def test_3(self) -> None:
    arr = [1]
    root = self.sol.build_BST(arr)
    self.assertEqual(str(arr), self.sol.print_in_order(root))
  
  def test_4(self) -> None:
    arr = []
    root = self.sol.build_BST(arr)
    self.assertEqual(str(arr), self.sol.print_in_order(root))