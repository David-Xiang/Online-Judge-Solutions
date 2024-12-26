# LeetCode 329
# Longest Increasing Path in a Matrix
# Dynamic Programming

from typing import List
import collections
import sys
import heapq

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        points = []
        for i in range(m):
            for j in range(n):
                points.append((matrix[i][j], (i, j)))
        points.sort(key = lambda x: x[0], reverse = True)
        lip = [[0] * n for i in range(m)]
        ans = 0
        for p in points:
            val = p[0]
            r, c = p[1]
            ans_pos = 1
            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if nr >= 0 and nr < m and nc >= 0 and nc < n and matrix[r][c] < matrix[nr][nc]:
                    ans_pos = max(lip[nr][nc] + 1, ans_pos)
            lip[r][c] = ans_pos
            ans = max(ans, ans_pos)
        return ans
            

if __name__ == "__main__":
    print(Solution().longestIncreasingPath([[7,8,9],[9,7,6],[7,2,3]]))
    # print(Solution().longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
    # print(Solution().longestIncreasingPath([[1]]))
