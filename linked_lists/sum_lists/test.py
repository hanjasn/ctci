import unittest
from solution import *


class SumListsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution1()
    
    def test_1(self) -> None:
        lst1 = LinkedList([7, 1, 6])
        lst2 = LinkedList([5, 9, 2])
        result = self.sol.sum_lists(lst1, lst2)
        self.assertEqual(912, self.sol.get_val(result))
    
    def test_2(self) -> None:
        lst1 = LinkedList([4, 3, 2, 1])
        lst2 = LinkedList([3, 2, 1])
        result = self.sol.sum_lists(lst1, lst2)
        self.assertEqual(1357, self.sol.get_val(result))
    
    def test_3(self) -> None:
        lst1 = LinkedList([7, 8, 9])
        lst2 = LinkedList([6, 7, 8])
        result = self.sol.sum_lists(lst1, lst2)
        self.assertEqual(1863, self.sol.get_val(result))
    
    def test_4(self) -> None:
        lst1 = LinkedList([0])
        lst2 = LinkedList([0])
        result = self.sol.sum_lists(lst1, lst2)
        self.assertEqual(0, self.sol.get_val(result))

    def test_5(self) -> None:
        lst1 = LinkedList()
        lst2 = LinkedList()
        result = self.sol.sum_lists(lst1, lst2)
        self.assertEqual(0, self.sol.get_val(result))


class SumListsReversedTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution1()
    
    def test_1(self) -> None:
        lst1 = LinkedList([6, 1, 7])
        lst2 = LinkedList([2, 9, 5])
        result = self.sol.sum_lists_reversed(lst1, lst2)
        self.assertEqual(912, self.sol.get_val_reversed(result))
    
    def test_2(self) -> None:
        lst1 = LinkedList([1, 2, 3, 4])
        lst2 = LinkedList([1, 2, 3])
        result = self.sol.sum_lists_reversed(lst1, lst2)
        self.assertEqual(1357, self.sol.get_val_reversed(result))
    
    def test_3(self) -> None:
        lst1 = LinkedList([9, 8, 7])
        lst2 = LinkedList([8, 7, 6])
        result = self.sol.sum_lists_reversed(lst1, lst2)
        self.assertEqual(1863, self.sol.get_val_reversed(result))
    
    def test_4(self) -> None:
        lst1 = LinkedList([0])
        lst2 = LinkedList([0])
        result = self.sol.sum_lists_reversed(lst1, lst2)
        self.assertEqual(0, self.sol.get_val_reversed(result))

    def test_5(self) -> None:
        lst1 = LinkedList()
        lst2 = LinkedList()
        result = self.sol.sum_lists_reversed(lst1, lst2)
        self.assertEqual(0, self.sol.get_val_reversed(result))