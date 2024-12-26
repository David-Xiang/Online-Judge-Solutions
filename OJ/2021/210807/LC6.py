# LeetCode 6
# ZigZag Conversion
# String

from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for i in range(numRows)]
        cycle = numRows + numRows - 2
        if cycle == 0:
            return s
        for i in range(len(s)):
            pos = i % cycle
            if pos < numRows:
                res[pos].append(s[i])
            else:
                res[numRows + numRows - pos - 2].append(s[i])
        return "".join(["".join(row) for row in res])


if __name__ == "__main__":
    print(Solution().convert(s = "PAYPALISHIRING", numRows = 3))
    print(Solution().convert(s = "PAYPALISHIRING", numRows = 4))
    print(Solution().convert(s = "A", numRows = 1))