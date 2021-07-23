import unittest
from queue_via_stacks import *


class QueueTest(unittest.TestCase):
  def setUp(self) -> None:
    self.queue = Queue()
  
  def test_1(self) -> None:
    self.queue.add(1)
    self.queue.add(2)
    self.queue.add(3)
    self.queue.add(4)
    self.queue.add(5)
    self.assertEqual("1, 2, 3, 4, 5", self.queue.print_values())

  def test_2(self) -> None:
    self.queue.add(1)
    self.queue.add(2)
    self.queue.remove()
    self.assertEqual("2", self.queue.print_values())
  
  def test_3(self) -> None:
    self.queue.add(1)
    self.queue.add(2)
    self.queue.remove()
    self.queue.add(3)
    self.queue.add(4)
    self.queue.add(5)
    self.queue.remove()
    self.queue.remove()
    self.assertEqual("4, 5", self.queue.print_values())

  def test_4(self) -> None:
    self.assertTrue(self.queue.empty())
  
  def test_5(self) -> None:
    self.queue.add(1)
    self.assertFalse(self.queue.empty())
  
  def test_6(self) -> None:
    self.queue.add(1)
    self.queue.remove()
    self.assertTrue(self.queue.empty())
  
  def test_7(self) -> None:
    self.assertEqual(None, self.queue.peek())
  
  def test_8(self) -> None:
    self.queue.add(1)
    self.queue.add(2)
    self.queue.add(3)
    self.queue.add(4)
    self.queue.add(5)
    self.assertEqual(1, self.queue.peek())
  
  def test_9(self) -> None:
    self.queue.add(1)
    self.queue.add(2)
    self.queue.add(3)
    self.queue.add(4)
    self.queue.add(5)
    self.queue.remove()
    self.assertEqual(2, self.queue.peek())