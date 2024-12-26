# LeetCode 118
# Pascal's Triangle
# Dynamic Programming

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            ans.append(ans[i - 1].copy())
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j] + ans[i - 1][j - 1]
            ans[i].append(1)
        return ans

if __name__ == "__main__":
    print(Solution().generate(5))