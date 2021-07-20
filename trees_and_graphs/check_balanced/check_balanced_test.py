import unittest
from check_balanced import *


class IsBalancedTest(unittest.TestCase):
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
    self.assertTrue(root.is_balanced())
  
  def test_2(self) -> None:
    root = BinaryTreeNode(5)
    root.insert_in_order(2)
    root.insert_in_order(1)
    root.insert_in_order(3)
    root.insert_in_order(4)
    root.insert_in_order(6)
    root.insert_in_order(7)
    root.insert_in_order(8)
    self.assertFalse(root.is_balanced())
  
  def test_3(self) -> None:
    root = BinaryTreeNode(10)
    root.insert_in_order(5)
    root.insert_in_order(2)
    root.insert_in_order(1)
    root.insert_in_order(3)
    root.insert_in_order(4)
    root.insert_in_order(7)
    root.insert_in_order(6)
    root.insert_in_order(8)
    root.insert_in_order(9)
    root.insert_in_order(15)
    root.insert_in_order(12)
    root.insert_in_order(17)
    self.assertFalse(root.is_balanced())
  
  def test_4(self) -> None:
    root = BinaryTreeNode(1)
    root.insert_in_order(2)
    root.insert_in_order(3)
    root.insert_in_order(4)
    root.insert_in_order(5)
    self.assertFalse(root.is_balanced())

  def test_5(self) -> None:
    root = BinaryTreeNode(5)
    root.insert_in_order(4)
    root.insert_in_order(3)
    root.insert_in_order(2)
    root.insert_in_order(1)
    self.assertFalse(root.is_balanced())
  
  def test_6(self) -> None:
    root = BinaryTreeNode(1)
    self.assertTrue(root.is_balanced())