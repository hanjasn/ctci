import unittest
from return_kth_to_last import *

class FindKthLastElement(unittest.TestCase):
  def setUp(self):
    self.sol = Solution1()
    self.list = LinkedList()

  def test_1(self) -> None:
    self.list.add(5)
    self.list.add(4)
    self.list.add(3)
    self.list.add(2)
    self.list.add(1)
    k = 1
    self.assertEqual(4, self.sol.find_kth_last_element(self.list.head, k).data)
  
  # Invalid test for Solution2
  def test_2(self) -> None:
    try:
      self.list.add(5)
      self.list.add(4)
      self.list.add(3)
      self.list.add(2)
      self.list.add(1)
      k = 5
      self.sol.find_kth_last_element(self.list.head, k)
      assert False
    except AttributeError:
      assert True
  
  # Invalid test for Solution2
  def test_3(self) -> None:
    try:
      k = 0
      self.sol.find_kth_last_element(self.list.head, k)
      assert False
    except AttributeError:
      assert True

class PrintKthLastElement(unittest.TestCase):
  def setUp(self):
    self.sol = Solution3()
    self.list = LinkedList()

  # Print 4
  def test_1(self):
    self.list.add(5)
    self.list.add(4)
    self.list.add(3)
    self.list.add(2)
    self.list.add(1)
    k = 1
    self.sol.print_kth_last_element(self.list.head, k)
  
  # Print nothing
  def test_2(self):
    self.list.add(5)
    self.list.add(4)
    self.list.add(3)
    self.list.add(2)
    self.list.add(1)
    k = 5
    self.sol.print_kth_last_element(self.list.head, k)
  
  # Print nothing
  def test_3(self):
    k = 0
    self.sol.print_kth_last_element(self.list.head, k)