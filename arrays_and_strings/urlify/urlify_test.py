import unittest
from urlify import *

class URLify(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_one_space(self):
    str = "a string  "
    length = 8
    new_str = self.sol.urlify(str, length)
    self.assertEqual("a%20string", new_str)
  
  def test_multiple_spaces(self):
    str = "this is a string      "
    length = 16
    new_str = self.sol.urlify(str, length)
    self.assertEqual("this%20is%20a%20string", new_str)
  
  def test_no_spaces(self):
    str = "string"
    length = 6
    new_str = self.sol.urlify(str, length)
    self.assertEqual("string", new_str)