import unittest
from palindrome_permutation import *

class PalindromePermutationTest(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_1(self):
    str = "Tact Coa"
    self.assertTrue(self.sol.palindrome_permutation(str))
  
  def test_2(self):
    str = "Was it a cat I saw"
    self.assertTrue(self.sol.palindrome_permutation(str))
  
  def test_3(self):
    str = "Wow"
    self.assertTrue(self.sol.palindrome_permutation(str))

  def test_4(self):
    str = "not a palindrome"
    self.assertFalse(self.sol.palindrome_permutation(str))

  def test_4(self):
    str = ""
    self.assertTrue(self.sol.palindrome_permutation(str))

  def test_5(self):
    str = " "
    self.assertTrue(self.sol.palindrome_permutation(str))

  def test_6(self):
    try:
      str = None
      self.sol.palindrome_permutation(str)
      assert False
    except AttributeError:
      assert True