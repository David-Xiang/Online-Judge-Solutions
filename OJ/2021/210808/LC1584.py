# LeetCode 1584
# Min Cost to Connect All Points
# Minimum Spanning Tree

from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        nums = len(points)
        if nums == 1:
            return 0
        elif nums == 2:
            return self.dis(points[0], points[1])
        edges = []
        from heapq import heappush, heappop
        for i in range(nums - 1):
            for j in range(i + 1, nums):
                heappush(edges, (self.dis(points[i], points[j]), i, j))
        fa = [i for i in range(nums)]
        ans = 0
        count = 0
        while count < nums - 1:
            while len(edges) > 0:
                cost, i, j = heappop(edges)
                if self.find(fa, i) != self.find(fa, j):
                    break
            ans = ans + cost
            self.union(fa, i, j)
            count = count + 1
        return ans

    def find(self, fa, i):
        if fa[i] != i:
            fa[i] = self.find(fa, fa[i])
        return fa[i]

    def union(self, fa, i, j):
        fi = self.find(fa, i)
        fj = self.find(fa, j)
        fa[fi] = fj

    def dis(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        

if __name__ == "__main__":
    print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
    print(Solution().minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
    print(Solution().minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]]))
    print(Solution().minCostConnectPoints([[-1000000,-1000000],[1000000,1000000]]))
    print(Solution().minCostConnectPoints([[0,0]]))