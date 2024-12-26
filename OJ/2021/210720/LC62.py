# LeetCode 62
# Unique Paths
# Dynamic Programming

from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    grid[i][j] = 1
                elif j == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]

if __name__ == "__main__":
    print(Solution().uniquePaths(3, 7))
    print(Solution().uniquePaths(3, 2))