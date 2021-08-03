"""
Triple Step

A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs. 
"""
from typing import List


# Time: O(n)
# Space: O(n)
# Top-down memoization solution
class Solution1:
    def triple_step(self, n: int) -> int:
        return self._triple_step(n, [0] * (n + 1))

    def _triple_step(self, n: int, memoize: List[int]) -> int:
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif memoize[n] == 0:
            memoize[n] = (
                self._triple_step(n - 1, memoize)
                + self._triple_step(n - 2, memoize)
                + self._triple_step(n - 3, memoize)
            )
        return memoize[n]

    # def triple_step(self, n: int) -> int:
    #     return self._triple_step(n, 0, [0] * (n + 1))

    # def _triple_step(self, n: int, i: int, memoize: list) -> int:
    #     if i == n:
    #         return 1

    #     total = 0
    #     if n - i >= 1:
    #         if memoize[i + 1] == 0:
    #             total += self._triple_step(n, i + 1, memoize)
    #         else:
    #             total += memoize[i + 1]
    #     if n - i >= 2:
    #         if memoize[i + 2] == 0:
    #             total += self._triple_step(n, i + 2, memoize)
    #         else:
    #             total += memoize[i + 2]
    #     if n - i >= 3:
    #         if memoize[i + 3] == 0:
    #             total += self._triple_step(n, i + 3, memoize)
    #         else:
    #             total += memoize[i + 3]
    #     memoize[i] = total
    #     return memoize[i]


# Time: O(3^n)
# Space: O(n)
# Brute-force solution
class Solution2:
    def triple_step(self, n: int) -> int:
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            return (
                self.triple_step(n - 1)
                + self.triple_step(n - 2)
                + self.triple_step(n - 3)
            )

    # def triple_step(self, n: int) -> int:
    #     return self._triple_step(n, 0)

    # def _triple_step(self, n: int, i: int) -> int:
    #     if i == n:
    #         return 1

    #     total = 0
    #     if n - i >= 1:
    #         total += self._triple_step(n, i + 1)
    #     if n - i >= 2:
    #         total += self._triple_step(n, i + 2)
    #     if n - i >= 3:
    #         total += self._triple_step(n, i + 3)
    #     return total
