import unittest
from solution import *


class GetPrevTest(unittest.TestCase):
  def setUp(self) -> None:
    self.sol = Solution1()
  
  def test_1(self) -> None:
    num = 0b10011
    self.assertEqual(0b1110, self.sol.get_prev(num))
  
  def test_2(self) -> None:
    num = 0b10000
    self.assertEqual(0b1000, self.sol.get_prev(num))
  
  def test_3(self) -> None:
    num = 0b1
    self.assertIsNone(self.sol.get_prev(num))


class GetNextTest(unittest.TestCase):
  def setUp(self) -> None:
    self.sol = Solution1()

  def test_1(self) -> None:
    num = 0b10011
    self.assertEqual(0b10101, self.sol.get_next(num))

  def test_2(self) -> None:
    num = 0b1111
    self.assertEqual(0b10111, self.sol.get_next(num))
  
  def test_3(self) -> None:
    num = 0b1
    self.assertEqual(0b10, self.sol.get_next(num))