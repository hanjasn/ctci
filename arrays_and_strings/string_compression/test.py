import unittest
from solution import *
from time import time


class CompressStringTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution1()

    def test_1(self) -> None:
        s = "aabcccccaaa"
        result = "a2b1c5a3"
        self.assertEqual(result, self.sol.compress_string(s))
    
    def test_2(self) -> None:
        s = "abcccccaaa"
        result = "a1b1c5a3"
        self.assertEqual(result, self.sol.compress_string(s))
    
    def test_3(self) -> None:
        s = "aaa"
        result = "a3"
        self.assertEqual(result, self.sol.compress_string(s))
    
    def test_4(self) -> None:
        s = "nolemonnomelon"
        self.assertEqual(s, self.sol.compress_string(s))
    
    def test_5(self) -> None:
        s = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(s, self.sol.compress_string(s))
    
    def test_6(self) -> None:
        s = ""
        self.assertEqual(s, self.sol.compress_string(s))
    
    def test_7(self) -> None:
        s = ''.join(['aa' for _ in range(5*10**6)]) # 10,000,000 iterations
        start = time()
        self.sol.compress_string(s)
        print(f'{time() - start:.4f} seconds')

    def test_8(self) -> None:
        s = ''.join(['ab' for _ in range(5*10**6)]) # 10,000,000 iterations
        start = time()
        self.sol.compress_string(s)
        print(f'{time() - start:.4f} seconds')