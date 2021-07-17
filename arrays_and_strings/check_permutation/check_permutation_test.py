import unittest
from check_permutation import *

class CheckPermutationTest(unittest.TestCase):
  def setUp(self):
    self.sol = Solution1()
  
  def test_1(self):
    str1, str2 = "dacb", "bacd"
    self.assertTrue(self.sol.check_permutation(str1, str2))
    
  def test_2(self):
    str1, str2 = "acb", "bacd"
    self.assertFalse(self.sol.check_permutation(str1, str2))

  def test_3(self):
    str1, str2 = "", ""
    self.assertTrue(self.sol.check_permutation(str1, str2))

  def test_4(self):
    str1, str2 = "", " "
    self.assertFalse(self.sol.check_permutation(str1, str2))

  def test_5(self):
    str1, str2 = "[]#^'a", "#a'^]["
    self.assertTrue(self.sol.check_permutation(str1, str2))