import unittest
from partition import *


class PartitionTest(unittest.TestCase):
  def setUp(self) -> None:
    self.sol = Solution1()
    self.list = LinkedList()
  
  def test_1(self) -> None:
    self.list.push(1)
    self.list.push(2)
    self.list.push(10)
    self.list.push(5)
    self.list.push(8)
    self.list.push(5)
    self.list.push(3)
    partition = 5

    self.list.head = self.sol.partition(self.list.head, partition)
    self.assertEqual("3, 2, 1, 5, 8, 5, 10", self.list.print_list())
  
  def test_2(self) -> None:
    self.list.push(1)
    self.list.push(1)
    self.list.push(1)
    self.list.push(0)
    self.list.push(0)
    self.list.push(0)
    partition = 1

    self.list.head = self.sol.partition(self.list.head, partition)
    self.assertEqual("0, 0, 0, 1, 1, 1", self.list.print_list())
  
  def test_3(self) -> None:
    self.list.push(0)
    self.list.push(0)
    self.list.push(0)
    self.list.push(1)
    self.list.push(1)
    self.list.push(1)
    partition = 1

    self.list.head = self.sol.partition(self.list.head, partition)
    self.assertEqual("0, 0, 0, 1, 1, 1", self.list.print_list())


# class PartitionTestSolution3(unittest.TestCase):
#   def setUp(self) -> None:
#     self.sol = Solution3()
#     self.list = LinkedList()
  
#   def test_1(self) -> None:
#     self.list.push(1)
#     self.list.push(2)
#     self.list.push(10)
#     self.list.push(5)
#     self.list.push(8)
#     self.list.push(5)
#     self.list.push(3)
#     partition = 5
#     self.sol.partition(self.list.head, partition)

#     self.assertEqual("3, 2, 1, 5, 10, 5, 8", self.list.print_list())
  
#   def test_2(self) -> None:
#     self.list.push(1)
#     self.list.push(1)
#     self.list.push(1)
#     self.list.push(0)
#     self.list.push(0)
#     self.list.push(0)
#     partition = 1
#     self.sol.partition(self.list.head, partition)
#     self.assertEqual("0, 0, 0, 1, 1, 1", self.list.print_list())
  
#   def test_3(self) -> None:
#     self.list.push(0)
#     self.list.push(0)
#     self.list.push(0)
#     self.list.push(1)
#     self.list.push(1)
#     self.list.push(1)
#     partition = 1
#     self.sol.partition(self.list.head, partition)
#     self.assertEqual("0, 0, 0, 1, 1, 1", self.list.print_list())