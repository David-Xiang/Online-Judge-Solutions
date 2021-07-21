# LeetCode 91
# Decode Ways
# Dynamic Programming

from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0] * len(s)
        dp[0] = 1 if self.isOneDigit(s, 0) else 0
        if len(s) == 1:
            return dp[0]
        if self.isOneDigit(s, 0) and self.isOneDigit(s, 1):
            dp[1] = dp[1] + 1
        if self.isTwoDigit(s, 0):
            dp[1] = dp[1] + 1
        
        for i in range(2, len(s)):
            if self.isOneDigit(s, i):
                dp[i] = dp[i] + dp[i - 1]
            if self.isTwoDigit(s, i - 1):
                dp[i] = dp[i] + dp[i - 2]
        return dp[len(s) - 1]

    def isOneDigit(self, s, i):
        return s[i] in "123456789"
    
    def isTwoDigit(self, s, i):
        return s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")

if __name__ == "__main__":
    print(Solution().numDecodings("12"))
    print(Solution().numDecodings("226"))
    print(Solution().numDecodings("0"))
    print(Solution().numDecodings("06"))