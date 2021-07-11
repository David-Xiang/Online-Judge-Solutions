# LeetCodeOffer 48
# Longest Substring without Repeating Characters
# Dynamic Programming

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return length
        
        dp = [1] * length
        last_index = {s[0]: 0}
        ans = 1
        for i in range(1, length):
            c = s[i]
            if c not in last_index or last_index[c] < i - dp[i - 1]:
                dp[i] += dp[i-1]
            else:
                dp[i] += i - last_index[c] - 1
            last_index[c] = i
            ans = max(ans, dp[i])
        return ans

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring("dvdf"))