import unittest
from delete_middle_node import *

class Delete(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()
    self.list = LinkedList()

  def test_1(self):
    node_a = Node('a')
    node_b = Node('b')
    node_c = Node('c')
    node_d = Node('d')
    node_e = Node('e')
    self.list.head = node_a
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d
    node_d.next = node_e

    self.assertTrue(self.sol.delete(node_c))
    self.assertEqual("a, b, d, e", self.list.print_list())
  
  def test_2(self):
    node_a = Node('a')
    node_b = Node('b')
    node_c = Node('c')
    node_d = Node('d')
    node_e = Node('e')
    self.list.head = node_a
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d
    node_d.next = node_e

    self.assertFalse(self.sol.delete(node_e))
    self.assertNotEqual("a, b, c, d", self.list.print_list())

  def test_3(self):
    self.assertFalse(self.sol.delete(self.list.head))
    self.assertEqual("", self.list.print_list())