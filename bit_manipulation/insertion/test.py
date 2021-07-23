import unittest
from solution import *


class InsertTest(unittest.TestCase):
  def setUp(self) -> None:
    self.sol = Solution()
  
  def test_1(self) -> None:
    self.assertEqual(0b10001001100, self.sol.update_bits(0b10000000000, 0b10011, 2, 6))
  
  def test_2(self) -> None:
    self.assertEqual(0b10001001100, self.sol.update_bits(0b10000000000, 0b10011, 2, 7))
  
  def test_2(self) -> None:
    self.assertEqual(0b1111, self.sol.update_bits(0b0, 0b1111, 0, 3))

  def test_3(self) -> None:
    self.assertEqual(0b10, self.sol.update_bits(0b0, 0b1, 1, 1))