# LeetCode 64
# Minimum Path Sum
# Dynamic Programming

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cost = [[0] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    cost[i][j] = grid[i][j]
                elif i == 0:
                    cost[i][j] = cost[i][j - 1] + grid[i][j]
                elif j == 0:
                    cost[i][j] = cost[i - 1][j] + grid[i][j]
                else:
                    cost[i][j] = min(cost[i - 1][j], cost[i][j - 1]) + grid[i][j]
        return cost[len(grid) - 1][len(grid[0]) - 1]

if __name__ == "__main__":
    print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(Solution().minPathSum([[1,2,3],[4,5,6]]))