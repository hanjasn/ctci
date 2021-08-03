"""
Robot in a Grid

Imagine a robot sitting on the upper left corner of a grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.
"""
from typing import List, Set, Tuple


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


# Time: O(rc) where r is rows and c is columns
# Space: O(rc)
# Backtracking algorithm while keeping track of visited points
class Solution1:
    def find_path(self, maze: List[List[bool]]) -> List[Point]:
        path = []
        if (
            len(maze) != 0
            and self._find_path(maze, len(maze) - 1, len(maze[0]) - 1, path, set())
            == True
        ):
            return path
        return None

    def _find_path(
        self,
        maze: List[List[bool]],
        x: int,
        y: int,
        path: List[Point],
        visited: Set[Tuple[int]],
    ) -> bool:
        if x < 0 or y < 0 or maze[x][y] == True:
            return False
        p = (x, y)
        if p in visited:
            return False

        visited.add(p)
        at_origin = x == 0 and y == 0
        if (
            at_origin
            or self._find_path(maze, x, y - 1, path, visited) == True
            or self._find_path(maze, x - 1, y, path, visited) == True
        ):
            path.append(Point(x, y))
            return True
        return False


# Time: O(2^(r+c))
# Space: O(r+c)
# Backtracking algorithm but more concise and in correct order
class Solution2:
    def find_path(self, maze: List[List[bool]]) -> List[Point]:
        path = []
        if (
            len(maze) != 0
            and self._find_path(maze, len(maze) - 1, len(maze[0]) - 1, path) == True
        ):
            return path
        return None

    def _find_path(
        self, maze: List[List[bool]], x: int, y: int, path: List[Point]
    ) -> bool:
        if x < 0 or y < 0 or maze[x][y] == True:
            return False

        is_at_origin = x == 0 and y == 0
        if (
            is_at_origin
            or self._find_path(maze, x, y - 1, path) == True
            or self._find_path(maze, x - 1, y, path) == True
        ):
            path.append(Point(x, y))
            return True
        return False


# Time: O(2^(r+c))
# Space: O(r+c)
# Backtracking algorithm but more concise
class Solution3:
    def find_path(self, maze: List[List[bool]]) -> List[Point]:
        path = []
        if len(maze) != 0 and self._find_path(maze, 0, 0, path) == True:
            path.reverse()
            return path
        return None

    def _find_path(
        self, maze: List[List[bool]], x: int, y: int, path: List[Point]
    ) -> bool:
        if x == len(maze) or y == len(maze[0]) or maze[x][y] == True:
            return False

        is_at_destination = x == len(maze) - 1 and y == len(maze[0]) - 1
        if (
            is_at_destination
            or self._find_path(maze, x + 1, y, path) == True
            or self._find_path(maze, x, y + 1, path) == True
        ):
            path.append(Point(x, y))
            return True
        return False


# Time: O(2^(r+c))
# Space: O(r+c)
# Backtracking algorithm
class Solution4:
    def find_path(self, maze: List[List[bool]]) -> List[Point]:
        path = []
        if len(maze) != 0 and self._find_path(maze, Point(0, 0), path) == True:
            return path
        return None

    def _find_path(
        self, maze: List[List[bool]], point: Point, path: List[Point]
    ) -> bool:
        if point.x == len(maze) - 1 and point.y == len(maze[0]) - 1:
            path.append(point)
            return True
        if self.can_go_right(maze, point):
            path.append(point)
            if self._find_path(maze, Point(point.x + 1, point.y), path) == True:
                return True
            path.pop()
        if self.can_go_down(maze, point):
            path.append(point)
            if self._find_path(maze, Point(point.x, point.y + 1), path) == True:
                return True
            path.pop()
        return False

    def can_go_right(self, maze: List[List[bool]], point: Point) -> bool:
        return point.x < len(maze) - 1 and maze[point.x + 1][point.y] == False

    def can_go_down(self, maze: List[List[bool]], point: Point) -> bool:
        return point.y < len(maze[0]) - 1 and maze[point.x][point.y + 1] == False
