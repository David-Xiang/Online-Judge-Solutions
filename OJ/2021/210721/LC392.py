# LeetCode 392
# Is Subsequence
# Dynamic Programming

from typing import List

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        if ls == 0:
            return True
        if lt == 0:
            return False
        dp = [[False] * (lt + 1) for i in range(ls + 1)]
        dp[0] = [True] * (lt + 1)
        for i in range(1, ls + 1):
            for j in range(1, lt + 1):
                dp[i][j] = dp[i][j - 1]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - 1]
        return dp[ls][lt]

if __name__ == "__main__":
    print(Solution().isSubsequence("abc", "ahbgdc"))
    print(Solution().isSubsequence("axc", "ahbgdc"))
    print(Solution().isSubsequence("b", "c"))
    print(Solution().isSubsequence("b", "abc"))
    print(Solution().isSubsequence("", "abc"))