import unittest
from is_unique import *

class IsUniqueTest(unittest.TestCase):
  def setUp(self):
    self.sol1 = Solution1()

  def test_1(self):
    str = "abc"
    self.assertTrue(self.sol1.is_unique(str))

  def test_2(self):
    str = "aab"
    self.assertFalse(self.sol1.is_unique(str))

  def test_3(self):
    str = "aba"
    self.assertFalse(self.sol1.is_unique(str))

  def test_4(self):
    str = "baa"
    self.assertFalse(self.sol1.is_unique(str))

  def test_5(self):
    str = ""
    self.assertTrue(self.sol1.is_unique(str))

  def test_6(self):
    str = "a"
    self.assertTrue(self.sol1.is_unique(str))

if __name__ == "__main__":
  unittest.main()