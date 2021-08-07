"""
String Rotation

Assume you have a method isSubstring which checks if one word is a substring of another. Given two stirngs, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
"""
from collections import deque


# Time: O(n) since checking if a string is a substring of another should run in O(n) time
# Space: O(n)
# If a string is a rotation of another, then it should be a substring of double the other string.
class Solution1:
    def is_rotation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        s2_twice = s2 + s2
        return s1 in s2_twice


# Time: O(n^2)
# Space: O(n)
# Brute-force algorithm
# Check every possible rotation of one string and check if it is equal to the other string
class Solution2:
    def is_rotation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        q1, q2 = deque(s1), deque(s2)
        for _ in range(len(q1)):
            if q1 == q2:
                return True
            q1.append(q1.popleft())
        return False