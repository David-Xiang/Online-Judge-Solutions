# LeetCode 96
# Unique Binary Search Trees
# Dynamic Programming

from typing import List

class Solution:
    def numTrees(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n + 1):
            for left in range(0, i):
                dp[i] = dp[i] + dp[left] * dp[i - left - 1]
        return dp[n]

if __name__ == "__main__":
    print(Solution().numTrees(1))
    print(Solution().numTrees(2))
    print(Solution().numTrees(3))
    