# LeetCode 14
# Longest Common Prefix
# String

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(s) for s in strs])
        for i in range(min_len):
            c = strs[0][i]
            for j in range(0, len(strs)):
                if strs[j][i] != c:
                    return strs[0][:i]
        return strs[0][:min_len]
        

if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))
    