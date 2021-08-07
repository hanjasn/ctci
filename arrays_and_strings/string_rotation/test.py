import unittest
from solution import *
from time import time


class IsRotationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution1()
    
    def test_1(self) -> None:
        s1 ="erbottlewat"
        s2 = "waterbottle"
        self.assertTrue(self.sol.is_rotation(s1, s2))
    
    def test_2(self) -> None:
        s1 = "awterbottle"
        s2 = "waterbottle"
        self.assertFalse(self.sol.is_rotation(s1, s2))
    
    def test_3(self) -> None:
        s1 = "catocat"
        s2 = "tacocat"
        self.assertFalse(self.sol.is_rotation(s1, s2))
    
    def test_4(self) -> None:
        s1 = "four"
        s2 = "three"
        self.assertFalse(self.sol.is_rotation(s1, s2))
    
    def test_5(self) -> None:
        s1 = ""
        s2 = ""
        self.assertTrue(self.sol.is_rotation(s1, s2))
    
    def test_6(self) -> None:
        s1 = ''.join(["a"] * (10**4))
        s2 = ["a"] * (10**4 - 1)
        s2.append("b")
        s2 = ''.join(s2)
        start = time()
        self.sol.is_rotation(s1, s2)
        print(f'{time() - start:.4f} seconds')
    
    def test_7(self) -> None:
        s1 = ''.join(["a"] * (10**5))
        s2 = ["a"] * (10**5 - 1)
        s2.append("b")
        s2 = ''.join(s2)
        start = time()
        self.sol.is_rotation(s1, s2)
        print(f'{time() - start:.4f} seconds')