# LeetCode 210
# Course Schedule II
# Topological Sort

from typing import List
import collections
import sys

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0 for i in range(numCourses)]
        for p in prerequisites:
            c, pc = p[0], p[1]
            adj[pc].append(c)
            indegree[c] = indegree[c] + 1

        q = collections.deque()
        ans = []
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        while len(q) > 0:
            c = q.popleft()
            ans.append(c)
            for nc in adj[c]:
                indegree[nc] = indegree[nc] - 1
                if indegree[nc] == 0:
                    q.append(nc)
        if len(ans) == numCourses:
            return ans
        return []


if __name__ == "__main__":
    print(Solution().findOrder(2, [[1, 0]]))
    print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(Solution().findOrder(1, []))