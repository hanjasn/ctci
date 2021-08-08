import unittest
from solution import *


class IntersectionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
    
    def test_1(self) -> None:
        lst = LinkedList([1, 2, 3, 4])
        prepend1 = LinkedList([0, 0, 0])
        prepend2 = LinkedList([1, 1, 1])
        prepend1.tail.next = prepend2.tail.next = lst.head
        prepend1.tail = prepend2.tail = lst.tail
        self.assertEqual(lst.head, self.sol.intersection(prepend1, prepend2))
    
    def test_2(self) -> None:
        lst = LinkedList([1, 2, 3, 4])
        prepend1 = LinkedList([0, 0, 0, 0])
        prepend2 = LinkedList([1, 1, 1])
        prepend1.tail.next = prepend2.tail.next = lst.head
        prepend1.tail = prepend2.tail = lst.tail
        self.assertEqual(lst.head, self.sol.intersection(prepend1, prepend2))
    
    def test_3(self) -> None:
        prepend1 = LinkedList([])
        prepend2 = LinkedList([0, 0, 0])
        self.assertEqual(None, self.sol.intersection(prepend1, prepend2))

    def test_4(self) -> None:
        prepend1 = LinkedList([])
        prepend2 = LinkedList([])
        self.assertEqual(None, self.sol.intersection(prepend1, prepend2))