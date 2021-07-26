import unittest
from solution import *


class RealToBinaryStringTest(unittest.TestCase):
  def setUp(self) -> None:
    self.sol = Solution()
  
  def test_1(self) -> None:
    num = 0.1875
    self.assertEqual("0.0011", self.sol.real_to_binary_string(num))

  def test_2(self) -> None:
    num = 0.03125
    self.assertEqual("0.00001", self.sol.real_to_binary_string(num))

  def test_3(self) -> None:
    num = 0.5
    self.assertEqual("0.1", self.sol.real_to_binary_string(num))

  def test_4(self) -> None:
    num = 0.96875
    self.assertEqual("0.11111", self.sol.real_to_binary_string(num))
  
  def test_5(self) -> None:
    num = 1
    self.assertEqual("ERROR", self.sol.real_to_binary_string(num))

  def test_6(self) -> None:
    num = 0
    self.assertEqual("ERROR", self.sol.real_to_binary_string(num))
  
  def test_7(self) -> None:
    num = 0.1
    self.assertEqual("ERROR", self.sol.real_to_binary_string(num))