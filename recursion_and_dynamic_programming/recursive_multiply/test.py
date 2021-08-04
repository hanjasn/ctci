import unittest
from solution import *
from time import time


class RecursiveMultiplyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution1()
    
    def test_1(self) -> None:
        self.assertEqual(2, self.sol.recursive_multiply(1, 2))
    
    def test_2(self) -> None:
        self.assertEqual(15, self.sol.recursive_multiply(3, 5))
    
    def test_3(self) -> None:
        self.assertEqual(9999, self.sol.recursive_multiply(99, 101))
    
    def test_4(self) -> None:
        self.assertEqual(0, self.sol.recursive_multiply(0, 727))
    
    def test_5(self) -> None:
        start = time()
        self.sol.recursive_multiply(900, 900)
        print(f'{time() - start:.5f} seconds')
    
    def test_6(self) -> None:
        start = time()
        self.sol.recursive_multiply(10**9, 10**9)
        print(f'{time() - start:.5f} seconds')