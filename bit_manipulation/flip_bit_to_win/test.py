import unittest
from solution import *


class LengthLongestSequenceTest(unittest.TestCase):
  def setUp(self) -> None:
    self.sol = Solution1()
  
  def test_1(self) -> None:
    num = 0b11011101111
    self.assertEqual(8, self.sol.length_longest_sequence(num))
  
  def test_2(self) -> None:
    num = 0b1
    self.assertEqual(1, self.sol.length_longest_sequence(num))
  
  def test_3(self) -> None:
    num = 0b0
    self.assertEqual(1, self.sol.length_longest_sequence(num))
  
  def test_4(self) -> None:
    num = 0b10000000
    self.assertEqual(2, self.sol.length_longest_sequence(num))

  def test_5(self) -> None:
    num = 0b00000001
    self.assertEqual(1, self.sol.length_longest_sequence(num))
  
  def test_6(self) -> None:
    num = 0b10101010
    self.assertEqual(3, self.sol.length_longest_sequence(num))
  
  def test_7(self) -> None:
    num = 0b1001
    self.assertEqual(2, self.sol.length_longest_sequence(num))
  
  def test_8(self) -> None:
    num = 0b1101
    self.assertEqual(4, self.sol.length_longest_sequence(num))
  
  def test_9(self) -> None:
    num = 0b1110111000001010001101011110111
    self.assertEqual(8, self.sol.length_longest_sequence(num))
  
  def test_10(self) -> None:
    num = 0b11101110000010100011010111101110
    self.assertEqual(8, self.sol.length_longest_sequence(num))