import unittest
from solution import *
from time import time


class TowersOfHanoiTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
    
    def test_1(self) -> None:
        n = 3
        result = self.sol.towers_of_hanoi(n)
        self.assertTrue(self.towers_equal(Stack(), result[0]))
        self.assertTrue(self.towers_equal(Stack(), result[1]))
        self.assertTrue(self.towers_equal(self.sol.build_tower(n), result[2]))
    
    def test_2(self) -> None:
        n = 10
        result = self.sol.towers_of_hanoi(n)
        self.assertTrue(self.towers_equal(Stack(), result[0]))
        self.assertTrue(self.towers_equal(Stack(), result[1]))
        self.assertTrue(self.towers_equal(self.sol.build_tower(n), result[2]))
    
    def test_3(self) -> None:
        n = 1
        result = self.sol.towers_of_hanoi(n)
        self.assertTrue(self.towers_equal(Stack(), result[0]))
        self.assertTrue(self.towers_equal(Stack(), result[1]))
        self.assertTrue(self.towers_equal(self.sol.build_tower(n), result[2]))
    
    def test_4(self) -> None:
        n = 0
        result = self.sol.towers_of_hanoi(n)
        self.assertTrue(self.towers_equal(Stack(), result[0]))
        self.assertTrue(self.towers_equal(Stack(), result[1]))
        self.assertTrue(self.towers_equal(Stack(), result[2]))
    
    def test_5(self) -> None:
        n = 18
        start = time()
        result = self.sol.towers_of_hanoi(n)
        print(f'{time() - start:.4f} seconds')
        self.assertTrue(self.towers_equal(Stack(), result[0]))
        self.assertTrue(self.towers_equal(Stack(), result[1]))
        self.assertTrue(self.towers_equal(self.sol.build_tower(n), result[2]))

    def towers_equal(self, t1: 'Stack[int]', t2: 'Stack[int]') -> bool:
        if t1.get_size() != t2.get_size():
            return False
        node1 = t1.top
        node2 = t2.top
        while node1 != None:
            if node1.data != node2.data:
                return False
            node1 = node1.next
            node2 = node2.next
        return True