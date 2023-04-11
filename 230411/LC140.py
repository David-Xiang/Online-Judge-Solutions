# LeetCode 140
# Word Break II
# Recursion

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        partial: List[List[str]] = [[]]
        for i in range(1, len(s) + 1): # substr [0, i)
            partial.append([])
            for j in range(i):
                if j == 0 and s[:i] in wordDict:
                    partial[i].append(s[:i])
                    continue
                
                if len(partial[j]) > 0 and s[j:i] in wordDict:
                    t = s[j:i]
                    partial[i].extend(arr + ' ' + t for arr in partial[j])

        return partial[len(s)]

    
if __name__ == '__main__':
    print(Solution().wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]))
    print(Solution().wordBreak(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]))
    print(Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))
    print(Solution().wordBreak(s = "a", wordDict = ["a"]))