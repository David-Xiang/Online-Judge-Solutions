# LeetCode 207
# Course Schedule
# Topological Sort

from typing import List
import collections
import sys

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depends = dict()
        for c, prereq in prerequisites:
            if c not in depends:
                depends[c] = [prereq]
            else:
                depends[c].append(prereq)
        taken = set()
        while len(taken) < numCourses:
            found = False
            for course in range(numCourses):
                if course in taken:
                    continue
                if course not in depends:
                    found = True
                    taken.add(course)
                    continue
                all_prereq_taken = True
                for prereq in depends[course]:
                    if prereq not in taken:
                        all_prereq_taken = False
                        break
                if all_prereq_taken:
                    found = True
                    taken.add(course)
            if not found:
                return False
        return True
    

    def canFinishBFS(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for c, d in prerequisites:
            adj[d].append(c)
            indegree[c] = indegree[c] + 1
        q = collections.deque()
        taken = set()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
                taken.add(c)
        count = 0
        
        while len(q) > 0:
            c = q.popleft()
            for nc in adj[c]:
                indegree[nc] = indegree[nc] - 1
                if indegree[nc] == 0 and nc not in taken:
                    q.append(nc)
                    taken.add(nc)
            count = count + 1
        return count == numCourses

if __name__ == "__main__":
    print(Solution().canFinishBFS(3, [[0,1],[0,2],[1,0]]))
    print(Solution().canFinishBFS(2, [[1,0],[0,1]]))
    print(Solution().canFinishBFS(5, [[1,4],[2,4],[3,1],[3,2]]))