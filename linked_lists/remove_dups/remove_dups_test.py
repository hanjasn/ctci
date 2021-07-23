import unittest
from remove_dups import *

class RemoveDupsTest(unittest.TestCase):
  def setUp(self):
    self.sol = Solution1()
    self.list = LinkedList()

  def test_1(self) -> None:
    self.list.add(3)
    self.list.add(1)
    self.list.add(1)
    self.list.add(2)
    self.list.add(1)
    self.sol.remove_dups(self.list.head)
    self.assertEqual("1, 2, 3", self.list.print_list())
  
  def test_2(self) -> None:
    self.list.add(4)
    self.list.add(3)
    self.list.add(2)
    self.list.add(1)
    self.list.add(1)
    self.sol.remove_dups(self.list.head)
    self.assertEqual("1, 2, 3, 4", self.list.print_list())
  
  # Fails for solution 2 because of sorting
  def test_3(self) -> None:
    self.list.add(1)
    self.list.add(1)
    self.list.add(2)
    self.list.add(3)
    self.list.add(4)
    self.sol.remove_dups(self.list.head)
    self.assertEqual("4, 3, 2, 1", self.list.print_list())
  
  def test_4(self) -> None:
    self.list.add(5)
    self.list.add(4)
    self.list.add(3)
    self.list.add(2)
    self.list.add(1)
    self.sol.remove_dups(self.list.head)
    self.assertEqual("1, 2, 3, 4, 5", self.list.print_list())
  
  def test_5(self) -> None:
    self.sol.remove_dups(self.list.head)
    self.assertEqual("", self.list.print_list())
  
  def test_6(self) -> None:
    self.list.add(0)
    self.sol.remove_dups(self.list.head)
    self.assertEqual("0", self.list.print_list())