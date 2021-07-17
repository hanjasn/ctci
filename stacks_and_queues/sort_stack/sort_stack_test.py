import unittest
from sort_stack import *

class StackTest(unittest.TestCase):
  def setUp(self) -> None:
    self.stack = Stack()
  
  def test_1(self) -> None:
    self.stack.push(5)
    self.stack.push(4)
    self.stack.push(3)
    self.stack.push(2)
    self.stack.push(1)
    self.assertEqual("1, 2, 3, 4, 5", self.stack.print_values())
    self.stack.sort()
    self.assertEqual("1, 2, 3, 4, 5", self.stack.print_values())
  
  def test_2(self) -> None:
    self.stack.push(1)
    self.stack.push(2)
    self.stack.push(3)
    self.stack.push(4)
    self.stack.push(5)
    self.assertEqual("5, 4, 3, 2, 1", self.stack.print_values())
    self.stack.sort()
    self.assertEqual("1, 2, 3, 4, 5", self.stack.print_values())
  
  def test_3(self) -> None:
    self.stack.push(9)
    self.stack.push(10)
    self.stack.push(6)
    self.stack.push(2)
    self.stack.push(3)
    self.stack.push(5)
    self.stack.push(4)
    self.stack.push(7)
    self.stack.push(8)
    self.stack.push(1)
    self.assertEqual("1, 8, 7, 4, 5, 3, 2, 6, 10, 9", self.stack.print_values())
    self.stack.sort()
    self.assertEqual("1, 2, 3, 4, 5, 6, 7, 8, 9, 10", self.stack.print_values())
  
  def test_4(self) -> None:
    self.assertEqual("", self.stack.print_values())
    self.stack.sort()
    self.assertEqual("", self.stack.print_values())
  
  def test_5(self) -> None:
    self.stack.push(1)
    self.assertEqual("1", self.stack.print_values())
    self.stack.sort()
    self.assertEqual("1", self.stack.print_values())
  
  def test_5(self) -> None:
    self.stack.push(1)
    self.stack.push(2)
    self.assertEqual("2, 1", self.stack.print_values())
    self.stack.sort()
    self.assertEqual("1, 2", self.stack.print_values())