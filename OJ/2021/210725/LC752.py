# LeetCode 752
# Open the Lock
# BFS

from typing import List
import collections

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends or target in deadends:
            return -1
        start = [0, 0, 0, 0]
        q = collections.deque()
        ans = 0
        vis = set()
        q.append(start)
        vis.add("".join([str(i) for i in start]))
        
        while len(q) > 0:
            l = len(q)
            for i in range(l):
                elem = q.popleft()
                password = "".join([str(i) for i in elem])
                if password == target:
                    return ans
                for pos in range(4):
                    for offset in [1, 9]:
                        adj = list(elem)
                        adj[pos] = (adj[pos] + offset) % 10
                        password = "".join([str(i) for i in adj])
                        if password not in vis and password not in deadends:
                            q.append(adj)
                            vis.add(password)
            ans = ans + 1
        return -1
        

if __name__ == "__main__":
    print(Solution().openLock(["0201","0101","0102","1212","2002"], "0202"))
    print(Solution().openLock(["8888"], "0009"))
    print(Solution().openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))
    print(Solution().openLock(["0000"], "8888"))