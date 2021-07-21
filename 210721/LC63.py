# LeetCode 63
# Unique Paths II
# Dynamic Programming

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for i in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if self.isValid(i, j - 1, obstacleGrid):
                    dp[i][j] = dp[i][j] + dp[i][j - 1]
                if self.isValid(i - 1, j, obstacleGrid):
                    dp[i][j] = dp[i][j] + dp[i - 1][j]
        return dp[n - 1][m - 1] if obstacleGrid[n - 1][m - 1] == 0 else 0

    def isValid(self, i, j, obstacleGrid):
        return i >= 0 and j >= 0 and obstacleGrid[i][j] == 0


    

if __name__ == "__main__":
    print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print(Solution().uniquePathsWithObstacles([[0,1],[0,0]]))