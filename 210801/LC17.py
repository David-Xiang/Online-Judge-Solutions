# LeetCode 17
# Letter Combinations of a Phone Number
# DFS

from typing import List

class Solution:
    numToChar = dict()
    numToChar["2"] = "abc"
    numToChar["3"] = "def"
    numToChar["4"] = "ghi"
    numToChar["5"] = "jkl"
    numToChar["6"] = "mno"
    numToChar["7"] = "pqrs"
    numToChar["8"] = "tuv"
    numToChar["9"] = "wxyz"

    def letterCombinations(self, digits: str) -> List[str]:
        return self.dfs(digits, 0, ["" for i in range(len(digits))], [])

    def dfs(self, digits, pos, choice, ans):
        if pos == len(digits):
            if pos > 0:
                ans.append("".join(choice))
            return ans
        for c in self.numToChar[digits[pos]]:
            choice[pos] = c
            self.dfs(digits, pos + 1, choice, ans)
        return ans
        
if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
    print(Solution().letterCombinations(""))
    print(Solution().letterCombinations("2"))