import unittest
from solution import *
from time import time


class TripleStepTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution1()
    
    def test_1(self) -> None:
        self.assertEqual(4, self.sol.triple_step(3))

    def test_2(self) -> None:
        self.assertEqual(274, self.sol.triple_step(10))
    
    def test_3(self) -> None:
        self.assertEqual(1, self.sol.triple_step(0))
    
    def test_4(self) -> None:
        start = time()
        self.sol.triple_step(22)
        print(f'{time() - start:.5f} seconds')
    
    def test_5(self) -> None:
        start = time()
        self.sol.triple_step(25)
        print(f'{time() - start:.5f} seconds')
    
    def test_6(self) -> None:
        start = time()
        self.sol.triple_step(900)
        print(f'{time() - start:.5f} seconds')