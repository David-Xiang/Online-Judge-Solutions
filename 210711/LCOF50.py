# LeetCodeOffer 50
# First Unique Character
# Array

from typing import List

class Solution:
    def firstUniqChar(self, s: str) -> str:
        last_index = {}
        ans = len(s) + 1
        for i in range(len(s)):
            c = s[i]
            if c not in last_index:
                last_index[c] = i
            else:
                last_index[c] = -1
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c in last_index and last_index[c] >= 0 and last_index[c] < ans:
                ans = min(ans, last_index[c])
        if ans < len(s):
            return s[ans]
        return " "

if __name__ == "__main__":
    print(Solution().firstUniqChar("abaccdeff"))
    print(Solution().firstUniqChar(""))
    print(Solution().firstUniqChar("leetcode"))