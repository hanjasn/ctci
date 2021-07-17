import unittest
from remove_dups import *

class RemoveDupsTest(unittest.TestCase):
  def setUp(self):
    self.sol = Solution1()
    self.list = LinkedList()

  def test_1(self) -> None:
    self.list.push(3)
    self.list.push(1)
    self.list.push(1)
    self.list.push(2)
    self.list.push(1)
    self.sol.remove_dups(self.list.head)
    self.assertEqual("1, 2, 3", self.list.print_list())
  
  def test_2(self) -> None:
    self.list.push(5)
    self.list.push(4)
    self.list.push(3)
    self.list.push(2)
    self.list.push(1)
    self.sol.remove_dups(self.list.head)
    self.assertEqual("1, 2, 3, 4, 5", self.list.print_list())
  
  def test_3(self) -> None:
    self.sol.remove_dups(self.list.head)
    self.assertEqual("", self.list.print_list())
  
  def test_4(self) -> None:
    self.list.push(0)
    self.sol.remove_dups(self.list.head)
    self.assertEqual("0", self.list.print_list())