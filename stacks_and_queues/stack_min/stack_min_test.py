import unittest
from stack_min import *


class StackTest(unittest.TestCase):
  def setUp(self):
    self.stack = Stack()
  
  def test_1(self):
    self.stack.push(1)
    self.stack.push(2)
    self.stack.push(3)
    self.stack.push(4)
    self.stack.push(5)
    self.assertEqual(1, self.stack.min())
  
  def test_2(self):
    self.stack.push(5)
    self.stack.push(4)
    self.stack.push(3)
    self.stack.push(2)
    self.stack.push(1)
    self.assertEqual(1, self.stack.min())

  def test_3(self):
    self.stack.push(1)
    self.stack.push(2)
    self.stack.push(3)
    self.stack.push(4)
    self.stack.push(5)
    self.stack.pop()
    self.assertEqual(1, self.stack.min())

  def test_4(self):
    self.stack.push(5)
    self.stack.push(4)
    self.stack.push(3)
    self.stack.push(2)
    self.stack.push(1)
    self.stack.pop()
    self.assertEqual(2, self.stack.min())
  
  def test_5(self):
    self.stack.push(1)
    self.assertEqual(1, self.stack.min())
  
  def test_6(self):
    self.assertEqual(None, self.stack.pop())
  
  def test_7(self):
    self.assertEqual(None, self.stack.min())