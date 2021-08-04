import unittest
from solution import *
from time import time


class FindingMagicIndexNonDistinctIntegersTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution1()
    
    def test_1(self) -> None:
        arr = [-3, -2, -1, 0, 4, 7, 9, 11]
        self.assertEqual(4, self.sol.find_magic_index(arr))
    
    def test_2(self) -> None:
        arr = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(-1, self.sol.find_magic_index(arr))
    
    def test_3(self) -> None:
        arr = []
        self.assertEqual(-1, self.sol.find_magic_index(arr))
    
    def test_4(self) -> None:
        arr = [100] * 101
        self.assertEqual(100, self.sol.find_magic_index(arr))
    
    def test_5(self) -> None:
        arr = [i for i in range(1, 10**6)]
        start = time()
        self.sol.find_magic_index(arr)
        print(f'{time() - start:.6f} seconds')
    
    def test_6(self) -> None:
        arr = [i for i in range(1, 10**7)]
        start = time()
        self.sol.find_magic_index(arr)
        print(f'{time() - start:.6f} seconds')


class FindMagicIndexDistinctIntegersTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution2()
    
    def test_1(self) -> None:
        arr = [-3, -2, -1, 0, 4, 7, 9, 11]
        self.assertEqual(4, self.sol.find_magic_index(arr))
    
    def test_2(self) -> None:
        arr = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(-1, self.sol.find_magic_index(arr))
    
    def test_3(self) -> None:
        arr = []
        self.assertEqual(-1, self.sol.find_magic_index(arr))
    
    def test_4(self) -> None:
        arr = [i for i in range(1, 10**7)]
        start = time()
        self.sol.find_magic_index(arr)
        print(f'{time() - start:.6f} seconds')
    
    def test_5(self) -> None:
        arr = [i for i in range(1, 10**8)]
        start = time()
        self.sol.find_magic_index(arr)
        print(f'{time() - start:.6f} seconds')
    
    def test_6(self) -> None:
        arr = [-1] * 10**9
        start = time()
        self.sol.find_magic_index(arr)
        print(f'{time() - start:.6f} seconds')