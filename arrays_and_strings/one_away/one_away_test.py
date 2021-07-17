import unittest
from one_away import *

class OneAwayTest(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_1(self):
    str1 = "pale"
    str2 = "ple"
    self.assertTrue(self.sol.is_one_away(str1, str2))
  
  def test_2(self):
    str1 = "pales"
    str2 = "pale"
    self.assertTrue(self.sol.is_one_away(str1, str2))

  def test_3(self):
    str1 = "pale"
    str2 = "bale"
    self.assertTrue(self.sol.is_one_away(str1, str2))
  
  def test_4(self):
    str1 = "pale"
    str2 = "bake"
    self.assertFalse(self.sol.is_one_away(str1, str2))

  def test_5(self):
    str1 = "pple"
    str2 = "ple"
    self.assertTrue(self.sol.is_one_away(str1, str2))

  def test_6(self):
    str1 = "bble"
    str2 = "ple"
    self.assertFalse(self.sol.is_one_away(str1, str2))