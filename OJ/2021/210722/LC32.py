# LeetCode 32
# Longest Valid Parentheses
# Dynamic Programming

from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        dp = [0] * len(s)
        dp[0], dp[1] = 0, 2 if s[0:2] == "()" else 0
        for i in range(2, len(s)):
            if s[i] == "(": # ...(
                dp[i] = 0
            elif s[i - 1] == "(": # ...()
                dp[i] = dp[i - 2] + 2
            elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":  # ..((...))
                dp[i] = dp[i - 1] + 2
                if i - dp[i - 1] - 2 >= 0:
                    dp[i] = dp[i] + dp[i - dp[i - 1] - 2]
        return max(dp)

if __name__ == "__main__":
    print(Solution().longestValidParentheses("(()"))
    print(Solution().longestValidParentheses(")()())"))
    print(Solution().longestValidParentheses(""))
    print(Solution().longestValidParentheses("(()))()"))