import unittest
from validate_bst import *


class IsBST(unittest.TestCase):
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
    self.assertTrue(root.is_BST())
  
  def test_2(self) -> None:
    root = BinaryTreeNode(5)
    root.insert_in_order(2)
    root.insert_in_order(1)
    root.insert_in_order(3)
    root.insert_in_order(4)
    root.insert_in_order(7)
    root.insert_in_order(6)
    root.insert_in_order(8)
    root.insert_in_order(9)
    root.left.data = 10
    self.assertFalse(root.is_BST())
  
  def test_3(self) -> None:
    root = BinaryTreeNode(5)
    root.insert_in_order(2)
    root.insert_in_order(1)
    root.insert_in_order(3)
    root.insert_in_order(4)
    root.insert_in_order(7)
    root.insert_in_order(6)
    root.insert_in_order(8)
    root.insert_in_order(9)
    node = root.find(8)
    node.right.data = -1
    self.assertFalse(root.is_BST())
  
  def test_4(self) -> None:
    root = BinaryTreeNode(20)
    l = BinaryTreeNode(10)
    r = BinaryTreeNode(30)
    lr = BinaryTreeNode(25)
    root.left = l
    root.right = r
    l.right = lr
    self.assertFalse(root.is_BST())
  
  def test_5(self) -> None:
    root = BinaryTreeNode(1)
    root.insert_in_order(2)
    root.insert_in_order(3)
    root.insert_in_order(4)
    root.insert_in_order(5)
    self.assertTrue(root.is_BST())
  
  def test_6(self) -> None:
    root = BinaryTreeNode(5)
    root.insert_in_order(4)
    root.insert_in_order(3)
    root.insert_in_order(2)
    root.insert_in_order(1)
    self.assertTrue(root.is_BST())
  
  def test_7(self) -> None:
    root = BinaryTreeNode(1)
    self.assertTrue(root.is_BST())


class IsBSTWithDup(unittest.TestCase):
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
    self.assertTrue(root.is_BST_with_dup())
  
  def test_2(self) -> None:
    root = BinaryTreeNode(5)
    root.insert_in_order(2)
    root.insert_in_order(1)
    root.insert_in_order(3)
    root.insert_in_order(4)
    root.insert_in_order(7)
    root.insert_in_order(6)
    root.insert_in_order(8)
    root.insert_in_order(9)
    root.left.data = 10
    self.assertFalse(root.is_BST_with_dup())
  
  def test_3(self) -> None:
    root = BinaryTreeNode(5)
    root.insert_in_order(2)
    root.insert_in_order(1)
    root.insert_in_order(3)
    root.insert_in_order(4)
    root.insert_in_order(7)
    root.insert_in_order(6)
    root.insert_in_order(8)
    root.insert_in_order(9)
    node = root.find(8)
    node.right.data = -1
    self.assertFalse(root.is_BST_with_dup())
  
  def test_4(self) -> None:
    root = BinaryTreeNode(20)
    l = BinaryTreeNode(10)
    r = BinaryTreeNode(30)
    lr = BinaryTreeNode(25)
    root.left = l
    root.right = r
    l.right = lr
    self.assertFalse(root.is_BST_with_dup())
  
  def test_5(self) -> None:
    root = BinaryTreeNode(20)
    l = BinaryTreeNode(20)
    r = BinaryTreeNode(30)
    ll = BinaryTreeNode(15)
    root.left = l
    root.right = r
    l.left = ll
    self.assertTrue(root.is_BST_with_dup())
  
  def test_6(self) -> None:
    root = BinaryTreeNode(20)
    l = BinaryTreeNode(10)
    r = BinaryTreeNode(30)
    lr = BinaryTreeNode(10)
    root.left = l
    root.right = r
    l.right = lr
    self.assertFalse(root.is_BST_with_dup())
  
  def test_7(self) -> None:
    root = BinaryTreeNode(1)
    root.insert_in_order(2)
    root.insert_in_order(3)
    root.insert_in_order(4)
    root.insert_in_order(5)
    self.assertTrue(root.is_BST_with_dup())
  
  def test_8(self) -> None:
    root = BinaryTreeNode(5)
    root.insert_in_order(4)
    root.insert_in_order(3)
    root.insert_in_order(2)
    root.insert_in_order(1)
    self.assertTrue(root.is_BST_with_dup())
  
  def test_9(self) -> None:
    root = BinaryTreeNode(1)
    self.assertTrue(root.is_BST_with_dup())