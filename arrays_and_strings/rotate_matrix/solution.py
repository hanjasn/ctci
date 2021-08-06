"""
Rotate Matrix

Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""
from typing import List


# Time: O(n^2)
# Space: O(1)
class Solution:
    def rotate_matrix(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        layers = -(n//-2)
        for i in range(layers):
            begin = i
            end = (n - 1) - i
            for j in range(begin, end):
                self.swap(matrix, j, begin, end, j)
                self.swap(matrix, j, begin, (n - 1) - j, end)
                self.swap(matrix, j, begin, begin, (n - 1) - j)
    
    def swap(self, matrix: List[List[int]], x1: int, y1: int, x2: int, y2: int) -> None:
        matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]