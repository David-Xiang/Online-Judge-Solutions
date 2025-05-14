#
# @lc app=leetcode id=3337 lang=python3
#
# [3337] Total Characters in String After Transformations II
#

# @lc code=start
from typing import List


class Solution:
    def matmul(self, a, b, mod):
        assert len(a[0]) == len(b)
        m, n, p = len(a), len(a[0]), len(b[0])
        res = [[0 for j in range(p)] for i in range(m)]
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    res[i][j] += (a[i][k] * b[k][j]) % mod
        return res

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        res = 0
        lookup = "abcdefghijklmnopqrstuvwxyz"
        mod = 1000000007
        m = [[0 for j in range(26)] for i in range(26)]
        for i, n in enumerate(nums):
            for j in range(n):
                m[(i + j + 1) % 26][i] = 1
        p = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
        while t != 0:
            if t % 2 == 1:
                p = self.matmul(p, m, mod)
            m = self.matmul(m, m, mod)
            t = t // 2
        count = [[0] for i in range(26)]
        for c in s:
            count[lookup.index(c)][0] += 1
        res = self.matmul(p, count, mod)
        return sum([sum(a) % 1000000007 for a in res]) % 1000000007


# @lc code=end
