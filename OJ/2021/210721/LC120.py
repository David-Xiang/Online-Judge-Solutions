# LeetCode 392
# Triangle
# Dynamic Programming

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        dp = triangle[len(triangle) - 1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]

if __name__ == "__main__":
    print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(Solution().minimumTotal([[-10]]))