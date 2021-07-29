# LeetCode 200
# Number Of Islands
# Union Find

from typing import List
import collections
import sys

class Solution:
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [-1] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    f[i * n + j] = i * n + j
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    for d in self.dirs:
                        x, y = i + d[0], j + d[1]
                        if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == "1":
                            self.union(f, i * n + j, x * n + y)
        count = 0
        for i in range(m):
            for j in range(n):
                    if f[i * n + j] == i * n + j:
                        count = count + 1
        return count

    def union(self, f, m, n):
        fm = self.find(f, m)
        fn = self.find(f, n)
        if fm != fn:
            f[fm] = fn
    
    def find(self, f, m):
        if f[m] != m:
            f[m] = self.find(f, f[m])
        return f[m]
        


if __name__ == "__main__":
    print(Solution().numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]))
    print(Solution().numIslands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]))