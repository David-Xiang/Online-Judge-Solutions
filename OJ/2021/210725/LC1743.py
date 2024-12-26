# LeetCode 1743
# Restore the Array From Adjacent Pairs
# Array

from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs) == 1:
            return adjacentPairs[0]
        adj = dict()
        for [x,y] in adjacentPairs:
            if x not in adj:
                adj[x] = [y]
            else:
                adj[x].append(y)
            if y not in adj:
                adj[y] = [x]
            else:
                adj[y].append(x)
        for k, v in adj.items():
            if len(v) == 1:
                break
        last_num = k
        next_num = adj[k][0]
        ans = [k, next_num]
        while len(adj[next_num]) == 2:
            if adj[next_num][0] == last_num:
                last_num = next_num
                next_num = adj[next_num][1]
                ans.append(next_num)
            else:
                last_num = next_num
                next_num = adj[next_num][0]
                ans.append(next_num)
        return ans
            

if __name__ == "__main__":
    print(Solution().restoreArray([[2,1],[3,4],[3,2]]))
    print(Solution().restoreArray([[4,-2],[1,4],[-3,1]]))
    print(Solution().restoreArray([[100000,-100000]]))