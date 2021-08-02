# LeetCode 743
# Network Delay Time
# Shortest Path

import pytest
from typing import List
import sys

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[sys.maxsize] * n for i in range(n)]
        for src, dst, dis in times:
            adj[src - 1][dst - 1] = dis
        for i in range(n):
            adj[i][i] = 0
        for m in range(n):
            for i in range(n):
                for j in range(n):
                    adj[i][j] = min(adj[i][j], adj[i][m] + adj[m][j])
        ans = 0
        for i in range(n):
            if i == k - 1:
                continue
            if adj[k - 1][i] == sys.maxsize:
                return -1
            ans = max(ans, adj[k - 1][i])
        return ans
    
if __name__ == "__main__":
    assert(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2)
    assert(Solution().networkDelayTime([[1,2,1]], 2, 1) == 1)
    assert(Solution().networkDelayTime([[1,2,1]], 2, 2) == -1)