# LeetCodeOffer 38 Medium
# Permutation of a String
# DFS, Bachtracing

from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        ans = []
        path = []
        self.dfs(s, path, ans, set())
        return ans        

    def dfs(self, s, path, ans, pos_used):
        if len(path) == len(s):
            ans.append("".join(path))
            return
        pos_not_used = set()
        for i in range(len(s)):
            if i not in pos_used and s[i] not in pos_not_used:
                pos_used.add(i)
                path.append(s[i])
                self.dfs(s, path, ans, pos_used)
                pos_used.remove(i)
                path.pop()
                pos_not_used.add(s[i])



if __name__ == "__main__":
    print(Solution().permutation("121"))