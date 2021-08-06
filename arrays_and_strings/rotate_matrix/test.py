import unittest
from solution import *
from pprint import pprint


# Clockwise rotation using (x, y) notation looks counterclockwise because matrix is mirrored
class RotateMatrixTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
    
    def test_1(self) -> None:
        matrix = [[i] * 4 for i in range(1, 5)]
        result = [[i for i in range(1, 5)] for _ in range(4)]
        pprint(matrix, width=14)
        self.sol.rotate_matrix(matrix)
        pprint(matrix, width=14)
        self.assertEqual(result, matrix)
    
    def test_2(self) -> None:
        matrix = [[i for i in range(0, 10)] for _ in range(10)]
        result = [[i for _ in range(10)] for i in range(9, -1, -1)]
        pprint(matrix, width=124)
        self.sol.rotate_matrix(matrix)
        pprint(matrix, width=124)
        self.assertEqual(result, matrix)
    
    def test_3(self) -> None:
        matrix = [[1]]
        result = [[1]]
        self.sol.rotate_matrix(matrix)
        self.assertEqual(result, matrix)
    
    def test_4(self) -> None:
        matrix = []
        result = []
        self.sol.rotate_matrix(matrix)
        self.assertEqual(result, matrix)