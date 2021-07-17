import unittest
from stack_of_plates import *


class SetOfStacksTest(unittest.TestCase):
  def setUp(self) -> None:
    limit = 3
    self.stacks = SetOfStacks(limit)
  
  def test_1(self) -> None:
    self.stacks.push(0)
    self.assertEqual("0", self.stacks.print_values())
  
  def test_2(self) -> None:
    self.stacks.push(0)
    self.stacks.push(1)
    self.stacks.push(2)
    self.stacks.push(3)
    self.assertEqual("3 | 2, 1, 0", self.stacks.print_values())
  
  def test_3(self) -> None:
    self.stacks.push(0)
    self.stacks.push(1)
    self.stacks.pop()
    self.assertEqual("0", self.stacks.print_values())
  
  def test_4(self) -> None:
    self.stacks.push(0)
    self.stacks.push(1)
    self.stacks.push(2)
    self.stacks.push(3)
    self.stacks.pop()
    self.assertEqual("2, 1, 0", self.stacks.print_values())
  
  def test_4(self) -> None:
    self.stacks.push(1)
    self.stacks.push(2)
    self.stacks.push(3)
    self.stacks.push(4)
    self.stacks.push(5)
    self.stacks.push(6)
    self.stacks.push(7)
    self.stacks.push(8)
    self.stacks.push(9)
    self.stacks.pop()
    self.stacks.pop()
    self.stacks.pop()
    self.stacks.pop()
    self.stacks.push(6)
    self.stacks.push(7)
    self.stacks.push(8)
    self.stacks.push(9)
    self.assertEqual("9, 8, 7 | 6, 5, 4 | 3, 2, 1", self.stacks.print_values())
  
  def test_5(self):
    self.stacks.push(0)
    self.stacks.push(1)
    self.stacks.push(2)
    self.stacks.push(3)
    self.stacks.push(4)
    self.stacks.push(5)
    self.stacks.push(6)
    self.stacks.push(7)
    self.stacks.pop_at(0)
    self.assertEqual("7 | 6, 5, 4 | 3, 1, 0", self.stacks.print_values())
    

  def test_6(self):
    self.stacks.push(0)
    self.stacks.push(1)
    self.stacks.push(2)
    self.stacks.push(3)
    self.stacks.push(4)
    self.stacks.push(5)
    self.stacks.push(6)
    self.stacks.push(7)
    self.stacks.pop_at(0)
    self.stacks.pop_at(2)
    self.assertEqual("6, 5, 4 | 3, 1, 0", self.stacks.print_values())

  def test_7(self):
    self.stacks.push(0)
    self.stacks.push(1)
    self.stacks.push(2)
    self.stacks.push(3)
    self.stacks.push(4)
    self.stacks.push(5)
    self.stacks.push(6)
    self.stacks.push(7)
    self.stacks.pop_at(0)
    self.stacks.pop_at(2)
    self.stacks.pop_at(0)
    self.assertEqual("6, 5 | 4, 1, 0", self.stacks.print_values())
  
  def test_8(self):
    self.stacks.push(0)
    self.stacks.push(1)
    self.stacks.push(2)
    self.stacks.push(3)
    self.stacks.push(4)
    self.stacks.push(5)
    self.stacks.push(6)
    self.stacks.push(7)
    self.stacks.pop_at(0)
    self.stacks.pop_at(2)
    self.stacks.pop_at(0)
    self.stacks.push(7)
    self.stacks.push(8)
    self.stacks.push(9)
    self.assertEqual("9, 8 | 7, 6, 5 | 4, 1, 0", self.stacks.print_values())