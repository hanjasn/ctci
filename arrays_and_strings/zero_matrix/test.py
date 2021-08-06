import unittest
from solution import *
from pprint import pprint
from time import time


class ZeroMatrixTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution1()
    
    def test_1(self) -> None:
        matrix = [[1, 1, 1, 1, 1],
                  [1, 1, 1, 0, 1],
                  [1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1]]
        result = [[1, 1, 1, 0, 1],
                  [0, 0, 0, 0, 0],
                  [1, 1, 1, 0, 1],
                  [1, 1, 1, 0, 1]]
        pprint(matrix, width=17)
        self.sol.zero_matrix(matrix)
        pprint(matrix, width=17)
        self.assertEqual(result, matrix)

    def test_2(self) -> None:
        matrix = [[1, 1, 1, 1, 1],
                  [1, 1, 1, 0, 1],
                  [1, 0, 1, 1, 1],
                  [1, 1, 1, 1, 1]]
        result = [[1, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [1, 0, 1, 0, 1]]
        pprint(matrix, width=17)
        self.sol.zero_matrix(matrix)
        pprint(matrix, width=17)
        self.assertEqual(result, matrix)
    
    def test_3(self) -> None:
        matrix = [[0 for __ in range(250)] for _ in range(250)]
        result = [[0 for __ in range(250)] for _ in range(250)]
        start = time()
        self.sol.zero_matrix(matrix)
        print(f'{time() - start:.4f} seconds')
        self.assertEqual(result, matrix)
    
    def test_4(self) -> None:
        matrix = [[0 for __ in range(400)] for _ in range(400)]
        result = [[0 for __ in range(400)] for _ in range(400)]
        start = time()
        self.sol.zero_matrix(matrix)
        print(f'{time() - start:.4f} seconds')
        self.assertEqual(result, matrix)