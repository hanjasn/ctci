import unittest
from solution import *
from typing import FrozenSet
from time import time


class PowerSetTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution1()
    
    def test_1(self) -> None:
        nums = [1, 2, 3]
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        expected = self.convert_to_frozenset(expected)
        actual = self.convert_to_frozenset(self.sol.power_set(nums))
        self.assertEqual(expected, actual)
    
    def test_2(self) -> None:
        nums = [1, 2, 3, 4, 5]
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4], [5], [1, 5], [2, 5], [1, 2, 5], [3, 5], [1, 3, 5], [2, 3, 5], [1, 2, 3, 5], [4, 5], [1, 4, 5], [2, 4, 5], [1, 2, 4, 5], [3, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5], [1, 2, 3, 4, 5]]
        expected = self.convert_to_frozenset(expected)
        actual = self.convert_to_frozenset(self.sol.power_set(nums))
        self.assertEqual(expected, actual)
    
    def test_3(self) -> None:
        nums = [1]
        self.assertEqual([[], [1]], self.sol.power_set(nums))

    def test_4(self) -> None:
        nums = []
        self.assertEqual([[]], self.sol.power_set(nums))
    
    def test_5(self) -> None:
        nums = [i for i in range(18)]
        start = time()
        self.sol.power_set(nums)
        print(f'{time() - start:.3f} seconds')
    
    def convert_to_frozenset(self, arr: List[List[int]]) -> FrozenSet[FrozenSet[int]]:
        temp = arr.copy()
        for i in range(len(temp)):
            temp[i] = frozenset(temp[i])
        return frozenset(temp)