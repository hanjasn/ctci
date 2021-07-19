import unittest
from list_of_depths import *


class ListOfDepthsTest(unittest.TestCase):
  def setUp(self) -> None:
    self.sol = SolutionBFS()
  
  def test_1(self) -> None:
    root = BinaryTreeNode(5)
    root.insert_in_order(2)
    root.insert_in_order(1)
    root.insert_in_order(3)
    root.insert_in_order(4)
    root.insert_in_order(7)
    root.insert_in_order(6)
    root.insert_in_order(8)
    root.insert_in_order(9)
    lists = self.sol.list_of_depths(root)
    self.assertEqual(4, len(lists))
    for depth_list in lists:
      print(depth_list)
    print()
  
  def test_2(self) -> None:
    root = BinaryTreeNode(1)
    lists = self.sol.list_of_depths(root)
    self.assertEqual(1, len(lists))
    for depth_list in lists:
      print(depth_list)
    print()
  
  def test_3(self) -> None:
    lists = self.sol.list_of_depths(None)
    self.assertEqual(0, len(lists))
    self.assertEqual("[]", str(lists))