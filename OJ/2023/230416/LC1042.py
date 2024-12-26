
import collections
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        novisit = set([i for i in range(n)])
        adj = [[] for i in range(n)]
        ans = [0] * n

        for path in paths:
            a, b = path[0] - 1, path[1] - 1
            adj[a].append(b)
            adj[b].append(a)

        count = 0
        q = collections.deque()
        while count < n:
            q.append(novisit.pop())
            while len(q) > 0:
                node = q.popleft()
                adj_ans = [ans[i] for i in adj[node]]
                for i in range(1, 5):
                    if i not in adj_ans:
                        ans[node] = i
                        break
                for i in adj[node]:
                    if i in novisit:
                        q.append(i)
                        novisit.remove(i)
                count = count + 1
        return ans


if __name__ == "__main__":
    print(Solution().gardenNoAdj(n=3, paths=[[1, 2], [2, 3], [3, 1]]))
    print(Solution().gardenNoAdj(n=4, paths=[[1, 2], [3, 4]]))
    print(Solution().gardenNoAdj(n=4, paths=[
          [1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]))
    print(Solution().gardenNoAdj(n=10000, paths=[]))
