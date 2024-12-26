# LeetCode 847
# Shortest Path Visiting All Nodes
# BFS

from typing import List
import sys

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        import collections
        q = collections.deque()
        node_num = len(graph)
        if node_num < 2:
            return 0
        visited = set()
        for i in range(node_num):
            state = 1 << i # 表示访问过的点仅i
            q.append((i, state))
            visited.add((i, state))
        step = 1
        end_state = (1 << (node_num)) - 1
        while len(q) > 0:
            len_state = len(q)
            for i in range(len_state):
                pos, state = q.popleft()
                for new_pos in graph[pos]:
                    new_state = state | 1 << new_pos
                    if new_state == end_state:
                        return step
                    if (new_pos, new_state) not in visited:
                        q.append((new_pos, new_state))
                        visited.add((new_pos, new_state))
            step = step + 1
        
if __name__ == "__main__":
    print(Solution().shortestPathLength([[1,2,3],[0],[0],[0]]))
    print(Solution().shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))