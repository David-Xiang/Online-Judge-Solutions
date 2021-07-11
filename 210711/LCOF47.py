# LeetCodeOffer 47
# Max vValue of Gifts
# Dynamic Programming

from typing import List

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        ans = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val = 0
                if i > 0:
                    val = max(val, ans[i-1][j])
                if j > 0:
                    val = max(val, ans[i][j-1])
                ans[i][j] += val + grid[i][j]
        return ans[len(grid)-1][len(grid[0])-1]

if __name__ == "__main__":
    grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    print(Solution().maxValue(grid))