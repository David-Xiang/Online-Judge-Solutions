# LeetCode 171
# Excel Sheet Column Number
# Array

from typing import List
import collections
import sys

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        seq = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = 0
        for i in range(len(columnTitle)):
            ans = ans * 26 + seq.index(columnTitle[i])
        return ans
        

if __name__ == "__main__":
    print(Solution().titleToNumber("A"))
    print(Solution().titleToNumber("FXSHRXW"))