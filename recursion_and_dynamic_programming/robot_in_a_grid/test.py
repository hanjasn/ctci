import unittest
from solution import *
from time import time


class FindPathTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution1()
    
    def test_1(self) -> None:
        maze = [[False, False, False],
                [False, False, False],
                [False, False, False]]
        path = [Point(0,0), Point(1,0), Point(2,0), Point(2,1), Point(2,2)]
        self.assertTrue(self.paths_equal(path, self.sol.find_path(maze)))
    
    def test_2(self) -> None:
        maze = [[False, False, False],
                [True,  False, False],
                [False, True,  False]]
        path = [Point(0,0), Point(0,1), Point(1,1), Point(1,2), Point(2,2)]
        self.assertTrue(self.paths_equal(path, self.sol.find_path(maze)))
    
    def test_3(self) -> None:
        maze = [[False, False, False],
                [True,  False, False],
                [False, True,  False],
                [False, False, False]]
        path = [Point(0,0), Point(0,1), Point(1,1), Point(1,2), Point(2,2), Point(3,2)]
        self.assertTrue(self.paths_equal(path, self.sol.find_path(maze)))
    
    def test_4(self) -> None:
        maze = [[False, False, False],
                [True,  False, False],
                [False, True,  True],
                [False, False, False]]
        self.assertEqual(None, self.sol.find_path(maze))
    
    def test_5(self) -> None:
        maze = []
        self.assertEqual(None, self.sol.find_path(maze))

    def test_6(self) -> None:
        maze = [[False] * 10 for _ in range(10)]
        for i in range(0, len(maze[0]) - 1):
            maze[1][i] = True
        
        start = time()
        self.sol.find_path(maze)
        print(f'{time() - start:.5f} seconds')
    
    def test_7(self) -> None:
        maze = [[False] * 12 for _ in range(12)]
        for i in range(0, len(maze[0]) - 1):
            maze[1][i] = True
        
        start = time()
        self.sol.find_path(maze)
        print(f'{time() - start:.5f} seconds')

    def test_8(self) -> None:
        maze = [[False] * 13 for _ in range(13)]
        for i in range(0, len(maze[0]) - 1):
            maze[1][i] = True
        
        start = time()
        self.sol.find_path(maze)
        print(f'{time() - start:.5f} seconds')
    
    def test_9(self) -> None:
        maze = [[False] * 480 for _ in range(480)]
        for i in range(0, len(maze[0]) - 1):
            maze[1][i] = True
        
        start = time()
        self.sol.find_path(maze)
        print(f'{time() - start:.5f} seconds')
    
    def paths_equal(self, path1: List[Point], path2: List[Point]) -> bool:
        if len(path1) != len(path2):
            return False
        for i in range(len(path1)):
            if path1[i].x != path2[i].x or path1[i].y != path2[i].y:
                return False
        return True
    
    def path_to_str(self, path: List[Point]) -> str:
        result = ""
        for point in path:
            result += f'({point.x}, {point.y})\n'
        return result


class S3S4FindPathTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution3()
    
    def test_1(self) -> None:
        maze = [[False, False, False],
                [False, False, False],
                [False, False, False]]
        path = [Point(0,0), Point(1,0), Point(2,0), Point(2,1), Point(2,2)]
        self.assertTrue(self.paths_equal(path, self.sol.find_path(maze)))
    
    def test_2(self) -> None:
        maze = [[False, False, False],
                [True,  False, False],
                [False, True,  False]]
        path = [Point(0,0), Point(0,1), Point(1,1), Point(1,2), Point(2,2)]
        self.assertTrue(self.paths_equal(path, self.sol.find_path(maze)))
    
    def test_3(self) -> None:
        maze = [[False, False, False],
                [True,  False, False],
                [False, True,  False],
                [False, False, False]]
        path = [Point(0,0), Point(0,1), Point(1,1), Point(1,2), Point(2,2), Point(3,2)]
        self.assertTrue(self.paths_equal(path, self.sol.find_path(maze)))
    
    def test_4(self) -> None:
        maze = [[False, False, False],
                [True,  False, False],
                [False, True,  True],
                [False, False, False]]
        self.assertEqual(None, self.sol.find_path(maze))
    
    def test_5(self) -> None:
        maze = []
        self.assertEqual(None, self.sol.find_path(maze))

    def test_6(self) -> None:
        maze = [[False] * 10 for _ in range(10)]
        for i in range(1, len(maze)):
            maze[i][len(maze[0]) - 2] = True
        
        start = time()
        self.sol.find_path(maze)
        print(f'{time() - start:.3f} seconds')
    
    def test_7(self) -> None:
        maze = [[False] * 12 for _ in range(12)]
        for i in range(1, len(maze)):
            maze[i][len(maze[0]) - 2] = True
        
        start = time()
        self.sol.find_path(maze)
        print(f'{time() - start:.3f} seconds')

    def test_8(self) -> None:
        maze = [[False] * 13 for _ in range(13)]
        for i in range(1, len(maze)):
            maze[i][len(maze[0]) - 2] = True
        
        start = time()
        self.sol.find_path(maze)
        print(f'{time() - start:.3f} seconds')
    
    def paths_equal(self, path1: List[Point], path2: List[Point]) -> bool:
        if len(path1) != len(path2):
            return False
        for i in range(len(path1)):
            if path1[i].x != path2[i].x or path1[i].y != path2[i].y:
                return False
        return True
    
    def path_to_str(self, path: List[Point]) -> str:
        result = ""
        for point in path:
            result += f'({point.x}, {point.y})\n'
        return result