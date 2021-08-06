"""
Zero Matrix

Write an algorithm such that if an element in an MxN matrix is 0, it's entire row and column are set to 0.
"""
from typing import List


# Time: O(nm)
# Space: O(1)
# Store information about each row and column in the first row and column of matrix to save space
class Solution1:
    def zero_matrix(self, matrix: List[List[int]]) -> None:
        x_has_zero = False
        y_has_zero = False
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                x_has_zero = True
                break
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                y_has_zero = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for x in range(len(matrix)):
            if matrix[x][0] == 0:
                self.set_zeros_x(matrix, x)
        for y in range(len(matrix[0])):
            if matrix[0][y] == 0:
                self.set_zeros_y(matrix, y)
        
        if x_has_zero == True:
            self.set_zeros_x(matrix, 0)
        if y_has_zero == True:
            self.set_zeros_y(matrix, 0)
    
    def set_zeros_x(self, matrix: List[List[int]], x: int) -> None:
        for i in range(len(matrix[0])):
            matrix[x][i] = 0
    
    def set_zeros_y(self, matrix: List[List[int]], y: int) -> None:
        for i in range(len(matrix)):
            matrix[i][y] = 0


# Time: O(nm)
# Space: O(n + m)
class Solution2:
    def zero_matrix(self, matrix: List[List[int]]) -> None:
        zeros_x = [1 for _ in range(len(matrix))]
        zeros_y = [1 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros_x[i] = 0
                    zeros_y[j] = 0
        
        for i in range(len(zeros_x)):
            if zeros_x[i] == 0:
                self.set_zeros_x(matrix, i)
        for i in range(len(zeros_y)):
            if zeros_y[i] == 0:
                self.set_zeros_y(matrix, i)
    
    def set_zeros_x(self, matrix: List[List[int]], x: int) -> None:
        for i in range(len(matrix[0])):
            matrix[x][i] = 0
    
    def set_zeros_y(self, matrix: List[List[int]], y: int) -> None:
        for i in range(len(matrix)):
            matrix[i][y] = 0


# Time: O(nm(n+m))
# Space: O(nm)
class Solution3:
    def zero_matrix(self, matrix: List[List[int]]) -> None:
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        for zero in zeros:
            self.set_zeros(matrix, zero[0], zero[1])
    
    def set_zeros(self, matrix: List[List[int]], i: int, j: int) -> None:
        for x in range(len(matrix)):
            matrix[x][j] = 0
        for y in range(len(matrix[0])):
            matrix[i][y] = 0