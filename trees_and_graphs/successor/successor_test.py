import unittest
from successor import *


class GetSuccessorTest(unittest.TestCase):
  def test_1(self) -> None:
    root = BinaryTreeNode(20)
    root.insert_in_order(10)
    root.insert_in_order(5)
    root.insert_in_order(15)
    root.insert_in_order(30)
    root.insert_in_order(25)
    root.insert_in_order(35)
    self.assertEqual(25, root.successor().data)
  
  def test_2(self) -> None:
    root = BinaryTreeNode(20)
    root.insert_in_order(10)
    root.insert_in_order(5)
    root.insert_in_order(15)
    root.insert_in_order(30)
    root.insert_in_order(25)
    root.insert_in_order(35)
    root.insert_in_order(40)
    node = root.find(30)
    self.assertEqual(35, node.successor().data)
  
  def test_3(self) -> None:
    root = BinaryTreeNode(20)
    root.insert_in_order(10)
    root.insert_in_order(5)
    node = root.find(10)
    self.assertEqual(20, node.successor().data)
  
  def test_4(self) -> None:
    root = BinaryTreeNode(20)
    root.insert_in_order(30)
    root.insert_in_order(25)
    node = root.find(30)
    self.assertEqual(None, node.successor())
  
  def test_5(self) -> None:
    root = BinaryTreeNode(20)
    root.insert_in_order(10)
    root.insert_in_order(5)
    root.insert_in_order(15)
    root.insert_in_order(30)
    root.insert_in_order(25)
    root.insert_in_order(35)
    node = root.find(15)
    self.assertEqual(20, node.successor().data)

  def test_6(self) -> None:
    root = BinaryTreeNode(20)
    root.insert_in_order(10)
    root.insert_in_order(5)
    root.insert_in_order(15)
    self.assertEqual(None, root.successor())