"""
Towers of Hanoi

In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto the next tower.
(3) A disk can only be placed on top of a larger disk.
Write a program to move the disks from the first tower to the last using stacks.
"""
from typing import List
from stack import *


# Time: O(2^n)
# Space: O(n)
class Solution:
    def towers_of_hanoi(self, n: int) -> List['Stack[int]']:
        towers = [self.build_tower(n), Stack(), Stack()]
        self._towers_of_hanoi(n, towers[0], towers[2], towers[1])
        return towers

    def _towers_of_hanoi(
        self, n: int, origin: Stack, destination: Stack, buffer: Stack
    ) -> None:
        if n == 0:
            return
        self._towers_of_hanoi(n - 1, origin, buffer, destination)
        destination.push(origin.pop())
        self._towers_of_hanoi(n - 1, buffer, destination, origin)

    def build_tower(self, n: int) -> Stack:
        stack = Stack()
        for i in range(n, 0, -1):
            stack.push(i)
        return stack
